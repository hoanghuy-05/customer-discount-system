# Import hàm calculate_discount từ file discount.py
from discount import calculate_discount

def test_vip_customer():
    # hàm này tương tự assertEqual trong JAVA là kỳ vọng hàm calculate_discount(60000000) phải trả về 0.1
    assert calculate_discount(60_000_000) == 0.1

def test_normal_customer():

    # Kỳ vọng hàm calculate_discount(30000000) phải trả về 0
    assert calculate_discount(30_000_000) == 0

# TC01: Tổng mua trước đây 60 triệu, đơn hàng mới 2 triệu
def test_tc01():

    # Khách hàng đã đạt điều kiện giảm giá
    assert calculate_discount(60_000_000, 2_000_000) == 0.1

# TC02: Tổng mua trước đây 30 triệu, đơn hàng mới 2 triệu
def test_tc02():

    # Khách hàng chưa đạt điều kiện giảm giá
    assert calculate_discount(30_000_000, 2_000_000) == 0

# TC03: Tổng mua trước đây 49 triệu, đơn hàng mới 2 triệu
def test_tc03():

    # Sau đơn hàng mới, khách hàng được kỳ vọng đạt điều kiện giảm giá
    assert calculate_discount(49_000_000, 2_000_000) == 0.1
