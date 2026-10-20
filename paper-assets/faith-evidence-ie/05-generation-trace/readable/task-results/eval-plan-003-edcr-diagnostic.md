# eval plan 003 edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_003_edcr_diagnostic_20260515T234255_result.json`
- **Structured JSON:** [`0675e3cc549ed87726e4.json`](../../sessions/06/0675e3cc549ed87726e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_003 不在 registry 中（可能仅在 roadmap 中追踪）。任务完成。

---

## 结果总结

**EDCR Cross-Method Diagnostic Table** 已生成（15 个方法），核心发现：

| 指标对 | Spearman | p-value |
|--------|----------|---------|
| EDCR vs rel_f1 | **-0.9648** | <0.0001 |
| EDCR vs evi_f1 | 0.0022 | 0.9941 |

**诊断结论：**

1. **EDCR 与 rel_f1 近乎完美负相关**（ρ=-0.96）— EDCR 本质上是 rel_f1 的变换，对功能正常方法的排序几乎无额外区分力
2. **EDCR 与 evi_f1 完全无关**（ρ≈0）— EDCR 不测量证据质量
3. **EDCR 的独特诊断价值**：识别病理性模型（GRPO QLoRA kl001/lr5e6），这些模型 evi_f1 高但 rel_f1 极低，说明在疯狂产生 distractor citations
4. **所有方法 EDCR 均 >0.63**，没有达到"relation-focused"（<0.6）的级别

**修正的数据问题：**
- `dpo_ced_1ep/` 是坏 eval（缺 sft_adapter），使用 `dpo_ced_1ep_fixed/` (rel_f1=0.4034, EDCR=0.7139)
- `rsft_flat_nli_s43/` 同样是坏 eval，reeval 运行中
- CED-reranker 无 predictions.json 文件（无法计算 EDCR）

**输出位置：**
- 服务器：`/root/autodl-tmp/eval_results/edcr_diagnostic_table.{md,csv}`
- Artifact: `art_20260515_3bd92e`

---
