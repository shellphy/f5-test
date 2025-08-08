import os
import glob

def get_cached_vocos_path(cache_dir="./cache/"):
    """自动检测缓存的Vocos模型路径"""
    vocos_pattern = os.path.join(cache_dir, "models--charactr--vocos-mel-24khz/snapshots/*/")
    vocos_dirs = glob.glob(vocos_pattern)
    if vocos_dirs:
        # 返回第一个找到的Vocos缓存目录
        return vocos_dirs[0].rstrip('/')
    return None

def get_cached_model_path(cache_dir="./cache/", model_name="F5-TTS"):
    """自动检测缓存的F5TTS模型路径"""
    model_pattern = os.path.join(cache_dir, f"models--SWivid--{model_name}/snapshots/*/")
    model_dirs = glob.glob(model_pattern)
    if model_dirs:
        # 在找到的目录中查找模型文件
        for model_dir in model_dirs:
            # 查找 .safetensors 或 .pt 文件
            for ext in ["*.safetensors", "*.pt"]:
                model_files = glob.glob(os.path.join(model_dir, "**", ext), recursive=True)
                if model_files:
                    return model_files[0]  # 返回第一个找到的模型文件
    return None

def main():
    from f5_tts.api import F5TTS
    
    f5tts = F5TTS(
        ckpt_file=get_cached_model_path(),
        vocoder_local_path=get_cached_vocos_path(),
        hf_cache_dir="./cache/"
    )
    
    f5tts.infer(
        ref_file="./basic_ref_zh.wav",
        ref_text="对，这就是我，万人敬仰的太乙真人。",
        gen_text="我的电话是: 1234567890",
        file_wave="./out.wav",
        seed=None,
    )

if __name__ == "__main__":
    main()
