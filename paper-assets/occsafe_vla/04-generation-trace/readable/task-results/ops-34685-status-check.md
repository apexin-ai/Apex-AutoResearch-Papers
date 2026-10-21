# ops 34685 status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-status-check_20260526T223938_result.json`
- **Structured JSON:** [`daab390d02eb96a837cf.json`](../../sessions/da/daab390d02eb96a837cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告 — westd-34685

### 1. GPU 状态

| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | **空闲** | 0MiB / 97887MiB | 0% |
| cuda:1 | **空闲** | 0MiB / 97887MiB | 0% |
| cuda:2 | **空闲** | 0MiB / 97887MiB | 0% |
| cuda:3 | **占用** | 62203MiB / 97887MiB | 99% |

GPU 型号：NVIDIA RTX PRO 6000 Blackwell (96GB)，CUDA 13.0

---

### 2. vanilla_v2_s1 — **已完成 ✅**

- `50000_chkpt` 目录存在且完整（model safetensors × 4、action_head、proprio_projector、lora_adapter、tokenizer 等全部到位），时间戳 May 27 06:31-06:32
- `40000_chkpt` 也保存了
- 运行目录 `openvla-7b+...--vanilla_v2_s1/` 仅有 `dataset_statistics.json`（正常，latest checkpoint 不保存完整模型）
- 没有找到这个实验的训练日志文件（不在 `/root/runs/` 下，可能是通过 tmux 手动启动的），但 **50000_chkpt 的完整存在已充分证明训练跑完了 50005 步**

---

### 3. detach_ln_s4 — **已失败 ❌**

- PID 510461 已不存在
- exit 文件：`1|2026-05-26T22:33:05Z`（退出码 1）
- **失败原因：wandb 未登录**。日志显示 `wandb.errors.errors.UsageError: No API key configured. Use wandb login to log in.`
- checkpoint 目录为空（0 个文件），说明还没开始训练就挂了
- 需要重新提交，启动命令中加 `WANDB_MODE=disabled` 或先 `wandb login`

---

### 4. cutoff_25k_s1_v2 — **运行中 🟢**

- PID 453581 存活，在 cuda:3 上跑
- 当前进度：**49043/50005**（98%），速度 ~1.09 it/s
- 预计剩余 ~15 分钟完成

---

### 5. eval 脚本

`/root/occsafe_vla/openvla-oft/vla-scripts/` 下的文件：
- `finetune.py`
- `deploy.py`
- **`evaluate_safelibero.py`** ← eval 脚本
- `merge_lora_weights_and_save.py`
- `extern/`

---

### 6. 磁盘空间

`/root/autodl-tmp/`: 200G used / 350G total，**151G 可用 (58%)**，充足。

---

### 总结

| 项目 | 状态 |
|------|------|
| **可用 GPU** | **cuda:0, cuda:1, cuda:2** 空闲，可立即用于 eval |
| vanilla_v2_s1 | 完成，50000_chkpt 就绪 |
| detach_ln_s4 | 失败（wandb 未配置），需重新提交 |
| cutoff_25k_s1_v2 | ~15 分钟后完成 |
| eval 脚本 | `evaluate_safelibero.py` |

---
