# analysis per relation 1 7b llama

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_relation_1_7b_llama_20260519T115920_result.json`
- **Structured JSON:** [`5710f5c1de10ee6d19a0.json`](../../sessions/57/5710f5c1de10ee6d19a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到服务器：

**1.7B Qwen (SFT → RSFT)**
- micro-F1: 0.4945 → 0.5290 (+3.45pp)
- 89 个高频关系中 55 个改善，30 个退化
- 最大收益：screenwriter (+0.172), conflict (+0.133), notable work (+0.127)
- 最大退化：founded by (-0.186), participant of (-0.166), cast member (-0.109)
- 平均改善 +0.053，平均退化 -0.047

**LLaMA-8B (SFT → RSFT)**
- micro-F1: 0.5514 → 0.5839 (+3.25pp)
- 89 个高频关系中 57 个改善，26 个退化
- 最大收益：operator (+0.305), participant of (+0.163), mother/screenwriter (+0.114)
- 最大退化：genre (-0.301), chairperson (-0.267), capital of (-0.152)
- 平均改善 +0.052，平均退化 -0.061
- LLaMA 的 hallucinated relations (0 gold, FP only) 有 25 种，显著多于 1.7B 的 6 种

输出文件：
- `/root/autodl-tmp/freige/scripts/analysis/results/per_relation_1_7b.txt` / `.csv`
- `/root/autodl-tmp/freige/scripts/analysis/results/per_relation_llama.txt` / `.csv`

---
