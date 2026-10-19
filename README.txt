API server — tuđi sistem koji omogućava pristup podacima.

API endpoint (link) — konkretna adresa preko koje tražiš podatke, npr. https://api.sondahub.com/v1/store/orders.

API client (tvoj Python kod) — šalje zahtev na tu adresu i preuzima porudžbine.


# https://api.sondahub.com/v1/store/orders


requests - python biblioteka za slanje HTTP zahteva drugim serverima.

Još jedna stvar: shipping_address je objekat, a kolona je JSONB. 
Ako ga prosleđuješ direktno, možda će biti potrebno da ga pretvoriš u JSON format pomoću psycopg.types.json.Jsonb.

cursor.fetchall() uzima sve redove koje je SQL upit pronašao i vraća ih Python-u kao listu.

render_template() je Flask funkcija koja učita HTML fajl iz foldera templates i vrati ga pregledaču.