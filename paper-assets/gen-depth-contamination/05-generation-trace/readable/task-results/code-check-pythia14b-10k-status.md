# code check pythia14b 10k status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_pythia14b_10k_status_20260522T141304_result.json`
- **Structured JSON:** [`9c1b8cf0ab0306c84018.json`](../../sessions/9c/9c1b8cf0ab0306c84018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：SUCCESS**

所有产出完整：

| 检查项 | 结果 |
|--------|------|
| depth_0~5.jsonl | 各 10,000 行 ✓ |
| features.csv | 60,001 行（含 header） ✓ |
| results JSON | 4 个 JSON + summary.txt ✓ |
| 错误日志 | 无 error/OOM/traceback ✓ |

**关键 Metrics（Pythia-1.4B, C4, 10K samples）：**

| Metric | 值 |
|--------|-----|
| **K\*** | **2**（depth 0→1 AUC=0.97, depth 1→2 AUC=0.62, 之后 <0.60） |
| AUC(0v1) | 0.9712 ± 0.0028 |
| AUC(1v2) | 0.6175 ± 0.0035 |
| AUC(2v3) | 0.5364 ± 0.0094 |
| AUC(3v4) | 0.5134 ± 0.0066 |
| AUC(4v5) | 0.5088 ± 0.0094 |
| JSD(0v1) | 0.1368 |
| JSD(1v2) | 0.0079 |
| Ordinal MAE | 1.2846 |
| Ordinal Acc | 0.3503 |
| Top feature | freq_entropy |

信号衰减模式清晰：depth 0→1 有极强区分度（AUC 0.97），depth 1→2 仍可区分（0.62），depth 2+ 接近随机。JSD 也呈指数衰减（0.137 → 0.008 → 0.003）。

---
