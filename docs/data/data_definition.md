# Definición de los datos

## Origen de los datos

- Los datos se obtuvieron del conjunto [Credit Card Approval Prediction](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction/data) disponible en *Kaggle*.

## Especificación de los scripts para la carga de datos

- Los datos se descargaron en formato `csv` y se cargaron con `Pandas` en el notebok de Python [Data_acquisition](https://github.com/jgarnicaa/CreditApprovalML/blob/main/scripts/data_acquisition/Data_acquisition.ipynb).

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- En este repositorio, los datos se encuentran en [scripts/data_acquisition](https://github.com/jgarnicaa/CreditApprovalML/tree/main/scripts/data_acquisition).
- Los datos están separados en dos tablas: Una con la [información socioeconómica](https://github.com/jgarnicaa/CreditApprovalML/blob/main/scripts/data_acquisition/application_record.csv) de cada cliente y otra con sus [estados de mora](https://github.com/jgarnicaa/CreditApprovalML/blob/main/scripts/data_acquisition/credit_record.csv) en otros créditos.
