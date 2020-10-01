from __future__ import print_function, unicode_literals
import shutil
import  numpy as np
import os
import sys
import click
import six
from Estados import  Estados
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import figlet_format


try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})

def log(string, color, font = "slant",figlet = False):
    if colored:
        if not figlet:
            six.print_(colored(string))
        
        else:
            six.print_(colored(figlet_format(string,font = font),color))
    
    else:
        six.print_(string)


def askEstado():
    Question = [
        {
            'type':'list',
            'name':'estado',
            'message':'Qual estado deseja os pesquisar?',
            'choices':['Acre',
                       'Alagoas',
                       'Amazonas',
                       'Amapa',
                       'Bahia',
                       'Ceara',
                       'Distrito Federal',
                       'Espirito Santo',
                       'Goias',
                       'Maranhao',
                       'Minas Gerais',
                       'Mato Grosso Do Sul',
                       'Mato Grosso',
                       'Para',
                       'Paraiba',
                       'Pernambuco',
                       'Piaui',
                       'Parana',
                       'Rio De Janeiro',
                       'Rio Grande Do Norte',
                       'Rondonia',
                       'Roraima',
                       'Rio Grande Do Sul',
                       'Santa Catarina',
                       'Sergipe',
                       'Sao Paulo',
                       'Tocantins',
                       'Sair'
                    ]
        }
    ]

    answer = prompt(Question,style = style)
    estado = answer['estado']

    estado = estado.replace(" ","")
    return estado

@click.command()
def main():
    log("Diários Eletrônicos de Justica", color = "blue", figlet=True)
    log("Bem-vindo à pesquisa:","green")

    e = askEstado()
    if e == 'Sair':
        log("Obrigado","red")
        return sys.exit()
    else:        
        E = Estados()    
        E.estado(e)
        log("Obrigado","red")

if __name__ == "__main__":
    main()

    


