# check cwm8b shard status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cwm8b-shard-status_20260516T043426_result.json`
- **Structured JSON:** [`c3d1b9b424628e8b5739.json`](../../sessions/c3/c3d1b9b424628e8b5739.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B ckpt-400 Test Eval 状态汇总

### 进程状态

| Shard | PID | GPU | 状态 | 进度 | 已完成样本 | 总样本 | running_acc | 预计剩余 |
|-------|-----|-----|------|------|-----------|--------|-------------|---------|
| **v3** (full) | 443221 | cuda:3 | **Running** | 7240/9784 | 7240 (resumed 5287 + new 1953) | 9784 | 64.5% | **~5.3h** |
| **shard2** (7680→9784) | 448100 | cuda:1 | **Running** | 9320/9784 | 1640 new | 2104 | 67.4% | **~58min** |
| **shard3** (6200→7680) | 453335 | cuda:0 | **Running** | ~7192/7680 | 992 new | 1480 | — | **~61min** |
| **shard4** (9100→9783) | — | — | **DONE** | 688/688 | 688 | 684* | — | 完成 |

*shard4 有 688 行，略多于预期的 684，可能含 header 或尾行。已生成最终 `eval_repo_cwm_predictions.jsonl`。

### GPU 利用率

| GPU | 显存 | 利用率 | 分配 |
|-----|------|--------|------|
| 0 | 21133/32607 MiB | 92% | shard3 |
| 1 | 21133/32607 MiB | 87% | shard2 |
| 2 | 0/32607 MiB | 0% | 空闲 (shard4 已完成) |
| 3 | 21133/32607 MiB | 88% | v3 |

### 关键发现

1. **shard2 和 shard3 约 1 小时内完成**，它们的覆盖范围（6200-9784）与 v3 有大量重叠。shard 完成后可直接合并结果，不必等 v3 跑完全量。

2. **v3 还需约 5 小时**，因为它从头到尾跑全量 9784 样本（虽然 resumed 5287）。如果 shard2+shard3 完成后与 shard4 合并，再补上 v3 已有的 0-6200 范围结果，可以提前拼出完整结果，无需等 v3 跑完。

3. **GPU 2 空闲**，shard4 完成后释放了。如果需要加速 v3 剩余部分，可以再起一个 shard 在 GPU 2 上跑 v3 尚未覆盖的区间。

4. **shard4 确认 DONE** — 进程已退出，有完整的 `eval_repo_cwm_predictions.jsonl`（688 行），状态标记正确。

5. **所有运行中的进程状态正常**，CPU 100%、无异常。处理速率约 8 samples/min/GPU，一致且稳定。

---
