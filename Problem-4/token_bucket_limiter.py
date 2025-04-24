"""
Problem 4: Backend API Design - Rate Limiting using Token Bucket

This implementation allows each user up to 5 requests per second using the Token Bucket algorithm.

How it works:
- Each user has a "bucket" with max 5 tokens.
- A request consumes a token.
- Tokens are replenished over time (1 token every 0.2 seconds).

Author: Sanjana Bathula
Date: 2025-04-24
"""

import time
from collections import defaultdict

class TokenBucketRateLimiter:
    def __init__(self, max_tokens=5, refill_rate=5):
        """
        Initialize the token bucket rate limiter.

        Args:
            max_tokens (int): Maximum tokens (capacity) per user.
            refill_rate (int): Tokens replenished per second.
        """
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate  # tokens per second
        self.users = defaultdict(lambda: {"tokens": max_tokens, "last_checked": time.time()})

    def allow_request(self, user_id: str) -> bool:
        current_time = time.time()
        user = self.users[user_id]

        elapsed = current_time - user["last_checked"]
        # Calculate how many tokens to add
        refill = elapsed * self.refill_rate
        user["tokens"] = min(self.max_tokens, user["tokens"] + refill)
        user["last_checked"] = current_time

        if user["tokens"] >= 1:
            user["tokens"] -= 1
            return True
        return False


if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(max_tokens=5, refill_rate=5)
    user = "sanjana"

    print(f"\nSimulating 7 requests in quick succession for user: {user}")
    for i in range(7):
        result = limiter.allow_request(user)
        print(f"Request {i + 1}: {'✅ Allowed' if result else '❌ Rate Limited'}")
        time.sleep(0.1)

    print("\nWaiting 1.2 seconds to refill tokens...\n")
    time.sleep(1.2)

    for i in range(3):
        result = limiter.allow_request(user)
        print(f"Request {i + 8}: {'✅ Allowed' if result else '❌ Rate Limited'}")
