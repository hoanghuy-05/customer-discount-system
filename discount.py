# Tổng tiền tối thiểu để khách hàng được giảm giá
MIN_TOTAL_FOR_DISCOUNT = 50_000_000

# Tỷ lệ giảm giá cho khách hàng thân thiết là 10%
DISCOUNT_RATE = 0.1

# Hàm tính tỷ lệ giảm giá
# previous_total: tổng giá trị mua hàng trước đó trong năm
# current_order: giá trị đơn hàng hiện tại
def calculate_discount(previous_total, current_order=0):

    # Kiểm tra điều kiện tổng tiền mua hàng để được giảm giá
    if previous_total >= MIN_TOTAL_FOR_DISCOUNT:

        # Nếu thỏa mãn điều kiện thì trả về tỷ lệ giảm giá 10%
        return DISCOUNT_RATE

    # Nếu chưa thỏa mãn điều kiện thì không được giảm giá
    return 0

test_cases = [
    ("TC01", 60_000_000, 2_000_000, 0.1),
    ("TC02", 30_000_000, 2_000_000, 0),
    ("TC03", 49_000_000, 2_000_000, 0.1),
]

for tc, previous_total, current_order, expected in test_cases:
    actual = calculate_discount(previous_total, current_order)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print("--------------------------------")
    print(f"{tc}")
    print(f"Tong mua truoc day: {previous_total}")
    print(f"Don hang moi: {current_order}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Status: {status}")
