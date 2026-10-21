#!/usr/bin/env python3
"""Generate Model Vulnerability Radar Chart (fig_model_radar.pdf)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import pi
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

ATTACKS = ['score_manipulation', 'position_bias', 'verbosity_bias',
           'authority_bias', 'sycophancy', 'prompt_injection']
ATTACK_LABELS = ['Score\nManip.', 'Position\nBias', 'Verbosity\nBias',
                 'Authority\nBias', 'Sycophancy', 'Prompt\nInjection']

api_data = {
    "claude-opus-4-6": {"prompt_injection": 0.00935, "sycophancy": 0.01105, "score_manipulation": 0.0073, "verbosity_bias": 0.0122, "position_bias": 0.01275, "authority_bias": 0.0131},
    "gpt-5.5": {"prompt_injection": 0.0149, "sycophancy": 0.0164, "score_manipulation": 0.0149, "verbosity_bias": 0.0132, "position_bias": 0.0149, "authority_bias": 0.00945},
    "gemini-3.1-pro-preview": {"prompt_injection": 0.0545, "sycophancy": 0.03055, "score_manipulation": 0.05175, "verbosity_bias": 0.0396, "position_bias": 0.03595, "authority_bias": 0.03225},
    "gpt-4.1": {"prompt_injection": 0.0114, "sycophancy": 0.00515, "score_manipulation": 0.00945, "verbosity_bias": 0.0114, "position_bias": 0.0211, "authority_bias": 0.0154},
    "claude-sonnet-4-6": {"prompt_injection": 0.0206, "sycophancy": 0.01235, "score_manipulation": 0.0285, "verbosity_bias": 0.0141, "position_bias": 0.0179, "authority_bias": 0.02235},
    "gpt-4.1-nano": {"prompt_injection": 0.1707, "sycophancy": 0.09695, "score_manipulation": 0.1024, "verbosity_bias": 0.09575, "position_bias": 0.11615, "authority_bias": 0.04785},
    "gemini-3.5-flash": {"prompt_injection": 0.0795, "sycophancy": 0.05235, "score_manipulation": 0.0319, "verbosity_bias": 0.0399, "position_bias": 0.0441, "authority_bias": 0.0394},
    "gpt-4.1-mini": {"prompt_injection": 0.01595, "sycophancy": 0.01425, "score_manipulation": 0.01355, "verbosity_bias": 0.008, "position_bias": 0.06145, "authority_bias": 0.008},
    "claude-3-haiku": {"prompt_injection": 0.76795, "sycophancy": 0.22415, "score_manipulation": 0.2149, "verbosity_bias": 0.43675, "position_bias": 0.05225, "authority_bias": 0.2016},
}

local_data = {
    "qwen2.5-72b": {"prompt_injection": 0.06351, "sycophancy": 0.03815, "score_manipulation": 0.02163, "verbosity_bias": 0.04287, "position_bias": 0.39082, "authority_bias": 0.03477},
    "llama3.1-70b": {"prompt_injection": 0.28327, "sycophancy": 0.04921, "score_manipulation": 0.04921, "verbosity_bias": 0.11666, "position_bias": 0.45759, "authority_bias": 0.06418},
    "mistral-large": {"prompt_injection": 0.17667, "sycophancy": 0.07167, "score_manipulation": 0.09667, "verbosity_bias": 0.04167, "position_bias": 0.47667, "authority_bias": 0.06852},
    "qwen2.5-32b": {"prompt_injection": 0.09145, "sycophancy": 0.06425, "score_manipulation": 0.06038, "verbosity_bias": 0.06568, "position_bias": 0.40700, "authority_bias": 0.07347},
    "qwen2.5-14b": {"prompt_injection": 0.10077, "sycophancy": 0.07753, "score_manipulation": 0.06545, "verbosity_bias": 0.08846, "position_bias": 0.25871, "authority_bias": 0.09289},
    "llama3.1-8b": {"prompt_injection": 0.48167, "sycophancy": 0.22333, "score_manipulation": 0.22365, "verbosity_bias": 0.16333, "position_bias": 0.30833, "authority_bias": 0.24667},
}

API_LABELS = {
    "claude-opus-4-6": "Opus 4.6",
    "gpt-5.5": "GPT-5.5",
    "gemini-3.1-pro-preview": "Gemini 3.1 Pro",
    "gpt-4.1": "GPT-4.1",
    "claude-sonnet-4-6": "Sonnet 4.6",
    "gpt-4.1-nano": "GPT-4.1 Nano",
    "gemini-3.5-flash": "Gemini 3.5 Flash",
    "gpt-4.1-mini": "GPT-4.1 Mini",
    "claude-3-haiku": "Claude 3 Haiku",
}
LOCAL_LABELS = {
    "qwen2.5-72b": "Qwen2.5-72B",
    "llama3.1-70b": "LLaMA 3.1-70B",
    "mistral-large": "Mistral-Large",
    "qwen2.5-32b": "Qwen2.5-32B",
    "qwen2.5-14b": "Qwen2.5-14B",
    "llama3.1-8b": "LLaMA 3.1-8B",
}

API_COLORS = [
    '#0D47A1', '#1565C0', '#1976D2', '#1E88E5', '#2196F3',
    '#42A5F5', '#64B5F6', '#90CAF9', '#5C6BC0',
]
LOCAL_COLORS = [
    '#BF360C', '#D84315', '#E64A19', '#F4511E', '#FF5722', '#FF7043',
]

N = len(ATTACKS)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


def plot_radar(ax, data_dict, labels_map, colors, panel_label):
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
    ax.set_thetagrids([a * 180 / pi for a in angles[:-1]], ATTACK_LABELS,
                      fontsize=7.5)

    max_val = max(max(v.values()) for v in data_dict.values())
    tick_max = min(0.8, round(max_val + 0.05, 1))
    ticks = np.arange(0.1, tick_max + 0.01, 0.1)
    ax.set_ylim(0, tick_max)
    ax.set_yticks(ticks)
    ax.set_yticklabels([f'{t:.0%}' for t in ticks], fontsize=6, color='#888888')

    ax.spines['polar'].set_visible(False)
    ax.grid(color='#E0E0E0', linewidth=0.5)

    handles = []
    for (model_id, vals), color in zip(data_dict.items(), colors):
        values = [vals[atk] for atk in ATTACKS]
        values += values[:1]
        lw = 2.2 if max(vals.values()) > 0.15 else 1.4
        line, = ax.plot(angles, values, linewidth=lw, color=color, alpha=0.85)
        ax.fill(angles, values, alpha=0.12, color=color)
        handles.append((line, labels_map[model_id]))

    ax.text(-0.08, 1.12, panel_label, transform=ax.transAxes,
            fontsize=11, fontweight='bold', va='top')
    return handles


fig = plt.figure(figsize=(9, 4), facecolor='white')

ax1 = fig.add_subplot(121, polar=True)
api_handles = plot_radar(ax1, api_data, API_LABELS, API_COLORS, '(a)')

ax2 = fig.add_subplot(122, polar=True)
local_handles = plot_radar(ax2, local_data, LOCAL_LABELS, LOCAL_COLORS, '(b)')

ax1.set_title('API Models', fontsize=10, fontweight='bold', pad=20)
ax2.set_title('Local Models', fontsize=10, fontweight='bold', pad=20)

ax1.legend([h[0] for h in api_handles], [h[1] for h in api_handles],
           loc='lower left', bbox_to_anchor=(-0.3, -0.22),
           ncol=3, fontsize=6.5, frameon=True, framealpha=0.9,
           edgecolor='#CCCCCC', handlelength=1.5, columnspacing=1.0)
ax2.legend([h[0] for h in local_handles], [h[1] for h in local_handles],
           loc='lower left', bbox_to_anchor=(-0.15, -0.18),
           ncol=3, fontsize=6.5, frameon=True, framealpha=0.9,
           edgecolor='#CCCCCC', handlelength=1.5, columnspacing=1.0)

plt.subplots_adjust(wspace=0.35)

outdir = '/root/cert_manip_resist_eval/figures'
os.makedirs(outdir, exist_ok=True)
plt.savefig(f'{outdir}/fig_model_radar.pdf')
plt.savefig(f'{outdir}/fig_model_radar.png')
print(f'Saved to {outdir}/fig_model_radar.pdf and .png')
