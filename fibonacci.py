n = int(input('Digite o valor que deseja ver a soma na sequência de fibonacci: '))

seq1 = 0
seq2 = 1
i = 0
print(0)
print(1)

sum = 0

while i < (n-2):
    fibo = seq1 + seq2
    seq1 = seq2
    seq2 = fibo

    sum += fibo
    i += 1

    print(f'Valor na sequência: {fibo} e soma {sum + 1}')

print(f'Resultado final {sum + 1}')
