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
      --base_model /root/autodl-tmp/models/Qwen3-4B \
      --sft_adapter /root/autodl-tmp/sft_output \
      --data_path /root/autodl-tmp/data/docred \
      --output_dir /root/autodl-tmp/rsft_generations \
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

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)


def load_model_and_tokenizer(base_model, sft_adapter=None, quantize=True):
    """加载 base model + 可选 QLoRA adapter，merge 后返回。"""
    logger.info("Loading tokenizer: %s", base_model)
    tokenizer = AutoTokenizer.from_pretrained(
        base_model, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, 'chat_template', None):
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
        prompt = tokenizer.apply_chat_template(
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
        top_p=0.9,
        pad_token_id=tokenizer.pad_token_id,
    )

    outputs = model.generate(**inputs, **generate_kwargs)

    # 截取新生成的 token
    input_len = inputs["input_ids"].shape[1]
    generated_ids = outputs[:, input_len:]
    texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    # 按 prompt 分组
    results = []
    for i in range(len(prompts)):
        start = i * num_generations
        end = start + num_generations
        results.append(texts[start:end])

    return results


def main():
    parser = argparse.ArgumentParser(description="RSFT Step 1: Batch Generation")
    parser.add_argument("--base_model", type=str, default="/root/autodl-tmp/models/Qwen3-4B",
                        help="Base model 路径")
    parser.add_argument("--sft_adapter", type=str, default="/root/autodl-tmp/sft_output",
                        help="SFT QLoRA adapter 路径")
    parser.add_argument("--data_path", type=str, default=None,
                        help="DocRED 数据目录")
    parser.add_argument("--split", type=str, default="train",
                        help="数据集 split (default: train)")
    parser.add_argument("--output_dir", type=str, default="/root/autodl-tmp/rsft_generations",
                        help="生成结果输出目录")
    parser.add_argument("--num_generations", type=int, default=8,
                        help="每个样本生成的候选数 (default: 8)")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="采样温度 (default: 0.7)")
    parser.add_argument("--batch_size", type=int, default=2,
                        help="每批处理的文档数 (default: 2)")
    parser.add_argument("--max_new_tokens", type=int, default=1024,
                        help="最大生成 token 数 (default: 1024)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction,
                        default=False, help="4-bit 量化 (default: off, bf16 sufficient for 4B model)")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "generations.jsonl"

    model, tokenizer = load_model_and_tokenizer(
        args.base_model, args.sft_adapter, quantize=args.quantize,
    )

    items = prepare_generation_data(args.data_path, args.split, tokenizer)

    completed = load_progress(args.output_dir)
    pending = [item for item in items if item["doc_id"] not in completed]
    logger.info("Total: %d, completed: %d, pending: %d", len(items), len(completed), len(pending))

    if not pending:
        logger.info("All documents already generated. Done.")
        return

    # 追加写模式
    with open(output_file, "a") as fout:
        for batch_start in tqdm(range(0, len(pending), args.batch_size), desc="Generating"):
            batch = pending[batch_start:batch_start + args.batch_size]
            prompts = [item["prompt"] for item in batch]

            try:
                batch_outputs = generate_batch(
                    model, tokenizer, prompts,
                    args.num_generations, args.temperature, args.max_new_tokens,
                )
            except torch.cuda.OutOfMemoryError:
                logger.warning("OOM on batch of %d, falling back to one-by-one", len(batch))
                torch.cuda.empty_cache()
                batch_outputs = []
                for p in prompts:
                    out = generate_batch(
                        model, tokenizer, [p],
                        args.num_generations, args.temperature, args.max_new_tokens,
                    )
                    batch_outputs.append(out[0])

            for item, generations in zip(batch, batch_outputs):
                for gen_idx, raw_text in enumerate(generations):
                    parsed_triples, format_ok = parse_model_output(raw_text)
                    record = {
                        "doc_id": item["doc_id"],
                        "generation_idx": gen_idx,
                        "prompt": item["prompt"],
                        "output": raw_text,
                        "raw_text": raw_text,
                        "parsed_triples": parsed_triples,
                        "format_ok": format_ok,
                        "gold_triples": item["gold_triples"],
                        "sents": item["sents"],
                    }
                    fout.write(json.dumps(record, ensure_ascii=False) + "\n")

                completed.add(item["doc_id"])

            fout.flush()
            save_progress(args.output_dir, completed)

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


if __name__ == "__main__":
    main()
