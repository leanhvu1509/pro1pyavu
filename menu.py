import library

lbb = library.Library("listbook.txt") 

while (True):
    print("\n----------Chào mừng đến với thư viện AVU---------\n")
    print(" 1. Danh sách sách thư viên \n 2. Thêm sách \n 3. Sửa sách",
            " \n 4. Xóa sách \n 5. Tìm sách \n 6. Thuê sách \n 7. Trả sách \n 8. DS sách đã thuê \n 9.Thoát!")
    try:
        choice = int(input("Vui lòng chọn chức năng: "))
    except ValueError:
        print("Lỗi!\nXin hãy chọn số!")
        
    if choice == 1:
        print("\nChức năng : Hiện thị danh sách sách thư viên\n")
        lbb.hien_thi()
    elif choice == 2:
        print("\nChức năng : Thêm sách\n")
        lbb.them_sach()
    elif choice == 3:
        print("\nChức năng : Cập nhật sách\n")
        lbb.sua_sach()
    elif choice == 4:
        print("\nChức năng : Xóa sách\n")
        lbb.xoa_sach()
    elif choice == 5:
        print("\nChức năng : Tìm kiếm sách\n",
                "---1. Theo ID\n ---2. Theo tên sách\n")
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
        print("\nChức năng : Thuê sách\n")
        lbb.thue_sach()
    elif choice == 7:
        print("\nChức năng : Trả sách\n")
        lbb.tra_sach()
    elif choice ==8:
        print("\n Chức năng: DS sách đã thuê")
        lbb.kiem_tra_sach_da_thue()
    elif choice == 9:
        print("\nThoát.\n")
        break
    else:
        print("Chức năng chọn nằm ngoài hệ thống!")
        continue

   


# with open("listbook.txt","r",encoding="utf8") as lb:
#     lbook = lb.readlines()
# lb.close()
# s = input("Nhap")
# l=open("listbook.txt","w",encoding="utf8")
# for line in lbook:
#     if line.strip("\n") != s:
#         l.write(line)
# s ="Có sẵn"
# if s == "Có sẵn":
#     print("true")
# else:
#     print("sai")