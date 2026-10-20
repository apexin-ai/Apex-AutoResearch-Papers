# ssh training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check_20260512T222000_result.json`
- **Structured JSON:** [`1fc95705e0af116bb093.json`](../../sessions/1f/1fc95705e0af116bb093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

grep 返回码 1 = 无匹配，即两个实验都没有 error/exception/oom/killed。

## 训练进度汇总

### 实验 1: repo-level-cwm-v9 (seetacloud-westd-4x5090)

| 指标 | 值 |
|------|-----|
| **进程状态** | 存活，PID 95806，已运行 36m36s |
| **RSS** | 5.2 GB |
| **当前进度** | **139 / 6633 steps (2.1%)** |
| **训练速度** | ~8.0 s/step |
| **已记录 loss** | 2 条（logging_steps=50 推测） |
| **Checkpoint** | 1 个已保存 (checkpoint-100) |
| **异常** | 无 error/exception/OOM |
| **Eval 耗时** | 每 100 steps 触发一次，9335 样本约 12 分钟 |
| **tqdm 预估训练时间** | ~14.6h（纯训练，不含 eval） |
| **Eval 开销估算** | 还剩 ~65 次 eval × 12min ≈ 13h |
| **总剩余时间估算** | **~27h**（远超预估 20h，eval 开销是主因） |

最近 loss 趋势：step 100 触发了 eval + checkpoint 保存后继续训练，当前稳定推进中。

### 实验 2: repo-level-cls-v4 (home-1x5090)

| 指标 | 值 |
|------|-----|
| **进程状态** | 存活，PID 2885139，已运行 25m07s |
| **RSS** | 1.8 MB（bash wrapper，实际 python 是子进程） |
| **当前进度** | **192 / 6633 steps (2.9%)** |
| **训练速度** | ~6.5 s/step |
| **已记录 loss** | 3 条 |
| **Loss 变化** | step 50: **80.21** → step 150: **1.36**（大幅收敛，正常） |
| **Checkpoint** | 0 个（首次 save 在 step 200，即将触发） |
| **异常** | 无 error/exception/OOM |
| **tqdm 预估训练时间** | ~12h（纯训练） |
| **Eval 开销估算** | 首次 eval 尚未发生（step 200 触发），总计 ~33 次 |
| **总剩余时间估算** | **~12h 训练 + eval 时间待观察** |

### 关键发现

1. **两个实验均正常运行，无异常信号。**
2. **CWM v9 的总时间可能远超 20h 预估**——eval 每 100 steps 跑一次（9335 samples，~12min/次），共 66 次 eval 累计约 13h 开销。如果 eval 频率不需要这么高，考虑增大 `eval_steps` 以加速训练。
3. **CLS v4 的 loss 收敛良好**，从 80.2 降到 1.36。首个 checkpoint 即将在 step 200 保存。
4. CLS v4 在单 5090 上每步反而比 CWM 在 4x5090 上更快（6.5s vs 8.0s），可能是 CWM 序列更长或有多卡通信开销。

---
