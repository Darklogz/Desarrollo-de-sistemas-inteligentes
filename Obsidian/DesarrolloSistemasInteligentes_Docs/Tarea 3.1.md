## Leonardo Alejandro Mondragón Morales
### ✏️ Pregunta 1

¿Cuántas casillas exploró **amplitud**? ¿Y **profundidad**?

**Tu respuesta:** Amplitud exploró 6 casillas y profundidad exploró 28.

---

### ✏️ Pregunta 2

¿Cuántos **pasos** tiene el camino de amplitud? ¿Y el de profundidad? ¿Cuál es el más corto?

**Tu respuesta:** El camino de amplitud tiene 2 pasos y el de profundidad tiene 26. El más corto es el de amplitud.

---

### ✏️ Pregunta 3

En una frase: ¿por qué el camino de amplitud nunca es más largo que el de profundidad?

**Tu respuesta:** Porque amplitud explora por niveles, primero todo lo que está a 1 paso, luego a 2, etc. Así la primera vez que llega a G lo hace por el camino con menos pasos. Profundidad se va por un camino y puede dar muchas vueltas antes de llegar.
### ✏️ Pregunta 4

Con el orden nuevo, ¿cuántos **pasos** tiene el camino de amplitud? ¿Y el de profundidad? ¿Cuál de los dos algoritmos cambió mucho su resultado y por qué crees que pasó?

**Tu respuesta:** Con el orden nuevo, amplitud tiene 2 pasos y profundidad también 2 pasos. El que cambió mucho fue profundidad: pasó de 26 pasos a 2 (y de explorar 28 casillas a solo 3). Creo que pasó porque profundidad se va por el primer camino que encuentra según el orden de las acciones. Con el orden original arriba, derecha... se alejó de la meta y dio una vuelta enorme, y con el nuevo orden le tocó ir directo hacia G. Amplitud no depende del orden porque revisa todo por niveles, y el camino más corto sigue siendo de 2 pasos (solo cambió cuántas casillas exploró, de 6 a 13).
### ✏️ Pregunta 5

En el laberinto 2, ¿cuántas casillas exploró amplitud y cuántas profundidad? ¿Cuántos pasos tiene el camino de cada una?

**Tu respuesta:** Amplitud exploró 66 casillas y profundidad 17. Ambas encontraron un camino de 16 pasos.

---

### ✏️ Pregunta 6

Con los resultados de los dos laberintos: ¿se puede decir que profundidad siempre explora menos casillas que amplitud, o que siempre explora más? Explica con tus datos.

**Tu respuesta:** No se puede decir ninguna de las dos. En el laberinto 1 profundidad exploró más (28 contra 6), pero en el laberinto 2 exploró menos (17 contra 66). Depende de la forma del mapa y del orden de las acciones: si profundidad se va hacia la meta explora poco, y si se va por el lado contrario explora mucho.
### ✏️ Pregunta 7

¿Cuántos **pasos** y cuánto **costo** tiene el camino de amplitud? ¿Y el de costo uniforme?

**Tu respuesta:** Amplitud: 4 pasos y costo 28 (va por arriba, por el lodo). Costo uniforme: 8 pasos y costo 8 (va por abajo, por terreno normal).

---

### ✏️ Pregunta 8

Amplitud encontró el camino con menos pasos, pero no el más barato. ¿Por qué? ¿Cuándo preferirías costo uniforme?

**Tu respuesta:** Porque amplitud solo cuenta pasos y no le importa lo que cuesta cada casilla, así que eligió la ruta corta que pasa por el lodo (9 por casilla). Costo uniforme sí suma el costo acumulado y por eso encontró la ruta de abajo, que tiene más pasos pero es más barata. Preferiría costo uniforme cuando los pasos no cuestan lo mismo, por ejemplo con distancias, tiempo, tráfico o gasolina.
### ✏️ Pregunta 9

¿Cuántas combinaciones probó la búsqueda? ¿Cuántos modelos entrenó en total? ¿Cuál fue la mejor combinación y su exactitud?

**Tu respuesta:** Probó 48 combinaciones (6 × 4 × 2). Como `cv=5`, entrenó 48 × 5 = 240 modelos en total. La mejor combinación fue `criterion = 'gini'`, `max_depth = 4`, `min_samples_leaf = 1`, con una exactitud de 0.916.
### ✏️ Pregunta 10

Con 5 hiperparámetros y 10 valores cada uno, ¿cuántas combinaciones hay y cuánto tiempo estimado tardaría? Después prueba con 3 hiperparámetros: ¿cuánto tarda?

**Tu respuesta:** Con 5 hiperparámetros y 10 valores cada uno hay 10⁵ = 100,000 combinaciones y el tiempo estimado fue de unos 16.1 minutos (0.3 horas). Con 3 hiperparámetros hay 1,000 combinaciones y tarda unos 0.2 minutos (alrededor de 10 segundos). El tiempo exacto puede variar un poco según tu computadora, pero la proporción es la misma.

---

### ✏️ Pregunta 11

Grid search es una búsqueda ciega. Con lo que viste en esta actividad, ¿cuál es su ventaja y cuál su problema?

**Tu respuesta:** La ventaja es que es segura: como prueba todas las combinaciones, siempre encuentra la mejor dentro de la rejilla y es muy fácil de entender y programar. El problema es que crece muy rápido, porque cada hiperparámetro nuevo multiplica el número de combinaciones (de 1,000 pasamos a 100,000 al agregar solo 2 hiperparámetros). Con muchos hiperparámetros se vuelve muy lenta y cara, porque prueba todo sin ninguna pista de por dónde conviene buscar.