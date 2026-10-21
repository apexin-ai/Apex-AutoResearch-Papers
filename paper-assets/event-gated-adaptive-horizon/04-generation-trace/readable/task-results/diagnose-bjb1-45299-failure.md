# diagnose bjb1 45299 failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-45299-failure_20260522T023856_result.json`
- **Structured JSON:** [`12ac911b7d40a50e3603.json`](../../sessions/12/12ac911b7d40a50e3603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是全部诊断原始结果：

---

### 1. TMUX SESSIONS
`tmux ls` 被 ssh_read_only 拦截（不在白名单）。但从 `ps aux` 可见 tmux session：
```
tmux new-session -d -s exp_041_dual_critic_walker_s3 ...
```

---

### 2. GPU STATUS
```
Fri May 22 10:39:15 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   29C    P8             36W /  600W |     526MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   38C    P0            123W /  600W |    3013MiB /  97887MiB |     21%      Default |
+-----------------------------------------+------------------------+----------------------+

| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    0   N/A  N/A           51103      G   python                                  515MiB |
|    1   N/A  N/A           51103      C   python                                 3004MiB |
+-----------------------------------------------------------------------------------------+
```

---

### 3. DREAMER PROCESSES (from ps aux)
```
PID 51103  3060 %CPU  python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3
```
这是 exp_041，正在 GPU1 上跑，GPU-Util 21%，进程活跃。

---

### 4. RECENT LOGS — 目录列表
```
-rw-r--r-- 1 root root   2443 May 22 03:51 exp_040_wide_dual_critic_cheetah.log
-rw-r--r-- 1 root root   2663 May 22 10:38 exp_041_dual_critic_walker_s3.log
```

---

### 5. exp_040 LOG (tail -50)
```
[SEED CHECK] config.seed = 0
Logdir logdir/exp_040_wide_dual_critic_cheetah
Create envs.
Action Space Box(-1.0, 1.0, (6,), float32)
Prefill dataset (2500 steps).
[0] dataset_size 2000.0 / train_return 7.9 / train_length 500.0 / train_episodes 4.0
...
Optimizer model_opt has 16933913 variables.
Traceback (most recent call last):
  File "/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py", line 447, in &lt;module>
    main(parser.parse_args(remaining))
  File "/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py", line 352, in main
    agent = Dreamer(
  File "/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py", line 96, in __init__
    self._task_behavior = models.ImagBehavior(config, self._wm)
  File "/root/autodl-tmp/event-gated-adaptive-horizon/models.py", line 500, in __init__
    assert not (getattr(config, "wide_critic", False) and getattr(config, "dual_critic", False)), \
AssertionError: wide_critic and dual_critic are mutually exclusive
EXIT_CODE=1
```

---

### 6. exp_041 LOG (tail -50)
```
[SEED CHECK] config.seed = 3
Logdir logdir/exp_041_dual_critic_walker_s3
Create envs.
Action Space Box(-1.0, 1.0, (6,), float32)
Prefill dataset (500 steps).
Logger: (5000 steps).
Simulate agent.
Encoder MLP shapes: {'height': (1,), 'orientations': (14,), 'velocity': (9,)}
Decoder MLP shapes: {'height': (1,), 'orientations': (14,), 'velocity': (9,)}
Optimizer model_opt has 16948256 variables.
Optimizer actor_opt has 1056780 variables.
Optimizer value_opt has 1181439 variables.
Optimizer value2_opt has 1181439 variables.
[5000]
Start evaluation.
[5000] eval_return 36.0 / eval_length 500.0 / eval_episodes 10.0
Start training.
```
（exp_041 正在正常运行中，PID 51103）

---

### 7. LOGDIR STATUS

**exp_040:**
```
total 24
drwxr-xr-x  4 root root  163 May 22 03:51 .
-rw-r--r--  1 root root  992 May 22 03:51 events.out.tfevents...
-rw-r--r--  1 root root  467 May 22 03:51 metrics.jsonl
drwxr-xr-x  2 root root   10 May 22 03:51 eval_eps
drwxr-xr-x  2 root root 4096 May 22 03:51 train_eps
```

**exp_041:**
```
total 36
drwxr-xr-x  4 root root 4096 May 22 10:38 .
-rw-r--r--  1 root root  992 May 22 03:51 events.out.tfevents...36223.0
-rw-r--r--  1 root root  264 May 22 10:38 events.out.tfevents...51103.0
-rw-r--r--  1 root root  582 May 22 10:38 metrics.jsonl
drwxr-xr-x  2 root root 4096 May 22 03:51 train_eps
drwxr-xr-x  2 root root 4096 May 22 10:38 eval_eps
```

---

### 8. METRICS.JSONL

**exp_040 (只有 prefill 数据，step=0，然后崩溃):**
```json
{"step": 0, "dataset_size": 2000.0, "train_return": 7.877443632460199, "train_length": 500.0, "train_episodes": 4.0}
{"step": 0, "dataset_size": 2000.0, "train_return": 6.384448079152207, "train_length": 500.0, "train_episodes": 4.0}
{"step": 0, "dataset_size": 2000.0, "train_return": 5.214318133541383, "train_length": 500.0, "train_episodes": 4.0}
{"step": 0, "dataset_size": 2000.0, "train_return": 6.51720693288371, "train_length": 500.0, "train_episodes": 4.0}
```

**exp_041 (刚跑到 step 5000 eval):**
```json
{"step": 0, "dataset_size": 2000.0, "train_return": 36.864967346191406, "train_length": 500.0, "train_episodes": 4.0}
{"step": 0, "dataset_size": 2000.0, "train_return": 30.628192901611328, "train_length": 500.0, "train_episodes": 4.0}
{"step": 0, "dataset_size": 2000.0, "train_return": 35.381988525390625, "train_length": 500.0, "train_episodes": 4.0}
{"step": 5000}
{"step": 5000, "eval_return": 36.027835845947266, "eval_length": 500.0, "eval_episodes": 10.0}
```

---

### 9. OOM/KERNEL ERRORS
`dmesg` 被 ssh_read_only 拦截。

---

### 10. NOHUP
`/root/nohup.out` 不存在。

---

### 11. DISK SPACE
```
Filesystem      Size  Used Avail Use% Mounted on
overlay          30G   16G   15G  52% /
/dev/sda2       439G   17G  399G   5% /usr/bin/nvidia-smi  (autodl-tmp)
shm             120G     0  120G   0% /dev/shm
```

---

### 12. CONDA ENV
未单独执行（需 `&&`），但从 ps aux 可确认 PID 51103 用的是 `/root/miniconda3` 下的 python。

---

**根因已清楚：**

- **exp_040 失败原因**：`models.py:500` 的 assert —— `wide_critic` 和 `dual_critic` 同时为 True，代码断言互斥，直接 crash，`EXIT_CODE=1`。这是配置冲突，实验名叫 `wide_dual_critic` 就说明两个 flag 都传了。
- **exp_041 当前状态**：正在正常运行（PID 51103, GPU1, 21% util, step 5000 已完成 eval），不存在失败。这是最新一次部署，看起来是修正了配置后重新跑的。

---
