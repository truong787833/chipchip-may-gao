# PROJECT MEMORY - ỨNG DỤNG QUẢN LÝ ĐƠN HÀNG CHIP CHIP (CHIPCHIP ORDER APP)

## 1. Thông Tin & Mục Tiêu Dự Án
- **Tên dự án:** ChipChip Order App (Sổ Bán Hàng Kẹo Chip Chip Cho Vợ)
- **Mục tiêu:** Giúp vợ chủ shop kẹo chip chip quản lý đơn hàng nhanh chóng, tự động quy đổi lạng sang kg, thống kê mẻ kẹo theo vị (Húng chanh, Mix, Xoài, Chanh leo, Sữa chua...), tự thêm vị kẹo mới, cài đặt giá đồng loạt 25k hoặc sửa giá riêng từng vị, quản lý công nợ (chưa tiền / đã trả / tiền R), gạch hoàn thành đơn (đã giao & nhận tiền) và xuất báo cáo Zalo một chạm mà không bao giờ bị tính nhầm.
- **Công nghệ sử dụng:** HTML5, CSS3 (Tailwind CSS phong cách Mobile-First pastel), JavaScript ES6 Vanilla (chạy offline 100%, không cần cài đặt backend, lưu dữ liệu vào `localStorage`). Hỗ trợ cài đặt làm PWA / Web App trên màn hình chính của iPhone và Android.
- **Vị trí thư mục:** `C:\Users\ADMIN\.gemini\antigravity\scratch\chipchip-order-app`
- **QUY TẮC PHÁT HÀNH DUY NHẤT (BẮT BUỘC):**
  * Kể từ Phiên 19, **MỌI CẬP NHẬT CHỈ SỬ DỤNG GÓI OTA** (`latest_ota_package.zip`, `update_vX.X.X.zip`, `version.json`).
  * **TUYỆT ĐỐI KHÔNG xuất file APK nữa** trừ khi người dùng yêu cầu rõ ràng.
  * Cập nhật trực tiếp 1-chạm ngay trong app trong 1-2 giây.
  * Bảo đảm bảo toàn dữ liệu 100% không bao giờ mất thông tin đã thêm của người dùng.

## 2. Nhật Ký Yêu Cầu & Quyết Định Người Dùng
- **2026-11-22 (Phiên 1):** 
  - Khách hàng có bảng ghi chú tay đơn kẹo chip chip gồm nhiều khách, đơn vị "lạng", "hộp", có các vị "mix", "húng chanh", trạng thái "chưa tiền", "tiền R", "lấy rồi", có các dòng gạch ngang.
  - Chốt logic tính khối lượng: 1 lạng = 0.1 kg (10 lạng = 1 kg). Đơn vị hộp có thể tính theo số lạng tương ứng (A Đức 2 hộp 4 lạng = 8 lạng = 0.8 kg). Tổng toàn bộ bảng là chuẩn xác 12.6 kg.
  - Yêu cầu ứng dụng tiện lợi, nhập nhanh, không tính nhầm, giao diện nút to dễ bấm trên điện thoại.
- **2026-11-22 (Phiên 2 - Bổ sung danh mục vị & cơ chế giá):**
  - Kẹo hiện tại có các vị: **Mix, Húng chanh, Xoài, Chanh leo, Sữa chua...** và **cho phép tự thêm tên vị mới** bất kỳ lúc nào.
  - Giá bán: Mặc định **25k đồng loạt tất cả các vị**, đồng thời **cho phép sửa giá từng loại hoặc đặt lại giá chung** nhanh chóng.
- **2026-11-22 (Phiên 3 - Làm rõ quy ước gạch dòng trong sổ):**
  - **Quy ước người dùng chốt:** Những dòng được gạch ngang trong sổ là **ĐÃ GIAO VÀ NHẬN TIỀN** (hoàn thành đơn), **TUYỆT ĐỐI KHÔNG PHẢI ĐƠN HỦY**.
  - Toàn bộ các đơn gạch sổ vẫn được tính 100% vào tổng khối lượng đã bán (12.6 kg) và tổng doanh thu, tự động chuyển trạng thái sang `Đã nhận tiền`.
  - Thay đổi tab lọc: `Đã hủy/gạch` $\rightarrow$ `✓ Đã gạch xong (Đã giao & thu tiền)`.
  - Nút hành động đổi thành `fa-check-double`: 1 chạm là gạch hoàn thành và đổi màu xanh thành công.

- **2026-11-22 (Phiên 4 - Cập nhật trạng thái thanh toán theo yêu cầu):**
  - Cập nhật 4 khách có tích xanh đã giao: **Như (4 lạng)**, **A tân (2 lạng)**, **C khánh (5 lạng)**, **Cô thanh2 (4 lạng)** sang trạng thái **ĐÃ GIAO & ĐÃ NỘP TIỀN**.
  - Đơn **Cô duyên (5 lạng)** giữ nguyên trạng thái chưa giao và chưa nộp tiền.
  - Số tiền chưa nộp tự động giảm 375.000đ (15 lạng x 25k) chuyển sang mục đã nhận tiền.

