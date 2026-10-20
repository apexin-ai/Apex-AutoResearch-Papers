# code mvp results now

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-results-now_20260512T154349_result.json`
- **Structured JSON:** [`b2184b06bfaf2e50c301.json`](../../sessions/b2/b2184b06bfaf2e50c301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**STATUS: RUNNING**

ACDC 仍在运行，结果文件不存在。详细进度：

| 方法 | 状态 | 详情 |
|------|------|------|
| EAP-IG | ✅ 完成 | 32491 edges scored, cached |
| Edge Pruning | ✅ 完成 | 32491 edges scored, cached |
| ACDC | 🔄 运行中 | τ=0.01 (第1/5轮), 15017/32491 edges (46.2%), ~6.85 it/s |

**ACDC 预计剩余时间：**
- 当前 τ=0.01 剩余：~42 min
- 之后还有 4 个 τ 值要跑，每轮 ~60 min
- **总剩余估计：~4.5-5 小时**

ACDC 当前状态：Removed 14963, Left 54 edges（τ=0.01 阈值下保留 54 条边）。

需要等 ACDC 全部 5 个 τ 跑完才能生成 `mvp_results.json`。要不要我定期回来检查进度？

---
