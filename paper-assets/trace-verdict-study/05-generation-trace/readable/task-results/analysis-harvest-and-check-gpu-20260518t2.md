# analysis harvest and check gpu 20260518T2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_and_check_gpu_20260518T2_20260518T183518_result.json`
- **Structured JSON:** [`92cee4e8d124432f3e85.json`](../../sessions/92/92cee4e8d124432f3e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
GPU STATUS: 双卡空闲 (RTX PRO 6000 Blackwell ×2, 0% util, 无进程)

DEEPSEEK_SEED456: accuracy=96.1% [95.0%, 97.1%]
  seed comparison: seed42=93.6%, seed456=96.1% (+2.4pp)
  pass F1=0.97, fail F1=0.93

QWEN7B_SEED123:   accuracy=96.0% [94.9%, 97.1%]
  seed comparison: seed42=93.6%, seed123=96.0% (+2.4pp)
  pass F1=0.97, fail F1=0.93
```

**注意事项：**
- 两个实验训练都完成了，但因磁盘满 (250G/250G 100%) 导致模型保存和 eval 写入失败。已清理中间 checkpoint 释放 2.5GB 后重跑 eval 成功。
- Qwen7b 的 final/ 用 checkpoint-444（最后一步）替换了截断的文件。
- 两个 seed 都显著高于 seed42 (93.6%)，三 seed 均在 93-97% 区间内，seed robustness 假设成立。
- 磁盘仍然很紧张 (247.5G/250G)，后续实验需要先清理旧 checkpoint。

---
