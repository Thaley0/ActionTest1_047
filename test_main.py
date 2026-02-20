from main import add

def test_add():
    assert add(2, 3) == 5  # Normal case
    assert add(-1, 3) == 0  # Case where one input is negative
    assert add(0, 0) == 0  # Edge case: both inputs are zero

# Run the tests
test_add()
print("All tests passed!")
