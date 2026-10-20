# analysis detach ln cka

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detach_ln_cka_20260524T083600_result.json`
- **Structured JSON:** [`3adcf3f6abda2a9b8bfc.json`](../../sessions/3a/3adcf3f6abda2a9b8bfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。CKA 结果汇总：

| Condition | DINOv2 mean | SigLIP mean |
|-----------|-------------|-------------|
| Vanilla | 0.968 | 0.953 |
| Full OCC | 0.964 | 0.960 |
| **Detach+LN** | **0.966** | **0.960** |
| Random OCC | 0.968 | 0.956 |
| Detach OCC (BN) | 0.539 | 0.312 |

**结论：Detach+LN CKA 完全恢复到 Vanilla 水平，与 Detach BN 的剧烈退化形成鲜明对比。BN 是表征退化的主因，梯度 detach 本身不破坏表征。**

文件已下载到 `artifacts/cka_detach_ln_results.json` 和 `artifacts/cka_detach_ln.pdf`，已注册 artifact 并更新 registry。

---
