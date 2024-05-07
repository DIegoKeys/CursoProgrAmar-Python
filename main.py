"""
Os aplicativos de computador modernos são fáceis de usar. A interação do usuário não se restringe a E / S baseada
em console. Eles têm uma interface gráfica de usuário (GUI) mais ergonômica, graças aos processadores de alta
velocidade e hardware gráfico poderoso. Esses aplicativos podem receber entradas por meio de cliques do mouse e
permitir que o usuário Osceola alternativas com a ajuda de botões de rádio, listas suspensas e outros elementos de
GUI (ou widgets).

Esses aplicativos são desenvolvidos usando uma das várias bibliotecas gráficas disponíveis. Uma biblioteca gráfica é um
 kit de ferramentas de software que possui uma coleção de classes que definem a funcionalidade de vários elementos da
 GUI. Essas bibliotecas gráficas geralmente são escritas em C / C ++. Muitos deles foram portados para Python na forma
 de módulos importáveis. Alguns deles estão listados abaixo:

Este tutorial explica o uso do Tkinter no desenvolvimento de programas Python baseados em GUI.

WxPython é um wrapper Python em torno de WxWidgets, outra biblioteca gráfica de plataforma cruzada.

PyGTK é o módulo que transporta o Python para outro kit de ferramentas de widget GUI popular chamado GTK.

PyQtis, a interface Python para Qt, é um framework GUI multiplataforma muito popular.

Tkinter é a porta Python para o kit de ferramentas Tcl-Tk GUI desenvolvido por Fredrik Lundh. Este módulo é fornecido
com distribuições padrão de Python para todas as plataformas.

Aplicativo GUI Básico
Os elementos da GUI e sua funcionalidade são definidos no módulo Tkinter. O código a seguir demonstra as etapas na
criação de uma IU.

"""
'''
Em primeiro lugar, importe o módulo TKinter. Após a importação, configure o objeto do aplicativo chamando a função 
Tk (). Isso criará uma janela de nível superior (raiz) com um quadro com uma barra de título, caixa de controle com 
os botões minimizar e fechar e uma área de cliente para armazenar outros widgets. O método geometry () define a 
largura, altura e coordenadas do canto superior esquerdo do quadro conforme abaixo (todos os valores estão em 
pixels): objJanela.geometry ("widthxheight + XPOS + YPOS") O objeto do aplicativo então entra em um evento de escuta 
loop chamando o método mainloop (). O aplicativo agora está constantemente esperando por qualquer evento gerado nos 
elementos nele. O evento pode ser um texto inserido em um campo de texto, uma seleção feita no menu suspenso ou botão 
de rádio, ações de clique único / duplo do mouse, etc. A funcionalidade do aplicativo envolve a execução de funções 
de retorno de chamada apropriadas em resposta a um tipo específico de evento. Discutiremos o tratamento de eventos 
posteriormente neste tutorial. O loop de eventos terminará quando o botão Fechar na barra de título for clicado.

Todas as classes de widget Tkinter são herdadas da classe Widget. Vamos adicionar os widgets mais usados.

Botão
O botão pode ser criado usando a classe Button. O construtor da classe Button requer uma referência à janela principal 
e às opções.

Assinatura: Button(janela, atributos)

Você pode definir as seguintes propriedades importantes para personalizar um botão:

text : caption of the button                    texto: legenda do botão
bg : background colour                          bg: cor de fundo
fg : foreground colour                          fg: cor de primeiro plano
font : font name and size                       fonte: nome e tamanho da fonte
image : to be displayed instead of text         imagem: a ser exibida em vez de texto
command : function to be called when clicked    comando: função a ser chamada quando clicada
 '''

'''
Label - Rótulo
Um rótulo pode ser criado na IU em Python usando a classe Label. O construtor Label requer o objeto de janela de nível 
superior e os parâmetros de opções. Os parâmetros de opção são semelhantes ao objeto Botão.

O seguinte adiciona um rótulo na janela.

Aqui, a legenda do rótulo será exibida em vermelho usando a fonte Helvetica de tamanho 16 pontos.
'''

# from tkinter import *
# objJanela=Tk()
#
# lblExemplo=Label(objJanela, text="ProgrAmar Label - Rótulo", fg='red', font=("Helvetica", 16))
# lblExemplo.place(x=25, y=50)
#
# objJanela.title('Curso ProgrAmar')
# objJanela.geometry("300x200+10+10")
# objJanela.mainloop()

