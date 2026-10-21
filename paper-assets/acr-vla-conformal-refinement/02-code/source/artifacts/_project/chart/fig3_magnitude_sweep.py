#!/usr/bin/env python3
"""Fig3: Magnitude sweep norm sensitivity curve (LIBERO-Spatial)."""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

FIG_DIR = Path(__file__).resolve().parent.parent / "paper" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ── data ─────────────────────────────────────────────────────────────
norms = np.array([0.03, 0.05, 0.10, 0.20, 0.30])

obs_only_sr = np.array([39.0, 35.0, 35.0, 35.0, 36.0])
obs_only_n  = np.array([8, 10, 10, 10, 10])

perdof_sr   = np.array([30.0, 31.0, 35.0, 28.3, 26.0])
perdof_n    = np.array([10, 10, 10, 6, 10])

argmin_sr   = 34.0
vla_only_sr = 30.0

# ── style ────────────────────────────────────────────────────────────
C_OBS    = "#009E73"
C_PER    = "#E69F00"
C_ARGMIN = "#555555"
C_VLA    = "#AAAAAA"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman", "Times"],
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8.5,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# ── plot ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(4.5, 3.0))

# light horizontal guidelines
for y in [25, 30, 35, 40, 45]:
    ax.axhline(y, color="#E0E0E0", linewidth=0.5, zorder=0)

# baselines
ax.axhline(argmin_sr, color=C_ARGMIN, linestyle="--", linewidth=1.0,
           label=f"Argmin K=10 ({argmin_sr:.0f}%)", zorder=1)
ax.axhline(vla_only_sr, color=C_VLA, linestyle=":", linewidth=1.0,
           label=f"VLA-only ({vla_only_sr:.0f}%)", zorder=1)

# --- obs_only ---
full_obs = obs_only_n == 10
ax.plot(norms[full_obs], obs_only_sr[full_obs], "-", color=C_OBS, linewidth=1.8, zorder=3)
ax.plot(norms[full_obs], obs_only_sr[full_obs], "o", color=C_OBS, markersize=6,
        zorder=4, label="ACR obs-only")
# partial points: hollow marker + connecting line segment
partial_obs = ~full_obs
if partial_obs.any():
    ax.plot(norms[partial_obs], obs_only_sr[partial_obs], "o", color=C_OBS,
            markersize=6, markerfacecolor="white", markeredgewidth=1.5, zorder=4)
    # dashed connector from partial to next full point
    for idx in np.where(partial_obs)[0]:
        if idx + 1 < len(norms):
            ax.plot(norms[idx:idx+2], obs_only_sr[idx:idx+2], "--", color=C_OBS,
                    linewidth=1.2, zorder=2)
        for i_p in np.where(partial_obs)[0]:
            ax.annotate(f"({obs_only_n[i_p]}/10)", (norms[i_p], obs_only_sr[i_p]),
                        textcoords="offset points", xytext=(6, 6),
                        fontsize=7, color=C_OBS, ha="left")

# --- perdof ---
full_per = perdof_n == 10
ax.plot(norms[full_per], perdof_sr[full_per], "-", color=C_PER, linewidth=1.8, zorder=3)
ax.plot(norms[full_per], perdof_sr[full_per], "s", color=C_PER, markersize=5.5,
        zorder=4, label="ACR per-DOF")
partial_per = ~full_per
if partial_per.any():
    ax.plot(norms[partial_per], perdof_sr[partial_per], "s", color=C_PER,
            markersize=5.5, markerfacecolor="white", markeredgewidth=1.5, zorder=4)
    for idx in np.where(partial_per)[0]:
        # dashed connectors to neighbours
        if idx - 1 >= 0:
            ax.plot(norms[idx-1:idx+1], perdof_sr[idx-1:idx+1], "--", color=C_PER,
                    linewidth=1.2, zorder=2)
        if idx + 1 < len(norms):
            ax.plot(norms[idx:idx+2], perdof_sr[idx:idx+2], "--", color=C_PER,
                    linewidth=1.2, zorder=2)
        for i_p in np.where(partial_per)[0]:
            ax.annotate(f"({perdof_n[i_p]}/10)", (norms[i_p], perdof_sr[i_p]),
                        textcoords="offset points", xytext=(-14, -10),
                        fontsize=7, color=C_PER, ha="center")

# reconnect full-point segments that were split by partial points
# obs_only: connect the line through all points with solid where both ends are full
for i in range(len(norms) - 1):
    if full_obs[i] and full_obs[i+1]:
        pass  # already drawn by the bulk plot
    # nothing extra needed — the bulk "-" line already connects consecutive full pts

# perdof: same — bulk line connects consecutive full points
# but we need to handle the gap around partial. The segments around idx=3 (0.20)
# are drawn dashed above, and the solid connects 0→1→2 and 4 is isolated.
# Let's add a solid segment 0→1→2 explicitly and the isolated point 4 is fine.
# Actually the bulk plot already handles contiguous full segments.

# ── annotation: drop at perdof 0.30 ─────────────────────────────────
drop_per = perdof_sr[4]  # 26.0 at norm=0.30
ax.annotate(
    "−9 pp\nfrom peak",
    xy=(0.30, drop_per + 0.5), xytext=(0.22, 22.5),
    fontsize=7.5, color=C_PER, ha="center", va="bottom",
    arrowprops=dict(arrowstyle="->", color=C_PER, lw=1.1),
)

# ── axes ─────────────────────────────────────────────────────────────
ax.set_xscale("log")
ax.set_xticks(norms)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:g}"))
ax.xaxis.set_minor_formatter(mticker.NullFormatter())
ax.set_xlim(0.025, 0.38)

ax.set_ylim(20, 50)
ax.set_xlabel(r"Correction magnitude norm $\varepsilon$")
ax.set_ylabel("Success Rate (%)")

ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor="#CCCCCC",
          framealpha=0.9)

fig.tight_layout()

# ── save ─────────────────────────────────────────────────────────────
pdf_path = FIG_DIR / "fig3_magnitude_sweep.pdf"
png_path = FIG_DIR / "fig3_magnitude_sweep.png"
fig.savefig(pdf_path)
fig.savefig(png_path)
plt.close(fig)

print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
