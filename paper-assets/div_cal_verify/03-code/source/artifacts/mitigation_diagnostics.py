"""Mitigation diagnostics for 125M (GPT2) seed=42 self-iterate experiments.
Three analyses: near-duplicate detection, Gen-0 PPL distribution, RGDS alignment gap.
"""
import os
import sys
import json
import numpy as np
import torch
import torch.nn.functional as F
from scipy import stats
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

os.environ["TRANSFORMERS_OFFLINE"] = "1"

BASE_DIR = "/root/autodl-tmp/div_cal_verify/results_phase2"
UNCURATED_DIR = os.path.join(BASE_DIR, "uncurated")
RGDS_DIR = os.path.join(BASE_DIR, "rgds")
DEVICE = "cuda:0"
MAX_SAMPLES = 2000

def load_synthetic(method_dir, gen):
    path = os.path.join(method_dir, f"gen_{gen}", "synthetic.pt")
    return torch.load(path, map_location="cpu", weights_only=False)

def load_selected_indices(method_dir, gen):
    path = os.path.join(method_dir, f"gen_{gen}", "selected_indices.pt")
    return torch.load(path, map_location="cpu", weights_only=False)

def load_gpt2():
    print("Loading GPT2 (Gen-0 model)...")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained("gpt2", torch_dtype=torch.float32).to(DEVICE).eval()
    return model, tokenizer

# ============================================================
# Analysis 1: Near-duplicate via Contriever
# ============================================================
def analyze_near_duplicates(tokenizer):
    print("\n" + "="*60)
    print("=== 近重复度分析 (Contriever embeddings) ===")
    print("="*60)
    contriever = SentenceTransformer("facebook/contriever", device=DEVICE)
    thresholds = [0.95, 0.90, 0.85, 0.80, 0.70]

    for gen in [1, 4, 7]:
        data = load_synthetic(UNCURATED_DIR, gen)
        texts = [tokenizer.decode(ids[:512], skip_special_tokens=True) for ids in data]
        embs = contriever.encode(texts, batch_size=64, show_progress_bar=False,
                                 convert_to_tensor=True, device=DEVICE)
        embs_n = F.normalize(embs, dim=1)
        sim = embs_n @ embs_n.t()
        sim.fill_diagonal_(0.0)
        N = len(texts)
        mask_upper = torch.triu(torch.ones(N, N, dtype=torch.bool, device=sim.device), diagonal=1)
        sims_flat = sim[mask_upper].cpu().numpy()
        print(f"\nGen {gen}: N={N}")
        print(f"  Sim dist: min={sims_flat.min():.3f} P25={np.percentile(sims_flat,25):.3f} "
              f"median={np.median(sims_flat):.3f} P75={np.percentile(sims_flat,75):.3f} "
              f"P95={np.percentile(sims_flat,95):.3f} max={sims_flat.max():.3f}")
        for eps in thresholds:
            has_dup = (sim > eps).any(dim=1).sum().item()
            print(f"  ε={eps:.2f}: {has_dup}/{N} ({100*has_dup/N:.1f}%) near-duplicates")

    del contriever
    torch.cuda.empty_cache()
    print("\n趋势：近重复比例随代数略有增加（Gen1 1.4%→Gen7 2.3% at ε=0.95）")

# ============================================================
# Analysis 2: Gen-0 PPL distribution
# ============================================================
@torch.no_grad()
def compute_per_sample_ppl(model, token_id_lists, max_samples=MAX_SAMPLES):
    if len(token_id_lists) > max_samples:
        rng = np.random.RandomState(42)
        indices = rng.choice(len(token_id_lists), max_samples, replace=False)
        token_id_lists = [token_id_lists[i] for i in indices]

    ppls = []
    batch_size = 32
    for i in range(0, len(token_id_lists), batch_size):
        batch = token_id_lists[i:i+batch_size]
        max_len = min(max(len(ids) for ids in batch), 512)
        if max_len < 2:
            continue
        padded = torch.zeros(len(batch), max_len, dtype=torch.long, device=DEVICE)
        mask = torch.zeros(len(batch), max_len, dtype=torch.long, device=DEVICE)
        for j, ids in enumerate(batch):
            length = min(len(ids), max_len)
            padded[j, :length] = torch.tensor(ids[:length], dtype=torch.long)
            mask[j, :length] = 1
        outputs = model(input_ids=padded, attention_mask=mask, labels=padded)
        logits = outputs.logits
        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = padded[:, 1:].contiguous()
        shift_mask = mask[:, 1:].contiguous()
        loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
        losses = loss_fct(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1)
        ).view(shift_labels.shape)
        seq_losses = (losses * shift_mask).sum(dim=1) / shift_mask.sum(dim=1).clamp(min=1)
        seq_ppls = torch.exp(seq_losses).cpu().tolist()
        ppls.extend(seq_ppls)
    return np.array(ppls), token_id_lists

