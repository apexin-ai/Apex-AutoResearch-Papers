# Type 3 字体消除报告

## 概述
- **扫描范围**: docs/paper/figures/ 下全部 39 个 PDF
- **检出 Type 3**: 21 个
- **修复后 Type 3**: 0 个

## 修复方法

### 方法 A: 脚本重新生成 (REGEN) — 14 个文件
在远程服务器上设置 `matplotlib.rcParams['pdf.fonttype'] = 42`（通过 MPLCONFIGDIR），重新运行原始生成脚本。
生成 TrueType 字体嵌入，文件大小通常更小。

### 方法 B: Ghostscript 轮廓转换 (GS) — 7 个文件
无独立生成脚本（inline 代码生成），使用 `gs -dNoOutputFonts` 将所有字体转为矢量路径。
视觉效果完全保留，但文件大小有所膨胀。

## 详细结果

| 文件 | 原始大小 | 修复后 | 比率 | 方法 | 论文使用 |
|------|---------|--------|------|------|---------|
| fig2.pdf | 21,853 | 14,066 | 0.64x | REGEN | YES |
| fig2_cross_instruction_heatmap.pdf | 22,965 | 21,342 | 0.93x | REGEN | - |
| fig3.pdf | 27,812 | 14,056 | 0.51x | REGEN | - |
| fig4.pdf | 20,772 | 39,680 | 1.91x | REGEN | YES |
| fig5.pdf | 31,971 | 58,536 | 1.83x | GS | YES |
| fig6.pdf | 32,897 | 78,758 | 2.39x | GS | YES |
| fig7.pdf | 25,754 | 26,177 | 1.02x | REGEN | YES |
| fig8a_trained_summary.pdf | 90,867 | 61,208 | 0.67x | GS | - |
| fig8a_trained_task0.pdf | 94,109 | 79,418 | 0.84x | GS | - |
| fig8b_untrained.pdf | 120,832 | 209,289 | 1.73x | GS | - |
| fig_32layer_attention.pdf | 20,278 | 13,545 | 0.67x | REGEN | - |
| fig_l1_stacked_bar.pdf | 26,978 | 39,155 | 1.45x | GS | YES |
| fig_matrix_heatmap.pdf | 32,252 | 35,993 | 1.12x | REGEN | YES |
| fig_multi_layer_attn.pdf | 25,664 | 22,753 | 0.89x | REGEN | YES |
| fig_ood_diagnostics.pdf | 37,559 | 20,966 | 0.56x | REGEN | YES |
| fig_overview_matplotlib_v2.pdf | 49,411 | 100,293 | 2.03x | GS | - |
| fig_probe_conditions.pdf | 18,640 | 14,605 | 0.78x | REGEN | YES |
| fig_random_subset_ablation.pdf | 17,698 | 12,696 | 0.72x | REGEN | - |
| fig_rsa_perlayer_curve.pdf | 19,655 | 19,537 | 0.99x | REGEN | YES |
| libero_spatial_r2_perlayer.pdf | 22,995 | 22,261 | 0.97x | REGEN | - |
| libero_spatial_rsa_perlayer.pdf | 24,627 | 23,968 | 0.97x | REGEN | - |

## 超过 2x 膨胀的文件
- `fig6.pdf` (2.39x, 79KB) — GS 方法, 论文 appendix 使用
- `fig_overview_matplotlib_v2.pdf` (2.03x, 100KB) — GS 方法, 不在论文 \includegraphics 中

两个文件绝对大小均 < 101KB，不影响论文编译或投稿。

## 原始文件备份
`/tmp/type3_backup/` 保存了全部 21 个原始文件。

## 使用的脚本（REGEN 方法）
- plot_action_probes.py → fig2, fig3, fig4
- plot_ood_diagnostics.py → fig_ood_diagnostics
- plot_spatial_results.py → fig7, libero_spatial_*
- plot_32layer_attention_profile.py → fig_32layer_attention
- plot_rsa_perlayer.py → fig_rsa_perlayer_curve
- plot_multi_layer_attention.py → fig_multi_layer_attn
- draw_matrix_heatmap.py → fig_matrix_heatmap
- gen_heatmap.py → fig2_cross_instruction_heatmap
- plot_three_condition_probe.py → fig_probe_conditions
- plot_random_subset (standalone) → fig_random_subset_ablation
