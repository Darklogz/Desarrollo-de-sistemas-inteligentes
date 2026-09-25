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