# hotfix metrics mauve tryexcept

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_metrics_mauve_tryexcept_20260517T201134_result.json`
- **Structured JSON:** [`0b903c712eef01382e1c.json`](../../sessions/0b/0b903c712eef01382e1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修改**: `/root/autodl-tmp/distrib_canary_collapse/metrics.py` 第 323-328 行

MAUVE 调用已包裹在 try/except 中：失败时打印警告并设 `results["mauve"] = None`。`json.dump` 会将 `None` 序列化为 `null`，不影响其他 metrics 计算。

---
