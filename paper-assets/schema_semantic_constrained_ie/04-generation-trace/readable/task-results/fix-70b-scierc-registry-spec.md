# fix 70b scierc registry spec

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_70b_scierc_registry_spec_20260518T132510_result.json`
- **Structured JSON:** [`7b6856bb1a69391382a1.json`](../../sessions/7b/7b6856bb1a69391382a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**data_path**：Registry 原记录 `data/scierc/test.jsonl` 不存在。实际数据文件是 `data/processed_data/test.json`（100 个文档，JSONL 格式）。代码按句子拆分后产生 551 个样本，与日志中 `Samples: 551` 一致。data_count=551 是正确的。

**实验状态**：两个实验均已跑完（551/551 success, 0 fail），进程已退出。

**日志迁移**：
- `/tmp/70b_unconstrained.log` → `logs/70b_scierc_unconstrained.log` (81,815 bytes)
- `/tmp/70b_constrained.log` → `logs/70b_scierc_constrained.log` (81,507 bytes)
- 原 `/tmp/` 文件保留未删

**Registry 更新**（两个实验均已修正）：
- `spec.data_path`: `data/scierc/test.jsonl` → `data/processed_data/test.json`
- `spec.log_path`: `/tmp/70b_*.log` → `logs/70b_scierc_*.log`
- 其余 spec 字段已完整恢复

注意：两个实验 status 仍为 RUNNING，实际已完成，后续需要跑 violation check 再转 DONE。

---
