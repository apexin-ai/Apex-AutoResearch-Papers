# deploy bjb1 18228 goal evals

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-goal-evals_20260524T070835_result.json`
- **Structured JSON:** [`6e11c6da54b0e03588a5.json`](../../sessions/6e/6e11c6da54b0e03588a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。bjb1-18228 GPU 分配：

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | precompute-pi05-object-2048-r2 | 不碰 |
| 1 | **eval-supp-long-vla-only-s47-r2** (PID 278846) | RUNNING |
| 2 | **eval-supp-goal-vla-only-s47** (PID 279117) | RUNNING |
| 3 | precompute-pi05-long-2048-r2 | 不碰 |

**选择理由：**
- Goal/Object s42-s46 五种方法全部 DONE，无缺口
- Long s47 四种方法在跑（crm/reconvla/adapt/k2mean），但现有 `eval-supp-long-vla-only-s47` 实际跑的是 k2mean (K=2 mean)，真正的 VLA-only (K=1) 缺失 → GPU 1 补上
- Goal s47 尚无任何 seed，VLA-only 不需要 CRM checkpoint → GPU 2 开跑

---
