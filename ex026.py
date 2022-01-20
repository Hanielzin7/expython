frase = str(input ('digite uma frase:')).upper()  .strip()
print ('a letra aparece A {} vezes'.format (frase.count("A")))
print ('a primeira letra  A aparece na posicão {}'.format (frase.find("A")+1))
print ('a última vez que o a apareceu foi na posição {}'.format(frase.rfind('A')+1))