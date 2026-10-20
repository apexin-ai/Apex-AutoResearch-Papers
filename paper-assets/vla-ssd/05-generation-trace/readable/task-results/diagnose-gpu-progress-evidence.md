# diagnose gpu progress evidence

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_progress_evidence_20260521T045940_result.json`
- **Structured JSON:** [`3f4828c9b9d325e81b95.json`](../../sessions/3f/3f4828c9b9d325e81b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Raw output:

```
=== NVIDIA-SMI ===
Thu May 21 13:00:16 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   34C    P0             86W /  600W |   15149MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |
| N/A   35C    P0             88W /  600W |    8515MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          513523      C   python                                15140MiB |
|    1   N/A  N/A          526944      C   python                                 8506MiB |
+-----------------------------------------------------------------------------------------+
=== PROCESS STATUS ===
   PID %CPU %MEM     ELAPSED COMMAND
513523 2757  5.6    04:14:02 python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py
526944 1912  0.5    01:33:37 python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained
```

ps aux grep 匹配行（含 tmux wrapper）:
```
root  513512  0.0  0.0  ... tmux new-session -d -s libero_object_full_pipeline ...
root  513523 2757  5.6  ... python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py
root  526939  0.0  0.0  ... bash -c ... nora_goal_pipeline_v2 ...
root  526943  0.0  0.0  ... timeout 28800 env bash -c ... nora_goal_full_pipeline.py --conditions trained untrained
root  526944 1912  0.5  ... python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained
```

```
=== CUDA:0 LOG (Object) ===
[08:50:11]     4400/5000
[08:50:16]     4500/5000
[08:50:16]   Task 9/10: pick_up_the_orange_juice_and_place_it_in_the_basket
[08:50:21]     4600/5000
[08:50:26]     4700/5000
[08:50:31]     4800/5000
[08:50:35]     4900/5000
[08:50:40]     5000/5000
[08:50:40] Phase 1 done: 5000 samples
[08:50:40] Phase 1: 249.1s
[08:50:40] Phase 2: action R2 probing
[09:14:49]   L0: img_mean R2=0.6952  last_pre R2=0.5710
[11:12:52]   L8: img_mean R2=0.6727  last_pre R2=0.6753
/root/miniconda3/lib/python3.12/site-packages/sklearn/neural_network/_multilayer_perceptron.py:785: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
  warnings.warn(
```

```
=== CUDA:1 LOG (NORA Goal v2) ===
```
（原始 tail -15 全是 sklearn ConvergenceWarning，无进度信息。补拉过滤后的实际进度：）

```
[11:34:45]     2900/5000
[11:34:51]     3000/5000
[11:34:51]   Task 6/10: put_the_cream_cheese_in_the_bowl
[11:34:58]     3100/5000
[11:35:04]     3200/5000
[11:35:11]     3300/5000
[11:35:17]     3400/5000
[11:35:23]     3500/5000
[11:35:23]   Task 7/10: put_the_wine_bottle_on_the_rack
[11:35:30]     3600/5000
[11:35:37]     3700/5000
[11:35:43]     3800/5000
[11:35:50]     3900/5000
[11:35:56]     4000/5000
[11:35:56]   Task 8/10: put_the_wine_bottle_on_top_of_the_cabinet
[11:36:03]     4100/5000
[11:36:09]     4200/5000
[11:36:16]     4300/5000
[11:36:22]     4400/5000
[11:36:29]     4500/5000
[11:36:29]   Task 9/10: turn_on_the_stove
[11:36:35]     4600/5000
[11:36:42]     4700/5000
[11:36:48]     4800/5000
[11:36:55]     4900/5000
[11:37:02]     5000/5000
[11:37:02] Phase 1 done: 5000 samples
[11:37:02] Phase 1: 593.4s
[11:37:02] Phase 2: action R2 probing
[12:01:46]   L0: img_mean R2=0.6081  last_pre R2=0.5864
```

```
=== TMUX SESSIONS ===
libero_object_full_pipeline: 1 windows (created Thu May 21 08:46:14 2026)
nora_goal_pipeline_v2: 1 windows (created Thu May 21 11:26:39 2026)
```

---
