# infra disk migration

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk_migration_20260520T195817_result.json`
- **Structured JSON:** [`de78ea97a23eeb383cbf.json`](../../sessions/de/de78ea97a23eeb383cbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移报告：

| 项目 | 状态 |
|------|------|
| 根分区 | 41% (13G/30G) — 无变化，因为符号链接已存在，缓存本就在数据盘 |
| 符号链接 | `/root/nlp_variance_gtheory/models/.hf_cache` → `/root/autodl-tmp/.hf_cache` ✓ |
| HF_HOME 持久化 | `export HF_HOME=/root/autodl-tmp/.hf_cache` 已写入 `.bashrc` ✓ |
| 数据盘 | 10% (33G/350G)，剩余 318G |

符号链接此前已正确配置，本次补齐了 `.bashrc` 中缺失的 `HF_HOME` 环境变量。根分区 41% 使用率健康，无需额外清理。

---
