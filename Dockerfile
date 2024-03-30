# Usar la imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de requisitos (requirements.txt) al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual al directorio de trabajo en la imagen
COPY . .

# Exponer el puerto 80 para que la aplicación pueda ser accesible externamente
EXPOSE 80

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80","--reload"]