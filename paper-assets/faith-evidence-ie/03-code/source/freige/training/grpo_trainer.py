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
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainerCallback
from trl import GRPOConfig, GRPOTrainer


def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, 'chat_template', None) or ''
    if 'enable_thinking' not in tmpl:
        kwargs.pop('enable_thinking', None)
    return tokenizer.apply_chat_template(messages, **kwargs)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

class KLDivergenceCallback(TrainerCallback):
    """Monitor KL divergence — log only, no early stopping.

    With QLoRA 4-bit, KL between ref and policy is unreliable due to
    quantization noise. We log it for diagnostics but do not penalize or stop.
    """

    def __init__(self, max_kl: float = 100.0):
        self.max_kl = max_kl

    def on_log(self, args, state, control, logs=None, **kwargs):
        if logs and "kl" in logs:
            kl = logs["kl"]
            if kl > self.max_kl:
                logger.warning("KL divergence %.2f exceeds monitoring threshold %.1f (monitoring only, not stopping)", kl, self.max_kl)

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
            if not isinstance(item, dict):
                continue
            has_head = "head" in item or "head_entity" in item
            has_tail = "tail" in item or "tail_entity" in item
            has_rel = "relation" in item or "type" in item or "label" in item
            evi_key = next((k for k in ("evidence", "sentence_ids") if k in item), None)
            has_evi = evi_key is not None and isinstance(item[evi_key], list)
            if has_head and has_tail and has_rel and has_evi:
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
                str(g.get("head") or "").lower().strip(),
                str(g.get("relation") or "").lower().strip(),
                str(g.get("tail") or "").lower().strip(),
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
        recall_penalty: bool = False,
    ):
        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
        self.__name__ = f"{mode}_reward"
        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
        self.verbalize = verbalize_triple
        self.mode = mode
        self._call_count = 0
        self.recall_penalty = recall_penalty
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
                    str(g.get("head") or "").lower().strip(),
                    str(g.get("relation") or "").lower().strip(),
                    str(g.get("tail") or "").lower().strip(),
                )
                gold_map[key] = g

            # F1 gate: at least one predicted triple must match gold
            has_gold_match = False
            for p in pred:
                if isinstance(p, dict):
                    _pk = (
                        str(p.get("head") or "").lower().strip(),
                        str(p.get("relation") or "").lower().strip(),
                        str(p.get("tail") or "").lower().strip(),
                    )
                    if _pk in gold_map:
                        has_gold_match = True
                        break
            if not has_gold_match:
                rewards.append(0.0)
                continue

            matched_gold_keys = set()
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
                if key in gold_map:
                    matched_gold_keys.add(key)
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

            mean_ced = sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
            if self.recall_penalty and gold_map:
                recall = len(matched_gold_keys) / len(gold_map)
                mean_ced *= recall
            rewards.append(mean_ced)

        return rewards


