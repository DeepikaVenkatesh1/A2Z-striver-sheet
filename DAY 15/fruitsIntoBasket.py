def total_fruit(fruits):
    basket = {}  # fruit_type → count in window
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1

        
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len