# check exp 059 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_059_status_20260524T061146_result.json`
- **Structured JSON:** [`a083d89ae7e35fef79fd.json`](../../sessions/a0/a083d89ae7e35fef79fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: running (elapsed 2h56m, training reached 105K steps, still collecting episodes)
CURRENT_STEP: 105000 (target reached)

--- ve_ratio trajectory ---
step=15K   ve_ratio=0.0287
step=25K   ve_ratio=0.1725
step=35K   ve_ratio=0.4037
step=45K   ve_ratio=0.7501
step=55K   ve_ratio=0.5805
step=65K   ve_ratio=1.2483
step=75K   ve_ratio=1.4905
step=85K   ve_ratio=3.3075  ← PEAK
step=95K   ve_ratio=0.6425
step=105K  ve_ratio=0.7557

VE_RATIO_PEAK: 3.3075 @ step 85K
VE_RATIO_FINAL: 0.7557 @ step 105K
NVE_PEAK: 4.84 (= 3.3075 / 0.683)
NVE_CLASSIFICATION: transient
  - NVE ≥ 1.5 from 65K-85K (20K steps), then drops to 0.94/1.11
  - Does NOT meet sustained threshold (≥ 35K steps)

EVAL_RETURN_FINAL: N/A (no eval/episode/score/mean in metrics)
TRAIN_RETURN (last episodes @ 108K): 19.8, 20.8, 86.6, 67.4
CHECKPOINT: checkpoint_25000.pt, checkpoint_75000.pt (no 100K/105K yet)
```

进程仍在运行，105K training steps 已完成但还在收集 episodes。ve_ratio 在 85K 处出现尖锐单点 peak (3.31, NVE=4.84)，随后迅速回落，属于 **transient** 而非 sustained CIVO。缺少 checkpoint_100000.pt，可能是 checkpoint_every=25000 会保存 25K/50K/75K/100K — 50K 和 100K 的 checkpoint 可能被覆盖或尚未写入。

---
