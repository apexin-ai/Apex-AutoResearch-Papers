# ops emergency disk cleanup 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency-disk-cleanup-34685_20260522T072943_result.json`
- **Structured JSON:** [`6c6255dde2d327d37582.json`](../../sessions/6c/6c6255dde2d327d37582.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部恢复完成。汇报：

## 结果

### 1. 磁盘清理
- **释放 284G**（350G → 66G used，285G 可用，19%）
- 删除：occ_s1_fresh 8 个中间 checkpoint (27500-45000)，depth_s0/s1 各 6 个 checkpoint (全部不完整)，cutoff_s1 1 个不完整 checkpoint

### 2. cutoff_s0 存活
- PID 125522，step 3200/50005，~1.08 it/s，正常运行
- `occ_loss=0.0131, action_loss=0.1416`

### 3. 恢复实验（全部从头重跑，save_freq=10000）

| 实验 | GPU | PID | 当前 step | 速度 | 初始 loss |
|------|-----|-----|-----------|------|-----------|
| depth_s0 | cuda:1 | 131535 | ~20 | ~1.08 it/s | depth=0.6663, action=0.7578 |
| depth_s1 | cuda:2 | 131682 | ~21 | ~1.09 it/s | (初始化中) |
| cutoff_s1 | cuda:3 | 131898 | ~20 | ~1.06 it/s | occ=0.2096, action=0.6367 |

### 4. 最终状态
- **nvidia-smi**: 4 GPU 全部 95-99% 利用率，各 ~62G/98G 显存
- **磁盘**: 66G/350G (19%)，充足
- **Registry**: 4 个实验 RUNNING（cutoff_s0 + 3 个新提交）

---
