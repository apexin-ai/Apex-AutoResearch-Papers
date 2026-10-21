# gpu check westd 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_westd-35807_20260529T044848_result.json`
- **Structured JSON:** [`1c316e9a91d299bdc08f.json`](../../sessions/1c/1c316e9a91d299bdc08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807 服务器状态汇总

### GPU 状态
| GPU | 型号 | 显存使用 | 利用率 | 温度 | 功耗 |
|-----|------|---------|--------|------|------|
| 0 | RTX PRO 6000 (98GB) | 19.1GB / 98GB | 100% | 63°C | 464W/600W |

**GPU 1-3 空闲**（nvidia-smi 未显示）。

### 活跃训练
**train_pi05_lora_baseline_s3_v2** — 正在跑
- PID: 93400（父进程 93395）
- 命令: `train_pi05_lora_baseline.py --scene object_pudding --seed 3 --gpu 0 --batch_size 32 --num_train_steps 30000`
- 当前进度: **step 3603 / 30000 (12%)**，运行 1h13m
- 速度: **~1.20 s/it**（稳定）
- Loss: ~0.12，lr=2.46e-05
- 预计剩余: ~8h48m（总约 10h）
- 日志: `/tmp/train_lora_s3_restart.log`

### eval_pi05_a1_best_s0_l005
**已完成**。结果文件 `eval_pi05_a1_best_s0_l005.json` 最后修改时间 May 28 07:37，不再有对应进程。

### tmux
`tmux ls` 被 read-only 限制，无法执行。但从进程列表看，训练是通过 nohup 启动的，非 tmux。

### 磁盘
| 挂载点 | 总计 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 350G | 282G | 69G | **81%** |

### 最近 eval 结果（/root/autodl-tmp/eval_results/）
最新: `eval_oracle_pi05_lora_s0.json` — May 29 09:33

### 最近训练日志（/root/colliforce-vla/logs/）
最新: `eval_s0_l01_30k_seed7.log` — May 27 18:23（2天前，无新日志产出）

---
