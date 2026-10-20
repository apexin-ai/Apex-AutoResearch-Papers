# code westd eval split prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-eval-split-prep_20260514T061503_result.json`
- **Structured JSON:** [`5cc1350e4b6e721dd6e1.json`](../../sessions/5c/5cc1350e4b6e721dd6e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件修改结果：

| 文件 | `--split` 参数 | val dry_run |
|------|---------------|-------------|
| `eval_repo_cls.py` | `{val,test}`, default=test | 9335 samples ✓ |
| `eval_repo_cwm.py` | `{val,test}`, default=test | (同结构) ✓ |

修改内容：
- 新增 `--split` 参数（choices=val/test, default=test）
- 数据路径动态切换 `swebench_{split}.jsonl`
- 日志显示当前 split
- 输出 JSON 包含 `"split"` 字段

默认行为不变（default="test"），现有脚本/命令无需改动。

---
