# ops launch 7b s123 cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-7b-s123-cuda3_20260518T133331_result.json`
- **Structured JSON:** [`461b280bdef0b2faa612.json`](../../sessions/46/461b280bdef0b2faa612.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，汇报：

| 项目 | 状态 |
|---|---|
| **PID 28640** | 已终止（确认死亡） |
| **新进程 PID** | 31158（python 子进程，父 bash PID 31153） |
| **cuda:3 显存** | 28,646 MiB / 97,887 MiB |
| **LoRA 配置** | r=16, alpha=32 ✓ |
| **训练样本** | 50,000 |

**全卡状态：**

| GPU | 显存占用 | GPU-Util | 进程 PID |
|---|---|---|---|
| cuda:0 | 69,204 MiB | 73% | 30306 |
| cuda:1 | 17,704 MiB | 90% | 25326 |
| cuda:2 | 64,768 MiB | 85% | 28900 |
| cuda:3 | 28,646 MiB | 88% | 31158 |

四卡全部在跑，cuda:3 的 7B d000 s123 训练已正常上 GPU。

---
