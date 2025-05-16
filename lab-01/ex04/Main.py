from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("******************************MENU*****************************")
    print("**   1. Them sinh vien.                                      **")
    print("**   2. Cap nhat thong tin sinh vien theo ID.                **")
    print("**   3. Xoa sinh vien theo ID.                               **")
    print("**   4. Tim kiem sinh vien theo ten                          **")
    print("**   5. Sap xep danh sach sinh vien theo diem trung binh.    **")
    print("**   6. Sap xep danh sach sinh vien theo ten chuyen nganh.   **")
    print("**   7. Hien thi danh sach sinh vien.                        **")
    print("**   0. Thoat.                                               **")
    print("***************************************************************")
    key = int(input("Moi ban chon: "))
    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")

    elif key == 2:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien theo ID.")
            ID = int(input("\nNhapID: "))
            qlsv.updateSinhVien(ID)
            print("\nCap nhat thong tin sinh vien thanh cong!")
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 3:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien theo ID.")
            ID = int(input("\nNhapID: "))
            if(qlsv.deleteByID(ID)):
                    print("\nSinh vien co ID = ", ID, " da bi xoa.")
            else:
                print("\nSinh vien co ID = ", ID, " khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 4:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("\nNhap ten sinh vien: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 5:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep danh sach sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 6:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep danh sach sinh vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 7:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu!")