'''
Entry - Entrada
Este widget renderiza uma caixa de texto de linha única para aceitar a entrada do usuário. Para entrada de texto com 
várias linhas, use o widget Texto. Além das propriedades já mencionadas, o construtor da classe Entry aceita o seguinte:

bd: tamanho da borda da caixa de texto; o padrão é 2 pixels.
show: para converter a caixa de texto em um campo de senha, defina show property para "*".
O código a seguir adiciona o campo de texto.

txtfld = Entry (objJanela, text = "Este é o widget Entry", bg = 'preto', fg = 'branco', bd = 5)

O exemplo a seguir cria uma janela com um botão, rótulo e campo de entrada.
'''

# from tkinter import *
# objJanela=Tk()
#
# btnExemplo=Button(objJanela, text="ProgrAmar Button widget", fg='blue')
# btnExemplo.place(x=80, y=100)
#
# lblExemplo=Label(objJanela, text="ProgrAmar Label widget", fg='red', font=("Helvetica", 16))
# lblExemplo.place(x=60, y=50)
#
# txtExemplo=Entry(objJanela, text="ProgrAmar Entry Widget", bd=5)
# txtExemplo.place(x=80, y=150)
#
# objJanela.title('Curso ProgrAmar Python')
# objJanela.geometry("300x200+10+10")
# objJanela.mainloop()

'''
Selection Widgets - Widgets de seleção
Radiobutton - Botão de opção: Este widget exibe um botão de alternância com um estado LIGADO / DESLIGADO. Pode haver mais de um botão,
 mas apenas um deles estará LIGADO em um determinado momento.

Checkbutton - Botão de verificação: Este também é um botão de alternância. Uma caixa de seleção retangular aparece antes de sua 
legenda. Seu estado LIGADO é exibido pela marca de seleção na caixa que desaparece quando é clicado em DESLIGADO.

Combobox - Combobox: esta classe é definida no módulo ttk do tkinterpackage. Ele preenche dados suspensos de um tipo de dados de 
coleção, como uma tupla ou uma lista como parâmetro de valores.

Listbox - Listbox: ao contrário do Combobox, este widget exibe toda a coleção de itens de string. O usuário pode selecionar um ou 
vários itens.

O exemplo a seguir demonstra a janela com os widgets de seleção: Radiobutton, Checkbutton, Listbox e Combobox:
'''

# from tkinter import *
# from tkinter.ttk import Combobox
#
# janela = Tk()
# strVar = StringVar()
# strVar.set("primeiro")
# lstDdata = ("primeiro", "segundo", "terceiro", "quarto")
# cmbbxPosicao = Combobox(janela, values=lstDdata)
# cmbbxPosicao.place(x=60, y=150)
#
# lstbxPosicao = Listbox(janela, height=5, selectmode='multiple')
# for num in lstDdata:
#     lstbxPosicao.insert(END, num)
# lstbxPosicao.place(x=250, y=150)
#
# intVarRadioButton0 = IntVar()
# intVarRadioButton0.set(1)
# rdbtnSexo1 = Radiobutton(janela, text="Masculino", variable=intVarRadioButton0, value=1)
# rdbtnSexo2 = Radiobutton(janela, text="Feminino", variable=intVarRadioButton0, value=2)
# rdbtnSexo1.place(x=100, y=50)
# rdbtnSexo2.place(x=180, y=50)
#
# chkbxEsportesPreferidosV1 = IntVar()
# chkbxEsportesPreferidosV2 = IntVar()
# chkbxEsportesPreferidos1 = Checkbutton(janela, text="Natação", variable=chkbxEsportesPreferidosV1)
# chkbxEsportesPreferidos2 = Checkbutton(janela, text="Futebol", variable=chkbxEsportesPreferidosV2)
# chkbxEsportesPreferidos1.place(x=100, y=100)
# chkbxEsportesPreferidos2.place(x=180, y=100)
#
# janela.title('Curso ProgrAmar')
# janela.geometry("400x300+10+10")
# janela.mainloop()

