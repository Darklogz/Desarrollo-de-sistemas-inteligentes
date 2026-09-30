### Acticidad 2.4

### 1. Árbol de decisión

**Definición:** Es un método supervisado no paramétrico para clasificación y regresión. Predice la variable objetivo aprendiendo reglas de decisión simples inferidas de los datos. [scikit-learn](https://scikit-learn.org/stable/modules/tree.html)

**Cómo funciona:** Divide el espacio de variables de forma recursiva. En cada nodo elige la variable y el umbral que minimizan una medida de impureza (Gini o entropía). Se detiene al llegar a un criterio como la profundidad máxima. [scikit-learn](https://scikit-learn.org/stable/modules/tree.html)

**Caso de uso:** Un tutorial de DataCamp usa un árbol para prevenir ataques cardíacos. [datacamp](https://www.datacamp.com/es/tutorial/decision-tree-classification-python)

**Fuentes:** [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html) y [https://www.datacamp.com/es/tutorial/decision-tree-classification-python](https://www.datacamp.com/es/tutorial/decision-tree-classification-python)

### 2. Regresión logística

**Definición:** A pesar del nombre, es un modelo lineal de clasificación y no de regresión. Modela las probabilidades de los resultados posibles con una función logística. [scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html)

**Cómo funciona:** Calcula la probabilidad de la clase positiva y la convierte en clase aplicando un umbral, por defecto 0.5. Se ajusta minimizando una función de costo con regularización opcional. [scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html)

**Caso de uso:** La guía menciona el riesgo de impago de un préstamo, la detección de fraude en transacciones y la probabilidad de curación o efectos secundarios en pruebas de medicamentos. [scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html)

**Fuente:** [https://scikit-learn.org/stable/modules/linear_model.html](https://scikit-learn.org/stable/modules/linear_model.html) (sección Logistic regression)

### 3. K vecinos más cercanos (k-NN)

**Definición:** Es un método basado en instancias que no construye un modelo general. Simplemente guarda los datos de entrenamiento. [scikit-learn](https://scikit-learn.org/stable/modules/neighbors.html)

**Cómo funciona:** Para un punto nuevo busca los k ejemplos de entrenamiento más cercanos, normalmente con distancia euclidiana, y le asigna la clase que más se repite entre ellos. Un k grande reduce el efecto del ruido pero vuelve menos nítidas las fronteras. [scikit-learn](https://scikit-learn.org/stable/modules/neighbors.html)

**Caso de uso:** Según la guía, ha funcionado bien con dígitos escritos a mano e imágenes satelitales. [scikit-learn](https://scikit-learn.org/stable/modules/neighbors.html)

**Fuente:** [https://scikit-learn.org/stable/modules/neighbors.html](https://scikit-learn.org/stable/modules/neighbors.html)

### 4. Naive Bayes

**Definición:** Es una familia de algoritmos supervisados basados en el teorema de Bayes. Asumen, de forma "ingenua", que las variables son independientes entre sí dada la clase. [scikit-learn](https://scikit-learn.org/stable/modules/naive_bayes.html)

**Cómo funciona:** Estima la probabilidad de cada clase y la probabilidad de cada variable dada la clase. Después elige la clase con mayor producto de esas probabilidades. [scikit-learn](https://scikit-learn.org/stable/modules/naive_bayes.html)

**Caso de uso:** Son famosos en la clasificación de documentos y el filtrado de spam, y necesitan pocos datos de entrenamiento. [scikit-learn](https://scikit-learn.org/stable/modules/naive_bayes.html)

**Fuente:** [https://scikit-learn.org/stable/modules/naive_bayes.html](https://scikit-learn.org/stable/modules/naive_bayes.html)

### 5. SVM (máquinas de vectores de soporte)

**Definición:** Son métodos supervisados para clasificación, regresión y detección de valores atípicos. [scikit-learn](https://scikit-learn.org/stable/modules/svm.html)

**Cómo funciona:** Buscan el hiperplano con la mayor distancia a los puntos más cercanos de cualquier clase. Esos puntos son los vectores de soporte. Con funciones kernel pueden separar datos que no son linealmente separables, y conviene escalar los datos antes. [scikit-learn](https://scikit-learn.org/stable/modules/svm.html)

**Caso de uso:** Clasificación de texto y correos electrónicos: Se usa para categorizar mensajes como spam o correo válido (ham), analizando la frecuencia y presencia de palabras clave.

**Fuente:** [https://scikit-learn.org/stable/modules/svm.html](https://scikit-learn.org/stable/modules/svm.html)

### 6. Bosque aleatorio (Random Forest)

**Definición:** Es un método de ensamble basado en árboles de decisión aleatorizados. La predicción final es el promedio de las predicciones de cada árbol. [scikit-learn](https://scikit-learn.org/stable/modules/ensemble.html)

**Cómo funciona:** Cada árbol se construye con una muestra con reemplazo del conjunto de entrenamiento y considera solo un subconjunto aleatorio de variables en cada división. Esa doble aleatoriedad reduce la varianza y el sobreajuste de los árboles individuales. [scikit-learn](https://scikit-learn.org/stable/modules/ensemble.html)

**Caso de uso:** Detección de fraude financiero: Analiza millones de transacciones bancarias en tiempo real. Identifica patrones sospechosos según el monto, la ubicación y el horario para bloquear operaciones fraudulentas.
**Fuente:** [https://scikit-learn.org/stable/modules/ensemble.html](https://scikit-learn.org/stable/modules/ensemble.html) (sección Random forests)

### 7. Red neuronal (perceptrón multicapa)

**Definición:** El perceptrón multicapa es un algoritmo supervisado que aprende una función no lineal para clasificación o regresión. A diferencia de la regresión logística, tiene una o más capas ocultas entre la entrada y la salida. [scikit-learn](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

**Cómo funciona:** Cada neurona oculta hace una suma ponderada de la capa anterior y le aplica una función de activación no lineal. Los pesos se entrenan con retropropagación y descenso de gradiente, minimizando la entropía cruzada en clasificación. [scikit-learn](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

**Caso de uso:** La guía incluye un ejemplo con MNIST (dígitos escritos a mano) que visualiza los pesos aprendidos. También advierte que esa implementación no es para aplicaciones a gran escala ni usa GPU. [scikit-learn](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

**Fuente:** [https://scikit-learn.org/stable/modules/neural_networks_supervised.html](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)


