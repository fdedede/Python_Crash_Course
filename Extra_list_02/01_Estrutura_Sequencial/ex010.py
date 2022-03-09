# Exercício Extra 010

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.'''



hour_pay = float(input('Earning per hour: '))
worked_hour = float(input('Hours of work: '))
gross_salary = hour_pay * worked_hour
ir = gross_salary * 0.11
inss = gross_salary * 0.08
sindicate = gross_salary * 0.05
net_salary = gross_salary - (ir + inss + sindicate)
print(f'O seu salário bruto é: R${gross_salary}')
print(f'Foram descontados R${ir} de IR(11%), R${inss} de INSS(8%) e R${sindicate} do sindicato')
print(f'O seu salário liquido é R${net_salary}')
