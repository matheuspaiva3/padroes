class ItemBiblioteca:
    def __init__(self, titulo, disponivel=True):
        self.titulo = titulo
        self.disponivel = disponivel

    def obter_titulo(self):
        return self.titulo

    def esta_disponivel(self):
        return self.disponivel

    def definir_disponibilidade(self, status):
        self.disponivel = status


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo)
        self.autor = autor
        self.ano_publicacao = ano_publicacao


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = set()

    def obter_nome(self):
        return self.nome

    def obter_email(self):
        return self.email


class GerenciadorEmprestimos:
    @staticmethod
    def emprestar_livro(usuario, livro):
        if livro.esta_disponivel():
            usuario.livros_emprestados.add(livro)
            livro.definir_disponibilidade(False)
            print(f"Livro '{livro.obter_titulo()}' emprestado para {usuario.obter_nome()}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    @staticmethod
    def devolver_livro(usuario, livro):
        if livro in usuario.livros_emprestados:
            usuario.livros_emprestados.remove(livro)
            livro.definir_disponibilidade(True)
            print(f"Livro '{livro.obter_titulo()}' devolvido por {usuario.obter_nome()}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não foi emprestado por {usuario.obter_nome()}.")


class GerenciadorLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros.append(livro)
            print(f"Livro '{livro.obter_titulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None


class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        if usuario.obter_nome() and usuario.obter_email():
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")
        else:
            print("Nome de usuário inválido.")

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None


# Exemplo de uso do código:

# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Criação dos gerenciadores
gerenciador_livros = GerenciadorLivros()
gerenciador_usuarios = GerenciadorUsuarios()

# Adicionar livros à biblioteca
gerenciador_livros.adicionar_livro(livro1)
gerenciador_livros.adicionar_livro(livro2)

# Adicionar usuários à biblioteca
gerenciador_usuarios.adicionar_usuario(usuario1)
gerenciador_usuarios.adicionar_usuario(usuario2)

# Empréstimo de livro
GerenciadorEmprestimos.emprestar_livro(usuario1, livro1)

# Tentativa de empréstimo de livro indisponível
GerenciadorEmprestimos.emprestar_livro(usuario2, livro1)

# Devolução de livro
GerenciadorEmprestimos.devolver_livro(usuario1, livro1)

# Remoção de livro
gerenciador_livros.remover_livro(livro2)

# Remoção de usuário
gerenciador_usuarios.remover_usuario(usuario2)

# Busca de livro e usuário
livro_encontrado = gerenciador_livros.buscar_livro("Python para Iniciantes")
usuario_encontrado = gerenciador_usuarios.buscar_usuario("Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())
if usuario_encontrado:
    print(usuario_encontrado.obter_nome())
