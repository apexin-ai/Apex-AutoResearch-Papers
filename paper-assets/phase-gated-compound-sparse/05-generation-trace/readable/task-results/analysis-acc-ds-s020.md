# analysis acc ds s020

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s020_20260515T211728_result.json`
- **Structured JSON:** [`6ab30238bb1fa370f8f4.json`](../../sessions/6a/6ab30238bb1fa370f8f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
ds_s020_acc = 0.26
ds_s020_correct = 13
ds_s020_total = 50
ds_s020_delta_vs_dense = -0.26
null_count = 31
null_rate = 0.62
trunc_count = 32
trunc_rate = 0.64
wrong_count = 6
wrong_rate = 0.12
heads_pruned = 140
total_time_s = 1560
```

**Conclusion: success**

剂量曲线严格单调递减：

| condition | accuracy | Δ vs dense |
|-----------|----------|------------|
| dense     | 0.52     | —          |
| s015      | 0.34     | -0.18      |
| **s020**  | **0.26** | **-0.26**  |
| s025      | (pending)|            |
| s030      | 0.10     | -0.42      |

s020 (0.26) 精确落在 s015 (0.34) 和 s030 (0.10) 之间，支持 dose-dependent degradation 假说。

注意点：null_rate 高达 62%（31/50 题模型未能提取答案，其中 32 题触发 2048 token 截断），说明 s020 剪枝强度下模型推理链路已严重受损，大量问题陷入无效循环直到截断。仅 6 题给出了错误答案（wrong_rate=12%），多数失败模式是「无输出」而非「错误输出」。

W&B：日志中无 wandb run ID。

---
