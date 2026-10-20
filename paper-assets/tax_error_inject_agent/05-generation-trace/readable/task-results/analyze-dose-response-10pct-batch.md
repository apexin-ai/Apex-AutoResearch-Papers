# analyze dose response 10pct batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_dose-response-10pct-batch_20260515T185522_result.json`
- **Structured JSON:** [`1492114153269599165d.json`](../../sessions/14/1492114153269599165d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部更新为 DONE。

```
exp_id                        | train_loss | final_loss | final_token_acc | steps | runtime_sec | checkpoint
------------------------------|------------|------------|-----------------|-------|-------------|----------
v4-taxei-fixed-inject10-s1    | 0.4225     | 0.3013     | 0.8947          | 1635  | 3469        | .../v0-20260516-015427/checkpoint-1635
v4-random-fixed-inject10-s0   | 0.4227     | 0.2760     | 0.9067          | 1635  | 3531        | .../v0-20260516-014835/checkpoint-1635
v4-taxei-fixed-inject10-s123  | 0.4234     | 0.3097     | 0.8882          | 1635  | 3497        | .../v0-20260516-014833/checkpoint-1635
```

三者 train_loss 高度一致（~0.423），与此前 s0 的 0.4238 对齐。random-s0 的 final_token_acc 略高（0.9067），taxei-s123 略低（0.8882），属正常 seed 间波动。

---
