# audit abstract crosscheck final

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_abstract-crosscheck-final_20260523T191605_result.json`
- **Structured JSON:** [`96a0f219188ab3267c0e.json`](../../sessions/96/96a0f219188ab3267c0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/final_audit_w1_abstract.md`。

**核心发现**：

**3 个不一致需修正**：
1. 1.7B 方差压缩倍数 — experiments 写 31×，appendix 表写 32.6×（rounded vs unrounded std 计算差异）
2. DREEAM Evi-F1 — experiments 文中写 54.01%，encoder_comparison 表写 54.15（差 0.14pp）
3. §5.5 EDCR — 文中写 0.654，Table 1 写 0.6487，且无任何单 seed 精确匹配 0.654

**4 个数字缺少表格支撑**（无法交叉验证）：Method B 51.52、CED reranking 48.64/81.88、post-hoc BM25 34.7/0.766。

其余 50+ 个数字全部验证一致，精度统一（仅 §5.5 存在轻微 dp 不统一）。

---
