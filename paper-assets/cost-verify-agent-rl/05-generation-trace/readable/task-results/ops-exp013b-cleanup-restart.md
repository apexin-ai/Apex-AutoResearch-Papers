# ops exp013b cleanup restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp013b-cleanup-restart_20260514T082737_result.json`
- **Structured JSON:** [`065fb84795180fd66331.json`](../../sessions/06/065fb84795180fd66331.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果汇报

### 清理前后对比

| 资源 | 清理后状态 |
|------|-----------|
| GPU 0 (RTX PRO 6000) | 0 MiB / 97887 MiB, 0% 利用率 |
| GPU 1 (RTX PRO 6000) | 0 MiB / 97887 MiB, 0% 利用率 |
| CPU RAM | 919 GiB 可用 / 1.0 TiB 总计 |
| 根分区 | 23G 可用 (25% 使用) |
| 数据盘 | 118G 可用 (54% 使用) |

### 清理动作
- 杀掉 1 个训练进程 (PID 263851)
- ray stop + 清理 /tmp/ray* 和 /dev/shm
- tmux 会话已清理
- 残留：仅 tensorboard + jupyter-lab（系统服务）

### val 并发
不需要降。919GB 可用 RAM 远超 20GB 阈值。当前 config 中 val `env_groups: 16` 保持不变。

### Checkpoint & Config 确认
- Checkpoint 存在：`/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/actor/`
- Config 存在且参数正确：
  - `use_kl_loss: True`, `kl_loss_coef: 0.01`
  - `format_penalty: 0`
  - train `env_groups: 8`, `group_size: 16`
  - val `env_groups: 16`, `group_size: 1`

**环境干净，可以重启 exp013b。**

---
