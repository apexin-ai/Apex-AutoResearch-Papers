"""Diversity Probe: 验证 SFT 模型在不同 temperature 下的输出多样性。

用法:
  CUDA_VISIBLE_DEVICES=2 python /root/autodl-tmp/scripts/diversity_probe.py
"""

import json
import itertools
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

sys.path.insert(0, "/root/autodl-tmp")

from freige.data.docred_processor import DocREDProcessor

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)

BASE_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
SFT_ADAPTER = "/root/autodl-tmp/sft_output"
DATA_DIR = "/root/autodl-tmp/data/docred"
OUTPUT_DIR = "/root/autodl-tmp/artifacts"
NUM_GENERATIONS = 8
TEMPERATURES = [0.7, 1.0]
MAX_NEW_TOKENS = 1024
NUM_SAMPLES = 3


def load_model():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading model (4-bit)...")
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        trust_remote_code=True,
        attn_implementation="sdpa",
        device_map="auto",
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        ),
    )

    print("Loading & merging SFT adapter...")
    model = PeftModel.from_pretrained(model, SFT_ADAPTER)
    model = model.merge_and_unload()
    model.eval()
    print("Model ready.")
    return model, tokenizer


def select_samples(data_dir, tokenizer, n=5):
    """选择不同复杂度的文档样本。"""
    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process("train")
    groups = processor.group_by_document(samples)

    doc_info = []
    for doc_id, doc_samples in groups.items():
        sft = processor.format_sft_sample(doc_samples)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{sft['instruction']}\n\n{sft['input']}"},
        ]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )
        gold_triples = json.loads(sft["output"])
        n_sents = len(doc_samples[0].sents)
        doc_info.append({
            "doc_id": doc_id,
            "prompt": prompt,
            "gold_triples": gold_triples,
            "gold_json": sft["output"],
            "n_triples": len(gold_triples),
            "n_sents": n_sents,
        })

    doc_info.sort(key=lambda x: x["n_triples"])
    total = len(doc_info)
    indices = [
        int(total * 0.15),
        int(total * 0.35),
        int(total * 0.55),
    ]
    selected = [doc_info[i] for i in indices[:n]]
    print(f"Selected {len(selected)} samples: " +
          ", ".join(f"{s['doc_id']}({s['n_triples']}t,{s['n_sents']}s)" for s in selected))
    return selected


def parse_json_output(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("[")
        end = text.rfind("]") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                return []
    return []


def format_reward(text):
    parsed = parse_json_output(text)
    if not isinstance(parsed, list):
        return 0.0
    if not parsed:
        return 0.1
    valid = 0
    for item in parsed:
        if (isinstance(item, dict) and "head" in item
                and "relation" in item and "tail" in item
                and "evidence" in item
                and isinstance(item["evidence"], list)):
            valid += 1
    return valid / len(parsed)


def f1_reward(text, gold_triples):
    pred = parse_json_output(text)
    gold_set = set()
    for g in gold_triples:
        gold_set.add((
            g.get("head", "").lower().strip(),
            g.get("relation", "").lower().strip(),
            g.get("tail", "").lower().strip(),
        ))
    pred_set = set()
    for p in pred:
        if isinstance(p, dict):
            pred_set.add((
                str(p.get("head") or "").lower().strip(),
                str(p.get("relation") or "").lower().strip(),
                str(p.get("tail") or "").lower().strip(),
            ))
    if not gold_set:
        return 1.0 if not pred_set else 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0.0
    rec = tp / len(gold_set) if gold_set else 0.0
    return 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0


def triple_set_from_text(text):
    parsed = parse_json_output(text)
    triples = set()
    for p in parsed:
        if isinstance(p, dict):
            triples.add((
                str(p.get("head") or "").lower().strip(),
                str(p.get("relation") or "").lower().strip(),
                str(p.get("tail") or "").lower().strip(),
            ))
    return triples


def pairwise_jaccard(outputs):
    """计算所有输出对之间的 Jaccard 相似度。"""
    triple_sets = [triple_set_from_text(o) for o in outputs]
    similarities = []
    for i, j in itertools.combinations(range(len(triple_sets)), 2):
        a, b = triple_sets[i], triple_sets[j]
        if not a and not b:
            similarities.append(1.0)
        elif not a or not b:
            similarities.append(0.0)
        else:
            inter = len(a & b)
            union = len(a | b)
            similarities.append(inter / union if union > 0 else 0.0)
    return similarities


def unique_triple_sets(outputs):
    """统计不同的 triple set 数量。"""
    seen = set()
    for o in outputs:
        ts = triple_set_from_text(o)
        seen.add(frozenset(ts))
    return len(seen)


@torch.no_grad()
def generate_n(model, tokenizer, prompt, n, temperature):
    """对单个 prompt 生成 n 个输出。逐个生成避免 OOM。"""
    results = []
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096).to(model.device)
    for i in range(n):
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=True,
            temperature=temperature,
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id,
        )
        input_len = inputs["input_ids"].shape[1]
        gen_ids = output[0, input_len:]
        text = tokenizer.decode(gen_ids, skip_special_tokens=True)
        results.append(text)
        print(f"    gen {i+1}/{n}: {len(gen_ids)} tokens, format={format_reward(text):.2f}")
    return results


