# Reporte del Modelo Final

## Resumen Ejecutivo

- Por medio de un bosque aleatorio con $100$ árboles de regresión, se obtuvo un valor de $0.9906$ para el `accuracy` de los datos de prueba.

## Descripción del Problema

- El objetivo principal del caso es predecir si un solicitante de tarjeta de crédito es un cliente "bueno" o "malo" con base en datos históricos de su perfil. Lo anterior corresponde a un problema de clasificación, y es por eso que se entrenó un modelo de bosque aleatorio para separar los perfiles entre dos categorías.

## Descripción del Modelo

- Para el modelo final se utilizó un bosque aleatorio para clasificación. Cabe resaltar que los hiperparámetros se seleccionaron de entre veinte combinaciones aleatorias, y la mejor combinación encontrada incluye $100$ árboles de clasificación con una profundidad máxima de $16$.

## Evaluación del Modelo

- El rendimiento del modelo se evaluó por medio del `accuracy`, el cual tuvo un valor de $0.9906$ con los datos de prueba. La matriz de confusión se puede ver a continuación, en donde se identificó que hubo más falsos positivos que negativos, pero este modelo es bastante consistente con la clasificación de perfiles.

|   | 0 | 1 |
| 0 | 10715 | 191 |
| 1 | 14 | 10891 |

## Conclusiones y Recomendaciones

- El rendimiento del último modelo fue bastante satisfactorio, teniendo en cuenta la métrica utilizada.

## Referencias

- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib - Pyplot](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Imbalanced-learn](https://imbalanced-learn.org/stable/)
- [Seaborn](https://seaborn.pydata.org/) 
