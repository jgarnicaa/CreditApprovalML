# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Predicción de Riesgo Crediticio Basado en Modelos de Machine Learning

## Objetivo del Proyecto

Desarrollar un modelo o modelos de machine learning que permita predecir si un solicitante de tarjeta de crédito es un cliente "bueno" o "malo", con base en datos históricos, y proponer estrategias para abordar el desbalance de clases y garantizar interpretabilidad en el modelo final

## Alcance del Proyecto

El proyecto abarcará las siguientes actividades:

- Análisis Exploratorio de Datos (EDA): Examinar las características del dataset, identificar patrones, valores faltantes, anomalías y el grado de desbalance en las clases.
- Construcción del Target: Definir las etiquetas de "bueno" o "malo" utilizando técnicas como el análisis de vintage o reglas basadas en los datos.
- Preparación de Datos: Realizar limpieza, transformación, y manejo de datos desbalanceados mediante técnicas como sobremuestreo (SMOTE) o submuestreo.
- Entrenamiento de Modelos: Implementar y evaluar modelos predictivos, incluyendo regresión logística, árboles de decisión, random forest, etc, priorizando el rendimiento y la interpretabilidad.
- Evaluación de Modelos: Medir la efectividad de los modelos utilizando métricas como F1-score, ROC-AUC, y matriz de confusión, con énfasis en minimizar falsos negativos.
- Implementación y Explicabilidad: Seleccionar un modelo final que ofrezca equilibrio entre rendimiento y explicabilidad, generando reportes que justifiquen las decisiones del modelo para su uso regulatorio y empresarial.

### Incluye:

- [Descripción de los datos disponibles]
	Dos tablas unidas por ID, con datos demográficos y financieros de solicitantes, como edad, ingresos, historial de pagos y saldos.
- [Descripción de los resultados esperados]
	- Modelo predictivo que clasifique a clientes como buenos o malos, con métricas clave como F1-score (>0.7).
	- Estrategias para manejar el desbalance y garantizar interpretabilidad.
	- Informe técnico y de negocio con justificaciones claras y reproducibilidad.
- [Criterios de éxito del proyecto]
	- Generación de un modelo confiable, explicable y con métricas satisfactorias.	

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

- Definición del Target: Construcción de etiquetas ("bueno" o "malo") mediante análisis de vintage u otras técnicas.
- Preparación de Datos: Limpieza, transformación, y manejo del desbalance con técnicas como SMOTE o submuestreo.
- Entrenamiento de Modelos: Comparar algoritmos como regresión logística, árboles de decisión, random forest y boosting, priorizando interpretabilidad y rendimiento.
- Evaluación: Validar el modelo con métricas clave y análisis de errores.
- Entrega: Seleccionar el mejor modelo, documentar resultados y recomendaciones, asegurando reproducibilidad.

## Cronograma
  

| Etapa                             | Duración Estimada | Fechas                       |  
|-----------------------------------|-------------------|------------------------------|  
| Entendimiento del negocio y carga de datos | 1 semana          | 29 de noviembre - 5 de diciembre |  
| Preprocesamiento y análisis exploratorio  | 1 semana          | 6 de diciembre - 12 de diciembre |  
| Construcción del target y extracción de características | 1 semana | 13 de diciembre - 19 de diciembre |  
| Entrenamiento y evaluación de modelos   | 2 semanas         | 20 de diciembre - 2 de enero     |  
| Evaluación final y entrega               | 1 semana          | 3 de enero - 9 de enero         |  

## Equipo del Proyecto

- Jose Eduardo Garnica Aza
- Samuel Moreno Vahos

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

El presupuesto del proyecto estará distribuido en las siguientes áreas clave:

- Infraestructura y Computación en la Nube: Servicios de almacenamiento y procesamiento para el manejo de datos y entrenamiento de modelos.

- Herramientas y Licencias: Software especializado (si aplica) y licencias necesarias para análisis y modelamiento.

- Recursos Humanos: Tiempo invertido por el equipo en análisis, modelamiento y entrega.

- Capacitación y Consultoría (opcional)

## Stakeholders

- Equipo evaluador de profesores

Relación: Responsable de la aprobación del modelo o modelos de crédito y su correcto funcionamiento
Expectativas: Espera obtener un modelo preciso que ayude a reducir riesgos, con un enfoque en la performance y justificación de las decisiones para su implementación en la aprobación de solicitudes de crédito.

- Equipo de Desarrollo de IA

Relación: Participa en la construcción, entrenamiento y evaluación del modelo.
Expectativas: Esperan claridad en los requerimientos del modelo y la entrega de un producto funcional y bien documentado, con enfoque en la optimización del rendimiento y la interpretabilidad.

## Aprobaciones