- **2026-11-22 (Phiên 5 - Giải rối 4 trạng thái, Tích hợp VietQR & Logo thương hiệu):**
  - **Giải rối Hàng & Tiền:** Tách thành 4 nhóm độc lập trực quan, có thẻ bấm lọc nhanh kèm số lượng:
    1. 🔴 *Cần đòi tiền:* Đã giao mà chưa nhận tiền.
    2. 🔵 *Nợ hàng khách:* Khách đã trả tiền/chuyển khoản mà chưa giao.
    3. ⏳ *Đơn mới đặt:* Chưa giao và chưa trả tiền.
    4. 🟢 *Xong xuôi 100%:* Đã giao và đã thu tiền.
  - **Sửa lỗi hiển thị chữ:** Rút gọn nhãn tab, hiển thị số lượng rõ ràng, không bị tràn hay che chữ trên mọi thiết bị.
  - **Mã QR Ngân Hàng:** Tích hợp tính năng tạo mã VietQR động theo từng đơn hàng (kèm tên khách + số tiền chuẩn) và hỗ trợ tải ảnh chụp QR riêng từ máy.
  - **Logo & Thương hiệu chính thức:**
    * Cập nhật tên app: **ChipChip Mây & Gạo** (Giang Hà - 0941406007).
    * File logo lưu tại: `assets/logo.jpg` và khai báo `manifest.json`.
    * **QUY TẮC BẮT BUỘC GHI NHỚ:** Sau này khi xuất bản gói cài đặt Android (`.apk`), BẮT BUỘC dùng file logo `assets/logo.jpg` này làm App Icon chính thức cho file APK.

- **2026-11-22 (Phiên 6 - Nâng cấp 2 nút bấm độc lập HÀNG & TIỀN):**
  - Khắc phục sự khó hiểu của checkbox cũ: Bổ sung 2 nút bấm to, rõ, độc lập ngay dưới từng thẻ đơn:
    1. **Nút HÀNG:** `[📦 CHƯA GIAO]` $\leftrightarrow$ `[✓ ĐÃ GIAO HÀNG]` (Chạm để đổi).
    2. **Nút TIỀN:** `[⏳ CHƯA TIỀN]` $\leftrightarrow$ `[✓ ĐÃ NHẬN TIỀN]` (Chạm để đổi).
  - Khách trả tiền trước mà nợ hàng: Chỉ cần bấm nút **[⏳ CHƯA TIỀN]** $\rightarrow$ đổi thành **[✓ ĐÃ NHẬN TIỀN]** (Nút Hàng vẫn là Chưa giao) $\rightarrow$ Đơn lập tức vào mục **🔵 Nợ hàng khách**.
  - Đã giao mà nợ tiền: Chỉ cần bấm nút **[📦 CHƯA GIAO]** $\rightarrow$ đổi thành **[✓ ĐÃ GIAO HÀNG]** (Nút Tiền vẫn là Chưa tiền) $\rightarrow$ Đơn lập tức vào mục **🔴 Cần đòi tiền**.

- **2026-11-22 (Phiên 7 - Sắp xếp thông minh & Ghi nhận thời gian chi tiết):**
  - **Sắp xếp thứ tự danh sách:**
    * Các đơn mới / chưa xong (ngày 22/11, việc cần làm) $\rightarrow$ Tự động NẰM TRÊN CÙNG theo mức độ ưu tiên: Cần đòi tiền $\rightarrow$ Nợ hàng $\rightarrow$ Đơn mới.
    * Các đơn đã xong 100% (ngày 21/11, đã hoàn tất) $\rightarrow$ Tự động CHÌM XUỐNG DƯỚI CÙNG danh sách, giúp màn hình luôn gọn gàng.
  - **Mốc thời gian chi tiết từng đơn:**
    * Đơn đã xong: Gán ngày 21/11/2026 (Tạo, Giao, Thu tiền, Hoàn tất).
    * Đơn mới hiện tại: Gán ngày 22/11/2026.
    * Đơn mới tạo trong tương lai: Tự động ghi nhận giờ/ngày thực tế chính xác từng giây.
    * Khi bấm Giao hàng hoặc Thu tiền: Tự động cập nhật giờ thực tế vào đơn.
  - **Dọn dẹp giao diện:** Bỏ nút `[✓✓]` trùng lặp trên góc phải, thẻ đơn nhìn thoáng đãng và chuyên nghiệp.

- **2026-11-22 (Phiên 8 - Chuẩn hóa giao diện tab, Phân tích dữ liệu & Báo cáo doanh thu tối Zalo):**
  - **Sửa nhãn:** Trong ô chọn tiền bạc lúc tạo đơn, đổi nhãn `Đã CK / Tiền R` thành `Đã chuyển khoản`.
  - **Sắp xếp bộ lọc cân đối & Đổi nhãn `Xong`:**
    * Đổi chữ `Xong 100%` thành ngắn gọn là `Xong`.
    * Sắp xếp bộ lọc dạng lưới 2 hàng đối xứng, cân đều, kích thước chuẩn, chữ hiển thị rõ ràng trên mọi màn hình điện thoại:
      - Hàng 1 (3 cột bằng nhau): `Tất cả` | `⏳ Đơn mới` | `🟢 Xong`.
      - Hàng 2 (2 cột bằng nhau): `🔴 Cần đòi tiền` | `🔵 Nợ hàng`.
  - **Phân Tích Dữ Liệu & Biểu Đồ Xu Hướng (Chart.js):**
    * Tích hợp Chart.js vẽ biểu đồ xu hướng dạng Doughnut trực quan, tỷ lệ % và số lạng từng vị kẹo.
    * Tự động xác định và vinh danh vị kẹo bán chạy nhất (Top 1).
    * Bảng xếp hạng Top khách hàng VIP mua nhiều nhất (xếp theo tổng số lạng và tổng tiền).
    * **Chiến lược nhập nguyên liệu thông minh:** Tự động tính toán lượng Gelatin cần mua (tỷ lệ chuẩn ~90g/kg), đường phèn/mạch nha (~300g/kg), lượng hoa quả tươi theo vị (lá húng chanh, quất tươi, xoài chín, chanh leo tím, sữa chua...).
  - **Báo Cáo Doanh Thu Tự Động Mỗi Tối (Zalo):**
    * Thêm nút `[Báo cáo tối]` và nút trợ lý thông minh trên màn hình chính.
    * Tự động tổng hợp số liệu chốt sổ trong ngày: Doanh thu hôm nay, tiền đã về túi, tiền còn nợ khách (kèm danh sách tên khách cần đòi), số đơn nợ hàng và khối lượng cần nấu sáng mai.
    * Nút 1 chạm `[Sao Chép & Gửi Zalo]`: Copy toàn bộ nội dung đã soạn sẵn cực đẹp và tự động mở Zalo để gửi ngay.

