# verify greedy constraint impl

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_greedy_constraint_impl_20260514T070945_result.json`
- **Structured JSON:** [`afbd191ccf4f069c51a6.json`](../../sessions/af/afbd191ccf4f069c51a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Implementation Review
- **Type: step-by-step** (正确)
- **Code: `run_greedy_constrained.py:solve_greedy_constrained`**
- 每次迭代在选择降级前检查 `count_2bit >= max_2bit`，命中则跳过 2-bit 选项。非 post-hoc。

## Delta 修正
原报告 delta=0.0012 是 artifact——代码硬编码了 `ref_mckp_ppl = 11.23`（四舍五入），实际 MCKP PPL = 11.2312 = Greedy PPL。**真实 delta = 0.0000**。

## Per-Head Allocation Comparison

| Model | Heads | Match | Diffs | Greedy Dist | MCKP Dist | Delta |
|-------|-------|-------|-------|-------------|-----------|-------|
| Qwen2.5-7B | 112 | 112/112 | 0 | 0.170428 | 0.170428 | 0.0 |
| Llama-3.1-8B | 256 | 256/256 | 0 | -0.571735 | -0.571735 | 0.0 |
| Mistral-7B-v0.3 | 256 | 255/256 | 1 | 0.000000 | 0.000000 | 0.0 |

Mistral 唯一差异：head 31,5 (greedy=8bit, mckp=4bit)。原因：该 head 4-bit 和 8-bit distortion 都是 0.0，greedy 逐级降到 8-bit 后预算已满停止，MCKP 可直接跳到 4-bit。对 distortion 和 PPL 无影响。

**结论：cardinality constraint 将解空间收窄到 greedy ≡ MCKP。三个模型验证了 solver-invariance。PPL eval 不需要——allocation 本身已一致。**

---
