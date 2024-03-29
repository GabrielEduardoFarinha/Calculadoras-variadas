import numpy as np

def newton_raphson(f, df, a, tol=1e-5):
    Nvezes = 1
    while True:
        f_a = f(a)
        df_a = df(a)
        if abs(df_a) < tol:
            print("Derivada muito próxima de zero. O método não convergirá.")
            return None
        a_new = a - f_a / df_a
        print("Interação- %d, X= %0.6f e a função f(X)= %0.6f" % (Nvezes, a_new, f(a_new)))
        if abs(a_new - a) < tol:
            return a_new
        a = a_new
        Nvezes += 1
#Minha parte(improvement na parte de input modificando as letras P e O para serem parametros na conta)
if __name__ == '__main__':
    expression = input("Digite a expressão da função f(x) (use 'P' para 3.1415 and 'O' for 1.61803): ")
    expression = expression.replace('P', '3.1415').replace('O', '1.61803')
    f = lambda x: eval(expression)
    df = lambda x: (f(x + 1e-5) - f(x)) / 1e-5

    a = float(input("Digite o chute inicial (a): "))

    root = newton_raphson(f, df, a)

    if root is not None:
        print("A raiz aproximada é:", root)
