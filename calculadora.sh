#!/bin/bash
# Script: calculadora.sh
# Descrição: Uma calculadora simples em Shell Script

echo "=== CALCULADORA SIMPLES ==="
echo ""

# Pede o primeiro número
echo "Digite o primeiro número:"
read num1

# Pede o segundo número
echo "Digite o segundo número:"
read num2

# Mostra as opções
echo ""
echo "Escolha a operação:"
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
echo ""

read operacao

# Realiza o cálculo baseado na escolha
if [ "$operacao" -eq 1 ]; then
    resultado=$((num1 + num2))
    echo "Resultado: $num1 + $num2 = $resultado"
elif [ "$operacao" -eq 2 ]; then
    resultado=$((num1 - num2))
    echo "Resultado: $num1 - $num2 = $resultado"
elif [ "$operacao" -eq 3 ]; then
    resultado=$((num1 * num2))
    echo "Resultado: $num1 * $num2 = $resultado"
elif [ "$operacao" -eq 4 ]; then
    if [ "$num2" -ne 0 ]; then
        resultado=$((num1 / num2))
        echo "Resultado: $num1 / $num2 = $resultado"
    else
        echo "Erro: Divisão por zero não permitida!"
    fi
else
    echo "Opção inválida!"
fi

echo ""
echo "=== FIM DA CALCULADORA ==="
