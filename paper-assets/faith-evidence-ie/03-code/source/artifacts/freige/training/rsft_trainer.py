"""RSFT (Rejection Sampling Fine-Tuning) 训练脚本。

从 SFT warmup checkpoint 继续训练，使用经 CED 打分筛选的高质量生成数据。
流程: base model → merge SFT adapter → 新 QLoRA → 在 RSFT 数据上训练。

输入: JSONL，每行 {"doc_id": ..., "input": ..., "output": ..., "ced_score": ..., ...}
输出: QLoRA adapter checkpoint
依赖: transformers, trl, peft, bitsandbytes, datasets

单卡:   python -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
            -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
"""

import argparse
import json
import logging
import os

import torch
from datasets import Dataset
from peft import LoraConfig, PeftModel, TaskType, get_peft_model
from torch.utils.data import WeightedRandomSampler
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainerCallback,
)
from trl import SFTConfig, SFTTrainer

from freige.training import LLAMA3_CHAT_TEMPLATE
from freige.training.sft_trainer import SYSTEM_PROMPT

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_BASE_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
DEFAULT_SFT_ADAPTER = "/root/autodl-tmp/sft_output"


def load_rsft_data(data_path: str, tokenizer, max_length: int = 2048):
    """加载 CED 筛选后的 RSFT 数据，格式化为 chat template 文本。

    每行 JSONL 的 input 字段作为 user message，output 字段作为 assistant response，
    经 apply_chat_template 拼接后用于 SFT 训练。超过 max_length 的样本被跳过
    而非截断，避免训练在不完整 JSON 输出上。

    Returns:
        (Dataset, list[float]): 训练数据集和对应的 CED scores
    """
    samples = []
    with open(data_path) as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))

    logger.info("Loaded %d RSFT samples from %s", len(samples), data_path)

    formatted = []
    ced_scores = []
    skipped = 0
    for s in samples:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": s["input"]},
            {"role": "assistant", "content": s["output"]},
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
            enable_thinking=False,
        )
        token_len = len(tokenizer.encode(text, add_special_tokens=False))
        if token_len > max_length:
            skipped += 1
            continue
        formatted.append({"text": text})
        ced_scores.append(s.get("ced_score", 1.0))

    if skipped:
        logger.warning("Skipped %d samples exceeding max_length=%d", skipped, max_length)

    if ced_scores:
        logger.info(
            "Prepared %d RSFT samples (CED scores: min=%.3f, max=%.3f, mean=%.3f)",
            len(formatted), min(ced_scores), max(ced_scores),
            sum(ced_scores) / len(ced_scores),
        )
    return Dataset.from_list(formatted), ced_scores


def prepare_eval_data(data_dir, tokenizer, max_docs=50):
    """Load DocRED dev set for task-level evaluation during training."""
    from freige.data.docred_processor import DocREDProcessor
    from freige.eval.evaluator import gold_from_docred

    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process("dev")
    groups = processor.group_by_document(samples)

    eval_items = []
    for doc_id, doc_samples in list(groups.items())[:max_docs]:
        sft_sample = processor.format_sft_sample(doc_samples)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
        ]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )
        eval_items.append({"doc_id": doc_id, "prompt": prompt})

    dev_path = os.path.join(data_dir, "dev.json")
    with open(dev_path) as f:
        dev_data = json.load(f)
    gold = gold_from_docred(dev_data)

    # Also build formatted eval dataset for loss-based eval
    eval_formatted = []
    for doc_id, doc_samples in groups.items():
        sft_sample = processor.format_sft_sample(doc_samples)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
            {"role": "assistant", "content": sft_sample["output"]},
        ]
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False, enable_thinking=False,
        )
        eval_formatted.append({"text": text})
    eval_dataset = Dataset.from_list(eval_formatted)

    return eval_items, gold, eval_dataset


