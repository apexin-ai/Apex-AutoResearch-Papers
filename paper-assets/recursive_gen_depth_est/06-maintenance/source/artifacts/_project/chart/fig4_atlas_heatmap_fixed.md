Fig 4 Atlas Heatmap - fixed data source

Before: plot_atlas_figures.py re-trained RF per cell → values drifted from Table
After: uses per-experiment RF 4-class accuracy from registry

Accuracy matrix (%):
              nucleus   temp=0.9   top-k=50
Pythia-1.4B    78.2      76.2       69.6
OLMo-1B        78.8      82.0       74.2
GPT-2 XL       83.3      85.4       76.6

Output: figures/paper/fig_atlas_heatmap.pdf / .png