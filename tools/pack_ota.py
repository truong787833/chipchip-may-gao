"""
ChipChip May & Gao - Ultra-Fast OTA Packager (Cong cu Dong Goi OTA Sieu Toc)
Tac gia: Phung Hai Truong
Chuc nang:
- Dong goi index.html, version.json va assets thanh goi cap nhat OTA sieu nhe (~200KB - 500KB).
- Xuat file latest_ota_package.zip va update_v{version}.zip san sang phat hanh.
- Tu dong dong bo sang chipchip_mobile/assets/web/ de chay dong bo.
"""

import os
import sys
import json
import zipfile
import shutil
import argparse
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION_FILE = os.path.join(ROOT_DIR, "version.json")
OUTPUT_DIR = os.path.join(ROOT_DIR, "dist_ota")
FLUTTER_WEB_ASSETS = os.path.abspath(os.path.join(ROOT_DIR, "..", "chipchip_mobile", "assets", "web"))


def load_version():
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "version": "1.0.1",
        "build_number": 101,
        "release_date": datetime.now().strftime("%Y-%m-%d"),
        "channel": "stable",
        "app_name": "ChipChip Mây & Gạo",
        "latest_version": "1.0.1",
        "latest_build": 101,
        "has_update": False,
        "changelog": []
    }


def save_version(data):
    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def pack_ota(bump=None, custom_version=None, changelog_msg=None):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ver_data = load_version()

    old_ver = ver_data.get("version", "1.0.1")
    old_build = int(ver_data.get("build_number", 101))

    if custom_version:
        new_ver = custom_version
        new_build = old_build + 1
    elif bump == "patch":
        parts = old_ver.split(".")
        parts[-1] = str(int(parts[-1]) + 1)
        new_ver = ".".join(parts)
        new_build = old_build + 1
    elif bump == "minor":
        parts = old_ver.split(".")
        parts[1] = str(int(parts[1]) + 1)
        parts[2] = "0"
        new_ver = ".".join(parts)
        new_build = old_build + 10
    else:
        new_ver = old_ver
        new_build = old_build

    ver_data["version"] = new_ver
    ver_data["latest_version"] = new_ver
    ver_data["build_number"] = new_build
    ver_data["latest_build"] = new_build
    ver_data["release_date"] = datetime.now().strftime("%Y-%m-%d")
    ver_data["has_update"] = False

    if changelog_msg:
        if "changelog" not in ver_data:
            ver_data["changelog"] = []
        ver_data["changelog"].insert(0, changelog_msg)

    save_version(ver_data)

    # Dong bo sang thu muc assets cua Flutter
    if os.path.exists(FLUTTER_WEB_ASSETS):
        shutil.copy2(VERSION_FILE, os.path.join(FLUTTER_WEB_ASSETS, "version.json"))
        index_src = os.path.join(ROOT_DIR, "index.html")
        if os.path.exists(index_src):
            shutil.copy2(index_src, os.path.join(FLUTTER_WEB_ASSETS, "index.html"))

    latest_zip_path = os.path.join(OUTPUT_DIR, "latest_ota_package.zip")
    versioned_zip_path = os.path.join(OUTPUT_DIR, f"update_v{new_ver}.zip")

    print("=" * 60)
    print("   CHIPCHIP MÂY & GẠO - ĐÓNG GÓI BẢN VÁ OTA SIÊU TỐC")
    print(f"   Phiên bản: v{new_ver} (Build {new_build})")
    print("=" * 60)

    # Cac file & thu muc can dong goi vao OTA
    include_targets = [
        ("index.html", os.path.join(ROOT_DIR, "index.html")),
        ("version.json", VERSION_FILE),
        ("assets", os.path.join(ROOT_DIR, "assets")),
    ]

    temp_zip = os.path.join(OUTPUT_DIR, "_packing_temp.zip")
    if os.path.exists(temp_zip):
        os.remove(temp_zip)

    packed_files = 0
    with zipfile.ZipFile(temp_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for arc_base, real_path in include_targets:
            if not os.path.exists(real_path):
                continue
            if os.path.isfile(real_path):
                zf.write(real_path, arc_base)
                packed_files += 1
            else:
                for root, dirs, files in os.walk(real_path):
                    for f in files:
                        if f.endswith(".tmp") or f.endswith(".bak"):
                            continue
                        full_f = os.path.join(root, f)
                        rel_f = os.path.relpath(full_f, ROOT_DIR)
                        zf.write(full_f, rel_f)
                        packed_files += 1

    shutil.copy2(temp_zip, latest_zip_path)
    shutil.copy2(temp_zip, versioned_zip_path)
    os.remove(temp_zip)

    size_kb = os.path.getsize(latest_zip_path) / 1024

    print(f"\n[+] Đã đóng gói thành công {packed_files} tệp tin!")
    print(f"[+] Kích thước gói OTA: {size_kb:.1f} KB - CỰC KỲ SIÊU NHẸ (Tải & nạp trong 1 giây)!")
    print(f"[+] Tệp 1 (phát hành chung): {latest_zip_path}")
    print(f"[+] Tệp 2 (theo phiên bản): {versioned_zip_path}")
    print("=" * 60)
    print("Xong! Người dùng chỉ cần gửi file này hoặc nạp qua giao diện app để cập nhật ngay lập tức.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dong goi OTA ChipChip May & Gao")
    parser.add_argument("--bump", choices=["patch", "minor"], help="Tang phien ban patch hoac minor")
    parser.add_argument("--version", dest="custom_version", help="Chi dinh phien ban cu the")
    parser.add_argument("--msg", dest="changelog_msg", help="Noi dung changelog")
    args = parser.parse_args()

    pack_ota(bump=args.bump, custom_version=args.custom_version, changelog_msg=args.changelog_msg)
