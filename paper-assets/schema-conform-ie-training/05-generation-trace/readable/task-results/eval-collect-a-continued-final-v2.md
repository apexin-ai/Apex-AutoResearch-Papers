# eval collect a continued final v2

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_a_continued_final_v2_20260513T231858_result.json`
- **Structured JSON:** [`0f7027e6823758a15671.json`](../../sessions/0f/0f7027e6823758a15671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程仍在运行。日志显示：

- **scierc_test** 已完成 (551/551)
- **crossner_politics** 刚开始 (5/651, ~1%)

scierc_test 结果：
| 指标 | 值 |
|------|-----|
| entity_f1 | 0.5172 |
| relation_f1 | 0.3004 |
| f1_correctness | 0.4185 |
| structural_validity | 1.0000 |
| type_conformance | 0.9814 |
| relational_constraint | 0.7102 |
| structural_completeness | 0.9819 |

输出目录还没有 JSON 文件（可能全部评完才写入）。crossner_politics 按 ~3s/it 估算还需 ~32 分钟，加上 crossner_science，预计整体还需 ~1 小时。

不做 registry 更新，不删 cron。

---
