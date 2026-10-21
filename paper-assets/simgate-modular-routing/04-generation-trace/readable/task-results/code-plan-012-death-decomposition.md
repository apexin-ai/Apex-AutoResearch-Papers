# code plan 012 death decomposition

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-012-death-decomposition_20260514T041153_result.json`
- **Structured JSON:** [`401c64c0440efcb387f8.json`](../../sessions/40/401c64c0440efcb387f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常，输出格式正确。

结果：
- 25 个 prescreening task，133 episodes
- `Delta_full = +45.99`，`Delta_nd = +0.83`，`death_avoidance_fraction = 0.9819`
- Pearson r = 0.9821 (p ≈ 0)，death rate 差异几乎完美预测 Delta
- CSV 列：task_name, n_episodes, death_rate_int, death_rate_det, delta_full, delta_nd, delta_penalty_replaced, det_pref, int_pref, no_pref

脚本已写入本地 `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/analysis/death_decomposition.py` 并在服务器上通过了 prescreening 数据验证。如需跑全量数据（含 mvp/plan_c），可以用逗号分隔目录或指定更具体的子目录避免超时。

---
