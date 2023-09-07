## Proyecto Final - Car Scout

Este proyecto tiene como objetivo crear un algoritmo de filtrado para el sitio web de autoscout, que recorra los elementos filtrados por cada país y detecte diferencias de precios en los automóviles. Actualmente, este repositorio contiene la versión beta del proyecto. En el futuro, se realizarán cambios para conectar la aplicación Streamlit a una base de datos y evitar la apertura de Selenium WebDriver cada vez que se realice un filtrado.

### Características principales
- **Filtrado de Datos**: Utiliza Selenium WebDriver para extraer datos de automóviles de autoscout, permitiendo aplicar filtros personalizados.
- **Recorrido por Países**: El proyecto recorre elementos de automóviles en varios países para analizar diferencias de precios.
- **Paralelización**: Utiliza paralelización para recorrer las páginas de manera eficiente según el país seleccionado.

### Uso
Para utilizar la versión actual del proyecto, sigue estos pasos:
1. Clona este repositorio a tu máquina local.
2. Instala las dependencias necesarias utilizando `pip install -r requirements.txt`.
3. Asegúrate de que tengas el WebDriver de Chrome instalado y que la ruta correcta esté configurada en el código.
4. Ejecuta la aplicación utilizando `streamlit run car_scout_app.py`.
5. Utiliza la aplicación web para aplicar filtros y ver los resultados de los automóviles en diferentes países.

### Futuras Mejoras
Las futuras mejoras para este proyecto incluyen:
- Conectar la aplicación Streamlit a una base de datos para almacenar y consultar datos de manera eficiente.
- Optimizar el proceso de scraping para mayor velocidad y eficiencia.
- Mejorar la interfaz de usuario y la experiencia del usuario en la aplicación web.

Este proyecto es un trabajo en curso y se espera que evolucione con el tiempo. Siéntete libre de contribuir o utilizar este proyecto como base para tus propios proyectos relacionados con el análisis de precios de automóviles.

Este proyecto es un trabajo en curso y se espera que evolucione con el tiempo. Siéntete libre de contribuir o utilizar este proyecto como base para tus propios proyectos relacionados con el análisis de precios de automóviles.