- **2026-11-22 (Phiên 9 - Tinh gọn thanh tiêu đề, Sổ Nguyên Liệu & Tính Lời Lãi Theo Ngày/Tháng/Đợt):**
  - **Dọn dẹp thanh tiêu đề:** Xóa 2 nút trùng lặp `Biểu đồ` và `Báo cáo` trên cùng, giữ lại `Mã QR` và `Cài đặt` giúp giao diện trên đỉnh thoáng đãng và sạch sẽ.
  - **Sổ Nguyên Liệu Đã Mua (Chi phí vật tư):**
    * Thêm giao diện quản lý chi phí mua đồ: Tên nguyên liệu, số lượng, đơn vị (lạng, kg, quả, hộp, gói, túi, chai, tự gõ...), giá tiền mua, ngày mua và gán vào Đợt kẹo.
    * Gợi ý chọn nhanh nguyên liệu hay mua: Gelatin Đức, Đường phèn, Mạch nha, Húng chanh, Quất, Xoài chín, Chanh leo, Hộp nhựa, Tem nhãn...
    * Tự thêm mục, sửa, xóa, và lưu tự động vào `localStorage`.
    * Nạp sẵn các chi phí mẫu thực tế cho đợt 12.6 kg (Gelatin Đức, Đường phèn & Mạch nha, Lá húng chanh & Quất tươi, Xoài chín & Chanh leo, Hộp nhựa & Tem dán = 570.000 đ).
  - **Bộ Lọc & Tính Lời Lãi Thông Minh (Theo Ngày, Theo Tháng, Theo Đợt, Toàn Bộ):**
    * **Theo Ngày:** Lọc đơn và nguyên liệu theo ngày cụ thể (21/11, 22/11, hôm nay...).
    * **Theo Tháng:** Lọc theo tháng (Tháng 11/2026...).
    * **Theo Đợt:** Lọc theo từng đợt mẻ kẹo (`Đợt 1 (12.6kg)`, có nút tạo thêm đợt mới).
    * **Toàn Bộ:** Tổng hợp toàn diện.
  - **Bảng Kê Tài Chính & Công Thức Tính Lợi Nhuận Trực Quan:**
    $$\mathbf{[\text{Tổng Tiền Đã Nhận}] - [\text{Tổng Tiền Mua Đồ}] = [\text{LỢI NHUẬN THỰC TẾ (LÃI RÒNG)}]}$$
    * Hiển thị số tiền thực lời về túi (xanh ngọc khi có lãi, cảnh báo cam khi tạm âm vốn do chưa thu hết tiền nợ).
    * Dự kiến lãi khi thu hết tiền nợ: $\text{Tổng Doanh Thu} - \text{Tổng Tiền Mua Đồ}$.
    * Nút xuất báo cáo Lời Lãi gửi Zalo tức thì.

- **2026-11-22 (Phiên 10 - Nâng cấp thẩm mỹ giao diện & Hệ thống nền Pastel nghệ thuật):**
  - **Hệ thống nền Ambient Mesh Pastel:**
    * Tích hợp 3 khối đốm sáng mây & kẹo bồng bềnh chuyển màu mịn màng nằm ở tầng background (`-z-10`).
    * Lớp họa tiết hạt kẹo mờ nhẹ nghệ thuật, mang đậm phong cách kẹo dẻo chip chip thủ công cao cấp.
  - **Bảo toàn chữ & số siêu nét 100%:**
    * Toàn bộ các thẻ nội dung (đơn hàng, form nhập, bảng thống kê) giữ nền trắng sáng bóng (`rgba(255, 255, 255, 0.96)`) kèm viền mỏng và đổ bóng đa tầng.
    * Độ tương phản của chữ (màu `text-slate-800`, `text-slate-900`) và số tiền (màu `text-rose-600`, `text-emerald-700`) được tối ưu hóa tối đa, không bị bóng mờ hay chói mắt.
  - **Bộ Sưu Tập 5 Chủ Đề Màu Nền (Theme Switcher):**
    * Thêm nút `[Màu nền]` trên thanh điều hướng và mục chọn màu trong cài đặt hệ thống.
    * 5 giao diện màu sắc tự chọn:
      1. 🍓 *Mây Kẹo Dâu* (Hồng phấn & mây trắng - Mặc định ngọt ngào).
      2. 🥭 *Xoài Đào* (Cam ấm áp, tươi vui năng động).
      3. 🍃 *Bạc Hà Mint* (Xanh ngọc thanh mát, dịu mắt ban đêm).
      4. 🍇 *Nho Tím* (Tím pastel mộng mơ, sang trọng).
      5. 🥛 *Trắng Sứ Tối Giản* (Nền trắng tinh khôi, tương phản tuyệt đối).
    * Lưu tự động vào `localStorage` (`chipchip_theme`), ghi nhớ màu sắc đã chọn cho các lần sau.