def compute_stats(values):
    if not values:
        return {"mean": 0, "std": 0, "min": 0, "max": 0}
    import statistics
    return {
        "mean": round(statistics.mean(values), 4),
        "std": round(statistics.stdev(values), 4) if len(values) > 1 else 0,
        "min": round(min(values), 4),
        "max": round(max(values), 4),
    }


def main():
    model, tokenizer = load_model()
    samples = select_samples(DATA_DIR, tokenizer, n=NUM_SAMPLES)

    all_results = []

    for si, sample in enumerate(samples):
        doc_id = sample["doc_id"]
        gold = sample["gold_triples"]
        print(f"\n{'='*60}")
        print(f"[{si+1}/{len(samples)}] doc={doc_id}, gold_triples={sample['n_triples']}, sents={sample['n_sents']}")

        doc_result = {"doc_id": doc_id, "n_gold": sample["n_triples"], "n_sents": sample["n_sents"]}

        for temp in TEMPERATURES:
            print(f"\n  temperature={temp}")
            t0 = time.time()
            outputs = generate_n(model, tokenizer, sample["prompt"], NUM_GENERATIONS, temp)
            elapsed = time.time() - t0

            f1_scores = [f1_reward(o, gold) for o in outputs]
            fmt_scores = [format_reward(o) for o in outputs]
            n_triples_per_output = [len(parse_json_output(o)) for o in outputs]
            jaccard_sims = pairwise_jaccard(outputs)
            n_unique = unique_triple_sets(outputs)
            n_format_ok = sum(1 for s in fmt_scores if s >= 0.9)
            n_nonempty = sum(1 for o in outputs if len(parse_json_output(o)) > 0)

            # Debug: show first format-ok output's parsed triples vs gold for F1 diagnosis
            for oi, o in enumerate(outputs):
                if format_reward(o) >= 0.9:
                    parsed = parse_json_output(o)
                    pred_tuples = [(str(p.get("head","")).lower().strip(),
                                    str(p.get("relation","")).lower().strip(),
                                    str(p.get("tail","")).lower().strip()) for p in parsed if isinstance(p, dict)]
                    gold_tuples = [(g["head"].lower().strip(), g["relation"].lower().strip(),
                                    g["tail"].lower().strip()) for g in gold]
                    print(f"  [DEBUG gen {oi}] pred_triples={pred_tuples[:3]}...")
                    print(f"  [DEBUG gen {oi}] gold_triples={gold_tuples[:3]}...")
                    print(f"  [DEBUG gen {oi}] intersection={set(pred_tuples) & set(gold_tuples)}")
                    break
            # Debug: show first 200 chars of a format-fail output
            for oi, o in enumerate(outputs):
                if format_reward(o) < 0.5:
                    print(f"  [DEBUG format-fail gen {oi}] text[:200]={repr(o[:200])}")
                    break

            temp_result = {
                "temperature": temp,
                "elapsed_sec": round(elapsed, 1),
                "f1": compute_stats(f1_scores),
                "format": compute_stats(fmt_scores),
                "n_triples": compute_stats([float(x) for x in n_triples_per_output]),
                "jaccard_sim": compute_stats(jaccard_sims),
                "n_unique_sets": n_unique,
                "n_format_ok": n_format_ok,
                "n_nonempty": n_nonempty,
                "raw_f1_scores": f1_scores,
                "raw_fmt_scores": fmt_scores,
                "raw_n_triples": n_triples_per_output,
                "raw_outputs": [o[:500] for o in outputs],
            }
            doc_result[f"temp_{temp}"] = temp_result

            print(f"  f1:  mean={temp_result['f1']['mean']:.3f} std={temp_result['f1']['std']:.3f} "
                  f"[{temp_result['f1']['min']:.3f}, {temp_result['f1']['max']:.3f}]")
            print(f"  fmt: mean={temp_result['format']['mean']:.3f}, ok={n_format_ok}/{NUM_GENERATIONS}")
            print(f"  jaccard: mean={temp_result['jaccard_sim']['mean']:.3f} std={temp_result['jaccard_sim']['std']:.3f}")
            print(f"  unique triple-sets: {n_unique}/{NUM_GENERATIONS}")
            print(f"  elapsed: {elapsed:.1f}s")

        all_results.append(doc_result)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Save raw JSON
    json_path = Path(OUTPUT_DIR) / "diversity_probe_raw.json"
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nRaw results saved to {json_path}")

    # Generate markdown report
    report = generate_report(all_results)
    md_path = Path(OUTPUT_DIR) / "diversity_probe_results.md"
    with open(md_path, "w") as f:
        f.write(report)
    print(f"Report saved to {md_path}")


