# eval rasp v9 checkpoints and unpruned grpo prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rasp_v9_checkpoints_and_unpruned_grpo_prep_20260516T014836_result.json`
- **Structured JSON:** [`069e13bbdf8f33afe0da.json`](../../sessions/06/069e13bbdf8f33afe0da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

## 报告

### Part 1: Unpruned GRPO（westd cuda:1）

**已经在运行了。** westd cuda:1 上已有 Unpruned GRPO v2 训练进程（PID 75381）：

```
/root/miniconda3/bin/python src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline/ \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 \
  --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 \
  --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true \
  --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 \
  --max_steps 100 --save_steps 5 --save_total_limit 10 --run_name grpo_unpruned_v2
```

- **进度**: step 2/100, ~30.76s/step, 预计 ~50 分钟完成
- **GPU 占用**: 47,314 MiB
- **脚本**: `train_grpo_v5.py`（不是 `grpo_stage2.py`，后者不存在）

westd cuda:0 也在忙——运行 `eval_gsm8k.py` 评估 sft_unpruned_baseline（17,654 MiB）。

| 项目 | 值 |
|------|-----|
| 1. SFT 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline/` |
| 1. SFT 模型大小 | **15GB**（model.safetensors 14.2 GiB） |
| 2. 启动命令 | 已在运行（见上） |
| 3. 磁盘空间 | **141GB 可用** / 250GB 总量（44% 使用），充足 |
| 4. Dry-run | 无需——模型已加载并在训练 |

### Part 2: RASP v9 Checkpoint（westb cuda:0）

RASP v9 **仍在训练**（PID 566666），未崩溃。output.log 中的磁盘满错误来自之前的 `grpo_unpruned_baseline` run（03:25 崩溃，输出目录已不存在），与 v9 无关。

| 项目 | 值 |
|------|-----|
| 5. Checkpoint | checkpoint-5, checkpoint-10, checkpoint-15 各 **27GB** |
| 进度 | step 15/30, ~401s/step, 预计再 ~100 分钟完成 |
| save_total_limit | 5（最多再存 2 个 checkpoint，磁盘 99GB 可用，够用） |
| 6. westb↔westd 直连 | **不能**（Permission denied） |
| 7. 评估方案 | 无法 scp，等 v9 完成后**在 westb 本地 eval** |

### 总结

无需任何操作——Unpruned GRPO v2 已在 westd:1 运行，RASP v9 正常在 westb:0 推进。两台机器不能直连，v9 checkpoint 需在 westb 本地评估。

---
