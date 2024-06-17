# Lista com todos os alunos
lista_alunos = [
    {'nome': 'Aluno1', 'nota_disciplina': 5, 'nota_constructo': {'AEA': 2, 'ATE': 5, 'MRE': 5, 'ELA': 5, 'ORG': 5, 'PCR': 5, 'ARE': 5, 'TAE': 5, 'RES': 5}},
    #{'nome': 'Aluno2', 'nota_disciplina': 6, 'nota_constructo': {'AEA': 3, 'ATE': 5, 'MRE': 5, 'ELA': 5, 'ORG': 5, 'PCR': 5, 'ARE': 5, 'TAE': 5, 'RES': 5}},
    # Adicione mais alunos conforme necessário, dados ficticios
]

# Lista com os constructos
#lista_constructos = ['OMI',	'OME','VAT', 'CAP', 'AEA', 'ATE', 'MRE', 'ELA', 'ORG', 'PCR', 'ARE', 'TAE', 'RES']
lista_constructos = ['AEA', 'ATE', 'MRE', 'ELA', 'ORG', 'PCR', 'ARE', 'TAE', 'RES']


# Lista com o texto da recomendação
lista_recomendacao = {
'AEA' : '''Avalie como você aborda as tarefas da disciplina sob diferentes pontos de
vista. 
Descreva a eficácia e a ineficácia da sua abordagem a partir do seu ponto de
vista. 
Imagine como um colega de classe avaliaria a sua abordagem. 
Ao analisar a forma como você lida com uma tarefa, você pode ser capaz de
descobrir o que está fazendo certo e o que está fazendo errado e então pode
mudar a sua abordagem. 
A sua confiança em ter um bom desempenho pode aumentar ao compreender
melhor a forma como você estuda, o que funciona e o que não funciona.''' ,

'ATE': '''Desenvolver boas habilidades de estudo resulta em menor ansiedade. 
Prepare-se bem para as aulas e tente terminar as tarefas pontualmente.
Não espere até o último minuto para realizar as tarefas ou para se preparar para uma prova. Isso ajudará você a se tornar confiante em situações de teste e talvez reduza a sua ansiedade.
Ao fazer uma prova, concentre-se em um item de cada vez; se estiver com dificuldades em uma questão, siga em frente e volte a essa questão depois.
Se não conseguir responder, lembre-se de que se você está bem-preparado;''', 

'MRE': '''
Liste os termos e tópicos importantes da disciplina. 
Defina-os e os repita em voz alta. 
Divida essa lista em listas menores compostas de termos que se relacionam. 
Construa imagens ou rimas que te ajudarão a lembrar dessas listas. 
Faça perguntas que ajudarão você a avaliar se você se lembra delas ou não. ''',

'ELA': ''',
Parafraseie e resuma as informações importantes. 
Use suas próprias palavras para descrever o conteúdo visto durante as aulas
ou em leituras específicas. 
Faça de conta que você é o professor e está tentando explicar a matéria para
os alunos. 
Tente descobrir como cada tópico da matéria se relaciona com os outros. 
Quais são as relações entre o que você ouviu em sala de aula, conversou em
discussões e leu no livro? ''',

'ORG': '''
Faça um resumo do seu material da disciplina e identifique onde seu texto e a
aula se sobrepõem e não se sobrepõem. Isso vai dar a você um ponto de partida para estabelecer conexões entre ideias apresentadas em dois contextos diferentes. 
Faça gráficos, diagramas ou tabelas dos conceitos importantes. 
Organogramas ou diagramas de árvore geralmente são bastante úteis para
ajudar a entender como as ideias se reúnem diferentemente. ''',

'ARE': '''
Leia rapidamente seu material antes de começar a ver como ele está
organizado. 
Olhe para os títulos e subtítulos do texto para ter uma ideia de como as coisas
se relacionam umas com as outras. 
Enquanto estiver lendo, faça perguntas a si mesmo sobre o parágrafo que
acabou de ler e escreva palavras-chave nas margens do livro ou em um
caderno. 
Tente determinar quais conceitos você não compreende bem. 
Apesar de esse método demorar bastante no início, você tem mais chance de
se lembrar do que leu. 
Isso economizará seu tempo depois quando estudar para a prova. ''',

'TAE': ''' 
Acompanhe o que você faz no seu tempo de estudo durante uma semana. 
Escreva seus objetivos para cada período de estudo e anote o que você
realmente cumpriu durante esse tempo. 
Analise o resultado ao final de uma semana. 
Talvez você precise mudar seu local de estudo, o período de estudo ou com
quem você estuda. 
Tente criar uma agenda que funcione bem para você. ''',

'RES': ''' 
Faça uma lista dos tópicos que você deixa para estudar no outro dia. 
Tente analisar por que você adia estudar esses tópicos conversando com
outros alunos. 
Ao falar com eles, talvez você considere uma abordagem que te ajude a agir
mais rapidamente ao invés de demorar a estudar o material. 
'''

}

# Lista com as dicas que serão retornadas
lista_retorno = []

# Nota mínima do constructo
nota_minima_constructo = 3

# Nota mínima da disciplina
nota_minima_disciplina = 6

for aluno in lista_alunos:
    if aluno['nota_disciplina'] <= nota_minima_disciplina:
        for constructo in lista_constructos:
            if aluno['nota_constructo'][constructo] <= nota_minima_constructo:
                texto_recomendacao = lista_recomendacao[constructo]
                lista_retorno.append(f"{aluno['nome']}: {texto_recomendacao}")

# Função fictícia para enviar email (para fins de exemplo)
def email(lista_retorno):
    for mensagem in lista_retorno:
        print(f"Enviando email: {mensagem}")

email(lista_retorno)
