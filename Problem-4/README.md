## 🔁 Trade-Offs: Sliding Window vs Token Bucket

| Feature              | Sliding Window Log               | Token Bucket                            |
|----------------------|----------------------------------|------------------------------------------|
| Precision            | High (tracks exact timestamps)   | Approximate (token-based)               |
| Memory Efficiency    | Lower (stores timestamps)        | Higher (stores only token count & time) |
| Burst Handling       | Harsh cut-off                    | Smooth burst tolerance                  |
| Scalability          | Less scalable at high traffic    | More scalable for large user base       |
| Implementation Ease  | Simple and intuitive             | Slightly more complex (timing logic)    |

---

## 🧪 Run Both

python rate_limiter.py         # Sliding Window
//
python token_bucket_limiter.py # Token Bucket
