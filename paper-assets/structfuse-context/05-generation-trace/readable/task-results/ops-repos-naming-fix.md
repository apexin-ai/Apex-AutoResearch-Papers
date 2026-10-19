# ops repos naming fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_repos-naming-fix_20260513T114200_result.json`
- **Structured JSON:** [`f5c3635924a48191836b.json`](../../sessions/f5/f5c3635924a48191836b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`clone_repos.sh` 已修复为 `sed 's/\//__/'`。

## 结果

| 项目 | 数量 |
|------|------|
| repos 总数 | 123 |
| 已 rename 为双下划线 | 123（全部） |
| 单下划线残留 | 0 |
| missing | 0 |
| clone_repos.sh | 已修复，`tr '/' '_'` → `sed 's/\//__/'` |

目录命名已全部对齐为 `org__repo` 格式，M2 pipeline 可以继续跑了。

---
