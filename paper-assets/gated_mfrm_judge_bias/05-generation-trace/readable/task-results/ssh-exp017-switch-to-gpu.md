# ssh exp017 switch to gpu

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_switch_to_gpu_20260523T070256_result.json`
- **Structured JSON:** [`349f298d6eff476988fe.json`](../../sessions/34/349f298d6eff476988fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU模式启动成功。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| CPU进程 | 已kill |
| 脚本修改 | `JAX_PLATFORMS="cpu"` + `XLA_FLAGS` → `CUDA_VISIBLE_DEVICES="0"` |
| 已有结果 | 7条有效（去重后），793条待跑，断点续跑 |
| GPU占用 | PID 318082，GPU 0，显存 73524 MiB |
| 并行链 | 单GPU只有1个device，4条chain串行执行（预期行为，单链GPU仍远快于CPU） |

---
