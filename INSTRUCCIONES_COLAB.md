# 📝 Instrucciones Detalladas para Google Colab

## 🚀 Guía Paso a Paso

### ¿Qué es Clarity Upscaler?

Clarity Upscaler es una herramienta de inteligencia artificial que mejora y aumenta la resolución de imágenes. Es una alternativa gratuita y open-source a herramientas comerciales como Magnific AI.

### ¿Por qué esta implementación para Colab?

Google Colab es una plataforma gratuita que ofrece:
- GPUs potentes sin costo
- Entorno Python pre-configurado
- Acceso fácil desde cualquier navegador
- No requiere instalación local

---

## 📋 Pre-requisitos

### 1. Cuenta de Google
- Necesitas una cuenta de Gmail/Google
- Colab funciona directamente desde el navegador

### 2. Habilitar GPU en Colab
```
1. Ve a "Runtime" en el menú superior
2. Selecciona "Change runtime type"
3. En "Hardware accelerator" selecciona "GPU" 
4. Haz clic en "Save"
```

### 3. Verificar GPU
Ejecuta esta celda para verificar que tienes GPU:
```python
import torch
print("GPU disponible:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
```

---

## 🔧 Proceso de Instalación

### Tiempo Estimado: 5-10 minutos

La instalación incluye:
1. **Verificación del sistema** (30 segundos)
2. **Instalación de PyTorch** (2-3 minutos)
3. **Clonado del repositorio** (1 minuto)
4. **Instalación de dependencias** (3-4 minutos)
5. **Descarga de modelos** (2-5 minutos)
6. **Configuración para Colab** (30 segundos)

### Indicadores de Progreso

✅ **"GPU detectada"** = Todo bien
⚠️ **Warnings amarillos** = Normal, continúa
❌ **Errores rojos** = Problema, revisa troubleshooting

---

## 🎯 Usando la Interfaz

### 1. Acceso a la Interfaz
- Busca el mensaje "Running on public URL:"
- Haz clic en el enlace que aparece
- Se abrirá la interfaz web de Clarity

### 2. Subir Imagen
```
1. Haz clic en el área de "Upload Image"
2. Selecciona tu imagen desde tu computadora
3. Formatos soportados: JPG, PNG, WebP
4. Tamaño recomendado: < 2048x2048 px
```

### 3. Configurar Parámetros

**Parámetros Básicos:**
- **Scale Factor**: Cuánto aumentar el tamaño (2x, 4x)
- **Strength**: Intensidad del efecto (0.1 - 1.0)
- **Steps**: Calidad vs velocidad (18-50 pasos)

**Parámetros Avanzados:**
- **CFG Scale**: Control de adherencia al prompt
- **Seed**: Para reproducir resultados
- **Sampler**: Algoritmo de generación

### 4. Generar
```
1. Haz clic en "Generate"
2. Espera el procesamiento (1-5 minutos)
3. El resultado aparecerá abajo
4. Haz clic derecho → "Save image as" para descargar
```

---

## ⚠️ Limitaciones y Consideraciones

### Colab Gratuito
- **Memoria GPU**: ~15GB
- **Tiempo de sesión**: 12 horas máximo
- **Inactividad**: Se desconecta después de ~90 minutos
- **Cola**: Puede haber espera en horarios pico

### Optimizaciones para T4 (GPU común en Colab gratuito)
- Usa imágenes ≤ 1024x1024 para mejor rendimiento
- Scale factor 2x es más rápido que 4x
- Menos pasos = más rápido pero menor calidad

### Gestión de Memoria
```python
# Si te quedas sin memoria, ejecuta:
import torch
torch.cuda.empty_cache()
```

---

## 🔧 Troubleshooting

### Error: "No GPU detected"
```
Causa: GPU no habilitada
Solución: Runtime → Change runtime type → GPU → Save
Luego: Runtime → Restart runtime
```

### Error: "CUDA out of memory"
```
Causa: Imagen muy grande o parámetros muy altos
Solución:
- Reduce el tamaño de imagen
- Baja el scale factor
- Reduce los steps
- Reinicia el runtime
```

### Error: "Module not found"
```
Causa: Instalación incompleta
Solución:
- Ejecuta todas las celdas desde el principio
- Verifica que no haya errores en las instalaciones
```

### Error: "Connection failed"
```
Causa: Colab perdió conexión
Solución:
- Recarga la página de Colab
- Ejecuta la celda de lanzamiento nuevamente
```

### Interfaz no carga
```
Causa: Puerto bloqueado o proceso no iniciado
Solución:
- Espera más tiempo (hasta 5 minutos)
- Busca la URL pública en los logs
- Ejecuta el método alternativo de lanzamiento
```

---

## 📊 Calidad vs Rendimiento

### Para Velocidad Máxima:
```
- Scale Factor: 2x
- Steps: 18-25
- CFG Scale: 6-7
- Imagen: ≤ 512x512
```

### Para Calidad Máxima:
```
- Scale Factor: 4x
- Steps: 40-50
- CFG Scale: 7-9
- Imagen: ≤ 1024x1024
```

### Equilibrio Recomendado:
```
- Scale Factor: 2x
- Steps: 30
- CFG Scale: 7
- Imagen: ≤ 768x768
```

---

## 🔄 Reiniciar y Actualizar

### Reiniciar Sesión
```python
# Si algo no funciona:
# 1. Runtime → Restart runtime
# 2. Ejecuta todas las celdas de nuevo
```

### Actualizar Código
```python
# Para obtener la última versión:
%cd /content
!rm -rf clarity-upscaler
# Luego ejecuta las celdas de instalación de nuevo
```

### Limpiar Memoria
```python
import gc
import torch

gc.collect()
torch.cuda.empty_cache()
print("Memoria limpia")
```

---

## 💡 Consejos Avanzados

### 1. Batch Processing
Para procesar múltiples imágenes, usa la función de carpeta si está disponible.

### 2. Guardar Configuraciones
Anota tus configuraciones favoritas para futuros usos.

### 3. Monitorear Recursos
```python
# Ver uso de GPU
!nvidia-smi
```

### 4. Acelerar Cargas Futuras
Los modelos se cachean, por lo que las siguientes ejecuciones serán más rápidas.

---

## 📱 Uso desde Móvil

### Colab en Móvil
- Funciona en navegadores móviles
- La interfaz se adapta a pantallas pequeñas
- Subida de imágenes desde galería del teléfono

### Consideraciones Móviles
- Conexión estable recomendada
- Las descargas van a la carpeta de descargas del navegador

---

## 🎨 Casos de Uso Comunes

### 1. Mejorar Fotos Antiguas
- Digitalizar fotos familiares viejas
- Aumentar resolución de imágenes escaneadas

### 2. Upscaling para Impresión
- Preparar imágenes para impresión en gran formato
- Mejorar texturas y detalles

### 3. Contenido Digital
- Mejorar thumbnails de videos
- Optimizar imágenes para web de alta resolución

### 4. Arte Digital
- Refinar ilustraciones digitales
- Mejorar screenshots de juegos

---

¿Tienes más preguntas? ¡Crea un issue en el repositorio!