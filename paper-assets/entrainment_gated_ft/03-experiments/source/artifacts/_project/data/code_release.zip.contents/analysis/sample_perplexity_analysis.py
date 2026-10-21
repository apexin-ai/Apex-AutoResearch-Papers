import json, os, csv, numpy as np, torch
from scipy import stats
from transformers import AutoTokenizer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fla.models.gated_deltanet import GatedDeltaNetForCausalLM
from fla.models.retnet import RetNetForCausalLM
from fla.models.hgrn2 import HGRN2ForCausalLM

# Fix HGRN2 _tied_weights_keys: list -> dict
HGRN2ForCausalLM._tied_weights_keys = {"lm_head.weight": "model.embeddings.weight"}

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'
MODEL_DIR = '/root/autodl-tmp/models_1.3b'
DEVICE = 'cuda:0'

ARCHS = {
    'GDN': {
        'pure_json': '1.3B-100B-GatedDeltaNet-pure.json',
        'h31_json': '1.3B-100B-GatedDeltaNet-hybrid-3-1.json',
        'h31_jsonl': '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl',
        'pure_model': '1.3B-100B-GatedDeltaNet-pure',
        'model_cls': GatedDeltaNetForCausalLM,
    },
    'RetNet': {
        'pure_json': '1.3B-100B-RetNet-pure.json',
        'h31_json': '1.3B-100B-RetNet-hybrid-3-1.json',
        'pure_model': '1.3B-100B-RetNet-pure',
        'model_cls': RetNetForCausalLM,
    },
    'HGRN2': {
        'pure_json': '1.3B-100B-HGRN2-pure.json',
        'h31_json': '1.3B-100B-HGRN2-hybrid-3-1.json',
        'pure_model': '1.3B-100B-HGRN2-pure',
        'model_cls': HGRN2ForCausalLM,
    },
}

TASK = 'lambada_openai'

def load_json_samples(json_path):
    with open(json_path) as f:
        d = json.load(f)
    return sorted(d['samples'][TASK], key=lambda x: x['doc_id'])

def load_jsonl_samples(jsonl_path):
    samples = []
    with open(jsonl_path) as f:
        for line in f:
            samples.append(json.loads(line))
    return sorted(samples, key=lambda x: x['doc_id'])

print("Loading lm_eval per-sample data...")
eval_data = {}
for arch, cfg in ARCHS.items():
    pure_samples = load_json_samples(os.path.join(DATA_DIR, cfg['pure_json']))
    if 'h31_jsonl' in cfg and os.path.exists(os.path.join(DATA_DIR, cfg['h31_jsonl'])):
        h31_samples = load_jsonl_samples(os.path.join(DATA_DIR, cfg['h31_jsonl']))
    else:
        h31_samples = load_json_samples(os.path.join(DATA_DIR, cfg['h31_json']))
    assert len(pure_samples) == len(h31_samples)
    pure_acc = np.array([s['acc'] for s in pure_samples])
    h31_acc = np.array([s['acc'] for s in h31_samples])
    helped = (pure_acc == 0) & (h31_acc == 1)
    hurt = (pure_acc == 1) & (h31_acc == 0)
    eval_data[arch] = {
        'pure_samples': pure_samples, 'pure_acc': pure_acc, 'h31_acc': h31_acc,
        'helped_mask': helped, 'hurt_mask': hurt,
    }
    print(f"  {arch}: {len(pure_samples)} samples, helped={helped.sum()}, hurt={hurt.sum()}")

texts = [s['doc']['text'] for s in eval_data['GDN']['pure_samples']]
doc_ids = [s['doc_id'] for s in eval_data['GDN']['pure_samples']]
n_samples = len(texts)
print(f"Total LAMBADA samples: {n_samples}")

