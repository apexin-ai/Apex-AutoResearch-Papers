import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

DATA = "exp_012_rerun_1024/samples_with_logprobs.jsonl"
OUT_PDF = "figures/fig_length_logprob_scatter.pdf"
OUT_PNG = "figures/fig_length_logprob_scatter.png"


def entity_f1(pred_ents, gold_ents):
    pred_set = {(e['text'], e['type'], e['start'], e['end']) for e in pred_ents}
    gold_set = {(e['text'], e['type'], e['start'], e['end']) for e in gold_ents}
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set) if pred_set else 0
    r = tp / len(gold_set) if gold_set else 0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def relation_f1(pred_rels, gold_rels):
    pred_set = {(r['head'], r['tail'], r['type']) for r in pred_rels}
    gold_set = {(r['head'], r['tail'], r['type']) for r in gold_rels}
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set) if pred_set else 0
    r = tp / len(gold_set) if gold_set else 0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


ner_tokens, ner_logprobs, ner_f1s = [], [], []
re_tokens, re_logprobs, re_f1s = [], [], []

with open(DATA) as f:
    for line in f:
        d = json.loads(line)
        gold = d['gold']
        gold_ents = gold.get('entities', [])
        gold_rels = gold.get('relations', [])

        for s in d['samples']:
            nt = s['n_tokens']
            mlp = s['mean_logprob']

            if gold_ents:
                ef1 = entity_f1(s.get('entities', []), gold_ents)
                ner_tokens.append(nt)
                ner_logprobs.append(mlp)
                ner_f1s.append(ef1)

            if gold_rels:
                rf1 = relation_f1(s.get('relations', []), gold_rels)
                re_tokens.append(nt)
                re_logprobs.append(mlp)
                re_f1s.append(rf1)

ner_tokens = np.array(ner_tokens)
ner_logprobs = np.array(ner_logprobs)
ner_f1s = np.array(ner_f1s)
re_tokens = np.array(re_tokens)
re_logprobs = np.array(re_logprobs)
re_f1s = np.array(re_f1s)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})


def f1_category(f1_arr):
    cat = np.empty(len(f1_arr), dtype=int)
    cat[f1_arr == 0] = 0
    cat[(f1_arr > 0) & (f1_arr < 0.5)] = 1
    cat[f1_arr >= 0.5] = 2
    return cat


def plot_panel(ax, tokens, logprobs, f1s, title):
    cats = f1_category(f1s)

    styles = {
        0: dict(color='#BBBBBB', marker='x', label='F1 = 0', s=10, alpha=0.35, linewidths=0.4),
        1: dict(color='#E8890C', marker='^', label='0 < F1 < 0.5', s=12, alpha=0.5, linewidths=0.3),
        2: dict(color='#2171B5', marker='o', label='F1 ≥ 0.5', s=12, alpha=0.5, linewidths=0.3, edgecolors='#2171B5'),
    }

    for cat_id in [0, 1, 2]:
        mask = cats == cat_id
        if mask.sum() == 0:
            continue
        kw = styles[cat_id].copy()
        lab = kw.pop('label')
        ax.scatter(tokens[mask], logprobs[mask], label=f'{lab} (n={mask.sum()})', zorder=2 + cat_id, **kw)

    rho, p_rho = stats.spearmanr(tokens, logprobs)
    r, p_r = stats.pearsonr(tokens, logprobs)

    p_str = f'{p_rho:.1e}' if p_rho < 0.001 else f'{p_rho:.3f}'
    ax.text(0.97, 0.03,
            f'Spearman ρ = {rho:.3f} (p = {p_str})\nPearson r = {r:.3f}',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=8, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#cccccc', alpha=0.95))

    if abs(rho) > 0.1:
        slope, intercept, _, _, _ = stats.linregress(tokens, logprobs)
        x_range = np.linspace(tokens.min(), tokens.max(), 100)
        ax.plot(x_range, slope * x_range + intercept, color='#d62728', linewidth=1.0,
                linestyle='--', alpha=0.7, zorder=5, label='OLS fit')

    ax.set_xlabel('Output token count')
    ax.set_ylabel('Mean log-probability')
    ax.set_title(title)
    ax.legend(loc='upper left', framealpha=0.9, edgecolor='#cccccc', borderpad=0.4, handletextpad=0.4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return rho, p_rho


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3))

rho_ner, p_ner = plot_panel(ax1, ner_tokens, ner_logprobs, ner_f1s, 'NER')
rho_re, p_re = plot_panel(ax2, re_tokens, re_logprobs, re_f1s, 'RE')

plt.tight_layout(w_pad=2.0)
fig.savefig(OUT_PDF)
fig.savefig(OUT_PNG)
plt.close()

print(f"NER: n={len(ner_tokens)}, Spearman ρ={rho_ner:.4f} (p={p_ner:.2e})")
print(f"RE:  n={len(re_tokens)}, Spearman ρ={rho_re:.4f} (p={p_re:.2e})")
print(f"Saved: {OUT_PDF}, {OUT_PNG}")
