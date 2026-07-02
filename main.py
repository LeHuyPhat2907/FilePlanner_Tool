def nhap_dung_luong_o_cung():
    print("=" * 50)
    print("      BƯỚC 1: KHAI BÁO THÔNG TIN Ổ CỨNG (ĐƠN VỊ: GB)")
    print("=" * 50)

    # 1. Nhập và kiểm tra tổng dung lượng
    while True:
        try:
            tong = float(input("Nhập TỔNG dung lượng ổ cứng của bạn (GB): "))
            if tong <= 0:
                print("Lỗi: Tổng dung lượng phải lớn hơn 0. Vui lòng nhập lại!")
                continue
            break # Thỏa mãn là số hợp lệ thì thoát vòng lặp
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số ký tự thuần túy (Ví dụ: 500, 256.5)!")

    # 2. Nhập kiểm tra dung lượng đã dùng
    while True:
        try:
            da_dung = float(input("Nhập số lượng Ổ CỨNG ĐÃ DÙNG (GB): "))
            if da_dung < 0:
                print("Lỗi: Dung lượng đã dùng không được là số âm. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số ký tự thuần túy (Ví dụ: 120, 80.4)!")
    
    return tong, da_dung

def tinh_toan_dung_luong(tong, da_dung):
   if da_dung > tong:
       print("Lỗi logic: Dung lượng đã dùng không thể lớn hơn tổng dung lượng ổ cứng!")
       return 0.0, 0.0
   
   # 1. Tính toán dung lượng trống bằng toán tử trừ (-)
   dung_luong_trong = tong - da_dung

   # 2. Tính tỉ lệ phần trăm bằng toán tử chia (/) và nhân (*)
   ty_le_trong = (dung_luong_trong / tong) * 100

   # 3. Hiển thị kết quả (làm tròn 2 chữ số thập phân bằng định dạng :.2f)
   print("\n" + "-" * 50)
   print("      KẾT QUẢ PHÂN TÍCH DUNG LƯỢNG Ổ CỨNG")
   print("-" * 50)
   print(f"Tổng dung lượng      : {tong:.2f} GB")
   print(f"Dung lượng đã dùng   : {da_dung:.2f} GB")
   print(f"Dung lượng còn trống : {dung_luong_trong:.2f} GB")
   print(f"Tỷ lệ trống          : {ty_le_trong:.2f}%")
   print("-" * 50)

   return dung_luong_trong, ty_le_trong

def kiem_tra_canh_bao_dung_luong(ty_le_trong):
    print("\n" + "=" * 50)
    print("      KẾT QUẢ KIỂM TRA TRẠNG THÁI Ổ CỨNG")
    print("=" * 50)

    # Áp dụng cấu trúc điều kiện if để kiểm tra tỷ lệ trống dưới 10%
    if ty_le_trong < 10.0:
        print("CẢNH BÁO NGHUY HIỂM: DUNG LƯỢNG TRỐNG CÒN DƯỚI 10%!")
        print("Ổ cứng của bạn đang ở trạng thái quá tải và cực kỳ bừa bộn.")
        print("Hiệu suất hệ thống có thể bị giảm sút nghiêm trọng.")
        print("ĐỀ XUẤT: Hãy tiến hành quy hoạch và dọn dẹp file ngay lập tức!")
    else:
        print("TRẠNG THÁI: Dung lượng ổ cứng hiện tại vẫn nằm trong mức an toàn.")
        print("Bạn có thể tiếp tục lên kế hoạch sắp xếp các nhóm file gọn gàng hơn.")
        
    print("=" * 50 + "\n")

def nhap_danh_sach_duoi_file():
    print("=" * 50)
    print("      BƯỚC 2: KHAI BÁO CÁC ĐUÔI FILE CẦN GOM NHÓM")
    print("=" * 50)
    print("Hướng dẫn: Nhập từng đuôi file (Ví dụ: .png, docx, .mp4)")
    print("Nhấn phím 'q' và Enter để HOÀN THÀNH việc khai báo.")
    print("-" * 50)

    danh_sach_ext = [] # Khởi tạo danh sách trống để lưu trữ dữ liệu đầu vào

    while True:
        # Nhập dữ liệu đầu vào và dùng .strip() để xóa khoảng trắng thừa ở 2 đầu
        nhap_vao = input("Nhập đuôi mở rộng (hoặc 'q' để dừng): ").strip()

        # Kiểm tra điều kiện thoát vòng lặp
        if nhap_vao.lower() == "q":
            print("\nĐã dừng nhận dữ liệu đầu vào từ người dùng.")
            break

        # Kiểm tra nếu người dùng không nhập gì mà chỉ bấm Enter
        if nhap_vao == "":
            print("Bạn chưa nhập gì cả. Vui lòng nhập đuôi file hoặc gõ 'q'!")
            continue

        # Thêm đuôi file vừa nhập vào danh sách lưu trữ
        danh_sach_ext.append(nhap_vao)
        print(f"Đã ghi nhận: '{nhap_vao}' (Tổng số trong hàng đợi: {len(danh_sach_ext)})")

    print(f"Danh sách đuôi file thô vừa thu thập: {danh_sach_ext}")
    print("=" * 50 + "\n")
    
    return danh_sach_ext

