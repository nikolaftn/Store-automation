CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    order_number VARCHAR(50),
    customer_id INTEGER,
    status VARCHAR(30),

    subtotal NUMERIC(12, 2),
    shipping NUMERIC(12, 2),
    tax NUMERIC(12, 2),
    discount NUMERIC(12, 2),
    total NUMERIC(12, 2),
    currency VARCHAR(10),

    payment_method VARCHAR(50),
    shipping_method VARCHAR(50),
    tracking_number VARCHAR(100),

    created_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ,
    placed_at TIMESTAMPTZ,
    paid_at TIMESTAMPTZ,
    shipped_at TIMESTAMPTZ,
    delivered_at TIMESTAMPTZ,

    shipping_address JSONB,
    notes TEXT
);