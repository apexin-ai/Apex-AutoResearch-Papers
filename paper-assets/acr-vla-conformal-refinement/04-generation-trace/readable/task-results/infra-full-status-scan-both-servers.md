# infra full status scan both servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-scan-both-servers_20260513T193729_result.json`
- **Structured JSON:** [`cbbb3e0773813a4dd7ad.json`](../../sessions/cb/cbbb3e0773813a4dd7ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 服务器 1: bjb1-18228（autodl-4090x4）

### 1a. nvidia-smi 完整输出

```
Thu May 14 03:37:48 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090        On  |   00000000:98:00.0 Off |                  Off |
| 30%   39C    P2             74W /  450W |    1423MiB /  24564MiB |     22%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4090        On  |   00000000:A8:00.0 Off |                  Off |
| 30%   41C    P2             85W /  450W |    1543MiB /  24564MiB |     24%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 4090        On  |   00000000:B8:00.0 Off |                  Off |
| 30%   39C    P2             91W /  450W |    1543MiB /  24564MiB |     26%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 4090        On  |   00000000:D8:00.0 Off |                  Off |
| 30%   40C    P2             82W /  450W |    1543MiB /  24564MiB |     19%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A           73766      C   python                                 1414MiB |
|    1   N/A  N/A           69657      C   python                                 1534MiB |
|    2   N/A  N/A           69803      C   python                                 1534MiB |
|    3   N/A  N/A           69947      C   python                                 1534MiB |
+-----------------------------------------------------------------------------------------+
```

### 1a. 进程列表（关键进程）

| GPU | PID | 任务 | 命令 |
|-----|-----|------|------|
| 0 | 73766 | **eval-spatial-v5-full** | `python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42` |
| 1 | 69657 | **precompute-v4-shard0** | `python -u src/train_crm.py --precompute --benchmark spatial object --shard_id 0 --num_shards 3` |
| 2 | 69803 | **precompute-v4-shard1** | `python -u src/train_crm.py --precompute --benchmark spatial object --shard_id 1 --num_shards 3` |
| 3 | 69947 | **precompute-v4-shard2** | `python -u src/train_crm.py --precompute --benchmark spatial object --shard_id 2 --num_shards 3` |

### 1a. runs 目录

```
total 120
-rw-r--r-- 1 root root 6362 May 14 03:37 precompute-v4-shard0.log
-rw-r--r-- 1 root root 6189 May 14 03:37 precompute-v4-shard2.log
-rw-r--r-- 1 root root 6438 May 14 03:37 precompute-v4-shard1.log
-rw-r--r-- 1 root root 1365 May 14 03:37 eval-spatial-v5-full.log
-rw-r--r-- 1 root root 1435 May 14 03:16 eval-spatial-v4-full.log
-rw-r--r-- 1 root root 9963 May 14 02:47 precompute-v3-shard2.log
-rw-r--r-- 1 root root 9735 May 14 02:44 precompute-v3-shard1.log
-rw-r--r-- 1 root root 9733 May 14 02:44 precompute-v3-shard0.log
-rw-r--r-- 1 root root 1365 May 14 02:25 eval-spatial-v3-full.log
-rw-r--r-- 1 root root 2408 May 14 00:20 precompute-v2-shard1.log
-rw-r--r-- 1 root root 2328 May 14 00:20 precompute-v2-shard0.log
-rw-r--r-- 1 root root 2492 May 14 00:20 precompute-v2-shard2.log
-rw-r--r-- 1 root root 9003 May 13 20:56 precompute-shard0.log
-rw-r--r-- 1 root root 9032 May 13 20:54 precompute-shard2.log
-rw-r--r-- 1 root root 8867 May 13 20:53 precompute-shard1.log
```

### 1b. eval-spatial-v4-full 日志（最后 50 行）

```
[robosuite WARNING] No private macro file found! (__init__.py:7)
[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)
[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)
[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'vla_only', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}
[eval] Mode: vla_only, benchmark: spatial
[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...
Loading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights:   0%|          | 0/489 [00:00<?, ?it/s]
Loading weights:  59%|█████▉    | 290/489 [00:00<00:00, 2885.06it/s]
Loading weights: 100%|██████████| 489/489 [00:00<00:00, 3396.87it/s]
Reducing the number of VLM layers to 16 ...
Loading weights from local directory
[eval] Loading LIBERO spatial environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
bash: line 1: 69389 Killed                  python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1
```

**判断：被 Killed。** 加载完模型和环境后被系统杀死（可能 OOM），没有产出任何 eval 结果。没有成功率数字。

### 1c. eval-spatial-v5-full 日志（最后 50 行）

```
[robosuite WARNING] No private macro file found! (__init__.py:7)
[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)
[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)
[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'vla_only', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}
[eval] Mode: vla_only, benchmark: spatial
[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...
Loading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights:   0%|          | 0/489 [00:00<?, ?it/s]
Loading weights:  61%|██████▏   | 300/489 [00:00<00:00, 2984.93it/s]
Loading weights: 100%|██████████| 489/489 [00:00<00:00, 3384.01it/s]
Reducing the number of VLM layers to 16 ...
Loading weights from local directory
[eval] Loading LIBERO spatial environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5
```

**判断：正在正常运行。** 第 1 个任务的第 5/10 个 rollout，当前成功率 4/5 (80%)。进程 PID 73766 在 GPU 0 上活跃（22% util, 1414MiB）。

### 1d. precompute-v4 cache 目录结构

```
/root/autodl-tmp/crm_cache/
├── spatial/     (已完成 merge)
│   ├── manifest.json
│   ├── obs_features.pt      (46.7MB)
│   ├── k_samples.pt         (14.6MB)
│   ├── expert_actions.pt    (1.5MB)
│   └── partial_s{0,1,2}_*.pt  (27 个 partial 文件)
│   总计: 30 个 .pt 文件
│
└── object/      (正在生成中)
    ├── partial_s0_0_500.pt
    ├── partial_s0_500_1000.pt
    ├── partial_s1_0_500.pt
    ├── partial_s1_500_1000.pt
    ├── partial_s1_1000_1500.pt
    ├── partial_s2_0_500.pt
    └── partial_s2_500_1000.pt
    总计: 7 个 .pt 文件（正在增长）
```

**总 .pt 文件数：37 个（spatial 30 + object 7，object 仍在生成）**

旧路径：
- `/root/autodl-tmp/crm_cache_v3/` — 存在（spatial + object 子目录）
- `/root/autodl-tmp/crm_cache_v4/` — **不存在**

### 1e. precompute-v4 shard 日志

**shard0 (GPU 1)** — 最后 20 行：
```
[precompute] Saved [4000:4056] -> partial_s0_4000_4056.pt
[merge] Shard 2 not done (3500/4055), skipping merge.
[precompute] Loading LIBERO demos (object)...
[precompute] 14570 total samples from 100 trajectories.
[precompute] Shard 0/3: 4857 samples
[precompute] [object] 100/4857 (43s elapsed, ~2044s remaining, 0.43s/sample)
[precompute] [object] 200/4857 (88s elapsed, ~2051s remaining, 0.44s/sample)
[precompute] [object] 300/4857 (131s elapsed, ~1995s remaining, 0.44s/sample)
[precompute] [object] 400/4857 (175s elapsed, ~1946s remaining, 0.44s/sample)
[precompute] [object] 500/4857 (220s elapsed, ~1917s remaining, 0.44s/sample)
[precompute] Saved [0:500] -> partial_s0_0_500.pt
[precompute] [object] 600/4857 (263s elapsed, ~1865s remaining, 0.44s/sample)
[precompute] [object] 700/4857 (305s elapsed, ~1813s remaining, 0.44s/sample)
[precompute] [object] 800/4857 (352s elapsed, ~1783s remaining, 0.44s/sample)
[precompute] [object] 900/4857 (395s elapsed, ~1735s remaining, 0.44s/sample)
[precompute] [object] 1000/4857 (438s elapsed, ~1691s remaining, 0.44s/sample)
[precompute] Saved [500:1000] -> partial_s0_500_1000.pt
[precompute] [object] 1100/4857 (484s elapsed, ~1654s remaining, 0.44s/sample)
[precompute] [object] 1200/4857 (527s elapsed, ~1605s remaining, 0.44s/sample)
[precompute] [object] 1300/4857 (571s elapsed, ~1563s remaining, 0.44s/sample)
```
状态：spatial 已完成，正在跑 object，进度 1300/4857（~27%），速度 0.44s/sample

**shard1 (GPU 2)** — 最后 20 行：
```
[merge] Shard 0 not done (3500/4056), skipping merge.
[precompute] Loading LIBERO demos (object)...
[precompute] 14570 total samples from 100 trajectories.
[precompute] Shard 1/3: 4857 samples
[precompute] [object] 100/4857 (43s elapsed, ~2052s remaining, 0.43s/sample)
[precompute] [object] 200/4857 (86s elapsed, ~1999s remaining, 0.43s/sample)
[precompute] [object] 300/4857 (131s elapsed, ~1989s remaining, 0.44s/sample)
[precompute] [object] 400/4857 (173s elapsed, ~1930s remaining, 0.43s/sample)
[precompute] [object] 500/4857 (215s elapsed, ~1877s remaining, 0.43s/sample)
[precompute] Saved [0:500] -> partial_s1_0_500.pt
[precompute] [object] 600/4857 (259s elapsed, ~1838s remaining, 0.43s/sample)
[precompute] [object] 700/4857 (300s elapsed, ~1784s remaining, 0.43s/sample)
[precompute] [object] 800/4857 (341s elapsed, ~1731s remaining, 0.43s/sample)
[precompute] [object] 900/4857 (385s elapsed, ~1692s remaining, 0.43s/sample)
[precompute] [object] 1000/4857 (428s elapsed, ~1652s remaining, 0.43s/sample)
[precompute] Saved [500:1000] -> partial_s1_500_1000.pt
[precompute] [object] 1100/4857 (470s elapsed, ~1605s remaining, 0.43s/sample)
[precompute] [object] 1200/4857 (514s elapsed, ~1566s remaining, 0.43s/sample)
[precompute] [object] 1300/4857 (557s elapsed, ~1524s remaining, 0.43s/sample)
[precompute] [object] 1400/4857 (601s elapsed, ~1485s remaining, 0.43s/sample)
```
状态：spatial 已完成，正在跑 object，进度 1400/4857（~29%），速度 0.43s/sample

**shard2 (GPU 3)** — 最后 20 行：
```
[precompute] Saved [3500:4000] -> partial_s2_3500_4000.pt
[precompute] [spatial] 4055/4055 (1856s elapsed, ~0s remaining, 0.46s/sample)
[precompute] Saved [4000:4055] -> partial_s2_4000_4055.pt
[merge] All 3 shard(s) complete. Merging...
[merge] Saved 12167 samples + manifest to /root/autodl-tmp/crm_cache/spatial
[precompute] Loading LIBERO demos (object)...
[precompute] 14570 total samples from 100 trajectories.
[precompute] Shard 2/3: 4856 samples
[precompute] [object] 100/4856 (47s elapsed, ~2218s remaining, 0.47s/sample)
[precompute] [object] 200/4856 (93s elapsed, ~2155s remaining, 0.46s/sample)
[precompute] [object] 300/4856 (141s elapsed, ~2136s remaining, 0.47s/sample)
[precompute] [object] 400/4856 (187s elapsed, ~2079s remaining, 0.47s/sample)
[precompute] [object] 500/4856 (233s elapsed, ~2034s remaining, 0.47s/sample)
[precompute] Saved [0:500] -> partial_s2_0_500.pt
[precompute] [object] 600/4856 (281s elapsed, ~1993s remaining, 0.47s/sample)
[precompute] [object] 700/4856 (328s elapsed, ~1947s remaining, 0.47s/sample)
[precompute] [object] 800/4856 (377s elapsed, ~1910s remaining, 0.47s/sample)
[precompute] [object] 900/4856 (424s elapsed, ~1866s remaining, 0.47s/sample)
[precompute] [object] 1000/4856 (471s elapsed, ~1817s remaining, 0.47s/sample)
[precompute] Saved [500:1000] -> partial_s2_500_1000.pt
```
状态：spatial 已完成并触发了 merge（12167 samples），正在跑 object，进度 1000/4856（~21%），速度 0.47s/sample

---

## 服务器 2: bjb2-40593（autodl-4090）

### 2a. nvidia-smi 完整输出

```
Thu May 14 03:37:58 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:3D:00.0 Off |                  Off |
| 30%   38C    P2            104W /  425W |    9640MiB /  24564MiB |     99%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A           95460    C+G   python                                 4033MiB |
|    0   N/A  N/A          103778    C+G   python                                 5573MiB |
+-----------------------------------------------------------------------------------------+
```

### 2a. 进程列表（关键进程）

| GPU | PID | 任务 | 命令 |
|-----|-----|------|------|
| 0 | 95460 | **eval-vla-only (旧的 nohup)** | `python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --max_steps 300` |
| 0 | 103778 | **eval-object-v4-full** | `python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42` |

注意：GPU 0 上同时跑了两个 python 进程，共占 9640MiB，GPU 利用率 99%。

### 2a. runs 目录

```
total 12
-rw-r--r-- 1 root root 1466 May 14 03:14 eval-object-v4-full.log
-rw-r--r-- 1 root root 3333 May 13 17:44 plan_014-reconvla-baseline.log
-rw-r--r-- 1 root root 2735 May 13 14:34 plan_001-crm-smolvla.log
```

### 2b. eval-object-v4-full 日志（最后 50 行）

```
[robosuite WARNING] No private macro file found! (__init__.py:7)
[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)
[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)
[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'vla_only', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}
[eval] Mode: vla_only, benchmark: object
[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...
Loading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights:   0%|          | 0/489 [00:00<?, ?it/s]
Loading weights:  21%|██▏       | 105/489 [00:00<00:00, 1049.00it/s]
Loading weights:  43%|████▎     | 210/489 [00:00<00:00, 707.41it/s] 
Loading weights:  59%|█████▉    | 288/489 [00:00<00:00, 698.70it/s]
Loading weights:  79%|███████▊  | 385/489 [00:00<00:00, 788.06it/s]
Loading weights: 100%|██████████| 489/489 [00:00<00:00, 857.84it/s]
Reducing the number of VLM layers to 16 ...
Loading weights from local directory
[eval] Loading LIBERO object environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
```

**判断：正在运行但尚无 rollout 输出。** 模型和环境已加载完毕，应该正在跑第一个任务的 rollout。进程 PID 103778 活跃（5573MiB, GPU 99%）。启动时间 03:13，已运行约 25 分钟。

---

## 综合摘要

| 任务 | 服务器 | 状态 | 备注 |
|------|--------|------|------|
| eval-spatial-v4-full | bjb1 | **被 Killed** | 加载后被杀，无结果 |
| eval-spatial-v5-full | bjb1 GPU0 | **运行中** | Task 1: 4/5 成功 (80%) |
| precompute-v4 spatial | bjb1 GPU1-3 | **已完成** | 12167 samples, merged |
| precompute-v4 object | bjb1 GPU1-3 | **运行中** | shard0: 1300/4857, shard1: 1400/4857, shard2: 1000/4856, ~0.44s/sample, 预计还需 ~25-30 分钟 |
| eval-object-v4-full | bjb2 GPU0 | **运行中** | 模型已加载，尚无 rollout 输出 |
| eval-vla-only (旧 nohup) | bjb2 GPU0 | **仍在运行** | PID 95460, 与 eval-object-v4-full 共享 GPU（可能互相影响速度） |

---
