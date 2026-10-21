# code check gemma2b 10k done

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_gemma2b_10k_done_20260522T231455_result.json`
- **Structured JSON:** [`42bb1665ba3ea592814f.json`](../../sessions/42/42bb1665ba3ea592814f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## exp_gemma2b_10k 实验报告

**状态**: 成功完成（2026-05-23 07:12 服务器时间）

### Pairwise AUC

| 对比 | 5K AUC | 10K AUC | 变化 |
|------|--------|---------|------|
| 0v1 | — | 0.9817 ± 0.0013 | — |
| 1v2 | 0.5981 | **0.6430 ± 0.0061** | +0.045 |
| 2v3 | — | 0.5550 ± 0.0073 | — |
| 3v4 | — | 0.5173 ± 0.0050 | — |
| 4v5 | — | 0.5101 ± 0.0123 | — |

### K* 判定

- **5K**: K\*=1（1v2=0.5981，borderline < θ=0.60）
- **10K**: **K\*=2**（1v2=0.6430，明确 > θ=0.60）

**关键发现**: 5K 的 borderline 判定 **不稳定**。增加到 10K 样本后，1v2 AUC 从 0.5981 跃升到 0.6430，跨过了 0.60 阈值，K\* 从 1 变为 2。这说明 5K 样本量不足以对 Gemma-2-2B 做出稳定的 depth-1 vs depth-2 区分判定。

**假设对比**: 原假设预期 K\*=1 保持不变，实际 K\*=2。Gemma-2-2B 的 distinguishable depth 比 5K 实验显示的更深。

Registry 已更新为 DONE/success，metrics 已记录。

---
