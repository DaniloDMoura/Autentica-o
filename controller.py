import bcrypt 
from password_strength import PasswordPolicy
from model import Usuario
from orm import session


class ValidarFormulario:
    

    @classmethod
    def validar_usuario(cls, usuario, *args):
        x = len(usuario)
        y = session.query(Usuario).filter_by(nome=usuario).first()
        
        if x >= 3 and x <= 30:
            if not y and args[0] == 'c':
                return False
            if y and args[0] == 'l':
                return True
            if not y and args[0] == 'l':
                return 3
            else:
                return 2
        else:
            return 1
    
    @classmethod
    def validar_email(cls, email, *args):
        permitido = [['@', '.', '.'],['@', '.']]
        x = session.query(Usuario).filter_by(email=email).first()

        valores = [i for i in email if(i == '@' or i == '.')]
        
        if permitido[0] == valores or permitido[1] == valores:
            if not x and args[0] == 'c':
                return False
            if x and args[0] == 'l':
                return 100
            if not x and args[0] == 'l':
                return 3
            else:
                return 2
        else:
            return 1
    
    @classmethod
    def validar_senha(cls, senha):
        regra = PasswordPolicy.from_names(strength = 0.66)
        teste = float(regra.password(senha).strength())
        
        if teste <= 0.33:
            return 1
        elif teste > 0.33 and teste <= 0.66:
            return 2
        return False
    
    @classmethod
    def checar_senha(cls, email, senha):
        senha_armazenada = session.query(Usuario).filter_by(email=email).first()      
        x = bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada.senha_hash.encode('utf-8'))

        if x:
            return 100
        else:
            return 3
    
    @classmethod
    def mensagens(cls, user = 0, ema = 0, psw = 0):
        # Mensagens de erro para usuário
        if user == 1:
            print('Usuário deve possuir no mínimo 3 caracteres')
        if user == 2:
            print('Usuário já existente, tente outro nome')
        if user == 3:
            print('Usuário não cadastrado ou erro de digitação')
        
        # Mensagens de erro para email
        if ema == 1:
            print('Email inválido')
        if ema == 2:
            print('Email já existente, tente outro email')
        if ema == 3:
            print('Email não cadastrado ou erro de digitação')
        
        # Mensagens para senha
        if psw == 1:
            print('\33[91mSenha muito fraca\33[0m')
        if psw == 2:
            print('\33[93mSenha mediana\33[0m')
        if psw == 3:
            print('Senha incompatível, tente novamente')


class CadastrarUsuario:


    @classmethod
    def cadastrar_usuario(cls, nome, email, senha):

        a = ValidarFormulario.validar_usuario(nome, 'c')
        b = ValidarFormulario.validar_email(email, 'c')
        c = ValidarFormulario.validar_senha(senha)

        if not a and not b and not c:
            senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt(14))

            usuario = Usuario(
                nome = nome,
                email = email,
                senha_hash = senha_hash
            )

            session.add(usuario)
            session.commit()

            print('Usuário cadastrado com sucesso')
        
        else:
            ValidarFormulario.mensagens(user = a, ema = b, psw = c)
            
        input('Pressione ENTER para continuar')


class LogarUsuario:
    

    @classmethod
    def login(cls, email, senha):
        a = ValidarFormulario.validar_email(email, 'l')

        if a == 100:
            c = ValidarFormulario.checar_senha(email, senha)
            
            if c == 100:
                print('Usuário logado com sucesso')
            else:
                ValidarFormulario.mensagens(psw = c)
        else:
            ValidarFormulario.mensagens(ema = a)

        input('Pressione ENTER para continuar')