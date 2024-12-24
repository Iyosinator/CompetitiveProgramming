class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customers in accounts:
            customer_wealth = sum(customers)
            max_wealth = max(max_wealth,customer_wealth)
        return max_wealth