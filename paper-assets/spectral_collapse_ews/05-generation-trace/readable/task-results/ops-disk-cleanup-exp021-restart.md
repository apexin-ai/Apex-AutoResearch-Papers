# ops disk cleanup exp021 restart

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-exp021-restart_20260524T045058_result.json`
- **Structured JSON:** [`6d76fe05b71881a0c664.json`](../../sessions/6d/6d76fe05b71881a0c664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 磁盘空间

| 时间 | 使用 | 可用 | 使用率 |
|------|------|------|--------|
| 删除前 | 250G | 2.7MB | 100% |
| 删除后 | 117G | 134G | 47% |

### 删除内容

1. **`checkpoints_phase1/`** — 117G，Pythia-410M 旧实验 checkpoints（7 个实验目录）
2. **`checkpoints_410m/gen_0~gen_10`** — ~17G，Pythia-410M 旧 checkpoint 残留
3. **`checkpoints_410m/exp_021/seed42/gen_2`** — 174MB，磁盘满时的损坏 checkpoint

### exp_020 状态

- PID 783957，GPU 0（26.4G VRAM，96% util）
- Gen 8/10 采样中（32960/50000 samples），运行正常

### exp_021 状态

- PID 858050，GPU 1（22.7G VRAM，100% util）
- **从 gen_1 断点恢复**（`--start_gen 2`），已加载 2 条已有结果
- 当前 Gen 2/3 训练中（r=1.0 纯真实数据），还需完成 Gen 2 和 Gen 3
- tmux session: `exp021`
- 日志: `/root/autodl-tmp/spectral_collapse_ews/logs/exp021_restart.log`

### nvidia-smi 确认

- GPU 0: exp_020 (PID 783957) — 26422MiB
- GPU 1: exp_021 (PID 858050) — 22728MiB

---
