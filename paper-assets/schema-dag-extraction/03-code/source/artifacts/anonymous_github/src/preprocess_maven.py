# Convert MAVEN event detection JSONL to per-sentence parquet format.
import argparse
import json
import os
from collections import defaultdict

import pandas as pd


def process_document(doc):
    sentences = doc.get("content", [])
    doc_id = doc["id"]

    sent_events = defaultdict(list)
    for event in doc.get("events", []):
        etype = event["type"]
        for mention in event.get("mention", []):
            sid = mention["sent_id"]
            sent_events[sid].append({
                "text": mention["trigger_word"],
                "type": etype,
                "start": mention["offset"][0],
                "end": mention["offset"][1],
            })

    sent_neg = defaultdict(list)
    for neg in doc.get("negative_triggers", []):
        sid = neg["sent_id"]
        sent_neg[sid].append({
            "text": neg["trigger_word"],
            "start": neg["offset"][0],
            "end": neg["offset"][1],
        })

    rows = []
    for sid, sent in enumerate(sentences):
        rows.append({
            "doc_id": doc_id,
            "sent_id": sid,
            "text": sent["sentence"],
            "tokens": sent["tokens"],
            "entities": sent_events.get(sid, []),
            "negative_triggers": sent_neg.get(sid, []),
        })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--split", default=None, help="Process single split (train/valid/test). If None, process all.")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    splits = [args.split] if args.split else ["train", "valid", "test"]

    for split in splits:
        inpath = os.path.join(args.input_dir, f"{split}.jsonl")
        if not os.path.exists(inpath):
            print(f"SKIP {inpath} (not found)")
            continue

        rows = []
        n_docs = 0
        with open(inpath) as f:
            for line in f:
                doc = json.loads(line)
                rows.extend(process_document(doc))
                n_docs += 1

        df = pd.DataFrame(rows)
        outpath = os.path.join(args.output_dir, f"{split}.parquet")
        df.to_parquet(outpath, index=False)
        n_events = sum(len(e) for e in df["entities"])
        print(f"{split}: {n_docs} docs -> {len(df)} sentences, {n_events} event mentions -> {outpath}")


if __name__ == "__main__":
    main()
