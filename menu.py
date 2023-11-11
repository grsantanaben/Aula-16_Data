### Introdução ao Módulo datetime em Python

#DIRETIVAS

#As diretivas da função `strftime` em Python são usadas para formatar objetos `datetime` em strings de acordo com um padrão específico. Aqui estão algumas das diretivas mais comuns que você pode usar com `strftime`:

#`%Y`: Ano com quatro dígitos (por exemplo, 2023).
#`%y`: Ano com dois dígitos (por exemplo, 23 para 2023).
#`%m`: Mês com zero à esquerda (por exemplo, 01 para janeiro).
#`%B`: Nome completo do mês (por exemplo, "January").
#`%b` ou `%h`: Nome abreviado do mês (por exemplo, "Jan").
#`%d`: Dia do mês com zero à esquerda (por exemplo, 05 para o dia 5).
#`%H`: Hora (00-23) com zero à esquerda.
#`%I`: Hora (01-12) com zero à esquerda.
#`%M`: Minuto com zero à esquerda.
#`%S`: Segundo com zero à esquerda.
#`%p`: AM ou PM (dependendo do horário).
#`%A`: Nome completo do dia da semana (por exemplo, "Sunday").
#`%a`: Nome abreviado do dia da semana (por exemplo, "Sun").
#`%j`: Dia do ano como um número decimal (001 a 366).
#`%U`: Número da semana no ano (00 a 53, onde a semana começa no domingo).
#`%W`: Número da semana no ano (00 a 53, onde a semana começa na segunda-feira).
#`%w`: Dia da semana como um número decimal (0 para domingo, 6 para sábado).
#`%Z`: Nome do fuso horário.
#`%z`: Offset do fuso horário (por exemplo, "+0200").

                #Aqui está um exemplo de como usar algumas dessas diretivas com `strftime`:

# from datetime import datetime
# dt = datetime(2023, 9, 27, 14, 30, 0)
# # Formatando a data e hora
# formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)  # Saída: "2023-09-27 14:30:00"
# # Formatando apenas a data
# formatted_date = dt.strftime("%A, %d de %B de %Y")
# print(formatted_date)  # Saída: "Wednesday, 27 de September de 2023"
# Essas diretivas permitem que você personalize a formatação de datas e horários de acordo com suas necessidades específicas.

# import datetime 
# data = datetime.datetime.now()
# print(data)

# date = datetime.datetime.now()
# n = datetime.datetime(days = 2)
# n3 = datetime.timedelca (days - 40)
# n2 = date - n3

# date = datetime.datetime.now()
# n = date.strftime(%y,%M )print 23
# print (n)

# ## Identificar idade das pessoas
# from datetime import datetime

# data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
# nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
# idade = datetime.now() - nascimento
# # Extrair apenas a parte dos anos da diferença de datas
# anos = idade.days // 365
# print(anos)

#EXERCÍCIOS 1** 

#1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.

from datetime import datetime
from timedelta import timedelta

# data = input('Digite sua data de nascimento no formato(ano, mes, dia)')
# dat = datetime.strptime(data, "%Y-%m-%d")
# data_atual = datetime.now()
# age = data_atual.year - dat.year - ((data_atual.month, data_atual.day)
# < (dat.month, dat.day))

# print(age)

#2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.
# from datetime import datetime 
# from timedelta import timedelta 

# data = datetime.datetime.now()
# seven = datetime.timedelta(days=7)
# data_seven = data + seven
# print(data)


#3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.

ano = int(input('Qua ano?'))
atual = datetime.datetime.now()
print ('O ano é:', atual)


#4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).