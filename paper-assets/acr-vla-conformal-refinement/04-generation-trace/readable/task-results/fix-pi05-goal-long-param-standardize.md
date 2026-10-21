# fix pi05 goal long param standardize

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pi05-goal-long-param-standardize_20260522T154824_result.json`
- **Structured JSON:** [`a106e7639f09b2717a29.json`](../../sessions/a1/a106e7639f09b2717a29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现代码行为：`evaluate.py` 的 `main()` 函数在 `mode=vla_only` 时会自动覆盖 K 值：
- `baseline_mode=single`（默认）→ `K=1`
- `baseline_mode=mean` → `K=10`

所以命令中的 `--K 10` 被忽略，实际全部用 `K=1`。**这对标准化没有影响**——所有 seed 都走同一段代码，K 都被覆盖为 1，参数完全一致。

## 部署总结

| 实验 ID | 服务器 | GPU | PID | tmux session |
|---------|--------|-----|-----|-------------|
| eval-pi05-vla-only-goal-seed43-r4 | bjb1-32546 | cuda:4 | 465874 | eval-pi05-vla-only-goal-seed43-r4 |
| eval-pi05-vla-only-goal-seed44-r4 | bjb1-32546 | cuda:5 | 466238 | eval-pi05-vla-only-goal-seed44-r4 |
| eval-pi05-vla-only-long-seed43-r4 | bjb1-18228 | cuda:1 | 41632 | eval-pi05-vla-only-long-seed43-r4 |
| eval-pi05-vla-only-long-seed44-r4 | bjb1-18228 | cuda:2 | 41914 | eval-pi05-vla-only-long-seed44-r4 |
| eval-pi05-vla-only-goal-seed42-r4 | bjb1-18228 | cuda:3 | 42259 | eval-pi05-vla-only-goal-seed42-r4 |
| eval-pi05-vla-only-long-seed42-r4 | bjb2-40593 | cuda:0 | 67669 | eval-pi05-vla-only-long-seed42-r4 |

**所有命令参数完全一致**（仅 SEED/GPU 不同）：
- `--mode vla_only --model pi05 --benchmark {goal|long} --seed {SEED} --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps {300|520}`
- 实际生效参数：K=1（代码对 vla_only+single 模式强制覆盖），n_action_steps=10, n_rollouts=20

**注意**：模板中缺失的 `--model pi05` 已补上。

**预计完成时间**：Goal (300 steps × 20 rollouts × 10 tasks) ~3-5h，Long (520 steps × 20 rollouts × 10 tasks) ~5-8h。

---
