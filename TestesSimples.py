texto = str("aqui jás um texto longo pra caralho porra")

texto.strip()

j = 0
limite = 10
a = 0
            
for i in texto:
    j += 1
    
    if j > limite and i == ' ':
        texto = texto[:j] + "\n" + texto[j:]
                    
        limite += a + 10
        a = 0
        
    if j > limite:
        a += 1
    
print(texto)
