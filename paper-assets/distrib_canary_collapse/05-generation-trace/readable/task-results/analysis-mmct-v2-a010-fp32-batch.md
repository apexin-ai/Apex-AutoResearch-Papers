# analysis mmct v2 a010 fp32 batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_v2_a010_fp32_batch_20260519T093436_result.json`
- **Structured JSON:** [`6adaa92eec1b25fb4156.json`](../../sessions/6a/6adaa92eec1b25fb4156.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**MMCT v2 α=0.10 fp32 双 seed 结果：**

| Mode | s42_fp32 | s43_fp32 | 跨 seed 一致 |
|------|----------|----------|-------------|
| uniform_forward | 0/8 | 0/8 | YES |
| weighted_global_forward | 0/8 | 0/8 | YES |
| weighted_pair_forward | 2/8 | 4/8 | NO |

**权威值：0/8**（uniform/wglobal 模式，双 seed 一致）

wpair 的 2-4/8 跨 seed 不稳定，根因是 3 个 null seed 导致 per-pair FPR 权重方差大。与 pre-D080 旧 a010_s42 的 wpair 1/8 比，uniform/wglobal 结果无变化。

产出：
- Artifact: `artifacts/mmct_v2_a010_fp32_results.md`
- JSON: `westd-19828:artifacts/mmct_results/mmct_v2_a010_fp32.json`
- Unified data: `westd-19828:artifacts/mmct_results/unified_data/a010_s42_fp32.json` / `a010_s43_fp32.json`

---
