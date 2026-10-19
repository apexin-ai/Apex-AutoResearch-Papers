# infra gemma L10 progress check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gemma-L10-progress-check_20260523T120151_result.json`
- **Structured JSON:** [`243a8ec7f6cb0d54e422.json`](../../sessions/24/243a8ec7f6cb0d54e422.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma L10 Steering 实验结果

**状态：已完成**（进程已退出，GPU 0 空闲：0% 利用率，0 MiB 显存）

### Probe
- Layer 10 probe accuracy: **70.6%**

### Baseline 分布 (n=158 conflict samples)
| both | neither | parametric | contextual |
|------|---------|------------|------------|
| 32   | 55      | 26         | 45         |

### Steering 结果

| alpha | steering flips | control flips | Fisher p | 显著? |
|-------|---------------|---------------|----------|-------|
| +5.0  | 3/158 (1.9%)  | 2/158 (1.3%)  | 1.0000   | No    |
| +10.0 | 1/158 (0.6%)  | 1/158 (0.6%)  | 1.0000   | No    |
| +20.0 | 5/158 (3.2%)  | 1/158 (0.6%)  | 0.2143   | No    |

所有 alpha 下 p→c 和 c→p 均为 0。Steering 在 L10 完全无效——flip 率极低且与 control 无显著差异，Bonferroni 校正后更不显著。结果文件保存在 `data/gemma2/steering_results.json`（注意不是预期的 `steering_results_L10_last.json`）。

---