def chuan_hoa_danh_sach_duoi_file(danh_sach_tho):
    danh_sach_chuan_hoa = []

    for item in danh_sach_tho:
        # 1. Loại bỏ khoảng trắng thừa (nếu có) và chuyển về chữ thường
        item_clean = item.strip().lower()

        # 2. Sử dụng hàm kiểm tra ký tự đầu để tự động thêm dấu chấm '.' nếu thiếu
        if not item_clean.startswith('.'):
            item_clean = '.' + item_clean
        
        # Thêm vào danh sách mới sau khi gọt giũa
        danh_sach_chuan_hoa.append(item_clean)

    print("-" * 50)
    print(f"Kết quả chuẩn hóa:")
    print(f"   + Danh sách gốc : {danh_sach_tho}")
    print(f"   + Danh sách chuẩn: {danh_sach_chuan_hoa}")
    print("-" * 50 + "\n")

    return danh_sach_chuan_hoa

def phan_loai_danh_sach_file(danh_sach_chuan):
    ke_hoach_quy_hoach = []

    print("=" * 50)
    print("      BƯỚC 3: TIẾN HÀNH PHÂN LOẠI & QUY HOẠCH")
    print("=" * 50)

    for ext in danh_sach_chuan:
        # Khởi tạo cấu trúc lưu trữ cho từng tệp tin
        ket_qua_item = {
            "duoi_file": ext,
            "nhom": "",
            "lenh_de_xuat": ""
        }

        if ext in ['.png', '.jpg', '.jpeg', '.gif']:
            ket_qua_item["nhom"] = "[Hinh_Anh]"
            # Sinh câu lệnh di chuyển giả lập trên Windows/Console làm gợi ý
            ket_qua_item["lenh_de_xuat"] = f"move *{ext} D:\\Hinh_Anh\\"
            print(f"Phát hiện nhóm HÌNH ẢNH: Đuôi {ext} -> Gom vào [Hinh_Anh]")
        elif ext in ['.docx', '.pdf', '.xlsx', '.pptx', '.txt']:
            ket_qua_item["nhom"] = "[Tai_Lieu]"
            ket_qua_item["lenh_de_xuat"] = f"move *{ext} D:\\Tai_Lieu\\"
            print(f"[TÀI LIỆU] Đuôi {ext} -> Gom vào [Tai_Lieu]")
        elif ext in ['.exe', '.msi', '.dmg', '.apk']:
            ket_qua_item["nhom"] = "[Cai_Dat_Phan_Mem]"
            ket_qua_item["lenh_de_xuat"] = f"move *{ext} D:\\Cai_Dat_Phan_Mem\\"
            print(f"[BỘ CÀI PHẦN MỀM] Đuôi {ext} -> Gom vào [Cai_Dat_Phan_Mem]")
        elif ext in ['.mp4', '.mkv', '.avi', '.mov']:
            ket_qua_item["nhom"] = "[Video_Phim]"
            ket_qua_item["lenh_de_xuat"] = f"move *{ext} D:\\Video_Phim\\"
            print(f"[VIDEO & PHIM] Đuôi {ext} -> Gom vào [Video_Phim]")
        else:
            ket_qua_item["nhom"] = "[File_Khac]"
            ket_qua_item["lenh_de_xuat"] = f"move *{ext} D:\\File_Khac\\"
            print(f"[FILE KHÁC] Đuôi {ext} -> Gom tạm vào [File_Khac] để phân loại sau")
        
        # Lưu item vào danh sách kế hoạch tổng
        ke_hoach_quy_hoach.append(ket_qua_item)
    
    print("-" * 50)
    return ke_hoach_quy_hoach