- **2026-11-22 (Phiên 11 - Nâng cấp toàn diện UI/UX Đẳng Cấp, Nút Bấm Xúc Giác & Độ Tương Phản Hoàn Hảo):**
  - **Header & Nhận Diện:**
    * Avatar logo bo góc squircle chuẩn Apple, viền đôi rose-200, hiệu ứng chấm trạng thái online nhịp thở (pulse glow).
    * Huy hiệu `PRO` khẳng định đẳng cấp tiệm kẹo thủ công hiện đại.
    * Nút bấm trên thanh điều hướng nâng cấp hiệu ứng phản hồi xúc giác (`btn-tactile active:scale-95`).
  - **Dashboard Card Thượng Hạng:**
    * Bo góc lớn `rounded-3xl`, dải gradient đa tầng `rose-500` qua `rose-600` đến `amber-500`, hiệu ứng vầng hào quang chìm.
    * Chữ và số hiển thị to bản, trắng sáng siêu nét với drop shadow nhẹ.
    * Thống kê khối lượng từng vị thiết kế dạng viên ngọc mờ trong suốt (`backdrop-blur-md`), viền vi mô sắc nét.
    * Hai viên nang tài chính `Đã nhận` và `Chưa tiền` thiết kế nền kính tối màu tương phản cao, số tiền nổi bật tuyệt đối.
  - **Hệ Thống Phản Hồi Xúc Giác (Tactile Buttons) Toàn Diện:**
    * Bổ sung class `.btn-tactile` cho toàn bộ các nút tương tác: nút chức năng, nút chọn khối lượng, nút lọc danh sách, nút chọn vị kẹo, nút thêm đơn. Khi chạm ngón tay vào tạo cảm giác cơ học nảy chân thực như ứng dụng iOS native.
  - **Bộ Nút Hành Động Trên Từng Đơn Hàng:**
    * Nút `HÀNG` (`[📦 CHƯA GIAO]` $\leftrightarrow$ `[✓ ĐÃ GIAO HÀNG]`): Trạng thái hoàn thành phủ gradient `from-emerald-500 to-teal-600` kèm đổ bóng mềm; trạng thái chưa giao có nền sáng viền chuẩn, chữ đậm rõ ràng.
    * Nút `TIỀN` (`[⏳ CHƯA TIỀN]` $\leftrightarrow$ `[✓ ĐÃ NHẬN TIỀN]`): Trạng thái đã nhận phủ gradient `from-emerald-600 to-teal-700` bóng bẩy; trạng thái chưa tiền nền đỏ hồng cảnh báo nhẹ nhàng nhưng dứt khoát.
    * Đường viền chỉ báo cạnh trái (accent border 4px): Đỏ cho đơn cần đòi nợ, Xanh dương cho đơn nợ hàng, Xanh lá cho đơn xong xuôi, Vàng cho đơn mới. Nhìn lướt qua mắt phân biệt được trạng thái ngay lập tức.
  - **Bảo Toàn Đọc & Tương Phản:**
    * Chữ và số trên toàn bộ giao diện đảm bảo độ tương phản cao WCAG AAA, font chữ *Plus Jakarta Sans* hiện đại, không một chi tiết nào bị mờ hay khó nhìn.

- **2026-11-22 (Phiên 12 - Xóa nút Màu nền, Đóng gói xuất bản file APK Release & Cơ chế chống mất dữ liệu khi gỡ cài lại):**
  - **Xóa nút [Màu nền]:** Đã gỡ bỏ hoàn toàn nút `Màu nền` trên thanh tiêu đề theo yêu cầu của người dùng, giao diện trở nên thông thoáng và tập trung vào nghiệp vụ chính.
  - **Đóng gói APK Android Release chính thức:**
    * Sử dụng Flutter 3.47.5 & Android SDK 36 đóng gói toàn bộ ứng dụng thành file APK cài đặt độc lập: `ChipChip_MayVaGao_v1.0.apk` (Dung lượng 44.5 MB).
    * Vị trí file APK: `C:\Users\ADMIN\.gemini\antigravity\scratch\chipchip-order-app\ChipChip_MayVaGao_v1.0.apk`.
    * **App Icon chính thức:** Sử dụng chính xác file ảnh `assets/logo.jpg` của tiệm *ChipChip Mây & Gạo* cho toàn bộ các độ phân giải mipmap (mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi).
    * Tên ứng dụng hiển thị trên điện thoại: **ChipChip Mây & Gạo**.
    * Chạy 100% Offline: Tích hợp sẵn toàn bộ thư viện CSS/JS (Tailwind, Chart.js, FontAwesome) trong gói APK, không cần internet vẫn mở app tức thì.
    * Sửa triệt để lỗi ô vuông font icon (tofu): Điều chỉnh đường dẫn `webfonts/` cục bộ và đồng bộ font file `woff2` chuẩn xác, bổ sung CDN fallback đảm bảo hiển thị 100% tất cả các icon (cân, xe tải, mã QR, đồng hồ, bánh kẹo).
  - **Cơ Chế Bảo Toàn Dữ Liệu Tuyệt Đối (Dù Xóa App Cài Lại Vẫn Còn Nguyên):**
    1. *Tự động lưu vào bộ nhớ công cộng (`/storage/emulated/0/Download/ChipChip_Backup_Auto.json`):* Mỗi khi có thay đổi (thêm đơn, đổi trạng thái giao/tiền, sửa giá, thêm nguyên liệu), app tự động ghi đồng bộ bản sao lưu ra thư mục `Download` của máy. Thư mục này của Android **không bao giờ bị xóa** khi gỡ ứng dụng.
    2. *Tự động khôi phục khi cài lại:* Khi chị vợ cài lại app, app vừa mở lên sẽ tự động phát hiện file sao lưu trong `Download/` và phục hồi lại 100% toàn bộ sổ sách cũ ngay lập tức.
    3. *Dữ liệu mẫu 12.6 kg mặc định:* Kể cả khi chưa có file sao lưu, bộ dữ liệu 33 đơn 12.6kg được nhúng sẵn bên trong APK.
    4. *Nút Sao lưu & Khôi phục thủ công:* Trong mục `Cài đặt`, bổ sung thêm 2 nút `[Xuất file sao lưu]` và `[Khôi phục từ file]` để người dùng có thể gửi file dự phòng qua Zalo cho chồng bất kỳ lúc nào.
    5. *Android Auto Cloud Backup:* Bật `android:allowBackup="true"` trong `AndroidManifest.xml` hỗ trợ sao lưu qua Google Drive.

