"""DeepSeek-V3 oracle calibration: binary ack classification vs GPT-4o 5-class annotations."""

import json
import os
import random
import time
from collections import defaultdict
from pathlib import Path

from openai import OpenAI

BASE = Path(__file__).resolve().parent.parent
ANNOTATIONS = BASE / "outputs/full_scale/llama_round_robin/annotations/annotations.jsonl"
TRACES = BASE / "outputs/full_scale/llama_round_robin/traces/traces.jsonl"
OUTPUT = BASE / "outputs/deepseek_calibration.json"

SYSTEM_PROMPT = """Classify whether this message in a multi-agent math conversation is an acknowledgment or substantive.

Acknowledgment: simple confirmation, repetition, or agreement that adds no new information, calculations, or reasoning. Restating what was already said without extending it.

Substantive: provides new calculations, reasoning steps, error corrections, verification with explanation, or extends the solution in any way.

Key rules:
1. If a message confirms correctness WITH a substantive explanation or adds new work, classify as substantive.
2. If a message discusses or evaluates the correctness of specific steps or calculations (e.g. "Each step is correctly calculated", "since each box holds 12 cookies"), classify as SUBSTANTIVE — this is verification, not mere acknowledgment.
3. Only classify as acknowledgment if the message is a bare confirmation with no reference to specific solution steps.

Respond with ONLY a JSON object (no markdown, no extra text):
{"is_ack": true, "confidence": 0.9}"""

SEED = 42
N_ACK = 50
N_NONACK = 50


def load_traces():
    traces = {}
    with open(TRACES) as f:
        for line in f:
            d = json.loads(line)
            traces[d["task_id"]] = d["messages"]
    return traces


def load_annotations():
    records = []
    with open(ANNOTATIONS) as f:
        for line in f:
            records.append(json.loads(line))
    return records


def get_message_content(messages, message_index):
    # message_index 0 = round 1, message_index 1 = round 2, etc.
    agent_msgs = [m for m in messages if m["round"] >= 1]
    if message_index < len(agent_msgs):
        return agent_msgs[message_index]["content"]
    return None


def get_prev_message_content(messages, message_index):
    agent_msgs = [m for m in messages if m["round"] >= 1]
    if message_index == 0:
        # Previous is the initial prompt (round 0)
        round0 = [m for m in messages if m["round"] == 0]
        return round0[0]["content"] if round0 else "[start]"
    if message_index - 1 < len(agent_msgs):
        return agent_msgs[message_index - 1]["content"]
    return "[start]"


