# ops d000 s42 symlink fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d000-s42-symlink-fix_20260516T010843_result.json`
- **Structured JSON:** [`2fc90b80ca1b17e85e30.json`](../../sessions/2f/2fc90b80ca1b17e85e30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已创建的 symlinks：**
- `Qwen2.5-3B_d000_a32_s42` → `Qwen2.5-3B_d000_s42`（替换了之前的空目录）
- `Qwen2.5-3B_d000_a32_s123` → `Qwen2.5-3B_d000_s123`（新建）

两者均通过 symlink 正确访问到 `adapter_config.json`（lora_alpha=32 已确认）。signals 目录无对应的 `d000_s42` / `d000_s123` 条目，无需处理。

---
