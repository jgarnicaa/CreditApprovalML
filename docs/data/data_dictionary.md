# Diccionario de datos

## Base de datos. Aplicación a crédito.

** Tabla de datos socioeconomicos de cada cliente que solicita el crédito. Colección de aproximadamente 438000 datos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles |
| --- | --- | --- | --- |
| ID | Código único de cliente usado como identificador entre bases de datos | Entero | [0 - 9999999] |
| CODE_GENDER | Valor que define el sexo de cada cliente | Caracter | M / F |
| FLAG_OWN_CAR | Valor que define la propiedad de un automovil al cliente | Booleano | Y / N |
| FLAG_OWN_REALTY | Valor que define la propiedad de un inmueble | Booleano | Y / N |
| CNT_CHILDREN | Cantidad de hijos por persona | Entero | [0 - 19] |
| AMT_INCOME_TOTAL | Ingreso anual del cliente | Flotante 1 decimal | [0 - 9999999.9] |
| NAME_INCOME_TYPE | Categoria del ingreso del cliente | Cadena de texto | ['Working' 'Commercial associate' 'Pensioner' 'State servant' 'Student'] |
| NAME_EDUCATION_TYPE | Status de educación más alto | Cadena de texto | ['Higher education' 'Secondary / secondary special' 'Incomplete higher' 'Lower secondary' 'Academic degree'] |
| NAME_FAMILY_STATUS | Situación civil del cliente | Cadena de texto | ['Civil marriage' 'Married' 'Single / not married' 'Separated' 'Widow'] |
| NAME_HOUSING_TYPE | Tipo de vivienda del cliente | Cadena de texto | ['Rented apartment' 'House / apartment' 'Municipal apartment' 'With parents' 'Co-op apartment' 'Office apartment'] |
| DAYS_BIRTH | Cantidad de días desde el nacimiento del cliente | Entero | [-25201 - -7489] |
| DAYS_EMPLOYED | Cantidad de días que el cliente tiene empleo  (si es positiva está desempleado) | Entero | [-17531 - 1000] |
| FLAG_MOBIL | Valor para definir posesión de celular | Booleano | 1 / 0 |
| FLAG_WORK_PHONE | Valor para definir posesión de telefono en el trabajo | Booleano | 1 / 0 |
| FLAG_PHONE | Valor para definir posesión de telefono fijo |  Booleano | 1 / 0 |
| OCCUPATION_TYPE | Ocupación del cliente | Cadena de texto | ['nan' 'Security staff' 'Sales staff' 'Accountants' 'Laborers' 'Managers' 'Drivers' 'Core staff' 'High skill tech staff' 'Cleaning staff' 'Private service staff' 'Cooking staff' 'Low-skill Laborers' 'Medicine staff' 'Secretaries' 'Waiters/barmen staff' 'HR staff' 'Realty agents' 'IT staff'] |
| CNT_FAM_MEMBERS | Tamaño del núcleo familiar del cliente | Entero | [1 - 20] |

## Base de datos 2. Seguimiento de mora en créditos

** Tabla de datos asociados a mora en créditos del cliente, se muestra sus status respecto al pago y el mes en que fue obtenida la información

| Variable | Descripción | Tipo de dato | Rango/Valores posibles |
| --- | --- | --- | --- |
| ID | Código único de cliente usado como identificador entre bases de datos | Entero | [0 - 9999999] |
| MONTHS_BALANCE | Mes del que se extrajo la información, siendo el mes 0 la actualidad | Entero | [-60 - 0] |
| STATUS | Variable que clasifica la cantidad de mora respecto al crédito*| Caracter| ['X' 'C' '0' '1' '2' '3' '4' '5'] 

\*  STATUS = 0: 1-29 días de mora, 1: 30-59 días de mora, 2: 60-89 días de mora, 3: 90-119 días de mora, 4: 120-149 días de mora, 5: Moroso o con deudas sin pagar, más de 150 días sin pagar C: Al día en ese mes X: Sin préstamo ese mes.

