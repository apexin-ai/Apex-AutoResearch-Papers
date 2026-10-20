# status quick ssh read 037 038 039

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_quick_ssh_read_037_038_039_20260521T194931_result.json`
- **Structured JSON:** [`249945b3282df43efdfe.json`](../../sessions/24/249945b3282df43efdfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-45299 ===
进程: 无 dreamer.py 进程
exp_037 最后3行:
{"step": 224000, "dataset_size": 112000.0, "train_return": 109.60469623887911, "train_length": 500.0, "train_episodes": 224.0}
{"step": 224000, "dataset_size": 112000.0, "train_return": 105.09554262290476, "train_length": 500.0, "train_episodes": 224.0}
{"step": 224000, "dataset_size": 112000.0, "train_return": 104.69793017115444, "train_length": 500.0, "train_episodes": 224.0}

=== bjb1-40020 ===
进程:
  - exp_027_tcn_walker_s0_sigma02 (tmux session, 残留)
  - exp_038_dual_critic_walker_s2: python -u dreamer.py ... --dual_critic True --seed 2 (运行中, CPU 596%)
  - exp_039_narrow_dual_critic_walker_s1: python -u dreamer.py ... --narrow_dual_critic True --seed 1 (运行中, CPU 618%)

exp_038 最后3行:
{"step": 208000, "dataset_size": 104000.0, "train_return": 114.9061508178711, "train_length": 500.0, "train_episodes": 208.0}
{"step": 208000, "dataset_size": 104000.0, "train_return": 89.86087036132812, "train_length": 500.0, "train_episodes": 208.0}
{"step": 208000, "dataset_size": 104000.0, "train_return": 123.50553894042969, "train_length": 500.0, "train_episodes": 208.0}

exp_039 最后3行:
{"step": 96000, "dataset_size": 48000.0, "train_return": 118.68193054199219, "train_length": 500.0, "train_episodes": 96.0}
{"step": 96000, "dataset_size": 48000.0, "train_return": 42.63587188720703, "train_length": 500.0, "train_episodes": 96.0}
{"step": 96000, "dataset_size": 48000.0, "train_return": 92.83245086669922, "train_length": 500.0, "train_episodes": 96.0}
```

---
