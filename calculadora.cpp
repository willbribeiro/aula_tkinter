#include <iostream>

using namespace std;

int main() {
    char operador;
    float num1, num2, resultado;

    cout << "Digite um operador (+, -, *, /): ";
    cin >> operador;

    cout << "Digite dois números: ";
    cin >> num1 >> num2;

    switch(operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if(num2 != 0)
                resultado = num1 / num2;
            else {
                cout << "Erro! Divisão por zero não é permitida." << endl;
                return -1; // Saída com erro
            }
            break;
        default:
            cout << "Operador inválido!" << endl;
            return -1; // Saída com erro
    }

    cout << "Resultado: " << num1 << " " << operador << " " << num2 << " = " << resultado << endl;

    return 0;
}
