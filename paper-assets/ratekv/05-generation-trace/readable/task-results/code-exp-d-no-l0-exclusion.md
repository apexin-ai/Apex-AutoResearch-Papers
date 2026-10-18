# code exp d no l0 exclusion

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_d_no_l0_exclusion_20260514T002131_result.json`
- **Structured JSON:** [`dfb51a0a73fed30cb066.json`](../../sessions/df/dfb51a0a73fed30cb066.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_d 完成，**conclusion = success**。

**关键结果：**

| | exp_c (L0 excluded) | exp_d (L0 NOT excluded) |
|---|---|---|
| L0 分配 | 8bit (手动排除) | 8bit (**solver 自动选择**) |
| Bit 分布 | 8:4, 4:100, 2:8 | 8:4, 4:100, 2:8 |
| PPL | 11.23 | 11.23 |
| Memory | 0.2500 | 0.2500 |

分配完全一致——solver 在没有任何 L0 手动约束的情况下，自动将 L0 的 4 个 head 保持在 8bit，2-bit 全部分配给了 L1-L4 的 head。

**Paper narrative 意义：** profiler 的 distortion 信号足以让 solver 自动发现 Layer 0 sensitivity，`l0_exclude_2bit` 约束是冗余的。可以 claim "the solver automatically discovers layer-level sensitivity without manual intervention"。

---
