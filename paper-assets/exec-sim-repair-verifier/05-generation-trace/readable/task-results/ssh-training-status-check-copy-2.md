# ssh training status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-status-check_20260521T130728_result.json`
- **Structured JSON:** [`f7793ebf66753fd7ce6f.json`](../../sessions/f7/f7793ebf66753fd7ce6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## deepseek-cwm-repo-s123-train-v3
- 进程状态: **ALIVE** (PID 28200, 运行 8h43m)
- 当前 step: **8062 / 12627 (63.8%)**
- 当前 epoch: 1.90
- 当前 loss: **0.0001 ~ 0.0009**（极低，收敛良好）
- 速度: ~8.1 s/it
- 预估完成: **~10h 后 → 明天 07:10 左右**
- Checkpoint: 仅 checkpoint-4209（resume 起点，无新 checkpoint 产出）
- 备注: 无异常

## qwen3-8b-cwm-repo-s456-train-v3
- 进程状态: **ALIVE** (PID 4561, 运行 15h28m)
- 当前 step: **5400 / 6633 (81.4%)**
- 当前 epoch: 2.44
- 当前 loss: **0.0050**，eval_loss: 0.4949
- 速度: ~12.0 s/it
- 预估完成: **~4h 后 → 今晚 01:10 左右**
- Checkpoint: checkpoint-300, checkpoint-5000, checkpoint-5100, checkpoint-5200, checkpoint-5300
- 备注: 无异常

## qwen3-8b-cwm-repo-s123-train-v4
- 进程状态: **ALIVE** (PID 4271, 运行 15h28m)
- 当前 step: **5300 / 6633 (79.9%)**
- 当前 epoch: 2.40
- 当前 loss: **0.0070**，eval_loss: 0.5076
- 速度: ~12.2 s/it
- 预估完成: **~4.5h 后 → 今晚 01:30 左右**
- Checkpoint: checkpoint-300, checkpoint-5000, checkpoint-5100, checkpoint-5200, checkpoint-5300
- 备注: 无异常

## deepseek-cwm-repo-s456-train-v2
- 进程状态: **DEAD — 训练已成功完成** ✓
- 最终 step: **12627 / 12627 (100%)**，epoch 3.0
- 最终 train_loss: **0.02127**，eval_loss: 5.2837
- 总训练时间: 27h32m55s
- Checkpoint:
  - `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/best` (67 MB)
  - `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-12627` (195 MB)
  - `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-8418`
- 备注: **GPU 1 已被新进程占用** — PID 56657（运行 19 分钟），正在对 checkpoint-8418 跑 `eval_repo_cwm.py` 推理评估

---

**GPU 汇总：**

| GPU | 温度 | 功耗 | 显存 | 利用率 | 进程 |
|-----|------|------|------|--------|------|
| 0 | 74°C | 444/575W | 30.5/32.6 GB | 93% | qwen s123 (PID 4271) |
| 1 | 61°C | 322/575W | 31.6/32.6 GB | 84% | **eval** deepseek s456 (PID 56657) |
| 2 | 72°C | 502/575W | 20.5/32.6 GB | 99% | deepseek s123 (PID 28200) |
| 3 | 78°C | 572/575W | 25.6/32.6 GB | 98% | qwen s456 (PID 4561) |

**关键发现：**
1. deepseek-cwm-repo-s456-train-v2 已于 20:46 完成，registry 状态需更新为 COMPLETED
2. GPU 1 上有人（或自动脚本）启动了 checkpoint-8418 的 eval，未在 registry 中登记
3. GPU 3 功耗接近上限 (572/575W)，温度 78°C 偏高但尚可
4. 两个 Qwen 实验预计今晚凌晨完成，deepseek s123 预计明早完成

---
