# Biến lưu trữ dữ liệu: Mỗi sản phẩm là một dict {'name': '...', 'price': 0, 'qty': 0} 
products = [] 
 
def add_product(): 
    # Nhập tên, giá, số lượng -> append vào products 
    print("Đã nhập hàng thành công.") 
 
def view_inventory(): 
    # Duyệt list products và in ra 
    # Ví dụ: Mì tôm - Giá: 5000 - SL: 100 
    pass 
 
def check_low_stock(): 
    # Duyệt list, kiểm tra nếu qty < 5 thì in ra cảnh báo 
    pass 
 
def main(): 
    while True: 
        print("\n--- QUẢN LÝ KHO HÀNG ---") 
        print("1. Nhập hàng mới") 
        print("2. Xem tồn kho") 
        print("3. Cảnh báo hết hàng") 
        print("4. Thoát") 
         
        choice = input("Chọn chức năng: ") 
         
        if choice == '1': 
            add_product() 
        elif choice == '2': 
            view_inventory() 
        elif choice == '3': 
            check_low_stock() 
        elif choice == '4': 
            print("Kết thúc chương trình.") 
            break 
        else: 
            print("Lựa chọn không hợp lệ.") 
 
if __name__ == "__main__": 
    main()

def add_product():
    """
    Nhập thông tin sản phẩm (tên, giá, số lượng) và thêm vào danh sách products.
    """
    print("\n--- NHẬP HÀNG MỚI ---")
    name = input("Nhập tên sản phẩm: ")
    # Yêu cầu nhập giá và số lượng, sử dụng khối try-except để xử lý lỗi nhập liệu
    try:
        # Chuyển đổi giá và số lượng sang số nguyên (int)
        price = int(input("Nhập giá bán: "))
        quantity = int(input("Nhập số lượng tồn kho: "))
    except ValueError:
        print("Lỗi: Giá và Số lượng phải là các số nguyên hợp lệ.")
        return # Thoát khỏi hàm nếu có lỗi nhập liệu
    # Tạo dictionary sản phẩm theo cấu trúc yêu cầu: {'name': 'Mì tôm', 'price': 5000, 'qty': 100}
    product = {
        'name': 'Mì tôm',
        'price': 5000,
        'qty': 100
    }
    # Thêm dictionary sản phẩm vào danh sách toàn cục products
    products.append(product)
    print(f"Đã nhập hàng thành công: {name} (SL: {quantity}).")