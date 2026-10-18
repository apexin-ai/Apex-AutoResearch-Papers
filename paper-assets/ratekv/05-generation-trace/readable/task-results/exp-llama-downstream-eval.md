# exp llama downstream eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama_downstream_eval_20260515T171016_result.json`
- **Structured JSON:** [`f57792ca7187eb448478.json`](../../sessions/f5/f57792ca7187eb448478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果已注册。

## 结果汇总

**Llama-3.1-8B Downstream Eval (0-shot, k=2, budget=0.25)**

MCKP allocation: 253×4bit + 1×8bit + 2×2bit

| Task | Baseline | Uniform 4-bit | MCKP k=2 | MCKP−Uni (pts) |
|------|----------|---------------|----------|----------------|
| ARC-C | 51.88 | 52.56 | 51.79 | **−0.77** |
| HellaSwag | 60.73 | 60.24 | 60.21 | **−0.03** |
| PIQA | 79.22 | 78.73 | 78.67 | **−0.06** |
| WinoGrande | 73.88 | 72.61 | 73.09 | **+0.48** |

**对比已有论文数据 (k=8)**：

| Task | k=8 delta | k=2 delta |
|------|-----------|-----------|
| ARC-C | −2.7 | −0.77 |
| HellaSwag | −0.1 | −0.03 |
| PIQA | −0.7 | −0.06 |
| WinoGrande | −0.2 | +0.48 |

k=2 对 downstream task 的退化显著小于 k=8，WinoGrande 甚至优于 uniform baseline。这符合预期——k=2 只允许 2 个 2-bit head，allocation 更保守（253/256 heads 仍为 4-bit），因此对 task accuracy 影响更小。

---
