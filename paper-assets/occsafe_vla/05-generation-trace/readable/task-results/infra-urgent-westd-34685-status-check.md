# infra urgent westd 34685 status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-westd-34685-status-check_20260521T070131_result.json`
- **Structured JSON:** [`059fca91a55332445680.json`](../../sessions/05/059fca91a55332445680.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals are running successfully — models loaded, rollouts in progress.

---

## 完整状态报告

### 1. finetune 进程
| Seed | 状态 | 详情 |
|------|------|------|
| **s0** | DEAD | kill 脚本于 06:57:27 UTC 杀死 (PID 76998)，50000_chkpt 已保存 |
| **s1** | ALIVE | PID 80898，GPU 1 (99%, 62GB)，从 17500 resume，当前 20000_chkpt |
| **s2** | DEAD | kill 脚本于 06:58:02 UTC 杀死 (PID 78171)，50000_chkpt 已保存 |

### 2-3. Checkpoints
| Seed | 最新 checkpoint | 时间 |
|------|-----------------|------|
| s0 | **50000_chkpt** ✓ | May 21 14:58 |
| s1 | 20000_chkpt (训练中) | May 21 13:44 |
| s2 | **50000_chkpt** ✓ | May 21 14:58 |

### 4-5. Eval trigger
- `monitor_and_eval_occ.sh` — 12:39 失败（PID 已过期）
- `eval_occ_salvage.sh` — 14:57 检测到 50000_chkpt 并触发 eval，但 **eval 失败**：50000_chkpt 是轻量保存（只有 LoRA adapter + heads），缺少 `config.json` 和 base model safetensors

### 6. Kill 脚本
正常工作：检测到 50000_chkpt 后成功杀死 s0/s2

### 7. GPU 状态
| GPU | Util | Memory | 用途 |
|-----|------|--------|------|
| 0 | 0% → eval | 0 → loading | **已启动 s0 eval** (PID 88639) |
| 1 | 99% | 62209 MiB | s1 训练中 |
| 2 | 0% → eval | 0 → loading | **已启动 s2 eval** (PID 90003) |
| 3 | 100% | 0 MiB | 异常（100% util 但 0 MiB） |

### 8. Eval 修复与重启
**根因**: 50000_chkpt 是轻量 checkpoint（仅含 LoRA adapter、action_head、occ_head、proprio_projector），不包含 config.json 和 model safetensors。

**修复**: 从 47500_chkpt 符号链接了 9 个缺失文件（config.json、generation_config.json、4 个 model safetensors 等）到 50000_chkpt，s0 和 s2 各做一次。

**当前状态**: 两个 eval 均已成功加载模型，正在跑 rollouts：
- s0: Task 0, rollout 7/20, ~5s/rollout
- s2: Task 0, rollout 1/20, ~9s/rollout

### 预计完成时间
10 tasks × 20 rollouts ≈ **20-30 分钟**后出结果，日志在 `/root/runs/occsafe_vla/eval_s0.log` 和 `eval_s2.log`。

---
