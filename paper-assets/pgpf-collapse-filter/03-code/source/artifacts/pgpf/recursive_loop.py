"""Recursive training loop: LoRA fine-tune → generate → score → filter → next generation.

Orchestrates the full PGPF pipeline across multiple generations.
Each generation: train on (filtered synthetic + optional real data), generate new synthetic,
score with property metrics, filter, repeat.
"""

import argparse
import json
import time
from pathlib import Path
from typing import Optional

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ImportError:
    torch = None

from pgpf.config import PGPFConfig
from pgpf.data_prep import load_dataset_splits, extract_assistant_texts
from pgpf.filters import build_filter, BaseFilter
from pgpf.metrics import corpus_self_bleu, vocab_coverage, embedding_diversity, held_out_perplexity
from pgpf.property_scorer import PropertyScorer
from pgpf.utils import save_jsonl, load_jsonl, save_json, ensure_dir, set_seed, logger, get_device


class RecursiveTrainingLoop:
    def __init__(self, config: PGPFConfig):
        self.config = config
        self.device = get_device()
        self.scorer = PropertyScorer(
            embedding_model_name=config.embedding_model,
            corpus_k=config.bleu_corpus_k,
            device=str(self.device),
        )
        self.filter: BaseFilter = build_filter(config)

        self._base_model = None
        self._base_tokenizer = None
        self._reference_vocab: Optional[set[str]] = None

    def run(self) -> None:
        set_seed(self.config.seed)
        ensure_dir(self.config.output_dir)

        data_splits = load_dataset_splits(self.config.data_dir)
        train_data = data_splits["train"]
        eval_texts = extract_assistant_texts(data_splits.get("test", []))

        # Gen-0 reference stats
        gen0_texts = extract_assistant_texts(train_data)
        self._reference_vocab = set(w for t in gen0_texts for w in t.split())
        logger.info("Setting gen-0 reference corpus for scorer...")
        self.scorer.set_reference_corpus(gen0_texts)

        current_train_data = train_data
        all_generation_metrics = []

        for gen in range(self.config.num_generations):
            logger.info(f"=== Generation {gen} ===")
            gen_dir = ensure_dir(Path(self.config.output_dir) / f"gen_{gen}")
            gen_start = time.time()

            # Step 1: LoRA fine-tune
            logger.info(f"[Gen {gen}] Fine-tuning with {len(current_train_data)} samples...")
            model, tokenizer = self._train_generation(current_train_data, gen)

            # Step 2: Generate synthetic data
            logger.info(f"[Gen {gen}] Generating {self.config.num_synthetic_per_gen} synthetic samples...")
            synthetic = self._generate_synthetic(model, tokenizer, train_data)
            save_jsonl(synthetic, self.config.synthetic_data_path(gen))

            # Step 3: Score synthetic samples
            logger.info(f"[Gen {gen}] Scoring synthetic samples...")
            synthetic_texts = extract_assistant_texts(synthetic)

            base_model, base_tokenizer = self._get_base_model()
            scores = self.scorer.score_batch(
                synthetic_texts,
                model=model,
                tokenizer=tokenizer,
                base_model=base_model,
                base_tokenizer=base_tokenizer,
            )

            scored_data = []
            for sample, score in zip(synthetic, scores):
                scored_data.append({**sample, "scores": score})
            save_jsonl(scored_data, self.config.scored_data_path(gen))

            # Step 4: Filter
            logger.info(f"[Gen {gen}] Filtering with {self.config.filter_method}...")
            filtered = self.filter.filter(synthetic, scores)
            logger.info(f"[Gen {gen}] Kept {len(filtered)}/{len(synthetic)} samples")

            # Step 5: Evaluate
            logger.info(f"[Gen {gen}] Computing evaluation metrics...")
            filtered_texts = extract_assistant_texts(filtered)
            gen_metrics = self._compute_metrics(model, tokenizer, filtered_texts, eval_texts, gen)
            gen_metrics["num_train_samples"] = len(current_train_data)
            gen_metrics["num_synthetic"] = len(synthetic)
            gen_metrics["num_filtered"] = len(filtered)
            gen_metrics["generation"] = gen
            gen_metrics["elapsed_seconds"] = time.time() - gen_start
            save_json(gen_metrics, self.config.metrics_path(gen))
            all_generation_metrics.append(gen_metrics)
            logger.info(f"[Gen {gen}] Metrics: {json.dumps(gen_metrics, indent=2)}")

            # Step 6: Prepare next generation's training data
            if self.config.real_data_mix_ratio > 0:
                import random
                n_real = int(len(filtered) * self.config.real_data_mix_ratio / (1 - self.config.real_data_mix_ratio))
                n_real = min(n_real, len(train_data))
                real_subset = random.sample(train_data, n_real)
                current_train_data = filtered + real_subset
            else:
                current_train_data = filtered

            # Free GPU memory
            del model
            torch.cuda.empty_cache() if torch.cuda.is_available() else None

        save_json(all_generation_metrics, Path(self.config.output_dir) / "all_metrics.json")
        logger.info("Recursive training complete.")

    def _train_generation(self, train_data: list[dict], generation: int) -> tuple:
        """LoRA fine-tune on train_data, return (model, tokenizer)."""
        from peft import LoraConfig, get_peft_model
        from trl import SFTTrainer, SFTConfig
        from datasets import Dataset

        cfg = self.config
        checkpoint_dir = str(cfg.checkpoint_dir(generation))

        tokenizer = AutoTokenizer.from_pretrained(cfg.model_name, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True,
        )

        lora_config = LoraConfig(
            r=cfg.lora.r,
            lora_alpha=cfg.lora.lora_alpha,
            lora_dropout=cfg.lora.lora_dropout,
            target_modules=cfg.lora.target_modules,
            task_type=cfg.lora.task_type,
        )
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

        train_ds = Dataset.from_list(train_data)

        training_args = SFTConfig(
            output_dir=checkpoint_dir,
            per_device_train_batch_size=cfg.training.per_device_train_batch_size,
            gradient_accumulation_steps=cfg.training.gradient_accumulation_steps,
            learning_rate=cfg.training.learning_rate,
            lr_scheduler_type=cfg.training.lr_scheduler_type,
            warmup_steps=cfg.training.warmup_steps,
            num_train_epochs=cfg.training.num_train_epochs,
            max_length=cfg.training.max_seq_length,
            bf16=cfg.training.bf16,
            logging_steps=cfg.training.logging_steps,
            save_strategy=cfg.training.save_strategy,
            report_to="none",
            seed=cfg.seed,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_ds,
            processing_class=tokenizer,
        )
        trainer.train()
        trainer.save_model(checkpoint_dir)

        return model, tokenizer

    def _generate_synthetic(
        self, model, tokenizer, real_data: list[dict], batch_size: int = 8
    ) -> list[dict]:
        """Generate synthetic responses in batches using the current model on real prompts."""
        import random

        cfg = self.config
        prompts = []
        for sample in real_data:
            msgs = sample["messages"]
            context = [m for m in msgs if m["role"] in ("system", "user")]
            if context:
                prompts.append(context)

        random.shuffle(prompts)
        prompts = prompts[: cfg.num_synthetic_per_gen]

        model.eval()
        tokenizer.padding_side = "left"
        synthetic = []
        n_total = len(prompts)

        for batch_start in range(0, n_total, batch_size):
            batch_prompts = prompts[batch_start : batch_start + batch_size]
            prompt_texts = [
                tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
                for msgs in batch_prompts
            ]

            try:
                inputs = tokenizer(
                    prompt_texts,
                    return_tensors="pt",
                    truncation=True,
                    max_length=cfg.training.max_seq_length,
                    padding=True,
                )
                input_ids = inputs.input_ids.to(model.device)
                attention_mask = inputs.attention_mask.to(model.device)

                with torch.no_grad():
                    outputs = model.generate(
                        input_ids,
                        attention_mask=attention_mask,
                        max_new_tokens=cfg.generation.max_new_tokens,
                        temperature=cfg.generation.temperature,
                        top_p=cfg.generation.top_p,
                        do_sample=cfg.generation.do_sample,
                        pad_token_id=tokenizer.pad_token_id,
                    )

                for i, context_msgs in enumerate(batch_prompts):
                    new_tokens = outputs[i][input_ids.shape[1] :]
                    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
                    full_messages = list(context_msgs) + [{"role": "assistant", "content": response}]
                    synthetic.append({"messages": full_messages})

            except Exception as e:
                logger.warning(f"Batch generation failed at {batch_start}: {e}, falling back to per-sample")
                for context_msgs in batch_prompts:
                    try:
                        prompt_text = tokenizer.apply_chat_template(context_msgs, tokenize=False, add_generation_prompt=True)
                        inp = tokenizer(prompt_text, return_tensors="pt", truncation=True, max_length=cfg.training.max_seq_length)
                        ids = inp.input_ids.to(model.device)
                        mask = torch.ones_like(ids)
                        with torch.no_grad():
                            out = model.generate(ids, attention_mask=mask, max_new_tokens=cfg.generation.max_new_tokens,
                                                 temperature=cfg.generation.temperature, top_p=cfg.generation.top_p,
                                                 do_sample=cfg.generation.do_sample, pad_token_id=tokenizer.pad_token_id)
                        response = tokenizer.decode(out[0][ids.shape[1]:], skip_special_tokens=True)
                        synthetic.append({"messages": list(context_msgs) + [{"role": "assistant", "content": response}]})
                    except Exception as e2:
                        logger.warning(f"Sample generation failed: {e2}, skipping")

            if (batch_start + batch_size) % 100 < batch_size or batch_start + batch_size >= n_total:
                logger.info(f"Step 2: generated {len(synthetic)}/{n_total} samples")

        return synthetic

    def _get_base_model(self):
        """Lazy-load the base model for quality scoring."""
        if self._base_model is None:
            logger.info("Loading base model for quality scoring...")
            self._base_tokenizer = AutoTokenizer.from_pretrained(
                self.config.model_name, trust_remote_code=True
            )
            if self._base_tokenizer.pad_token is None:
                self._base_tokenizer.pad_token = self._base_tokenizer.eos_token
            self._base_model = AutoModelForCausalLM.from_pretrained(
                self.config.model_name,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                trust_remote_code=True,
            )
            self._base_model.eval()
        return self._base_model, self._base_tokenizer

    def _compute_metrics(
        self,
        model,
        tokenizer,
        filtered_texts: list[str],
        eval_texts: list[str],
        generation: int,
    ) -> dict:
        metrics = {}

        metrics["self_bleu"] = corpus_self_bleu(filtered_texts)
        if self._reference_vocab:
            metrics["vocab_coverage"] = vocab_coverage(filtered_texts, self._reference_vocab)

        embeddings = self.scorer.embed_texts(filtered_texts)
        metrics["embedding_diversity"] = embedding_diversity(embeddings)

        if eval_texts:
            metrics["held_out_ppl"] = held_out_perplexity(model, tokenizer, eval_texts[:200])

        return metrics


def main():
    parser = argparse.ArgumentParser(description="PGPF Recursive Training Loop")
    parser.add_argument("--model_name", type=str, default=None)
    parser.add_argument("--num_generations", type=int, default=None)
    parser.add_argument("--filter_method", type=str, default=None, choices=[
        "no_filter", "random", "confidence", "pgpf_static", "lexical_only",
    ])
    parser.add_argument("--retention_rate", type=float, default=None)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--data_dir", type=str, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--real_data_mix_ratio", type=float, default=None)
    args = parser.parse_args()

    config = PGPFConfig()
    for field_name in [
        "model_name", "num_generations", "filter_method", "retention_rate",
        "output_dir", "data_dir", "seed", "real_data_mix_ratio",
    ]:
        val = getattr(args, field_name, None)
        if val is not None:
            setattr(config, field_name, val)

    loop = RecursiveTrainingLoop(config)
    loop.run()


if __name__ == "__main__":
    main()
