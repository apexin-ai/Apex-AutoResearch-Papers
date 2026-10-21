# code post hoc retrieval baseline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post_hoc_retrieval_baseline_20260517T125425_result.json`
- **Structured JSON:** [`8e7a34142e24cad43089.json`](../../sessions/8e/8e7a34142e24cad43089.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出

**脚本**: `/root/autodl-tmp/freige/eval/post_hoc_retrieval.py`
**结果目录**: `/root/autodl-tmp/eval_results/post_hoc_bm25/`

## 评估结果对比

| Method | Rel-F1 | Evi-F1_joint | EDCR |
|---|---|---|---|
| **Post-hoc BM25 (entity, k=2)** | 0.4876 | 0.3473 | 0.7664 |
| Post-hoc BM25 (entity, k=3) | 0.4876 | 0.2989 | 0.8256 |
| Post-hoc BM25 (entity, oracle-k) | 0.4876 | 0.3834 | 0.7334 |
| Post-hoc BM25 (ent+rel, k=2) | 0.4876 | 0.3420 | 0.7712 |
| SFT (jointly trained) | 0.4049 | 0.3147 | 0.6982 |
| **RSFT-CED s43** | **0.4601** | **0.3605** | **0.6542** |

## 关键发现

1. **Post-hoc BM25 最优配置 (entity_only, k=2)** evi_f1_joint=0.3473，低于 RSFT 的 0.3605（-1.3pp），且 EDCR 高出 11.2pp（0.7664 vs 0.6542），表明 post-hoc 检索的 evidence 噪声显著更大。

2. **即使给予 oracle-k（已知 gold evidence 数量）**，post-hoc 天花板为 0.3834，仅比 RSFT 高 2.3pp，但 EDCR 仍差 7.9pp。

3. **Entity-only 查询优于 entity+relation**，说明 relation 名称（如 "country"）对 BM25 检索引入噪声。

4. **论文叙事**：Joint generation（RSFT）的优势 = 更低 EDCR（更可信的 evidence）+ 单次推理 + 无需额外检索流水线；post-hoc retrieval 即使 rel_f1 更高，joint evidence 质量仍不如联合训练。

---
