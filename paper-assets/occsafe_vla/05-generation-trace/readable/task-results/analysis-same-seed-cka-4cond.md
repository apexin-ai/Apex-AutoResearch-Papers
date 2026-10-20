# analysis same seed cka 4cond

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_same_seed_cka_4cond_20260525T050056_result.json`
- **Structured JSON:** [`52c711b553460f08bd09.json`](../../sessions/52/52c711b553460f08bd09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CKA 分析完成。实验 `cka_same_seed_4cond` 已注册为 DONE。

## Same-Seed CKA 结果（seed=42, 200 samples, vs pretrained）

| Condition | DINOv2 mean CKA | DINOv2 min CKA | SigLIP mean CKA | SigLIP min CKA |
|---|---|---|---|---|
| **Vanilla** | 0.9676 | 0.8993 | 0.9530 | 0.8425 |
| **Full OCC (BN)** | 0.9594 | 0.8422 | 0.9593 | 0.8799 |
| **Detach+BN** | 0.9635 | 0.8895 | 0.9532 | 0.8292 |
| **Full OCC (LN)** | **0.6404** | **0.2558** | 0.9497 | 0.8479 |

关键发现：
- **Full OCC (LN) 严重破坏 DINOv2 表征**：mean CKA 仅 0.64（其余三个 >0.95），最低 block 降至 0.26（block 23）。早期 block 2-3 也仅 ~0.31。
- **SigLIP 全部条件均保持良好**（mean ~0.95），LN 对 SigLIP 无显著影响。
- **Vanilla / Full OCC (BN) / Detach+BN 三者 DINOv2 CKA 接近**（0.96-0.97），说明 BN 和梯度 detach 均能有效保护 DINOv2 表征。
- LN 的破坏具有选择性：只影响 DINOv2，不影响 SigLIP，说明 LN 归一化统计量与 DINOv2 的 pre-norm 结构存在冲突。

产出位于 `westd-10894:/root/autodl-tmp/analysis/cka_same_seed/`。

---
