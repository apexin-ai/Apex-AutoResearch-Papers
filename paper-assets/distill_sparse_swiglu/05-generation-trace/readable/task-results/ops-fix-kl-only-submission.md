# ops fix kl only submission

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_kl_only_submission_20260515T172402_result.json`
- **Structured JSON:** [`19b6f64676a81d740ba2.json`](../../sessions/19/19b6f64676a81d740ba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：训练正常运行中，不需要修复

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| cuda:0 | 100% | 67,569 / 97,887 MiB |
| cuda:1 | 100% | 67,569 / 97,887 MiB |

### 进程状态
| 实验 | PID | GPU | seed | CPU% | 启动时间 |
|------|-----|-----|------|------|---------|
| kl_only_s0 | 88764 | cuda:0 | 0 | 102% | 01:19 |
| kl_only_s1 | 88843 | cuda:1 | 1 | 100% | 01:19 |

### 训练进度
两个实验均在 **Step 120/1000**，KL loss 持续下降，sparsity 在 0.48~0.50 附近波动（target=0.5），lambda 自适应调节正常。

**kl_only_s0** (seed=0): step 120, kl_norm=0.3906, sparsity=0.477
**kl_only_s1** (seed=1): step 120, kl_norm=0.4453, sparsity=0.477

### 结论
进程在跑，GPU 满载。`submit_training_job` 报 "duplicate session" 是正确行为——tmux 会话存在且训练活跃。**不要杀进程。** Main Agent 需要手动注册 cron 监控这两个实验。

---