class TaskEvalCallback(TrainerCallback):
    """End-of-epoch task eval: generate on dev subset → compute F1 / Evi-F1 / EDCR."""

    def __init__(self, tokenizer, eval_items, gold, train_file, max_new_tokens=1024):
        self.tokenizer = tokenizer
        self.eval_items = eval_items
        self.gold = gold
        self.train_file = train_file
        self.max_new_tokens = max_new_tokens
        self._evaluator = None

    @property
    def evaluator(self):
        if self._evaluator is None:
            from freige.eval.evaluator import DocREDEvaluator
            if self.train_file and os.path.exists(self.train_file):
                self._evaluator = DocREDEvaluator.from_train_file(self.train_file)
            else:
                self._evaluator = DocREDEvaluator()
        return self._evaluator

    def on_epoch_end(self, args, state, control, model=None, **kwargs):
        if not state.is_world_process_zero:
            return
        self._run_task_eval(model, state)

    def _run_task_eval(self, model, state):
        from freige.eval.evaluator import parse_model_output

        model.eval()
        model.config.use_cache = True
        if hasattr(model, "gradient_checkpointing_disable"):
            model.gradient_checkpointing_disable()

        all_predictions = []
        for item in self.eval_items:
            inputs = self.tokenizer(
                item["prompt"], return_tensors="pt", truncation=True, max_length=4096,
            ).to(model.device)
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=self.max_new_tokens,
                    do_sample=False,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            generated = outputs[0][inputs["input_ids"].shape[1]:]
            text = self.tokenizer.decode(generated, skip_special_tokens=True)
            triples, _ = parse_model_output(text)
            for t in triples:
                t["doc_id"] = item["doc_id"]
            all_predictions.extend(triples)

        metrics = self.evaluator.evaluate(all_predictions, self.gold)

        log_metrics = {
            "eval/rel_f1": metrics["f1"],
            "eval/ign_f1": metrics["ign_f1"],
            "eval/evi_f1": metrics["evi_f1"],
            "eval/evi_precision": metrics["evi_precision"],
            "eval/evi_recall": metrics["evi_recall"],
            "eval/edcr": metrics.get("edcr", 0),
            "eval/n_predictions": len(all_predictions),
        }
        try:
            import wandb
            if wandb.run is not None:
                wandb.log(log_metrics, step=state.global_step)
        except ImportError:
            pass

        logger.info(
            "Task eval @ step %d: F1=%.4f, Ign-F1=%.4f, Evi-F1=%.4f, EDCR=%.4f (%d preds)",
            state.global_step, metrics["f1"], metrics["ign_f1"],
            metrics["evi_f1"], metrics.get("edcr", 0), len(all_predictions),
        )

        model.config.use_cache = False
        if hasattr(model, "gradient_checkpointing_enable"):
            model.gradient_checkpointing_enable()
        model.train()


