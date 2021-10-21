import datetime
from os import replace

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
            self.dictBook.update(
                {
                str(id):
                    {
                        'ten_sach':line.replace("\n",""),
                        'nguoi_thue':'',
                        'ngay_thue':'',
                        'status':'Có sẵn'
                    }
                }
            )
            id += 1
    
    def hien_thi(self):
        print("------------------------Danh sách sách thư viên---------------------")
        print("ID","\t", "Tên sách")
        print("--------------------------------------------------------------------")

        for key,value in self.dictBook.items():
            print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"]")


    def them_sach(self):
        new_book = input("Nhập tên sách: ")
        if new_book == "":
            return self.them_sach()
        elif len(new_book)>30:
            print("Tiêu đề sách quá dài (quá 30 chữ)")
            return self.them_sach()
        else:
            with open(self.list_books,"a",encoding="utf8") as nb:
                nb.writelines(f"{new_book}\n")
            self.dictBook.update({
                str(int(max(self.dictBook))+1):
                    {
                        'ten_sach':new_book,
                        'nguoi_thue':'',
                        'ngay_thue':'',
                        'status':'Có sẵn'
                    }
            })
            print(f"{new_book} đã được thêm mới!")
    
    def sua_sach(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
    
            if not self.dictBook[idsach]['status'] == "Có sẵn" :
                print(f"Sách này đang được thuê vui lòng nên chưa cập nhật được!!")
            elif self.dictBook[idsach]['status'] == "Có sẵn" :
                nhap_sach = input("Nhập tên: ")
                if nhap_sach == "" :
                    print("Lỗi tên sách không được để trống. Vui lòng làm lại!!")
                    return self.sua_sach()
                elif len(nhap_sach)>30:
                    print("Lỗi tiêu đề sách quá dài (quá 30 chữ). Vui lòng làm lại!!")
                    return self.sua_sach()
                else:
                    # with open("listbook.txt","r",encoding="utf8") as lbss:
                    #     lbooksc = lbss.readlines()
                    # lbss.close()
                    # ub = open(self.list_books,"a",encoding="utf8")
                    # for line in ub:
                    #     ub.writelines(f"{nhap_sach}\n")

                    self.dictBook[idsach]['ten_sach'] = nhap_sach
                    print("Đã thuê thành công!\n")
        else:
            print("ID sách không tìm thấy")
            
    
    def xoa_sach(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
            del self.dictBook[idsach]
            print("Xóa thành công!!")
            # with open("listbook.txt","r",encoding="utf8") as lbxs:
            #     lbookxc = lbxs.readlines()
            # lbxs.close()
            # id = int(idsach)-1
            # del lbookxc[id]
            # l=open("listbook.txt","w+",encoding="utf8")
            # for line in lbookxc:
            #     l.write(line)
            # l.close()
        else:
            print("ID sách không tìm thấy")
            
    
    def tim_sach_theo_id(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
            print(f"Thông tin sách: {self.dictBook[idsach]['ten_sach']} - [{self.dictBook[idsach]['status']}] {self.dictBook[idsach]['nguoi_thue']} {self.dictBook[idsach]['ngay_thue']}")
        else:
            print("ID sách không tìm thấy")
    
    def tim_sach_theo_ten(self):
        nhap_khoa = input("Nhập tên sách cần tìm: ")
        for key,value in self.dictBook.items():
            if value.get('ten_sach') == nhap_khoa:
                print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"]")
        else:    
            print("Sách bạn tìm không thấy. Vui lòng kiểm tra lại khóa tìm kiếm!")

    def sap_xep_sach_theo_id_giam_dan(self):
        # print(sorted(self.dictBook.items(),reverse=True))
        for key,value in sorted(self.dictBook.items(),reverse=True):
            print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"]")
        
    def kiem_tra_sach_da_thue(self):
        print("------------------------Danh sách sách đã thuê---------------------")
        print("ID","\t", "Tên sách")
        print("--------------------------------------------------------------------")
        for key,value in self.dictBook.items():
            if value.get('status') != "Có sẵn" :
                print(key,"\t",value.get("ten_sach"),"- [",value.get("status"),"] - <",value.get("nguoi_thue"),"> - ",value.get("ngay_thue"))
                
    def thue_sach(self):
        idsach = input("Nhập ID sách: ")
        current_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if idsach in self.dictBook.keys():
            if not self.dictBook[idsach]['status'] == 'Có sẵn' :
                print(f"Sách này đã được thuê bởi {self.dictBook[idsach]['nguoi_thue']} vào {self.dictBook[idsach]['ngay_thue']}")
            elif self.dictBook[idsach]['status'] == 'Có sẵn' :
                nhap_ten = input("Nhập tên: ")
                self.dictBook[idsach]['nguoi_thue'] = nhap_ten
                self.dictBook[idsach]['ngay_thue'] = current_day
                self.dictBook[idsach]['status'] = 'Đã thuê'
                print("Đã thuê thành công!\n")
        else:
            print("ID sách không tìm thấy")
            

    def tra_sach(self):
        idsach = input("Nhập ID sách: ")
        if idsach in self.dictBook.keys():
                self.dictBook[idsach]['nguoi_thue'] = ''
                self.dictBook[idsach]['ngay_thue'] = ''
                self.dictBook[idsach]['status'] = 'Có sẵn'
                print("Đã trả thành công!\n")
        else:
            print("ID sách không tìm thấy")
            

# if __name__ == "__main__":  
#     lbb = Library("listbook.txt")
#     lbb.hien_thi()
    # lbb.them_sach()
    # lbb.thue_sach()
    # lbb.hien_thi()
    # lbb.tra_sach()
    # lbb.thue_sach()
    # lbb.hien_thi()
    # lbb.tim_sach_theo_id()
    # lbb.tim_sach_theo_ten()
    # lbb.sua_sach()
    # lbb.hien_thi()
    # lbb.kiem_tra_sach_da_thue()
    # lbb.sap_xep_sach_theo_id_giam_dan()
    # lbb.xoa_sach()
    # lbb.hien_thi()