def generate_report(results):
    lines = ["# SFT 模型输出多样性探测 (Diversity Probe)", ""]
    lines.append(f"- Base model: `Qwen3-4B`")
    lines.append(f"- Adapter: `sft_output` (QLoRA)")
    lines.append(f"- N generations per sample: {NUM_GENERATIONS}")
    lines.append(f"- Temperatures: {TEMPERATURES}")
    lines.append(f"- Samples: {len(results)}")
    lines.append("")

    for temp in TEMPERATURES:
        key = f"temp_{temp}"
        lines.append(f"## Temperature = {temp}")
        lines.append("")

        # Per-sample table
        lines.append("| Doc ID | #Gold | F1 mean±std | F1 range | Fmt OK | Jaccard mean±std | Unique Sets |")
        lines.append("|--------|-------|-------------|----------|--------|------------------|-------------|")
        for r in results:
            t = r[key]
            lines.append(
                f"| {r['doc_id'][:25]} | {r['n_gold']} | "
                f"{t['f1']['mean']:.3f}±{t['f1']['std']:.3f} | "
                f"[{t['f1']['min']:.3f}, {t['f1']['max']:.3f}] | "
                f"{t['n_format_ok']}/{NUM_GENERATIONS} | "
                f"{t['jaccard_sim']['mean']:.3f}±{t['jaccard_sim']['std']:.3f} | "
                f"{t['n_unique_sets']}/{NUM_GENERATIONS} |"
            )
        lines.append("")

        # Aggregate stats
        all_f1_means = [r[key]["f1"]["mean"] for r in results]
        all_f1_stds = [r[key]["f1"]["std"] for r in results]
        all_jaccard_means = [r[key]["jaccard_sim"]["mean"] for r in results]
        all_unique = [r[key]["n_unique_sets"] for r in results]
        all_fmt_ok = [r[key]["n_format_ok"] for r in results]

        import statistics
        lines.append(f"**Aggregate (n={len(results)} docs):**")
        lines.append(f"- F1 mean across docs: {statistics.mean(all_f1_means):.3f}")
        lines.append(f"- F1 std across docs (diversity signal): {statistics.mean(all_f1_stds):.3f}")
        lines.append(f"- Jaccard similarity (lower = more diverse): {statistics.mean(all_jaccard_means):.3f}")
        lines.append(f"- Avg unique triple-sets: {statistics.mean(all_unique):.1f}/{NUM_GENERATIONS}")
        lines.append(f"- Format compliance: {statistics.mean(all_fmt_ok):.1f}/{NUM_GENERATIONS}")
        lines.append("")

    # Comparison
    lines.append("## Temperature 对比")
    lines.append("")
    lines.append("| Metric | T=0.7 | T=1.0 | Delta |")
    lines.append("|--------|-------|-------|-------|")

    import statistics
    for metric_name, extractor in [
        ("F1 mean", lambda r, k: r[k]["f1"]["mean"]),
        ("F1 std (diversity)", lambda r, k: r[k]["f1"]["std"]),
        ("Jaccard sim", lambda r, k: r[k]["jaccard_sim"]["mean"]),
        ("Unique sets", lambda r, k: r[k]["n_unique_sets"]),
        ("Format OK", lambda r, k: r[k]["n_format_ok"]),
    ]:
        v07 = statistics.mean([extractor(r, "temp_0.7") for r in results])
        v10 = statistics.mean([extractor(r, "temp_1.0") for r in results])
        delta = v10 - v07
        lines.append(f"| {metric_name} | {v07:.3f} | {v10:.3f} | {delta:+.3f} |")
    lines.append("")

    # Conclusion
    lines.append("## 结论与建议")
    lines.append("")

    avg_jaccard_07 = statistics.mean([r["temp_0.7"]["jaccard_sim"]["mean"] for r in results])
    avg_jaccard_10 = statistics.mean([r["temp_1.0"]["jaccard_sim"]["mean"] for r in results])
    avg_unique_07 = statistics.mean([r["temp_0.7"]["n_unique_sets"] for r in results])
    avg_unique_10 = statistics.mean([r["temp_1.0"]["n_unique_sets"] for r in results])
    avg_fmt_07 = statistics.mean([r["temp_0.7"]["n_format_ok"] for r in results])
    avg_fmt_10 = statistics.mean([r["temp_1.0"]["n_format_ok"] for r in results])

    if avg_unique_07 >= 5:
        lines.append(f"- **T=0.7 多样性充足** (avg {avg_unique_07:.1f}/{NUM_GENERATIONS} unique sets, "
                     f"jaccard={avg_jaccard_07:.3f}), RSFT 在 T=0.7 下可行。")
    elif avg_unique_10 >= 5:
        lines.append(f"- T=0.7 多样性不足 ({avg_unique_07:.1f} unique sets)。"
                     f"**T=1.0 多样性可接受** ({avg_unique_10:.1f} unique sets), "
                     f"建议用 T=1.0 做 RSFT。")
    else:
        lines.append(f"- **两种 temperature 多样性均不足** (T=0.7: {avg_unique_07:.1f}, T=1.0: {avg_unique_10:.1f} unique sets)。")
        lines.append("- 建议替代方案：")
        lines.append("  1. 提高 temperature 至 1.2-1.5")
        lines.append("  2. 降低 top_p 至 0.8 + 更高 temperature")
        lines.append("  3. 启用 dropout (train mode) 增加随机性")
        lines.append("  4. 考虑放弃 RSFT，直接用 GRPO")

    if avg_fmt_07 < 6 or avg_fmt_10 < 6:
        lines.append(f"- **格式合规率偏低** (T=0.7: {avg_fmt_07:.1f}, T=1.0: {avg_fmt_10:.1f})，"
                     f"高 temperature 可能导致输出格式崩坏，需要权衡。")

    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
