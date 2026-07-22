# 🚀 SECOP Smart

SECOP Smart es una plataforma desarrollada para facilitar la consulta, análisis y seguimiento de procesos de contratación pública publicados en **SECOP II**, utilizando la API de Datos Abiertos de Colombia.

El objetivo es automatizar la búsqueda de oportunidades de contratación, analizar la información de los procesos y generar reportes que apoyen la toma de decisiones.

---

# 📌 Características

- Consulta de procesos de contratación en SECOP II.
- Filtros dinámicos para la búsqueda de procesos.
- Catálogos dinámicos para alimentar los filtros del frontend.
- Arquitectura desacoplada mediante FastAPI.
- Preparado para integración con Angular.
- Base para exportación a Excel, Word y PDF.
- Preparado para futuras funcionalidades con Inteligencia Artificial.

---

# 🏗️ Arquitectura

El proyecto sigue una arquitectura por capas que permite mantener una clara separación de responsabilidades.

```text
Angular
    │
    ▼
FastAPI
    │
    ▼
Services
    │
    ▼
Repositories
    │
    ▼
API Datos Abiertos SECOP II
```

## Capas

### API (Routes)

Recibe las solicitudes HTTP y expone los endpoints del sistema.

### Services

Contiene la lógica de negocio y transforma la información antes de enviarla al cliente.

### Repositories

Gestiona la comunicación con la API de Datos Abiertos de SECOP II.

### Models

Define los modelos de datos mediante Pydantic.

### Core

Centraliza la configuración del proyecto.

---

# 🛠️ Tecnologías

## Backend

- Python 3.13
- FastAPI
- HTTPX
- Pydantic
- Pandas
- OpenPyXL
- Uvicorn

## Frontend (Próximamente)

- Angular
- Angular Material
- Tailwind CSS

---

# 📁 Estructura del proyecto

```text
secop-smart/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│
├── README.md
└── .gitignore
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/secop-smart.git
```

## 2. Ingresar al proyecto

```bash
cd secop-smart/backend
```

## 3. Crear el entorno virtual

Windows

```bash
python -m venv venv
```

Activar

```bash
venv\Scripts\activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 5. Configurar variables de entorno

Crear un archivo `.env`

```env
SECOP_API_URL=https://www.datos.gov.co/resource/p6dx-8zbt.json
```

## 6. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

---

# 📡 Endpoints implementados

## Obtener procesos

```http
GET /procesos
```

### Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| limit | Número de registros |
| buscar | Palabra clave |
| estado | Estado del proceso |

### Ejemplo

```http
GET /procesos?buscar=puente&estado=Presentación de oferta&limit=20
```

---

## Obtener catálogos

```http
GET /catalogos/{campo}
```

Ejemplos

```http
GET /catalogos/estado_del_procedimiento
```

```http
GET /catalogos/modalidad_de_contratacion
```

```http
GET /catalogos/departamento_entidad
```

Este endpoint devuelve los valores únicos del campo solicitado para alimentar listas desplegables en el frontend.

---

# 📊 Estado actual del proyecto

## Backend

- ✅ Arquitectura FastAPI
- ✅ Repository Pattern
- ✅ Configuración centralizada
- ✅ Integración con SECOP II
- ✅ Consulta de procesos
- ✅ Modelos Pydantic
- ✅ Catálogos dinámicos

## Frontend

- ⏳ En desarrollo

---

# 🗺️ Roadmap

## Backend

- [x] Arquitectura base
- [x] Integración con SECOP II
- [x] Consulta de procesos
- [x] Catálogos dinámicos
- [ ] Filtros dinámicos avanzados
- [ ] Paginación
- [ ] Exportación a Excel
- [ ] Descarga de documentos
- [ ] Análisis documental

## Frontend

- [ ] Angular
- [ ] Dashboard
- [ ] Búsqueda avanzada
- [ ] Visualización de procesos
- [ ] Exportación de resultados

## Inteligencia Artificial

- [ ] Resumen automático de procesos
- [ ] Análisis de pliegos
- [ ] Comparación de documentos
- [ ] Generación de observaciones técnicas

---

# 📚 Documentación

FastAPI genera automáticamente la documentación de la API.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🤝 Contribuciones

Actualmente este proyecto se encuentra en desarrollo. Las contribuciones serán bienvenidas una vez se publique la primera versión estable.

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

# 👨‍💻 Autor

**Fabian Jaimes**

Ingeniero de Sistemas con experiencia en el desarrollo de soluciones tecnológicas orientadas a la automatización de procesos, análisis de información y transformación digital.

Proyecto desarrollado con fines académicos y profesionales para facilitar la consulta, análisis y seguimiento de procesos de contratación pública publicados en SECOP II.