import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

def test_fibonacci_small():
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

def test_bank_account_init_and_balance():
    acc = BankAccount("Alice", 100)
    assert acc.balance() == 100
    with pytest.raises(ValueError):
        BankAccount("", 50)
    with pytest.raises(ValueError):
        BankAccount("Bob", -10)

def test_deposit():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.balance() == 150
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_withdraw():
    acc = BankAccount("Alice", 100)
    acc.withdraw(50)
    assert acc.balance() == 50
    with pytest.raises(ValueError):
        acc.withdraw(0)
    with pytest.raises(ValueError):
        acc.withdraw(-10)
    with pytest.raises(ValueError):
        acc.withdraw(100)

def test_transfer_to():
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)
    acc1.transfer_to(acc2, 30)
    assert acc1.balance() == 70
    assert acc2.balance() == 80

    with pytest.raises(ValueError):
        acc1.transfer_to("NotAnAccount", 10)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, 0)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, -10)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, 1000)

def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_prime_factors_invalid():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-5)

def test_moving_average_basic():
    vals = [1, 2, 3, 4, 5]
    assert moving_average(vals, 1) == [1, 2, 3, 4, 5]
    assert moving_average(vals, 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average(vals, 3) == [2.0, 3.0, 4.0]

def test_moving_average_invalid():
    with pytest.raises(ValueError):
        moving_average([1,2,3], 0)
    with pytest.raises(ValueError):
        moving_average([1,2,3], -1)

def test_moving_average_window_larger_than_list():
    assert moving_average([1,2], 3) == []

def test_normalize_scores_basic():
    scores = [0, 50, 100]
    normalized = normalize_scores(scores)
    assert normalized == [0.0, 0.5, 1.0]

def test_normalize_scores_invalid():
    with pytest.raises(ValueError):
        normalize_scores([-1, 50, 70])
    with pytest.raises(ValueError):
        normalize_scores([10, 150])
