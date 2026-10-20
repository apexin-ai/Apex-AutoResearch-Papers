# code turnkv press

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_turnkv_press_20260513T090754_result.json`
- **Structured JSON:** [`3a01e066056fc90cb564.json`](../../sessions/3a/3a01e066056fc90cb564.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 17 个测试通过。

创建的文件：

| 文件 | 用途 |
|------|------|
| `src/turnkv/__init__.py` | 包初始化，导出 `TurnKVPress`, `Segment`, EASS 函数 |
| `src/turnkv/press.py` | `TurnKVPress` 主类，包装 `ExpectedAttentionPress`，在 `score()` 中执行 segment-aware 分数调制 |
| `src/turnkv/eass.py` | EASS 核心逻辑：`compute_eass`（per-token→per-segment 聚合）、`compute_budget`（structural prior + recency decay + z-scored EASS 调制）、`map_budget_to_scores`（segment budget 乘回 per-token scores）；同时定义 `Segment` dataclass |
| `tests/torch_shim.py` | numpy-backed minimal torch API，支持无 torch 环境测试 |
| `tests/test_press.py` | 17 个单元测试覆盖 EASS 聚合、budget 计算（角色先验/recency decay/clipping/beta 灵敏度）、score mapping（保序性/budget=1 恒等性）、TurnKVPress 集成（有/无 segments、compression_ratio 继承） |

---