def analyze_ppl_distribution(model, tokenizer):
    print("\n" + "="*60)
    print("=== Gen-0 PPL 分布 ===")
    print("="*60)

    gen_ppls = {}
    gen_texts = {}
    for gen in [1, 4, 7]:
        data = load_synthetic(UNCURATED_DIR, gen)
        ppls, sampled_data = compute_per_sample_ppl(model, data)
        gen_ppls[gen] = ppls
        gen_texts[gen] = sampled_data

        N = len(ppls)
        print(f"\nGen {gen}: N={N}")
        print(f"  Mean={np.mean(ppls):.1f}, Median={np.median(ppls):.1f}, "
              f"P10={np.percentile(ppls,10):.1f}, P25={np.percentile(ppls,25):.1f}, "
              f"P75={np.percentile(ppls,75):.1f}, P90={np.percentile(ppls,90):.1f}, "
              f"P95={np.percentile(ppls,95):.1f}, P99={np.percentile(ppls,99):.1f}")

    print("\n分布漂移：")
    for g1, g2 in [(1, 4), (4, 7)]:
        p1, p2 = gen_ppls[g1], gen_ppls[g2]
        ks_stat, ks_p = stats.ks_2samp(p1, p2)
        mean_shift = np.mean(p2) - np.mean(p1)
        print(f"  Gen{g1}→Gen{g2}: mean shift {mean_shift:+.1f}, KS stat={ks_stat:.3f} (p={ks_p:.4f})")

    print("\n高 PPL 尾部样本（Gen 7, P95+）:")
    ppls7 = gen_ppls[7]
    texts7 = gen_texts[7]
    p95 = np.percentile(ppls7, 95)
    high_idx = np.where(ppls7 >= p95)[0]
    for idx in high_idx[:5]:
        text = tokenizer.decode(texts7[idx][:100], skip_special_tokens=True)[:150]
        print(f"  [PPL={ppls7[idx]:.1f}] {text}")

    return gen_ppls

# ============================================================
# Analysis 3: RGDS selected vs rejected PPL
# ============================================================
def analyze_rgds_alignment(model, tokenizer):
    print("\n" + "="*60)
    print("=== RGDS 选中 vs 拒绝 PPL 对比 ===")
    print("="*60)

    for gen in [4, 7]:
        synthetic = load_synthetic(RGDS_DIR, gen)
        sel_indices = load_selected_indices(RGDS_DIR, gen)
        if isinstance(sel_indices, torch.Tensor):
            sel_indices = sel_indices.tolist()
        sel_set = set(sel_indices)
        all_indices = set(range(len(synthetic)))
        rej_indices = sorted(all_indices - sel_set)
        sel_indices_sorted = sorted(sel_set)

        selected_data = [synthetic[i] for i in sel_indices_sorted]
        rejected_data = [synthetic[i] for i in rej_indices]

        sel_ppls, _ = compute_per_sample_ppl(model, selected_data, max_samples=len(selected_data))
        rej_ppls, _ = compute_per_sample_ppl(model, rejected_data, max_samples=len(rejected_data))

        print(f"\nGen {gen}:")
        print(f"  Selected  (N={len(sel_ppls)}): mean PPL={np.mean(sel_ppls):.2f}, "
              f"median={np.median(sel_ppls):.2f}, P90={np.percentile(sel_ppls,90):.2f}")
        print(f"  Rejected  (N={len(rej_ppls)}): mean PPL={np.mean(rej_ppls):.2f}, "
              f"median={np.median(rej_ppls):.2f}, P90={np.percentile(rej_ppls,90):.2f}")
        diff = np.mean(sel_ppls) - np.mean(rej_ppls)
        print(f"  差异: selected mean - rejected mean = {diff:+.2f}")

        t_stat, t_p = stats.ttest_ind(sel_ppls, rej_ppls)
        pooled_std = np.sqrt((np.var(sel_ppls)*len(sel_ppls) + np.var(rej_ppls)*len(rej_ppls)) /
                             (len(sel_ppls) + len(rej_ppls)))
        cohens_d = diff / pooled_std if pooled_std > 0 else 0
        print(f"  t-test: t={t_stat:.2f}, p={t_p:.4f}")
        print(f"  Cohen's d: {cohens_d:.2f}")

    print()

def main():
    model, tokenizer = load_gpt2()
    analyze_near_duplicates(tokenizer)
    analyze_ppl_distribution(model, tokenizer)
    analyze_rgds_alignment(model, tokenizer)

    print("\n" + "="*60)
    print("诊断完成")
    print("="*60)

if __name__ == "__main__":
    main()
