import os
import glob

def get_cached_vocos_path(cache_dir="./cache/"):
    """自动检测缓存的Vocos模型路径"""
    vocos_pattern = os.path.join(cache_dir, "hub/models--charactr--vocos-mel-24khz/snapshots/*/")
    vocos_dirs = glob.glob(vocos_pattern)
    if vocos_dirs:
        # 返回第一个找到的Vocos缓存目录
        return vocos_dirs[0].rstrip('/')
    return None

def main():
    os.environ['HF_HOME'] = "./cache/"
    from f5_tts.api import F5TTS
    
    # 自动检测并使用本地缓存的Vocos模型，避免误导性的下载消息
    vocoder_local_path = get_cached_vocos_path()
    if vocoder_local_path:
        print(f"使用缓存的Vocos模型: {vocoder_local_path}")
        f5tts = F5TTS(vocoder_local_path=vocoder_local_path)
    else:
        print("未找到缓存的Vocos模型，将使用默认下载方式")
        f5tts = F5TTS()
    
    f5tts.infer(
        ref_file="./basic_ref_zh.wav",
        ref_text="对，这就是我，万人敬仰的太乙真人。",
        gen_text="我的电话是: 1234567890",
        file_wave="./out.wav",
        seed=None,
    )

if __name__ == "__main__":
    main()
