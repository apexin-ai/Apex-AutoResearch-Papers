# check westd full status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-full-status_20260514T150645_result.json`
- **Structured JSON:** [`ade90a8b3c8fba0269c7.json`](../../sessions/ad/ade90a8b3c8fba0269c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 进程 | PID | 显存 | GPU利用率 | 状态 |
|-----|------|-----|------|-----------|------|
| cuda:0 | CWM seed123 eval | 195531 | 13.0/32.6 GB | 84% | 运行中 |
| cuda:1 | CWM v12 eval | 195668 | 13.0/32.6 GB | 82% | 运行中 |
| cuda:2 | CWM 8B train | 245775 | 21.2/32.6 GB | 96% | 运行中 |
| cuda:3 | CLS 8B s123 train | 248041 | 26.8/32.6 GB | 64% | 运行中 |

## CWM Eval 进度
- **seed123**: 7904/9784 完成 (80.8%), running_acc=59.1%, ~6.5 sec/sample → 剩余 1880 样本, 预计还需 **~3.4 小时** (~02:30 完成)
- **v12**: 8016/9784 完成 (81.9%), running_acc=57.8%, ~6.5 sec/sample → 剩余 1768 样本, 预计还需 **~3.2 小时** (~02:15 完成)

## 8B 训练进度
- **CWM 8B** (PID 245775, cuda:2): step **1300/6633** (19.6%), 从 ckpt-1200 resume 于 22:28
  - 当前正在跑 val eval (7059/9335)，eval 完成后继续训练
  - 训练速度 ~12 sec/step，eval 每轮约 19 min（9335 val samples）
  - 剩余 5333 步纯训练 ≈ 17.8h + eval 开销 → 预计还需 **~20-24 小时**
  - loss: 0.54 (step 1300), epoch 0.59

- **CLS 8B s123** (PID 248041, cuda:3): step **2529/6633** (38.1%), 从 ckpt-2400 resume 于 22:46
  - 训练速度 ~8 sec/step
  - 剩余 4104 步 ≈ **~9.1 小时** (纯训练，不含 eval 开销)
  - loss: 0.73 (step 2500), epoch 1.13

## CLS 8B s42 Checkpoint 路径

有两组 s42 checkpoints，均无活跃训练进程：

| 路径 | 最新 checkpoint | 每个大小 | 最后更新 |
|------|----------------|---------|---------|
| `/root/autodl-tmp/checkpoints_repo_cls_8b/` | checkpoint-3000 | 176M | May 14 05:30 |
| `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` | checkpoint-600 | 176M | May 14 08:50 |

- `checkpoints_repo_cls_8b` 更完整（到 step 3000），推荐 scp 这个
- 可 scp 到 home: **可以**。单个 checkpoint 176M，5 个共 ~880M。数据盘剩余 118GB，网络带宽不是瓶颈
- 注意：两组 s42 训练均已停止（无进程），最远只到 3000/6633（未训完）

---
