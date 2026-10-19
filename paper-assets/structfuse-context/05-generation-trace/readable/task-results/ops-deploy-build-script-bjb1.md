# ops deploy build script bjb1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-build-script-bjb1_20260513T114703_result.json`
- **Structured JSON:** [`44c767825a3065c0280f.json`](../../sessions/44/44c767825a3065c0280f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 1 就绪，汇报：

**脚本部署** — 3 个脚本均已写入 `/root/structfuse/scripts/` 并设置 `+x`：
- `build_full_m2_data.sh` (3453B)
- `run_full_m2_training.sh` (5039B)
- `schedule_m2_runs.sh` (4433B)

**依赖检查** — 全部通过：
| 依赖 | 状态 |
|------|------|
| `build_m1_training_data.py` | 存在 (20944B) |
| Qwen2.5-Coder-3B `config.json` | 存在 |
| `all.jsonl` | 存在 (6.1GB) |
| `repos/` 目录 | 存在，~120 个仓库（双下划线命名） |

**Dry-run 语法检查** — 3 个脚本 `bash -n` 全部 `SYNTAX_OK`。

**build_m1_training_data.py 参数** — 与 `build_full_m2_data.sh` 调用一致：`--extraction-dir`, `--repos-dir`, `--output-dir`, `--seed`, `--model-path` 全部匹配。

可以启动数据构建。

---
