# ssh check exp001 and exp006 readiness

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp001-and-exp006-readiness_20260513T214001_result.json`
- **Structured JSON:** [`f4a420cdaaf30e5079ff.json`](../../sessions/f4/f4a420cdaaf30e5079ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### exp_001_baseline — **已完成**

| 项目 | 值 |
|------|-----|
| 状态 | Finished（PID 9409 已退出） |
| 最终训练 step | 512,000 |
| 最后一次 eval | step 505,000, **eval_return = 970.41** |
| eval 总次数 | 51 次（每 10k steps） |
| Checkpoint | `latest.pt`（219MB）✓ |
| 收敛情况 | ~100k step 后 plateau 在 920–970 区间，最后一次 eval 为全程最高 |

### exp_006_fixed_dt2 — **代码已就绪**

`gate_fixed_dt` 参数已完整实现：

- `configs.yaml:114` — 默认值 `gate_fixed_dt: 0`（0 = 使用 Gumbel-Softmax gate）
- `models.py` 中有完整条件分支（L188/245/314/547/562/572）：当 `gate_fixed_dt > 0` 时跳过 gate 网络，直接用固定 dt 值

建议启动命令：

```bash
CUDA_VISIBLE_DEVICES=0 python dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/fixed_dt2_s1 \
  --steps 500000 --seed 1 \
  --compile False --device cuda:0 \
  --gate_enabled True --gate_fixed_dt 2
```

---
