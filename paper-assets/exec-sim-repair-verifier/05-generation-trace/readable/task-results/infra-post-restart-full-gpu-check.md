# infra post restart full gpu check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-full-gpu-check_20260518T163243_result.json`
- **Structured JSON:** [`2bfc3a2c966078154f68.json`](../../sessions/2b/2bfc3a2c966078154f68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 服务器 | GPU | 任务 | PID | 存活 | 进度 | running_acc | GPU util% | VRAM (MiB) | 已运行 | ETA |
|--------|-----|------|-----|------|------|-------------|-----------|------------|--------|-----|
| seetacloud | 0 | CLS v5 retrain | 698033 | ✅ | 4894/6315 steps (77%) | eval_loss=0.159 @ep2 | 99% | 24861/32607 | 13h45m | ~4.0h |
| seetacloud | 1 | CWM s42 best @seq4096 | 662946 | ✅ | 6971/9784 (71.3%) | 56.6% (3943/6971) | 51% | 17699/32607 | 1d 0h13m | ~9.8h |
| seetacloud | 2 | CWM s42 e3 @seq2048 | 734440 | ✅ | 891/9784 (9.1%) | 65.9% (587/891) | 55% | 15765/32607 | 2h43m | ~27.2h |
| seetacloud | 3 | CWM s123 e2 @seq4096 | 668680 | ✅ | 6543/9784 (66.9%) | 61.6% (4032/6543) | 46% | 17699/32607 | 23h02m | ~11.4h |
| home | 0 | CWM s42 e2 @seq2048 | 4141145 | ✅ | 841/9784 (8.6%) | 66.9% (563/841) | 86% | 15575/32607 | 1h38m | ~17.4h |

**5/5 进程全部存活，服务器重启未受影响。**

关键观察：
- seq2048 的两个 eval (GPU 2, home) 刚启动不久，running_acc 都偏高 (~66%)，样本量还小
- seq4096 的两个 eval (GPU 1, GPU 3) 已跑 2/3+，s123 的 acc (61.6%) 明显高于 s42 best (56.6%)
- CLS v5 训练 77% 完成，约 4 小时后结束

---