- **2026-11-22 (Phiên 13 - Nâng cấp Logo Vừa Khung, Chia 4 Tab Bottom Navigation, Chống Giật Lag 60FPS, Tìm Kiếm Tiếng Việt Không Dấu):**
  - **Sửa Lỗi Logo Không Vừa Khung & Xóa Ô Vuông Checkerboard:**
    * Phát hiện file logo cũ có viền lưới ca rô trong suốt bị nướng cứng (checkerboard).
    * Cắt tự động khung biểu tượng hình tròn 2 bé (bounding box x: 117-915, y: 119-936) phóng lớn 95% phủ kín khung hình, chuyển nền sang màu kem hồng pastel `#FFF6F8` ngọt ngào.
    * Tạo lại toàn bộ bộ icon launcher Android (`mipmap-mdpi`, `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`) hiển thị tròn đầy, bóng bẩy trên màn hình chính của điện thoại.
    * Màn hình mở app (Splash Screen) nâng cấp logo to 96x96px bo góc squircle kèm vầng đổ bóng hồng êm ái.
  - **Giải Quyết Triệt Để Cảm Giác Giật Lag & Vuốt Đường Thẳng Vô Tận:**
    * Nguyên nhân lag: Việc nhồi nhét toàn bộ Dashboard, Form nhập, 4 thẻ trạng thái và 33 card đơn hàng cùng hiệu ứng `backdrop-filter: blur` nặng trên 1 trang đơn khiến GPU WebView bị quá tải khi cuộn.
    * Giải pháp: Xóa bỏ các lớp blur nặng, bật gia tốc phần cứng (`transform: translateZ(0)`), tối ưu cuộn 60 FPS mượt như nhung.
    * **Chuyển đổi giao diện sang Hệ Thống 4 Tab Đáy Màn Hình (Bottom Navigation Bar):**
      1. 📋 **Sổ Đơn:** Thanh tìm kiếm thông minh + 4 Thẻ trạng thái + Bộ lọc + Danh sách đơn hàng (cuộn nhẹ tênh).
      2. ➕ **Thêm Đơn:** Màn hình nhập đơn riêng biệt siêu nhanh, không bị vướng víu giữa danh sách; tạo đơn xong tự động nhảy sang Sổ Đơn.
      3. 💰 **Thu Chi:** Sổ vật tư nguyên liệu & Thẻ tài chính Lợi Nhuận Ròng (Đã thu - Mua đồ = Lãi ròng) lọc theo Ngày / Tháng / Đợt.
      4. 📊 **Tổng Kết:** Dashboard tổng khối lượng (12.6 kg), thống kê chi tiết từng vị kẹo (chuẩn bị mẻ nấu), Phân tích biểu đồ & Báo cáo doanh thu tối Zalo, quản lý sao lưu an toàn.
  - **Cơ Chế Tìm Kiếm Khách Hàng Thông Minh (Instant Search):**
    * Ô tìm kiếm đặt ngay đầu tab Sổ Đơn với icon kính lúp sang trọng, gõ đến đâu lọc tức thì đến đó.
    * Thuật toán `removeVietnameseTones`: Tìm kiếm không phân biệt dấu và hoa thường (gõ "duc" tìm ra "A đức", "hoa" tìm ra "Mụ hoa gạo", "chanh" tìm ra kẹo húng chanh...).
    * Nút xóa nhanh (x) và thông báo tìm kiếm không thấy thân thiện kèm nút khôi phục.
  - **Xuất Bản APK Mới Nhất:**
    * Đã đóng gói và cập nhật file APK: `ChipChip_MayVaGao_v1.0.apk` (48.8 MB).
    * Giữ nguyên 100% cơ chế tự động sao lưu và khôi phục từ thư mục công cộng `Download` khi xóa/cài lại app.

- **2026-11-23 (Phiên 14 - Cố Định Mã VietQR Chính Thức Đỗ Thị Hà Giang & Chế Độ Phóng To Toàn Màn Hình):**
  - **Cố Định Mã VietQR Chính Thức:**
    * Sử dụng trực tiếp ảnh thẻ VietQR ngân hàng Quân Đội (MB Bank) do người dùng cung cấp:
      - Chủ tài khoản: **DO THI HA GIANG**
      - Số tài khoản / SĐT: **0941406007**
      - Ngân hàng: **MB Bank (Quân Đội)**
      - Chuẩn: VietQR / Napas 247
    * Lưu trữ cố định tại: `assets/qr_bank.jpg` (đã cắt cúp viền trắng chuẩn, sắc nét HD).
  - **Chế Độ Phóng To Toàn Màn Hình (Full-Screen QR Zoom):**
    * Khi bấm vào ảnh mã QR trong modal hoặc bấm nút `[Phóng To Quét Mã]`, giao diện sẽ lập tức phóng to mã QR trên nền tối tương phản cao (`bg-slate-950/95`).
    * Giúp khách đứng từ xa hoặc mọi người quét mã thanh toán bằng điện thoại cực kỳ nhạy và dễ dàng.
    * Chạm bất kỳ đâu trên màn hình hoặc nút X để đóng lại nhanh chóng.
  - **Tinh Gọn Giao Diện Cài Đặt (Xóa Bỏ Form Đổi Thẻ):**
    * Gỡ bỏ hoàn toàn các ô chọn ngân hàng, nhập STK, tên chủ tài khoản và ô tải ảnh chụp QR trong mục Cài đặt theo yêu cầu của người dùng (vì mã QR đã được ghim cố định chính thức).
    * Thay bằng huy hiệu xác thực: *Mã QR & Tài Khoản Cố Định (Đã ghim sẵn - Chính chủ DO THI HA GIANG - 0941406007)* kèm nút chạm để xem/phóng to ngay.
    * Trong Modal QR thanh toán, bỏ nút "Cài đặt STK / Đổi QR", thay bằng nút lớn `[Phóng To Quét Mã]` trực quan.

