"""RSFT Step 1: 批量生成候选输出。

用 SFT warmup 模型对每个训练样本生成 N 个候选输出 (temperature sampling)，
保存为 JSONL 供后续 CED 打分筛选。

输入:
  - base model (Qwen3-4B) + QLoRA adapter (SFT checkpoint)
  - DocRED train_annotated.json

输出 (保存到 --output_dir):
  - generations.jsonl: 每行一个生成结果
    {"doc_id", "generation_idx", "prompt", "output", "raw_text", "parsed_triples", "format_ok"}
  - progress.json: 已完成的 doc_id 列表（用于断点续传）

依赖: transformers, peft, bitsandbytes, torch, tqdm

用法:
  python -m freige.training.rsft_generate \
      --base_model ./outputs \
      --sft_adapter ./outputs \
      --data_path ./data/docred \
      --output_dir ./outputs \
      --num_generations 8 --temperature 0.7 --batch_size 4
"""

import argparse
import json
import logging
import os
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from tqdm import tqdm

from freige.data.docred_processor import DocREDProcessor
from freige.eval.evaluator import parse_model_output
from freige.training import LLAMA3_CHAT_TEMPLATE
from freige.training.diversity_metrics import build_triple_set, compute_doc_diversity, compute_diversity_from_file


def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, 'chat_template', None) or ''
    if 'enable_thinking' not in tmpl:
        kwargs.pop('enable_thinking', None)
    return tokenizer.apply_chat_template(messages, **kwargs)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)


def load_model_and_tokenizer(base_model, sft_adapter=None, quantize=False):
    """加载 base model + 可选 QLoRA adapter，merge 后返回。"""
    logger.info("Loading tokenizer: %s", base_model)
    tokenizer = AutoTokenizer.from_pretrained(
        base_model, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, "chat_template", None):
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE

    logger.info("Loading model: %s", base_model)
    model_kwargs = dict(trust_remote_code=True, attn_implementation="sdpa", device_map="auto")
    if quantize:
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16

    model = AutoModelForCausalLM.from_pretrained(base_model, **model_kwargs)

    if sft_adapter:
        logger.info("Loading & merging SFT adapter: %s", sft_adapter)
        model = PeftModel.from_pretrained(model, sft_adapter)
        model = model.merge_and_unload()

    model.eval()
    return model, tokenizer


def prepare_generation_data(data_dir, split, tokenizer):
    """加载 DocRED 数据，构建每个文档的 prompt 和 gold 信息。

    Returns:
        list of dict: 每个文档一条，含 doc_id, prompt, gold_triples, sents
    """
    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process(split)
    groups = processor.group_by_document(samples)

    items = []
    for doc_id, doc_samples in groups.items():
        sft_sample = processor.format_sft_sample(doc_samples)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
        ]
        prompt = _apply_chat_template(tokenizer, 
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )

        gold_triples = []
        for s in doc_samples:
            gold_triples.append({
                "head": s.head.name,
                "relation": s.relation_name,
                "tail": s.tail.name,
                "evidence": s.evidence_sent_ids,
                "hard_negative_sent_ids": s.hard_negative_sent_ids,
            })

        ref = doc_samples[0]
        items.append({
            "doc_id": doc_id,
            "prompt": prompt,
            "gold_triples": gold_triples,
            "sents": ref.sents,
            "sft_output": sft_sample["output"],
        })

    logger.info("Prepared %d documents for generation", len(items))
    return items


def load_progress(output_dir):
    """加载已完成的 doc_id 集合（断点续传）。"""
    progress_path = Path(output_dir) / "progress.json"
    if progress_path.exists():
        with open(progress_path) as f:
            data = json.load(f)
        completed = set(data.get("completed_doc_ids", []))
        logger.info("Resuming: %d documents already completed", len(completed))
        return completed
    return set()


def save_progress(output_dir, completed_doc_ids):
    """保存已完成 doc_id 列表。"""
    progress_path = Path(output_dir) / "progress.json"
    with open(progress_path, "w") as f:
        json.dump({"completed_doc_ids": sorted(completed_doc_ids)}, f)


