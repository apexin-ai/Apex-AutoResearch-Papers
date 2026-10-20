# ops gpqa progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpqa_progress_check_20260517T021222_result.json`
- **Structured JSON:** [`afe4903f49d9c08320ff.json`](../../sessions/af/afe4903f49d9c08320ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 个 GPQA 实验状态汇总

| 实验 | PID | 状态 | 进度 | 运行时间 | 预估剩余 |
|------|-----|------|------|----------|----------|
| gpqa_ds_importance_s020 | 580927 | **alive** | 143/198 (72%) | 8h51m | ~3.4h |
| gpqa_ds_importance_s025 | 599103 | **alive** | 56/198 (28%) | 2h59m | ~7.6h |
| gpqa_ds_importance_s030 | 606507 | **alive** | 25/198 (13%) | 1h12m | ~8.2h |
| gpqa_ds_random_s020 | 606658 | **alive** | 25/198 (13%) | 1h12m | ~8.2h |

**说明：**
- 所有进程正常运行中
- 输出目录（`profiling_output_gpqa_ds_*`）当前为空，结果应该是全部跑完后统一写入
- s020 最先启动（早约6h），进度最快；s025 启动时间为其一半左右但进度偏慢（平均每题 ~3.2min vs s020 的 ~3.7min），可能因为 sparsity 0.25 生成更长
- s030 和 random_s020 同时启动，进度一致（~2.9min/题），按当前速率约还需 8h+
- s020 的 timeout 为 24h（充足），其余为 18h（对于 ~9.5h 总时也充足）

---
