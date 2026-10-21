# code unified eval pipeline

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_eval_pipeline_20260522T040903_result.json`
- **Structured JSON:** [`ad1e55f47082424d2048.json`](../../sessions/ad/ad1e55f47082424d2048.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在输出完整结果。

---

## 产出汇总

### 1. westd-47453 HF Checkpoint 清单

| # | Exp ID | Path | Size | safetensors |
|---|--------|------|------|-------------|
| 1 | SFT baseline | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` | ~3.8G | model.safetensors |
| 2 | seed4 step15 | `.../exp029-seed4/global_step_15_hf` | 3.8G | model.safetensors |
| 3 | seed5 step10 | `.../exp029-seed5/global_step_10_hf` | 3.8G | model.safetensors |
| 4 | seed6 step15 | `.../exp029-seed6/global_step_15_hf` | 3.8G | model.safetensors |
| 5 | seed8 step5 | `.../qwen_exp029_seed8_step5_hf` | 3.8G | model.safetensors |
| 6 | intervention C step5 | `.../intervention_c_hard_cap_step5_hf` | 3.8G | model.safetensors |
| 7 | intervention C step7 | `.../intervention_c_hard_cap_step7_hf` | 3.8G | model.safetensors |
| 8 | high-KL step5 | `.../exp029_seed7_high_kl_step5_hf` | 3.8G | model.safetensors |
| 9 | high-KL step7 | `.../exp029_seed7_high_kl_step7_hf` | 3.8G | model.safetensors |
| 10 | C' step5 | `.../qwen_c_prime_step5_hf` | 3.8G | model.safetensors |

另有 FSDP 格式（未转换）：`exp029-seed8/global_step_5`（已有对应 HF）

### 2. eval_checkpoint.py 接口

已修改，新增 `--eval_dataset` 参数：

```bash
python3 scripts/eval_checkpoint.py \
    --checkpoint_path &lt;PATH> \
    --num_episodes 134 \
    --max_steps 50 \
    --temperature 0.4 \
    --eval_dataset eval_out_of_distribution \
    --gpu 0 \
    --gpu_memory_utilization 0.85 \
    --output_dir /root/autodl-tmp/eval_results/
```

两台服务器（westd + bjb1）都已 patch。

### 3. Batch eval 脚本

`/root/cost-verify-agent-rl/scripts/batch_ood_eval.sh` 已创建于 westd，dry-run 通过。

```bash
bash scripts/batch_ood_eval.sh --gpu 0          # 实际运行
bash scripts/batch_ood_eval.sh --gpu 0 --dry-run # 仅预览
```

功能：串行跑 10 个 checkpoint 的 134-task OOD eval，自动跳过已完成项，汇总到 `table1_ood_results.json`。

### 4. Table 1 Checkpoint 需求 vs 可用状态

| Table 1 行 | 状态 | 位置 |
|------------|------|------|
| SFT baseline | **westd 可用** | `qwen3_exp021_ragen_sft_v4` |
| Seed 1 (step 15) | **不存在** | 两台服务器均未找到 |
| Seed 3 (step 15) | **不存在** | westd 有空目录 `exp029_seed3/`，无 checkpoint |
| Seed 4 (step 15, collapsed) | **westd 可用** | `exp029-seed4/global_step_15_hf` |
| Seed 5 (step 10) | **westd 可用** | `exp029-seed5/global_step_10_hf`；bjb1 已有旧 OOD 结果(37.3%) |
| Seed 6 (step 15) | **westd 可用** | `exp029-seed6/global_step_15_hf`；bjb1 已有旧 OOD 结果(29.9%) |
| Seed 7 (step 7, collapsed) | **不存在** | 仅有 high-KL 变体，无原始 seed7 |
| Seed 8 (step 5, pre-collapse) | **westd 可用** | `qwen_exp029_seed8_step5_hf` |
| Intervention C step5 | **westd 可用** | `intervention_c_hard_cap_step5_hf` |
| Intervention C step7 | **westd 可用** | `intervention_c_hard_cap_step7_hf` |
| High-KL step5 | **westd 可用** | `exp029_seed7_high_kl_step5_hf` |
| High-KL step7 | **westd 可用** | `exp029_seed7_high_kl_step7_hf` |
| C' step5 | **westd 可用** | `qwen_c_prime_step5_hf` |
| Seed 2048 | **待训练** | — |

**缺失 checkpoint：Seed 1、Seed 3、原始 Seed 7（非 high-KL）。** 这三个需要确认是否曾训练过、是否有 FSDP 原始 checkpoint 需要转换，或者从 Table 1 中移除。

**注意**：bjb1 上 seed5/seed6 的旧 OOD 结果使用了不同的 eval 脚本（`eval_ood_seed5.py`，用 `&lt;answer>` tag 格式），与统一 pipeline 的 message format 不同。建议全部用 `eval_checkpoint.py` 重跑以保证一致性。

---
