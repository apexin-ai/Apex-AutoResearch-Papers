# fix experiments v1 placeholders

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-v1-placeholders_20260515T035615_result.json`
- **Structured JSON:** [`7df25bc6304311409bb1.json`](../../sessions/7d/7df25bc6304311409bb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两份文件的数字已经完全一致，无需修改：

| 数据项 | experiment_setup_v1.md | experiments_v1.md | 状态 |
|--------|----------------------|-------------------|------|
| SWE-smith 总量 | 50,869 | 50,869 (line 5) | 一致 |
| 过滤后可用 | 44,173 | 44,173 (line 5, 138) | 一致 |
| 成功提取 | 15,897 (36.0%) | 15,897 (36.0%) (line 5) | 一致 |
| CodeQL 提取 | 15,133 | 15,133 (line 5) | 一致 |
| beniget fallback | 764 | 764 (line 5) | 一致 |
| 训练实例 | 14,288 | 14,288 (line 5) | 一致 |

experiments_v1.md 中的 15,133 是作为 "via CodeQL" 的子项正确使用的，不是被当作总 structural data 数。两份文件已同步，不存在需要替换的旧 placeholder。

---
