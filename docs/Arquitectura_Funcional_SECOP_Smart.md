# Arquitectura Funcional - SECOP Smart

## Objetivo

Desarrollar una plataforma que permita consultar, analizar y realizar seguimiento a los procesos de contratación publicados en SECOP II, mediante filtros avanzados, generación de reportes y futuras capacidades de análisis documental e Inteligencia Artificial.

---

# Arquitectura del sistema

SECOP Smart implementa una arquitectura por capas que desacopla la lógica de negocio del acceso a los datos, facilitando el mantenimiento y la escalabilidad.

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

---

# Módulos del sistema

## Módulo 1 - Búsqueda de procesos

Permite consultar procesos de contratación publicados en SECOP II utilizando diferentes criterios de búsqueda.

### Filtros implementados

| Campo | Estado |
|--------|--------|
| Buscar | ✅ Implementado |
| Estado | ✅ Implementado |
| Tipo de proceso | ✅ Implementado |
| Fecha de publicación (Desde) | ✅ Implementado |
| Fecha de publicación (Hasta) | ✅ Implementado |
| Fecha de presentación de ofertas (Desde) | ✅ Implementado |
| Fecha de presentación de ofertas (Hasta) | ✅ Implementado |

### Filtros planificados

| Campo | Estado |
|--------|--------|
| Datos de la entidad | 🔜 Planeado |
| Número del proceso | 🔜 Planeado |
| Descripción | 🔜 Planeado |
| Código UNSPSC | 🔜 Planeado |
| Departamento | 🔜 Planeado |
| Ciudad | 🔜 Planeado |
| Región | 🔜 Planeado |
| Cuantía | 🔜 Planeado |

---

# Resultado esperado

La búsqueda devuelve una colección de procesos con la siguiente información:

| Campo |
|--------|
| Entidad |
| NIT |
| Departamento |
| Ciudad |
| Número del proceso |
| Objeto |
| Modalidad |
| Estado |
| Fecha de publicación |

---

# Estado actual del proyecto

## Sprint 1 - Backend ✅

### Arquitectura

- Arquitectura por capas.
- Repository Pattern.
- Modelos Pydantic.
- Construcción dinámica de parámetros de búsqueda.

### Integración

- Integración con la API pública de Datos Abiertos de SECOP II.
- Transformación del modelo de datos de SECOP al modelo interno del sistema.

### Funcionalidades implementadas

- Consulta de procesos.
- Búsqueda avanzada.
- Catálogos dinámicos.
- Filtro por estado.
- Filtro por modalidad de contratación.
- Filtro por fecha de publicación.
- Filtro por fecha de presentación de ofertas.

---

## Sprint 2 - Frontend 🚧

Actividades planificadas:

- Layout principal.
- Header.
- Sidebar.
- Formulario de búsqueda.
- Tabla de resultados.
- Consumo de la API REST.
- Paginación.

---

# Funcionalidades futuras

## Reportes

- Exportación de resultados a Excel.
- Exportación a Word.
- Exportación a PDF.

## Gestión documental

- Consulta del detalle del proceso.
- Descarga automática de documentos.
- Organización de documentos por proceso.

## Inteligencia Artificial

- Resumen automático del proceso.
- Análisis documental.
- Comparación de documentos.
- Generación de observaciones técnicas.

## Seguimiento

- Procesos favoritos.
- Alertas de cambios.
- Seguimiento del estado de los procesos.

---

# Próximos Sprints

## Sprint 2

- Desarrollo del frontend en Angular.
- Integración con el backend.
- Visualización de resultados.

## Sprint 3

- Exportación a Excel.
- Paginación.
- Mejoras en la búsqueda.

## Sprint 4

- Descarga de documentos.
- Análisis documental.

## Sprint 5

- Inteligencia Artificial.
- Dashboard e indicadores.