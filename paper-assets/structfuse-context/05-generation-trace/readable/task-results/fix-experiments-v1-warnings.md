# fix experiments v1 warnings

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-v1-warnings_20260514T225801_result.json`
- **Structured JSON:** [`46cf5a79c915ebec0805.json`](../../sessions/46/46cf5a79c915ebec0805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 处修改完成：

1. **Warning 1 — Table 6 Total**：36.0% → **34.3%**（对齐 `plan_006_scalability` registry），§4.1 正文同步更新（coverage rate + remaining 比例 64%→65.7%）
2. **Warning 2 — Table 2 checkpoint**：数值更新为 R@1 checkpoint 4 位小数（0.5357/0.5557/0.5436/0.4922/0.5078/0.4869），表标题加注 "R@1 checkpoint"，delta 不变
3. **Warning 3 — SWE-bench → SWE-smith**：引用改为 `\cite{yang2025swesmith}`，新增 task→instance 展开说明（5,029 tasks × 多 gold files = 44,173 instances）
4. **Info 4 — cite key**：`cocohanere2025` → `fan2025cocohanere`
5. **Info 5 — temperature**：`temperature τ = 0.07` → `learnable temperature initialized at τ = 0.07`

---
