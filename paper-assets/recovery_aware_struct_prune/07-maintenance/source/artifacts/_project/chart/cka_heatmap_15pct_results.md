CKA Heatmap 15% Sparsity Results

Remote paths (westd-29022):
- Heatmap PNG: /root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_15pct.png
- CKA-only JSON: /root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_cka_only_15.json
- Standard JSON: /root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_standard_15.json
- Dense reprs cache: /root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/dense_reprs.pt

Diagonal CKA means:
| Method      | 15% sparsity | 20% sparsity |
|-------------|-------------|-------------|
| CKA-only    | 0.6104      | 0.6202      |
| Standard    | 0.8958      | 0.9039      |

Key findings:
- CKA-only 15%: layers 9-23 CKA drops to 0.42-0.51, significant representation reorganization
- Standard 15%: overall high similarity (>0.7), minor dip at layers 4-6
- Pattern consistent with 20%, confirming diversity preservation mechanism