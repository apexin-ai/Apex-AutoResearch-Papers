# code plan 702 k1 eval deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_702-k1-eval-deploy_20260517T152040_result.json`
- **Structured JSON:** [`ad8c1e77cff18ff23699.json`](../../sessions/ad/ad8c1e77cff18ff23699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**已部署 3 个 K=1 CRM ACCG eval 任务**（bjb1-32546）：

| Exp ID | GPU | Seed | tmux session |
|--------|-----|------|--------------|
| eval-k1-crm-accg-object-seed42 | 1 | 42 | eval-k1-accg-seed42 |
| eval-k1-crm-accg-object-seed43 | 4 | 43 | eval-k1-accg-seed43 |
| eval-k1-crm-accg-object-seed44 | 5 | 44 | eval-k1-accg-seed44 |

**修改内容**：给 `evaluate.py` 添加了 `crm_k1_accg` mode，加载 `MultiScaleCRM`（327K params），使用 fallback 单特征模式（960D obs → correction），max_correction_norm=0.2。

**配置**：每个 eval = 10 tasks × 10 rollouts = 100 episodes，LIBERO-Object benchmark。Registry 已注册 RUNNING。

Seed42 的 rollout 已开始执行，运行正常。

---
