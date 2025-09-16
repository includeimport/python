import database

database.create_table_customers()

many_customers = [
                    ('John', 'Elder', 'john@codemy.com'),
                    ('Wes', 'Brown', 'wes@gmail.com'),
                    ('Steph', 'Kuewa', 'steph@gmail.com'),
                    ('Dan', 'Pas', 'dan@gmail.com'),
                    ('Mary', 'Brown', 'mary@gmail.com'),
                ]

database.add_many(many_customers)

# Add a record to the database
database.add_one("Laura", "Smith", "laura@smith.com")

# Show all the records
database.show_all()

# Delete Record use rowid as string 6 is wrong. '6' correct
print("\nDELTE record 6")
database.delete_one('6')

database.show_all()

# Add Many Records
stuff = [
    ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
    ('Joshua', 'Raintree', 'joshua@raintree.com')
    ]

database.add_many(stuff)

database.show_all()

# Lookup Email Address Record
database.email_lookup("john@codemy.com")

database.drop_table_customers()