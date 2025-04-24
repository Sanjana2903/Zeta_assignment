"""
Problem 4: Backend API Design - Rate Limiting for Banking Transactions

This script implements a basic rate limiter using the Sliding Window Log algorithm.
Each user is limited to a maximum of 5 requests per second.

Approach:
- For each user, we maintain a deque of timestamps.
- When a request arrives, we:
    1. Remove outdated timestamps.
    2. Check if the user has made fewer than 5 requests in the last 1 second.
    3. Allow or deny the request accordingly.

Author: Sanjana Bathula
Date: 2025-04-24
"""

from collections import defaultdict, deque
from time import time, sleep

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int = 5, interval: float = 1.0):
        """
        Initialize the rate limiter.

        Args:
            max_requests (int): Max allowed requests per user in the interval.
            interval (float): Time window in seconds.
        """
        self.max_requests = max_requests
        self.interval = interval
        self.user_requests = defaultdict(deque)

    def allow_request(self, user_id: str) -> bool:
        """
        Determine whether a request should be allowed for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if allowed, False if rate-limited.
        """
        current_time = time()
        requests = self.user_requests[user_id]

        # Remove outdated requests outside the time window
        while requests and current_time - requests[0] > self.interval:
            requests.popleft()

        if len(requests) < self.max_requests:
            requests.append(current_time)
            return True
        else:
            return False


if __name__ == "__main__":
    # Example test case
    rate_limiter = SlidingWindowRateLimiter(max_requests=5, interval=1)

    user = "sanjana"

    print(f"\nSimulating 7 requests in quick succession for user: {user}")
    for i in range(7):
        result = rate_limiter.allow_request(user)
        print(f"Request {i + 1}: {'✅ Allowed' if result else '❌ Rate Limited'}")
        sleep(0.1)  # simulate short delay between requests

    print("\nWaiting 1.2 seconds to reset the window...\n")
    sleep(1.2)

    for i in range(3):
        result = rate_limiter.allow_request(user)
        print(f"Request {i + 8}: {'✅ Allowed' if result else '❌ Rate Limited'}")
