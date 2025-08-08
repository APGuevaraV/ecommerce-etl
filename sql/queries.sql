-- 1. Total de ventas por país
SELECT Country, SUM(Quantity * UnitPrice) AS TotalSales
FROM orders
GROUP BY Country
ORDER BY TotalSales DESC;

-- 2. Top 10 productos más vendidos
SELECT Description, SUM(Quantity) AS TotalQuantity
FROM orders
GROUP BY Description
ORDER BY TotalQuantity DESC
LIMIT 10;

-- 3. Ventas mensuales
SELECT 
    strftime('%Y-%m', InvoiceDate) AS Month,
    SUM(Quantity * UnitPrice) AS MonthlySales
FROM orders
GROUP BY Month
ORDER BY Month;

-- 4. Clientes con mayor gasto total
SELECT CustomerID, SUM(Quantity * UnitPrice) AS TotalSpent
FROM orders
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 10;

-- 5. Precio promedio por producto
SELECT Description, AVG(UnitPrice) AS AvgPrice
FROM orders
GROUP BY Description
ORDER BY AvgPrice DESC;
