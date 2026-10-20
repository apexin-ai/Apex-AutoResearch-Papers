# ssh d065 tcr full

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d065_tcr_full_20260519T113441_result.json`
- **Structured JSON:** [`6e99e40fb5e365ce4514.json`](../../sessions/6e/6e99e40fb5e365ce4514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TCR 全量实验完成。10 个 RE 配置全部跑完，结果汇总：

**CF 消除：所有配置 100%**

**核心发现：**

| | SciERC (7 rels) | DocRED (96 rels) |
|---|---|---|
| ZS CF baseline | 0.67-9.75% | 11.61-23.71% |
| LoRA CF baseline | 0.46-1.19% | 0.36-0.42% |
| Fundamental conflict (ZS) | 0-2% | 13.5-22.8% |
| Fundamental conflict (LoRA) | 0% | ~12% |
| E-F1 cost (ZS) | -0.013 to +0.001 | -0.034 to -0.060 |
| E-F1 cost (LoRA) | -0.002 to -0.008 | -0.002 |

- DocRED fundamental conflict 率比 SciERC 高 6-12x，与 schema 复杂度直接相关
- LoRA 模型 TCR 成本极低（E-F1 Δ < 0.002）
- 70B 模型仍有 11.61% CF，schema 约束瓶颈不随模型规模消失
- WikiEvents 跳过（EE 格式需重写约束满足逻辑）
- 修补了 `tcr_resolver.py` 的 `load_schema` 以兼容 DocRED dict 格式 schema

报告：`/root/schema_semantic_constrained_ie/d065_tcr_full_results.md`，已注册 artifact。

---
