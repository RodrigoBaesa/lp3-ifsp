# LP3 IFSP  

Repositório para organizar os códigos da disciplina linguagem de
Programação 3.

## Instruções Lab de informática

Ao chegar no laboratório:

1-Configurar o usuário local do git

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

2-Fazer o clone do seu repositório no GitHub
```bash
git clone https://github.com/SEU_USUARIO/lp3-ifsp.git
```

3-Abrir o repo no VSCode
```bash
code lp3-ifsp
```

4-Criar um token para realizar os pushs

Settings -> Developer Settings -> Personal aces tokens -> Tokens (classic)

Generate new token, selecionar a pḉão Generate new token classic, marcar a opção scope repo

## Antes de Sair do Laboratório
1-Remover configurações de usuário do git local
```bash
git config --global --unset user.name
git config --global --unset user.email
```

2-Deletar o token no GitHub

3-Deslogar do GitHub