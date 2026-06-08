input_name = input("Nhập tên khách hàng: ")
input_name_product = input("Nhập tên sản phẩm: ")
input_price = input("Nhập đơn giá sản phẩm: ")
if not input_price.isdigit():
    print("Dơn giá sản phẩm phải là số và phải là số nguyên")
else:
    input_price = int(input_price)
    input_quantity = input("Nhập số lượng mua: ")
    if not input_quantity.isdigit:
        print("Số lượng mua phải là số và là phải số nguyên")
    else:
        input_quantity = int(input_quantity)
        amount_due = input_price * input_quantity
        if amount_due >= 100000:
            discount = amount_due * 0.1
            amount_after_discount = amount_due - discount
            print("===== HÓA ĐƠN ====="
                f"\nKhách hàng: {input_name}"
                f"\nSản phẩm: {input_name_product}"
                f"\nĐơn giá: {input_price} VNĐ"
                f"\nSố lượng: {input_quantity}"
                f"\nThành tiền: {amount_due} VNĐ"
                f"\nSố tiền sau giảm giá: {int(amount_after_discount)} VNĐ"
                "\n==================")
        else:
            print("===== HÓA ĐƠN ====="
                f"\nKhách hàng: {input_name}"
                f"\nSản phẩm: {input_name_product}"
                f"\nĐơn giá: {input_price} VNĐ"
                f"\nSố lượng: {input_quantity}"
                f"\nThành tiền: {amount_due} VNĐ"
                f"\nSố tiền sau giảm giá: Không được giảm giá"
                "\n==================")