# deploy cqa1 32758 spatial seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-spatial-seeds_20260524T070703_result.json`
- **Structured JSON:** [`d0eebba81f8fd3524eaa.json`](../../sessions/d0/d0eebba81f8fd3524eaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况汇总：

- **Goal s45/s46**: 10/10 实验全部 DONE
- **Spatial s45/s46**: 全部 DONE（registry 中 4 个 RUNNING 条目是僵尸，cqa1-32758 上并没有对应 tmux session）
- **cqa1-32758 tmux**: 只有 `long-adapt-s47` (cuda:4) 和 `long-vla-s47` (cuda:5)，GPU 0-3 完全空闲

**Spatial s47 状态**：只有 CRM (eval-supp-spatial-crm-norm005-s47) 在跑，缺 4 个方法：
1. VLA-only s47
2. Adaptive τ=0.25 s47
3. Reconvla s47
4. K2mean s47

正好 4 个实验对 4 张 GPU。要部署 Spatial s47 补全吗？还是有其他安排？

---
