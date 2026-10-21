"""Figure A.3: Gradient SNR trajectory — KL vs BCE over 1000 training steps."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'cm',
})

COL_KL  = '#4472C4'
COL_BCE = '#E05A3A'

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

steps = np.array([0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000])

kl_mean = np.array([
    1.2956733371538576e-05, 2.5334954261779785e-04, 6.113781710155308e-04,
    5.700207548215985e-04, 2.3567494645249099e-04, 2.3308649542741477e-04,
    3.464480396360159e-04, 3.388772893231362e-04, 3.500452730804682e-04,
    5.835744668729603e-04, 2.1453911904245615e-04, 2.970779678435065e-05,
    5.523565923795104e-04, 8.77720071002841e-04,
])
kl_ci_lo = np.array([
    7.360159869633805e-06, 1.4717240274655222e-04, 4.83955190470071e-04,
    4.7539334222246776e-04, 1.7454024144043578e-04, 1.737218737796996e-04,
    2.4066227852812883e-04, 2.8911733466106365e-04, 2.9260610345360256e-04,
    4.4527891732388646e-04, 1.128199579401e-04, 1.7404022288044286e-05,
    4.5707749360185727e-04, 6.138791949455868e-04,
])
kl_ci_hi = np.array([
    1.8553306873443347e-05, 3.5952668248904346e-04, 7.388011515609906e-04,
    6.646481674207293e-04, 2.968096514645462e-04, 2.9245111707512997e-04,
    4.5223380074390295e-04, 3.8863724398520877e-04, 4.074844427073338e-04,
    7.218700164220342e-04, 3.1625828014481233e-04, 4.201157128065701e-05,
    6.476356911571635e-04, 1.141560947060095e-03,
])

bce_mean = np.array([
    6.990545080043375e-05, 8.232939762820024e-06, 1.729041337966919e-03,
    2.9259882867336273e-03, 3.07848141528666e-03, 3.99128720164299e-03,
    1.7421682132408023e-03, 4.220924340188503e-03, 1.6771267401054502e-03,
    5.062801297754049e-03, 1.4131924835965037e-03, 1.038489630445838e-03,
    1.970048062503338e-03, 2.02628830447793e-03,
])
bce_ci_lo = np.array([
    5.279848063248854e-05, 5.820687274953616e-06, 6.659333503240255e-04,
    1.3077121652648434e-03, 2.440582192018413e-03, 2.8634059681604757e-03,
    1.2065655083637937e-03, 2.7501309339854996e-03, 1.126070846300626e-03,
    3.6193370441147854e-03, 9.328168596835326e-04, 6.354701824708862e-04,
    1.4372976670020004e-03, 1.4981359136526243e-03,
])
bce_ci_hi = np.array([
    8.701242096837897e-05, 1.0645192250686432e-05, 2.7921493256098124e-03,
    4.544264408202411e-03, 3.7163806385549073e-03, 5.1191684351255045e-03,
    2.277770918117811e-03, 5.6917177463915065e-03, 2.2281826339102745e-03,
    6.506265551393314e-03, 1.8935681075094748e-03, 1.4415090784207897e-03,
    2.5027984580046755e-03, 2.554440695303236e-03,
])

fig, ax = plt.subplots(figsize=(3.3, 2.5))

ax.fill_between(steps, kl_ci_lo, kl_ci_hi, color=COL_KL, alpha=0.12, zorder=2)
ax.plot(steps, kl_mean, color=COL_KL, marker='o', markersize=4,
        linewidth=1.3, label='Forward KL', zorder=3,
        markeredgecolor='white', markeredgewidth=0.4)

ax.fill_between(steps, bce_ci_lo, bce_ci_hi, color=COL_BCE, alpha=0.12, zorder=2)
ax.plot(steps, bce_mean, color=COL_BCE, marker='s', markersize=4,
        linewidth=1.3, label='BCE', zorder=3,
        markeredgecolor='white', markeredgewidth=0.4)

ax.set_yscale('log')
ax.set_xlabel('Training Step')
ax.set_ylabel('Gradient SNR')
ax.set_xlim(-20, 1020)

ax.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

ax.legend(loc='lower right', frameon=True, fancybox=False,
          edgecolor='#DDDDDD', framealpha=0.9, fontsize=7,
          bbox_to_anchor=(0.98, 0.02), handletextpad=0.4)

ax.annotate(
    'BCE: higher SNR\nbut worse masks',
    xy=(400, bce_mean[7]),
    xytext=(620, 1.5e-02),
    fontsize=7, ha='center',
    arrowprops=dict(arrowstyle='->', color='#888888', lw=0.7),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8F0',
              edgecolor='#E0E0E0', alpha=0.9, linewidth=0.5),
)

fig.tight_layout()
fig.savefig(f'{OUT}/snr_trajectory.pdf')
fig.savefig(f'{OUT}/snr_trajectory.png')
print('Saved snr_trajectory.pdf/.png')
plt.close()
