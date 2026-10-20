# ops check redocred rsft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_redocred_rsft_eval_r2_20260516T173222_result.json`
- **Structured JSON:** [`b5a9959485f03a319f40.json`](../../sessions/b5/b5a9959485f03a319f40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_007_redocred_rsft_eval_r2**: 进程正常完成，conclusion=**negative**。

结果摘要：

| 指标 | 值 |
|------|------|
| Ign-F1 | 0.0026 |
| F1 | 0.0025 |
| Evi-F1 | 0.8837 |
| EDCR | 0.9978 |
| Format OK | 489/493 (99.2%) |
| field_compliance | 0% |
| evidence_format | 0% |
| TP | 19 / 7431 gold |
| Truncated | 117/493 |

CED-RSFT adapter (`rsft_output_ced_s43/checkpoint-510`) 在 Re-DocRED 上关系抽取几乎完全失败（Ign-F1=0.0026 vs SFT baseline 0.3659）。field_compliance_rate=0 说明模型输出格式与 Re-DocRED 的 gold schema 不匹配，7931 条预测中只有 19 条命中。跨数据集迁移未成功。

Cron 已清除，registry 已更新为 DONE/negative。

---
