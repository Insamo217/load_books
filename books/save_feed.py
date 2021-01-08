import xml.etree.ElementTree as xml
import psycopg2

conn = psycopg2.connect(dbname='books', user='insamo', password='217', host='localhost')
cursor = conn.cursor()

cursor.execute('SELECT id from books_books')
rows = cursor.fetchall()
for row in rows[0]:
    id_book1 = str(row)
for row in rows[1]:
    id_book2 = str(row)

cursor.execute('SELECT title from books_books')
rows = cursor.fetchall()
for row in rows[0]:
    name_book1 = row
for row in rows[1]:
    name_book2 = row

cursor.execute('SELECT description from books_books')
rows = cursor.fetchall()
for row in rows[0]:
    description_book1 = row
for row in rows[1]:
    description_book2 = row

cursor.execute('SELECT price from books_books')
rows = cursor.fetchall()
for row in rows[0]:
    price_book1 = str(row)
for row in rows[0]:
    price_book2 = str(row)

cursor.execute('SELECT photo from books_books')
rows = cursor.fetchall()
for row in rows[0]:
    photo1 = row
for row in rows[0]:
    photo2 = row


def generateXML(filename):
    root = xml.Element('feed')
    root.set('version', '1')
    c1 = xml.Element('offers')
    root.append(c1)

    offer1 = xml.SubElement(c1, 'offer')
    id = xml.SubElement(offer1, 'id')
    id.text = id_book1
    seller = xml.SubElement(offer1, 'seller')
    contacts = xml.SubElement(seller, 'contacts')
    phone = xml.SubElement(contacts, 'phone')
    phone.text = '+7-915-267-03-62'
    locations = xml.SubElement(seller, 'locations')
    location = xml.SubElement(locations, 'location')
    address = xml.SubElement(location, 'address')
    address.text = 'Россия, Ногинск, Белякова 1'
    title = xml.SubElement(offer1, 'title')
    title.text = name_book1
    description = xml.SubElement(offer1, 'description')
    description.text = description_book1
    condition = xml.SubElement(offer1, 'condition')
    condition.text = 'new'
    category = xml.SubElement(offer1, 'category')
    category.text = 'Книги'
    images = xml.SubElement(offer1, 'images')
    images.text = photo1
    price = xml.SubElement(offer1, 'price')
    price.text = price_book1

    offer2 = xml.SubElement(c1, 'offer')
    id = xml.SubElement(offer2, 'id')
    id.text = id_book2
    seller = xml.SubElement(offer2, 'seller')
    contacts = xml.SubElement(seller, 'contacts')
    phone = xml.SubElement(contacts, 'phone')
    phone.text = '+7-915-267-03-62'
    locations = xml.SubElement(seller, 'locations')
    location = xml.SubElement(locations, 'location')
    address = xml.SubElement(location, 'address')
    address.text = 'Россия, Ногинск, Белякова 1'
    title = xml.SubElement(offer2, 'title')
    title.text = name_book2
    description = xml.SubElement(offer2, 'description')
    description.text = 'Срочно продаю книгу'
    condition = xml.SubElement(offer2, 'condition')
    condition.text = 'new'
    category = xml.SubElement(offer2, 'category')
    category.text = 'Книги'
    images = xml.SubElement(offer2, 'images')
    images.text = photo2
    price = xml.SubElement(offer2, 'price')
    price.text = price_book2

    tree = xml.ElementTree(root)
    with open(filename, 'wb') as files:
        tree.write(files, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    generateXML('feed.xml')
