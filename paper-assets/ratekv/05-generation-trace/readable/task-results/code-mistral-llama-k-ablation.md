# code mistral llama k ablation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_llama_k_ablation_20260514T071221_result.json`
- **Structured JSON:** [`9bde320cef3797ee1dfa.json`](../../sessions/9b/9bde320cef3797ee1dfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 sweep 全部完成。汇总结果：

---

## K Ablation Sweep 结果

### Mistral-7B-v0.3 (256 KV heads, budget=0.25)

| k | PPL | 2bit | 4bit | 8bit | 16bit | mem |
|---|-----|------|------|------|-------|-----|
| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.2480 |
| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.2490 |
| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.2500 |
| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.2480 |
| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.2500 |
| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.2500 |

**PPL 随 k 单调递增。** 2-bit compounding 效应严重——每多 1 个 2-bit head 约增加 ~0.011 PPL。即使 best k=4 也比 uniform 差 0.034。对 Mistral，constrained MCKP 在 4x budget 下无法 beat uniform。

### Llama-3.1-8B (256 KV heads, budget=0.25)

| k | PPL | 2bit | 4bit | 8bit | 16bit | mem |
|---|-----|------|------|------|-------|-----|
| 4-18 (all) | **8.4498** | 2 | 253 | 1 | 0 | 0.2500 |
| uniform 4-bit | 8.469 | 0 | 256 | 0 | 0 | 0.2500 |

**所有 k 值结果完全相同。** MCKP solver 自然只选 2 个 head 到 2-bit（constraint 从不 binding）。Llama 在 4x 下 MCKP 比 uniform 好 0.019 PPL（marginal）。

### 论文叙事
- Qwen (112 heads): 最优 k=8 (7.1%)，U 形曲线，constrained MCKP 大幅优于 uniform
- Mistral (256 heads): k 越小越好（单调），constraint 无法挽救 2-bit compounding
- Llama (256 heads): 天然 k=2，constraint 不起作用，MCKP 收益 marginal

---
