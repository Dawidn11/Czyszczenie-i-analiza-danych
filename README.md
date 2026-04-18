# Czyszczenie-i-analiza-danych
Czyszczenie "brudnych" danych w pythonie z wykorzystaniem bilbioteki Pandas oraz ich analiza w MySQL.

Do czyszczenia danych użyłem biblioteki Pandas w pythonie.
Surowe dane zawierały błędy, które uniemożliwiały bezpośrednią analizę:
- Niejednolite nazewnictwo
- Błędy w formatach
- Brakujące dane
 Po zaimportowaniu wyczyszczonych danych do MySQL przeprowadziłem analize przy użyciu:
- JOINs: Połączenie dwóch tabel.
- Subqueries: Wyłonienie transakcji o przychodzie powyżej średniej.
- Agregacje: Zestawienia przychodów i zysków netto z podziałem na kraje i kategorie.
- Flitering (HAVING): Selekcja rynków o najwyższym priorytecie (obrót > 5000).
