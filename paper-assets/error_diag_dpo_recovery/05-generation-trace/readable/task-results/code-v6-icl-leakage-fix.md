# code v6 icl leakage fix

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v6_icl_leakage_fix_20260512T195157_result.json`
- **Structured JSON:** [`213793651a063040a7ce.json`](../../sessions/21/213793651a063040a7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 通过，5 个 task 全部正常，输出格式验证通过。

修改总结（4 处改动）：

1. **`load_expert_examples`**：`by_type[tt].append(msgs)` → `by_type[tt].append({"game_file": item["game_file"], "msgs": msgs})`，保留 game_file 信息

2. **`sample_icl_examples` 签名**：新增 `exclude_game_file: str = None` 参数

3. **`sample_icl_examples` 函数体**：同类型采样池和 fallback 池都过滤掉 `game_file == exclude_game_file` 的条目，返回值提取 `c["msgs"]`

4. **`collect_single_trajectory` 调用处**：传入 `exclude_game_file=game_file`

---
