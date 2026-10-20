# analysis regenerate summaries

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_regenerate_summaries_20260515T170831_result.json`
- **Structured JSON:** [`96323ae6ba1d7ef71198.json`](../../sessions/96/96323ae6ba1d7ef71198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已用统一 eval 数字重新生成并注册。

**关键变化汇总：**

| 项目 | 旧值 | 新值 |
|------|------|------|
| uniform mean | 17.693 | 17.694 |
| adaptive seed42 (n_min=3) | 17.690 | **17.644** |
| adaptive mean (n_min=3) | 17.653 | **17.639** |
| adaptive_fix seed42 (n_min=2) | 17.650 | 17.653 |
| adaptive_fix seed456 | 17.660 | 17.657 |
| n_min=3 std | 0.032 | **0.007** |
| n_min=2 std | 0.009 | **0.007** |
| capture ratio (aggregate) | ~87% | **~91%** |
| tau_05 | RUNNING | **DONE, PPL=17.688** |

**叙事修正：**
- n_min=3 seed42 的 PPL 从 17.690（与 uniform 持平）修正为 17.644 — 先前的 "异常偏高" 是 eval 不一致的产物
- n_min=2 vs n_min=3 的 std 相同（0.007），旧的 "3.5x 更稳定" 叙事已移除
- n_min=3 mean (17.639) 实际略优于 n_min=2 (17.651)，差异在噪声范围内
- D019 capture ratio 从 ~87% 上升至 ~91%
- D031 note 更新：variance 差异是 eval artifact

---
