# audit bjb2 28827 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-deploy_20260526T154456_result.json`
- **Structured JSON:** [`eb66803791164302e222.json`](../../sessions/eb/eb66803791164302e222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

中止部署。所有 6 张 GPU 全部在用，不符合 C001 约束。

## 审计结果

**GPU 状态**：6/6 全部占用（违反 C001，禁止部署）

| GPU | 显存 | 进程 | 运行实验 | 已运行 |
|---|---|---|---|---|
| 0 | 12529 MiB | 443692 | pi05 adaptive_conformal_crm spatial s42 tau=0.15 | 1h37m |
| 1 | 12529 MiB | 444363 | pi05 adaptive_conformal_crm spatial s42 tau=0.35 | 1h36m |
| 2 | 12593 MiB | 445988 | pi05 adaptive_conformal_crm goal s42 tau=0.15 | 1h34m |
| 3 | 12593 MiB | 448295 | pi05 adaptive_conformal_crm goal s42 tau=0.35 | 1h32m |
| 4 | 14045 MiB | 450041 | pi05 adaptive_conformal_crm long s42 tau=0.15 | 1h30m |
| 5 | 14045 MiB | 451711 | pi05 adaptive_conformal_crm long s42 tau=0.35 | 1h29m |

**部署结果**：未部署任何实验，未执行步骤 2-4。

**说明**：上游"全部空闲"报告与实测冲突。bjb2-28827 实为满载，正在跑 6 个 pi05 adaptive conformal CRM 实验（spatial/goal/long × tau=0.15/0.35，全是 s42，K=2，norm=0.2），均已运行 1h29m–1h37m。按 C001 禁止抢占已有实验直接提交。建议：等当前 6 实验完成（按 20 rollout 体量预计还需 1-2h），收割时严格按 C002 审查日志后再做下一轮部署决策。

---