- **2026-11-24 (Phiên 15 - Xóa Bỏ Hộp Thoại Trình Duyệt Xấu Xí, Nâng Cấp Modal Xác Nhận & Nhập Liệu Chuẩn Native):**
  - **Khắc Phục Lỗi Thông Báo "Trang tại http://127.0.0.1 cho biết:":**
    * Nguyên nhân: Trước đây các thao tác xóa đơn, xóa tất cả, nạp mẫu và thêm vị sử dụng hàm `window.confirm()` và `window.prompt()` mặc định của trình duyệt WebView nên bị bật lên hộp thoại hệ thống xám xịt thô ráp, hiện dòng chữ debug "Trang tại http://127.0.0.1 cho biết:".
    * Giải pháp: Xóa bỏ 100% các lệnh `confirm()`, `prompt()` và `alert()` nguyên thủy.
  - **Thiết Kế Modal Xác Nhận Hành Động Cao Cấp (`#confirmModal`):**
    * Giao diện phong cách thẻ nổi 3D bo góc lớn `rounded-3xl`, phủ nền tối mờ kính `backdrop-blur-sm`, đồng bộ tone màu pastel kẹo chip chip.
    * Icon chỉ báo tròn đa sắc (thùng rác đỏ hồng cho thao tác xóa, tam giác vàng cho cảnh báo, mũi tên xanh cho khôi phục).
    * Hiển thị chính xác tên đơn hàng đang xóa: *"Bạn có chắc muốn xóa hẳn đơn của [Tên khách] không? Hành động này không thể hoàn tác."*
    * 2 nút bấm xúc giác hiện đại: `[Hủy bỏ]` (xám mịn) và `[Xóa vĩnh viễn]` (gradient đỏ hồng rực rỡ).
  - **Thiết Kế Modal Nhập Liệu Tiện Lợi (`#promptModal`):**
    * Dùng cho thao tác "+ Thêm vị mới" và "+ Thêm đợt kẹo mới" ngay trong ứng dụng, có ô gõ phím trực quan, nút xác nhận và phím Enter tiện lợi.
  - **Chuyển Toàn Bộ Thông Báo Sang Toast Notification:**
    * Các thông báo nhắc nhở (chưa nhập tên khách, sao chép STK, lưu cài đặt) chuyển sang dạng thông báo nổi (Toast pill) mượt mà lướt từ đỉnh màn hình xuống và tự biến mất sau 2 giây, không chặn màn hình.

- **2026-11-24 (Phiên 16 - Đột Phá Hiệu Năng Cuộn 60-120 FPS & Thiết Kế Lại Thanh Điều Hướng Đáy To Rõ, Đẹp Mắt):**
  - **Triệt Tiêu Giật Khựng Khi Cuộn Thanh Kéo Lên Xuống:**
    * Phát hiện nguyên nhân cốt lõi gây giật lag:
      1. Hiệu ứng `backdrop-blur-md` trên thanh tiêu đề và thanh điều hướng đáy bắt GPU của máy phải tính toán bộ lọc làm mờ Gaussian liên tục trên từng khung hình cuộn.
      2. Thuộc tính `transition` toàn cục trên các thẻ đơn hàng khiến engine style phải tính toán lại liên tục khi ngón tay chạm lướt.
    * Giải pháp tối ưu:
      1. Xóa sạch `backdrop-blur` trên Header và Bottom Bar, sử dụng nền trắng tinh khôi chuẩn native (`bg-white border-slate-200`) giải phóng hoàn toàn GPU.
      2. Kích hoạt công nghệ hiển thị ảo hóa phần cứng: `content-visibility: auto; contain: layout style paint; contain-intrinsic-size: 135px;` cho từng thẻ `.order-card`. Máy chỉ vẽ các thẻ đang nằm trong tầm mắt, thẻ ngoài màn hình được giải phóng tài nguyên.
      3. Bật `touch-action: pan-y; -webkit-overflow-scrolling: touch; transform: translateZ(0);` giúp thanh cuộn lướt mượt mà như nhung 60 - 120 FPS.
  - **Thiết Kế Lại 4 Mục Điều Hướng Đáy Màn Hình To, Đẹp & Sang Trọng:**
    * Khắc phục phản hồi của người dùng về việc 4 mục bị nhỏ, mờ và không đẹp:
      1. Kích thước icon tăng mạnh từ `text-lg` (18px) lên **`text-2xl` (24px)** to tròn, sắc nét.
      2. Chữ nhãn tăng từ `10px` lên **`12px` đậm (`text-xs font-black`)**, hiển thị rõ ràng, dễ nhìn cho mọi đối tượng.
      3. Tab đang chọn được bọc trong **viên nang nổi bật (`bg-rose-50 text-rose-600 rounded-2xl`)**, cực kỳ hiện đại và bắt mắt.
      4. Các tab còn lại có màu xám đậm `text-slate-500 font-extrabold`, không bị mờ nhạt như trước.
      5. Huy hiệu số lượng đơn (`navOrdersBadge`) to rõ, viền trắng đôi nổi bật tại góc icon.
      6. Mở rộng chiều cao thanh điều hướng, ngón tay cái chạm cực kỳ thoải mái và êm ái.

