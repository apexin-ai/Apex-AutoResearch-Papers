# diagnose multiscale seed43 r2 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_multiscale-seed43-r2-exit_20260517T205414_result.json`
- **Structured JSON:** [`ae0bef1c1e481d4dbe91.json`](../../sessions/ae/ae0bef1c1e481d4dbe91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session 中（可能已在之前 session 删除或从未在此 session 创建），跳过。

---

## 结果汇总

**eval-k1-crm-multiscale-object-seed43-r2** — 完成，结论：**negative**

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| bbq_sauce | 20% |
| ketchup | 0% |
| tomato_sauce | 20% |
| butter | 0% |
| milk | 0% |
| chocolate_pudding | 20% |
| orange_juice | 20% |
| **Overall** | **9.0%** |

K=1 CRM multi-scale (ACCG 4×960D) 在 seed43 上 overall SR = 9%，与之前 single-scale K=1 CRM 的 negative 结论一致（seed42/43/44 均为 negative）。multi-scale 架构未能挽救 K=1 的性能。

**cuda:1 已释放**（4 MiB / 0% utilization），可部署 OpenVLA eval。

---
