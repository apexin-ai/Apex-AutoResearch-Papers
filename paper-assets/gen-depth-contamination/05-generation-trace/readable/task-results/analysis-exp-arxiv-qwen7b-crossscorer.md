# analysis exp arXiv qwen7b crossscorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_qwen7b_crossscorer_20260518T030219_result.json`
- **Structured JSON:** [`4ded03f8656b7729abc8.json`](../../sessions/4d/4ded03f8656b7729abc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## exp_arXiv_qwen7b_crossscorer 结果

**实验状态**: 成功完成 (EXIT_CODE=0)

**Hypothesis**: 2v3 AUC ≥ 0.60 → K\*=3 scorer-independent
**Result**: **Rejected (negative)**

| Pair | Pythia-1.4B (cross) | Qwen-1.5B (orig) | Delta |
|------|----:|----:|------:|
| 0v1 | 0.958 | 0.983 | -0.025 |
| 1v2 | 0.817 | 0.835 | -0.018 |
| **2v3** | **0.599** | **0.626** | **-0.027** |
| 3v4 | 0.542 | 0.544 | -0.002 |
| 4v5 | 0.519 | 0.513 | +0.006 |

**K\* = 2**（cross-scorer），原 K\*=3（Qwen scorer）

关键发现：
- 2v3 AUC=0.5989，差 0.0011 未过 0.60 阈值（3/5 folds 过线，borderline）
- Qwen family bias 约 0.027 AUC，小但足以翻转阈值判定
- Depths 0-2 的污染信号 robustly scorer-independent
- 保守估计 arXiv scorer-independent K\*=2，真实边界在 [2, 3] 区间

报告已写入 artifacts 并注册，registry 已更新为 DONE/negative。

---
