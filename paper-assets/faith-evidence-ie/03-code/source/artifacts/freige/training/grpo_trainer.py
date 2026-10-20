"""GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。

支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。

单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1
多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \
            --stage 1 --reward_device cpu
不量化: 加 --no_quantize
"""

import argparse
import json
import logging
import math
import os
import re
from pathlib import Path
from typing import Optional

import torch
from datasets import Dataset
from peft import LoraConfig, PeftModel, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import GRPOConfig, GRPOTrainer

from freige.training import LLAMA3_CHAT_TEMPLATE

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)


def _parse_json_output(text: str) -> list[dict]:
    """从模型输出中解析 JSON 列表。"""
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


def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
    rewards = []
    for text in completions:
        parsed = _parse_json_output(text)
        if not isinstance(parsed, list):
            rewards.append(0.0)
            continue
        if not parsed:
            rewards.append(0.1)
            continue
        valid = 0
        for item in parsed:
            if (isinstance(item, dict) and "head" in item
                    and "relation" in item and "tail" in item
                    and "evidence" in item
                    and isinstance(item["evidence"], list)):
                valid += 1
        rewards.append(valid / len(parsed))
    return rewards


def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。

    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
    completions 中每 num_generations 个对应同一个 prompt。
    """
    num_gen = len(completions) // len(gold_triples)
    rewards = []

    for i, text in enumerate(completions):
        gold_idx = i // num_gen
        gold_str = gold_triples[gold_idx]
        try:
            gold = json.loads(gold_str)
        except (json.JSONDecodeError, IndexError):
            rewards.append(0.0)
            continue

        pred = _parse_json_output(text)

        gold_set = set()
        for g in gold:
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
            rewards.append(1.0 if not pred_set else 0.0)
            continue

        tp = len(pred_set & gold_set)
        prec = tp / len(pred_set) if pred_set else 0.0
        rec = tp / len(gold_set) if gold_set else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        rewards.append(f1)

    return rewards


class CEDRewardWrapper:
    """将 CED 奖励封装为 GRPO 兼容的 reward function。

    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，
    返回所有 triples 的平均 CED reward。
    """

    def __init__(
        self,
        nli_model: str = "cross-encoder/nli-deberta-v3-base",
        tau: float = 0.5,
        mode: str = "ced",
        device: str = None,
        tau_start: float = None,
        tau_end: float = None,
        total_steps: int = None,
    ):
        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
        self.__name__ = f"{mode}_reward"
        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
        self.verbalize = verbalize_triple
        self.mode = mode
        self._call_count = 0
        if tau_start is not None and tau_end is not None:
            self.tau_start = tau_start
            self.tau_end = tau_end
            self.total_steps = total_steps
        else:
            self.tau_start = tau
            self.tau_end = tau
            self.total_steps = None

    @property
    def tau(self) -> float:
        if self.total_steps and self.total_steps > 0:
            progress = min(self._call_count / self.total_steps, 1.0)
        else:
            progress = 1.0
        return self.tau_start + (self.tau_end - self.tau_start) * progress

    def __call__(
        self,
        completions: list[str],
        all_sents: list[str],
        gold_triples: list[str],
        **kwargs,
    ) -> list[float]:
        """计算 CED/flat-NLI 奖励。

        all_sents: JSON 字符串列表，每个元素为文档句子列表。
        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。
        """
        current_tau = self.tau
        self._call_count += 1
        num_gen = len(completions) // len(all_sents)
        rewards = []

        for i, text in enumerate(completions):
            prompt_idx = i // num_gen
            try:
                sents = json.loads(all_sents[prompt_idx])
                gold = json.loads(gold_triples[prompt_idx])
            except (json.JSONDecodeError, IndexError):
                rewards.append(0.0)
                continue

            pred = _parse_json_output(text)
            if not pred:
                rewards.append(0.0)
                continue

            gold_map = {}
            for g in gold:
                key = (
                    g.get("head", "").lower().strip(),
                    g.get("relation", "").lower().strip(),
                    g.get("tail", "").lower().strip(),
                )
                gold_map[key] = g

            triple_rewards = []
            for p in pred:
                if not isinstance(p, dict):
                    continue
                pred_evi_ids = p.get("evidence", [])
                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
                    triple_rewards.append(0.0)
                    continue

                claim = self.verbalize(
                    str(p.get("head") or ""),
                    str(p.get("relation") or ""),
                    str(p.get("tail") or ""),
                )
                cited_sents = [sents[idx] for idx in pred_evi_ids
                               if isinstance(idx, int) and 0 <= idx < len(sents)]
                if not cited_sents:
                    triple_rewards.append(0.0)
                    continue

                key = (
                    str(p.get("head") or "").lower().strip(),
                    str(p.get("relation") or "").lower().strip(),
                    str(p.get("tail") or "").lower().strip(),
                )
                matched_gold = gold_map.get(key, {})
                hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
                hard_neg_sents = [sents[idx] for idx in hard_neg_ids
                                  if isinstance(idx, int) and 0 <= idx < len(sents)]

                if self.mode == "flat_nli":
                    result = self.reward_model.compute_flat_nli_reward(
                        claim, cited_sents, tau=current_tau,
                    )
                else:
                    result = self.reward_model.compute_ced_reward(
                        claim, cited_sents, hard_neg_sents, tau=current_tau,
                    )
                triple_rewards.append(result["reward"])

            rewards.append(
                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
            )

        return rewards


def prepare_grpo_dataset(
    data_dir: str = None,
    split: str = "train",
    tokenizer=None,
) -> Dataset:
    """准备 GRPO prompt 数据集。

    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。
    """
    from freige.data.docred_processor import DocREDProcessor

    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process(split)
    groups = processor.group_by_document(samples)

    dataset_items = []
    for doc_id, doc_samples in groups.items():
        sft_sample = processor.format_sft_sample(doc_samples)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
        ]
        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
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
        dataset_items.append({
            "prompt": prompt,
            "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
            "all_sents": json.dumps(ref.sents, ensure_ascii=False),
        })

    logger.info("Prepared %d GRPO prompts", len(dataset_items))
    return Dataset.from_list(dataset_items)


def main():
    parser = argparse.ArgumentParser(description="FREIGE GRPO Training")
    parser.add_argument("--model_name", type=str, default="/root/autodl-tmp/models/Qwen3-4B",
                        help="基础模型或 SFT checkpoint 路径")
    parser.add_argument("--sft_adapter", type=str, default=None,
                        help="SFT LoRA adapter 路径（如果与 model_name 不同）")
    parser.add_argument("--data_dir", type=str, default=None)
    parser.add_argument("--output_dir", type=str, default="./grpo_output")
    parser.add_argument("--stage", type=int, default=1, choices=[1, 2, 3],
                        help="Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED")
    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
    parser.add_argument("--num_generations", type=int, default=4)
    parser.add_argument("--lora_rank", type=int, default=64)
    parser.add_argument("--lora_alpha", type=int, default=128)
    parser.add_argument("--max_length", type=int, default=4096)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
    parser.add_argument("--deepspeed", type=str, default=None,
                        help="DeepSpeed 配置文件路径")
    parser.add_argument("--reward_device", type=str, default="cpu",
                        help="CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）")
    parser.add_argument("--per_device_batch_size", type=int, default=1)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
    parser.add_argument("--num_epochs", type=int, default=1)
    parser.add_argument("--learning_rate", type=float, default=5e-5)
    parser.add_argument("--tau_start", type=float, default=0.3,
                        help="CED tau 初始值")
    parser.add_argument("--tau_end", type=float, default=0.5,
                        help="CED tau 最终值（线性调度）")
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="freige-grpo")
    parser.add_argument("--wandb_run_name", type=str, default=None)
    args = parser.parse_args()

    if args.wandb_project and "WANDB_API_KEY" in os.environ:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_NAME"] = args.wandb_run_name

    logger.info("Loading tokenizer: %s", args.model_name)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name,
        trust_remote_code=True,
        padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, 'chat_template', None):
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE

    logger.info("Preparing dataset...")
    train_dataset = prepare_grpo_dataset(
        data_dir=args.data_dir,
        split="train",
        tokenizer=tokenizer,
    )

    logger.info("Loading model: %s", args.model_name)
    model_kwargs = dict(
        trust_remote_code=True,
        attn_implementation="sdpa",
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
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)

    if args.sft_adapter:
        logger.info("Loading SFT adapter from %s", args.sft_adapter)
        model = PeftModel.from_pretrained(model, args.sft_adapter)
        model = model.merge_and_unload()

    reward_fns = [format_reward_fn, f1_reward_fn]

    if args.stage >= 2:
        mode = "flat_nli" if args.stage == 2 else "ced"
        num_gpus = int(os.environ.get("WORLD_SIZE", 1))
        steps_per_epoch = math.ceil(
            len(train_dataset) / (args.per_device_batch_size * num_gpus * args.gradient_accumulation_steps)
        )
        total_steps = steps_per_epoch * args.num_epochs
        ced_wrapper = CEDRewardWrapper(
            nli_model=args.nli_model,
            mode=mode,
            device=args.reward_device,
            tau_start=args.tau_start,
            tau_end=args.tau_end,
            total_steps=total_steps,
        )
        reward_fns.append(ced_wrapper)
        logger.info(
            "Stage %d: using %s reward, tau %.2f→%.2f over %d steps",
            args.stage, mode, args.tau_start, args.tau_end, total_steps,
        )
    else:
        logger.info("Stage 1: extraction-only (format + F1 rewards)")

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                         "gate_proj", "up_proj", "down_proj"],
    )

    grpo_config = GRPOConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        bf16=args.bf16,
        logging_steps=5,
        save_strategy="epoch",
        save_total_limit=2,
        seed=args.seed,
        num_generations=args.num_generations,
        max_completion_length=args.max_new_tokens,
        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=args.deepspeed,
    )

    trainer = GRPOTrainer(
        model=model,
        args=grpo_config,
        train_dataset=train_dataset,
        reward_funcs=reward_fns,
        peft_config=lora_config,
        processing_class=tokenizer,
    )

    logger.info("Starting GRPO training (stage %d)...", args.stage)
    trainer.train()

    logger.info("Saving model to %s", args.output_dir)
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("GRPO training (stage %d) complete.", args.stage)


if __name__ == "__main__":
    main()
