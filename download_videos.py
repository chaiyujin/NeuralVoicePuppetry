import os
import time
import argparse
import numpy as np
import pandas as pd


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-S", "--source_excel", type=str, required=True)
    parser.add_argument("-O", "--output_dir",   type=str, required=True)
    args = parser.parse_args()

    df = pd.read_excel(args.source_excel)
    idx = list(df.columns.values).index("Filename")
    for i, record in enumerate(df.values):
        filename = record[idx]
        year = filename[3:7]
        date = filename[7:11]
        url = f"https://download.media.tagesschau.de/video/{year}/{date}/{filename}.mp4"
        out = os.path.join(args.output_dir, f"Sequence_{i+1:03d}.mp4")
        if os.path.exists(out):
            continue

        print("[download]", url)
        os.makedirs(args.output_dir, exist_ok=True)
        os.system(f"youtube-dl --proxy socks5://127.0.0.1:1080 \"{url}\" --output \"{out}\"")