def load_progress_from_jsonl(output_file, num_generations):
    """从 generations.jsonl 重建已完成的 doc_id 集合（比 progress.json 更可靠）。

    扫描 jsonl 文件，统计每个 doc_id 的条目数。
    完整的 doc（条目数 >= num_generations）标记为已完成。
    不完整的 doc 条目会被从文件中移除，以便重新生成。
    """
    if not Path(output_file).exists():
        return set()
    doc_counts = {}
    with open(output_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                doc_id = rec["doc_id"]
                doc_counts[doc_id] = doc_counts.get(doc_id, 0) + 1
            except (json.JSONDecodeError, KeyError):
                continue
    completed = {did for did, cnt in doc_counts.items() if cnt >= num_generations}
    partial = {did: cnt for did, cnt in doc_counts.items() if cnt < num_generations}
    if partial:
        partial_ids = set(partial.keys())
        logger.warning("Found %d partial docs, truncating from JSONL: %s",
                       len(partial), dict(list(partial.items())[:5]))
        tmp_file = str(output_file) + ".tmp"
        with open(output_file) as fin, open(tmp_file, "w") as fout:
            for line_in in fin:
                try:
                    rec = json.loads(line_in.strip())
                    if rec["doc_id"] not in partial_ids:
                        fout.write(line_in)
                except (json.JSONDecodeError, KeyError):
                    continue
        os.replace(tmp_file, str(output_file))
    total_lines = sum(cnt for did, cnt in doc_counts.items() if did in completed)
    logger.info("Resumed from JSONL: %d complete docs (%d lines)", len(completed), total_lines)
    return completed


@torch.no_grad()
def generate_batch(model, tokenizer, prompts, num_generations, temperature, max_new_tokens):
    """对一批 prompt 各生成 num_generations 个输出。

    Returns:
        list[list[str]]: outer = prompts, inner = num_generations 个输出文本
    """
    # 将每个 prompt 重复 num_generations 次，一次性生成
    expanded_prompts = []
    for p in prompts:
        expanded_prompts.extend([p] * num_generations)

    inputs = tokenizer(
        expanded_prompts, return_tensors="pt", padding=True, truncation=True,
        max_length=4096,
    ).to(model.device)

    generate_kwargs = dict(
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
    )

    outputs = model.generate(**inputs, **generate_kwargs)

    # 截取新生成的 token
    input_len = inputs["input_ids"].shape[1]
    generated_ids = outputs[:, input_len:]
    texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    # 检测截断: 生成长度达到 max_new_tokens 上限
    non_pad_lens = (generated_ids != tokenizer.pad_token_id).sum(dim=1).tolist()
    truncated_flags = [length >= max_new_tokens for length in non_pad_lens]

    # 按 prompt 分组
    results = []
    trunc_results = []
    for i in range(len(prompts)):
        start = i * num_generations
        end = start + num_generations
        results.append(texts[start:end])
        trunc_results.append(truncated_flags[start:end])

    return results, trunc_results


def main():
    parser = argparse.ArgumentParser(description="RSFT Step 1: Batch Generation")
    parser.add_argument("--base_model", type=str, default="./outputs",
                        help="Base model 路径")
    parser.add_argument("--sft_adapter", type=str, default="./outputs",
                        help="SFT QLoRA adapter 路径")
    parser.add_argument("--data_path", type=str, default=None,
                        help="DocRED 数据目录")
    parser.add_argument("--split", type=str, default="train",
                        help="数据集 split (default: train)")
    parser.add_argument("--output_dir", type=str, default="./outputs",
                        help="生成结果输出目录")
    parser.add_argument("--num_generations", type=int, default=8,
                        help="每个样本生成的候选数 (default: 8)")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="采样温度 (default: 0.7)")
    parser.add_argument("--top_p", type=float, default=0.95,
                        help="Top-p 采样 (default: 0.95)")
    parser.add_argument("--batch_size", type=int, default=1,
                        help="每批处理的文档数 (default: 2)")
    parser.add_argument("--max_new_tokens", type=int, default=1024,
                        help="最大生成 token 数 (default: 1024)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--quantize", action="store_true",
                        help="4-bit 量化 (default: off)")
    parser.add_argument("--start_idx", type=int, default=0,
                        help="Start document index (inclusive)")
    parser.add_argument("--end_idx", type=int, default=-1,
                        help="End document index (exclusive), -1 means all")
    parser.add_argument("--shard_id", type=int, default=0,
                        help="Shard index for parallel generation")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from existing generations.jsonl instead of progress.json")
    parser.add_argument("--num_shards", type=int, default=1,
                        help="Total number of shards for parallel generation")
    parser.add_argument("--repetition_penalty", type=float, default=1.0,
                        help="Repetition penalty (default: 1.0, no penalty)")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    if args.num_shards > 1:
        output_dir = Path(args.output_dir) / f"shard_{args.shard_id}"
    else:
        output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "generations.jsonl"

    model, tokenizer = load_model_and_tokenizer(
        args.base_model, args.sft_adapter, quantize=args.quantize,
    )

    # D034 fix: Qwen3-4B generation_config.json overrides kwargs, must set explicitly
    model.generation_config.temperature = args.temperature
    model.generation_config.top_k = 0
    model.generation_config.top_p = args.top_p
    model.generation_config.do_sample = True
    if args.repetition_penalty != 1.0:
        model.generation_config.repetition_penalty = args.repetition_penalty

    items = prepare_generation_data(args.data_path, args.split, tokenizer)

    if args.num_shards > 1:
        total = len(items)
        per_shard = total // args.num_shards
        start = args.shard_id * per_shard
        end = start + per_shard if args.shard_id < args.num_shards - 1 else total
        items = items[start:end]
        logger.info("Shard %d/%d: docs [%d:%d] -> %d documents",
                    args.shard_id, args.num_shards, start, end, len(items))
    elif args.end_idx > 0:
        items = items[args.start_idx:args.end_idx]
        logger.info("Slice: [%d:%d] -> %d documents", args.start_idx, args.end_idx, len(items))
    elif args.start_idx > 0:
        items = items[args.start_idx:]
        logger.info("Slice: [%d:end] -> %d documents", args.start_idx, len(items))
    else:
        logger.info("Full dataset: %d documents", len(items))

    if args.resume:
        completed = load_progress_from_jsonl(output_file, args.num_generations)
    else:
        completed = load_progress(output_dir)
    pending = [item for item in items if item["doc_id"] not in completed]
    logger.info("Total: %d, completed: %d, pending: %d", len(items), len(completed), len(pending))

    if not pending:
        logger.info("All documents already generated. Done.")
        return

    # RSFT 监控计数器
    mon_format_ok = 0
    mon_truncated = 0
    mon_total_gens = 0
    mon_diversity_sum = 0.0
    mon_doc_count = 0
    mon_window_format_ok = 0
    mon_window_truncated = 0
    mon_window_total = 0
    mon_window_diversity = 0.0
    mon_window_docs = 0

    def _print_monitor(prefix, n_docs, n_gens, n_fmt_ok, n_trunc, div_sum):
        fmt_rate = n_fmt_ok / n_gens * 100 if n_gens else 0
        trunc_rate = n_trunc / n_gens * 100 if n_gens else 0
        mean_div = div_sum / n_docs if n_docs else 0
        print(f"\n[RSFT Monitor] {prefix} ({n_docs} docs, {n_gens} generations):")
        print(f"  format_ok_rate: {fmt_rate:.1f}%")
        print(f"  truncation_rate: {trunc_rate:.1f}%")
        n_gen = args.num_generations
        print(f"  mean_diversity: {mean_div * n_gen:.1f}/{n_gen}")
        if fmt_rate < 85:
            print(f"  \u26a0\ufe0f WARNING: format_ok_rate below 85%, consider fixing parser")
        if trunc_rate > 10:
            print(f"  \u26a0\ufe0f WARNING: truncation_rate above 10%, consider max_new_tokens=3072")
        print(flush=True)

    # 追加写模式
    with open(output_file, "a") as fout:
        for batch_start in tqdm(range(0, len(pending), args.batch_size), desc="Generating"):
            batch = pending[batch_start:batch_start + args.batch_size]
            prompts = [item["prompt"] for item in batch]

            try:
                batch_outputs, batch_trunc = generate_batch(
                    model, tokenizer, prompts,
                    args.num_generations, args.temperature, args.max_new_tokens,
                )
            except torch.cuda.OutOfMemoryError:
                logger.warning("OOM on batch of %d, falling back to one-by-one", len(batch))
                torch.cuda.empty_cache()
                batch_outputs = []
                batch_trunc = []
                for p in prompts:
                    out, trunc = generate_batch(
                        model, tokenizer, [p],
                        args.num_generations, args.temperature, args.max_new_tokens,
                    )
                    batch_outputs.append(out[0])
                    batch_trunc.append(trunc[0])

            for item, generations, trunc_flags in zip(batch, batch_outputs, batch_trunc):
                doc_triple_sets = set()
                for gen_idx, raw_text in enumerate(generations):
                    parsed_triples, format_ok = parse_model_output(raw_text)
                    truncated = trunc_flags[gen_idx] if gen_idx < len(trunc_flags) else False
                    record = {
                        "doc_id": item["doc_id"],
                        "generation_idx": gen_idx,
                        "prompt": item["prompt"],
                        "output": raw_text,
                        "raw_text": raw_text,
                        "parsed_triples": parsed_triples,
                        "format_ok": format_ok,
                        "truncated": truncated,
                        "gold_triples": item["gold_triples"],
                        "sents": item["sents"],
                    }
                    fout.write(json.dumps(record, ensure_ascii=False) + "\n")

                    # 监控计数
                    mon_total_gens += 1
                    mon_window_total += 1
                    if format_ok:
                        mon_format_ok += 1
                        mon_window_format_ok += 1
                    if truncated:
                        mon_truncated += 1
                        mon_window_truncated += 1
                    triple_key = build_triple_set(parsed_triples)
                    doc_triple_sets.add(triple_key)

                diversity = len(doc_triple_sets) / len(generations)
                mon_diversity_sum += diversity
                mon_doc_count += 1
                mon_window_diversity += diversity
                mon_window_docs += 1

                # 每 100 个文档打印一次监控
                if mon_doc_count == 100:
                    _print_monitor("First 100 samples", mon_doc_count, mon_total_gens,
                                   mon_format_ok, mon_truncated, mon_diversity_sum)
                elif mon_doc_count > 100 and mon_window_docs >= 100:
                    _print_monitor(f"Docs {mon_doc_count - mon_window_docs + 1}-{mon_doc_count}",
                                   mon_window_docs, mon_window_total,
                                   mon_window_format_ok, mon_window_truncated, mon_window_diversity)
                    mon_window_format_ok = 0
                    mon_window_truncated = 0
                    mon_window_total = 0
                    mon_window_diversity = 0.0
                    mon_window_docs = 0

                completed.add(item["doc_id"])

            fout.flush()
            save_progress(output_dir, completed)

    logger.info("Generation complete. %d documents, %d total outputs → %s",
                len(items), len(items) * args.num_generations, output_file)

    # 统计
    n_format_ok = 0
    n_total = 0
    with open(output_file) as f:
        for line in f:
            rec = json.loads(line)
            n_total += 1
            if rec.get("format_ok"):
                n_format_ok += 1

    logger.info("Format compliance: %d/%d (%.1f%%)", n_format_ok, n_total,
                100 * n_format_ok / n_total if n_total else 0)

    # Cross-check: recompute diversity from saved file
    try:
        div_stats = compute_diversity_from_file(str(output_file))
        logger.info(
            "Diversity cross-check (from file): mean=%.2f/%d, median=%.1f/%d, n_docs=%d",
            div_stats["mean_diversity"], div_stats["n_generations"],
            div_stats["median_diversity"], div_stats["n_generations"],
            div_stats["n_docs"],
        )
    except Exception as e:
        logger.warning("Diversity cross-check failed: %s", e)


if __name__ == "__main__":
    main()