'''
Event Handling - Manipulação de eventos
Um evento é uma notificação recebida pelo objeto do aplicativo de vários widgets da GUI como resultado da interação do 
usuário. O objeto Aplicativo está sempre antecipando eventos à medida que executa um loop de escuta de eventos. As 
ações do usuário incluem clique com o botão do mouse ou clique duplo, tecla do teclado pressionada enquanto o controle 
está dentro da caixa de texto, certos ganhos de elemento ou sai de foco, etc.

Os eventos são expressos como strings no formato <modifier-type-qualifier>.

Muitos eventos são representados apenas como qualificadores. O tipo define a classe do evento.

A tabela a seguir mostra como o Tkinter reconhece diferentes eventos:

evento          modificadordo   tipo            qualificador    Ação

<Button-1>                      Botão               1           Clique com o botão esquerdo do mouse.
<Button-2>                      Botão               2           Clique com o botão do meio do mouse.
<Destroy>                       Destroy                         Window está sendo destruída.
<Duble-Button-1>  Double        Botão               1           Clique duas vezes no primeiro botão 1 do mouse.
<Enter>           Enter                                         Cursor entra na janela.
<Expose>                        Expose                          Expor a janela total ou parcialmente exposta.
<KeyPress-a>                    KeyPress            a           Qualquer tecla foi pressionada.
<KeyRelease>                    KeyRelease                      Qualquer chave foi liberada.
<Leave>                         Leave                           o cursor Deixa a janela.
<Print>                                          Print          A tecla IMPRIMIR foi pressionada.
<FocusIn>                       FocusIn                         O widget ganha foco.
<FocusOut>                      FocusOut                        O widget perde o foco.

Um evento deve ser registrado com um ou mais widgets GUI no aplicativo. Se não for, será ignorado. No Tkinter, existem 
duas maneiras de registrar um evento com um widget. A primeira maneira é usando o método bind () e a segunda maneira é 
usando o parâmetro de comando no construtor do widget.

Método Bind ()
O método bind () associa um evento a uma função de retorno de chamada para que, quando o evento ocorrer, a função seja 
chamada.

Syntax:
                            Widget.bind(event, callback)

Por exemplo, para invocar a função MyButtonClicked () no clique do botão esquerdo, use o seguinte código:

from tkinter import *
objJanela=Tk()
btn = Button(objJanela, text='OK')
btn.bind('<Button-1>', MyButtonClicked)

O objeto de evento é caracterizado por muitas propriedades, como widget de origem, coordenadas de posição, número do 
botão do mouse e tipo de evento. Eles podem ser passados para a função de retorno de chamada, se necessário.

Parâmetro de Comando
Cada widget responde principalmente a um tipo específico. Por exemplo, Button é uma fonte do evento Button. Portanto, é 
por padrão vinculado a ele. Os métodos construtores de muitas classes de widget têm um parâmetro opcional chamado 
command. Este parâmetro de comando é definido para retornar a função que será chamada sempre que seu evento associado 
ocorrer. Este método é mais conveniente do que o método bind ().

btn = Botão (janela, texto = 'OK', comando = myEventHandlerFunction)

No exemplo abaixo, a janela do aplicativo possui dois campos de entrada de texto e outro para exibir o resultado. 
Existem dois objetos de botão com as legendas Adicionar e Subtrair. O usuário deve inserir o número nos dois widgets de 
entrada. Sua adição ou subtração é exibida na terceira.

O primeiro botão (Adicionar) é configurado usando o parâmetro de comando. Seu valor é o método add () na classe. 
O segundo botão usa o método bind () para registrar o clique do botão esquerdo com o método sub (). Ambos os métodos 
lêem o conteúdo dos campos de texto pelo método get () do widget Entry, analisa os números, realiza a adição / subtração
 e exibe o resultado no terceiro campo de texto usando o método insert ().

'''
from tkinter import *


class MinhaJanela:
    def __init__(self, tkJanela):
        self.lblPrimeiroMembro = Label(tkJanela, text='Primeiro Membro')
        self.lblSegundoMembro = Label(tkJanela, text='Secgundo Membro')
        self.lblReultado = Label(tkJanela, text='Resultado')
        self.txtPrimeiroMembro = Entry(bd=3)
        self.txtSegundoMembro = Entry()
        self.txtResultado = Entry()
        self.lblPrimeiroMembro.place(x=100, y=50)
        self.txtPrimeiroMembro.place(x=200, y=50)
        self.lblSegundoMembro.place(x=100, y=100)
        self.txtSegundoMembro.place(x=200, y=100)
        self.btnAdicionar = Button(tkJanela, text='Adiciona - (+)', command=self.add)
        self.btnSubtrair = Button(tkJanela, text='Subtrai - (-)')
        self.btnSubtrair.bind('<1>', self.sub)
        self.btnAdicionar.place(x=100, y=150)
        self.btnSubtrair.place(x=200, y=150)
        self.lblReultado.place(x=100, y=200)
        self.txtResultado.place(x=200, y=200)

    def add(self):
        self.txtResultado.delete(0, 'end')
        num1 = int(self.txtPrimeiroMembro.get())
        num2 = int(self.txtSegundoMembro.get())
        result = num1 + num2
        self.txtResultado.insert(END, str(result))

    def sub(self, event):
        self.txtResultado.delete(0, 'end')
        num1 = int(self.txtPrimeiroMembro.get())
        num2 = int(self.txtSegundoMembro.get())
        result = num1 - num2
        self.txtResultado.insert(END, str(result))


objJanela = Tk()
objMinhaJanela = MinhaJanela(objJanela)
objJanela.title('Hello Python')
objJanela.geometry("400x300+10+10")
objJanela.mainloop()