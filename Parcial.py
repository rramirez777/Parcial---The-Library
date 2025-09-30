# Bilbioteca Virtual :D

import re

def password (password):

    miss = []

    if len (password) < 8:
        miss.append("La contraseña debe tener minimo 8 caracteres")

    if not re.search(r"[A-Z]", password):
        miss.append("La contraseña debe tener minimo 1 letra mayusucla")

    if not re.search(r"[a-z]", password):
        miss.append("La contraseña debe tener minimo 1 letra miniscula")

    if not re.search(r"\d", password):
        miss.append("La contraseña debe tener minimo un numero")
        
    if not re.search(r"[^\w\s]", password):
        miss.append("La contraseña debe tener minimo 1 simbolo/caracter especial") 

    return miss


class User:
        def __init__(self, Usuario, correo, contraseña ):
            self.Usuario = Usuario
            self.contraseña = contraseña
            self.correo = correo

        def __str__(self):
            return f"Usuario: {self.Usuario} → Correo: ({self.correo}) → Contraseña: {self.contraseña}"
        

        @classmethod
        def Enter_Data(cls):
            Usuario = input("Usuario: ").strip()
            correo = input("Correo: ").strip()
            
            while True:
                Contraseña = input("Contraseña: ").strip()
                misses = password(Contraseña)

                if not misses:
                    break
                else:
                    print(" Contraseña inválida. ", ", ".join(misses))
            return cls(Usuario, correo, Contraseña)


        def buscar_libro_genero(self, genero, libros):
            encontrados = [libro for libro in libros if libro.genero.lower() == genero.lower()]
            if encontrados:
                print("Libros encontrados:")
                for libro in encontrados:
                    print(libro)
            else:
                print("No se encontraron libros de ese género.")



class Bibliotecario:
        def __init__(self, BUsuario, Bcorreo, Bcontraseña ):
            self.BUsuario = BUsuario
            self.Bcontraseña = Bcontraseña
            self.Bcorreo = Bcorreo
            self._libros = []  

        def __str__(self):
            return f"Usuario: {self.BUsuario} → Correo: ({self.Bcorreo}) → Contraseña: {self.Bcontraseña}"
        

        @classmethod
        def BEnter_Data(cls):
            BUsuario = input("Usuario: ").strip()
            Bcorreo = input("Correo: ").strip()
            
            while True:
                BContraseña = input("Contraseña: ").strip()
                misses = password(BContraseña)

                if not misses:
                    break
                else:
                    print(" Contraseña inválida. ", ", ".join(misses))
            return cls(BUsuario, Bcorreo, BContraseña)

        class Libro:
            def __init__(self, titulo, codigo, genero, generos):
                self.titulo = titulo
                self.codigo = codigo
                self.genero = genero
                self.generos = generos
                generos=["Sci-fi", "Terror", "Historia"]

            @classmethod
            def elegir_genero(cls):
                print("Elige el género del libro:")
                for idx, gen in enumerate(cls.generos, 1):
                    print(f"{idx}. {gen}")
                while True:
                    try:
                        opcion = int(input("Número de género: "))
                        if 1 <= opcion <= len(cls.generos):
                            return cls.generos[opcion - 1]
                        else:
                            print("Opción inválida. Intenta de nuevo.")
                    except ValueError:
                        print("Ingresa un número válido.")


            def __str__(self):
                return f"Titulo: {self.titulo} → Genero: ({self.genero}) → Codigo(ISBN): {self.codigo}"

        def crear_libro(self):
            titulo = input("Titulo: ").strip()
            generos = ["Sci-fi", "Terror", "Historia"]
            print("Elige el género del libro:")
            for idx, gen in enumerate(generos, 1):
                print(f"{idx}. {gen}")
            while True:
                try:
                    opcion = int(input("Número de género: "))
                    if 1 <= opcion <= len(generos):
                        genero = generos[opcion - 1]
                        break
                    else:
                        print("Opción inválida. Intenta de nuevo.")
                except ValueError:
                    print("Ingresa un número válido.")
            codigo = input("Codigo: ").strip()
            libro = self.Libro(titulo, codigo, genero, generos)
            self._libros.append(libro)
            print("Libro creado con éxito:")
            print(libro)
            return libro

        def mostrar_libros(self):
            if not self._libros:
                print("No hay libros registrados.")
            else:
                for libro in self._libros:
                    print(libro)
    

Question=input("Escribe ""Usuario"" si eres un usario corriente o ""Bibliotecario"" si eres un trabajador")
if Question == "Usuario":
        if __name__ == "__main__":
            user = User.Enter_Data()
            print("\nUsuario creado con éxito:")
            print(user)
            Ask2=input("\nDesea ver los libros disponibles?: (Si/No)")
            if Ask2 == "Si":
                print("\nLibros disponibles:")
                search = Bibliotecario("temp", "temp@correo.com", "Temp123!")
                genero = input("Ingrese el género a buscar: ")
                user.buscar_libro_genero(genero, search._libros)
                search.mostrar_libros()
                
    
elif Question== "Bibliotecario":
        if __name__ == "__main__":
            Buser = Bibliotecario.BEnter_Data()
            Ask1=input("\nBienvenido Bibliotecario, Va a agregar al gun libro?: (Si/No)")
            if Ask1 == "Si":
                Buser.crear_libro()
                print("\nLibro/s registrados:")
                Buser.mostrar_libros()
            else:
                print("\nBien:")

