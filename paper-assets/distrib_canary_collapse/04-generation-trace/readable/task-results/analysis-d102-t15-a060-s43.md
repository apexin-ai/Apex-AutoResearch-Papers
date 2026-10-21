# analysis d102 t15 a060 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t15-a060-s43_20260523T200453_result.json`
- **Structured JSON:** [`43f45ab053da698bd599.json`](../../sessions/43/43f45ab053da698bd599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 分析完成。

**scale_14b_t15_a060_s43_fp32 结果：**

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG (FDR) | 6/8 | 3/8 |
| DiffXCorr (FDR) | 6/8 | 6/8 |
| Threshold Onset | 8/8 | — |
| TY Granger | 3/8 | — |
| **Robust pairs** | **6/8** | — |

Mauve 对两种 canary 都弱 (1/5 votes)，distinct 指标信号强。PermG reverse 3/8 来自 ece→distinct 的双向耦合。

产出：
- 远程: `results/phase_diagram/t15_a060_s43_fp32_14b/analysis/5method_leadlag.json`
- 本地: `artifacts/D102_14b_t15_a060_s43_fp32.json`
- Registry metrics 已更新
- 分析总结: `artifacts/_project/d102_t15_a060_s43_result_20260523.md`

---