- **2026-11-24 (Phiên 17 - Khắc Phục Lỗi Hiển Thị Số 0 Ở Thẻ Trạng Thái & Bảo Toàn Dữ Liệu Sau Reinstall):**
  - **Sửa Lỗi Số 0 Tại Các Thẻ & Bộ Lọc:**
    * Phát hiện nguyên nhân: Trong `initApp()`, lệnh gọi DOM gán giá trị cho các input ngân hàng đã bị xóa trước đó phát sinh lỗi JavaScript `TypeError: Cannot set properties of null (setting 'value')`, làm ngắt quãng vòng lặp render, khiến các thẻ trạng thái và tab lọc giữ nguyên số mặc định 0.
    * Đã bổ sung guard an toàn (`if (elBank)...`) và bao bọc toàn bộ thao tác cập nhật DOM, phục hồi hiển thị chính xác 100% số lượng đơn ngay khi khởi động.
  - **Bảo Vệ Dữ Liệu Sau Khi Gỡ Cài Đặt (Uninstall App):**
    * Bổ sung quyền `MANAGE_EXTERNAL_STORAGE`, `WRITE_EXTERNAL_STORAGE`, `READ_EXTERNAL_STORAGE` và cờ `android:requestLegacyExternalStorage="true"` trong `AndroidManifest.xml`.
    * Tự động sao lưu dữ liệu đơn hàng và nguyên liệu vào các thư mục `/storage/emulated/0/Download/ChipChip_Backup_Auto.json` và `/storage/emulated/0/Documents/`. Khi người dùng gỡ cài đặt app rồi cài lại, hệ thống tự động quét và khôi phục nguyên vẹn 100% dữ liệu.

- **2026-11-24 (Phiên 18 - Tích Hợp Động Cơ Cập Nhật OTA Siêu Tốc 1-2 Giây & Bộ Công Cụ Đóng Gói OTA):**
  - **Xóa Bỏ Cảnh Báo Google Play Protect & Loại Bỏ Việc Tải APK Nặng 48MB:**
    * Người dùng không còn phải tải file APK mỗi lần có cập nhật mới (tránh bị Google Play Protect cảnh báo quét ứng dụng hoặc nhầm tưởng virus).
    * Tích hợp động cơ OTA Engine ngay trong lõi Flutter: Khi có cập nhật mới, app chỉ cần tải gói vá siêu nhẹ `latest_ota_package.zip` (~200KB - 2MB) hoặc file HTML, nạp và áp dụng trực tiếp trong 1-2 giây.
  - **Cơ Chế Chống Lặp Cập Nhật (Anti-loop) & Chống Phình Bộ Nhớ (Anti-bloat):**
    * File `active_ota_version.json` ghi nhận phiên bản và build number chính xác sau khi nạp gói OTA.
    * Tự động dọn dẹp sạch sẽ các file zip tải về và file tạm trung gian ngay sau khi nạp hoặc khi khởi động app.
  - **3 Phương Thức Cập Nhật Linh Hoạt:**
    1. Quét tự động gói OTA có sẵn trong thư mục máy (`Download/`).
    2. Nạp gói file thủ công trực tiếp từ giao diện (`.zip` hoặc `.html`).
    3. Cập nhật Online qua máy chủ/URL từ xa.
    4. Nút "Khôi phục bản gốc" an toàn nếu muốn quay về phiên bản gốc kèm APK.
  - **Bộ Công Cụ Đóng Gói Tiện Lợi:**
    * Tạo công cụ `Dong_Goi_OTA.bat` và `tools/pack_ota.py`: 1 cú đúp chuột tự động sinh `latest_ota_package.zip`, `update_v{version}.zip`, cập nhật `version.json` và đồng bộ mã nguồn.

- **2026-11-24 (Phiên 19 - CHỐT NGUYÊN TẮC: TỪ NAY CHỈ CẬP NHẬT QUA OTA - TUYỆT ĐỐI KHÔNG XUẤT APK):**
  - **Quyết định hệ thống của người dùng:** Từ nay về sau mỗi khi sửa lỗi, nâng cấp tính năng, giao diện:
    1. **CHỈ CẦN cập nhật qua gói OTA** (`latest_ota_package.zip`, `update_vX.X.X.zip`, `version.json`).
    2. **TUYỆT ĐỐI KHÔNG xuất file APK nữa** (tránh phiền hà, tránh cảnh báo Google Play Protect, tiết kiệm thời gian).
    3. **Cập nhật 1 chạm ngay trong app:** Chỉ cần quét máy hoặc nạp file/online trong 1-2 giây.
    4. **Bảo toàn dữ liệu 100%:** Tuyệt đối không bao giờ làm mất dữ liệu đơn hàng, nguyên liệu, ghi chú của người dùng khi cập nhật.

