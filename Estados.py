from Downloader import downloadFile
import numpy as np
import click
import six
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import requests
from bs4 import BeautifulSoup

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


class Estados(object):

    def estado(self,argument):
        method_name = argument
        method = getattr(self,method_name, lambda : "Estado invalido")
        return method()
    
    def Alagoas(self):


        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-04-08','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-06-11','2020-06-24','2020-06-29','','2020-09-07','2020-09-16','2020-10-12','2020-10-28','2020-11-02','2020-11-15','2020-11-20','2020-11-30','2020-12-8','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='AL'
        

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            dateStr = dia+"/"+mes+"/"+ano

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "https://www2.tjal.jus.br/cdje/downloadCaderno.do?dtDiario="+dateStr+"&cdCaderno=3&tpDownload=D"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Acre(self):
        return "Não Implementado"

    
    def Amazonas(self):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-04-08','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-06-11','2020-06-24','2020-06-29','','2020-09-07','2020-09-16','2020-10-12','2020-10-28','2020-11-02','2020-11-15','2020-11-20','2020-11-30','2020-12-08','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        e='AM'
        date =start

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            dateStr = dia+"/"+mes+"/"+ano

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "https://consultasaj.tjam.jus.br/cdje/downloadCaderno.do?dtDiario="+dateStr+"&cdCaderno=2&tpDownload=D"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Bahia(self):
        pass

    def Ceara(self):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-03-19','2020-03-25','2020-04-09','2020-04-10','2020-04-13','2020-04-21','2020-05-01','2020-05-27','2020-05-28','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='CE'
        

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            dateStr = dia+"/"+mes+"/"+ano

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "https://esaj.tjce.jus.br/cdje/downloadCaderno.do?dtDiario="+dateStr+"&cdCaderno=2&tpDownload=D"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")        
         
    def DistritoFederal(self):


        iniAno = np.datetime64('2020-01-01')
        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-04-08','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-06-11','2020-08-11','2020-09-07','2020-10-12','2020-10-28','2020-11-02','2020-11-15','2020-11-20','2020-11-30','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

       self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        

        edicaoInicial = np.busday_count(iniAno,start,weekmask= [1,1,1,1,1,0,0],holidays=holidays2020)
        
        edicaoFinal = np.busday_count(iniAno,end,holidays=holidays2020)
        
        e='DF'
        
        for i in range(edicaoInicial,edicaoFinal+1):
            num = i+1
            fileUrl = "https://pesquisadje-api.tjdft.jus.br/v1/diarios/pdf/2020/"+str(num)+".pdf"
            nomeArquivo = "Diario-"+str(num)+".pdf"
            
            downloadFile(fileUrl,nomeArquivo,e)
            print("Download:"+nomeArquivo)

        print("Arquivos Baixados")

    def EspiritoSanto(self):
        pass

    def Goias(self):
        pass

    def Maranhao(self):
        pass

    def MinasGerais(self):
        pass

    def MatoGrossoDoSul(self):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start
        e='MS'
        

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            dateStr = dia+"/"+mes+"/"+ano

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "https://esaj.tjms.jus.br/cdje/downloadCaderno.do?dtDiario="+dateStr+"&cdCaderno=-1&tpDownload=D"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")
    
    def MatoGrosso(self):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-04-09','2020-04-10','2020-04-20','2020-04-21','2020-05-01','2020-06-11','2020-06-12','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-11-20','2020-12-08','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='MT'
        

        while date <= end:

            
            if np.is_busday(date,holidays=holidays2020):

                edicao = self.__definirEdicaoMT(date)

                nomeArquivo = "Diario-"+str(edicao)+".pdf"

                fileUrl = "http://dje.tjmt.jus.br/publicacoes/"+str(edicao)+"-2020%20CADERNO%20JUDICIAL%20DO%20TRIBUNAL%20DE%20JUSTICA.pdf"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Para(self):
        pass

    def Paraiba(self):
        pass

    def Pernambuco(self):
        pass

    def Piaui(self):

        holidays2020 = np.array(['2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05','2020-05-15','2020-01-06','2020-02-03','2020-02-10','2020-02-24','2020-02-25','2020-04-09','2020-04-10','2020-04-17','2020-04-21','2020-05-01','2020-05-20','2020-08-11','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='PI'
       

        iniAno = np.datetime64('2020-01-01')

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]
            ano = ano[2]+ano[3]

            dateStr = ano+mes+dia

            
            if np.is_busday(date,holidays=holidays2020):



                edicao = 8819 + np.busday_count(iniAno,date + np.timedelta64(1,'D'),holidays=holidays2020)
                edicaoStr = "dj" + dateStr + "_" + str(edicao)

                nomeArquivo = "Diario-"+edicaoStr+".pdf"

                fileUrl = "http://www.tjpi.jus.br/diarioeletronico/public/"+edicaoStr+".pdf"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Parana(self):
        pass

    def RioDeJaneiro(self):
        print("Não Implementado")

    def RioGrandeDoNorte(self):
        print("Não implementado")
    
    def Rondonia(self):

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        ano = str(start).rsplit('-')[0]

        url = "https://portal.tjro.jus.br/diario-api/list.php?ano="+ano

        result = requests.get(url)

        diarios = result.json()

        e='RO'
        date =start

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            nomeArquivo = "Diario-"+str(date)+".pdf"

            fileUrl = self.__apiUrl(diarios,dia,mes,ano)

            if fileUrl != "Not Found":
                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
           
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")
    
    def Roraima(self):

        holidays2020 = np.array(['2020-01-01','2020-01-20','2020-02-24','2020-02-25','2020-02-26','2020-04-09','2020-04-10','2020-04-20','2020-04-21','2020-05-01','2020-06-11','2020-06-12','2020-06-29','2020-07-09','2020-07-10','2020-08-10','2020-09-07','2020-09-16','2020-10-12','2020-10-28','2020-11-02','2020-11-15','2020-11-20','2020-11-30','2020-12-08','2020-12-24','2020-12-25','2020-12-31'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='RR'

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "http://diario.tjrr.jus.br/dpj/dpj-"+ano+mes+dia+".pdf"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")
    
    def RioGrandeDoSul(self):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-04-10','2020-04-21','2020-05-01','2020-06-11','2020-06-12','2020-09-07','2020-09-20','2020-10-12','2020-11-02','2020-11-15','2020-11-20','2020-12-08','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')
        cadernos = ['0','5','7','6','8']

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='RS'

        while date <= end:

            if np.is_busday(date,holidays=holidays2020):

                edicao = self.__EdicaoRS(date)

                

                for c in cadernos:
                    nomeArquivo = "Diario-"+str(date)+"caderno-"+c+".pdf"
                    fileUrl ="https://www.tjrs.jus.br/servicos/diario_justica/download_edicao.php?tp="+c+"&ed="+edicao
                    diretorio = e+"/"+c
                    downloadFile(fileUrl,nomeArquivo,diretorio)
                    print("Download:"+nomeArquivo)


            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")
    
    def SantaCatarina(self):
        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        e='SC'
        date =start
        cadernos = ['1','2','3','4']

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            strDia = dia+"/"+mes+"/"+ano

            url = "http://busca.tjsc.jus.br/dje-consulta/rest/diario/dia?dia="+strDia
            result = requests.get(url)
            resultJson = result.json()

            try:

                edicao = str(resultJson[str(date)][0]['edicao'])
            except KeyError:

                edicao = None

            
            if edicao != None:
                for c in cadernos:
                    try:
                        fileUrl = "http://busca.tjsc.jus.br/dje-consulta/rest/diario/caderno?edicao="+edicao+"&cdCaderno="+c
                        nomeArquivo = "Diario-"+str(date)+"-caderno-"+c+".pdf"
                        diretorio = e+"/"+"caderno "+c
                        downloadFile(fileUrl,nomeArquivo,diretorio)
                        print("Download:"+nomeArquivo)

                    except:
                        raise


            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Sergipe(self):
        holidays2020 = np.array(['2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05','2020-01-06','2020-02-24','2020-02-25','2020-02-26','2020-03-16','2020-03-17','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-05-01','2020-05-22','2020-05-25','2020-05-26','2020-06-11','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='SE'

        while date <= end:

            if np.is_busday(date,holidays=holidays2020):

                edicao = self.__EdicaoSE(date)
                
                nomeArquivo = "Diario-"+str(date)+".pdf"
                fileUrl ="http://www.diario.tjse.jus.br/diario/diarios/"+edicao+".pdf"
                diretorio = e
                downloadFile(fileUrl,nomeArquivo,diretorio)
                print("Download:"+nomeArquivo)


            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")
    
    def SaoPaulo(self):

        holidays2020 = np.array(['2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05','2020-01-06','2020-02-24','2020-02-25','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-05-20','2020-05-22','2020-05-25','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        self.__log("Data de inicio e fim da pesquisa:","green")

        dataInit,dataFim = self.__askDate()
        
        start = np.datetime64(dataInit)
        end = np.datetime64(dataFim)

        date = start

        e='SP'

        while date <= end:

            dia = str(date).rsplit('-')[2]
            mes = str(date).rsplit('-')[1]
            ano = str(date).rsplit('-')[0]

            dateStr = dia+"/"+mes+"/"+ano

            e='SP'

            if np.is_busday(date,holidays=holidays2020):

                nomeArquivo = "Diario-"+str(date)+".pdf"

                fileUrl = "https://esaj.tjce.jus.br/cdje/downloadCaderno.do?dtDiario="+dateStr+"&cdCaderno=2&tpDownload=D"

                downloadFile(fileUrl,nomeArquivo,e)
                print("Download:"+nomeArquivo)
            
            date = date + np.timedelta64(1,'D')

        print("Arquivos Baixados")

    def Tocantins(self):

        result = requests.get("https://wwa.tjto.jus.br/diario/pesquisa/arquivos")
        c = result.content
        soup = BeautifulSoup(c, 'html.parser')

        elementsA = soup.find_all('a')
        lista = []

        for link in elementsA:
            lista.append(link.get('href'))
        
        listHref = []

        for i in lista:
            temp = i.rsplit(".")
            if temp[-1] == "pdf":
                listHref.append(i)
        
        e='TO'
        
        for fileUrl in listHref:
            temp = fileUrl.rsplit(".")
            tempEdicao = temp[-2].rsplit("/")
            edicao = tempEdicao[-1]
            nomeArquivo = "Diario-"+edicao+".pdf"
            diretorio = e+"/2020"
            self.__log("Download:"+nomeArquivo,"red")
            downloadFile(fileUrl,nomeArquivo,diretorio)
        
        self.__log("Concluido","green")
            



        

    def __definirEdicaoMT(self,date):

        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-02-26','2020-04-09','2020-04-10','2020-04-20','2020-04-21','2020-05-01','2020-06-11','2020-06-12','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-11-20','2020-12-08','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')

        iniAno = np.datetime64('2020-01-01')

        delta = np.busday_count(iniAno,date,holidays=holidays2020)

        return 10646 + delta
    
    def __EdicaoRS(self,date):
        holidays2020 = np.array(['2020-01-01','2020-02-24','2020-02-25','2020-04-10','2020-04-21','2020-05-01','2020-06-11','2020-06-12','2020-09-07','2020-09-20','2020-10-12','2020-11-02','2020-11-15','2020-11-20','2020-12-08','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')
        iniAno = np.datetime64('2020-01-01')
        delta = np.busday_count(iniAno,date,holidays=holidays2020)

        return str(6655 + delta-1)

    def __EdicaoSE(self,date):

        holidays2020 = np.array(['2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05','2020-01-06','2020-02-24','2020-02-25','2020-02-26','2020-03-16','2020-03-17','2020-04-09','2020-04-10','2020-04-21','2020-05-01','2020-05-01','2020-05-22','2020-05-25','2020-05-26','2020-06-11','2020-09-07','2020-10-12','2020-11-02','2020-11-15','2020-12-24','2020-12-25','2020-12-30'],dtype='datetime64')
        iniAno = np.datetime64('2020-01-01')
        delta = np.busday_count(iniAno,date,holidays=holidays2020)
        return str(5289 + delta-1)
    
    
    def __log(self,string, color, font = "slant",figlet = False):
        if colored:
            if not figlet:
                six.print_(colored(string))
            
            else:
                six.print_(colored(figlet_format(string,font = font),color))
        
        else:
            six.print_(string)
    
    def __askDate(self):

        style = style_from_dict({Token.QuestionMark: '#fac731 bold',
                                Token.Answer: '#4688f1 bold',
                                Token.Instruction: '',  # default
                                Token.Separator: '#cc5454',
                                Token.Selected: '#0abf5b',  # default
                                Token.Pointer: '#673ab7 bold',
                                Token.Question: '',
        })

        Questions = [
        {
            'type':'input',
            'name':'ano',
            'message':'Qual o ano da pesquisa:'

        },
        {
            'type':'input',
            'name':'diaInicial',
            'message':'Dia inicial:',
            
        },
        {
            'type':'input',
            'name':'mesInicial',
            'message':'Mes Inicial:'
        },
        {
            'type':'input',
            'name':'diaFinal',
            'message':'Dia Final:'
        },
        {
            'type':'input',
            'name':'mesFinal',
            'message':'Mes Final:'
        }
        ]

        answer = prompt(Questions,style = style)

        dataInit = str(answer['ano']) + '-' + str(answer['mesInicial']) + '-' + str(answer['diaInicial'])
        dataFim = str(answer['ano']) +  '-' + str(answer['mesFinal']) + '-' + str(answer['diaFinal'])

        return dataInit,dataFim
    
    def __apiUrl(self,jsonObject,dia,mes,ano):

        try:
            urlFile = [obj for obj in jsonObject if obj['year']== ano and obj['month'] == mes and obj['day'] == dia ][0]['url']
        except IndexError:
            urlFile = "Not Found"
        
        return urlFile
    




     
    