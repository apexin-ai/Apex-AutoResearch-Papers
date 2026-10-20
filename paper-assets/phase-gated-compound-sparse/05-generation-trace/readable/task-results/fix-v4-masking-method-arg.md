# fix v4 masking method arg

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_v4_masking_method_arg_20260513T232226_result.json`
- **Structured JSON:** [`e0ee7320a1430cfb21dd.json`](../../sessions/e0/e0ee7320a1430cfb21dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。三处改动：

1. **`parse_args()`** — 新增 `--masking_method` 参数，choices=`['importance', 'random']`，default=`'importance'`
2. **mask 构建逻辑** — `masking_method == 'random'` 时传 `importance=None`，底层 `_select_heads_to_mask` / `_select_kv_to_evict` 已支持随机模式
3. **输出 JSON config** — `"masking_method"` 从硬编码 `"importance"` 改为 `args.masking_method`

验证结果：
- `--help` 显示 `--masking_method {importance,random}`
- importance 模式 dry-run 成功，JSON 输出 `"masking_method": "importance"`
- random 模式 dry-run 成功，JSON 输出 `"masking_method": "random"`

---
