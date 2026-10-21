"""推理+评测完整流程: 加载 Qwen3-4B + LoRA adapter → 批量推理 → 解析输出 → 计算 F1/Evi-F1/EDCR。

输入:
  - base model (Qwen3-4B) + 可选 LoRA adapter (SFT/GRPO checkpoint)
  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)

输出 (保存到 --output_dir):
  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等
  - predictions.json: 每个文档的详细预测 (doc_id, raw_output, parsed_triples, gold_triples, truncated, format_ok)

依赖: transformers, peft, bitsandbytes, torch, tqdm
"""

import argparse
import json
import logging
import time
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from tqdm import tqdm

from freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES
from freige.training import LLAMA3_CHAT_TEMPLATE
from freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)


NO_EVIDENCE_SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, and tail entity. "
    "Output as a JSON list."
)


# ---------------------------------------------------------------------------
# A. 模型加载
# ---------------------------------------------------------------------------

def load_model_and_tokenizer(model_path, adapter_path=None, sft_adapter_path=None, quantize=True):
    """加载 Qwen3-4B + 可选 LoRA adapter (4-bit QLoRA)。

    Args:
        model_path: base model 路径
        adapter_path: LoRA adapter 路径（SFT 或 GRPO checkpoint），None 则不加载
    Returns:
        (model, tokenizer)
    """
    logger.info("Loading tokenizer: %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True,
        padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, "chat_template", None):
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE

    logger.info("Loading model: %s", model_path)
    model_kwargs = dict(
        trust_remote_code=True,
        attn_implementation="sdpa",
        device_map="auto",
    )
    if quantize:
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16

    model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)

    if sft_adapter_path:
        logger.info("Loading & merging SFT adapter: %s", sft_adapter_path)
        model = PeftModel.from_pretrained(model, sft_adapter_path)
        model = model.merge_and_unload()

    if adapter_path:
        logger.info("Loading LoRA adapter: %s", adapter_path)
        model = PeftModel.from_pretrained(model, adapter_path)

    model.eval()
    return model, tokenizer


# ---------------------------------------------------------------------------
# B. Prompt 构造
# ---------------------------------------------------------------------------


def _apply_chat_template(tokenizer, messages, **kwargs):
    """Wrap apply_chat_template to skip enable_thinking for tokenizers whose template doesn't use it."""
    tmpl = getattr(tokenizer, "chat_template", None) or ""
    if "enable_thinking" not in tmpl:
        kwargs.pop("enable_thinking", None)
    return tokenizer.apply_chat_template(messages, **kwargs)


