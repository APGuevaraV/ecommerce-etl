-- Creación de la tabla orders
CREATE TABLE IF NOT EXISTS orders (
    InvoiceNo TEXT NOT NULL,
    StockCode TEXT NOT NULL,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice REAL,
    CustomerID TEXT,
    Country TEXT
);
