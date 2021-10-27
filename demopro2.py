# print("\n1. Tên sách\t2. Tác giả\t3. Nhà xuất bản\n4. Năm xuất bản\t5. Giá sách\t6. Số trang")
print ("{:<30} {:<30} {:<30} {:<30}\n{:<30} {:<30} {:<30} {:<30}\n{:<30} {:<30}"
        .format('1. DS sách thư viện','2. Thêm mới sách','3. Cập nhật sách','4. Xóa sách'
                ,'5. Tìm kiếm sách','6. Sắp xếp sách','7. Thuê sách','8. Trả sách','9. DS sách đã thuê','10.Thoát!'))
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