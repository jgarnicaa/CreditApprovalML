# Reporte de Datos

## Resumen general de los datos

El conjunto de datos cuenta con un total de $438557$ observaciones. Se tienen $17$ variables socioeconómicas y $2$ variables relacionadas con el pago de los créditos. En la primera tabla se evidencia la falta de datos para la columna de "ocupación" además de la presencia de información duplicada.

## Resumen de calidad de los datos

Hay $134203$ valores faltantes, lo cual representa cerca del $31\%$ de las filas de la tabla `application_record`. Se trata del atributo de la ocupación del cliente, por lo que sí será un dato importante para las predicciones. Por eso, en la limpieza se deben reemplazar o rellenar dichos valores.

## Variable objetivo

El conjunto de datos escogido no posee una columna con etiquetas, por lo que, antes de entrenar el modelo, se debe definir el criterio de selección para aprobar los créditos. En este trabajo, el criterio se basa en el tiempo de mora que tiene cada cliente. Sólo son "perfiles buenos" aquellos que están al día con sus créditos actuales.

## Variables individuales

Entre las variables explicativas se cuenta con el sexo del cliente, si posee un auto, una propiedad o casa, la cantidad de hijos, su ingreso anual, el origen de dicho ingreso, nivel de educación, estado civil, entre otras variables relacionadas con el empleo y la posesión de dispositivos de comunicación.

## Ranking de variables

La variable de número de hijos puede estar muy correlacionada con la variable del tamaño del núcleo familiar del cliente, por lo que se podría eliminar alguna de estas columnas.
