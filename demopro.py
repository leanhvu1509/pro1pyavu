from collections import OrderedDict
temp = {}
id = 1
list_books = "demopro.txt"
with open(list_books,encoding="utf8") as lb:
    lbook = lb.readlines()
    
for line in lbook:
    # print(line.replace("\n","").split("-"))
    mang = line.replace("\n","").split("-")
    name = mang[0]
    tacgia = mang[1]
    sotrang = mang[2]
    # print(name+" - "+tacgia+" - "+sotrang)
    temp.update(
        {
        str(id):
            {
                'ten_sach':name,
                'tac_gia':tacgia,
                'so_trang':sotrang,
                'nguoi_thue':'',
                'ngay_thue':'',
                'status':'Có sẵn'
            }         
        }
    )
    id+=1
# print(temp)
res = OrderedDict(sorted(temp.items(),key=lambda x:x[1]['so_trang'],reverse= True))
print(res)
print("------------------------Danh sách sách thư viên---------------------")
print ("{:<5} {:<35} {:<15} {:<10} {:<10}".format('ID','Ten sach','Tac gia','So trang','Status'))
print("--------------------------------------------------------------------")
for key,value in res.items():
    print("{:<5} {:<35} {:<15} {:<10} {:<10}"
            .format(key,value.get("ten_sach"),value.get("tac_gia"),value.get("so_trang"),value.get("status")))

new_book = input("Nhập tên sách: ")
new_tg = input("Nhap tg: ")
new_page= input("Nhap so trang: ")
temp.update({
    str(int(max(temp))+1):
        {
            'ten_sach':new_book,
            'tac_gia':new_tg,
            'so_trang':new_page,
            'nguoi_thue':'',
            'ngay_thue':'',
            'status':'Có sẵn'
        }
    })
new_input = new_book+"-"+new_tg+"-"+new_page
with open(list_books,"a",encoding="utf8") as lw:
    lw.writelines(f"{new_input}\n")

print("------------------------Danh sách sách thư viên---------------------")
print ("{:<5} {:<35} {:<15} {:<10} {:<10}".format('ID','Ten sach','Tac gia','So trang','Status'))
print("--------------------------------------------------------------------")
for key,value in temp.items():
    print("{:<5} {:<35} {:<15} {:<10} {:<10}"
            .format(key,value.get("ten_sach"),value.get("tac_gia"),value.get("so_trang"),value.get("status")))