def classify_with_model(client, model_name, prev_content, content):
    prev_text = (prev_content or "[start]")[:2000]
    curr_text = (content or "")[:3000]
    user_prompt = f"### Previous message:\n{prev_text}\n\n### Current message to classify:\n{curr_text}"

    for attempt in range(3):
        try:
            extra = {}
            if "openrouter.ai" in (client.base_url.host or ""):
                extra["extra_body"] = {
                    "provider": {"order": ["Together", "DeepInfra", "Fireworks"]}
                }
            resp = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=64,
                **extra,
            )
            text = resp.choices[0].message.content.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(text)
            return bool(result["is_ack"]), float(result.get("confidence", 0.5)), None
        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "rate" in err_msg.lower():
                wait = 2 ** (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif "401" in err_msg or ("auth" in err_msg.lower() and "invalid" not in err_msg.lower()):
                print(f"  AUTH ERROR: {err_msg}")
                return False, 0.0, f"auth_error: {err_msg}"
            else:
                print(f"  Attempt {attempt+1} failed: {e}")
                time.sleep(1)

    return False, 0.0, "all_attempts_failed"


def compute_metrics(gpt4o_labels, deepseek_labels):
    tp = fp = fn = tn = 0
    for g, d in zip(gpt4o_labels, deepseek_labels):
        if g and d:
            tp += 1
        elif not g and d:
            fp += 1
        elif g and not d:
            fn += 1
        else:
            tn += 1

    n = len(gpt4o_labels)
    agreement = (tp + tn) / n

    # Cohen's kappa
    p_yes_g = (tp + fn) / n
    p_yes_d = (tp + fp) / n
    p_e = p_yes_g * p_yes_d + (1 - p_yes_g) * (1 - p_yes_d)
    kappa = (agreement - p_e) / (1 - p_e) if p_e < 1 else 1.0

    prec_ack = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec_ack = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1_ack = 2 * prec_ack * rec_ack / (prec_ack + rec_ack) if (prec_ack + rec_ack) > 0 else 0.0

    return {
        "cohens_kappa": round(kappa, 4),
        "raw_agreement": round(agreement, 4),
        "confusion_matrix": {"tp": tp, "fp": fp, "fn": fn, "tn": tn},
        "precision_ack": round(prec_ack, 4),
        "recall_ack": round(rec_ack, 4),
        "f1_ack": round(f1_ack, 4),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Oracle calibration: binary ack classification")
    parser.add_argument("--api-key", type=str, default=None,
                        help="API key (or set ORACLE_API_KEY env var)")
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com/v1",
                        help="API base URL (default: DeepSeek; use http://localhost:PORT/v1 for local vLLM)")
    parser.add_argument("--model", type=str, default="deepseek-chat",
                        help="Model name (default: deepseek-chat)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output file path (default: outputs/MODEL_calibration.json)")
    cli_args = parser.parse_args()

    print("Loading data...")
    traces = load_traces()
    annotations = load_annotations()

    ack_records = [a for a in annotations if a["annotation_a"]["type"] == "acknowledgment"]
    nonack_records = [a for a in annotations if a["annotation_a"]["type"] != "acknowledgment"]

    print(f"Total annotations: {len(annotations)} (ack={len(ack_records)}, non-ack={len(nonack_records)})")

    rng = random.Random(SEED)
    sampled_ack = rng.sample(ack_records, min(N_ACK, len(ack_records)))
    sampled_nonack = rng.sample(nonack_records, min(N_NONACK, len(nonack_records)))
    samples = sampled_ack + sampled_nonack
    rng.shuffle(samples)

    print(f"Sampled {len(samples)} messages ({len(sampled_ack)} ack + {len(sampled_nonack)} non-ack)")

    api_key = [REDACTED] or os.environ.get("ORACLE_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        api_key = "[REDACTED]"
        if "localhost" not in cli_args.base_url:
            raise SystemExit("ERROR: --api-key or ORACLE_API_KEY env var required for remote API")
    model_name = cli_args.model
    output_path = Path(cli_args.output) if cli_args.output else BASE / f"outputs/{model_name.replace('/', '_')}_calibration.json"

    client = OpenAI(api_key=[REDACTED], base_url=cli_args.base_url)
    print(f"Using model={model_name} at {cli_args.base_url}")

    gpt4o_labels = []
    oracle_labels = []
    per_sample = []
    api_errors = 0

    for i, rec in enumerate(samples):
        task_id = rec["task_id"]
        msg_idx = rec["message_index"]
        gpt4o_type = rec["annotation_a"]["type"]
        gpt4o_binary = gpt4o_type == "acknowledgment"

        messages = traces.get(task_id, [])
        content = get_message_content(messages, msg_idx)
        prev_content = get_prev_message_content(messages, msg_idx)

        if content is None:
            print(f"  [{i+1}/{len(samples)}] SKIP {task_id}:msg{msg_idx} - content not found")
            continue

        is_ack, conf, error = classify_with_model(client, model_name, prev_content, content)

        if error:
            api_errors += 1
            if "auth_error" in error:
                print(f"\n  FATAL: API authentication failed. Check your API key.")
                print(f"  Error: {error}")
                raise SystemExit(1)

        gpt4o_labels.append(gpt4o_binary)
        oracle_labels.append(is_ack)

        agree = "✓" if gpt4o_binary == is_ack else "✗"
        print(f"  [{i+1}/{len(samples)}] {agree} gpt4o={gpt4o_type}({'ack' if gpt4o_binary else 'sub'}) oracle={'ack' if is_ack else 'sub'}(conf={conf:.2f}){' ERR' if error else ''}")

        per_sample.append({
            "task_id": task_id,
            "message_index": msg_idx,
            "gpt4o_type": gpt4o_type,
            "gpt4o_binary": gpt4o_binary,
            "oracle_is_ack": is_ack,
            "oracle_confidence": conf,
            "agree": gpt4o_binary == is_ack,
            "error": error,
            "content_preview": content[:200],
        })

        time.sleep(0.5)

    if api_errors > 0:
        print(f"\nWARNING: {api_errors}/{len(samples)} API calls failed (defaulted to non-ack)")
        if api_errors == len(samples):
            print("ALL API calls failed — results are invalid. Check API key and endpoint.")
            raise SystemExit(1)

    metrics = compute_metrics(gpt4o_labels, oracle_labels)

    disagree_by_type = defaultdict(lambda: {"total": 0, "disagree": 0})
    for s in per_sample:
        t = s["gpt4o_type"]
        disagree_by_type[t]["total"] += 1
        if not s["agree"]:
            disagree_by_type[t]["disagree"] += 1

    result = {
        "n_samples": len(gpt4o_labels),
        "api_errors": api_errors,
        **metrics,
        "oracle_model": model_name,
        "oracle_base_url": cli_args.base_url,
        "reference_model": "gpt-4o (5-class → binary)",
        "disagreement_by_gpt4o_type": {
            k: {"total": v["total"], "disagree": v["disagree"],
                "disagree_rate": round(v["disagree"] / v["total"], 4) if v["total"] > 0 else 0}
            for k, v in disagree_by_type.items()
        },
        "per_sample_results": per_sample,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"Model:          {model_name}")
    print(f"Cohen's κ:      {metrics['cohens_kappa']}")
    print(f"Raw agreement:  {metrics['raw_agreement']}")
    print(f"Confusion:      {metrics['confusion_matrix']}")
    print(f"Precision(ack): {metrics['precision_ack']}")
    print(f"Recall(ack):    {metrics['recall_ack']}")
    print(f"F1(ack):        {metrics['f1_ack']}")
    print(f"API errors:     {api_errors}/{len(samples)}")
    print(f"\nDisagreement by GPT-4o type:")
    for t, v in sorted(disagree_by_type.items(), key=lambda x: -x[1]["disagree"]):
        print(f"  {t:25s}: {v['disagree']}/{v['total']} disagree ({v['disagree']/v['total']*100:.1f}%)")
    verdict = "PASS" if metrics["cohens_kappa"] >= 0.85 else "FAIL"
    print(f"\nVerdict: {verdict} (threshold κ ≥ 0.85)")
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
