# code hires mckp reeval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hires_mckp_reeval_20260514T064307_result.json`
- **Structured JSON:** [`a00df562a6c293850cb9.json`](../../sessions/a0/a00df562a6c293850cb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

## 结果汇总

```
=== Hires MCKP Re-evaluation (current eval_ppl.py, bf16) ===
                            新值        旧值         备注
Baseline bf16 PPL:         9.8106      8.819       旧 eval 版本偏低 ~1.0
Constrained MCKP bf16 PPL: 10.9131     9.569       旧 eval 版本偏低 ~1.3
Uniform 4-bit bf16 PPL:   15.4454     15.45(fp16)  几乎一致
Delta (MCKP vs baseline):  +1.1025     +0.750
Delta (MCKP vs uniform):   -4.5323
Token count:               298938
```

**论文 headline 数字**（全部基于当前 eval_ppl.py, bf16, WikiText-2 test, stride=512）：
- MCKP allocation（budget=0.25, {8:4, 4:100, 2:8}）比 baseline 仅增加 **+1.10 PPL**
- 比 uniform 4-bit 改善 **4.53 PPL**（10.91 vs 15.45）
- Baseline 9.8106 与其他实验完全一致，数字可比

---
