# analysis 14b rsft s43 test eval pair

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b-rsft-s43-test-eval-pair_20260523T165542_result.json`
- **Structured JSON:** [`6e46e2b3312852ec9fa0.json`](../../sessions/6e/6e46e2b3312852ec9fa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**14B s43 evidence tax = +0.08pp**（with_evi 0.3767 vs no_evi 0.3775）

**14B 2-seed 汇总：**
- s42: +0.77pp, s43: +0.08pp
- Mean: **+0.43 ± 0.49pp**
- 方向一致（no-evi 略优），但幅度极小，evidence 输出对 RE 性能的负面影响可忽略

两个实验均 conclusion=success。报告已写入 `artifacts/test_eval_14b_rsft_s43_pair/analysis.md`。

---
