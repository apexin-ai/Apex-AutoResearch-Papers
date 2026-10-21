# ssh urgent status check westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-status-check-westd_20260513T110204_result.json`
- **Structured JSON:** [`c1662af3222bd4e40167.json`](../../sessions/c1/c1662af3222bd4e40167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 分配全景

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 78% | 24.9/31.8 GB | CLS seed123 |
| 1 | 97% | 16.3/31.8 GB | CWM seed123 |
| 2 | 98% | 13.5/31.8 GB | **CWM v11** |
| 3 | 98% | 25.8/31.8 GB | 8B CLS |

### 各实验详情

#### 1. CWM v11 (PID 130026, cuda:2) — 最关键
- **ALIVE**, 运行 2h42m
- **Step 400/6633** (6.0%), 日志显示正在做 eval (8719/9335, 93%)
- eval_loss 趋势持续下降：`0.5039 → 0.3643 → 0.3213 → 0.3066`
- train_loss: `6.64 → 5.48 → 4.98`
- best_checkpoint: `checkpoint-400`, best_metric: `0.3066`
- **未完成**，预估剩余 ~40h（按当前速度 ~14 it/s）

#### 2. CLS seed123 (PID 141198, cuda:0)
- **ALIVE**, 运行 57min
- **Step 310/6633** (4.7%), ~7s/it
- eval_loss@200: `0.0808`
- train_loss: `11.31 → 1.56 → 1.17`（收敛很快）

#### 3. CWM seed123 (PID 142397, cuda:1)
- **ALIVE**, 运行 37min
- **Step 273/6633** (4.1%), ~9.5s/it
- eval_loss@100: `0.5049`（刚过 step 200 的 eval）
- train_loss: `28.67 → 20.43`（还在初期下降中）

#### 4. 8B CLS (PID 140055, cuda:3)
- **ALIVE**, 运行 1h03m
- **Step 273/6633** (4.1%), ~9.5s/it
- eval_loss@200: `0.0767`（比 4B CLS 的 0.0808 更低）
- train_loss: `15.95 → 2.64 → 2.01`

### 关键结论
- **CWM v11 未完成**，6% 进度，loss 稳降中，一切正常
- 4 个实验全部健康运行，无异常
- 8B CLS 的 eval_loss (0.0767) 略优于 4B CLS seed123 (0.0808)，值得关注

---
