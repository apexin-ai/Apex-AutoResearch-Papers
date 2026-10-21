# ops fix cp stats bug

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_cp_stats_bug_20260520T062012_result.json`
- **Structured JSON:** [`8bff2744a50565691bc6.json`](../../sessions/8b/8bff2744a50565691bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复验证通过。

**修复结果**：

| | 修复前 (buggy) | 修复后 |
|---|---|---|
| 统计基数 | 所有 cp≠null 的 annotations | 仅 is_jailbreak=True |
| n_jailbreak_with_cp | (未记录) | **52** |
| mean | 2.37→2.8 (含 non-jb 噪音) | **1.42** |
| median | 0.0 | 0.0 |
| mean_relative | 0.1258→0.142 | **0.0452** |

**完成的修改**：

1. **服务器脚本** `annotate_cp_llm_qwen3.py` — 三处修复：
   - `annotate_one`: non-jailbreak 时 `cp = None`
   - `save_results`: CP 统计只算 `is_jailbreak=True`，新增 `n_jailbreak_with_cp`
   - `main()` 末尾摘要：同上过滤
2. **本地脚本副本** — 同步修复
3. **Post-hoc 修正** — 已自动执行，输出 JSON 已修正
4. 修正脚本保留在服务器 `/root/autodl-tmp/contrastive_trace_safety/scripts/fix_cp_stats_posthoc.py`

---
