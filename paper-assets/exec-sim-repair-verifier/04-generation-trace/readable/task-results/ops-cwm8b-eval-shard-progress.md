# ops cwm8b eval shard progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-eval-shard-progress_20260516T032512_result.json`
- **Structured JSON:** [`f572401bd5ff81058871.json`](../../sessions/f5/f572401bd5ff81058871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B ckpt-400 Test Eval 进度报告

### 进程状态：4/4 存活

| Shard | PID | GPU | 已运行 | GPU利用率 | 显存 |
|-------|--------|------|--------|-----------|------|
| v3 | 443221 | cuda:0 | 2h38m | 88% | 21.1/31.8 GB |
| shard2 | 448094 | cuda:1 | 1h59m | 89% | 21.1/31.8 GB |
| shard3 | 453335 | cuda:0* | 47m | 88% | 21.1/31.8 GB |
| shard4 | 454722 | cuda:2 | 34m | 88% | 21.3/31.8 GB |

### 各 shard 进度

从 shard4 log 时间戳算出实际处理速度：**~8.3 samples/min**（batch_size=8, ~58s/batch）。

| Shard | 范围 | 已完成 | 总量 | 进度 | 预估剩余 |
|-------|------|--------|------|------|----------|
| **v3** | 0-9784 | 6646 | 9784 | 67.9% | ~6h18m* |
| **shard2** | 7680-9784 | 1039 | 2104 | 49.4% | ~2h08m |
| **shard3** | 6200-7680 | 400 | 1480 | 27.0% | ~2h10m |
| **shard4** | 9100-9784 | 292 | 684 | 42.7% | ~47min |

### 关键发现

**v3 是断点续跑**：v3 运行 2h38m 但已有 6646 行结果。按实际速度 8.3/min 算，2h38m 只能跑 ~1317 个新样本，说明之前已有 ~5323 条 resumed 结果。

**范围重叠**：
- v3 (全量) 与 shard2/3/4 有重叠，需要后续去重
- shard2 (7680-9784) 与 shard4 (9100-9784) 也有重叠

**全量覆盖 ETA**：
- 0-6200：已被 v3 完成 ✓
- 6200-7680：v3 (~idx 6646) 和 shard3 (~idx 6600) 都在跑，瓶颈 ~**2h10m**
- 7680-9100：shard2 在跑 (~idx 8719)，~**46min** 完成这段
- 9100-9784：shard4 最快，~**47min** 完成

**整体 ETA：~2h10m**（瓶颈在 shard3 的 6200-7680 段）

### 健康状态
- 无 OOM 风险（21GB/32GB，余量充足）
- 4 GPU 利用率均匀 88-89%，速度一致 ~8.3 samples/min
- shard4 running_acc=69.3%，状态正常
- 无异常，全部正常推进

---
