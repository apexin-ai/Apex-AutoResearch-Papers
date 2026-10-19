# fix starcoder checkpoint cleanup bug

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_starcoder_checkpoint_cleanup_bug_20260514T193339_result.json`
- **Structured JSON:** [`857673ab76a48398f198.json`](../../sessions/85/857673ab76a48398f198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复结果：

1. **修复内容**：`run_m2_full_starcoder_resume.sh` 第 105-107 行，删除了永远为 false 的 `if [ -d "${OUTPUT_DIR}/best" ]` 条件包裹，改为无条件执行 `find "${OUTPUT_DIR}" -maxdepth 1 -name "checkpoint-*" -type d -exec rm -rf {} + 2>/dev/null || true`，与 Qwen 脚本行为一致。
2. **残留 checkpoint**：无。`find` 未发现任何残留的 `checkpoint-*` 目录，无需清理，释放空间 0GB。
3. **语法验证**：`bash -n` 通过，无语法错误。
4. **Qwen 脚本**：无此 bug，第 104 行已是无条件清理。

---
