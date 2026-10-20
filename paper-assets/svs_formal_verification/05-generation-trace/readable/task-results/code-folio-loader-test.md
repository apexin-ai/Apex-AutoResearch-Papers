# code folio loader test

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_folio_loader_test_20260514T075246_result.json`
- **Structured JSON:** [`f2ce3e92d4e73e0e3384.json`](../../sessions/f2/f2ce3e92d4e73e0e3384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Part A: cost_tracker 定价修复 ✓
已部署到远程。新增 `deepseek/deepseek-v3.2`（$0.27/$1.10）、`deepseek/deepseek-v4-pro`（$0.80/$3.20）和 `LOCAL_GPU_COST_PER_HOUR = 3.0`。验证通过。MVP（PID 24681）未重启，定价修复影响下次运行。

### Part B: FOLIO 数据加载 ✓
更新了 `loader.py`（远程 + 本地 artifacts）：
- 新增 `subset` 参数（`"train"` / `"validation"`）
- 新增 `_load_folio_local()` 从 `/root/autodl-tmp/data/folio/folio-{subset}.jsonl` 加载
- 修复 `num_problems=0` 表示加载全部的逻辑
- 回退链：HF → 本地 JSONL → JSON cache

**Label 分布**（`"Uncertain"` 已统一映射为 `"Unknown"`）：

| subset | True | False | Unknown | 总计 |
|--------|------|-------|---------|------|
| validation | 72 | 63 | 69 | 204 |
| train | 388 | 286 | 330 | 1004 |

---
