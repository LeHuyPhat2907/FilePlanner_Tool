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
                print("❌ Lỗi: Dung lượng đã dùng không được là số âm. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số ký tự thuần túy (Ví dụ: 120, 80.4)!")
    
    return tong, da_dung

# # Đoạn code dùng để chạy thử nghiệm tính năng của riêng Task 3
if __name__ == "__main__":
    tong_dl, da_dung_dl = nhap_dung_luong_o_cung()
    print("-" * 50)
    print(f"--> [Dữ liệu đã nhận] Tổng: {tong_dl} GB | Đã dùng: {da_dung_dl} GB")
    print("-" * 50)
