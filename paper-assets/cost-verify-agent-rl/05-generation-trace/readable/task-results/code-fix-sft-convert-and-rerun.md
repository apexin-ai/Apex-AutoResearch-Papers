# code fix sft convert and rerun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_sft_convert_and_rerun_20260514T031707_result.json`
- **Structured JSON:** [`14da1e95cff7640a782a.json`](../../sessions/14/14da1e95cff7640a782a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。产出报告：

---

### 修复 diff

**Bug 1 — Action 提取**（从正则反推改为 tool_calls 直接提取）:
```diff
- action = extract_action(tool_text)
- if action is None:
-     return None, "extract_fail", []
+ tool_calls = msgs[i].get("tool_calls")
+ if not tool_calls:
+     return None, "no_tool_calls", []
+ try:
+     action = json.loads(tool_calls[0]["function"]["arguments"])["action"]
+ except (KeyError, json.JSONDecodeError, IndexError):
+     return None, "tool_calls_parse_fail", []
```
删除了 `extract_action()` 函数（~30 行正则逻辑）。

**Bug 2 — System prompt 缺前缀**:
```diff
- RAGEN_SYSTEM_PROMPT = """You are an expert agent in the ALFRED...
+ RAGEN_SYSTEM_PROMPT = """You're a helpful assistant. You are an expert agent in the ALFRED...
```

### 转换统计

| 指标 | 值 |
|------|-----|
| 总数 | 1200 |
| 成功转换 | **1200（100%，0 过滤）** |
| 平均 turns | 9.6 |
| Max/Min turns | 24 / 4 |
| System prompt | `"You're a helpful assistant. You are an expert agent..."` ✓ |

### Dry-run 结果

| 指标 | 值 |
|------|-----|
| Step 1 loss | 2.9302 |
| Step 2 loss | 2.9621 |
| 训练状态 | **成功** |

### 清理

旧 checkpoint `exp008_sft/checkpoint-75` 已删除。

---
