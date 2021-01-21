def converte_hora(horario): 
    # Checando se o horário é AM.
    # Se os 2 primeiros números forem 12(meia-noite), trocar por 00.
    # Caso seja qualquer outro número apenas retornar o horário sem o AM.
    if horario[-2:] == "AM":
        if horario[:2] == "12": 
            return "00" + horario[2:-2] 
        
        else: 
            return horario[:-2] 
      
    # Checando se o horario é PM (poderia ser somente um else, mas optei por um elif por clareza) .
    # Se os 2 primeiros números forem 12(meio-dia), apenas retornar o horário sem o PM.
    # Caso seja qualquer outro número, adicionar 12 as horas do antigo horário.   
    elif horario[-2:] == "PM":
        if horario[:2] == "12": 
            return horario[:-2] 
          
        else: 
            hora = int(horario[:2]) + 12
            minutos_segundos = horario[2:8]
            return str(hora)+minutos_segundos 
  
    
print(converte_hora("12:00:00AM")) 
print(converte_hora("12:00:00PM")) 
