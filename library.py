import datetime
from os import replace
from collections import OrderedDict
class Library:
    """
    Đây là lớp xử lý các chức năng của quản lý thư viên (console)
    """
    def __init__(self,list_books):
        self.list_books = "listbook.txt"
        self.dictBook = {}
        id = 1
        with open(self.list_books,encoding="utf8") as lb:
            lbook = lb.readlines()
        for line in lbook:
            temp = line.replace("\n","").split("-")
            ten_sach = temp[0]
            tac_gia = temp[1]
            nxb = temp[2]
            nam_xb = temp[3]
            price = temp[4]
            so_trang = temp[5]
            self.dictBook.update(
                {
                str(id):
                    {
                    'ten_sach':ten_sach,
                    'tac_gia':tac_gia,
                    'nxb':nxb,
                    'nam_xb':nam_xb,
                    'price':price,
                    'so_trang':so_trang,
                    'status':'Có sẵn',
                    'nguoi_thue':'',
                    'sdt':'',
                    'ngay_thue':''
                    }
                }
            )
            id += 1
            
    # Hàm hiển thị danh sách sách thư viện
    def hien_thi(self):
        print("--------------------------------------------------Danh sách sách thư viên--------------------------------------------------")
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<10}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        for key,value in self.dictBook.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<10}"
                    .format(key,value.get("ten_sach"),value.get("tac_gia"),value.get("nxb")
                            ,value.get("nam_xb"),value.get("price"),value.get("so_trang"),value.get("status")))
        print("---------------------------------------------------------------------------------------------------------------------------")
    # Hàm thêm sách vào thư viện
    def them_sach(self):
        new_book = input("Nhập tên sách: ")
        new_tg = input("Nhập tên tác giả: ")
        new_nxb = input("Nhập tên NXB: ")
        new_nam = input("Nhập năm xuất bản: ")
        new_gia = input("Nhập giá sách: ")
        new_page = input("Nhập số trang: ")
        if new_book == "":
            return self.them_sach()
        elif len(new_book)>30:
            print("Tiêu đề sách quá dài (quá 30 chữ)")
            return self.them_sach()
        else:
            new_input = new_book+"-"+new_tg+"-"+new_nxb+"-"+new_nam+"-"+new_gia+"-"+new_page
            with open(self.list_books,"a",encoding="utf8") as nb:
                nb.writelines(f"{new_input}\n")
            self.dictBook.update({
                str(int(max(self.dictBook))+1):
                    {
                    'ten_sach':new_book,
                    'tac_gia':new_tg,
                    'nxb':new_nxb,
                    'nam_xb':new_nam,
                    'price':new_gia,
                    'so_trang':new_page,
                    'status':'Có sẵn',
                    'nguoi_thue':'',
                    'sdt':'',
                    'ngay_thue':''
                    }
            })
            print(f"\n<{new_book}> đã được thêm mới thành công!")
    
    # Hàm cập nhật sách
    def sua_sach(self):
        idsach = input("Nhập ID sách cần cập nhật: ")
        if idsach in self.dictBook.keys():
            if not self.dictBook[idsach]['status'] == "Có sẵn" :
                print(f"Sách này đang được thuê vui lòng nên chưa cập nhật được!!")
            elif self.dictBook[idsach]['status'] == "Có sẵn" :
                print("\n1. Tên sách\t2. Tác giả\t3. Nhà xuất bản\n4. Năm xuất bản\t5. Giá sách\t6. Số trang")
                try:
                    lua_chon = int(input("Vui lòng chọn cột cần sửa: "))
                except ValueError:
                    print("Lỗi nhập!\nVui lòng làm lại")
                else:
                    if lua_chon == 1:
                        nhap_sach = input("Nhập tên: ")
                        if nhap_sach == "" :
                            print("Lỗi tên sách không được để trống. Vui lòng làm lại!!")
                            return self.sua_sach()
                        elif len(nhap_sach)>30:
                            print("Lỗi tiêu đề sách quá dài (quá 30 chữ). Vui lòng làm lại!!")
                            return self.sua_sach()
                        else:
                            self.dictBook[idsach]['ten_sach'] = nhap_sach
                            print("Đã cập nhật thành công!\n")
                    elif lua_chon == 2:
                        nhap_tg = input("Nhập tên tác giả: ")
                        self.dictBook[idsach]['tac_gia'] = nhap_tg
                        print("Đã cập nhật thành công!\n")
                    elif lua_chon == 3:
                        nhap_nxb = input("Nhập NXB: ")
                        self.dictBook[idsach]['nxb'] = nhap_nxb
                        print("Đã cập nhật thành công!\n")
                    elif lua_chon == 4:
                        nhap_nam = input("Nhập năm xuất bản: ")
                        self.dictBook[idsach]['nam_xb'] = nhap_nam
                        print("Đã cập nhật thành công!\n")
                    elif lua_chon == 5:
                        nhap_price = input("Nhập giá sách: ")
                        self.dictBook[idsach]['price'] = nhap_price
                        print("Đã cập nhật thành công!\n")
                    elif lua_chon == 6:
                        nhap_pages = input("Nhập số trang: ")
                        self.dictBook[idsach]['so_trang'] = nhap_pages
                        print("Đã cập nhật thành công!\n")
                    else:
                        print("Lựa chọn đó không tồn tại!")
        else:
            print("ID sách không tìm thấy")
            
    # Hàm xóa sách thư viện
    def xoa_sach(self):
        idsach = input("Nhập ID sách cần xóa: ")
        if idsach in self.dictBook.keys():
            del self.dictBook[idsach]
            print("Xóa thành công!!")
            
            with open("listbook.txt","r",encoding="utf8") as lbxs:
                lbookxc = lbxs.readlines()
            lbxs.close()
            id = int(idsach)-1
            del lbookxc[id]
            l=open("listbook.txt","w+",encoding="utf8")
            for line in lbookxc:
                l.write(line)
            l.close()
        else:
            print("ID sách không tìm thấy")
            
    # Hàm tim kiếm sách theo id
    def tim_sach_theo_id(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
            print ("{:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12} {:<20} {:<10} {:<15}"
                .format('Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng','Người thuê','SĐT','Ngày thuê'))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print ("{:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12} {:<20} {:<10} {:<15}"
                .format(self.dictBook[idsach]['ten_sach'],
                        self.dictBook[idsach]['tac_gia'],
                        self.dictBook[idsach]['nxb'],
                        self.dictBook[idsach]['nam_xb'],
                        self.dictBook[idsach]['price'],
                        self.dictBook[idsach]['so_trang'],
                        self.dictBook[idsach]['status'],
                        self.dictBook[idsach]['nguoi_thue'],
                        self.dictBook[idsach]['sdt'],
                        self.dictBook[idsach]['ngay_thue']))
        else:
            print("ID sách không tìm thấy")
    
    # Hàm tim kiếm sách theo tên
    def tim_sach_theo_ten(self):
        nhap_khoa = input("Nhập tên sách cần tìm: ").upper()
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                    .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        dem=0
        for key,value in self.dictBook.items():
            resultfor = value.get('ten_sach')
            if nhap_khoa in resultfor.upper() :
                print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                    .format(key,self.dictBook[key]['ten_sach'],
                            self.dictBook[key]['tac_gia'],
                            self.dictBook[key]['nxb'],
                            self.dictBook[key]['nam_xb'],
                            self.dictBook[key]['price'],
                            self.dictBook[key]['so_trang'],
                            self.dictBook[key]['status']))
                dem+=1
                # print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"]")
            
        else:
            print("Có {} kết quả thỏa mãn yêu cầu tìm kiếm!".format(dem))
            
    # Hàm sắp xếp id giảm dần
    def sap_xep_sach_theo_id_giam_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        for key,value in sorted(self.dictBook.items(),reverse=True):
            print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format(key,
                        self.dictBook[key]['ten_sach'],
                        self.dictBook[key]['tac_gia'],
                        self.dictBook[key]['nxb'],
                        self.dictBook[key]['nam_xb'],
                        self.dictBook[key]['price'],
                        self.dictBook[key]['so_trang'],
                        self.dictBook[key]['status']))
    
    #Hàm sắp xếp theo tên sách (A-Z)
    def sap_xep_sach_theo_ten(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        res = OrderedDict(sorted(self.dictBook.items(),key=lambda x:x[1]['ten_sach'],reverse= False))
        for key,value in res.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
            .format(key,value.get("ten_sach"),
                    value.get("tac_gia"),value.get("nxb"),
                    value.get("nam_xb"),value.get("price"),
                    value.get("so_trang"),value.get("status")))
    
    # Hàm sắp xếp theo năm XB (giảm dần)
    def sap_xep_sach_theo_nam_xb_giam_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        res = OrderedDict(sorted(self.dictBook.items(),key=lambda x:x[1]['nam_xb'],reverse= True))
        for key,value in res.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
            .format(key,value.get("ten_sach"),
                    value.get("tac_gia"),value.get("nxb"),
                    value.get("nam_xb"),value.get("price"),
                    value.get("so_trang"),value.get("status")))
    
    # Hàm sắp xếp theo năm xb tăng dần
    def sap_xep_sach_theo_nam_xb_tang_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        res = OrderedDict(sorted(self.dictBook.items(),key=lambda x:x[1]['nam_xb'],reverse= False))
        for key,value in res.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
            .format(key,value.get("ten_sach"),
                    value.get("tac_gia"),value.get("nxb"),
                    value.get("nam_xb"),value.get("price"),
                    value.get("so_trang"),value.get("status")))
    
    # Hàm sắp xếp theo năm xb tăng dần
    def sap_xep_sach_theo_price_giam_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        res = OrderedDict(sorted(self.dictBook.items(),key=lambda x:x[1]['price'],reverse= True))
        for key,value in res.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
            .format(key,value.get("ten_sach"),
                    value.get("tac_gia"),value.get("nxb"),
                    value.get("nam_xb"),value.get("price"),
                    value.get("so_trang"),value.get("status")))
    
    # Hàm sắp xếp theo năm xb tăng dần
    def sap_xep_sach_theo_price_tang_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        print ("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
                .format('ID','Tên sách','Tác giả','NXB','Năm XB','Giá','Số trang','Tình trạng'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        res = OrderedDict(sorted(self.dictBook.items(),key=lambda x:x[1]['price'],reverse= False))
        for key,value in res.items():
            print("{:<5} {:<35} {:<20} {:<15} {:<10} {:<15} {:<10} {:<12}"
            .format(key,value.get("ten_sach"),
                    value.get("tac_gia"),value.get("nxb"),
                    value.get("nam_xb"),value.get("price"),
                    value.get("so_trang"),value.get("status")))
    
    # Kiểm tra sách đã thuê ở thư viên
    def kiem_tra_sach_da_thue(self):
        print ("{:<5} {:<35} {:<20} {:<15} {:<15}"
                .format('ID','Tên sách','Tên người thuê','Số ĐT','Ngày thuê'))
        print("---------------------------------------------------------------------------------------------------------------------------")
        for key,value in self.dictBook.items():
            if value.get('status') != "Có sẵn":
                print ("{:<5} {:<35} {:<20} {:<15} {:<15}"
                    .format(key,
                            self.dictBook[key]['ten_sach'],
                            self.dictBook[key]['nguoi_thue'],
                            self.dictBook[key]['sdt'],
                            self.dictBook[key]['ngay_thue']))
                # print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"] - <",value.get("nguoi_thue"),"> - ",value.get("ngay_thue"))

    # Hàm xử lý cho thuê sách  
    def thue_sach(self):
        idsach = input("Nhập ID sách cần thuê: ")
        current_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if idsach in self.dictBook.keys():
            if not self.dictBook[idsach]['status'] == 'Có sẵn' :
                print(f"Sách này đã được thuê bởi {self.dictBook[idsach]['nguoi_thue']} vào {self.dictBook[idsach]['ngay_thue']}")
            elif self.dictBook[idsach]['status'] == 'Có sẵn' :
                nhap_ten = input("Nhập tên: ")
                nhap_sdt = input("Nhập SĐT: ")
                self.dictBook[idsach]['nguoi_thue'] = nhap_ten
                self.dictBook[idsach]['sdt'] = nhap_sdt
                self.dictBook[idsach]['ngay_thue'] = current_day
                self.dictBook[idsach]['status'] = 'Đã thuê'
                print("Đã thuê sách thành công!\n")
        else:
            print("ID sách không tìm thấy")
            
    # Hàm xử lý trả sách thư viên
    def tra_sach(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
                self.dictBook[idsach]['nguoi_thue'] = ''
                self.dictBook[idsach]['sdt'] = ''
                self.dictBook[idsach]['ngay_thue'] = ''
                self.dictBook[idsach]['status'] = 'Có sẵn'
                print("Đã trả sách thành công!\n")
        else:
            print("ID sách không tìm thấy")
            

# if __name__ == "__main__":  
#     lbb = Library("listbook.txt")
    # lbb.hien_thi()
    # lbb.them_sach()
    # lbb.sua_sach()
    # lbb.hien_thi()
    # lbb.tra_sach()
    # lbb.thue_sach()
    # lbb.thue_sach()
    # lbb.hien_thi()
    # lbb.tra_sach()
    # lbb.hien_thi()
    # lbb.tim_sach_theo_id()
    # lbb.tim_sach_theo_ten()
    # lbb.sua_sach()
    # lbb.hien_thi()
    # lbb.kiem_tra_sach_da_thue()
    # lbb.sap_xep_sach_theo_id_giam_dan()
    # lbb.sap_xep_sach_theo_ten()
    # lbb.sap_xep_sach_theo_nam_xb_giam_dan()
    # lbb.xoa_sach()
    # lbb.hien_thi()