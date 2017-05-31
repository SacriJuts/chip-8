RAM = [0 for i in range(4096)]  # RAM
V = [0 for i in range(16)]      # registers
I = 0                           # special register
PC = 0                          # PC = Program Counter | addresse de l'instruction à executer
SP = 0                          # SP = Stack Pointer | redirige vers le plus haut niveau du stack
Stack = [0 for i in range(16)]  # Stack, 16 valeurs de 16 bits => max 65532 valeurs
