# RGDS MVP main loop: iterative generate → monitor → select → train → evaluate.
# Usage: python run_mvp.py --method rgds --num_generations 4 --gpu_ids 0,1

import argparse
import json
import os
import shutil
import time
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from representation_monitor import (
    compute_rankme,
    compute_knn_probe,
    compute_diversity_scores,
    failsafe_check,
    load_contriever,
    extract_hidden_states,
)
from diversity_selection import select_data
from evaluate import (
    compute_held_out_perplexity,
    compute_rare_ngram_survival,
    compute_rank_correlation,
)


def parse_args():
    p = argparse.ArgumentParser(description="RGDS MVP iterative training loop")
    p.add_argument("--method", type=str, required=True,
                   choices=["rgds", "external_only", "uncurated"],
                   help="Selection method: rgds (ours), external_only (always Contriever), uncurated (no selection)")
    p.add_argument("--num_generations", type=int, default=4)
    p.add_argument("--data_dir", type=str, default="./data")
    p.add_argument("--output_dir", type=str, default="./results")
    p.add_argument("--student_model", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--generator_model", type=str, default="Qwen/Qwen3-4B")
    p.add_argument("--gen_tokens", type=int, default=500_000,
                   help="Tokens to generate per iteration")
    p.add_argument("--selection_budget_ratio", type=float, default=0.5,
                   help="Fraction of generated data to select")
    p.add_argument("--pca_dim", type=int, default=32)
    p.add_argument("--gpu_ids", type=str, default="0,1",
                   help="Comma-separated GPU ids (first=generator, second=student)")
    p.add_argument("--seed", type=int, default=42)
    # training hyperparams
    p.add_argument("--train_lr", type=float, default=2e-5)
    p.add_argument("--train_epochs", type=int, default=1)
    p.add_argument("--train_batch_size", type=int, default=4)
    p.add_argument("--train_grad_accum", type=int, default=8)
    p.add_argument("--seq_len", type=int, default=512)
    # generation hyperparams
    p.add_argument("--gen_batch_size", type=int, default=8)
    p.add_argument("--gen_temperature", type=float, default=0.8)
    p.add_argument("--gen_top_p", type=float, default=0.95)
    p.add_argument("--gen_max_new_tokens", type=int, default=512)
    # failsafe thresholds
    p.add_argument("--tau_rank", type=float, default=0.5)
    p.add_argument("--tau_knn", type=float, default=0.6)
    return p.parse_args()


def run_generation(generator_model, tokenizer, train_chunks, gen_dir, args, device):
    """Generate synthetic data for one iteration."""
    from generate import build_prompts, generate_batch

    num_prompts = (args.gen_tokens // args.gen_max_new_tokens) + 1
    prompts = build_prompts(train_chunks, tokenizer, num_prompts)

    all_generated = []
    total_tokens = 0
    for i in range(0, len(prompts), args.gen_batch_size):
        batch_prompts = prompts[i:i + args.gen_batch_size]
        generated = generate_batch(
            generator_model, tokenizer, batch_prompts,
            args.gen_max_new_tokens, args.gen_temperature, args.gen_top_p, device
        )
        for seq in generated:
            seq = seq[seq != tokenizer.pad_token_id].tolist()
            if len(seq) > 0:
                all_generated.append(seq)
                total_tokens += len(seq)
        if total_tokens >= args.gen_tokens:
            break

    synth_path = gen_dir / "synthetic.pt"
    torch.save(all_generated, synth_path)
    return all_generated


def run_selection(student_model, tokenizer, candidates, ref_chunks, ref_embeddings,
                  device, args, gen, contriever_model, rankme_gen0):
    """Select data according to the chosen method."""
    if args.method == "uncurated":
        return list(range(len(candidates)))

    if args.method == "external_only":
        selection_method = "contriever"
    elif args.method == "rgds":
        # monitor and decide
        rankme = compute_rankme(student_model, ref_chunks, device)
        knn_acc = compute_knn_probe(
            student_model, ref_chunks,
            torch.load(Path(args.data_dir) / "ref_rare_labels.pt", weights_only=True),
            device
        )
        should_fallback, reason = failsafe_check(
            rankme, rankme_gen0, knn_acc,
            tau_rank=args.tau_rank, tau_knn=args.tau_knn
        )
        if should_fallback:
            print(f"  FAILSAFE TRIGGERED (gen {gen}): {reason} → switching to Contriever")
            selection_method = "contriever"
        else:
            print(f"  Representations healthy (RankMe={rankme:.1f}, kNN={knn_acc:.3f}) → using internal")
            selection_method = "internal"
    else:
        raise ValueError(f"Unknown method: {args.method}")

    budget = int(len(candidates) * args.selection_budget_ratio)
    selected = select_data(
        student_model, tokenizer, candidates, ref_chunks, ref_embeddings,
        device, method=selection_method, contriever_model=contriever_model,
        pca_dim=args.pca_dim, budget=budget
    )
    return selected


def run_training(student_model, tokenizer, selected_data, checkpoint_dir, device, args):
    """Fine-tune student model on selected data for one generation."""
    from train_student import TokenDataset, train_one_epoch
    from torch.utils.data import DataLoader
    from transformers import get_cosine_schedule_with_warmup
    import math

    dataset = TokenDataset(selected_data, args.seq_len)
    dataloader = DataLoader(dataset, batch_size=args.train_batch_size, shuffle=True,
                            num_workers=2, pin_memory=True)

    optimizer = torch.optim.AdamW(
        student_model.parameters(), lr=args.train_lr, weight_decay=0.01
    )
    total_steps = math.ceil(len(dataloader) / args.train_grad_accum) * args.train_epochs
    warmup_steps = int(total_steps * 0.05)
    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    for epoch in range(args.train_epochs):
        avg_loss = train_one_epoch(student_model, dataloader, optimizer, scheduler, device, args)

    student_model.save_pretrained(checkpoint_dir)
    tokenizer.save_pretrained(checkpoint_dir)
    return avg_loss


def run_evaluation(student_model, tokenizer, ref_chunks, rare_labels, test_chunks,
                   synthetic_data, device, contriever_model, batch_size=32):
    """Compute all evaluation metrics."""
    metrics = {}

    metrics["held_out_perplexity"] = compute_held_out_perplexity(
        student_model, test_chunks, device, batch_size
    )
    metrics["rankme"] = compute_rankme(student_model, ref_chunks, device, batch_size)
    metrics["knn_probe_accuracy"] = compute_knn_probe(
        student_model, ref_chunks, rare_labels, device, batch_size=batch_size
    )

    ref_texts = [tokenizer.decode(c, skip_special_tokens=True) for c in ref_chunks[:1000]]
    synth_texts = [tokenizer.decode(ids, skip_special_tokens=True) for ids in synthetic_data[:1000]]
    metrics["rare_ngram_survival"] = compute_rare_ngram_survival(ref_texts, synth_texts)

    subset = ref_chunks[:500]
    corr, pval = compute_rank_correlation(
        student_model, tokenizer, subset, device, contriever_model, batch_size
    )
    metrics["rank_correlation"] = corr
    metrics["rank_correlation_pvalue"] = pval

    return metrics


def main():
    args = parse_args()
    torch.manual_seed(args.seed)

    gpu_list = [int(g) for g in args.gpu_ids.split(",")]
    gen_device = f"cuda:{gpu_list[0]}"
    student_device = f"cuda:{gpu_list[-1]}"

    method_dir = Path(args.output_dir) / args.method
    method_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    ref_chunks = torch.load(Path(args.data_dir) / "ref_chunks.pt", weights_only=True)
    rare_labels = torch.load(Path(args.data_dir) / "ref_rare_labels.pt", weights_only=True)
    test_chunks = torch.load(Path(args.data_dir) / "test_chunks.pt", weights_only=True)
    train_chunks = torch.load(Path(args.data_dir) / "train_chunks.pt", weights_only=True)

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.student_model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    gen_tokenizer = AutoTokenizer.from_pretrained(args.generator_model, trust_remote_code=True)
    if gen_tokenizer.pad_token is None:
        gen_tokenizer.pad_token = gen_tokenizer.eos_token

    # Load Contriever (needed for external_only and rgds failsafe)
    contriever_model = None
    if args.method in ("rgds", "external_only"):
        print("Loading Contriever...")
        contriever_model = load_contriever(device="cpu")

    # Load student model
    print(f"Loading student model: {args.student_model}")
    student_model = AutoModelForCausalLM.from_pretrained(
        args.student_model, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(student_device)

    # Gen-0 baseline: compute RankMe before any training
    print("Computing gen-0 RankMe baseline...")
    rankme_gen0 = compute_rankme(student_model, ref_chunks, student_device)
    print(f"  Gen-0 RankMe: {rankme_gen0:.2f}")

    # Precompute reference embeddings for PCA (on base student)
    ref_embeddings = extract_hidden_states(student_model, ref_chunks, student_device)

    # Load generator
    print(f"Loading generator: {args.generator_model}")
    generator_model = AutoModelForCausalLM.from_pretrained(
        args.generator_model, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(gen_device).eval()

    all_results = {"method": args.method, "generations": [], "rankme_gen0": rankme_gen0}

    for gen in range(args.num_generations):
        gen_start = time.time()
        gen_dir = method_dir / f"gen_{gen}"
        gen_dir.mkdir(parents=True, exist_ok=True)
        ckpt_dir = gen_dir / "checkpoint"
        print(f"\n{'='*60}")
        print(f"Generation {gen}/{args.num_generations - 1} | Method: {args.method}")
        print(f"{'='*60}")

        # 1. Generate
        print("\n[1/5] Generating synthetic data...")
        synthetic = run_generation(
            generator_model, gen_tokenizer, train_chunks, gen_dir, args, gen_device
        )
        print(f"  Generated {len(synthetic)} sequences")

        # 2. Select
        print(f"\n[2/5] Selecting data (method={args.method})...")
        selected_indices = run_selection(
            student_model, tokenizer, synthetic, ref_chunks, ref_embeddings,
            student_device, args, gen, contriever_model, rankme_gen0
        )
        selected_data = [synthetic[i] for i in selected_indices]
        print(f"  Selected {len(selected_data)}/{len(synthetic)} sequences")

        # save selected data
        torch.save(selected_data, gen_dir / "selected.pt")
        torch.save(selected_indices, gen_dir / "selected_indices.pt")

        # 3. Train
        print(f"\n[3/5] Training student (lr={args.train_lr}, epochs={args.train_epochs})...")
        # create a namespace-like object for train_one_epoch compatibility
        train_args = argparse.Namespace(
            gradient_accumulation_steps=args.train_grad_accum,
            max_grad_norm=1.0,
        )
        avg_loss = run_training(student_model, tokenizer, selected_data, str(ckpt_dir),
                                student_device, train_args)
        print(f"  Final avg loss: {avg_loss:.4f}")

        # 4. Evaluate
        print("\n[4/5] Evaluating...")
        metrics = run_evaluation(
            student_model, tokenizer, ref_chunks, rare_labels, test_chunks,
            synthetic, student_device, contriever_model
        )
        gen_elapsed = time.time() - gen_start
        metrics["generation"] = gen
        metrics["num_synthetic"] = len(synthetic)
        metrics["num_selected"] = len(selected_data)
        metrics["train_loss"] = avg_loss
        metrics["elapsed_seconds"] = gen_elapsed

        # 5. Save metrics
        with open(gen_dir / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)

        all_results["generations"].append(metrics)

        print(f"\n[5/5] Gen {gen} summary:")
        print(f"  Perplexity:     {metrics['held_out_perplexity']:.2f}")
        print(f"  RankMe:         {metrics['rankme']:.2f}")
        print(f"  k-NN accuracy:  {metrics['knn_probe_accuracy']:.4f}")
        print(f"  Rare n-gram:    {metrics.get('rare_ngram_survival', 'N/A')}")
        print(f"  Rank corr:      {metrics['rank_correlation']:.4f}")
        print(f"  Time:           {gen_elapsed:.0f}s")

        # Update ref embeddings for next generation PCA (use current student)
        ref_embeddings = extract_hidden_states(student_model, ref_chunks, student_device)

    # Save overall results
    with open(method_dir / "all_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Print summary table
    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY — {args.method}")
    print(f"{'='*60}")
    print(f"{'Gen':>4} {'PPL':>8} {'RankMe':>8} {'kNN':>8} {'Rare':>8} {'Corr':>8}")
    for r in all_results["generations"]:
        print(f"{r['generation']:>4} {r['held_out_perplexity']:>8.2f} {r['rankme']:>8.2f} "
              f"{r['knn_probe_accuracy']:>8.4f} {r.get('rare_ngram_survival', 0):>8.4f} "
              f"{r['rank_correlation']:>8.4f}")


if __name__ == "__main__":
    main()
