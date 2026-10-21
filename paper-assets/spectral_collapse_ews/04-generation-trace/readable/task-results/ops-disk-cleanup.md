# ops disk cleanup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_20260520T081104_result.json`
- **Structured JSON:** [`3ae98323d36d6ae1bacb.json`](../../sessions/3a/3ae98323d36d6ae1bacb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果：

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 可用空间 | 12G | **27G** |
| 释放量 | — | **~15G** |
| 使用率 | 96% | **90%** |

27G 可用，未达 29G 目标（差 2G）。原因是 `linear_increasing_seed42` 实际只有 1.6G 而非预估更大。三个批准删除的目录已全部清除，剩余 `checkpoints_phase1/` 内容：

| 目录 | 大小 | 备注 |
|------|------|------|
| adaptive_k10_seed42 | 17G | |
| fixed_mix_r025_seed42 | 17G | |
| fixed_mix_r02_seed42 | 17G | |
| fixed_mix_r03_seed42 | 17G | |
| fixed_mix_r03_seed43 | 4.6G | 可能正在运行 |
| fixed_mix_seed42 | 17G | |
| pure_collapse_seed43 | 17G | 正在运行 |
| pure_collapse_seed44 | 1.6G | 正在运行 |

27G 应足够支撑 exp_012 + exp_013 的 16-18G checkpoint 写入。如需严格达到 29G，需要你确认是否可以删除其他 phase1 checkpoint。

---
