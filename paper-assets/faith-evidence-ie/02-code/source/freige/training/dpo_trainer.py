"""DPO (Direct Preference Optimization) 训练脚本。

从 SFT warmup checkpoint 继续训练，使用 CED 打分构建的偏好对。
流程: base model → merge SFT adapter → 新 LoRA → DPO 训练。

禁止使用 QLoRA 4-bit 量化（CUBLAS 错误），使用 bf16 全精度 + LoRA。

输入: dpo_pairs.jsonl，每行 {"input", "chosen", "rejected", "margin", ...}
       (由 dpo_data_builder.py 生成)
输出: LoRA adapter checkpoint
依赖: transformers, trl, peft, datasets

单卡:   python -m freige.training.dpo_trainer \
            --dpo_data_path data.jsonl --output_dir ./dpo_output
多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
            -m freige.training.dpo_trainer \
            --dpo_data_path data.jsonl --output_dir ./dpo_output
"""

import argparse
import json
import logging
import os

import torch
from datasets import Dataset
from peft import LoraConfig, PeftModel, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import DPOConfig, DPOTrainer

from freige.training.sft_trainer import SYSTEM_PROMPT


def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, 'chat_template', None) or ''
    if 'enable_thinking' not in tmpl:
        kwargs.pop('enable_thinking', None)
    return tokenizer.apply_chat_template(messages, **kwargs)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_BASE_MODEL = "./outputs"
DEFAULT_SFT_ADAPTER = "./outputs"


def load_dpo_data(data_path: str, tokenizer, max_length: int = 2048):
    """加载 DPO 偏好对，格式化为 TRL DPOTrainer 所需格式。

    使用 apply_chat_template 将 input/chosen/rejected 转换为带 chat token 的文本。
    超过 max_length 的样本跳过（不截断，避免不完整 JSON 输出）。

    Returns:
        Dataset with columns: prompt, chosen, rejected (text strings)
    """
    samples = []
    with open(data_path) as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))

    logger.info("Loaded %d DPO pairs from %s", len(samples), data_path)

    prompt_msgs_template = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

    formatted = []
    skipped = 0
    for s in samples:
        user_msg = {"role": "user", "content": s["input"]}
        prompt_msgs = prompt_msgs_template + [user_msg]

        prompt_text = _apply_chat_template(tokenizer, 
            prompt_msgs, tokenize=False,
            add_generation_prompt=True, enable_thinking=False,
        )

        # 用 apply_chat_template 生成完整对话文本，提取 response 部分（含 <|im_end|>）
        chosen_full = _apply_chat_template(tokenizer, 
            prompt_msgs + [{"role": "assistant", "content": s["chosen"]}],
            tokenize=False, add_generation_prompt=False, enable_thinking=False,
        )
        rejected_full = _apply_chat_template(tokenizer, 
            prompt_msgs + [{"role": "assistant", "content": s["rejected"]}],
            tokenize=False, add_generation_prompt=False, enable_thinking=False,
        )

        chosen_response = chosen_full[len(prompt_text):]
        rejected_response = rejected_full[len(prompt_text):]

        max_tok = max(
            len(tokenizer.encode(chosen_full, add_special_tokens=False)),
            len(tokenizer.encode(rejected_full, add_special_tokens=False)),
        )
        if max_tok > max_length:
            skipped += 1
            continue

        formatted.append({
            "prompt": prompt_text,
            "chosen": chosen_response,
            "rejected": rejected_response,
        })

    if skipped:
        logger.warning("Skipped %d pairs exceeding max_length=%d", skipped, max_length)

    logger.info("Prepared %d DPO pairs for training", len(formatted))
    return Dataset.from_list(formatted)


def main():
    parser = argparse.ArgumentParser(description="FREIGE DPO Training")
    parser.add_argument("--base_model", type=str, default=DEFAULT_BASE_MODEL)
    parser.add_argument("--sft_adapter", type=str, default=DEFAULT_SFT_ADAPTER,
                        help="SFT warmup adapter 路径 (set '' to skip)")
    parser.add_argument("--dpo_data_path", type=str, required=True,
                        help="DPO 偏好对数据 (dpo_pairs.jsonl)")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="LoRA adapter 输出目录")

    # DPO 参数
    parser.add_argument("--beta", type=float, default=0.1,
                        help="DPO KL penalty coefficient (default: 0.1)")
    parser.add_argument("--loss_type", type=str, default="sigmoid",
                        choices=["sigmoid", "hinge", "ipo", "kto_pair"],
                        help="DPO loss 类型 (default: sigmoid)")
    parser.add_argument("--label_smoothing", type=float, default=0.0,
                        help="Label smoothing (default: 0.0)")

    # 训练参数
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--per_device_batch_size", type=int, default=2)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=8)
    parser.add_argument("--learning_rate", type=float, default=5e-6,
                        help="DPO 学习率，通常比 SFT 小 (default: 5e-6)")
    parser.add_argument("--warmup_steps", type=int, default=50)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--max_prompt_length", type=int, default=1536)
    parser.add_argument("--save_steps", type=int, default=100)
    parser.add_argument("--save_total_limit", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)

    # W&B
    parser.add_argument("--wandb_project", type=str, default="your-project")
    parser.add_argument("--wandb_run_name", type=str, default=None)

    # LoRA
    parser.add_argument("--lora_rank", type=int, default=64)
    parser.add_argument("--lora_alpha", type=int, default=128)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--deepspeed", type=str, default=None,
                        help="DeepSpeed 配置文件路径")
    args = parser.parse_args()

    # W&B
    if args.wandb_project and "WANDB_API_KEY" in os.environ:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_NAME"] = args.wandb_run_name

    # Tokenizer
    logger.info("Loading tokenizer: %s", args.base_model)
    tokenizer = AutoTokenizer.from_pretrained(
        args.base_model, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Data
    logger.info("Loading DPO data: %s", args.dpo_data_path)
    train_dataset = load_dpo_data(
        args.dpo_data_path, tokenizer, args.max_length,
    )

    # Model: base -> merge SFT adapter -> new LoRA (bf16, no quantization)
    logger.info("Loading base model (bf16, no quantization): %s", args.base_model)
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        trust_remote_code=True,
        attn_implementation="sdpa",
        torch_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        device_map={"": local_rank},
    )

    if args.sft_adapter:
        logger.info("Merging SFT adapter: %s", args.sft_adapter)
        model = PeftModel.from_pretrained(model, args.sft_adapter)
        model = model.merge_and_unload()

    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # Fresh LoRA for DPO (与 SFT/RSFT 相同结构)
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

    # DPOTrainer + PEFT: ref_model=None 时自动用 frozen base weights 作为 reference。
    # 由于我们先 merge 了 SFT adapter 再加新 LoRA，frozen weights = SFT checkpoint。

    training_args = DPOConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_steps=args.warmup_steps,
        bf16=args.bf16,
        logging_steps=10,
        save_strategy="steps",
        save_steps=args.save_steps,
        save_total_limit=args.save_total_limit,
        seed=args.seed,
        beta=args.beta,
        loss_type=args.loss_type,
        label_smoothing=args.label_smoothing,
        max_length=args.max_length,

        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=args.deepspeed,
    )

    trainer = DPOTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        processing_class=tokenizer,
    )

    logger.info(
        "Starting DPO training (%d pairs, beta=%.2f, loss=%s)...",
        len(train_dataset), args.beta, args.loss_type,
    )
    trainer.train()

    logger.info("Saving model to %s", args.output_dir)
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("DPO training complete.")


if __name__ == "__main__":
    main()
