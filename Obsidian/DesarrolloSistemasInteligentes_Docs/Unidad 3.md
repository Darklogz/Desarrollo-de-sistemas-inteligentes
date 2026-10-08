## Actividades 3.1

1. Problemas de búsqueda
* **Definición:** Situación formal en la que un agente debe encontrar una secuencia de acciones que lo conduzca desde una situación inicial hasta un estado meta predefinido.

2. Espacio de estados
* **Definición:** Conjunto de todos los estados alcanzables desde el estado inicial mediante cualquier secuencia válida de acciones.

 3. Estado inicial
* **Definición:** Estado en el que se encuentra el agente al comenzar el proceso de resolución del problema ($s_0$).

4. Acciones
* **Definición:** Conjunto de operaciones o alternativas disponibles $A(s)$ que el agente puede ejecutar cuando se encuentra en un estado determinado $s$.

 5. Modelo de transición
* **Definición:** Función $Result(s, a)$ que especifica de forma explícita cuál es el estado resultante al aplicar la acción $a$ en el estado $s$.

6. Prueba de meta
* **Definición:** Función o condición $Goal(s)$ que evalúa un estado dado $s$ y determina si satisface los requerimientos del objetivo buscado.

 7. Costo del camino
* **Definición:** Función numérica $c(s, a, s')$ que asigna un costo acumulado a la secuencia de acciones que conforman un trayecto.

8. Solución
* **Definición:** Secuencia de acciones que transforma el estado inicial en un estado que satisface con éxito la prueba de meta.

 9. Frontera
* **Definición:** Conjunto de todos los nodos hoja o pendientes de expandir que forman el frente de exploración en un momento dado (nodos abiertos).

10. Nodo
* **Definición:** Estructura de datos dentro del árbol de búsqueda que representa un estado e incluye punteros al nodo padre, la acción aplicada y el costo acumulado.

11. Agente de resolución de problemas
* **Definición:** Agente basado en metas que decide qué hacer formulando el problema y buscando una secuencia ordenada de acciones antes de ejecutarlas.

12. Sistemas de búsqueda (ciega)
* **Definición:** Sistemas de exploración que recorren el espacio de estados utilizando únicamente la definición formal del problema, sin información extra del dominio.

13. Búsqueda no informada (ciega)
* **Definición:** Estrategias de búsqueda que operan mediante exploración sistemática o fuerza bruta, sin estimaciones sobre la proximidad a la meta.

14. Búsqueda en amplitud (BFS)
* **Definición:** Estrategia de búsqueda que expande primero el nodo raíz y luego todos sus sucesores nivel por nivel a lo largo del árbol.

 15. Búsqueda en profundidad (DFS)
* **Definición:** Estrategia de búsqueda que expande siempre el nodo de mayor profundidad presente en la frontera actual.

16. Búsqueda de costo uniforme (UCS)
* **Definición:** Algoritmo que expande prioritariamente el nodo $n$ de la frontera con el menor costo de camino acumulado $g(n)$.

17. Cola (FIFO)
* **Definición:** Estructura de datos "First-In, First-Out" (el primero en entrar es el primero en salir), empleada para gestionar la frontera en la búsqueda en amplitud.

18. Pila (LIFO)
* **Definición:** Estructura de datos "Last-In, Last-Out" (el último en entrar es el primero en salir), empleada para gestionar la frontera en la búsqueda en profundidad.

19. Completitud
* **Definición:** Propiedad que garantiza que un algoritmo de búsqueda encontrará una solución siempre que exista al menos una en el espacio de estados.

 20. Optimalidad
* **Definición:** Propiedad que asegura que el algoritmo devolverá la solución que posee el menor costo del camino posible entre todas las soluciones válidas.

21. Complejidad en tiempo
* **Definición:** Medida de la cantidad de nodos generados o pasos ejecutados por el algoritmo antes de hallar una solución.

 22. Complejidad en espacio
* **Definición:** Medida de la cantidad máxima de memoria requerida por el algoritmo durante la ejecución de la búsqueda (tamaño de la frontera).

Fuentes:
https://es.scribd.com/document/792467890/document
https://es.scribd.com/document/579359069/03-Busqueda-no-Informada-1
https://es.scribd.com/document/1062652996/Clase-1
