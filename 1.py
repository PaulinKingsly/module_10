import unittest

num = [56, 9, 11, 2]

def create_max_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x * 3, reverse=True)
    return int(''.join(nums))
max_number = create_max_number(num)
print(max_number)

class TestCreateMaxNumber(unittest.TestCase):
    def test_create_max_number(self):
        nums = [56, 9, 11, 2]
        expected_result = 956211
        result = create_max_number(nums)
        self.assertEqual(result, expected_result)

    def test_create_max_number_zero(self):
        nums = [0]
        expected_result = 0
        result = create_max_number(nums)
        self.assertEqual(result, expected_result)

    def test_create_max_number_single(self):
        nums = [1, 2, 3, 6]
        expected_result = 6321
        result = create_max_number(nums)
        self.assertEqual(result, expected_result)

    def test_create_max_number_triple(self):
        nums = [333, 999, 777]
        expected_result = 999777333
        result = create_max_number(nums)
        self.assertEqual(result, expected_result)


    def test_create_max_number_str(self):
        nums = [56, 9, 'str', 2]
        with self.assertRaises(TypeError):
            create_max_number(nums)

if __name__ == '__main__':
    unittest.main()








