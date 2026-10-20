# analysis n32 greedy consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n32_greedy_consistency_20260516T143116_result.json`
- **Structured JSON:** [`a5bbee310ab3294045d6.json`](../../sessions/a5/a5bbee310ab3294045d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### 根因（两个 bug 叠加）

1. **`analyze_n32.py` 用 `samples[0]`（T=1.0 随机 sample）冒充 greedy**，而非读取数据中的 `"greedy"` 字段。这导致 Greedy_F1 被低估为 0.5880（实际 greedy = 0.6141）。

2. **两个数据源的 greedy decode 不同**：exp_001_seed42_v2（N=2~16）和 exp_025_n32（N=32）中 29/551 实例的 greedy 不一致（推理时浮点非确定性），导致即使修正 bug1 后仍有 3pp 差异。

### 修复

用 exp_025_n32 数据统一计算 N={2,4,8,16,32}（subsample + 同一 greedy），结果保存在 `output/exp_025_n32/unified_results.json`。

### 修正后统一表格

| N  | Degen% | Greedy_F1 | Oracle_F1 | Oracle_gap | LP_Δ   | SJ_Δ   | FK_Δ   | EM_Δ   | VC_Δ   |
|----|--------|-----------|-----------|------------|--------|--------|--------|--------|--------|
| 2  | 44.1%  | 0.6141    | 0.6579    | 0.0438     | -0.75  | -2.54  | -2.54  | -2.54  | -2.27  |
| 4  | 22.4%  | 0.6141    | 0.7122    | 0.0980     | -0.01  | -0.61  | -0.50  | -1.27  | -1.30  |
| 8  | 12.4%  | 0.6141    | 0.7522    | 0.1381     | **+0.42** | +0.03 | +0.11 | -0.33  | -1.82  |
| 16 | 6.8%   | 0.6141    | 0.7813    | 0.1672     | **+0.63** | +0.26 | +0.43 | -0.15  | -2.91  |
| 32 | 4.0%   | 0.6141    | 0.8061    | 0.1919     | **+0.91** | +0.33 | **+0.62** | +0.21 | -4.18  |

### 结论

- Selection delta 为正（LP 从 N=8 开始超 greedy，至 N=32 达 +0.91pp）
- 趋势 monotonic：更多 sample → 更好 selection
- N=32 时 4/5 信号为正（LP/SJ/FK/EM），仅 VC 失败
- **论文 narrative "selection at sufficient N succeeds" 成立**，但幅度比 buggy 版本小（+0.91pp vs 之前声称的 +3.53pp）

---
