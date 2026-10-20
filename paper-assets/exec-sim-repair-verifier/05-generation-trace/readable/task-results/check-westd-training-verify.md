# check westd training verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-training-verify_20260514T060847_result.json`
- **Structured JSON:** [`7934a32e3e25aabf3389.json`](../../sessions/79/7934a32e3e25aabf3389.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 块 GPU 状态汇总

| GPU | 任务 | PID | 显存 | 利用率 | 进度 | 速度 | 预估 ETA |
|-----|------|-----|------|--------|------|------|----------|
| **0** | CWM seed123 eval | 195531 | 13.0/32.6 GB | 87% | 2864/9784 (29.3%) | ~52s/8样本 | ~**5.3h** (约 19:20) |
| **1** | CWM v12 eval | 195668 | 13.0/32.6 GB | 87% | 2888/9784 (29.5%) | ~51s/8样本 | ~**5.2h** (约 19:18) |
| **2** | 8B CWM 训练 | 210573 | 31.5/32.6 GB | 99% | 72/6633 (1.1%) | ~12.2s/step | ~**22.2h** (明天 ~12:15) |
| **3** | 8B CLS seed123 训练 | 210657 | 23.6/32.6 GB | 98% | 113/6633 (1.7%) | ~8.4s/step | ~**15.2h** (明天 ~05:15) |

### 关键观察

**Eval (GPU 0/1):**
- 两个 CWM eval 都在正常推进，running_acc 均稳定在 ~57.5-57.6%
- 从 09:03 启动至今已跑 5h，完成约 29%，预计今晚 19:00-19:30 完成

**训练 (GPU 2/3):**
- 两个 8B 训练都已开始 step 输出，正常跑起来了
- 数据集划分：train=70,748 / val=9,335，与预期一致
- CWM 截断率 4.5%（train）/ 20.2%（val），CLS 截断率 3.8%（train）/ 20.2%（val）
- GPU 2 (CWM) 比 GPU 3 (CLS) 慢很多：12.2s/step vs 8.4s/step，显存也更满（31.5 vs 23.6 GB）
- Loss：CLS step50=233.27 → step100=16.45，下降正常；CWM 日志中 step50 显示 loss 但还未到 step100

**注意**：CWM 训练 val 截断率 20.2% 较高，可能影响最终验证指标。

---
