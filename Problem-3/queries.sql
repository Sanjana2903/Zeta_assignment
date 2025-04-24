CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(64) UNIQUE NOT NULL,
    balance DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    last_updated TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(64) NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('credit', 'debit')),
    created_at TIMESTAMP DEFAULT NOW()
);
