# analysis cka dose response full s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_dose_response_full_s0_20260525T070531_result.json`
- **Structured JSON:** [`dd85d8e8cc12325b53b5.json`](../../sessions/dd/dd85d8e8cc12325b53b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：s0 cutoff 实验不存在。**

当前状态：

| 条件 | s0 (seed 42) 状态 |
|------|-------------------|
| Vanilla s0 | ✅ 在 10894 |
| Full OCC s0 | ✅ 在 10894 |
| Detach+BN s0 | ✅ 在 10894 |
| Full OCC+LN s0 | ✅ 在 10894 |
| cutoff_25k_s0 | ❌ 不存在 |
| cutoff_s0 (35K) | ❌ 不存在 |
| cutoff_45k_s0 | ❌ 不存在 |
| reverse_cutoff_s0 | ❌ 不存在 |

34685 上 4 个 GPU 全部在跑 s1/s2 v3 重训（~16% 进度，还需 ~10h），没有任何 s0 cutoff checkpoint。

10894 上 4 个 GPU 全部空闲（无 GPU 进程）。

**建议方案：**在 10894 上训练这 4 个 s0 cutoff 实验，用 cuda:2 和 cuda:3 跑两批（每批 2 个，各 ~13h），cuda:0 给 cutoff_15k_s0（或一起跑），cuda:1 留给 CKA。训练完成后再执行 CKA 分析。

是否要我在 10894 上启动这 4 个 s0 cutoff 训练？

---
