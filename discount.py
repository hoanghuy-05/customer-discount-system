# Tổng tiền tối thiểu để khách hàng được giảm giá
MIN_TOTAL_FOR_DISCOUNT = 50_000_000

# Tỷ lệ giảm giá cho khách hàng thân thiết là 10%
DISCOUNT_RATE = 0.1


# Hàm tính tỷ lệ giảm giá
# previous_total: tổng giá trị mua hàng trước đó trong năm
# current_order: giá trị đơn hàng hiện tại, mặc định là 0 nếu không truyền vào
def calculate_discount(previous_total, current_order=0):

    # Tính tổng giá trị mua hàng sau khi cộng thêm đơn hàng hiện tại
    total_purchase = previous_total + current_order

    # Nếu tổng giá trị mua hàng đạt từ 50 triệu trở lên
    if total_purchase >= MIN_TOTAL_FOR_DISCOUNT:

        # Trả về tỷ lệ giảm giá 10%
        return DISCOUNT_RATE

    # Nếu chưa đạt 50 triệu thì không được giảm giá
    return 0