def compute_perplexity(model_cls, model_path, texts, batch_size=4):
    print(f"  Loading model: {model_path}", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = model_cls.from_pretrained(model_path, torch_dtype=torch.float16).to(DEVICE)
    model.eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    losses = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        encodings = tokenizer(batch_texts, return_tensors='pt', padding=True, truncation=True, max_length=512)
        input_ids = encodings['input_ids'].to(DEVICE)
        attention_mask = encodings['attention_mask'].to(DEVICE)
        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = input_ids[:, 1:].contiguous()
        shift_mask = attention_mask[:, 1:].contiguous()
        loss_fct = torch.nn.CrossEntropyLoss(reduction='none')
        token_losses = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1)).view(shift_labels.shape)
        masked_losses = token_losses * shift_mask.float()
        sample_lengths = shift_mask.sum(dim=1).float()
        sample_losses = (masked_losses.sum(dim=1) / sample_lengths.clamp(min=1)).cpu().numpy()
        losses.extend(sample_losses.tolist())
        if (i // batch_size) % 200 == 0:
            print(f"    Batch {i//batch_size}/{(len(texts)-1)//batch_size + 1}, GPU mem: {torch.cuda.max_memory_allocated()/1024**3:.1f}GB", flush=True)
    del model
    torch.cuda.empty_cache()
    return np.array(losses)

# Hardcode GDN and RetNet results from previous run
print("\nLoading cached GDN/RetNet results, computing HGRN2...")
perplexities = {}

# Recompute all 3 to be safe (GDN and RetNet are fast ~2min each)
for arch, cfg in ARCHS.items():
    model_path = os.path.join(MODEL_DIR, cfg['pure_model'])
    print(f"\n=== {arch} ===", flush=True)
    perplexities[arch] = compute_perplexity(cfg['model_cls'], model_path, texts, batch_size=4)
    print(f"  {arch}: mean_loss={perplexities[arch].mean():.4f}, std={perplexities[arch].std():.4f}", flush=True)

# Save CSV
csv_path = os.path.join(OUT_DIR, 'sample_perplexity_results.csv')
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    header = ['doc_id']
    for arch in ARCHS:
        header.extend([f'{arch}_pure_loss', f'{arch}_helped', f'{arch}_hurt'])
    w.writerow(header)
    for i in range(n_samples):
        row = [doc_ids[i]]
        for arch in ARCHS:
            row.append(f"{perplexities[arch][i]:.6f}")
            row.append(int(eval_data[arch]['helped_mask'][i]))
            row.append(int(eval_data[arch]['hurt_mask'][i]))
        w.writerow(row)
print(f"\nCSV saved: {csv_path}", flush=True)

# Statistical tests
print("\n" + "=" * 70)
print("STATISTICAL ANALYSIS: Pure-model loss ~ helped/hurt")
print("=" * 70)

results = {}
for arch in ARCHS:
    ppl = perplexities[arch]
    helped = eval_data[arch]['helped_mask']
    hurt = eval_data[arch]['hurt_mask']
    ppl_helped = ppl[helped]
    ppl_hurt = ppl[hurt]
    u_stat, p_val = stats.mannwhitneyu(ppl_helped, ppl_hurt, alternative='two-sided')
    n1, n2 = len(ppl_helped), len(ppl_hurt)
    r_rb = 1 - (2 * u_stat) / (n1 * n2)
    results[arch] = {
        'n_helped': n1, 'n_hurt': n2,
        'helped_mean': float(ppl_helped.mean()), 'helped_median': float(np.median(ppl_helped)),
        'hurt_mean': float(ppl_hurt.mean()), 'hurt_median': float(np.median(ppl_hurt)),
        'helped_std': float(ppl_helped.std()), 'hurt_std': float(ppl_hurt.std()),
        'U': float(u_stat), 'p': float(p_val), 'r_rb': float(r_rb),
    }
    print(f"\n  {arch}:")
    print(f"    Helped (n={n1}): mean={ppl_helped.mean():.4f}, median={np.median(ppl_helped):.4f}, std={ppl_helped.std():.4f}")
    print(f"    Hurt   (n={n2}): mean={ppl_hurt.mean():.4f}, median={np.median(ppl_hurt):.4f}, std={ppl_hurt.std():.4f}")
    print(f"    Mann-Whitney U={u_stat:.1f}, p={p_val:.6f}, rank-biserial r={r_rb:.4f}")
    if p_val < 0.05:
        direction = "helped > hurt" if ppl_helped.mean() > ppl_hurt.mean() else "helped < hurt"
        print(f"    ** Significant (p<0.05): {direction}")
    else:
        print(f"    Not significant (p>0.05)")

# Cross-architecture comparison
print("\n" + "=" * 70)
print("CROSS-ARCHITECTURE COMPARISON")
print("=" * 70)

arch_names = list(ARCHS.keys())
print("\n  Kruskal-Wallis on helped-sample perplexities:")
helped_ppls = []
for arch in arch_names:
    ppl_h = perplexities[arch][eval_data[arch]['helped_mask']]
    helped_ppls.append(ppl_h)
    print(f"  {arch} helped: n={len(ppl_h)}, mean={ppl_h.mean():.4f}, median={np.median(ppl_h):.4f}")

kw_stat, kw_p = stats.kruskal(*helped_ppls)
print(f"\n  Kruskal-Wallis H={kw_stat:.2f}, p={kw_p:.6f}")

pairwise_results = {}
print("\n  Pairwise Mann-Whitney (helped samples):")
for i in range(len(arch_names)):
    for j in range(i+1, len(arch_names)):
        u, p = stats.mannwhitneyu(helped_ppls[i], helped_ppls[j], alternative='two-sided')
        n1, n2 = len(helped_ppls[i]), len(helped_ppls[j])
        r = 1 - (2 * u) / (n1 * n2)
        key = f"{arch_names[i]}_vs_{arch_names[j]}"
        pairwise_results[key] = {'U': float(u), 'p': float(p), 'r': float(r)}
        print(f"    {arch_names[i]} vs {arch_names[j]}: U={u:.1f}, p={p:.6f}, r={r:.4f}")

print("\n  Kruskal-Wallis on hurt-sample perplexities:")
hurt_ppls = []
for arch in arch_names:
    ppl_r = perplexities[arch][eval_data[arch]['hurt_mask']]
    hurt_ppls.append(ppl_r)
    print(f"  {arch} hurt: n={len(ppl_r)}, mean={ppl_r.mean():.4f}, median={np.median(ppl_r):.4f}")

kw_hurt_stat, kw_hurt_p = stats.kruskal(*hurt_ppls)
print(f"\n  Kruskal-Wallis H={kw_hurt_stat:.2f}, p={kw_hurt_p:.6f}")

# Violin plot
print("\nGenerating violin plot...", flush=True)
fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=True)
colors_helped = '#4C72B0'
colors_hurt = '#DD8452'