class WeightedSFTTrainer(SFTTrainer):
    """SFTTrainer with CED score-weighted sampling.

    高 CED score 的样本被更频繁采样。使用 WeightedRandomSampler 实现，
    适用于单机训练。多机 DDP 场景下 Accelerate 会替换 sampler，
    此时 weighted_sampling 不生效，需改用数据集层面的过采样。
    """

    def __init__(self, *args, sample_weights=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.sample_weights = sample_weights

    def _get_train_sampler(self, dataset=None):
        if self.sample_weights is not None:
            ds = dataset if dataset is not None else self.train_dataset
            return WeightedRandomSampler(
                weights=self.sample_weights,
                num_samples=len(ds),
                replacement=True,
            )
        return super()._get_train_sampler(dataset)


def main():
    parser = argparse.ArgumentParser(description="FREIGE RSFT Training")
    parser.add_argument("--base_model", type=str, default=DEFAULT_BASE_MODEL)
    parser.add_argument("--sft_adapter", type=str, default=DEFAULT_SFT_ADAPTER,
                        help="SFT warmup adapter 路径 (merge 后训练新 LoRA)")
    parser.add_argument("--rsft_data_path", type=str, required=True,
                        help="CED 筛选后的 RSFT 训练数据 (JSONL)")
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--learning_rate", type=float, default=2e-5)
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--per_device_batch_size", type=int, default=4)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
    parser.add_argument("--warmup_steps", type=int, default=100)
    parser.add_argument("--save_steps", type=int, default=50)
    parser.add_argument("--save_total_limit", type=int, default=5)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="freige-rsft")
    parser.add_argument("--wandb_run_name", type=str, default=None)
    parser.add_argument("--weighted_sampling", action="store_true",
                        help="按 CED score 加权采样（高分样本更频繁）")
    parser.add_argument("--quantize", action="store_true",
                        help="启用 4-bit QLoRA 量化")
    parser.add_argument("--lora_rank", type=int, default=64)
    parser.add_argument("--lora_alpha", type=int, default=128)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--deepspeed", type=str, default=None,
                        help="DeepSpeed 配置文件路径")
    parser.add_argument("--eval_data_dir", type=str, default=None,
                        help="DocRED data dir (contains dev.json) for task-level eval")
    parser.add_argument("--eval_max_docs", type=int, default=50,
                        help="Max dev docs for task-level eval during training")
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--max_steps", type=int, default=-1,
                        help="Override num_epochs: stop after N steps (-1 = use num_epochs)")
    args = parser.parse_args()

    # W&B
    if args.wandb_project and "WANDB_API_KEY" in os.environ:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_NAME"] = args.wandb_run_name

    # Tokenizer
    logger.info("Loading tokenizer: %s", args.base_model)
    tokenizer = AutoTokenizer.from_pretrained(
        args.base_model, trust_remote_code=True, padding_side="right",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, 'chat_template', None):
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE

    # Data
    logger.info("Loading RSFT data: %s", args.rsft_data_path)
    train_dataset, ced_scores = load_rsft_data(
        args.rsft_data_path, tokenizer, args.max_length,
    )

    # Model: base → merge SFT adapter → new LoRA
    logger.info("Loading base model: %s", args.base_model)
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    model_kwargs = dict(
        trust_remote_code=True,
        attn_implementation="sdpa",
        device_map={"": local_rank},
    )
    if args.quantize:
        logger.info("Using 4-bit QLoRA quantization")
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16

    model = AutoModelForCausalLM.from_pretrained(args.base_model, **model_kwargs)

    if args.sft_adapter:
        logger.info("Merging SFT adapter: %s", args.sft_adapter)
        model = PeftModel.from_pretrained(model, args.sft_adapter)
        model = model.merge_and_unload()

    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # Fresh LoRA for RSFT (与 SFT warmup 相同结构)
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                         "gate_proj", "up_proj", "down_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Eval data
    eval_dataset = None
    callbacks = []
    if args.eval_data_dir:
        logger.info("Loading eval data from %s (max %d docs for task eval)",
                     args.eval_data_dir, args.eval_max_docs)
        eval_items, gold, eval_dataset = prepare_eval_data(
            args.eval_data_dir, tokenizer, args.eval_max_docs,
        )
        train_file = os.path.join(args.eval_data_dir, "train_annotated.json")
        callbacks.append(TaskEvalCallback(
            tokenizer=tokenizer,
            eval_items=eval_items,
            gold=gold,
            train_file=train_file,
            max_new_tokens=args.max_new_tokens,
        ))
        logger.info("Task eval enabled: %d docs, %d gold triples",
                     len(eval_items), len(gold))

    # Training config
    training_args = SFTConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_steps=args.warmup_steps,
        bf16=args.bf16,
        logging_steps=10,
        eval_strategy="epoch" if eval_dataset is not None else "no",
        save_strategy="steps",
        save_steps=args.save_steps,
        save_total_limit=args.save_total_limit,
        seed=args.seed,
        max_length=args.max_length,
        dataset_text_field="text",
        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=args.deepspeed,
        max_steps=args.max_steps,
    )

    sample_weights = ced_scores if args.weighted_sampling else None

    trainer = WeightedSFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
        sample_weights=sample_weights,
        callbacks=callbacks,
    )

    logger.info(
        "Starting RSFT training (%d samples, weighted=%s)...",
        len(train_dataset), args.weighted_sampling,
    )
    trainer.train()

    logger.info("Saving model to %s", args.output_dir)
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("RSFT training complete.")


if __name__ == "__main__":
    main()
