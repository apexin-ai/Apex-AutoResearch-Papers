# analyze w8 qwen docred ft semantic only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w8_qwen_docred_ft_semantic_only_20260516T161925_result.json`
- **Structured JSON:** [`ad63279d899657224780.json`](../../sessions/ad/ad63279d899657224780.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总结果：

## w8_qwen_docred_ft_semantic_only — ✓ SUCCESS

| 指标 | 值 | 对比 grammar_only | 对比 unconstrained baseline |
|------|------|---|---|
| **DR_pct** | **0.21%** | 0.61% | 0.76% |
| E_F1 | 82.15 | 82.19 | — |
| R_F1 | 40.89 | 40.85 | — |
| ET_pct | 0% | — | — |
| RV_pct | 0.23% | ��� | — |
| CF_pct | 0.27% | — | ��� |
| parse_fail | 7.52% | 7.01% | — |

**关键发现**：
- DR 从 baseline 0.76% → 0.21%，降幅 **72%**，超出预期（假设 0.3-0.5%）
- 与 SciERC 上 semantic_only 降 DR 68% 的模式高度一致
- F1 指标与 grammar_only 几乎完全一致（E_F1 差 0.04pp, R_F1 差 0.04pp），说明 semantic 约束不损害抽取质量
- semantic_only 在 DR 降幅上显著优于 grammar_only（0.21% vs 0.61%），确认 **semantic 层是 DR 降低的主要贡献者**

---
