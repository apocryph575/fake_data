from faker import Faker
import sqlite3


def get_data():
    fake = Faker('pl_PL')
    name = fake.name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=55)
    address = fake.address().replace('\n', ', ')
    email = fake.email(domain='gmail.com')
    phone = fake.phone_number()
    card = fake.credit_card_number()
    company = fake.company()
    job = fake.job()
    return [name, dob, address, email, phone, card, job, company]


def main():
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        name text,
        birthdays text,
        address text,
        phone integer,
        card integer,
        email text,
        job text,
        company text
    )""")

    for i in range(10):
        info = get_data()
        c.execute(f"INSERT INTO users (name,birthdays,address,phone,card,email,job,company) VALUES (?,?,?,?,?,?,?,?)", info)


    c.execute("SELECT * FROM users")
    print(c.fetchall())
    db.commit()
    db.close()


if __name__ == "__main__":
    main()