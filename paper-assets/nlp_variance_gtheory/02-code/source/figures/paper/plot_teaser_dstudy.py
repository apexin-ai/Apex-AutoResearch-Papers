#!/usr/bin/env python3
"""Generate teaser D-study figure for Introduction."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../../artifacts/exp004/data/intermediate_dstudy_table.json')
OUT_DIR = os.path.dirname(__file__)

with open(DATA_PATH) as f:
    data = json.load(f)

designs = {d['name']: d for d in data['designs']}

curves = [
    ('Single-condition (typical)', designs['Single-condition (typical)'], '#E69F00', 's', '--'),
    ('3 prompts × 3 seeds (recommended)', designs['Moderate'], '#009E73', '^', '-'),
    ('Full multi-facet (1,296 cond.)', designs['Full multi-facet'], '#0072B2', 'o', '-'),
]

fig, ax = plt.subplots(figsize=(5.5, 3.2))

for label, d, color, marker, ls in curves:
    proj = d['g_projections']
    ns = sorted([int(k) for k in proj.keys()])
    gs = [proj[str(n)] for n in ns]
    ax.plot(ns, gs, color=color, marker=marker, markersize=5, linewidth=1.8,
            linestyle=ls, label=label, zorder=3)

ax.axhline(y=0.80, color='#999999', linestyle=':', linewidth=1.0, zorder=1)
ax.text(1020, 0.805, '$G = 0.80$', fontsize=7.5, color='#666666', va='bottom')

offsets = {55: (0, 10), 178: (0, 10), 552: (0, 10)}
for d, n_g80, color in [
    (designs['Single-condition (typical)'], 552, '#E69F00'),
    (designs['Moderate'], 178, '#009E73'),
    (designs['Full multi-facet'], 55, '#0072B2'),
]:
    ax.plot(n_g80, 0.80, 'o', color=color, markersize=7, zorder=5,
            markeredgecolor='white', markeredgewidth=1.2)
    ox, oy = offsets[n_g80]
    ax.annotate(f'n={n_g80}', xy=(n_g80, 0.80),
                xytext=(ox, oy), textcoords='offset points',
                fontsize=7, ha='center', color=color, fontweight='bold')

ax.annotate('', xy=(70, 0.70), xytext=(530, 0.70),
            arrowprops=dict(arrowstyle='<->', color='#CC79A7', lw=1.5))
ax.text(180, 0.675, '10× fewer items', fontsize=7.5, ha='center',
        color='#CC79A7', fontweight='bold')

ax.set_xlabel('Number of items', fontsize=9)
ax.set_ylabel('Generalizability coefficient ($G$)', fontsize=9)
ax.set_xscale('log')
ax.set_xlim(20, 1200)
ax.set_ylim(0.05, 1.02)
ax.set_xticks([25, 50, 100, 200, 500, 1000])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(labelsize=8)

ax.legend(fontsize=7, loc='lower right', framealpha=0.9, edgecolor='#CCCCCC')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout(pad=0.4)
fig.savefig(os.path.join(OUT_DIR, 'fig0_teaser_dstudy.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(OUT_DIR, 'fig0_teaser_dstudy.png'), bbox_inches='tight', dpi=300)
print('Saved fig0_teaser_dstudy.pdf and .png')
