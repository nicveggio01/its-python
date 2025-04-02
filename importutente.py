from utente3 import utente, privilegi, admin

utente1= utente("Niccolò", "Veggian", "nic_veggio01", "nic.veggian@mail.com")

privilegi_admin= privilegi("lettura", "scrittura", "esecuzione")

admin1= admin(utente1, privilegi_admin)

admin1.display_info_utente()

admin1.display_privilegi()

utente1.greet_user()