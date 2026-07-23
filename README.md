# 🚀 SECOP Smart

SECOP Smart es una plataforma desarrollada para facilitar la consulta, análisis y seguimiento de procesos de contratación pública publicados en **SECOP II**, utilizando la API de Datos Abiertos de Colombia.

El proyecto busca automatizar la búsqueda de oportunidades de contratación, centralizar la información de los procesos y servir como base para futuras funcionalidades como exportación de reportes, análisis documental mediante Inteligencia Artificial y seguimiento de procesos contractuales.

---

# 📌 Características

## Funcionalidades implementadas

- Consulta de procesos de contratación en SECOP II.
- Búsqueda por palabra clave.
- Filtro por estado del proceso.
- Filtro por modalidad de contratación.
- Filtro por fecha de publicación.
- Filtro por fecha de recepción de ofertas.
- Catálogos dinámicos para listas desplegables.
- Arquitectura por capas.
- Repository Pattern.
- Transformación de datos mediante modelos Pydantic.
- API REST documentada automáticamente mediante Swagger.

## Funcionalidades planeadas

- Exportación de resultados a Excel.
- Exportación a Word y PDF.
- Descarga automática de documentos del proceso.
- Dashboard de indicadores.
- Seguimiento de procesos.
- Análisis documental mediante Inteligencia Artificial.

---

# 🏗️ Arquitectura

El proyecto implementa una arquitectura por capas para garantizar una adecuada separación de responsabilidades y facilitar el mantenimiento del sistema.

```text
                Angular
                   │
                   ▼
              FastAPI (API)
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

Expone los endpoints REST y recibe las solicitudes HTTP.

### Services

Contiene la lógica de negocio y transforma la información obtenida desde el repositorio.

### Repositories

Gestiona la comunicación con la API pública de Datos Abiertos de SECOP II.

### Models

Define los modelos de datos utilizando Pydantic.

### Core

Centraliza la configuración del proyecto y las variables de entorno.

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
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── docs/
│   └── Arquitectura_Funcional_SECOP_Smart.md
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

## 2. Ingresar al backend

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

Crear el archivo `.env`

```env
SECOP_API_URL=https://www.datos.gov.co/resource/p6dx-8zbt.json
TIMEOUT=30
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

Obtiene procesos de contratación utilizando filtros básicos.

### Parámetros

| Parámetro | Tipo |
|-----------|------|
| limit | integer |
| buscar | string |
| estado | string |

---

## Obtener catálogos

```http
GET /catalogos/{campo}
```

Permite obtener los valores únicos de un campo para alimentar listas desplegables.

Ejemplos

```http
GET /catalogos/estado_resumen
```

```http
GET /catalogos/modalidad_de_contratacion
```

```http
GET /catalogos/departamento_entidad
```

---

## Búsqueda avanzada

```http
POST /busqueda
```

Permite realizar búsquedas utilizando múltiples filtros simultáneamente.

### Body

| Campo | Tipo |
|--------|------|
| buscar | string |
| estado | string |
| tipo_proceso | string |
| fecha_publicacion_desde | date |
| fecha_publicacion_hasta | date |
| fecha_presentacion_desde | date |
| fecha_presentacion_hasta | date |
| limit | integer |

Ejemplo

```json
{
  "buscar": "puente",
  "estado": "Presentación de oferta",
  "tipo_proceso": "Licitación pública",
  "fecha_publicacion_desde": "2026-01-01",
  "fecha_publicacion_hasta": "2026-01-31",
  "fecha_presentacion_desde": null,
  "fecha_presentacion_hasta": null,
  "limit": 20
}
```

---

# 📊 Estado del proyecto

## ✅ Sprint 1 - Backend (Finalizado)

### Arquitectura

- Arquitectura por capas.
- Repository Pattern.
- Modelos Pydantic.

### Integración

- Integración con la API pública de SECOP II.
- Transformación de datos del modelo de SECOP al modelo interno.

### Funcionalidades implementadas

- Consulta de procesos.
- Catálogos dinámicos.
- Búsqueda avanzada.
- Filtro por estado.
- Filtro por modalidad.
- Filtro por fecha de publicación.
- Filtro por fecha de recepción de ofertas.
- Construcción dinámica de parámetros de búsqueda.

---

## 🚧 Sprint 2 - Frontend (En desarrollo)

Próximas actividades:

- Layout principal.
- Header.
- Sidebar.
- Formulario de búsqueda.
- Tabla de resultados.
- Integración con la API.
- Paginación.

---

# 🗺️ Roadmap

## Backend

- [x] Arquitectura base
- [x] Repository Pattern
- [x] Integración con SECOP II
- [x] Consulta de procesos
- [x] Catálogos dinámicos
- [x] Búsqueda avanzada
- [x] Filtros por estado
- [x] Filtros por modalidad
- [x] Filtros por fechas
- [ ] Paginación
- [ ] Exportación a Excel
- [ ] Descarga de documentos
- [ ] Análisis documental mediante IA

## Frontend

- [ ] Angular
- [ ] Layout principal
- [ ] Dashboard
- [ ] Formulario de búsqueda
- [ ] Tabla de resultados
- [ ] Consumo de la API
- [ ] Paginación

## Inteligencia Artificial

- [ ] Resumen automático de procesos.
- [ ] Clasificación de documentos.
- [ ] Comparación de pliegos.
- [ ] Generación de observaciones técnicas.
- [ ] Asistente para análisis contractual.

---

# 📚 Documentación

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📦 Versiones

**Versión actual**

```
v0.1.0
```

## Historial

| Versión | Estado |
|----------|--------|
| v0.1.0 | Backend MVP finalizado |

---

# 🤝 Contribuciones

Actualmente el proyecto se encuentra en desarrollo activo.

Las contribuciones serán bienvenidas una vez se publique la primera versión estable.

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

# 👨‍💻 Autor

**Fabian Jaimes**

Ingeniero de Sistemas.

Proyecto desarrollado con fines académicos y profesionales para facilitar la consulta, análisis y seguimiento de procesos de contratación pública publicados en SECOP II.