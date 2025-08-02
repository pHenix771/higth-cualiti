#!/usr/bin/env python3
"""
Clarity Upscaler - Script de configuración para Google Colab
Autor: Adaptación para Colab del proyecto original de philz1337x
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
import shutil
from pathlib import Path
import torch
import json

class ColabSetup:
    def __init__(self):
        self.base_dir = '/content/clarity-upscaler'
        self.models_dir = os.path.join(self.base_dir, 'models')
        
    def check_gpu(self):
        """Verificar disponibilidad de GPU"""
        print("🔧 Verificando configuración del sistema...")
        
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✅ GPU detectada: {gpu_name}")
            print(f"🚀 Memoria GPU: {gpu_memory:.1f} GB")
            return True
        else:
            print("⚠️ ¡ADVERTENCIA! No se detectó GPU.")
            print("Ve a Runtime → Change runtime type → Hardware accelerator → GPU")
            return False
    
    def install_dependencies(self):
        """Instalar dependencias necesarias"""
        print("📦 Instalando dependencias...")
        
        # Actualizar pip
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        
        # Dependencias críticas
        critical_deps = [
            'torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118',
            'transformers==4.30.2',
            'accelerate',
            'diffusers',
            'gradio==3.41.2',
            'fastapi',
            'pillow',
            'numpy',
            'opencv-python',
            'scipy',
            'scikit-image',
            'omegaconf',
            'einops',
            'safetensors'
        ]
        
        for dep in critical_deps:
            try:
                print(f"Installing: {dep}")
                subprocess.run([sys.executable, '-m', 'pip', 'install'] + dep.split(), 
                             check=False, capture_output=True)
            except Exception as e:
                print(f"Warning: Could not install {dep}: {e}")
    
    def clone_repository(self):
        """Clonar el repositorio de Clarity Upscaler"""
        os.chdir('/content')
        
        if os.path.exists('clarity-upscaler'):
            print("📁 Repositorio ya existe, actualizando...")
            os.chdir('clarity-upscaler')
            subprocess.run(['git', 'pull'], check=False)
        else:
            print("📂 Clonando repositorio...")
            subprocess.run(['git', 'clone', 'https://github.com/philz1337x/clarity-upscaler.git'], 
                         check=True)
        
        os.chdir('/content/clarity-upscaler')
    
    def install_requirements(self):
        """Instalar requirements.txt del proyecto"""
        print("📋 Instalando requirements del proyecto...")
        
        if os.path.exists('requirements.txt'):
            try:
                with open('requirements.txt', 'r') as f:
                    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                
                for req in requirements:
                    try:
                        subprocess.run([sys.executable, '-m', 'pip', 'install', req], 
                                     check=False, capture_output=True)
                    except:
                        pass  # Continuar si hay errores menores
            except Exception as e:
                print(f"Warning: Error installing requirements: {e}")
    
    def setup_models(self):
        """Configurar directorios de modelos"""
        print("🤖 Configurando directorios de modelos...")
        
        model_dirs = [
            'models/Stable-diffusion',
            'models/ControlNet',
            'models/Lora',
            'models/ESRGAN',
            'models/VAE'
        ]
        
        for dir_name in model_dirs:
            os.makedirs(dir_name, exist_ok=True)
        
        # Ejecutar script de descarga si existe
        if os.path.exists('download_weights.py'):
            try:
                subprocess.run([sys.executable, 'download_weights.py'], 
                             check=False, timeout=600)
            except Exception as e:
                print(f"Warning: Error en download_weights.py: {e}")
    
    def configure_for_colab(self):
        """Configurar para Google Colab"""
        print("⚙️ Configurando para Google Colab...")
        
        # Variables de entorno
        env_vars = {
            'GRADIO_SERVER_NAME': '0.0.0.0',
            'GRADIO_SERVER_PORT': '7860',
            'CUDA_VISIBLE_DEVICES': '0',
            'PYTORCH_CUDA_ALLOC_CONF': 'max_split_size_mb:128',
            'SD_WEBUI_RESTARTING': '1'
        }
        
        for key, value in env_vars.items():
            os.environ[key] = value
        
        # Agregar directorio actual al Python path
        current_dir = os.getcwd()
        if current_dir not in sys.path:
            sys.path.append(current_dir)
    
    def create_launch_script(self):
        """Crear script de lanzamiento optimizado para Colab"""
        launch_script = '''
import os
import sys
import argparse

# Configurar argumentos para Colab
args = [
    "--listen",
    "--port", "7860", 
    "--share",
    "--enable-insecure-extension-access",
    "--no-half-vae",
    "--opt-split-attention",
    "--disable-console-progressbars",
    "--no-download-sd-model"
]

# Configurar sys.argv
sys.argv = ["webui.py"] + args

# Importar y ejecutar webui
if __name__ == "__main__":
    exec(open("webui.py").read())
'''
        
        with open('launch_colab.py', 'w') as f:
            f.write(launch_script)
        
        print("🚀 Script de lanzamiento creado")
    
    def run_setup(self):
        """Ejecutar configuración completa"""
        print("🎯 Iniciando configuración de Clarity Upscaler para Colab...")
        
        try:
            self.check_gpu()
            self.install_dependencies()
            self.clone_repository()
            self.install_requirements()
            self.setup_models()
            self.configure_for_colab()
            self.create_launch_script()
            
            print("\n✅ ¡Configuración completada exitosamente!")
            print("🚀 Ahora puedes ejecutar: python launch_colab.py")
            print("🌐 O usar el notebook para lanzar la interfaz")
            
        except Exception as e:
            print(f"\n❌ Error en la configuración: {e}")
            print("🔧 Intenta ejecutar las secciones individualmente")

if __name__ == "__main__":
    setup = ColabSetup()
    setup.run_setup()