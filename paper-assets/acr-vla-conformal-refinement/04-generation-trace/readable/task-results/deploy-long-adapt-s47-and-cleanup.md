# deploy long adapt s47 and cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_long-adapt-s47-and-cleanup_20260524T121115_result.json`
- **Structured JSON:** [`9d35c7837c35d0b5f1d7.json`](../../sessions/9d/9d35c7837c35d0b5f1d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Part 1 — Reconvla 重复进程**：PID 316673 在 bjb1-32546 上已不存在（可能 SIGHUP 自然终止）。无 long/reconvla tmux session。GPU 0-5 全部空闲。无需 kill。

**Part 3 — Long s47 Adaptive 假失败检查**：未找到 `eval_long_adaptive_conformal_crm_tau0.25_seed47.json`。仅有 vla_only/crm_obs_only/reconvla 三个 long s47 结果。**是真失败**，需提交重试。

**Part 2 — 重试已部署**：
- exp_id: `eval-supp-long-adapt-tau025-s47-r2`
- server: bjb1-32546, GPU cuda:1
- tmux session: `eval-supp-long-adapt-tau025-s47-r2`
- PID: 433348
- log: `/root/acr-vla-conformal-refinement/logs/eval-supp-long-adapt-tau025-s47-r2.log`
- 已加载 SmolVLA + CRM，进入 long 环境 init 阶段
- registry: status=RUNNING, parent=eval-supp-long-adapt-tau025-s47

---
