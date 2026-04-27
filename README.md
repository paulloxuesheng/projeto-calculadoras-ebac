# 🧮 Calculadoras EBAC - Projeto Final

## 📌 Sobre o Projeto

Este repositório contém **duas versões** de uma calculadora desenvolvida como parte do curso da EBAC (Escola Britânica de Artes Criativas e Tecnologia):

| Versão | Arquivo | Descrição |
|--------|---------|-----------|
| **Python** | `calculadora.py` | Calculadora com loop de repetição, compatível com qualquer sistema que tenha Python instalado |
| **Shell Script** | `calculadora.sh` | Calculadora para terminal Linux, com permissões ajustadas para segurança |

Ambas as versões realizam as quatro operações básicas: **soma, subtração, multiplicação e divisão**.

---

## 🐍 Calculadora Python

### O que o código faz

O script `calculadora.py` implementa uma calculadora interativa com as seguintes funcionalidades:

1. Exibe um título de abertura
2. Solicita dois números ao usuário
3. Apresenta um menu com 4 opções de operação
4. Executa o cálculo escolhido
5. Exibe o resultado formatado
6. Trata o erro de divisão por zero
7. Pergunta se o usuário deseja continuar (loop `while`)
8. Exibe mensagem de encerramento

### Como executar

**Pré-requisito:** Ter Python 3 instalado no sistema.

```bash
python3 calculadora.py



Exemplos de Execução

========================================
CALCULADORA
========================================

------------------------------
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha a operação:
1 - SOMA (+)
2 - SUBTRAÇÃO (-)
3 - MULTIPLICAÇÃO (×)
4 - DIVISÃO (/)
Digite o número da operação (1, 2, 3 ou 4): 1

Resultado: 10.0 + 5.0 = 15.0

------------------------------
Deseja fazer outra operação? (s/n): n

Obrigado por usar a calculadora!


Explicação técnica do código Python
Linha/Código	Explicação
print("=" * 40)	Imprime 40 sinais de igual (=) para criar uma linha visual
while continuar == "s":	Loop que mantém o programa rodando enquanto o usuário digitar "s"
float(input(...))	Lê o que o usuário digita e converte para número decimal
if escolha == "1":	Estrutura condicional que verifica qual operação foi escolhida
elif escolha == "2":	"Senão se" - verifica a próxima condição
print(f"...")	Exibe o resultado usando f-string (formatação com variáveis)
input(...).lower()	Lê a resposta e converte para minúscula (para aceitar "S" ou "s")


🐧 Calculadora Shell Script (Linux)

Criar o arquivo do script no terminal:
```bash
nano calculadora.sh
```
> O `nano` é um editor de texto simples que funciona direto
> no terminal. Com ele, escrevemos e salvamos o código do script.

Escrever o código da calculadora dentro do arquivo
> Toda a lógica da calculadora foi digitada dentro do editor Nano
> e salva no arquivo `calculadora.sh`.
> 
O que o código faz
O script calculadora.sh foi desenvolvido para terminal Linux e realiza as mesmas operações da versão Python, utilizando comandos nativos do bash.

Passo a passo para criar e executar (comandos utilizados no desafio)
Durante o desenvolvimento da calculadora no Linux, segui estes passos:

Passo	Comando	O que faz
1	nano calculadora.sh	Cria um novo arquivo chamado calculadora.sh usando o editor Nano
2	(escrever o código)	Insere o código da calculadora dentro do arquivo
3	chmod +x calculadora.sh	Torna o arquivo executável (acrescenta permissão de execução)
4	chmod 744 calculadora.sh	Ajusta permissões: proprietário pode tudo (7), grupo e outros apenas leitura (4)
5	./calculadora.sh	Executa o script da calculadora

Explicação das permissões Linux
Número	Significado
7	Leitura (4) + Escrita (2) + Execução (1) = 7 (proprietário)
4	Apenas leitura (grupo e outros)
Ou seja:

Proprietário: pode ler, escrever e executar o arquivo

Grupo e outros: só podem ler o arquivo (não podem modificar ou executar)



Como executar (para quem baixar seu projeto)
# 1. Dê permissão de execução (apenas na primeira vez)
chmod +x calculadora.sh

# 2. Execute o script
./calculadora.sh

## Exemplo de execução

=== CALCULADORA SIMPLES ===

Digite o primeiro número:
10
Digite o segundo número:
5

Escolha a operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão

1
Resultado: 10 + 5 = 15

=== FIM DA CALCULADORA ===


## Explicação técnica do código Shell Script
Linha/Código	Explicação
#!/bin/bash	Chamado de "shebang". Indica que o script deve ser executado com o interpretador bash
echo	Comando para exibir mensagens na tela
read num1	Lê o que o usuário digita e armazena na variável num1
if [ "$operacao" -eq 1 ]	Verifica se a variável operacao é igual a 1 (comparação numérica)
resultado=$((num1 + num2))	Realiza o cálculo e armazena o resultado na variável resultado
-ne 0	"Not Equal" - verifica se o número é diferente de zero (evita divisão por zero)

## Estrutura do Repositório
projeto-calculadora-ebac/
├── calculadora.py      # Script Python
├── calculadora.sh      # Script Shell (Linux)
└── README.md           # Documentação do projeto

## 👨‍💻 Autor

João Paulo Ferreira
Desenvolvido como projeto prático do curso EBAC — Escola Britânica
de Artes Criativas e Tecnologia.

## 💡Aprendizados aplicados neste projeto
✅ Criação de scripts em Python com loops e condicionais

✅ Desenvolvimento de scripts bash para Linux

✅ Gerenciamento de permissões de arquivos (chmod)

✅ Versionamento de código com Git e GitHub

✅ Documentação de projetos com README.md

✅ Estruturação de portfólio profissional

## 📚 Contexto do Projeto
Este projeto foi desenvolvido como parte do curso da EBAC (Escola Britânica de Artes Criativas e Tecnologia), unificando dois desafios anteriores:

Calculadora em Python (Google Colab)

Calculadora em Shell Script (Linux)

O objetivo final é demonstrar a capacidade de organizar e documentar projetos em um repositório GitHub, uma habilidade essencial para qualquer profissional de tecnologia.

## Obrigado por visitar meu projeto! 🚀

