# deploy bjb2 40593 single

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-40593-single_20260524T070715_result.json`
- **Structured JSON:** [`90f2f8f1b1c612f8a5be.json`](../../sessions/90/90f2f8f1b1c612f8a5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态总结：**

| 项目 | 状态 |
|------|------|
| GPU 0 | 被 `eval-spatial-crm-s47` 占用（6006 MiB, 21% util），第 2/10 任务 |
| 磁盘 | `/root/autodl-tmp` 118G 可用（53%），比预期宽裕 |
| 之前的 obj-s45 | 已完成并收割（76.5%），registry 已更新 |
| `eval_spatial_k2mean_seed45` | 已完成并收割（80.0%），registry 已更新 |

**无法部署新实验**：GPU 0 正在跑 `eval-supp-spatial-crm-norm005-s47`（PID 235730, tmux: `eval-spatial-crm-s47`），当前在第 2/10 个任务，预计还需数小时。

**GPU 空闲后的建议部署**（按优先级）：
1. **Spatial VLA-only s47** — 与当前跑的 CRM s47 配对，补齐 seed47 coverage
2. **Spatial K2mean s47** / **Spatial Reconvla s47** / **Spatial Adapt s47** — 同样补 seed47

Spatial VLA-only s46 已在 bjb2-28827 上 RUNNING，且结果已 DONE（80.5%），不需要重跑。

---
