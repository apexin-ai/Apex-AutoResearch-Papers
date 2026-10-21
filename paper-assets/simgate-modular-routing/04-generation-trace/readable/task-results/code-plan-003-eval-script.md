# code plan 003 eval script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-003-eval-script_20260514T071320_result.json`
- **Structured JSON:** [`8e89d66f510fb086dcde.json`](../../sessions/8e/8e89d66f510fb086dcde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个条件的评估完成。结果：

```
Condition                 Score        90% CI          Success    Death    SimRatio
always-internal          -37.16  [-43.39, -31.43]     0.1237    0.4072    0.0000
always-deterministic     -11.64  [-17.39,  -6.55]     0.2371    0.1856    1.0000
oracle                    -9.03  [-14.14,  -4.15]     0.2423    0.1649    0.9623
random                   -23.75  [-29.60, -18.11]     0.1649    0.2835    0.5027
trained-router           -11.64  [-17.39,  -6.55]     0.2371    0.1856    1.0000
```

**关键发现**：
- **trained-router 与 always-deterministic 结果完全相同**：router 对所有 194 个 episode 全部预测 "deterministic"（sim_ratio=1.0）。这与 plan-012 的分析一致 — ~90% routing signal 来自 death avoidance，router 学到了"永远选 deterministic 更安全"
- **oracle 仅比 always-deterministic 好 ~2.6 分**：oracle 有 96.2% 的 episode 也选 deterministic，说明 internal 仅在极少数 episode 上更优
- **always-internal 死亡率 40.7%**，always-deterministic 仅 18.6%

**产出文件**（在服务器 `results/plan_003_eval/`）：
- `overall_results.json` — 按条件聚合的指标 + bootstrap 90% CI
- `per_task_results.csv` — 按 task × condition 的分拆
- `episode_details.jsonl` — 逐 episode 路由决策和分数
- `per_task_results.json` — 同上 JSON 格式

**脚本路径**：`src/eval_end_to_end.py`，已在服务器上。本地副本在 workspace 中。

**注意事项**：
- 68/194 episodes 在 step_map 中有匹配（labeled_steps.jsonl 的 key 格式与 episode_summary 的 episode_idx 不完全对齐）。对于没有 step 数据的 episode，router 默认选 deterministic。不影响结论因为有 step 数据的 episode router 也全部预测 deterministic
- 如需使用 `checkpoints/plan-002-formal-v6/final_adapter` 作为默认 checkpoint 路径，命令为：
```bash
python src/eval_end_to_end.py \
  --conditions always-internal,always-deterministic,oracle,random,trained-router \
  --router_checkpoint checkpoints/plan-002-formal-v6/final_adapter \
  --data_dir results/plan_c \
  --output_dir results/plan_003_eval \
  --seed 42
```

---
