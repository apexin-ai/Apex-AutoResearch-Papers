# ops westd41074 disk emergency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-disk-emergency_20260520T031058_result.json`
- **Structured JSON:** [`492f5681ba32032e5b7a.json`](../../sessions/49/492f5681ba32032e5b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务完成报告

### 已完成操作：

1. **checkpoint_step10000.pt 已删除** — 释放 ~19 GB
   - 路径：`/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m128/checkpoint_step10000.pt`
   - 额外清理：M=96/M=64 旧 checkpoint（checkpoint_step459.pt, checkpoint_step536.pt, checkpoint.pt × 2）也已删除

2. **M=96 重启** — 实际 Python PID=**66050**, save_every=50000 ✓
   - 命令：`python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml`
   - GPU 2, 从头训练

3. **M=64 重启** — 实际 Python PID=**66389**, save_every=50000 ✓
   - 命令：`python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml`
   - GPU 3, 从头训练

4. **M=128 (PID=26118) 未动** — GPU 0 正常运行中

5. **磁盘状态**：250G 总量，147G 使用，104G 可用（59%）
   - 首次 checkpoint 将在 step 50000 保存（~20 GB/file × 2 = 40 GB），104G 余量充足

### 注意事项：
- M=96/M=64 当前仍在 "Computing action statistics" 阶段（273K samples 两进程并行扫描，I/O 竞争导致较慢，预计总共 ~20-30 分钟）。完成后会开始出 training step log 并占用 GPU 显存。
- 可稍后用 `tail /tmp/train_m96.log` 和 `nvidia-smi` 验证训练正式开始。

---
