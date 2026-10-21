# code scp scatter and degen

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scp_scatter_and_degen_20260518T224855_result.json`
- **Structured JSON:** [`0a1ce46e6f7355568ede.json`](../../sessions/0a/0a1ce46e6f7355568ede.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### Part A: Scatter Plot
本地文件已就位：`artifacts/fig_degeneracy_lp_scatter_v2.pdf` (23704 bytes，与远端一致)

### Part B: 4 个 degen% 值

| 实验 | n_degen / n_total | degen% |
|------|-------------------|--------|
| rank=8 SciERC | 38 / 529 | **7.18%** |
| N=32 SciERC | 38 / 529 | **7.18%** |
| N=16 SciERC seed42 | 64 / 529 | **12.10%** |
| FewNERD N=8 seed42 | 4479 / 32565 | **13.75%** |

结果已保存到远端 `output/supplement_degen_results.json`。

注意：N=16 SciERC seed42 使用的是 `exp001_n16_seed42`（旧版本），其 degen% (12.10%) 与 scatter_v2_data.json 中 base SciERC seed42 的 17.77%（来自 `exp_001_seed42_v2`）不同，是不同的推理运行。

---