for idx, arch in enumerate(ARCHS):
    ax = axes[idx]
    ppl = perplexities[arch]
    helped = eval_data[arch]['helped_mask']
    hurt = eval_data[arch]['hurt_mask']
    ppl_h = ppl[helped]
    ppl_r = ppl[hurt]

    parts = ax.violinplot([ppl_h, ppl_r], positions=[0, 1], showmeans=True, showmedians=True, widths=0.7)
    parts['bodies'][0].set_facecolor(colors_helped)
    parts['bodies'][1].set_facecolor(colors_hurt)
    for body in parts['bodies']:
        body.set_alpha(0.7)
        body.set_edgecolor('black')
        body.set_linewidth(0.5)
    parts['cmeans'].set_color('black')
    parts['cmeans'].set_linewidth(1.5)
    parts['cmedians'].set_color('red')
    parts['cmedians'].set_linewidth(1.5)

    r = results[arch]
    sig_marker = '***' if r['p'] < 0.001 else '**' if r['p'] < 0.01 else '*' if r['p'] < 0.05 else 'ns'

    ax.set_xticks([0, 1])
    ax.set_xticklabels([f"Helped\n(n={int(helped.sum())})", f"Hurt\n(n={int(hurt.sum())})"], fontsize=10)
    ax.set_title(f"{arch}\np={r['p']:.4f} ({sig_marker}), r={r['r_rb']:.3f}", fontsize=11)
    if idx == 0:
        ax.set_ylabel("Pure-model loss (cross-entropy)", fontsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.text(0, ppl_h.mean() + 0.05, f"μ={ppl_h.mean():.2f}", ha='center', va='bottom', fontsize=8, color='black')
    ax.text(1, ppl_r.mean() + 0.05, f"μ={ppl_r.mean():.2f}", ha='center', va='bottom', fontsize=8, color='black')

fig.suptitle("Per-sample Pure-Model Loss: Helped vs Hurt by Attention (h3-1)", fontsize=13, y=1.02)
fig.text(0.5, -0.03, "Helped = pure wrong, h3-1 right | Hurt = pure right, h3-1 wrong | Black line = mean, Red line = median",
         ha='center', fontsize=9, style='italic', color='#555555')
plt.tight_layout()

for ext in ['png', 'pdf']:
    path = os.path.join(OUT_DIR, f'sample_perplexity_figure.{ext}')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {path}")
plt.close()

# Summary JSON
summary = {
    'phase2_perplexity': {
        'per_arch': results,
        'cross_arch_helped': {
            'kruskal_wallis_H': float(kw_stat),
            'kruskal_wallis_p': float(kw_p),
            'pairwise': pairwise_results,
        },
        'cross_arch_hurt': {
            'kruskal_wallis_H': float(kw_hurt_stat),
            'kruskal_wallis_p': float(kw_hurt_p),
        },
    }
}

with open(os.path.join(OUT_DIR, 'sample_perplexity_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)
print(f"\nSummary JSON saved.", flush=True)

# Final Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
for arch in ARCHS:
    r = results[arch]
    sig = "***" if r['p'] < 0.001 else "**" if r['p'] < 0.01 else "*" if r['p'] < 0.05 else "ns"
    print(f"  {arch}: U={r['U']:.0f}, p={r['p']:.6f} {sig}, r_rb={r['r_rb']:.4f}")
    print(f"         helped_mean={r['helped_mean']:.4f}, hurt_mean={r['hurt_mean']:.4f}")
print(f"\n  Cross-arch helped Kruskal-Wallis: H={kw_stat:.2f}, p={kw_p:.6f}")
print(f"  Cross-arch hurt Kruskal-Wallis: H={kw_hurt_stat:.2f}, p={kw_hurt_p:.6f}")
print("\nDone.")
