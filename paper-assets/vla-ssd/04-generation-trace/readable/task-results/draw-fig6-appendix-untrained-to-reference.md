# draw fig6 appendix untrained to reference

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_draw_fig6_appendix_untrained_to_reference_20260523T195340_result.json`
- **Structured JSON:** [`a32e64c54b25ac64c15f.json`](../../sessions/a3/a32e64c54b25ac64c15f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 个 PDF 已传输到本地。

## 汇报

### 已修改并重新生成的图（7 个）

| 本地文件名 | 修改内容 | 脚本 |
|---|---|---|
| `fig_counterfactual_bar.pdf` | title: "Untrained base VLMs" → "Reference base VLMs" | `/tmp/draw_counterfactual_bar.py` |
| `fig_action_r2_threecond.pdf` | legend: "Untrained VLA" → "Reference VLA" | `/root/vla-ssd/scripts/plot_action_r2_threecond.py` |
| `fig_multi_layer_attn.pdf` | legend: "Untrained VLA" → "Reference VLA" | `/tmp/plot_multi_layer_attention.py` |
| `fig_rsa_perlayer_curve.pdf` | legend: "Untrained, image mean/last pre-action" → "Reference, ..." | `/tmp/plot_rsa_perlayer.py` |
| `fig_32layer_attention.pdf` | legend: "Untrained VLA" → "Reference VLA" (2处) | `/root/vla-ssd/scripts/plot_full_32layer_attention.py` |
| `fig_probe_conditions.pdf` | legend: "Untrained VLA" → "Reference VLA" | `/root/vla-ssd/scripts/plot_three_condition_probe.py` |
| `fig2_cross_instruction_heatmap.pdf` | ylabel: "Untrained\nlast_preaction" → "Reference\nlast_preaction" | `/tmp/gen_heatmap.py` |

另外 2 个脚本也已修改但输出不在 paper 目录中：
- `plot_32layer_attention_profile.py` — legend "Untrained VLA" → "Reference VLA"
- `plot_threecond_multiseed_v2.py` — legend "Untrained" → "Reference"

### 不包含 "Untrained" 的图（跳过）
- `fig_teaser.pdf`, `fig_specificity_bootstrap_30seeds.pdf`, `fig_ood_diagnostics.pdf`, `fig_claim_evidence.pdf`, `fig_matrix_heatmap.pdf`, `fig_overview.pdf`, `fig_dose_response.pdf`

### 其他 Worker 处理（跳过）
- `fig_r2_collapse.pdf`, `fig_cross_arch_l1.pdf`

---
