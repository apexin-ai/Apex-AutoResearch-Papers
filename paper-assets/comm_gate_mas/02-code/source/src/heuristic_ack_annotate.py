"""Generate heuristic ack annotations: len(content) < threshold → acknowledgment."""

import argparse
import json
import os


def annotate(traces_path: str, output_dir: str, threshold: int = 30):
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "annotations.jsonl")

    total = 0
    ack_count = 0

    with open(traces_path) as fin, open(out_path, "w") as fout:
        for line in fin:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd == 0:
                    continue
                content = msg.get("content", "")
                is_ack = len(content) < threshold
                label = "acknowledgment" if is_ack else "non_ack"
                total += 1
                if is_ack:
                    ack_count += 1
                entry = {
                    "task_id": task_id,
                    "message_index": rnd - 1,
                    "annotation_a": {"type": label},
                }
                fout.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Annotated {total} messages: {ack_count} ack ({ack_count/total*100:.1f}%), "
          f"{total - ack_count} non_ack ({(total-ack_count)/total*100:.1f}%)")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--traces", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--threshold", type=int, default=30)
    args = parser.parse_args()
    annotate(args.traces, args.output_dir, args.threshold)
