# ops s3 backup v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3_backup_v2_20260525T212718_result.json`
- **Structured JSON:** [`8c240b1bf755646aaaa6.json`](../../sessions/8c/8c240b1bf755646aaaa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。

**(a) Tarball**
- 路径: `/tmp/turn_residual_gating-final.tar.gz`
- 大小: 209,880,099 bytes (201 MB)

**(b) S3 URI**
- `s3://agent-ml-manager-backups-emnlp/manager-backup/backends/turn_residual_gating/project-archive/turn_residual_gating-final.tar.gz`

**(c) 备份内容**
- 打包目录: `~/turn_residual_gating/`（含 `artifacts/`, `checkpoints/`, `data/`, `eval_results/`, `logs/`, `outputs/`, `results/`, `runs/`, `scripts/`, `src/`）
- 排除项: `*.safetensors`, `*.bin`, `__pycache__`, `.venv`, `wandb/run-*`

---
