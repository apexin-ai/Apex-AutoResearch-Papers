# ops retrain pipeline exec

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_retrain-pipeline-exec_20260521T180729_result.json`
- **Structured JSON:** [`ea2de495ceefec9a8693.json`](../../sessions/ea/ea2de495ceefec9a8693.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Object CRM training 正常运行：
- **GPU 0**: 557 MiB, 10% utilization
- **Epoch 1, batch 50/1950**: loss = 0.009459
- 1950 batches/epoch (62K train samples / 32 batch_size)

## 最终输出总结

### 1. rsync 文件数
- Object: 387 (bjb1-32546) + 64 (bjb2-40593) partial files → 已全部在 bjb1-18228
- Spatial: 84 (bjb2-28827 current) + 18 (bjb1-18228 local shard 6) partial files

### 2. Merge manifest n_samples
| Benchmark | **n_samples** | 预期 | 占比 |
|-----------|-------------|------|------|
| **Object** | **69,303** | 72,500 | **95.6%** ✓ |
| **Spatial** | **待 merge** | 60,250 | **~84% 当前可用** ⚠️ |

**Spatial 阻塞**: bjb2-28827 上 6 个 spatial precompute shards 仍在运行（7300/8608, ~50 min 剩余）。完成后需要：
1. 再次 `scp -3 bjb2-28827:spatial/*.pt` → bjb1-18228
2. Merge: `python merge_precompute_cache.py --cache_dir .../spatial/ --num_shards 7 --total_samples 60250 --allow_partial --concat`
3. 启动 spatial CRM training（GPU 1）

### 3. CRM training PID
- **Object**: PID **800111** (GPU 0) ✅ 运行中
- **Spatial**: 待启动

### 4. 初始 loss
- **Object epoch 1 batch 50**: **loss = 0.009459**

---
