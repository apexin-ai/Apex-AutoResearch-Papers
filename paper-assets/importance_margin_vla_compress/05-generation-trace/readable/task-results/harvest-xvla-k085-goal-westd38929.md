# harvest xvla k085 goal westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_xvla-k085-goal-westd38929_20260524T022025_result.json`
- **Structured JSON:** [`94f432d2588aaa210200.json`](../../sessions/94/94f432d2588aaa210200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Object 条目已存在且已是 DONE 状态，metrics 已正确。

**收割完成。X-VLA Random k=0.85 全部三个 suite 结果：**

| Suite | SR | 95% CI | Episodes |
|-------|-----|--------|----------|
| **Goal** | 60.4% | [56.1%, 64.6%] | 500 |
| **Object** | 65.0% | [60.7%, 69.1%] | 500 |
| **Spatial** | 68.2% | [64.0%, 72.1%] | 500 |

Registry 状态：
- `eval_xvla_random_k085_goal_seed42` → DONE ✓（本次收割）
- `eval_xvla_random_k085_object_seed42` → DONE ✓（已有）
- `eval_xvla_random_k085_spatial_seed42` → DONE ✓（metrics 已更新至 68.2%）

对比 π0.5 的 disruption peak（Goal k=0.85=52.4%），X-VLA 在 k=0.85 没有出现明显的 disruption peak — 三个 suite 的 SR 都相对平稳，支持 BART connector（无 RoPE）不会产生位置编码中断的假说。

---
