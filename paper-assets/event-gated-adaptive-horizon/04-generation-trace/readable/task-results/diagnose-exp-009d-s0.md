# diagnose exp 009d s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009d_s0_20260515T120737_result.json`
- **Structured JSON:** [`940a22fdb247357e3cb7.json`](../../sessions/94/940a22fdb247357e3cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原因已明确。

## 诊断结果

**失败原因**: 启动命令的工作目录 (`/root/runs/event-gated-adaptive-horizon/`) 下找不到 `dreamer.py`。

```
python: can't open file '/root/runs/event-gated-adaptive-horizon/dreamer.py': [Errno 2] No such file or directory
```

项目代码实际在 `/root/autodl-tmp/event-gated-adaptive-horizon/`，而启动命令在 `/root/runs/event-gated-adaptive-horizon/` 下执行，该目录只有日志文件，没有源码。

**对比**: s1 实验正常运行（代码路径正确，已跑到 115K steps 后被 Terminated）。

## 修复

重新提交 exp_009d_baseline_walker_s0 时，确保：
1. `cd /root/autodl-tmp/event-gated-adaptive-horizon/` 后再执行 python 命令，或
2. 使用绝对路径 `python /root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py ...`

正确的启动命令示例：
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py \
  --logdir logdir/walker_walk_baseline_s0 \
  --configs defaults \
  --task dmc_walker_walk \
  --seed 0 \
  --steps 500000
```

（具体参数以实际实验配置为准）

---
