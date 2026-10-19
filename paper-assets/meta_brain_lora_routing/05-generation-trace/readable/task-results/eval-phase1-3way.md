# eval phase1 3way

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_phase1_3way_20260516T074213_result.json`
- **Structured JSON:** [`711204a4047808760cbb.json`](../../sessions/71/711204a4047808760cbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval_par_v1 | cuda:0 | 411042 | RUNNING |
| eval_univ_r16 | cuda:1 | 411121 | RUNNING |
| eval_univ_r48 | cuda:3 | 411431 | RUNNING |

**验证阶段输出**：`2026-05-16 15:43:13,095 [INFO] Loading PI0 model...` — 模型成功加载，无 crash、无参数错误。

**无异常**。3 个评估均已在 tmux 后台运行，timeout 6 小时，日志分别在 `~/runs/meta_brain_lora_routing/eval_{par_v1,univ_r16,univ_r48}.log`。

---
