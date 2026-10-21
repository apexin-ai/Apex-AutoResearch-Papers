# code r19w2 k30 40 50 injection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19w2_k30_40_50_injection_20260523T170454_result.json`
- **Structured JSON:** [`adc93f08d97a0b80e813.json`](../../sessions/ad/adc93f08d97a0b80e813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Merged CSV saved to `summary_by_k_full.csv`.

## 结果汇报

### k=30,40,50 各 contamination_p 下的 ΔFPR（non-target subjects）

| k | p=0.1 | p=0.3 | p=0.5 |
|---|-------|-------|-------|
| 30 | 0.026±0.006 | 0.180±0.021 | 0.362±0.026 |
| 40 | 0.041±0.023 | 0.254±0.067 | 0.406±0.054 |
| 50 | 0.056±0.027 | 0.303±0.064 | 0.458±0.053 |

### 关键发现

**ΔFPR 随 k 单调递增** — 在 p=0.5 下，ΔFPR 从 k=1 的 0.002 → k=10 的 0.069 → k=20 的 0.167 → k=30 的 0.362 → k=50 的 0.458。趋势完全符合预期：matching variable 被越多 contaminated subjects 污染，non-target 的 false positive 率越高。

**k=50, p=0.5 时 ΔFPR = 0.458** — 远超 0.05 阈值。non-target subjects 的 FPR 从 baseline 的 ~0.31 飙升到 0.77，matching variable 已完全失效。

**即使 p=0.1（轻度 contamination），k=50 的 ΔFPR 也达到 0.056** — 刚超过 0.05 threshold，说明 88% subject 覆盖率下即使 10% 的 contamination 也足以让 matching variable 不可靠。

**ΔTPR 在高 k 时反而下降** — k=30/p=0.5 的 ΔTPR 只有 0.159（对比 k=1/p=0.5 的 0.518），因为 matching variable 本身被污染后降低了 target subject 上的检测灵敏度。k=50/p=0.5 回升到 0.439，可能是因为极端注入量使得信号仍然压过噪声。

---
