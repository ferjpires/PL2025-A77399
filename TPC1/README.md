# 📌 TPC1 - Somador On/Off

## 📅 Data
12/02/2025

## 👤 Autor
- **Nome:** Fernando Jorge Silva Pires
- **Número de Aluno:** A77399
![Fernando Pires](../fernandopires.jpg)

## 📖 Resumo
Este trabalho consistiu em:
- Desenvolver um programa em Python (`sum.py`) que processa um ficheiro de texto (`text.txt`) ou uma string inserida pelo utilizador e insere os resultados num ficheiro (`output.txt`);
- Implementar um somador que soma sequências de dígitos no texto, controlado pelas palavras "On" e "Off";
- Exibir o resultado da soma sempre que o caracter "=" for encontrado.

## 📂 Resultados
Os resultados do programa são escritos no ficheiro `output.txt`. Todos os ficheiros podem ser encontrados na página [https://github.com/ferjpires/PL2025-A77399//tree/main/TPC1](https://github.com/ferjpires/PL2025-A77399//tree/main/TPC1).

---

## 🛠️ Como Usar

### Passos para Executar o Programa

1. **Execute o programa**:
   No terminal, execute o seguinte comando:
   ```bash
   python sum.py
   ```
2. **Escolha a opção de entrada**:

- Escolha 1 para inserir uma string diretamente.

- Escolha 2 para ler de um ficheiro.

3. **Funcionamento do programa**:

- Se escolher a opção 1, insira a string diretamente.

- Se escolher a opção 2, insira o nome do ficheiro (por exemplo, `text.txt`).

- O programa processará o texto, somando os números quando o somador estiver ligado ("On") e exibindo a soma sempre que encontrar "=".

4. **Output**:

O programa escreverá as somas parciais e a soma final no ficheiro `output.txt`.

## 📝 Notas
- O programa é **case-insensitive** para as palavras "On" e "Off", ou seja, reconhece-as independentemente de estarem em maiúsculas ou minúsculas.
- O programa ignora caracteres não numéricos quando o somador está desligado ("Off").
- O caracter "=" serve como um marcador para escrever a soma atual.
