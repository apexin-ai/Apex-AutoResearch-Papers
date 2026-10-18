# ops cqa1 full check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-full-check_20260520T123934_result.json`
- **Structured JSON:** [`3b1f74814326dbb8b736.json`](../../sessions/3b/3b1f74814326dbb8b736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**1. Kill zombie PID**
```
=== PID 858906 killed ===
```

**2. GPU 状态**
```
866924, GPU-7ee85176-9244-062b-6f11-e7ff7d06c9ae, 4519 MiB
868193, GPU-a2a15ad4-2e8d-72f9-62e5-cd246f7fc5d0, 4271 MiB
894197, GPU-c242dd9c-f3b7-fad5-77f0-5017abd1a6cf, 4519 MiB
```

**3. X-VLA seed43 完成情况**
```
=== seed43 k=0.9 ===
no summary yet
=== seed43 k=0.7 ===
no summary yet
=== seed43 k=0.5 ===
no summary yet
```

**4. OFT CV 崩溃状态**
```
root     866917  0.0  0.0   4364  2024 ?        S    19:50   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && export MUJOCO_GL=egl && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 nohup python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.9 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.9_libero_object_seed43.json > logs/xvla_prune_k09_seed43.log 2>&1 & K09=$! CUDA_VISIBLE_DEVICES=2 nohup python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.7 --num_episodes 50 --seed 43 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.7_libero_object_seed43.json > logs/xvla_prune_k07_seed43.log 2>&1 & K07=$! CUDA_VISIBLE_DEVICES=3 nohup python -u compute_openvla_oft_cv.py > logs/oft_cv_computation.log 2>&1 & OFT=$! echo "K09=$K09 K07=$K07 OFT=$OFT"
```

3 个 GPU 在用（各 ~4.3-4.5 GiB）。seed43 三个 k 值都还没产出 summary。OFT CV 进程（PID 866917 的子进程）仍在运行中。

---
