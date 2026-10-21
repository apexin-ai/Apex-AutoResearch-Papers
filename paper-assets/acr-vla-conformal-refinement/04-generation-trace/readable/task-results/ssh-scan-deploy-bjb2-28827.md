# ssh scan deploy bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-deploy-bjb2-28827_20260523T232236_result.json`
- **Structured JSON:** [`e8fdf71442c5169ebc19.json`](../../sessions/e8/e8fdf71442c5169ebc19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 扫描结果汇总

**bjb2-28827 当前无空闲 GPU。**

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| cuda:0 | goal-vla-only-s46 | 1/10 tasks | ~6h |
| cuda:1 | goal-k2mean-s46 | 1/10 tasks | ~6h |
| cuda:2 | goal-reconvla-s46 | 1/10 tasks | ~10h+ (K=10) |
| cuda:3 | goal-crm-s46 | 1/10 tasks | ~10h+ (K=10) |
| cuda:4 | long-k2mean-s45 | 5/10 tasks | ~3-4h |
| cuda:5 | goal-adapt-s46 | 1/10 tasks | ~6h |

**部署结果：**
- **Goal s46 全部 5 个实验**：已在运行，无需重复部署
- **P0: Long VLA-only s43 (eval-supp-long-vla-only-s43-r2)**：无法部署，没有空闲 GPU

**选项：**
1. 等 cuda:4 (long-k2mean-s45) 完成后部署 Long VLA-only s43（~3-4h）
2. 在其他服务器（bjb2-40593 或 bjb1-32546 或 cqa1-32758）找空闲 GPU 部署
3. 手动排队——不做操作，等 GPU 释放后再部署

需要指示如何处理 P0 实验。

---
