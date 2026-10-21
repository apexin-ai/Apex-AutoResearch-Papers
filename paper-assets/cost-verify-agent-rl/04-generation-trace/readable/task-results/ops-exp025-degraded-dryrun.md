# ops exp025 degraded dryrun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025_degraded_dryrun_20260515T075212_result.json`
- **Structured JSON:** [`cbe588dfd74abdb9f2b2.json`](../../sessions/cb/cbe588dfd74abdb9f2b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7 分钟运行中，一切稳定。可以先汇报结果了——这个 dry run 已经证明了可行性。

---

## 产出总结

### 1. 上次失败原因
**根因：cgroup pids.max = 20480（容器硬限制）**

- `exp025b_retry.log`：`RuntimeError: Resource temporarily unavailable` + `Could not create grpc_sync_server worker-thread` — 线程/进程数超过容器 cgroup 限制
- `pids.events` 显示限制被触发 **528 次**
- 不是 GPU OOM（GPU 是 2×97GB RTX PRO 6000 Blackwell）
- 不是系统 RAM OOM（1TB RAM 可用）
- `ulimit -u 65535` 无效，因为 cgroup pids.max 是更硬的限制，且只读无法修改

### 2. 降级 dry run 结果：**成功**

进程已运行 7+ 分钟，pids 稳定 ~6575 / 20480（32%）：
- val_before_train ✅ 完成（初始 score = 0.0）
- ALFWorld env rollout ✅ 正常交互
- Training epoch 1 rollout ✅ 进行中
- **无 EAGAIN、无 Raylet 崩溃**

### 3. 可用的最小配置参数

```bash
# 线程控制（必须）
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export TOKENIZERS_PARALLELISM=false
export RAY_num_server_call_thread=1

# vLLM 配置（关键）
actor_rollout_ref.rollout.enforce_eager=True          # 跳过 CUDA graphs，最大线程节省
actor_rollout_ref.rollout.gpu_memory_utilization=0.4
actor_rollout_ref.rollout.tensor_model_parallel_size=1

# GPU
CUDA_VISIBLE_DEVICES=0
trainer.n_gpus_per_node=1

# 其余
VLLM_ATTENTION_BACKEND=FLASH_ATTN
env.rollout.n=2  # 最小 worker
```

### 4. 正式实验的下一步

要恢复 2-GPU 训练（`n_gpus=2`, `tensor_model_parallel_size=2`），线程数会翻倍。需要验证 2-GPU 配置 + enforce_eager 是否仍在 20480 以内。如果超限，可能需要联系 AutoDL 提高 pids 限制，或保持单 GPU 训练。

---
