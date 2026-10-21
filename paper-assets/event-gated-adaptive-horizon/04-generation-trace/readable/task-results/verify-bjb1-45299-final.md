# verify bjb1 45299 final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb1-45299-final_20260522T030513_result.json`
- **Structured JSON:** [`c427540cd11411b907a2.json`](../../sessions/c4/c427540cd11411b907a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### === NVIDIA-SMI ===
```
Fri May 22 11:05:33 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   39C    P0            135W /  600W |    4063MiB /  97887MiB |     22%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   42C    P0            125W /  600W |    3017MiB /  97887MiB |     23%      Default |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|    0   N/A  N/A           51103      G   python                                  515MiB |
|    0   N/A  N/A           52397    C+G   python                                 3519MiB |
|    1   N/A  N/A           51103      C   python                                 3008MiB |
+-----------------------------------------------------------------------------------------+
```

### === DREAMER PROCESSES ===
```
PID 52397 — python -u dreamer.py --task dmc_cheetah_run  --seed 1 --device cuda:0 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah
PID 51103 — python -u dreamer.py --task dmc_walker_walk  --seed 3 --device cuda:0 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3
```

### === EXP_040 METRICS ===
```
-rw-r--r-- 1 root root 2794 May 22 11:02 metrics.jsonl

step: 5000, eval_return: 13.48, value1_mean: 0.00076, value2_mean: 0.00076, gate_dt_mean: 2.0
```

### === EXP_041 METRICS ===
```
-rw-r--r-- 1 root root 7172 May 22 11:03 metrics.jsonl

step: 20000, train_return: 212.47 (latest episode), train_episodes: 20
```

---
