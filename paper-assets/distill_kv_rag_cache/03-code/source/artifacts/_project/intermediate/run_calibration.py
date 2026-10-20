"""Run KVTC PCA calibration on a set of texts and save the result.

Usage:
    python scripts/run_calibration.py \
        --model meta-llama/Llama-3.1-8B-Instruct \
        --output /root/autodl-tmp/compresslink/calibration/ \
        --num-samples 10
"""

import argparse
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from compresslink.calibration import KVTCCalibrator


DEFAULT_CALIBRATION_TEXTS = [
    "The history of artificial intelligence began in antiquity, with myths and stories of artificial beings endowed with intelligence.",
    "Machine learning is a subset of artificial intelligence that provides systems the ability to learn and improve from experience.",
    "Natural language processing is a subfield of linguistics, computer science, and artificial intelligence concerned with interactions between computers and human language.",
    "Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning.",
    "Reinforcement learning is an area of machine learning concerned with how intelligent agents ought to take actions in an environment.",
    "Computer vision is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.",
    "Robotics is an interdisciplinary branch of computer science and engineering that involves the design, construction, operation, and use of robots.",
    "Quantum computing is the use of quantum phenomena such as superposition and entanglement to perform computation.",
    "Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior.",
    "Information retrieval is the activity of obtaining information system resources that are relevant to an information need from a collection.",
    "Knowledge representation and reasoning is the field of artificial intelligence dedicated to representing information about the world in a form that a computer system can use.",
    "The Transformer architecture was introduced in the paper 'Attention Is All You Need' and has since become the dominant architecture in natural language processing.",
]


def main():
    parser = argparse.ArgumentParser(description="Run KVTC PCA calibration")
    parser.add_argument("--model", type=str, default="meta-llama/Llama-3.1-8B-Instruct")
    parser.add_argument("--output", type=str, default="/root/autodl-tmp/compresslink/calibration/")
    parser.add_argument("--num-samples", type=int, default=10)
    parser.add_argument("--data", type=str, default=None, help="JSONL file; uses 'context' field as calibration text")
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    print(f"Loading model {args.model} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch_dtype,
        device_map="auto",
    )

    if args.data:
        texts = []
        with open(args.data) as f:
            for line in f:
                rec = json.loads(line)
                texts.append(rec["context"])
                if len(texts) >= args.num_samples:
                    break
    else:
        texts = DEFAULT_CALIBRATION_TEXTS

    calibrator = KVTCCalibrator(
        model=model,
        tokenizer=tokenizer,
        num_samples=args.num_samples,
        save_dir=args.output,
    )

    print(f"Collecting NoPE KV from {min(len(texts), args.num_samples)} samples ...")
    kv_data = calibrator.collect_nope_kv(texts)

    print("Computing PCA ...")
    calibration = calibrator.compute_pca(kv_data)

    save_path = str(Path(args.output) / "calibration.pt")
    calibrator.save(calibration, save_path)
    print(f"Saved calibration to {save_path}")

    num_entries = len(calibration)
    sample_key = next(iter(calibration))
    sample = calibration[sample_key]
    explained = sample["eigenvalues"].cumsum(0) / sample["eigenvalues"].sum()
    dim_90 = (explained < 0.9).sum().item() + 1
    print(f"  {num_entries} entries (layer, head, kind)")
    print(f"  Example {sample_key}: 90% variance in {dim_90}/{sample['eigenvalues'].shape[0]} dims")


if __name__ == "__main__":
    main()
