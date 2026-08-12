# Personal Goals Display
# HW 3 - variáveis, input(), print(), caracteres de escape e palavras reservadas

# 1) Importa o módulo keyword (usado no final para listar as palavras reservadas)
import keyword

# 2) Coleta os dados do usuário com input()
#    Cada resposta é guardada em uma variável com nome válido e significativo:
#    - só letras, números e "_"
#    - não começa com número
#    - não é uma palavra reservada do Python
print("=== Personal Goals Display ===\n")

person_name = input("What is your name? ")
goal_name = input("What is one personal goal you have? ")
target_month = input("In which month do you want to achieve it? ")

# 3) Variável numérica (int, não string) com o tempo diário de prática
daily_minutes = 30

# 4) print() com vários valores separados por vírgula.
#    A vírgula junta os valores automaticamente com um espaço entre eles,
#    e aceita misturar texto com variáveis de tipos diferentes (str e int).
#    O "\n" no começo pula uma linha antes do bloco.
print("\n--- Your Goal Card ---")
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")

# 5) Argumento end= : troca o final padrão do print (que é "\n")
#    Assim o próximo print continua na MESMA linha.
print("\nQuick view:")
print(person_name, end=" - ")        # termina com " - " em vez de quebrar linha
print(goal_name, end=" - ")          # continua na mesma linha
print(target_month, end=" | ")       # continua na mesma linha
print(daily_minutes, "min/day")      # este último quebra a linha normalmente

# 6) Resumo final: texto fixo + variáveis + número, tudo em um único print()
print("\n--- Summary ---")
print(person_name, "wants to achieve the goal of", goal_name,
      "by", target_month, "and will practice", daily_minutes,
      "minutes every day.\n")

# 7) Lista de palavras reservadas do Python
#    (nenhuma delas pode ser usada como nome de variável)
print("Python reserved keywords:")
print(keyword.kwlist)