def build_prompt(tokenizer, instruction, input_text, system_prompt=SYSTEM_PROMPT):
    """构建与训练一致的 chat prompt（Qwen3 传 enable_thinking=False，其他模型跳过）。"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{instruction}\n\n{input_text}"},
    ]
    return _apply_chat_template(
        tokenizer, messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )


def prepare_eval_data(data_dir, split, tokenizer, include_evidence=True, system_prompt=SYSTEM_PROMPT):
    """加载 DocRED 数据，构建 eval prompts、gold 标注和 per-doc gold map。"""
    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process(split)
    groups = processor.group_by_document(samples)

    eval_items = []
    for doc_id, doc_samples in groups.items():
        sft_sample = processor.format_sft_sample(doc_samples, include_evidence=include_evidence)
        prompt = build_prompt(
            tokenizer, sft_sample["instruction"], sft_sample["input"], system_prompt=system_prompt
        )
        eval_items.append({"doc_id": doc_id, "prompt": prompt})

    split_file = Path(data_dir) / SPLIT_FILENAMES[split]
    with open(split_file) as f:
        raw_docred = json.load(f)
    gold = gold_from_docred(raw_docred)

    gold_by_doc = {}
    for g in gold:
        gold_by_doc.setdefault(g["doc_id"], []).append(g)

    logger.info("Prepared %d eval documents, %d gold triples", len(eval_items), len(gold))
    return eval_items, gold, gold_by_doc




def prepare_test_data(data_dir, tokenizer, include_evidence=True, system_prompt=SYSTEM_PROMPT):
    """Test split 无 labels，直接从 vertexSet 构建 entity list + prompt。

    Args:
        data_dir: DocRED 数据目录
        tokenizer: 用于构建 chat prompt
        include_evidence: 是否在 instruction 中要求 evidence
        system_prompt: system prompt 文本

    Returns:
        (eval_items, raw_docs): eval_items 是 [{doc_id, prompt}]，raw_docs 是原始 JSON docs
    """
    test_file = Path(data_dir) / SPLIT_FILENAMES["test"]
    with open(test_file) as f:
        raw_docs = json.load(f)

    eval_items = []
    for doc in raw_docs:
        doc_id = doc.get("title", "")
        sents = [" ".join(s) for s in doc["sents"]]
        vertex_set = doc["vertexSet"]

        numbered_sents = "\n".join(f"[{i}] {s}" for i, s in enumerate(sents))

        entity_list = set()
        for entity in vertex_set:
            name = entity[0]["name"]
            etype = entity[0].get("type", "UNK")
            entity_list.add(f"{name} ({etype})")
        entity_str = ", ".join(sorted(entity_list))

        if include_evidence:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, tail entity, "
                "and the sentence IDs that serve as evidence. "
                "Output as a JSON list."
            )
        else:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, and tail entity. "
                "Output as a JSON list."
            )

        input_text = f"Document:\n{numbered_sents}\n\nEntities: {entity_str}"
        prompt = build_prompt(tokenizer, instruction, input_text, system_prompt=system_prompt)
        eval_items.append({"doc_id": doc_id, "prompt": prompt})

    logger.info("Prepared %d test documents for inference", len(eval_items))
    return eval_items, raw_docs


def convert_to_codalab(raw_results, raw_docs):
    """将模型预测转换为 CodaLab 提交格式 [{title, h_idx, t_idx, r, evidence}, ...]。

    Args:
        raw_results: run_inference 输出
        raw_docs: test.json 原始文档列表

    Returns:
        list[dict]: CodaLab 提交条目
    """
    from freige.data.docred_processor import DOCRED_REL_INFO
    rel_name_to_code = {v.lower().strip(): k for k, v in DOCRED_REL_INFO.items()}

    doc_entity_map = {}
    for doc in raw_docs:
        doc_id = doc.get("title", "")
        name_to_idx = {}
        for idx, entity in enumerate(doc["vertexSet"]):
            # lowercase + strip 容错：模型输出的 entity name 可能有大小写/空格差异
            name = entity[0]["name"].lower().strip()
            if name not in name_to_idx:
                name_to_idx[name] = idx
        doc_entity_map[doc_id] = name_to_idx

    submissions = []
    for r in raw_results:
        doc_id = r["doc_id"]
        name_to_idx = doc_entity_map.get(doc_id, {})
        for triple in r["parsed_triples"]:
            h_name = triple["head"].lower().strip()
            t_name = triple["tail"].lower().strip()
            rel_name = triple["relation"].lower().strip()

            h_idx = name_to_idx.get(h_name)
            t_idx = name_to_idx.get(t_name)
            r_code = rel_name_to_code.get(rel_name)

            if h_idx is None or t_idx is None or r_code is None:
                continue

            entry = {
                "title": doc_id,
                "h_idx": h_idx,
                "t_idx": t_idx,
                "r": r_code,
                "evidence": triple.get("evidence", []),
            }
            submissions.append(entry)

    logger.info("CodaLab conversion: %d entries from %d documents", len(submissions), len(raw_results))
    return submissions


# ---------------------------------------------------------------------------
# C. 批量推理
# ---------------------------------------------------------------------------

def _get_input_device(model):
    """获取模型输入应放置的设备。"""
    for obj in [model, getattr(model, "base_model", None)]:
        if obj is not None and hasattr(obj, "hf_device_map"):
            first = next(iter(obj.hf_device_map.values()))
            return f"cuda:{first}" if isinstance(first, int) else first
    return model.device


@torch.no_grad()
def run_inference(model, tokenizer, eval_items, batch_size=8, max_new_tokens=1024):
    """对每个文档生成预测。

    Returns:
        List[dict]: {doc_id, raw_output, parsed_triples, truncated, format_ok}
    """
    results = []
    n_truncated = 0
    n_errors = 0
    device = _get_input_device(model)

    for i in tqdm(range(0, len(eval_items), batch_size), desc="Inference"):
        batch = eval_items[i : i + batch_size]
        prompts = [item["prompt"] for item in batch]

        try:
            inputs = tokenizer(
                prompts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=4096,
            ).to(device)

            prompt_len = inputs["input_ids"].shape[1]

            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
            )
        except Exception as e:
            logger.error("Batch %d failed: %s", i, e)
            for item in batch:
                results.append({
                    "doc_id": item["doc_id"],
                    "raw_output": "",
                    "parsed_triples": [],
                    "truncated": False,
                    "format_ok": False,
                })
                n_errors += 1
            continue

        for j, item in enumerate(batch):
            generated_ids = outputs[j][prompt_len:]

            if tokenizer.pad_token_id is not None:
                mask = generated_ids != tokenizer.pad_token_id
                if mask.any():
                    last_real = mask.nonzero()[-1].item() + 1
                    generated_ids = generated_ids[:last_real]
                else:
                    generated_ids = generated_ids[:0]

            generated_text = tokenizer.decode(generated_ids, skip_special_tokens=True)
            truncated = len(generated_ids) >= max_new_tokens
            if truncated:
                n_truncated += 1

            parsed, format_ok = parse_model_output(generated_text)
            results.append({
                "doc_id": item["doc_id"],
                "raw_output": generated_text,
                "parsed_triples": parsed,
                "truncated": truncated,
                "format_ok": format_ok,
            })

    logger.info(
        "Inference done. %d/%d truncated, %d errors.",
        n_truncated, len(eval_items), n_errors,
    )
    return results


# ---------------------------------------------------------------------------
# E. 评测
# ---------------------------------------------------------------------------

def evaluate(predictions_flat, gold, raw_outputs, data_dir, split="dev"):
    """调用 DocREDEvaluator 计算指标。"""
    train_path = Path(data_dir) / "train_annotated.json"
    if train_path.exists():
        evaluator = DocREDEvaluator.from_train_file(str(train_path))
    else:
        logger.warning("train_annotated.json not found, Ign-F1 = F1")
        evaluator = DocREDEvaluator()

    return evaluator.evaluate(predictions_flat, gold, raw_outputs)


# ---------------------------------------------------------------------------
# F. 完整报告
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="FREIGE 推理+评测: model → predict → evaluate"
    )
    parser.add_argument("--model_path", required=True,
                        help="Base model 路径，或 LoRA adapter 路径（需配合 --base_model）")
    parser.add_argument("--base_model", default="./outputs",
                        help="Base model（当 model_path 是 adapter 时需要）")
    parser.add_argument("--sft_adapter", default=None,
                        help="SFT adapter 路径（评估 GRPO checkpoint 时需要，先 merge 再加载 GRPO adapter）")
    parser.add_argument("--data_path", required=True,
                        help="DocRED 数据目录（含 dev.json, train_annotated.json）")
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--split", default="dev", choices=["dev", "test"])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--no_evidence", action="store_true", default=False,
                        help="Use no-evidence prompt (for SFT-without-evidence ablation)")
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction,
                        default=True, help="4-bit NF4 quantization（default: on）")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 自动检测 model_path 是 adapter 还是完整模型
    adapter_config = Path(args.model_path) / "adapter_config.json"
    if adapter_config.exists():
        base_model_path = args.base_model
        adapter_path = args.model_path
        logger.info("Detected adapter at %s, base: %s", adapter_path, base_model_path)
    else:
        base_model_path = args.model_path
        adapter_path = None
        logger.info("Full model: %s (no adapter)", base_model_path)


    if adapter_config.exists() and args.sft_adapter is None:
        if args.base_model == parser.get_default("base_model"):
            raise ValueError(
                f"model_path '{args.model_path}' is a LoRA adapter (adapter_config.json found), "
                f"but --sft_adapter is not set. RSFT/DPO/GRPO adapters are trained on SFT-merged "
                f"model and MUST be evaluated with --sft_adapter pointing to the SFT adapter directory. "
                f"Add: --sft_adapter /path/to/sft_output"
            )
        else:
            logger.warning("--sft_adapter not set but --base_model is non-default (%s); assuming base is already merged.", args.base_model)

    model, tokenizer = load_model_and_tokenizer(
        base_model_path, adapter_path, sft_adapter_path=args.sft_adapter,
        quantize=args.quantize,
    )
    _sys_prompt = NO_EVIDENCE_SYSTEM_PROMPT if args.no_evidence else SYSTEM_PROMPT
    _include_evi = not args.no_evidence
    if args.split == "test":
        eval_items, raw_docs = prepare_test_data(
            args.data_path, tokenizer,
            include_evidence=_include_evi, system_prompt=_sys_prompt,
        )
        gold, gold_by_doc = [], {}
    else:
        eval_items, gold, gold_by_doc = prepare_eval_data(
            args.data_path, args.split, tokenizer,
            include_evidence=_include_evi, system_prompt=_sys_prompt,
        )

    t0 = time.time()
    raw_results = run_inference(
        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens
    )
    elapsed = time.time() - t0
    logger.info("Inference: %.1fs (%.2f s/doc)", elapsed, elapsed / max(len(eval_items), 1))

    # 展平为 evaluator 格式
    all_predictions = []
    raw_outputs_for_eval = []
    for r in raw_results:
        doc_id = r["doc_id"]
        for triple in r["parsed_triples"]:
            all_predictions.append({
                "doc_id": doc_id,
                "head": triple["head"],
                "tail": triple["tail"],
                "relation": triple["relation"],
                "evidence": triple.get("evidence", []),
            })
        raw_outputs_for_eval.append({"doc_id": doc_id, "raw_text": r["raw_output"]})

    if args.split == "test":
        metrics = {"note": "test split - submit to CodaLab for evaluation"}
        codalab_preds = convert_to_codalab(raw_results, raw_docs)
        codalab_path = output_dir / "codalab_submission.json"
        with open(codalab_path, "w") as f:
            json.dump(codalab_preds, f, ensure_ascii=False)
        logger.info("CodaLab submission \u2192 %s (%d predictions)", codalab_path, len(codalab_preds))
    else:
        metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)

    n_truncated = sum(1 for r in raw_results if r["truncated"])
    n_format_ok = sum(1 for r in raw_results if r["format_ok"])
    n_total = len(raw_results)
    metrics["n_documents"] = n_total
    metrics["n_predictions"] = len(all_predictions)
    metrics["n_truncated"] = n_truncated
    metrics["n_format_ok"] = n_format_ok
    metrics["format_ok_rate"] = n_format_ok / n_total if n_total else 0.0
    metrics["inference_time_seconds"] = round(elapsed, 1)
    metrics["config"] = vars(args)

    # 保存 metrics.json
    metrics_path = output_dir / "metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
    logger.info("Metrics → %s", metrics_path)

    # 保存 predictions.json（每文档详细信息）
    detailed = []
    for r in raw_results:
        doc_id = r["doc_id"]
        doc_gold = gold_by_doc.get(doc_id, [])
        gold_triples = [
            {"head": g["head"], "tail": g["tail"], "relation": g["relation"],
             "evidence": g.get("evidence", [])}
            for g in doc_gold
        ]
        detailed.append({
            "doc_id": doc_id,
            "raw_output": r["raw_output"],
            "parsed_triples": r["parsed_triples"],
            "gold_triples": gold_triples,
            "truncated": r["truncated"],
            "format_ok": r["format_ok"],
        })

    pred_path = output_dir / "predictions.json"
    with open(pred_path, "w") as f:
        json.dump(detailed, f, indent=2, ensure_ascii=False)
    logger.info("Predictions → %s", pred_path)

    # 控制台汇总
    if args.split == "test":
        print("\n" + "=" * 50)
        print(f"  Test Documents: {n_total}")
        print(f"  Predictions:    {len(all_predictions)}")
        print(f"  CodaLab file:   {len(codalab_preds)} entries")
        print(f"  Format OK:      {n_format_ok}/{n_total} ({metrics.get('format_ok_rate', 0):.1%})")
        print(f"  Truncated:      {n_truncated}/{n_total}")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print(f"  F1:          {metrics['f1']:.4f}")
        print(f"  Ign-F1:      {metrics['ign_f1']:.4f}")
        print(f"  Evi-F1(DREEAM): {metrics.get('evi_f1_joint', 0):.4f}")
        print(f"  Evi-F1(TP):     {metrics['evi_f1']:.4f}")
        print(f"  EDCR:        {metrics.get('edcr', 0):.4f}")
        print(f"  Format OK:   {n_format_ok}/{n_total} ({metrics['format_ok_rate']:.1%})")
        print(f"  Truncated:   {n_truncated}/{n_total}")
        print(f"  Predictions: {len(all_predictions)}")
        print("=" * 50)


if __name__ == "__main__":
    main()
