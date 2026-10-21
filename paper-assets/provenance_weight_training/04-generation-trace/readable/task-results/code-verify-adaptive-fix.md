# code verify adaptive fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_adaptive_fix_20260514T140941_result.json`
- **Structured JSON:** [`ab64ded081767fbfc683.json`](../../sessions/ab/ab64ded081767fbfc683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：READY**

验证结果：

| 检查项 | 期望 | 实际 | 状态 |
|--------|------|------|------|
| n_min 默认值 | 2（非 3） | `max(2, batch_size // 2)` — 下界为 2 | ✅ |
| ESS 下界 | batch_size // 2 | `args.n_min = max(2, args.batch_size // 2)` (L279-280) | ✅ |
| 无 EMA | 不存在 EMA/smooth 代码 | `find_optimal_b` 直接返回 b*，无任何平滑逻辑 | ✅ |
| 代码可加载 | import 成功 | `import OK` | ✅ |

`adaptive` 路径逻辑清晰：每个 batch 调用 `find_optimal_b(q_scores, tau, n_min)` 得到 b*，直接计算权重，无 EMA 残留。可以直接提交 adaptive_fix 实验。

---
