# code mistral l0 heuristic supplement

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_l0_heuristic_supplement_20260514T071406_result.json`
- **Structured JSON:** [`ee32278b0deaf4a984f6.json`](../../sessions/ee/ee32278b0deaf4a984f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral 的所有条件已经跑完了。`l0_heuristic_corrected_results.json` 中包含完整结果：

```
Mistral l0_heuristic supplement:
L0-random seed=0: PPL=7.5233
L0-random seed=1: PPL=7.6099
L0-random seed=2: PPL=7.4134
L0-random seed=3: PPL=7.5860
L0-random seed=4: PPL=7.6692
L0-random mean±std: 7.5604 ± 0.0871
Naive positional: PPL=7.4807
MCKP constrained: PPL=7.3231
Uniform 4-bit: PPL=7.1314
Baseline bf16: PPL=7.0351
```

无需补跑，所有 seeds 1-4 和 naive positional 已在结果文件中。

当前 GPU 状态：cuda:0 空闲，cuda:1 被占用（67GB）。

---
