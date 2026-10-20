# code fix rrf skip patterns

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-rrf-skip-patterns_20260516T030407_result.json`
- **Structured JSON:** [`046f65af15c3b5cd8bb4.json`](../../sessions/04/046f65af15c3b5cd8bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已有修复，无需修改。**

`ALPHA16_BLOCKLIST`（第43-49行）已包含这5个目录的精确名称，且第233行同时检查了 `SKIP_PATTERNS` 和 `ALPHA16_BLOCKLIST`：

```python
if any(pat in model_id for pat in SKIP_PATTERNS) or model_id in ALPHA16_BLOCKLIST:
```

- `SKIP_PATTERNS` → substring 匹配，处理含 "DEPRECATED" 的目录
- `ALPHA16_BLOCKLIST` → 精确匹配（set membership），处理这5个 alpha=16 目录

两个引用点完全相同（仅第233行），不存在遗漏的代码路径。且精确匹配比 substring 匹配更安全，不会误伤 `d000_a32_s42` 等有效目录。

---
