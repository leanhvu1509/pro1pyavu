import library

lbb = library.Library("listbook.txt") 

while (True):
    print("\n----------------------------------------Chào mừng đến với thư viện AVU----------------------------------------\n")
    print ("{:<30} {:<30} {:<30} {:<30}\n{:<30} {:<30} {:<30} {:<30}\n{:<30}"
        .format('1. DS sách thư viện','2. Thêm mới sách','3. Cập nhật sách','4. Xóa sách',
                '5. Tìm kiếm sách','6. Sắp xếp sách','7. Quản thuê & trả sách','8. DS sách đã thuê',
                '9.Thoát!'))
    try:
        choice = int(input("Vui lòng chọn chức năng: "))
    except ValueError:
        print("Lỗi! Xin hãy chọn số!")
        
    if choice == 1:
        print("\nChức năng : Hiện thị danh sách sách thư viên\n")
        lbb.hien_thi()
    elif choice == 2:
        print("\nChức năng : Thêm mới sách\n")
        lbb.them_sach()
    elif choice == 3:
        print("\nChức năng : Cập nhật sách\n")
        lbb.sua_sach()
    elif choice == 4:
        print("\nChức năng : Xóa sách\n")
        lbb.xoa_sach()
    elif choice == 5:
        print("\nChức năng : Tìm kiếm sách\n",
                "---1. Theo mã ID\n ---2. Theo tên sách\n")
        try:
            chon = int(input("Xin lựa chọn 1 trong 2 chức năng trên :"))
        except ValueError:
            print("Lỗi nhập!\nVui lòng làm lại")
            break
        else:
            if chon == 1:
                lbb.tim_sach_theo_id()
            elif chon == 2:
                lbb.tim_sach_theo_ten()
            else:
                print("Lựa chọn đó không tồn tại!")
    elif choice == 6:
        print("\nChức năng : sắp xếp sách\n")
        print ("{:<45} {:<45}\n{:<45} {:<45}\n{:<45} {:<45}"
                .format('1. Theo ID giảm dần','2. Theo tên sách',
                        '3. Theo năm xuất bản (giảm dần)','4. Theo năm xuất bản (tăng dần)',
                        '5. Theo năm giá sách (giảm dần)','6. Theo năm giá sách (tăng dần)'))
        try:
            chon = int(input("Xin lựa chọn 1 trong 6 chức năng trên :"))
        except ValueError:
            print("Lỗi nhập!\nVui lòng làm lại")
            break
        else:
            if chon == 1:
                lbb.sap_xep_sach_theo_id_giam_dan()
            elif chon == 2:
                lbb.sap_xep_sach_theo_ten()
            elif chon == 3:
                lbb.sap_xep_sach_theo_nam_xb_giam_dan()
            elif chon == 4:
                lbb.sap_xep_sach_theo_nam_xb_tang_dan()
            elif chon == 5:
                lbb.sap_xep_sach_theo_price_giam_dan()
            elif chon == 6:
                lbb.sap_xep_sach_theo_price_tang_dan()
            else:
                print("Lựa chọn đó không tồn tại!")
    elif choice == 7:
        print("\nChức năng : Quản lý thuê sách và trả sách\n",
                "---1. Thuê sách\n ---2. Trả sách\n")
        try:
            chon = int(input("Xin lựa chọn 1 trong 2 chức năng trên :"))
        except ValueError:
            print("Lỗi nhập!\nVui lòng làm lại")
            break
        else:
            if chon == 1:
                lbb.thue_sach()
            elif chon == 2:
                lbb.tra_sach()
            else:
                print("Lựa chọn đó không tồn tại!")
    elif choice ==8:
        print("\n Chức năng: DS sách đã thuê")
        lbb.kiem_tra_sach_da_thue()
    elif choice == 9:
        print("\nThoát.\n")
        break
    else:
        print("Chức năng chọn nằm ngoài hệ thống!")
        continue

