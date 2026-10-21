# check qwen3 progress urgent

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen3-progress-urgent_20260524T040641_result.json`
- **Structured JSON:** [`068d15337c73c2f38f05.json`](../../sessions/06/068d15337c73c2f38f05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验**全部完成**，results.json 已写入。进程仍在运行可能是做收尾工作。

```
seed123: [完成] 344/344 | SC=84.30% | SICA=85.47% | Δ=+1.16 pp | 耗时 9h58m
seed456: [完成] 345/345 | SC=83.48% | SICA=86.67% | Δ=+3.19 pp | 耗时 9h59m
seed789: [完成] 347/347 | SC=85.30% | SICA=85.30% | Δ=+0.00 pp | 耗时 9h58m
```

**三种子汇总：**

| 指标 | Mean | Std |
|------|------|-----|
| SC | 84.36% | ±0.91 |
| SICA | 85.81% | ±0.74 |
| **Δ (SICA−SC)** | **+1.45 pp** | — |

注意事项：
- n_problems 在种子间略有差异（344/345/347），可能是某些问题的 extraction 失败导致跳过（extraction_rate 约 99.6-99.9%）
- seed789 的 SICA 和 SC 完全一致（85.30%），Δ=0；seed456 的 Δ 最大（+3.19 pp）
- 矛盾率（contradiction_rate）稳定在 0.4-0.5%，约 40-43 个问题存在约束矛盾

---
