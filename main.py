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

# # Đoạn code dùng để chạy thử nghiệm tính năng của riêng Task 3
if __name__ == "__main__":
    # Import hoặc gọi trực tiếp hàm từ Task 3 cũ
    # (Giả định hàm nhap_dung_luong_o_cung đã có sẵn ở trên)
    tong_dl, da_dung_dl = nhap_dung_luong_o_cung()
    
    # Gọi hàm xử lý tính toán của Task 4
    trong_dl, ty_le_dl = tinh_toan_dung_luong(tong_dl, da_dung_dl)
