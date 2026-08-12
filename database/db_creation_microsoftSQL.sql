-- Create Database
CREATE DATABASE sonar_store;
GO

USE sonar_store;
GO

-----------------------------------------------------
-- T-Shirts Table
-----------------------------------------------------
CREATE TABLE t_shirts
(
    t_shirt_id INT IDENTITY(1,1) PRIMARY KEY,

    brand VARCHAR(20) NOT NULL
        CHECK (brand IN ('Van Huesen', 'Levi', 'Nike', 'Adidas')),

    color VARCHAR(20) NOT NULL
        CHECK (color IN ('Red', 'Blue', 'Black', 'White')),

    size VARCHAR(5) NOT NULL
        CHECK (size IN ('XS', 'S', 'M', 'L', 'XL')),

    price INT NOT NULL
        CHECK (price BETWEEN 10 AND 50),

    stock_quantity INT NOT NULL,

    CONSTRAINT UQ_Brand_Color_Size
        UNIQUE (brand, color, size)
);
GO

-----------------------------------------------------
-- Discounts Table
-----------------------------------------------------
CREATE TABLE discounts
(
    discount_id INT IDENTITY(1,1) PRIMARY KEY,

    t_shirt_id INT NOT NULL,

    pct_discount DECIMAL(5,2)
        CHECK (pct_discount BETWEEN 0 AND 100),

    CONSTRAINT FK_Discounts_TShirts
        FOREIGN KEY (t_shirt_id)
        REFERENCES t_shirts(t_shirt_id)
);
GO

-----------------------------------------------------
-- Populate All 80 Unique T-Shirts
-----------------------------------------------------
;WITH Brands AS
(
    SELECT 'Van Huesen' AS brand
    UNION ALL SELECT 'Levi'
    UNION ALL SELECT 'Nike'
    UNION ALL SELECT 'Adidas'
),
Colors AS
(
    SELECT 'Red' AS color
    UNION ALL SELECT 'Blue'
    UNION ALL SELECT 'Black'
    UNION ALL SELECT 'White'
),
Sizes AS
(
    SELECT 'XS' AS size
    UNION ALL SELECT 'S'
    UNION ALL SELECT 'M'
    UNION ALL SELECT 'L'
    UNION ALL SELECT 'XL'
)
INSERT INTO t_shirts
(
    brand,
    color,
    size,
    price,
    stock_quantity
)
SELECT
    b.brand,
    c.color,
    s.size,

    -- Random price between 10 and 50
    10 + ABS(CHECKSUM(NEWID())) % 41,

    -- Random stock between 10 and 100
    10 + ABS(CHECKSUM(NEWID())) % 91

FROM Brands b
CROSS JOIN Colors c
CROSS JOIN Sizes s;
GO

-----------------------------------------------------
-- Sample Discounts
-----------------------------------------------------
INSERT INTO discounts
(
    t_shirt_id,
    pct_discount
)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);
GO

-----------------------------------------------------
-- Verification
-----------------------------------------------------
SELECT COUNT(*) AS Total_TShirts
FROM t_shirts;
GO

SELECT TOP 20 *
FROM t_shirts;
GO

SELECT *
FROM discounts;
GO