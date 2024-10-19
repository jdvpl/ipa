from faker import Faker

# Crear una instancia de Faker
fake = Faker()

# Generar script SQL para insertar 1000 usuarios
with open("insert_users.sql", "w") as file:
    file.write("INSERT INTO users (email, last_name, name)\nVALUES\n")

    for i in range(1, 1001):
        email = fake.email()
        last_name = fake.last_name()
        name = fake.first_name()
        line = f"('{email}', '{last_name}', '{name}')"
        
        if i != 1000:
            line += ",\n"
        else:
            line += ";\n"
        
        file.write(line)

print("Archivo insert_users.sql generado exitosamente.")
