# ops check redocred rsft r2 exit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_redocred_rsft_r2_exit_20260516T173248_result.json`
- **Structured JSON:** [`8740457a2c8693ab1b7d.json`](../../sessions/87/8740457a2c8693ab1b7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结论：negative** — 进程正常退出，但 RE 指标极差。

| 指标 | 值 | 说明 |
|------|----|------|
| F1 | 0.0025 | 几乎为零 (baseline Ign-F1=0.3659) |
| Ign-F1 | 0.0026 | 跨数据集迁移完全失败 |
| Evi-F1 | 0.8837 | evidence 提取正常 |
| EDCR | 0.9978 | 格式正常 |
| TP | 19 / 7431 gold | 仅命中 19 个三元组 |

CED-RSFT checkpoint-510 在 Re-DocRED 上的关系抽取能力基本丧失，说明 DocRED RSFT 训练未迁移到 Re-DocRED 标注体系。Cron 已不存在（可能已被清理），registry 已更新为 DONE/negative。

---