class WeightedRewardFn:
    """Wrap a reward function with a scalar weight."""

    def __init__(self, fn, weight: float):
        self.__name__ = getattr(fn, "__name__", fn.__class__.__name__)
        self.fn = fn
        self.weight = weight

    def __call__(self, *args, **kwargs):
        rewards = self.fn(*args, **kwargs)
        return [r * self.weight for r in rewards]


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
        prompt = _apply_chat_template(tokenizer, 
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
    parser.add_argument("--model_name", type=str, default="./outputs",
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
    parser.add_argument("--learning_rate", "--lr", type=float, default=5e-5)
    parser.add_argument("--tau_start", type=float, default=0.3,
                        help="CED tau 初始值")
    parser.add_argument("--tau_end", type=float, default=0.5,
                        help="CED tau 最终值（线性调度）")
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="your-project")
    parser.add_argument("--wandb_run_name", type=str, default=None)
    parser.add_argument("--format_reward_weight", type=float, default=1.0,
                        help="Weight for format reward")
    parser.add_argument("--f1_reward_weight", type=float, default=1.0,
                        help="Weight for F1 reward")
    parser.add_argument("--ced_reward_weight", type=float, default=1.0,
                        help="Weight for CED reward")
    parser.add_argument("--save_steps", type=int, default=None,
                        help="Save checkpoint every N steps (overrides save_strategy to 'steps')")
    parser.add_argument("--save_total_limit", type=int, default=5,
                        help="Max checkpoints to keep")
    parser.add_argument("--max_steps", type=int, default=-1,
                        help="Max training steps (-1 = use num_epochs)")
    parser.add_argument("--num_iterations", type=int, default=1,
                        help="GRPO num_iterations per batch (>1 enables clipping)")
    parser.add_argument("--kl_coef", type=float, default=0.0,
                        help="KL penalty coefficient (beta)")
    parser.add_argument("--max_kl", type=float, default=100.0,
                        help="KL early stopping threshold")
    parser.add_argument("--ced_recall_penalty", action="store_true", default=False,
                        help="Multiply CED reward by recall to penalize under-prediction")
    parser.add_argument("--resume_from_checkpoint", type=str, default=None)
    args = parser.parse_args()

    if args.wandb_project and "WANDB_API_KEY" in os.environ:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_NAME"] = args.wandb_run_name

    tokenizer_path = args.sft_adapter if args.sft_adapter else args.model_name
    logger.info("Loading tokenizer: %s", tokenizer_path)
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_path,
        trust_remote_code=True,
        padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info("Preparing dataset...")
    train_dataset = prepare_grpo_dataset(
        data_dir=args.data_dir,
        split="train",
        tokenizer=tokenizer,
    )

    logger.info("Loading model: %s", args.model_name)
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
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
        model_kwargs["device_map"] = {"":  local_rank}
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)

    if args.sft_adapter:
        logger.info("Loading SFT adapter from %s", args.sft_adapter)
        model = PeftModel.from_pretrained(model, args.sft_adapter)
        model = model.merge_and_unload()

    reward_fns = [
        WeightedRewardFn(format_reward_fn, args.format_reward_weight),
        WeightedRewardFn(f1_reward_fn, args.f1_reward_weight),
    ]

    if args.stage >= 2 and args.ced_reward_weight > 0:
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
            recall_penalty=args.ced_recall_penalty,
        )
        reward_fns.append(WeightedRewardFn(ced_wrapper, args.ced_reward_weight))
        logger.info(
            "Stage %d: using %s reward, tau %.2f→%.2f over %d steps",
            args.stage, mode, args.tau_start, args.tau_end, total_steps,
        )
    else:
        logger.info("Extraction-only mode: format + F1 rewards (stage=%d, ced_weight=%.1f)", args.stage, args.ced_reward_weight)

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                         "gate_proj", "up_proj", "down_proj"],
    )

    save_strategy = "steps" if args.save_steps else "epoch"
    save_steps = args.save_steps if args.save_steps else None

    grpo_config_kwargs = dict(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        bf16=args.bf16,
        logging_steps=5,
        save_strategy=save_strategy,
        save_total_limit=args.save_total_limit,
        seed=args.seed,
        num_generations=args.num_generations,
        max_completion_length=args.max_new_tokens,
        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=args.deepspeed,
        num_iterations=args.num_iterations,
        generation_batch_size=args.num_generations,
    )
    if save_steps:
        grpo_config_kwargs["save_steps"] = save_steps
    if args.max_steps > 0:
        grpo_config_kwargs["max_steps"] = args.max_steps
    if args.kl_coef > 0:
        grpo_config_kwargs["beta"] = args.kl_coef
    grpo_config = GRPOConfig(**grpo_config_kwargs)

    callbacks = [KLDivergenceCallback(max_kl=args.max_kl)]

    trainer = GRPOTrainer(
        model=model,
        args=grpo_config,
        train_dataset=train_dataset,
        reward_funcs=reward_fns,
        peft_config=lora_config,
        processing_class=tokenizer,
        callbacks=callbacks,
    )

    logger.info("Starting GRPO training (stage %d)...", args.stage)
    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)

    logger.info("Saving model to %s", args.output_dir)
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("GRPO training (stage %d) complete.", args.stage)


if __name__ == "__main__":
    main()
