# research semisynthetic pipeline explore

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_semisynthetic-pipeline-explore_20260524T152903_result.json`
- **Structured JSON:** [`d6f2eeff0f8aea70c02e.json`](../../sessions/d6/d6f2eeff0f8aea70c02e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/semisynthetic_pipeline_report.md`。

核心发现：
- **MC 模拟不需要原始文本**，只需要 per-subgroup 的 FPR/FNR 和子组权重（这些从 LLM annotation pilot 获得）
- 每个 LLM 对应一个独立的 `run_*_hetero_tau.py` 脚本，CM 参数硬编码在文件顶部
- 所有核心函数（DGP、CM 估计、校正、聚合）可直接复用，**唯一需要新写的是 AG News 的 LLM 标注 pilot 和子组定义**
- 现有框架只支持 binary Z（2×2 CM），AG News 4-class 需要 binarize（最小改动方案）

---
