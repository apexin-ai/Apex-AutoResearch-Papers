# check mistral heuristic k value

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mistral_heuristic_k_value_20260514T093421_result.json`
- **Structured JSON:** [`31766c98050bfd388454.json`](../../sessions/31/31766c98050bfd388454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**Mistral 在 `l0_heuristic_corrected` 中用的 `k=16`。**

代码证据（`run_l0_heuristic_corrected.py` 第 ~38 行）：
```python
"Mistral-7B-v0.3": {
    ...
    "k": 16,
    "mckp_ppl": 7.323,
},
```

这个 `k` 值直接用于 `build_l0_random_allocation` 和 `build_naive_heuristic_allocation`，控制有多少个 non-L0 head 被分配 2-bit。代码中还有 budget 断言验证 `expected_budget == 0.25`，说明 k=16 是满足 budget=0.25 约束的正确值（对于 Mistral 的 32 layers × 8 kv_heads = 256 total heads）。

结果文件也确认实验成功运行并产出了 Mistral 的完整结果（MCKP PPL=7.323, naive=7.481, L0-random mean=7.560）。

**与 Table 1 的冲突**：如果 Table 1 Mistral MCKP 用的是 k=4 (PPL=7.16)，那和 heuristic 实验的 k=16 不在同一对比条件下。需要统一 k 值才能公平对比。

---
