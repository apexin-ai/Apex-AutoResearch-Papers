# deploy bjb2 28827 backfill 3gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-backfill-3gpu_20260528T073447_result.json`
- **Structured JSON:** [`61d3e1813c16daaf6b9f.json`](../../sessions/61/61d3e1813c16daaf6b9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个进程均在运行。部署汇报：

| GPU | exp_id | PID | 模式 |
|-----|--------|-----|------|
| cuda:1 | eval-supp-long-adapt-tau025-s47-r2 | 191673 | adaptive_conformal_crm, seed=47, tau=0.25 |
| cuda:4 | eval-supp-long-k2mean-s46 | 192019 | vla_only (K=2, mean), seed=46 |
| cuda:5 | eval-supp-long-reconvla-s46 | 192687 | reconvla (K=10), seed=46 |

cuda:1 已加载模型（5687MiB），cuda:4/5 正在加载中。cuda:2/3 原有实验未受影响。cuda:0 空闲未动。timeout 均 8h。

---
