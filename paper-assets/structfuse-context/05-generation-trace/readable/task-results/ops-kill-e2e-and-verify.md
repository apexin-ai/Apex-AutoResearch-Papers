# ops kill e2e and verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-e2e-and-verify_20260515T204812_result.json`
- **Structured JSON:** [`542075ca299643658a7f.json`](../../sessions/54/542075ca299643658a7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**Kill 确认**：
- PID 94874（E2E eval）已 kill，PID 94869 同时清理
- GPU 0 显存从 ~74 GB → ~62.6 GB，**释放 ~11.5 GB**

**训练进程存活**：
- PID 18427（Qwen dataflow_s43）：存活，CPU 99.6%，运行 4h55m
- PID 61328（SWE-bench retrieval eval）：存活，CPU 105%，运行 2h03m

**GPU 利用率（kill 后）**：
| GPU | 利用率 | 显存使用 / 总量 |
|-----|--------|----------------|
| 0 | 100% | 62,620 / 97,887 MiB |
| 1 | 100% | 54,767 / 97,887 MiB |

**训练进度**（日志最新）：
- 当前在 **step 900**，epoch 1（共 1405 steps/epoch）
- loss 持续下降：0.67→0.07→0.02（step 50→400→900）
- eval@500：val_loss=0.4617, **R@1=0.5495**, R@5=0.9728, R@10=1.0

**eval@1000 尚未到达**，训练正在 step 900，预计很快会触发。trainer_state.json 尚未生成（只有 best checkpoint 目录）。

---
