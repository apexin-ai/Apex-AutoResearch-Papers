# ssh 14b training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-training-progress-check_20260523T062110_result.json`
- **Structured JSON:** [`ffedc17212e31b971f7c.json`](../../sessions/ff/ffedc17212e31b971f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。

```
=== 14B Multi-seed Training Progress ===

| 实验 | GPU | 状态 | 当前step/总step | Train Loss (ep0.94) | Eval Loss (ep1.0) | 速度 | 预计剩余 |
|------|-----|------|----------------|--------------------|--------------------|------|---------|
| cls14b-func-s123 | 0 | RUNNING | 802/1434 (56%) | 0.0539 | 0.0683 | 7.12s/it | ~75min |
| cls14b-func-s456 | 1 | RUNNING | 801/1434 (56%) | 0.0585 | 0.0659 | 7.19s/it | ~76min |
| cwm14b-func-s123 | 2 | RUNNING | 808/1434 (56%) | 0.0402 | 0.0447 | 7.03s/it | ~73min |
| cwm14b-func-s456 | 3 | RUNNING | 812/1434 (57%) | 0.0382 | 0.0451 | 7.03s/it | ~73min |
```

**注意**：实际 total steps = 1434（478 steps/epoch × 3 epochs），不是任务描述中的 4302。4 个实验均在 epoch 2 中段，运行已 ~1h37m，GPU 利用率 53-67%，显存占满（~31GB/32GB）。

**Eval**：4 个实验均未完成，无法执行 eval。预计全部在 ~75 分钟后完成。

**Loss 趋势观察**：
- CWM 模型 loss 明显低于 CLS（0.038-0.040 vs 0.054-0.059），与 s42 的模式一致
- 两个 seed 之间 loss 差异很小（CLS: 0.054 vs 0.059, CWM: 0.038 vs 0.040），seed 稳定性好

---
