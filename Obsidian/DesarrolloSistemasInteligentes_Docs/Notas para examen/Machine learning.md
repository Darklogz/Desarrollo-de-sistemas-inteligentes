
Un programa aprende de una experiencia E, respeco a una tarea T y una medida de desempeño P, si su desempeño en T medido por P mejora con la experiencia E


#### Ejemplos
Filtro de spam
T: clasificar un correo como spam o no spam
P: % de correos correctamente clasificados sobre un conjunto de prueba
E: correos ya etiquetados como spam/no spam por usuarios

Programa de damas
T: jugar partidas de damas
P % de partidas ganadas
E: partidas de práctica jugadas contra sí mismo u otros componentes


### Flujos de trabajo

1. Definir la tarea (T): que se quiere predecir o decidir
2. Reunir la experiencia (E): los datos de los que el sistema va a aprender
3. Elegir cómo medir el desempeño (P): la métrica que dirá si el modelo sirve
4. Entrenar: el algoritmo ajusta sus parámetros internos para minimizar el error sobre los datos de entrenamiento
5. Evaluar: se mide P sobre datos que el modelo nunca vio durante el entrenamiento
6. Usar o ajustar: si P es suficiente, se despliega; si no, se repite el ciclo con más datos o un modelo distinto
### Clasificación de machine learning

**Supervisado**
En el aprendizaje supervisado, el agente observa algunos pares de ejemplo entrada-salida y aprende una función que va de la entrada a la salida

**No supervisado**
En el aprendizaje no supervisado el agente aprende patrones en la entrada aunque no se le proporcione retroalimentación 

**Por refuerzo**
El aprendizaje por refuerzo es aprender qué hacer cómo asociar situaciones con acciones de manera que se maximice una señal numérica de recompensa

