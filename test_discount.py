# Import hàm calculate_discount từ file discount.py để kiểm thử
from discount import calculate_discount

# Kiểm tra khách hàng đã mua trên 50 triệu
def test_vip_customer():

    # Kỳ vọng khách hàng mua 60 triệu sẽ được giảm giá 10%
    assert calculate_discount(60_000_000) == 0.1

# Kiểm tra khách hàng chưa đạt 50 triệu
def test_normal_customer():

    # Kỳ vọng khách hàng mua 30 triệu sẽ không được giảm giá
    assert calculate_discount(30_000_000) == 0

# Test case TC01: tổng mua trước đó là 60 triệu, đơn hàng mới là 2 triệu
def test_tc01():
    # Tổng sau khi mua là 62 triệu nên được giảm giá 10%
    assert calculate_discount(60_000_000, 2_000_000) == 0.1

# Test case TC02: tổng mua trước đó là 30 triệu, đơn hàng mới là 2 triệu
def test_tc02():
    # Tổng sau khi mua là 32 triệu nên không được giảm giá
    assert calculate_discount(30_000_000, 2_000_000) == 0

# Test case TC03: tổng mua trước đó là 49 triệu, đơn hàng mới là 2 triệu
def test_tc03():
    # Tổng sau khi mua là 51 triệu nên được giảm giá 10%
    assert calculate_discount(49_000_000, 2_000_000) == 0.1