# eval llama3b reeval unified v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama3b_reeval_unified_v2_20260517T144546_result.json`
- **Structured JSON:** [`58871c83129bb8d14a77.json`](../../sessions/58/58871c83129bb8d14a77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，结果如下：

```
Uniform:  PPL=10.53, loss=2.3545, tokens=4,017,316
Adaptive: PPL=10.58, loss=2.3590, tokens=4,017,316
Token 一致性: YES
```

两个 checkpoint 的 token 数**完全一致**（4,017,316），确认此次评估参数完全对齐。脚本使用同一份 tokenized texts（5000 docs），sliding window stride=1024（max_length//2=2048//2），fp16 autocast 硬编码。

结论：Uniform 的 PPL 略优于 Adaptive（10.53 vs 10.58，loss 差 0.0045）。

---
