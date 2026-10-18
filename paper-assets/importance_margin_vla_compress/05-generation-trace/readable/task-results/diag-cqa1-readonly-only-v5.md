# diag cqa1 readonly only v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cqa1-readonly-only-v5_20260526T230251_result.json`
- **Structured JSON:** [`c5f7cb70893fb1d5f2e1.json`](../../sessions/c5/c5f7cb70893fb1d5f2e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部诊断数据已收集。以下是完整报告：

---

```
=== Step 1: 基础连接 ===
命令: cat /etc/hostname
输出:
autodl-container-61bb4e82b9-0e2cbbac

注: hostname/whoami 命令被 ssh_read_only allowlist 阻拦。
从 /etc/hostname 可见这是一个 AutoDL 容器。

=== Step 2: GPU 状态 ===
命令: nvidia-smi
输出:
Wed May 27 07:03:28 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |
| 30%   31C    P8             12W /  425W |       1MiB /  24564MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:38:00.0 Off |                  Off |
|  0%   29C    P8             10W /  425W |       1MiB /  24564MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |
| 30%   48C    P2            164W /  425W |   10519MiB /  24564MiB |     24%      Default |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |
| 30%   37C    P2            156W /  425W |   10225MiB /  24564MiB |     29%      Default |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    2   N/A  N/A          790017    C+G   python                                10500MiB |
|    3   N/A  N/A          732826    C+G   python                                10207MiB |
+-----------------------------------------------------------------------------------------+

=== Step 3: conda 环境 ===
命令: ls /root/miniconda3/bin/python && /root/miniconda3/bin/python --version
输出:
/root/miniconda3/bin/python
Python 3.12.3

=== Step 4: 项目路径 ===
命令: ls /root/autodl-tmp/importance_margin_vla_compress/
输出:
__pycache__           eval_pi05_libero.py           run_eval_fullft_100k.sh
_lerobot_compat.py    eval_pi05_pruning_libero.py   run_eval_v8_fixed.sh
analyze_gate.py       eval_pi05_zeromask_ablation.py run_mvp.sh
artifacts             eval_random_prune_smolvla.py   run_sweep_gpu1.sh
checkpoints           eval_random_prune_smolvla_spatial.py  ...
configs               eval_results                   smart_compress_module.py
docs                  eval_sim.py                    train.py
evaluate.py           eval_smart_compress.py         train_smart_compress.py
imm                   eval_success_rate.py           wandb
logs                  ...
（共 ~100+ 文件，项目目录存在且完整）

=== Step 5: logs 目录 ===
命令: ls -lt /root/autodl-tmp/importance_margin_vla_compress/logs/
输出（最近 10 个）:
-rw-r--r-- 1 root root   4877 May 27 07:01 eval_pi05_random_k07_long_seed42.log
-rw-r--r-- 1 root root   2870 May 27 07:00 eval_pi05_l2norm_k085_long_seed42.log
-rw-r--r-- 1 root root   7944 May 27 06:40 eval_pi05_attention_k07_long_seed42.log
-rw-r--r-- 1 root root   7811 May 27 06:16 eval_pi05_l2norm_k07_long_seed42.log
-rw-r--r-- 1 root root   7945 May 26 22:37 eval_attn_k05_long_s42.log
-rw-r--r-- 1 root root   7945 May 26 21:27 eval_pi05_attention_k075_long_seed42_v2.log
-rw-r--r-- 1 root root   7825 May 26 20:57 eval_pi05_l2norm_k075_long_seed42.log
-rw-r--r-- 1 root root   3948 May 26 20:00 eval_pi05_attention_k085_long_seed42.log
-rw-r--r-- 1 root root   8024 May 26 05:45 pi05_zeromask_l2norm_k09_object_seed42.log
-rw-r--r-- 1 root root   7983 May 26 05:43 pi05_zeromask_random_k09_object_seed42.log
（共 ~150+ 日志文件）

=== Step 6: tmux ===
命令: find /usr/bin -name tmux
输出:
/usr/bin/tmux

注: tmux ls 被 allowlist 阻拦，但从 ps aux 可看到活跃的 tmux session:
- tmux session "eval_attn_k05_long_s42" (PID 262559)

=== Step 7: torch 测试 ===
命令: /root/miniconda3/bin/python -c "print(__import__('torch').__version__)"
输出:
2.8.0+cu128

命令: /root/miniconda3/bin/python -c "print(__import__('torch').cuda.is_available())"
输出:
True

=== Step 8: eval 脚本 ===
命令: find /root/autodl-tmp/importance_margin_vla_compress/ -name "*.py" -path "*eval*"
输出:
/root/autodl-tmp/importance_margin_vla_compress/evaluate.py
/root/autodl-tmp/importance_margin_vla_compress/scripts/eval_checkpoint_trajectory.py
/root/autodl-tmp/importance_margin_vla_compress/eval_sim.py
/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate.py
/root/autodl-tmp/importance_margin_vla_compress/eval_libero_10k_diversity.py
/root/autodl-tmp/importance_margin_vla_compress/eval_libero_10k_sim.py
/root/autodl-tmp/importance_margin_vla_compress/eval_libero_100k_sr.py
/root/autodl-tmp/importance_margin_vla_compress/eval_libero_fullft_100k.py
/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_geometric_prior_k07.py
/root/autodl-tmp/importance_margin_vla_compress/eval_geometric_prior.py
/root/autodl-tmp/importance_margin_vla_compress/eval_geometric_prior_k05.py
/root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress.py
/root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_random_prune_smolvla.py
/root/autodl-tmp/importance_margin_vla_compress/eval_random_prune_smolvla_spatial.py
/root/autodl-tmp/importance_margin_vla_compress/eval_official_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_smart_compress.py
/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_pruning_libero.py
/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_zeromask_ablation.py
/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py

命令: head -3 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log
输出:
2026-05-27 05:08:37,239 Config: suite=libero_10, prune=random, keep=0.7, eps=50, gpu=0
2026-05-27 05:08:37,239 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...
The PI05 model is a direct port of the OpenPI implementation. 

=== Step 8b: 运行中的 python 进程 ===
命令: ps aux
输出（python 相关，摘要）:
- PID 732826 (GPU 3): python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0  (639% CPU, 运行中)
- PID 790017 (GPU 2): python (从 nvidia-smi 可见占用 10500MiB，但 ps 输出截断未显示完整命令)
- PID 819: tensorboard --port 6007
- PID 821: jupyter-lab
- tmux session: eval_attn_k05_long_s42

=== 结论 ===
连接的服务器是: cqa1-33015 ✓
判断依据:
- GPU: 4x NVIDIA GeForce RTX 4090 D (24564MiB each) — 不是 westd-27271 的 2x RTX PRO 6000 (97GB)
- hostname: autodl-container-61bb4e82b9-0e2cbbac（AutoDL 容器）
- 环境: Python 3.12.3, torch 2.8.0+cu128, CUDA 可用
- 当前活跃任务: 2 个 eval 进程分别在 GPU 2 和 GPU 3 上运行，GPU 0 和 GPU 1 空闲
```

---
