# ops eval precheck

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_precheck_20260526T221530_result.json`
- **Structured JSON:** [`5ecc245d4527e0c4ff1f.json`](../../sessions/5e/5ecc245d4527e0c4ff1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_prep_l01_high.md`。

核心发现：

1. **λ=0.1 s0, s1, s2 的 eval 已全部完成** — westd-45947 上有 seed=7 的 reeval 结果（今天完成）
2. **LoRA baseline s2 是唯一阻塞项** — checkpoint 仅到 18000，未在训练中，需恢复训练到 30000
3. **所有 6 个 GPU 当前被占用**，跑 eval/reeval batch，新任务需等完成
4. westd-35807 的 s1_l01 eval 之前 ep 114/200 中断，但 westd-45947 已补齐

---
