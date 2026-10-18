# audit attn strict prune diag

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_attn_strict_prune_diag_20260527T125459_result.json`
- **Structured JSON:** [`e84cebc13812da27e3ac.json`](../../sessions/e8/e84cebc13812da27e3ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部有 `[PRUNE-DIAG]` 输出，确认使用了正确的物理 token 移除脚本。

## 审计结果

| 实验 | PRUNE-DIAG | n_keep | 期望值 | 结论 |
|------|-----------|--------|--------|------|
| **attn k=0.9 strict** (SR=64%) | ✅ 有 | 230/256 | ~230 (256×0.9) | ✅ 正确脚本 |
| **attn k=0.85 strict** (SR=50%) | ✅ 有 | 217/256 | ~218 (256×0.85) | ✅ 正确脚本 |
| **attn k=0.95 strict (对照)** | ✅ 有 | 243/256 | ~243 (256×0.95) | ✅ 正确脚本 |

三个实验的 n_keep 值均与 `floor(256 × k)` 一致，score_range 和 first_indices 格式也吻合。**两个待审实验都用了正确的物理 token 移除脚本，结果可用，无需重跑。**

关于 k=0.85 strict SR=50% 与旧版 lenient 50% 相同：这是巧合，不是旧脚本的标志——日志明确显示 n_keep=217（非 256）。

---
