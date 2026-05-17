# Netflix Titles EDA Project

## Descripción del Proyecto

Este proyecto explora el dataset de Netflix Titles utilizando Python y librerías comunes de Data Science como Pandas, Matplotlib y Seaborn. El objetivo del análisis es identificar tendencias en el contenido de Netflix, comprender la distribución entre películas y series, y analizar cómo ha evolucionado la plataforma a lo largo del tiempo.

El proyecto sigue un pipeline reproducible de análisis de datos utilizando una estructura modular.

---

# Dataset

Dataset utilizado:

* Netflix Titles Dataset de Kaggle
* Fuente: https://www.kaggle.com/datasets/shivamb/netflix-shows

El dataset contiene información sobre películas y series de Netflix incluyendo:

* Título
* Tipo de contenido (película o serie)
* Director
* País
* Año de lanzamiento
* Clasificación
* Duración
* Géneros

---

# Estructura del Proyecto

```bash
project_demo/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── io.py
│   ├── cleaning.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
│
├── README.md
├── main.py
└── requirements.txt
```

---

# Preguntas Principales

El análisis se centra en las siguientes preguntas:

1. ¿Qué tipo de contenido domina en Netflix?
2. ¿Cómo ha evolucionado el catálogo de Netflix a lo largo del tiempo?
3. ¿Qué países producen más contenido?
4. ¿Cuáles son las clasificaciones más comunes?
5. ¿Qué géneros aparecen con mayor frecuencia?

---

# Limpieza de Datos

Las siguientes tareas de limpieza fueron realizadas:

* Eliminación de filas duplicadas
* Tratamiento de valores nulos
* Revisión de tipos de datos
* Limpieza de información categórica

---

# Feature Engineering

Se crearon tres nuevas variables:

* `content_age` → Antigüedad del contenido según el año de lanzamiento
* `decade` → Agrupación por décadas para análisis temporal
* `duration_num` → Extracción numérica de la columna duración

---

# Visualizaciones

El notebook incluye varias visualizaciones como:

* Películas vs Series
* Contenido publicado por año
* Países con mayor producción
* Distribución de clasificaciones
* Géneros más comunes
* Heatmap de correlación

---

# Hallazgos Principales

Algunos insights importantes obtenidos del análisis:

* Netflix incrementó significativamente la producción de contenido después de 2015.
* Las películas representan la mayor parte del catálogo.
* Estados Unidos domina el catálogo de la plataforma.
* TV-MA es una de las clasificaciones más frecuentes.
* Drama e International Movies aparecen entre los géneros más comunes.

---

# Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# Cómo Ejecutar el Proyecto

## 1. Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Ejecutar el pipeline

```bash
python main.py
```

---

## 4. Abrir notebook

```bash
jupyter notebook notebooks/eda.ipynb
```

---

# Conclusión

Este proyecto demuestra un flujo completo de Exploratory Data Analysis utilizando una estructura modular y reproducible. El análisis permite identificar tendencias relevantes del catálogo de Netflix y demuestra habilidades prácticas en limpieza de datos, feature engineering, visualización y organización de proyectos de Data Science.