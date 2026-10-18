# check cqa1 gpu1 imm100k status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_gpu1_imm100k_status_20260517T010718_result.json`
- **Structured JSON:** [`b221a6536140077b34f3.json`](../../sessions/b2/b221a6536140077b34f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

```
=== IMM 100K 状态 ===
GPU 1: 空闲确认 (0MiB, 0%)
训练进程: ✅ 已完成 (stage: "complete")
最终 step: Stage1 10000/10000 + Stage2 20000/20000 = 30000 total

=== Checkpoint 信息 ===
路径: checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt
大小: 878.2 MB
元数据: stage="complete", 只含 model_state_dict + config
Baseline source: checkpoints/libero_full_ft/step_099999/checkpoint.pt (100K Full FT, step=99999, seed=42, imm=disabled)

=== 完整 Checkpoint 列表 ===
Stage 1: step_002000 ~ step_008000 (每个 898MB) + stage1_done (879MB)
Stage 2: step_002000 ~ step_018000 (每个 1.3GB) + final (879MB)

=== Config 确认 ===
libero_imm_twostage_fullft.yaml:
  - baseline_checkpoint: "checkpoints/libero_full_ft/step_099999/checkpoint.pt"
  - stage1_steps: 10000, stage2_steps: 20000
  - k_ratio: 0.5, delta: 0.3, seed: 42
  - output_dir: "checkpoints/libero_imm_twostage_fullft"

Baseline checkpoint (libero_full_ft/step_099999) 确认:
  - total_steps: 100000, step: 99999
  - imm.enabled: False (纯 Full FT baseline)
  - seed: 42

=== 结论 ===
IMM Full FT 100K seed=42 训练已正常完成。它基于 100K Full FT baseline（step_099999），
完成了 Stage1(ACIS 10K) + Stage2(Expert FT 20K) 全部流程。
Final checkpoint 在: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt
```

当前 GPU 1 空闲可用。另外两个正在运行的 IMM 训练：
- `libero_imm_fullft_seed0`: GPU 2, Stage2 step 16700/20000
- `libero_imm_fullft_k07`: GPU 3, Stage2 step 13200/20000

---
