import os

def main():
    os.environ['HF_HOME'] = "./cache/"
    from f5_tts.api import F5TTS
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