def tao_goi_y_va_thong_ke(ke_hoach_quy_hoach):
    if not ke_hoach_quy_hoach:
        print("Không có dữ liệu để xử lý gợi ý.")
        return
    
    print("=" * 50)
    print("      BƯỚC 4: HỆ THỐNG GỢI Ý & THỐNG KÊ (Task 13 & 14)")
    print("=" * 50)

    tong_so_file = len(ke_hoach_quy_hoach)

    # Sử dụng set để lọc ra danh sách các nhóm độc bản (không trùng lặp)
    danh_sach_nhom_doc_ban = set()
    for item in ke_hoach_quy_hoach:
        danh_sach_nhom_doc_ban.add(item["nhom"])
    
    tong_so_nhom = len(danh_sach_nhom_doc_ban)

    print(f"📊 THỐNG KÊ PHIÊN LÀM VIỆC:")
    print(f"   + Tổng số đuôi mở rộng đã khai báo: {tong_so_file} định dạng.")
    print(f"   + Tổng số nhóm thư mục cần quy hoạch: {tong_so_nhom} nhóm.")
    print("-" * 50)

    print("DANH SÁCH LỆNH DI CHUYỂN ĐỀ XUẤT (Gợi ý dọn dẹp):")
    for stt, item in enumerate(ke_hoach_quy_hoach, start=1):
        print(f"   {stt}. Định dạng '{item['duoi_file']}' -> Thuộc nhóm: {item['nhom']}")
        print(f"      Lệnh đề xuất: {item['lenh_de_xuat']}")
    
    print("=" * 50 + "\n")

def hien_thi_menu_chao_mung():
    print("\n" + "*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "    TRỢ LÝ TỰ ĐỘNG LÊN KẾ HOẠCH QUY HOẠCH & DỌN DẸP FILE    " + "*")
    print("*" + "               --- FILE PLANNER TOOL v1.0 ---             " + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print(" Chào mừng bạn! Hãy khai báo thông tin để nhận sơ đồ dọn dẹp.\n")

def xuat_bao_cao_tong_ket(ke_hoach_quy_hoach):
    if not ke_hoach_quy_hoach:
        print("Không có dữ liệu để xuất báo cáo.")
        return

    print("\n" + "=" * 65)
    print("        BÁO CÁO SƠ ĐỒ KẾ HOẠCH QUY HOẠCH Ổ CỨNG TỔNG THỂ")
    print("=" * 65)
    
    # Định dạng tiêu đề cột cho bảng Console
    print(f"{'STT':<5} | {'Định Dạng':<12} | {'Nhóm Thư Mục Đích':<20} | {'Trạng Thái'}")
    print("-" * 65)

    # Duyệt in từng dòng dữ liệu trong bảng
    for idx, item in enumerate(ke_hoach_quy_hoach, start=1):
        ext = item["duoi_file"]
        nhom = item["nhom"]
        
        # Tạo nhãn trạng thái trực quan
        if nhom == "[File_Khac]":
            trang_thai = "Cần phân loại thủ công thêm"
        else:
            trang_thai = "Đã sẵn sàng di chuyển"

        print(f"{idx:<5} | {ext:<12} | {nhom:<20} | {trang_thai}")

    print("-" * 65)
    print("Lời khuyên: Hãy tạo các thư mục đích tương ứng trên ổ cứng của bạn")
    print("   và chạy các câu lệnh gợi ý (ở Bước 4) để hoàn tất việc dọn dẹp!")
    print("=" * 65 + "\n")

# Tái cấu trúc lại hàm main() chạy chính để tích hợp toàn bộ 16 Task đã làm
def main():
    # 1. Menu chào mừng (Task 15)
    hien_thi_menu_chao_mung()
    
    # 2. Khối nhập liệu & Tính toán ổ cứng (Task 3, 4, 5)
    tong_dl, da_dung_dl = nhap_dung_luong_o_cung()
    trong_dl, ty_le_dl = tinh_toan_dung_luong(tong_dl, da_dung_dl)
    kiem_tra_canh_bao_dung_luong(ty_le_dl)
    
    # 3. Vòng lặp nhận danh sách và chuẩn hóa (Task 6, 7)
    danh_sach_tho = nhap_danh_sach_duoi_file()
    if not danh_sach_tho:
        print("Bye bye! Bạn không nhập đuôi file nào.")
        return
        
    danh_sach_chuan = chuan_hoa_danh_sach_duoi_file(danh_sach_tho)
    
    # 4. Phân loại cốt lõi (Task 8 -> 12)
    ket_qua_quy_hoach = phan_loai_danh_sach_file(danh_sach_chuan)
    
    # 5. Thống kê & Lệnh gợi ý (Task 13, 14)
    tao_goi_y_va_thong_ke(ket_qua_quy_hoach)
    
    # 6. Xuất báo cáo tổng kết dạng bảng (Task 16)
    xuat_bao_cao_tong_ket(ket_qua_quy_hoach)

if __name__ == "__main__":
    main()
