# code fix m1 extraction script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_m1_extraction_script_20260512T161643_result.json`
- **Structured JSON:** [`2a89f5d11dfe4fb3886d.json`](../../sessions/2a/2a89f5d11dfe4fb3886d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个修复全部完成，语法验证通过。

**修改汇总：**

| 修复项 | 文件 | 变更 |
|--------|------|------|
| CodeQL PATH | `run_m1_extraction.sh` | 第3行加 `export PATH="/opt/codeql:$PATH"` |
| set -e → pipefail | `run_m1_extraction.sh` | 原文件已是 `set -o pipefail` 无 `set -e`，无需改动 |
| workers 4→8 | `run_m1_extraction.sh` | `--workers 8` |
| CodeQL DB 自动清理 | `batch_extract.py` | `process_repo_group()` 末尾 return 前，`shutil.rmtree(db_dir)` 删除该 group 的 CodeQL database |

未启动 M1 提取，P2b 训练（PID 238645）未受影响。

---
