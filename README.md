# 🔎 Clarity AI | Image Upscaler & Enhancer para Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu-repo/clarity-upscaler-colab/blob/main/Clarity_Upscaler_Colab.ipynb)

## 🌟 Descripción

Esta es una implementación optimizada de **Clarity Upscaler** para funcionar perfectamente en **Google Colab**. Clarity AI es una alternativa gratuita y open-source a Magnific para mejorar y hacer upscaling de imágenes usando inteligencia artificial.

### ✨ Características

- 🚀 **Fácil de usar**: Solo ejecuta las celdas del notebook en orden
- 🎯 **Optimizado para Colab**: Configuraciones específicas para GPUs T4
- 🔧 **Sin errores**: Manejo automático de dependencias y conflictos
- 🌐 **Interfaz web**: Gradio UI accesible desde el navegador
- 💻 **Gratuito**: Funciona en la versión gratuita de Google Colab

## 🚀 Inicio Rápido

### Opción 1: Usar el Notebook (Recomendado)

1. **Abre el notebook en Colab**: [Clarity_Upscaler_Colab.ipynb](./Clarity_Upscaler_Colab.ipynb)
2. **Habilita GPU**: Runtime → Change runtime type → Hardware accelerator → GPU
3. **Ejecuta las celdas en orden**: Comenzando desde la primera celda
4. **Espera la instalación**: Puede tomar 5-10 minutos la primera vez
5. **¡Disfruta!**: Una vez que aparezca la URL pública, haz clic para acceder

### Opción 2: Instalación Manual

Si prefieres más control, puedes usar los scripts de configuración:

```python
# En una celda de Colab
!git clone https://github.com/tu-repo/clarity-upscaler-colab.git
%cd clarity-upscaler-colab
!python colab_setup.py
```

## 📋 Requisitos

- **Google Colab** (gratuito o Pro)
- **GPU habilitada** (obligatorio)
- **Conexión a internet** estable

## 🔧 Solución de Problemas

### Errores Comunes

**❌ "No GPU detected"**
```
Solución: Runtime → Change runtime type → Hardware accelerator → GPU → Save
```

**❌ "Out of memory"**
```
Solución: Reduce el tamaño de la imagen de entrada o reinicia el runtime
```

**❌ "Module not found"**
```
Solución: Ejecuta la celda de troubleshooting o reinicia completamente
```

**❌ "Connection timeout"**
```
Solución: Espera más tiempo o reinicia la sesión de Colab
```

### Script de Diagnóstico

```python
# Ejecuta esto en una celda para diagnóstico
!python -c "
import torch
print('GPU disponible:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('GPU:', torch.cuda.get_device_name(0))
    print('Memoria:', torch.cuda.get_device_properties(0).total_memory / 1e9, 'GB')
"
```

## 📖 Cómo Usar

1. **Sube tu imagen**: Arrastra o haz clic para subir una imagen
2. **Ajusta parámetros**: Modifica la configuración según tus necesidades
3. **Haz clic en Generate**: Espera el procesamiento (puede tomar varios minutos)
4. **Descarga el resultado**: Guarda tu imagen mejorada

### 💡 Consejos para Mejores Resultados

- **Calidad de entrada**: Usa imágenes de buena calidad
- **Tamaño moderado**: En Colab gratuito, evita imágenes muy grandes (>2048px)
- **Paciencia**: El primer uso puede tardar más por la descarga de modelos
- **Experimentación**: Prueba diferentes configuraciones

## 📁 Estructura del Proyecto

```
clarity-upscaler-colab/
├── Clarity_Upscaler_Colab.ipynb    # Notebook principal
├── colab_setup.py                  # Script de configuración
├── colab_fixes.py                  # Fixes específicos para Colab
├── README.md                       # Este archivo
└── examples/                       # Imágenes de ejemplo
```

## ⚠️ Limitaciones en Colab Gratuito

- **Memoria GPU**: ~15GB (suficiente para la mayoría de casos)
- **Tiempo de sesión**: ~12 horas máximo
- **Desconexión por inactividad**: ~90 minutos
- **Recursos limitados**: Puede ser lento en horarios pico

## 🔄 Actualizaciones

Para obtener la última versión:

```python
# En Colab
%cd /content
!rm -rf clarity-upscaler  # Solo si existe una versión anterior
!git clone https://github.com/philz1337x/clarity-upscaler.git
```

## 🤝 Contribuir

Si encuentras errores o tienes mejoras:

1. Abre un Issue describiendo el problema
2. Fork este repositorio
3. Haz tus cambios
4. Envía un Pull Request

## 📄 Licencias

- **Este proyecto**: MIT License
- **Clarity Upscaler original**: [AGPL-3.0](https://github.com/philz1337x/clarity-upscaler/blob/main/LICENSE.txt)

## 🙏 Créditos

- **Autor original**: [philz1337x](https://github.com/philz1337x)
- **Repositorio original**: [clarity-upscaler](https://github.com/philz1337x/clarity-upscaler)
- **Adaptación para Colab**: Tu servidor E1

## 📞 Soporte

Si necesitas ayuda:

1. **Revisa la sección de troubleshooting** arriba
2. **Busca en Issues** existentes
3. **Crea un nuevo Issue** si no encuentras solución
4. **Sígueme** para actualizaciones

---

## 🌟 ¿Te ha sido útil?

Si este proyecto te ha ayudado, considera:

- ⭐ **Dar una estrella** al repositorio
- 🔄 **Compartir** con otros desarrolladores  
- 🐦 **Seguir** en redes sociales para actualizaciones

---

**¡Happy upscaling! 🎨✨**