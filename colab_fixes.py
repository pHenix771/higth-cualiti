"""
Fixes y patches específicos para hacer que Clarity Upscaler funcione en Google Colab
"""

import os
import sys
import warnings
import subprocess
from pathlib import Path

def apply_colab_fixes():
    """Aplicar fixes específicos para Colab"""
    print("🔧 Aplicando fixes para Google Colab...")
    
    # Suprimir warnings molestos
    warnings.filterwarnings("ignore", category=UserWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)
    
    # Fix para torch
    try:
        import torch
        if torch.cuda.is_available():
            torch.backends.cudnn.benchmark = True
            torch.backends.cuda.matmul.allow_tf32 = True
    except:
        pass
    
    # Fix para gradio en Colab
    os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
    os.environ['GRADIO_SHARE'] = 'True'
    
    # Fix para memoria
    if 'PYTORCH_CUDA_ALLOC_CONF' not in os.environ:
        os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
    
    print("✅ Fixes aplicados")

def fix_imports():
    """Fix para importaciones problemáticas"""
    try:
        # Patch común para módulos faltantes
        import sys
        import importlib.util
        
        # Crear módulos dummy si faltan
        missing_modules = ['xformers', 'clip', 'ldm']
        
        for module in missing_modules:
            if importlib.util.find_spec(module) is None:
                sys.modules[module] = type(sys)('dummy_' + module)
                
    except Exception as e:
        print(f"Warning en fix_imports: {e}")

def patch_webui_for_colab():
    """Patchear webui.py para mejor compatibilidad con Colab"""
    webui_path = 'webui.py'
    
    if not os.path.exists(webui_path):
        return
    
    try:
        with open(webui_path, 'r') as f:
            content = f.read()
        
        # Patches comunes
        patches = [
            # Forzar share=True para Colab
            ('share=cmd_opts.share', 'share=True'),
            # Forzar server_name para Colab
            ('server_name=initialize_util.gradio_server_name()', 'server_name="0.0.0.0"'),
            # Desactivar auto-launch en Colab
            ('inbrowser=auto_launch_browser', 'inbrowser=False')
        ]
        
        modified = False
        for old, new in patches:
            if old in content and new not in content:
                content = content.replace(old, new)
                modified = True
        
        if modified:
            with open(webui_path + '.bak', 'w') as f:
                f.write(content)  # Backup
            
            with open(webui_path, 'w') as f:
                f.write(content)
            
            print("🔧 webui.py parcheado para Colab")
    
    except Exception as e:
        print(f"Warning: No se pudo patchear webui.py: {e}")

def install_missing_deps():
    """Instalar dependencias faltantes comunes"""
    common_missing = [
        'accelerate',
        'xformers',
        'controlnet-aux',
        'opencv-contrib-python'
    ]
    
    for dep in common_missing:
        try:
            __import__(dep.replace('-', '_'))
        except ImportError:
            try:
                print(f"📦 Instalando {dep}...")
                subprocess.run([sys.executable, '-m', 'pip', 'install', dep, '-q'], 
                             check=False)
            except:
                pass

def optimize_for_colab_gpu():
    """Optimizaciones específicas para GPU de Colab"""
    try:
        import torch
        
        if torch.cuda.is_available():
            # Configuraciones para T4 (GPU común en Colab gratuito)
            device = torch.cuda.get_device_name(0).lower()
            
            if 't4' in device:
                # Optimizaciones para T4
                os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
                os.environ['TORCH_CUDNN_V8_API_ENABLED'] = '1'
                print("🎮 Optimizaciones para T4 aplicadas")
            
            # Limpiar caché de GPU
            torch.cuda.empty_cache()
            
    except Exception as e:
        print(f"Warning en optimización GPU: {e}")

def create_colab_config():
    """Crear configuración específica para Colab"""
    config = {
        "outdir_samples": "/content/outputs",
        "outdir_txt2img_samples": "/content/outputs/txt2img",
        "outdir_img2img_samples": "/content/outputs/img2img",
        "outdir_extras_samples": "/content/outputs/extras",
        "outdir_grids": "/content/outputs/grids",
        "outdir_save": "/content/saved",
        "save_to_dirs": True,
        "grid_save_to_dirs": False,
        "use_original_name_batch": False,
        "enable_pnginfo": True,
        "save_txt": False,
        "samples_filename_pattern": "",
        "save_images_add_number": True,
        "grid_only_if_multiple": True,
        "grid_prevent_empty_spots": False,
        "n_rows": -1,
        "enable_batch_seeds": True,
        "comma_padding_backtrack": 20,
        "CLIP_stop_at_last_layers": 1,
        "upcast_attn": False,
        "auto_launch_browser": "Disable",
        "show_warnings": False,
        "hide_samplers": [],
        "eta_ddim": 0.0,
        "eta_ancestral": 1.0,
        "ddim_discretize": "uniform",
        "s_churn": 0.0,
        "s_tmin": 0.0,
        "s_noise": 1.0,
        "eta_noise_seed_delta": 0,
        "always_discard_next_to_last_sigma": False,
        "uni_pc_variant": "bh1",
        "uni_pc_skip_type": "time_uniform",
        "uni_pc_order": 3,
        "uni_pc_lower_order_final": True
    }
    
    os.makedirs('/content/clarity-upscaler/config', exist_ok=True)
    
    import json
    with open('/content/clarity-upscaler/config/config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("⚙️ Configuración de Colab creada")

def apply_all_fixes():
    """Aplicar todos los fixes necesarios"""
    print("🔧 Aplicando todos los fixes para Colab...")
    
    apply_colab_fixes()
    fix_imports()
    install_missing_deps()
    patch_webui_for_colab()
    optimize_for_colab_gpu()
    create_colab_config()
    
    print("✅ Todos los fixes aplicados correctamente!")

if __name__ == "__main__":
    apply_all_fixes()