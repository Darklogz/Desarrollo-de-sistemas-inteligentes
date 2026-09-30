## Leonardo Alejandro Mondragón Morales


¿las dos clases tienen la misma cantidad de casos? Anota qué porcentaje del total es maligno. Lo vamos a necesitar en el Paso 10.
357 son benignos y 212 son malignos por lo que están desbalanceadas

¿Qué medida usó el modelo en la primera pregunta (la de hasta arriba)? ¿Coincide con lo que viste en la gráfica del Paso 4? ¿Usó las 10 medidas o solo algunas?
La primera pregunta es que si usa puntos cóncavos, sí coincide con el paso 4 y el árbol solo uso 4 preguntas (puntos cóncavos, área, textura y radio) no todas

¿Cuál de los dos errores es más grave en este escenario y por qué?
El falso negativo es el más grave en este escenario: significa clasificar como benigno un tumor que en realidad es maligno, lo que retrasa y evita que se le dé seguimiento a un paciente que tenga que ser atendido de forma urgente


- **T, P, E.** Con tus palabras, escribe cuál es la tarea, la medida de desempeño y la experiencia en este ejercicio.
T: Clasificar un tumor como benigno o maligno
P: porcentaje de diagnósticos correctos
E: los 569 casos ya diagnosticados y los que diagnostique de forma correcta
- **Supervisado.** Explica en dos líneas qué parte del código hace que este ejercicio sea _supervisado_. (Pista: Paso 7.)
En el Paso 7, la línea modelo.fit(X_entrena, y_entrena) es la que hace el aprendizaje supervisado, porque al modelo no solo se le dan las medidas de los pacientes (X_entrena), sino también la respuesta correcta de cada uno (y_entrena, el diagnóstico dado por el especialista).
- **Las reglas.** Escribe con palabras la regla completa de una de las ramas del árbol del Paso 8, desde arriba hasta una hoja. Ejemplo de formato: _"Si el radio es ≤ … y …, entonces el modelo dice …"_.
Si puntos_concavos es mayor a 0.05, y la textura es mayor a 15.43, entonces el modelo dice maligno, sin importar el valor del radio.
- **Los errores.** Anota tu exactitud, tus falsos positivos y tus falsos negativos. ¿Recomendarías usar este modelo en el hospital tal como está? Justifica.
Dio 93% lo cual no es para nada suficiente para algo tan delicado como la detección de cancer de mama podría servir como una segunda prueba sin embargo un profesional sigue siendo más eficiente
- **Experimenta.** En el Paso 6 cambia `random_state=42` por otro número y vuelve a ejecutar todo (menú _Entorno de ejecución → Ejecutar todas_). ¿Cambió la exactitud? ¿Por qué crees que pasa?
Cambie a 23 no cambio en mi caso pero al cambiar la "semilla" tiende a cambiar el resultado
- **Reflexión.** En el Paso 12, ¿qué profundidad elegirías y por qué?
la profundidad 3 ya que es la que tuvo mejores resultados en el 93%


### Segunda parte

Se agregaron nuevos modelos

|index|modelo|exactitud\_prueba|falsos\_negativos|
|---|---|---|---|
|0|Red neuronal|0\.965|5|
|1|SVM|0\.953|7|
|2|k vecinos más cercanos|0\.953|5|
|3|Bosque aleatorio|0\.942|6|
|4|Regresión logística|0\.942|5|
|5|Árbol de decisión|0\.93|6|
|6|Naive Bayes|0\.906|11|
- **T, P, E.** Con tus palabras, escribe cuál es la tarea, la medida de desempeño y la experiencia en este ejercicio.
(T) clasificar un tumor como benigno o maligno a partir de 10 medidas de los núcleos de las células. La medida de desempeño 
(P) es el porcentaje de diagnósticos correctos en pacientes que el modelo no vio durante el entrenamiento, y en especial cuántos tumores malignos se le escapan. 
(E) son los 569 casos que ya fueron diagnosticados por especialistas.
- **Supervisado.** Explica en dos líneas qué parte del código hace que este ejercicio sea _supervisado_. (Pista: Paso 7.)
Es supervisado por la línea `modelo.fit(X_entrena, y_entrena)` del Paso 7, porque al modelo no solo le damos las medidas (`X_entrena`) sino también la respuesta correcta de cada caso (`y_entrena`, el diagnóstico). Así el modelo aprende a relacionar las medidas con la etiqueta.
- **Las reglas.** Escribe con palabras la regla completa de una de las ramas del árbol del Paso 8, desde arriba hasta una hoja. Ejemplo de formato: _"Si el radio es ≤ … y …, entonces el modelo dice …"_.
Si los puntos cóncavos son > 0.05, y la textura es > 15.43, y el radio es > 14.43, entonces el modelo dice **maligno**. En el entrenamiento, los 109 pacientes que llegaron a esa hoja eran malignos, así que su gini es 0.
- **Los errores.** Anota tu exactitud, tus falsos positivos y tus falsos negativos. ¿Recomendarías usar este modelo en el hospital tal como está? Justifica.
Mi exactitud fue de 93.0 %, con 6 falsos positivos y 6 falsos negativos. El modelo detectó 58 de 64 tumores malignos (90.6 %). No lo recomendaría tal como está para usarlo solo. Dejaría pasar como benignos a 6 de cada 64 pacientes con cáncer, y ese es el error más grave. Sí serviría como apoyo para priorizar la revisión, siempre con el especialista revisando los casos. Además, la exactitud sería mejor que la de un modelo que dice "benigno" a todos (62.6 % en prueba), pero eso no basta en medicina.
- **Experimenta.** En el Paso 6 cambia `random_state=42` por otro número y vuelve a ejecutar todo (menú _Entorno de ejecución → Ejecutar todas_). ¿Cambió la exactitud? ¿Por qué crees que pasa?
Sí cambió, con `random_state` 0 saqué 91.2 %, con 1 saqué 92.4 %, con 7 saqué 89.5 % y con 123 saqué 95.3 %. Cambia porque cada número manda pacientes distintos al conjunto de prueba, y como son solo 171 pacientes, un solo paciente mueve la exactitud 0.6 puntos. Por eso una sola prueba no basta para concluir que un modelo es mejor que otro.
- **Reflexión.** En el Paso 12, ¿qué profundidad elegirías y por qué?
Elegiría profundidad 3. Es la que da la mejor exactitud en prueba (93.0 %, contra 91.2 % con profundidad 1 o 2, 91.8 % con 5 y 91.2 % sin límite). Con profundidad 5 o sin límite, la exactitud en entrenamiento sube a 99 % y 100 %, pero en prueba baja. Eso es sobreajuste: el árbol memoriza en lugar de aprender reglas generales. Además, con profundidad 3 el árbol se puede leer completo.
- **Comparar modelos.** Con la tabla del Paso 13, elige el modelo que recomendarías al hospital. Justifica tomando en cuenta la exactitud, los falsos negativos y si se puede explicar su decisión.
La red neuronal es la que usaría más ya que es a la que le fue mejor
- **Experimenta con modelos.** En el Paso 13 cambia `n_neighbors` de k-NN (por defecto 5) a 1 y a 15: `KNeighborsClassifier(n_neighbors=15)`. ¿Qué pasa con la exactitud?
Con k=1 la exactitud bajó a 92.4 % (en entrenamiento da 100 %, o sea que memoriza y sobreajusta). Con k=5 fue de 95.3 % y con k=15 subió a 95.9 %. Al usar más vecinos el modelo se vuelve menos sensible a casos raros y generaliza mejor.