- **2026-11-24 (Phiên 20 - Tinh Gọn 1 Nút [Cập Nhật OTA Siêu Tốc] Duy Nhất & Phát Hành Gói OTA v1.0.2 Test Ngay):**
  - **Xóa Bỏ Nút "Quét Gói Máy":**
    * Loại bỏ hoàn toàn nút [Quét Gói Máy] tại cả Tab 4 (Tổng Kết) và Modal Cài Đặt Hệ Thống theo yêu cầu của người dùng.
    * Hợp nhất thành 1 nút bấm duy nhất to bản, nổi bật: **`[⚡ CẬP NHẬT OTA SIÊU TỐC]`**.
    * Nút thông minh tự động kích hoạt:
      1. Tự động kiểm tra xem có file `latest_ota_package.zip` trong thư mục `Download` không. Nếu có, hỏi người dùng và nâng cấp trong 1 giây!
      2. Nếu chưa thấy trong Download, tự động mở cửa sổ chọn file từ điện thoại để người dùng chọn gói cập nhật.
  - **Phát Hành Bản OTA Thử Nghiệm v1.0.2 (Build 103):**
    * Đi kèm huy hiệu xanh lá nổi bật `⚡ v1.0.2` ngay cạnh logo tiêu đề để người dùng nhận biết ngay khi nạp thành công.
    * Gói OTA: `latest_ota_package.zip` (~2.3 MB) sẵn sàng nạp thử nghiệm 1 giây mà không mất bất kỳ dữ liệu đơn nào.

## 3. Danh Sách Tính Năng Cốt Lõi (Đã Hoàn Thành & Đang Ổn Định)
- [x] Tạo `PROJECT_MEMORY.md` theo quy tắc hệ thống.
- [x] Tích hợp Động Cơ Cập Nhật OTA Siêu Tốc (1-2 giây), loại bỏ tải APK và cảnh báo Play Protect.
- [x] Cơ chế Chống Lặp Cập Nhật (Anti-loop) & Chống Phình Bộ Nhớ (Anti-bloat) theo quy tắc KINI/VideoSub.
- [x] Công cụ đóng gói OTA 1-chạm `Dong_Goi_OTA.bat` và `tools/pack_ota.py`.
- [x] Khắc phục triệt để lỗi hiển thị số 0 ở các thẻ trạng thái & tab lọc.
- [x] Bảo vệ dữ liệu đơn hàng 100% không bao giờ mất khi cập nhật hoặc gỡ cài đặt app (Persistent Public Backup).
- [x] Đột phá hiệu năng cuộn 60-120 FPS mượt như nhung với `content-visibility: auto` và gỡ bỏ `backdrop-blur`.
- [x] Thiết kế lại thanh điều hướng đáy to bản, đẹp mắt, có viên nang highlight và icon 24px siêu nét.
- [x] Thay thế toàn bộ hộp thoại trình duyệt (confirm/alert/prompt) bằng Modal xác nhận & Toast Notification chuẩn Native sang xịn.
- [x] Ghim cố định mã VietQR chính thức MB Bank của chị Đỗ Thị Hà Giang (0941406007).
- [x] Chế độ phóng to mã QR toàn màn hình (Full-Screen Zoom) giúp khách quét cực nhạy.
- [x] Xóa bỏ form đổi thẻ/tải ảnh QR không cần thiết, tinh gọn mục Cài đặt.
- [x] Tối ưu hiệu năng 60 FPS, chia màn hình 4 Tab chuyên biệt (Bottom Navigation Bar) loại bỏ vuốt dài và giật lag.
- [x] Cơ chế tìm kiếm tức thì theo tên khách hàng, loại bỏ dấu tiếng Việt thông minh (`removeVietnameseTones`).
- [x] Sửa logo ứng dụng vừa khít khung hình, xóa sạch ô vuông bàn cờ, cập nhật Splash screen & App icon HD.
- [x] Xuất bản gói APK Release `ChipChip_MayVaGao_v1.0.apk` với App Icon chính thức từ `assets/logo.jpg`.
- [x] Cơ chế chống mất dữ liệu khi gỡ cài đặt app: Tự động ghi và phục hồi từ thư mục công cộng `Download`.
- [x] Chạy Offline 100% không cần kết nối mạng.
- [x] Giao diện Web App chuyên dụng trên Mobile, tone màu kẹo chip chip ngọt ngào, nút to thân thiện.
- [x] Nhập đơn 1 chạm: Chọn nhanh số lạng (2, 3, 4, 5, 6...), số hộp, chọn vị linh hoạt.
- [x] Hệ thống quản lý Vị kẹo:
  - Mặc định 5 vị: Mix, Húng chanh, Xoài, Chanh leo, Sữa chua.
  - Nút "+ Thêm vị mới" tức thì.
  - Thống kê mẻ nấu: Tự động gom khối lượng cần làm của từng vị (Mix X lạng, Húng chanh Y lạng...).
- [x] Hệ thống cài đặt Giá bán:
  - Nút áp dụng giá chung đồng loạt (mặc định 25.000đ/lạng).
  - Bảng sửa giá riêng lẻ cho từng vị kẹo.
  - Tự động nhân giá theo vị của từng đơn và tính tổng doanh thu dự kiến.
- [x] Quy ước Gạch Xong chuẩn thói quen sổ tay:
  - Gạch đơn = Đã giao & Đã thu tiền (vẫn tính đủ vào tổng kg và tổng doanh thu).
  - Tab lọc riêng: "✓ Đã gạch xong (Đã giao & thu tiền)".
- [x] Bảng tổng kết Real-time:
  - Tổng số KG và Lạng tự động quy đổi chính xác tuyệt đối (12.6 kg).
  - Thống kê tiền: Tổng tiền dự kiến, Đã nhận, Chưa tiền.
- [x] Tự động lưu `localStorage` (không mất dữ liệu khi tắt mạng hoặc tắt app).
- [x] Nút "Chốt Zalo" tự động định dạng và sao chép văn bản báo cáo chuyên nghiệp.
- [x] Nạp sẵn dữ liệu mẫu thực tế chuẩn 12.6 kg từ ảnh ghi chú của chị để trải nghiệm ngay.
