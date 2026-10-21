# code r15 base instruct temporal dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r15_base_instruct_temporal_dif_20260523T094436_result.json`
- **Structured JSON:** [`04716f11a339fc3ee2d3.json`](../../sessions/04/04716f11a339fc3ee2d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

| | Base-only | Instruct-only | Overall |
|---|---|---|---|
| **N_ref / N_foc** | 861 / 548 | 219 / 259 | 1080 / 807 |
| **C%** | 32.1% | 36.5% | 31.3% |
| **N_DIF_C** | 4018 | 4567 | — |
| **ρ(diff, Δ_MH)** | −0.570 | −0.079 | — |
| **Focal-fav (2024↑)** | 39.9% | 65.6% | — |
| **Ref-fav (2023↑)** | 60.1% | 34.4% | — |

关键发现：

1. **两个子集的 C% 都远超 overall 的 31.3%**，temporal DIF 不是某一类模型独有的——base 和 instruct 都存在严重的测量不稳定性。

2. **方向差异极为显著**：
   - Base 模型：60.1% ref-favoring → 2024 base 模型在 DIF items 上表现更差（ρ=−0.57，难题上尤其明显）
   - Instruct 模型：65.6% focal-favoring → 2024 instruct 模型在 DIF items 上表现更好

3. **ρ 的差异**：Base 的 ρ=−0.57 说明难题上 2023→2024 的退步尤其严重；Instruct 的 ρ≈0 说明 DIF 在各难度水平均匀分布。

输出已保存到 `artifacts/r15_base_instruct_temporal_dif/`。

---
