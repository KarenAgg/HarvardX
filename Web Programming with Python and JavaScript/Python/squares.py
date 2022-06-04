# Using a created function
from functions import square 

'''É necessário importar as funções da maneira acima, ou usar somente "import functions" para
liberar todas as funções do doc, porém antes de usa-las será necessário chamar a função, ex: "functions.square"'''

for i in range(10):
    print(f"The square of {i} is {square(i)}")