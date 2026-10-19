"""Extract text embeddings from AdvBench traces using all-MiniLM-L6-v2.

Output format matches existing pipeline: .pkl dict mapping trace_id -> ndarray(T, 384).

Usage:
    # Full extraction
    python -m src.advbench.extract_text_embeddings

    # Custom output
    python -m src.advbench.extract_text_embeddings --output artifacts/r1_8b_text_emb_new.pkl

    # Dry-run
    python -m src.advbench.extract_text_embeddings --dry-run
"""

import argparse
import pickle
from collections import defaultdict

import numpy as np
from sentence_transformers import SentenceTransformer

HF_DATASET = "ishitakakkar-10/HarmThoughts"
TARGET_MODEL = "r1-8b"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
DEFAULT_OUTPUT = "DATA_DIR/artifacts/r1_8b_text_emb_all.pkl"
SAFETY_LABELS = {"RA", "AL", "CC", "ED", "IA"}


def load_traces(model_name: str = TARGET_MODEL):
    from datasets import load_dataset

    ds = load_dataset(HF_DATASET, split="train")
    traces_raw = defaultdict(list)
    for row in ds:
        if row["model_name"] != model_name:
            continue
        sid = row["sentence_id"]
        parts = sid.rsplit("-", 1)
        trace_id = parts[0]
        step_idx = int(parts[1]) - 1

        traces_raw[trace_id].append({
            "step_idx": step_idx,
            "sentence": row["sentence"],
        })

    traces = {}
    for trace_id, steps in traces_raw.items():
        steps.sort(key=lambda x: x["step_idx"])
        traces[trace_id] = [s["sentence"] for s in steps]

    return traces


def main():
    parser = argparse.ArgumentParser(
        description="Extract text embeddings from R1-8B traces using MiniLM-L6-v2"
    )
    parser.add_argument("--model", default=EMBEDDING_MODEL)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-size", type=int, default=128,
                        help="Sentences per batch for encoding")
    parser.add_argument("--dry-run", action="store_true",
                        help="Process only 2 traces")
    args = parser.parse_args()

    print("Loading traces from HarmThoughts...")
    traces = load_traces()
    print(f"Loaded {len(traces)} traces")

    if args.dry_run:
        trace_ids = list(traces.keys())[:2]
        traces = {k: traces[k] for k in trace_ids}
        print(f"Dry-run: processing {len(traces)} traces")

    print(f"Loading embedding model: {args.model}")
    encoder = SentenceTransformer(args.model)

    all_sentences = []
    sentence_map = []  # (trace_id, step_idx)
    for trace_id, sentences in traces.items():
        for step_idx, sent in enumerate(sentences):
            all_sentences.append(sent)
            sentence_map.append((trace_id, step_idx))

    print(f"Encoding {len(all_sentences)} sentences...")
    embeddings = encoder.encode(
        all_sentences,
        batch_size=args.batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
    )

    result = {}
    for (trace_id, step_idx), emb in zip(sentence_map, embeddings):
        if trace_id not in result:
            result[trace_id] = {}
        result[trace_id][step_idx] = emb

    output_dict = {}
    for trace_id, step_embs in result.items():
        n_steps = max(step_embs.keys()) + 1
        arr = np.zeros((n_steps, EMBEDDING_DIM), dtype=np.float32)
        for idx, emb in step_embs.items():
            arr[idx] = emb
        output_dict[trace_id] = arr

    if args.dry_run:
        for tid, arr in output_dict.items():
            print(f"  {tid}: shape={arr.shape} dtype={arr.dtype}")

    with open(args.output, "wb") as f:
        pickle.dump(output_dict, f)
    print(f"Saved {len(output_dict)} trace embeddings to {args.output}")


if __name__ == "__main__":
    main()
