# diag 8b cell c episode v2 oom

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_8b_cell_c_episode_v2_oom_20260519T121253_result.json`
- **Structured JSON:** [`781cd38106e264c27235.json`](../../sessions/78/781cd38106e264c27235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diagnose_8b_cell_c_oom.md`。

**核心发现**：

1. **`ppo_max_token_len_per_gpu` 是完全的 no-op** -- `use_dynamic_bsz=False` 时代码根本不读这个参数，micro-batch 按 `ppo_micro_batch_size_per_gpu=1` 固定切分。这就是为什么 v2 改了参数但内存数字完全一样。

2. **OOM 位置**：`dp_actor.py:468 loss.backward()` -- actor update 的 backward pass，4 个 GPU 同时崩。失败的 8.76 GiB 分配是 lm_head 的 fp32 logits 梯度 (1, ~15475, 151936)。

3. **90 GiB 占用成因**：fp32 model params (8.2G) + gradients (8.2G) + logits tensor (4.7G) + checkpoint activations (4.6G) + FSDP buffers + 大量 allocator 碎片 (118G allocated vs 90G active)。

**推荐修复（方案 A）**：
```yaml
actor_rollout_ref:
  actor:
    use_dynamic_bsz: True
    ppo_max_token_len_per_gpu: 8192
    fsdp_config:
      param_offload: True
      entropy_from_logits_with_chunking: True
      entropy_checkpointing: True
```

`param_offload: True` 释放 ~8 GiB，加上原有 5 GiB 余量 = 13 GiB > 8.76 GiB 需求。代价是训练速度降低 10-20%。

---
