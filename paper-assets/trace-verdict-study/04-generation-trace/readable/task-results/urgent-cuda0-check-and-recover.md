# urgent cuda0 check and recover

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cuda0_check_and_recover_20260515T231135_result.json`
- **Structured JSON:** [`b2e80ba89390b709f4be.json`](../../sessions/b2/b2e80ba89390b709f4be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。当前状态总结：

**deepseek_full_trace_seed42_v3** — DONE
- accuracy=79.16%, fail_f1=0.637, pass_f1=0.854, lift=+7.6pp over majority baseline
- Registry metrics 已更新

**GPU 利用率正常**
- cuda:0: 89% util, 92GB/98GB — full_trace_512tok_seed42 训练中
- cuda:1: 99% util, 62GB/98GB — full_trace_256tok_seed42 训练中（v3 eval 已结束，GPU 1 内存已释放）

---
