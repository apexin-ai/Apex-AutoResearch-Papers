# diagnose bootstrap ci ioi retry

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642_result.json`
- **Structured JSON:** [`3c3810c17134f26c1127.json`](../../sessions/3c/3c3810c17134f26c1127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已完成。** `bootstrap_ci_results.json` 已存在且包含完整的 IOI Bootstrap CI 结果（n_valid=1000）：

| 指标 | 值 |
|------|-----|
| CSS=1.0 CPR | 0.0295 (16 edges, ACDC) |
| Best single (EP) CPR | 0.0829 (100 edges) |
| observed delta | -0.0535 |
| bootstrap CI | [-0.290, 0.259] |
| **p-value** | **0.342** |
| significant | **false** |

实验没有失败——结果文件在 `19:50` 已写入完毕，1000 个 bootstrap 样本全部完成。任务描述中的 "westd-pro6000" 服务器不存在于当前可用列表（实际是 westd-39279），可能是旧信息。

**结论**：CSS=1.0 在 IOI 任务上相对 best single method 的 advantage 不显著（p=0.342, CI 包含 0，delta 为负），即 CSS 共识电路在 IOI 上没有统计显著的优势。这与 SVA 的结果（p=0.099）方向一致——CSS 在这些任务上并未展现出显著优势。

无需重跑实验。需要我将结果注册到 registry 吗？

---
