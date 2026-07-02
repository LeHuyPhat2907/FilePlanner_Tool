# 📂 File Planner Tool - Trợ Lý Quy Hoạch Ổ Cứng Tự Động

**File Planner Tool** là một ứng dụng Console viết bằng ngôn ngữ Python, đóng vai trò như một trợ lý ảo giúp người dùng lên kế hoạch, phân loại và dọn dẹp các tệp tin bừa bộn (đặc biệt là thư mục `Downloads`) một cách khoa học chỉ sau vài giây khai báo.

---

## 🚀 Tính Năng Cốt Lõi

* **Kiểm tra trạng thái ổ cứng:** Nhập thông số và tự động tính toán tỷ lệ dung lượng trống.
* **Cảnh báo thông minh:** Hệ thống kích hoạt cảnh báo nghiêm trọng nếu dung lượng trống hệ thống rơi xuống dưới mức nguy hiểm (< 10%).
* **Bộ lọc phân loại toàn diện:** Sử dụng cấu trúc rẽ nhánh cấu hình sẵn để phân loại hàng loạt đuôi mở rộng:
  * 📸 `[Hinh_Anh]`: `.png`, `.jpg`, `.jpeg`, `.gif`
  * 📄 `[Tai_Lieu]`: `.docx`, `.pdf`, `.xlsx`, `.pptx`, `.txt`
  * ⚙️ `[Cai_Dat_Phan_Mem]`: `.exe`, `.msi`, `.dmg`, `.apk`
  * 🎬 `[Video_Phim]`: `.mp4`, `.mkv`, `.avi`, `.mov`
  * 📦 `[File_Khac]`: Các định dạng lạ khác cần lọc thủ công.
* **Xử lý chuỗi thông minh:** Tự động gọt khoảng trắng thừa, chuyển chữ HOA thành chữ thường và bù dấu chấm `.` nếu người dùng quên nhập (Ví dụ: `PNG` hoặc `docx` đều được chuẩn hóa chuẩn format).
* **Sinh câu lệnh di chuyển đề xuất:** Xuất ra các dòng lệnh `move` mẫu tương ứng cho từng định dạng để người dùng copy-paste thực thi trên Terminal hệ thống.
* **Xuất báo cáo dạng bảng:** Tổng kết kế hoạch dọn dẹp bằng bảng phân cột trực quan trước khi kết thúc chương trình.

---

## 🛠️ Yêu Cầu Hệ Thống & Cấu Trúc Thư Mục

### Yêu cầu
* **Python 3.x** trở lên (Không cần cài đặt thêm thư viện).




### Cấu trúc dự án
```text
FilePlanner_Tool/
│
├── data/
│   └── extensions_note.txt   # Tài liệu ghi chú các định dạng file mở rộng
│
├── .gitignore                # File cấu hình bỏ qua tệp tin rác khi push Git
├── main.py                   # Mã nguồn chạy chính của chương trình
└── README.md                 # Tài liệu hướng dẫn sử dụng (File này)
```
## Hướng Dẫn Chạy Chương Trình
1. Mở Terminal hoặc Command Prompt (cmd) tại thư mục chứa dự án.
2. Chạy câu lệnh sau để khởi động tool:
```text
python main.py
```
3. Tiến hành nhập các thông số theo chỉ dẫn trên màn hình:
* **Bước 1: Khai báo Tổng dung lượng và Dung lượng đã dùng để kiểm tra độ an toàn của ổ cứng.
* **Bước 2: Nhập liên tục các đuôi mở rộng đang bừa bộn. Gõ q để dừng nhận dữ liệu.
* **Bước 3 & 4: Nhận kết quả phân tích thống kê và sơ đồ bảng kế hoạch quy hoạch tổng thể.

## 👤 Tác Giả & Nhà Phát Triển

Dự án được nghiên cứu, thiết kế, phát triển và kiểm thử độc lập 100% bởi:

* **Lập trình viên:** Lê Huy Phát
* **Vai trò:** Toàn quyền phát triển dự án (Full-cycle Developer từ phân tích luồng, thiết kế cấu trúc dữ liệu, hiện thực hóa mã nguồn cho đến kiểm thử dữ liệu biên).
