### Modelo Predictivo para Diagnóstico del Carcinoma Hepatocelular
**Descripción:** La meta del proyecto es desarrollar un modelo de Machine Learning capaz de clasificar a los pacientes del hospital Hermanos Ameijeiras según la información contenida en planillas médicas en tres categorías:

1. **Tratamiento inmediato:** Diagnóstico confirmado de cáncer de hígado.
2. **Revisión en tres meses:** Sospecha de cáncer de hígado.
3. **Revisión en seis meses:** Estado general saludable.

## Obtención de datos
Inicialmente, el proyecto contó con **planillas estructuradas** que registraban observaciones médicas de los **ultrasonidos**. Estas contenían información detallada sobre cada paciente, marcada según criterios específicos. Sin embargo, su uso para el modelo de ML presentó un problema fundamental:

El diagnóstico en las planillas se determinaba únicamente por la interpretación médica basada en criterios predefinidos.

En términos computacionales, la estructura de las planillas permitía replicar el diagnóstico con una simple condicional en Python (if ciertas características están presentes, entonces el paciente tiene cierta condición).

Esto significaba que no era necesario un modelo de Machine Learning, ya que los patrones de enfermedad reflejados en las planillas eran los mismos que los médicos habían identificado manualmente.

Además, el modelo de ML no tendría acceso a los detalles visuales de los ultrasonidos que podrían contener información adicional relevante para mejorar la precisión del diagnóstico.

Por estas razones, el enfoque cambió hacia el análisis directo de **imágenes de ultrasonido**, permitiendo que el modelo aprendiera patrones más profundos y no solo los criterios establecidos por médicos humanos.

Los **ultrasonidos** estaban en formatos diversos y no estandarizados, lo que dificultaba su uso directo en el procesamiento.

## Conversión y extracción de imágenes
Se utilizó el software **RadiAnt DICOM Viewer** para analizar los videos e imágenes obtenidos.

A partir de los **archivos DICOM**, se realizó la conversión y exportación de imágenes al formato **JPEG**.

Para aumentar la cantidad de datos disponibles, los videos de ultrasonido se transformaron en múltiples imágenes estáticas, generando una gran cantidad de muestras para el entrenamiento del modelo.

## Preprocesamiento de imágenes
Se aplicó un script en Python utilizando **OpenCV** para recortar todas las imágenes y eliminar elementos no relevantes.

Se ajustaron los bordes para mantener únicamente la región de interés (ultrasonido), optimizando los datos para su procesamiento posterior.