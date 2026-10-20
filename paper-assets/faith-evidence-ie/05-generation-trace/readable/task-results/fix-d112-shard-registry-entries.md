# fix d112 shard registry entries

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d112_shard_registry_entries_20260519T004337_result.json`
- **Structured JSON:** [`cc6a76d645ab3f2b6d68.json`](../../sessions/cc/cc6a76d645ab3f2b6d68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 修复完成。汇总：

| exp_id | status | gpu | PID | docs 范围 |
|--------|--------|-----|-----|----------|
| `d112_rsft_s44_gen_shard0` | RUNNING | cuda:3 | 590423 | [0:756] |
| `d112_rsft_s44_gen_shard1` | RUNNING | cuda:1 | 587729 | [756:1512] |
| `d112_rsft_s44_gen_shard2` | RUNNING | cuda:2 | 587819 | [1512:2268] |
| `d112_rsft_s44_gen_shard3` | RUNNING | cuda:0 | 590568 | [2268:3027] |

- shard0/shard3：新建，状态从 PREPARING 推进至 RUNNING
- shard1/shard2：已清除多余 parent 字段，更新 hypothesis 和 spec（补充 gpu_ids/pid）
- `d112_rsft_s44_generate`：已确认为 DONE 状态，无需修改

---
