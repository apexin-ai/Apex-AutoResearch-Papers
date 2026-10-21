# backup discover westd 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_backup_discover-westd-21461_20260525T205612_result.json`
- **Structured JSON:** [`1f8066e6d04fbebad26d.json`](../../sessions/1f/1f8066e6d04fbebad26d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/backup_discovery_westd21461.md`。

关键发现：
- **需备份总量约 2.8G**：LoRA checkpoints 2.4G（qwen3_8b_lora_wikievents + llama_lora_docred 各 1.2G），outputs 140M，数据盘 schema_outputs 145M，data 88M，代码约 2M
- **排除 72G 公开模型**（/root/autodl-tmp/models/）
- 服务器上无 .git、无 venv、无 wandb 缓存
- rsync 需要两条命令：一条同步项目根目录（排除 `__pycache__`/`.pytest_cache`），一条同步 `/root/autodl-tmp/schema_outputs/`

---
