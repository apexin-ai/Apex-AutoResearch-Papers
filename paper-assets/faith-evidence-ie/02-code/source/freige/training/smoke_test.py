#!/usr/bin/env python3
# Launch:
#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py
#   deepspeed --num_gpus 4 training/smoke_test.py
"""Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).

Uses synthetic data only. No freige imports. Runs 10 training steps and reports
loss trend, peak VRAM, gradient norms, and PASS/FAIL.
"""

import json
import math
import os
import random
import time

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import GRPOConfig, GRPOTrainer


def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, 'chat_template', None) or ''
    if 'enable_thinking' not in tmpl:
        kwargs.pop('enable_thinking', None)
    return tokenizer.apply_chat_template(messages, **kwargs)


os.environ.setdefault("WANDB_DISABLED", "true")

SEED = 42
NUM_STEPS = 10
NUM_GENERATIONS = 4
MAX_COMPLETION_LENGTH = 256
MODEL_NAME = "./outputs"

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)

DEEPSPEED_CONFIG = {
    "bf16": {"enabled": True},
    "zero_optimization": {
        "stage": 2,
        "offload_optimizer": {
            "device": "cpu",
            "pin_memory": True
        },
        "allgather_partitions": True,
        "allgather_bucket_size": 5e8,
        "reduce_scatter": True,
        "reduce_bucket_size": 5e8,
        "overlap_comm": True,
        "contiguous_gradients": True
    },
    "gradient_accumulation_steps": "auto",
    "gradient_clipping": "auto",
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto",
}

DUMMY_DOCS = [
    {
        "sents": [
            "Albert Einstein was born in Ulm, Germany in 1879.",
            "He developed the theory of relativity while working at the Swiss Patent Office.",
            "Einstein later moved to the United States and joined Princeton University.",
            "He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.",
        ],
        "entities": ["Albert Einstein", "Ulm", "Germany", "United States", "Princeton University"],
        "triples": [
            {"head": "Albert Einstein", "relation": "place of birth", "tail": "Ulm", "evidence": [0]},
            {"head": "Albert Einstein", "relation": "country of citizenship", "tail": "Germany", "evidence": [0]},
            {"head": "Albert Einstein", "relation": "employer", "tail": "Princeton University", "evidence": [2]},
        ],
    },
    {
        "sents": [
            "The Eiffel Tower is a wrought-iron lattice tower in Paris, France.",
            "It was designed by Gustave Eiffel's company and built between 1887 and 1889.",
            "The tower is 330 metres tall and the tallest structure in Paris.",
            "It has become a global cultural icon of France.",
        ],
        "entities": ["Eiffel Tower", "Paris", "France", "Gustave Eiffel"],
        "triples": [
            {"head": "Eiffel Tower", "relation": "located in", "tail": "Paris", "evidence": [0]},
            {"head": "Eiffel Tower", "relation": "country", "tail": "France", "evidence": [0, 3]},
            {"head": "Eiffel Tower", "relation": "creator", "tail": "Gustave Eiffel", "evidence": [1]},
        ],
    },
    {
        "sents": [
            "Tokyo is the capital and most populous city of Japan.",
            "The Greater Tokyo Area is the most populous metropolitan area in the world.",
            "Tokyo was originally known as Edo and was renamed in 1868.",
            "The city hosted the Summer Olympics in 1964 and 2021.",
        ],
        "entities": ["Tokyo", "Japan", "Edo"],
        "triples": [
            {"head": "Tokyo", "relation": "capital of", "tail": "Japan", "evidence": [0]},
            {"head": "Tokyo", "relation": "country", "tail": "Japan", "evidence": [0]},
        ],
    },
    {
        "sents": [
            "Marie Curie was a Polish-French physicist and chemist.",
            "She conducted pioneering research on radioactivity at the University of Paris.",
            "Curie was the first woman to win a Nobel Prize in 1903.",
            "She won a second Nobel Prize in Chemistry in 1911.",
            "Marie Curie was born in Warsaw, Poland.",
        ],
        "entities": ["Marie Curie", "University of Paris", "Warsaw", "Poland"],
        "triples": [
            {"head": "Marie Curie", "relation": "employer", "tail": "University of Paris", "evidence": [1]},
            {"head": "Marie Curie", "relation": "place of birth", "tail": "Warsaw", "evidence": [4]},
            {"head": "Marie Curie", "relation": "country of citizenship", "tail": "Poland", "evidence": [0, 4]},
        ],
    },
    {
        "sents": [
            "Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.",
            "The company started as an online bookstore.",
            "Amazon's headquarters is located in Seattle, Washington.",
            "It is one of the Big Five American technology companies.",
        ],
        "entities": ["Amazon", "Jeff Bezos", "Bellevue", "Seattle", "Washington"],
        "triples": [
            {"head": "Amazon", "relation": "founded by", "tail": "Jeff Bezos", "evidence": [0]},
            {"head": "Amazon", "relation": "headquarters location", "tail": "Seattle", "evidence": [2]},
            {"head": "Amazon", "relation": "location of formation", "tail": "Bellevue", "evidence": [0]},
        ],
    },
]


def generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:
    rng = random.Random(seed)
    items = []
    for i in range(n_samples):
        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]
        numbered = "\n".join(f"[{j}] {s}" for j, s in enumerate(doc["sents"]))
        entity_str = ", ".join(doc["entities"])
        user_msg = (
            f"Document:\n{numbered}\n\n"
            f"Entities: {entity_str}\n\n"
            "Extract all relation triples with evidence sentence IDs."
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ]
        prompt = _apply_chat_template(tokenizer, 
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )
        gold = rng.sample(doc["triples"], k=min(len(doc["triples"]), rng.randint(1, 3)))
        items.append({
            "prompt": prompt,
            "gold_triples": json.dumps(gold, ensure_ascii=False),
        })
    return Dataset.from_list(items)


def _parse_json_output(text: str) -> list[dict]:
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


class LossLogger:
    def __init__(self):
        self.losses = []
        self.grad_norms = []


loss_logger = LossLogger()
_orig_log = None


def _patch_trainer_logging(trainer):
    global _orig_log
    _orig_log = trainer.log

    def patched_log(logs, *args, **kwargs):
        if "loss" in logs:
            loss_logger.losses.append(logs["loss"])
        if "grad_norm" in logs:
            loss_logger.grad_norms.append(logs["grad_norm"])
        return _orig_log(logs, *args, **kwargs)

    trainer.log = patched_log


def main():
    t0 = time.time()
    local_rank = int(os.environ.get("LOCAL_RANK", 0))

    print(f"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side="left")
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"[rank {local_rank}] Generating dummy dataset...")
    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)

    print(f"[rank {local_rank}] Loading model with 4-bit QLoRA...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        trust_remote_code=True,
        attn_implementation="sdpa",
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=64,
        lora_alpha=128,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    )

    output_dir = "/tmp/freige_smoke_test"
    grpo_config = GRPOConfig(
        output_dir=output_dir,
        max_steps=NUM_STEPS,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=2,
        learning_rate=5e-5,
        bf16=True,
        logging_steps=1,
        save_strategy="no",
        seed=SEED,
        num_generations=NUM_GENERATIONS,
        max_completion_length=MAX_COMPLETION_LENGTH,
        report_to="none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=DEEPSPEED_CONFIG,
    )

    trainer = GRPOTrainer(
        model=model,
        args=grpo_config,
        train_dataset=dataset,
        reward_funcs=[format_reward_fn],
        peft_config=lora_config,
        processing_class=tokenizer,
    )
    _patch_trainer_logging(trainer)

    print(f"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...")
    torch.cuda.reset_peak_memory_stats()
    trainer.train()
    elapsed = time.time() - t0

    if local_rank == 0:
        print("\n" + "=" * 60)
        print("SMOKE TEST RESULTS")
        print("=" * 60)

        print(f"\n--- Loss per step ---")
        for i, loss in enumerate(loss_logger.losses):
            print(f"  step {i + 1}: {loss:.4f}")

        print(f"\n--- Gradient norms ---")
        for i, gn in enumerate(loss_logger.grad_norms):
            print(f"  step {i + 1}: {gn:.4f}")

        print(f"\n--- GPU peak memory ---")
        for i in range(torch.cuda.device_count()):
            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2
            print(f"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)")

        print(f"\n--- Total time: {elapsed:.1f}s ---")

        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)
        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False
        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True

        if len(loss_logger.losses) >= 4:
            last3_avg = sum(loss_logger.losses[-3:]) / 3
            first_loss = loss_logger.losses[0]
            loss_decreased = last3_avg < first_loss
        else:
            loss_decreased = True

        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad

        print(f"\n--- Diagnostics ---")
        print(f"  Loss decreased (last 3 avg < first): {loss_decreased}")
        print(f"  NaN in loss: {has_nan_loss}")
        print(f"  NaN in grad_norm: {has_nan_grad}")
        print(f"  All-zero grad_norm: {has_zero_grad}")
        print(f"\n{'PASS' if passed else 'FAIL'}")
        print("=" * 60)


if __name__ == "__main__":
    main()
