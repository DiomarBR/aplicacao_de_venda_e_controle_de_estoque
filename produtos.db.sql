BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "produtos" (
	"Codigo de barras"	NUMERIC,
	"Codigo de barras  alternativo"	NUMERIC,
	"Nome do produto"	TEXT,
	"Valor do produto"	NUMERIC,
	"Quantidade do produto"	NUMERIC
);
CREATE TABLE IF NOT EXISTS "Vendas" (
	"Codigo do produto "	NUMERIC,
	"Codigo02 do produto"	NUMERIC,
	"Nome do produto"	TEXT,
	"Valor do produto"	NUMERIC,
	"Quantodade de produtos vendidos"	NUMERIC,
	"Valor total dos produtos "	NUMERIC
);
INSERT INTO "produtos" ("Codigo de barras","Codigo de barras  alternativo","Nome do produto","Valor do produto","Quantidade do produto") VALUES (62662999,62626262,'Pao',21,25);
COMMIT;
