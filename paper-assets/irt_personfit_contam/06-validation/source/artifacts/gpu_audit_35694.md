# GPU 审计报告 — westd-35694
**时间**: 2026-05-21 ~23:30

## 1. GPU 占用情况

| GPU | PID | 进程 | VRAM | GPU Util | 状态 |
|-----|-----|------|------|----------|------|
| 0 | 143378 | `train.py --condition clean_s8` (Llama clean s8) | 20871/97887 MiB (21%) | 84% | ALIVE, 训练中 |
| 1 | 143458 | `train.py --condition clean_s9` (Llama clean s9) | 28807/97887 MiB (29%) | 92% | ALIVE, 训练中 |
| 2 | 141866 | `train_grpo.py --gpu 2` (GRPO) | 10913/97887 MiB (11%) | 82% | ALIVE, 训练中 |
| 3 | 143599 | `train.py --condition clean_s10` (Llama clean s10) | 25977/97887 MiB (27%) | 96% | ALIVE, 训练中 |

## 2. 旧进程存活状态

| PID | 原任务 | 状态 |
|-----|--------|------|
| 97791 | GRPO (旧) | **DEAD** |
| 99807 | Llama clean s8 (旧) | **DEAD** |
| 99214 | Llama clean s7 | **DEAD** |
| 98622 | s5 eval zombie | **DEAD** |
| 96745 | s6 train zombie | **DEAD** |

所有旧进程已自然退出，无 zombie 残留。

## 3. GRPO 进度

- **Step**: 469/3000 (15.6%)
- **Epoch**: ~0.014
- **速度**: ~3.4s/step
- **已运行**: ~23 min
- **ETA**: ~2h25m (预计完成 ~02:00)
- **Reward**: 波动中 (近几步 -0.025 ~ 0.775)
- **Entropy**: ~1.7
- **日志**: `/root/runs/irt_personfit_contam/exp-post-rl-v3.log`

## 4. Llama clean 训练状态

| Seed | 训练 | 进度 | Eval | 结果 |
|------|------|------|------|------|
| s2 | 完成 | — | 完成 | acc=0.5954, lz*=-0.182, theta=-0.630 |
| s3 | 完成 | — | 完成 | acc=0.5943, lz*=-1.084, theta=-0.640 |
| s4 | 完成 | — | 完成 | acc=0.5923, lz*=0.021, theta=-0.644 |
| s5 | 完成 | — | 完成 | acc=0.5965, lz*=1.732, theta=-0.630 |
| s6 | 完成 | — | 完成 | acc=0.6010, lz*=2.847, theta=-0.603 |
| s7 | 完成 | 939/939 | 完成 | acc=0.5929, lz*=-0.401, theta=-0.636 |
| s8 | 训练中 | 380/939 (40%) | 未开始 | — |
| s9 | 训练中 | 379/939 (40%) | 未开始 | — |
| s10 | 训练中 | 380/939 (40%) | 未开始 | — |

s8/s9/s10 预计 ~11 min 后完成（剩余 ~560 步 x ~1.1s/step）。

## 5. Qwen clean s10

- **训练**: 完成（有 adapter_model.safetensors + checkpoint-313/626/939）
- **Eval**: 完成
- **结果**: acc=0.6758, lz*=8.149, theta=-0.116

## 6. 空闲 GPU

**无空闲 GPU** — 4 卡全部在用。

s8/s9/s10 训练约 10 min 后完成，届时 GPU 0/1/3 将释放。

## 7. Zombie 进程

**无需 kill** — 所有旧 PID (97791, 99807, 99214, 98622, 96745) 均已自然退出。

## 8. 磁盘

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / | 30G | 1.4G | 29G | 5% |
| /root/autodl-tmp | 250G | 84G | 167G | 34% |

磁盘空间充裕。
