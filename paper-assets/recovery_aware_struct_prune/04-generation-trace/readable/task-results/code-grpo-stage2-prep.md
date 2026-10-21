# code grpo stage2 prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_stage2_prep_20260515T003122_result.json`
- **Structured JSON:** [`3fb5649a53971d2635b4.json`](../../sessions/3f/3fb5649a53971d2635b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集到所有必要信息。现在总结结果和准备好的命令。

---

## GRPO Stage 2 代码准备总结

### 验证结果

1. **SFT checkpoint 完整性** ✓
   - `sft_rasp_20/`：config.json, tokenizer, model.safetensors（12.3GB），保留 `per_layer_intermediate_size` 非均匀结构
   - `sft_standard_20/`：同上

2. **模型加载** ✓
   - `load_pruned_model` 正确识别非均匀 MLP（range [8128, 18944]）
   - 加载到 cuda:0 成功，6161.9M 参数
   - 可生成 token（greedy decode 通过）

3. **GRPO 脚本兼容性** ✓
   - 脚本接受 SFT checkpoint 路径，成功走到 "Starting GRPO training"
   - 被 kill 是因为评估进程占用 GPU 显存导致内存不足，**不是代码问题**

4. **Dry-run 未完成** ⚠️
   - 当前 GPU 0/1 各有一个 `quick_eval.py` 进程（评估 SFT 模型），各占 ~12.7GB + 91-96% GPU util
   - GRPO 需要 ~65GB 显存（model + ref_model + optimizer + gradients），与评估进程共存时峰值超限
   - **需等评估完成后再做 dry-run / 正式训练**

### GRPO Stage 2 训练命令

之前 GRPO 参数推算：lr=1e-6, batch=2, accum=8, temp=0.7, num_gen=4, max_samples=2000, max_completion_length=4096, 约 500 steps

**RASP SFT → GRPO（GPU 0）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/recovery_aware_struct_prune

nohup bash -c 'CUDA_VISIBLE_DEVICES=0 python src/train_grpo.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/ \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_sft_rasp_20 \
  --gpu 0 \
  --max_samples 2000 \
  --num_train_epochs 4 \
  --max_completion_length 4096 \
  --run_name grpo_sft_rasp_20' \
  > /root/runs/recovery_aware_struct_prune/grpo_sft_rasp_20.log 2>&1 &
```

**Standard SFT → GRPO（GPU 1）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/recovery_aware_struct_prune

nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python src/train_grpo.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/ \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_sft_standard_20 \
  --gpu 1 \
  --max_samples 2000 \
  --num_train_epochs 4 \
  --max_completion_length 4096 \
  --run_name grpo_sft_standard_20' \
  > /root/runs/recovery_aware_struct_prune/grpo_sft_standard_20.log 2>&1 &
```

### 启动前提
- 等待 `quick_eval.py` 评估进程完成（PID 260651 GPU0, PID 260845 GPU1）
- 建议评估完成后先做一次 dry-run 验证（加 `--max_samples 16 --num_train_epochs 1 --gradient_accumulation_steps 1 --max_completion_length 256 --report_to none`）

---
