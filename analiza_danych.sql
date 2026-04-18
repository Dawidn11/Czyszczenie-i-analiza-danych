CREATE TABLE sprzedaz_tabela AS
SELECT
    s.ID,
    s.Data,
    s.Produkt,
    p.Kategoria,
    p.Producent,
    s.Cena,
    s.Ilosc,
    s.Przychod,
    s.Kraj,
    p.Marza_Procent
FROM clean_sales s
INNER JOIN produkty_info p ON s.Produkt = p.Produkt;

SELECT 
    Kraj, 
    SUM(Przychod) AS suma_przychodow
FROM sprzedaz_tabela
GROUP BY Kraj 
ORDER BY suma_przychodow DESC;

SELECT 
    Produkt, 
    COUNT(*) AS ilosc_sprzedazy
FROM sprzedaz_tabela
GROUP BY Produkt
ORDER BY ilosc_sprzedazy DESC;

SELECT 
    Produkt, 
    Przychod
FROM sprzedaz_tabela
WHERE Przychod > (SELECT AVG(Przychod) FROM sprzedaz_tabela)
ORDER BY Przychod DESC;

SELECT
    Data,
    SUM(Ilosc) AS Ilosc_sprzedazy
FROM sprzedaz_tabela
GROUP BY Data
ORDER BY Ilosc_sprzedazy DESC
LIMIT 5;

SELECT
    Kraj,
    ROUND(SUM(Przychod * (Marza_Procent / 100)), 2) AS Zysk
FROM sprzedaz_tabela
GROUP BY Kraj
ORDER BY Zysk DESC;

SELECT 
    Kraj,
    SUM(Przychod) AS suma_przychodow
FROM sprzedaz_tabela
GROUP BY Kraj
HAVING SUM(Przychod) > 5000
ORDER BY suma_przychodow DESC;
