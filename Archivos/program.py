import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip())

a = int(lines[1])
b = int(lines[2])
A = int(lines[3])
B = int(lines[4])
entrada = int(lines[5])

M = (a*b) -1
e = (A*M) + a
d = (B*M) + b
n = int(((e*d)-1) / M)


if (lines[0]=="E"):
  salida = (e * entrada) % n 
else:
  salida = (entrada * d) % n

print (salida)