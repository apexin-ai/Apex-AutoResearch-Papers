# fix batch64 config memory

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batch64_config_memory_20260517T072814_result.json`
- **Structured JSON:** [`5fb60f164e95148e8951.json`](../../sessions/5f/5fb60f164e95148e8951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成的修改：**
1. **配置文件** `libero_fullft_batch64.yaml`：`num_workers: 1`, `save_every: 2000`, `pin_memory: false`
2. **训练脚本** `train.py`：
   - `pin_memory` 改为从配置读取（`train_cfg.get("pin_memory", True)`）
   - 每 500 步打印 `[MEM]` 内存使用信息
3. **Kill 旧进程** PID 8723 → **重启训练** PID 14927（GPU 1, tmux session `libero_fullft_batch64_v2`）

**验证结果：**
- step=0 已打印 `[MEM] total=1007.5GB avail=956.3GB used=51.2GB`（系统内存充足）
- loss=1.5052, grad=11.21 正常
- GPU 2/3 上的 k=0.7/k=0.3 训练未受影响

---
