# deploy bjb1 18228 gpu12

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T064352_result.json`
- **Structured JSON:** [`7474efa9bd534d68b5e3.json`](../../sessions/74/7474efa9bd534d68b5e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Spatial s45 的 Adaptive 和 Reconvla 实验在 registry 中已有 DONE(success) 记录：

- `eval-supp-spatial-adapt-tau025-s45-r3` → DONE, success
- `eval-supp-spatial-reconvla-s45` → DONE, success
- `eval-supp-spatial-vla-only-s45` → DONE, success
- `eval-supp-spatial-crm-norm005-s45` → DONE, success

s46 同理全部完成。Spatial 已经有至少 5 seeds (s42-s46) 的完整数据。

另外 bjb1-18228 上没有 `crm_unified_4suite_r4` checkpoint（其他服务器上有），只有 `crm_unified_4suite/crm_best.pt`。

**需要你确认**：
1. 这两个 spatial s45 实验是否需要重跑？如果不需要，你想在 GPU 1+2 上部署什么实验？
2. QUEUED 列表中还有 `eval-supp-spatial-crm-norm005-s47`(PREPARING) 和一些 Object s45 实验可以部署，或者你有其他安排？

---
