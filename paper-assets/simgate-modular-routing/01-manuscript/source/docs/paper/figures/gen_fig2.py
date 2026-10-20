"""Generate Figure 2: Dose-response curves for Retry and Reflexion interventions.

Data: per_task_dose_response_data.json (10 death-prone tasks, N=1..5).
72B horizontal line updated to 30.6% (78/255, 11-task aggregate from backbone-scaling-70b).
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

# Per-task death rates (%) — 10 death-prone tasks
RETRY = {
    "chemistry-mix":      [55, 55, 50, 50, 50],
    "find-animal":        [50, 55, 50, 50, 55],
    "freeze":             [55, 55, 55, 50, 50],
    "grow-fruit":         [45, 50, 45, 40, 50],
    "id-life-stages-1":   [35, 30, 25, 30, 25],
    "id-life-stages-2":   [25, 25, 25, 25, 25],
    "inclined-plane":     [55, 55, 45, 45, 45],
    "lifespan-long":      [50, 45, 45, 40, 45],
    "lifespan-l-then-s":  [55, 45, 45, 45, 35],
    "meas-melt-point":    [55, 55, 50, 55, 55],
}
REFLEXION = {
    "chemistry-mix":      [55, 45, 25, 35, 20],
    "find-animal":        [50, 40, 45, 30, 45],
    "freeze":             [55, 50, 50, 50, 60],
    "grow-fruit":         [50, 35, 30, 25, 25],
    "id-life-stages-1":   [35, 30, 35, 35, 35],
    "id-life-stages-2":   [25, 25, 25, 25, 30],
    "inclined-plane":     [50, 40, 20, 30, 35],
    "lifespan-long":      [50, 40, 45, 40, 40],
    "lifespan-l-then-s":  [55, 45, 30, 45, 35],
    "meas-melt-point":    [50, 50, 35, 50, 25],
}

NS = [1, 2, 3, 4, 5]

def compute_stats(data_dict):
    means, ci_lo, ci_hi = [], [], []
    for i in range(5):
        vals = np.array([v[i] for v in data_dict.values()])
        m = vals.mean()
        se = vals.std(ddof=1) / np.sqrt(len(vals))
        t_crit = 2.262  # t(0.025, df=9)
        means.append(m)
        ci_lo.append(m - t_crit * se)
        ci_hi.append(m + t_crit * se)
    return means, ci_lo, ci_hi

retry_m, retry_lo, retry_hi = compute_stats(RETRY)
reflex_m, reflex_lo, reflex_hi = compute_stats(REFLEXION)

fig, ax = plt.subplots(figsize=(3.4, 2.5))

ax.fill_between(NS, retry_lo, retry_hi, color=paper_style.C_INTERNAL,
                alpha=paper_style.CI_ALPHA, zorder=1, edgecolor='none')
ax.plot(NS, retry_m, color=paper_style.C_INTERNAL, marker='o', markersize=5,
        markeredgecolor='white', markeredgewidth=paper_style.MARKER_EDGE_WIDTH,
        alpha=0.92, label='Retry', zorder=3,
        path_effects=paper_style.marker_shadow())

ax.fill_between(NS, reflex_lo, reflex_hi, color=paper_style.C_DETERMINISTIC,
                alpha=paper_style.CI_ALPHA, zorder=1, edgecolor='none')
ax.plot(NS, reflex_m, color=paper_style.C_DETERMINISTIC, marker='s', markersize=5,
        markeredgecolor='white', markeredgewidth=paper_style.MARKER_EDGE_WIDTH,
        alpha=0.92, label='Reflexion', zorder=3,
        path_effects=paper_style.marker_shadow())

ax.axhline(y=30.6, color=paper_style.C_REGRESSION,
           linestyle=(0, (5, 2, 1, 2)), linewidth=0.9, alpha=0.6, zorder=2)
ax.text(0.98, 30.6, '72B (30.6%)', va='bottom', ha='right', fontsize=6.5,
        color=paper_style.C_REGRESSION, transform=ax.get_yaxis_transform())

ax.axhline(y=16.3, color=paper_style.C_NEUTRAL,
           linestyle=(0, (2, 2)), linewidth=0.8, alpha=0.6, zorder=2)
ax.text(0.98, 16.3, 'Deterministic (16.3%)', va='bottom', ha='right', fontsize=6.5,
        color=paper_style.C_NEUTRAL, transform=ax.get_yaxis_transform())

ax.set_xlabel('Number of Trials (N)')
ax.set_ylabel('Death Rate (%)')
ax.set_xlim(0.7, 5.3)
ax.set_ylim(10, 60)
ax.xaxis.set_major_locator(ticker.FixedLocator([1, 2, 3, 4, 5]))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

paper_style.add_y_grid(ax)

leg = ax.legend(loc='upper right', frameon=True)
paper_style.style_legend(leg)

fig.tight_layout(pad=0.4)
out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ('pdf', 'png'):
    path = os.path.join(out_dir, f'dose_response.{ext}')
    fig.savefig(path, format=ext if ext == 'png' else None,
                dpi=300, bbox_inches='tight', pad_inches=0.08)
plt.close()
print(f"Saved: {os.path.join(out_dir, 'dose_response.pdf')} ({os.path.getsize(os.path.join(out_dir, 'dose_response.pdf'))} bytes)")
