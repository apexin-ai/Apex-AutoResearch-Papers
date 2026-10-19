# analysis comet tertile ablation 105

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comet-tertile-ablation-105_20260522T021600_result.json`
- **Structured JSON:** [`728e094cd2611b082082.json`](../../sessions/72/728e094cd2611b082082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## COMET Tertile Ablation 结果 (plan_105)

| Tertile | COMET range | n | balanced_acc |
|---------|-------------|---|-------------|
| **Low** | [0.44, 0.64] | 56 | **0.6635** |
| **Med** | [0.64, 0.76] | 56 | **0.6769** |
| **High** | [0.76, 0.95] | 56 | **0.6071** |

- **Full test bal_acc**: 0.6488 (EN→ZH, layer 22)
- **Delta (High - Low)**: **-5.64 pp** (方向反转 — 高 COMET 反而 probe acc 更低)
- **Fisher exact test**: p = 0.695, OR = 0.79 (远未显著)

**结论: NOT confounder。** 翻译质量与探针准确率无正相关。高 COMET 样本的 probe acc 反而略低于低 COMET 样本，且差异不显著。COMET gate 可以放宽而不影响探针实验的效度。

已完成：
1. 脚本 `/root/clkc_mech_interp/src/comet_tertile_ablation.py`
2. 结果 `/root/clkc_mech_interp/data/qwen3/comet_tertile_ablation.json`
3. `mvp_probe_v1` registry metrics 已更新
4. Artifact 已注册

**阈值修正**：`validate_translation.py` line 171 已经是 `>= threshold`，无需修改。

---
