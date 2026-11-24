@echo off
chcp 65001 >nul
title ChipChip Mây & Gạo - Đóng Gói Bản Vá Cập Nhật OTA Siêu Tốc
cd /d "%~dp0"

echo ================================================================
echo    CHIPCHIP MÂY & GẠO - ĐÓNG GÓI BẢN VÁ OTA SIÊU TỐC CHO APP
echo    Phát triển bởi: Phùng Hải Trường
echo ================================================================
echo.

python tools\pack_ota.py %*

echo.
echo Gói OTA đã được tạo trong thư mục dist_ota\
echo Bấm phím bất kỳ để mở thư mục chứa gói OTA...
pause >nul
explorer dist_ota
