
Definición: regla practica que estima que tan lejos está un estado de la meta

manhattan: 
g: lo que ya costo llegar desde S hasta esa casilla
h: lo que se estima que falta desde aqui hasta G
f=g+h: costo total estimado de un camino  



Sistema de triaje de urgencias medicas
Variables de entrada
Frecuencia cardiaca
Temperatura corporal
Nivel de dolor reportado --> leve, moderado, severo, insopotable
(de losanteriores) bajo, normal alto 
Variables de salida
Prioridad de atención 
- [ ] Baja
- [ ] media
- [ ] Alta

#### Reglas
Si FC=B Y T=B Y ND= L ENTONCES ALTA
