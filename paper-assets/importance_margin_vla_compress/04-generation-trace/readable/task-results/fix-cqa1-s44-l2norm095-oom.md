# fix cqa1 s44 l2norm095 oom

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-s44-l2norm095-oom_20260527T224041_result.json`
- **Structured JSON:** [`267608622e65bf0dfcb6.json`](../../sessions/26/267608622e65bf0dfcb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行正常，正在 CPU 加载 π0.5 模型（~32GB RAM 已分配）。模型上 GPU 后显存会分配约 10GB，GPU 1 有 24GB 容量，无 OOM 风险。

**部署结果汇总：**
- **tmux session**: `eval_pi05_l2norm_k095_long_seed44_strict_cqa1`
- **PID**: 797637（python 进程），797633（bash 父进程）
- **GPU**: 物理卡 1（`CUDA_VISIBLE_DEVICES=1`），24564MiB 全空闲
- **状态**: R (running)，模型 CPU 加载中，加载完成后自动移至 GPU 1
- **log**: `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_long_seed44_strict_cqa1.log`
- **环境变量**: `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1` 均已确认

GPU 1 完全空闲（0 进程、1MiB 显存），不会重复之前 OOM 的问题。

---
