from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os 

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)
    
    print("\nAdicionando usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: " )
    senha = input("Digite a senha do usuário: ")
    
    service.criar_usuario(nome=nome, email=email, senha=senha)

    #Exibindo todos os usuários na tabela usuarios do banco de dados
    print("\nListando usuários cadastrados: ")
    lista_usuarios= service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome} - Email: {usuario.email} - Senha:{usuario.senha}")

if __name__ == "__main__":
    os.system("cls||clear")
    main()