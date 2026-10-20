# code plan 003 edcr pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_edcr_pipeline_20260515T210707_result.json`
- **Structured JSON:** [`82a2f7639b3abe7e883a.json`](../../sessions/82/82a2f7639b3abe7e883a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果验证正确：
- GRPO QLoRA lr5e6 ckpt100: rel_f1=0.0147, evi_f1=0.8502, edcr=0.9869 — 与 registry 记录的 0.0138/0.8500/0.9900 高度吻合（微小差异来自 prediction 文件差异）
- DPO-CED 1ep 和 RSFT-flatNLI s43 的 eval 还在运行中，跳过正常

脚本位于 `/root/autodl-tmp/freige/scripts/edcr_diagnostic.py`，功能完整：
- `--auto-discover`: 扫描已有 eval 结果
- `--methods NAME:PATH`: 手动指定方法
- 输出 `edcr_diagnostic.json`（汇总 JSON，含 per-relation-type 和 per-document EDCR 分布）
- 输出 `edcr_diagnostic.tex`（LaTeX table + per-relation table）
- EDCR 逻辑复用 `DocREDEvaluator.compute_edcr` + `_triple_key`

EDCR diagnostic 的关键发现：GRPO QLoRA 系列的 EDCR 极高（0.85-0.99），median 接近 1.0，证实 catastrophic forgetting 导致模型几乎所有 evidence citation 都是 distractor。相反 RSFT-CED 和 GRPO bf16 的 EDCR 显著低于 SFT baseline（0.63-0.66 vs 0.71），验证了 Claim 4。

---
