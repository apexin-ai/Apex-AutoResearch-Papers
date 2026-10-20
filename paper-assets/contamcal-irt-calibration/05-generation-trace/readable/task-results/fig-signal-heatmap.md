# fig signal heatmap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fig_signal_heatmap_20260517T094543_result.json`
- **Structured JSON:** [`901675fca717d54974de.json`](../../sessions/90/901675fca717d54974de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成成功。

结果：
- PDF: 26,100 bytes, PNG: 98,426 bytes（均 > 10KB）
- 保存位置：`/root/contamcal-irt-calibration/figures/fig_signal_heatmap.pdf` 和 `.png`

数据摘要：

| Signal | 0.5B d005 | 0.5B d025 | 1.5B d005 | 1.5B d025 | 3B d005 | 3B d025 |
|--------|-----------|-----------|-----------|-----------|---------|---------|
| S1 Embedding | **0.98** | **0.97** | **0.98** | **0.97** | **0.95** | **0.94** |
| S2 Min-K%++ | 0.53 | 0.55 | 0.56 | 0.53 | 0.52 | 0.52 |
| S4 Self-Critique | 0.53 | 0.52 | 0.53 | 0.52 | 0.53 | 0.50 |
| RRF Ensemble | **0.69** | **0.70** | **0.70** | **0.70** | **0.66** | **0.67** |

d100 列全部接近 0.5（使用 d005 labels 时，d100 模型已无法区分子集）。

注意：S1 Embedding 在 0.5B/1.5B 间完全相同，因为该信号基于固定 embedding 模型计算文本相似度，与训练模型无关（同 seed 同 dosage → 相同训练集 → 相同信号）。S2/S4 是模型相关的但检测力弱（AUC~0.52-0.56）。

---
