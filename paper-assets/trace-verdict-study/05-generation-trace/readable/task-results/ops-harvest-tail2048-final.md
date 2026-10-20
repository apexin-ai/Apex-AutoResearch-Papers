# ops harvest tail2048 final

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_tail2048_final_20260517T171726_result.json`
- **Structured JSON:** [`9859048bac8f5208f20a.json`](../../sessions/98/9859048bac8f5208f20a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，eval_results.json 包含完整 metrics 和 CI。

## 结果汇总

| Metric | **Qwen-1.5B tail-2048** | **DeepSeek-6.7B tail-2048** |
|---|---|---|
| **Accuracy** | **0.9790** [0.9706, 0.9874] | **0.9496** [0.9370, 0.9622] |
| Lift over majority | +0.2639 | +0.2345 |
| n_test | 1190 | 1190 |
| **Pass Precision** | 0.9758 [0.9655, 0.9862] | 0.9692 [0.9571, 0.9809] |
| **Pass Recall** | 0.9953 [0.9904, 0.9989] | 0.9600 [0.9466, 0.9729] |
| **Pass F1** | 0.9855 [0.9794, 0.9912] | 0.9646 [0.9554, 0.9733] |
| **Fail Precision** | 0.9876 [0.9746, 0.9970] | 0.9020 [0.8719, 0.9333] |
| **Fail Recall** | 0.9381 [0.9110, 0.9646] | 0.9233 [0.8934, 0.9518] |
| **Fail F1** | 0.9622 [0.9460, 0.9768] | 0.9125 [0.8909, 0.9341] |

**关键发现**：Qwen-1.5B 以 97.9% accuracy 显著优于 DeepSeek-6.7B 的 95.0%（CI 不重叠）。小模型在这个任务上反而更强，所有 precision/recall/F1 指标均全面领先。GPU 当前空闲，无运行进程。

---
