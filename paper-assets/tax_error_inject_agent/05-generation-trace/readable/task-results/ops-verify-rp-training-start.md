# ops verify rp training start

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-rp-training-start_20260516T021908_result.json`
- **Structured JSON:** [`35a77cb7b5ed1b139875.json`](../../sessions/35/35a77cb7b5ed1b139875.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部 **RUNNING**，状态正常。

| 训练 | PID | GPU | 显存占用 | GPU 利用率 | 进度 | 速度 | 运行时间 |
|------|-----|-----|---------|-----------|------|------|---------|
| v4-taxei-rp-s42 | 222969 | cuda:0 | 32013/32607 MiB | 99% | 48/5415 | ~2.6s/it | 2m36s |
| v4-taxei-rp-s0 | 223049 | cuda:1 | 27761/32607 MiB | 78% | 45/5415 | ~2.5s/it | 2m34s |
| v4-taxei-rp-s123 | 223254 | cuda:2 | 27047/32607 MiB | 99% | 45/5415 | ~2.8s/it | 2m32s |
| v4-taxei-rp-s1 | 224231 | cuda:3 | 26777/32607 MiB | 99% | 11/5415 | ~2.5s/it | 1m07s |

所有进程存活，日志持续输出训练迭代，无 OOM 或错误。s1 启动略晚约 1.5 分钟，但已正常训练。预计每个 run 总训练时间约 3.5-4 小时。

---
