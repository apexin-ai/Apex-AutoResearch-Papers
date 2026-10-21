# ops fix save checkpoint and restart m64

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-save-checkpoint-and-restart-m64_20260521T090742_result.json`
- **Structured JSON:** [`d690967e4c70f7cdf83d.json`](../../sessions/d6/d690967e4c70f7cdf83d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M64v6 训练已启动！step=0, loss=16.2283, save_every=10000。

汇总全部完成情况：

## 产出

### 1. save_checkpoint 修改 (diff)

**`train_openvla_smart_compress.py`:**
- `save_checkpoint()` 新增 `final=False, max_keep_ckpt=3` 参数
- `final=False` (step checkpoint): 只保存 `compressor_state_dict` — 仅含 `"compressor"` 关键字的参数 (~500MB)
- `final=True` (graceful exit / 训练结束): 保存完整 `model_state_dict` + `checkpoint.pt` (~19GB)
- 自动清理旧 step checkpoint，只保留最新 3 个
- Resume 逻辑兼容两种格式 (`compressor_state_dict` / `model_state_dict`)
- Step checkpoint 保存后打印文件大小 (MB)

**`eval_openvla_smart_compress.py`:**
- 加载兼容：自动检测 `compressor_state_dict` vs `model_state_dict`

### 2. M64v6 状态
- **PID**: 59671 (tmux session `train_m64v6`)
- **GPU**: cuda:3 (27GB occupied)
- **wandb run**: `openvla_sc_m64_seed42_v6` (offline mode)
- **save_every**: 10000 (已从 50000 改为 10000)
- **训练已开始**: step=0, loss=16.2283

### 3. 服务器脚本同步
- **westd-41074**: 已修改 ✓ (M64v6 使用新代码)
- **westd-27271**: 已修改 ✓ (M32 运行中进程仍用旧代码，需重启才生效)
- M96 (westd-41074): 旧代码运行中，不重启

### 4. 磁盘空间
- westd-41074: 75GB 可用（新 step checkpoint ~500MB × 3 = 1.5GB，充裕）

---
