# code fix 019b maniskill config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-019b-maniskill-config_20260517T033639_result.json`
- **Structured JSON:** [`5f94bfa41e880118ea8f.json`](../../sessions/5f/5f94bfa41e880118ea8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果：**
- 在 `configs.yaml` 中添加了通用 `maniskill` config section（与 `maniskill_state` 内容一致）
- exp_019b_pickcube_civo_trigger 已成功启动（PID 646809，tmux session `exp019b`），无 KeyError
- 训练已开始：完成首次 eval（return=1.1），正在进行训练迭代，gate_dt 指标正常输出（gate_dt_mean=2.0，gate_dt_2_frac=1.0，符合 `--gate_fixed_dt 2` 设定）

**根因：** configs.yaml 中只有 `maniskill_state`/`maniskill_stackcube`/`maniskill_peginsertion`，没有通用 `maniskill` 名称。019a_v2 实际使用的是 `--configs defaults maniskill_state`。019b 的命令写成了 `--configs defaults maniskill`，但该 key 不存在。

---
