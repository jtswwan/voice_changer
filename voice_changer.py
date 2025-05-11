import argparse
import librosa
import soundfile as sf

def change_pitch(input_path, output_path, semitones):
    """
    讀取 input_path，調整音高後輸出到 output_path。
    semitones 正數聲調變高（如模擬年輕、輕快語氣），
    負數聲調變低（如模擬沉穩、安撫語氣）。
    """
    # 讀取音訊，保持原採樣率
    y, sr = librosa.load(input_path, sr=None)
    # 進行音高搬移
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=semitones)
    # 輸出到 WAV 檔
    sf.write(output_path, y_shifted, sr)
    print(f"[完成] {input_path} → {output_path} （移動 {semitones} 半音）")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI 陪伴專案：變聲腳本")
    parser.add_argument("--input",  "-i", required=True, help="輸入 WAV 檔案路徑")
    parser.add_argument("--output", "-o", required=True, help="輸出 WAV 檔案路徑")
    parser.add_argument(
        "--semitones", "-s", type=float, default=0,
        help="半音調整量；正值聲調變高，負值聲調變低"
    )
    args = parser.parse_args()
    change_pitch(args.input, args.output, args.semitones)
