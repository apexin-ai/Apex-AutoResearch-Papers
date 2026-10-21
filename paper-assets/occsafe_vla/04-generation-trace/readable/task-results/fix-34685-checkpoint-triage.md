# fix 34685 checkpoint triage

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685_checkpoint_triage_20260528T015744_result.json`
- **Structured JSON:** [`0bca6bec8de8120d0abd.json`](../../sessions/0b/0bca6bec8de8120d0abd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 实验状态

| 实验 | 服务器 | GPU | 状态 | 当前步数 | 预计完成 (UTC) |
|------|--------|-----|------|----------|-------------|
| detach_ln_v2_s3 | westd-34685 | cuda:3 | **运行中** | ~33700/50005 | ~06:12 |
| full_occ_ln_v2_s3 | westd-34685 | cuda:2 | **运行中** | ~33800/50005 | ~06:08 |
| detach_ln_v2_s2 | westd-34685 | cuda:0 | **已恢复** | 从25000恢复，刚启动 | 取决于stop逻辑 |
| vanilla_object_s1 | westd-10894 | cuda:0 | **运行中** | ~31200/50005 | ~06:45 |
| detach_ln_v2_s4 | westd-10894 | cuda:1 | **运行中** | ~12690/50005 | ~11:30 (紧张!) |

### 2. Checkpoint 目录内容

**detach_ln_v2_s2** (`/root/autodl-tmp/checkpoints/detach_ln_v2_s2/`):
- 20000_chkpt — 完整
- 25000_chkpt — 完整（~15GB merged model），用作恢复起点
- 30000_chkpt — **不完整**（仅 365MB adapter/head，缺少 merged model safetensors）

**detach_ln_v2_s3**: 25000_chkpt, 30000_chkpt — 均完整
**full_occ_ln_v2_s3**: 25000_chkpt, 30000_chkpt — 均完整
**detach_ln_v2_s4**: 5000_chkpt, 10000_chkpt — 均完整

### 3. 崩溃根因 & 恢复操作

**根因**: 服务器上的 `cleanup_daemon.sh` 每30分钟运行 `cleanup_checkpoints.sh`，只保留每个实验最新的2个 checkpoint。detach_ln_v2_s2 之前从 15000_chkpt resume，cleanup 后来删了 15000_chkpt。当训练在 step 30000 保存时，`save_training_checkpoint` 尝试从 `vla_path`（指向已删除的 15000_chkpt）加载 base model 做 LoRA merge → OSError 崩溃。

**已执行恢复操作**:
1. **kill cleanup daemon** (PID 39450) — 防止 25000_chkpt 被清理导致同样崩溃
2. **从 25000_chkpt resume** — 新 PID **45380** (GPU 0, 62194 MiB)，训练已开始

**注意**: 恢复后 batch_idx 从 0 重计，[AUX] 显示 step=0。但 checkpoint 保存使用 global_step (resume_step + batch_idx)，所以 checkpoint 命名会正确。

### 4. 磁盘空间

| 服务器 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| westd-34685 | 350G | 168G | 183G | 48% |
| westd-10894 | 250G | 116G | 135G | 47% |

### 5. 风险提示

- **detach_ln_v2_s4** 在 10894 上预计 ~11:30 UTC 完成，距 DDL 仅 30 分钟余量
- cleanup daemon 已杀，短期内不会有磁盘清理。磁盘空间充足，不会有问题
- 未删除任何文件

---
