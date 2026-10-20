# ssh fix bs8 oom cuda2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_bs8_oom_cuda2_20260515T185123_result.json`
- **Structured JSON:** [`f4dddf1f5de4f4ab0e83.json`](../../sessions/f4/f4dddf1f5de4f4ab0e83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. bs8_nmin2_seed42_r2 状态
**出乎意料：进程仍然存活。** PID 238714 运行 ~8 分钟，已到 step 194/6103（3%），ETA ~3:54，速度 ~2.4s/step。**没有 OOM。**

GPU 2 显存占用：81705 MiB / 97887 MiB（83.5%），有 ~16GB 余量。运行在 RTX PRO 6000 Blackwell（97.9GB，不是预期的 96GB），可能正因为多出的 ~2GB 才避免了 OOM。

### 2. OOM 修复方案
**方案 A：gradient_checkpointing**，已添加到远程脚本：
- `pretrain_weighted.py` line 286: 新增 `--gradient_checkpointing` 参数
- `pretrain_weighted.py` line 349: `TrainingArguments` 中传入 `gradient_checkpointing=args.gradient_checkpointing`

### 3. dry-run 结果
在 GPU 3（已有 46.5GB 其他进程占用）上跑了 bs8+gradient_checkpointing：
- 成功执行 2/3 步，无 OOM（第 3 步被 SSH 30s 超时截断，不是 OOM）
- gradient_checkpointing 版本显存 < 51GB（与 46.5GB 共存于 97.9GB GPU）
- 代价：速度从 ~2.4s/step 降到 ~10s/step（约 4x 慢）

### 4. 建议
**当前 bs8_nmin2_seed42_r2 还在正常运行，不需要重新提交。** 它可能跑完全程不 OOM（GPU 实际有 97.9GB 而非 96GB）。

如果后续确实 OOM 了，准备好的新命令（加 `--gradient_checkpointing`）：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16 --gradient_checkpointing
```

注意事项：gradient_checkpointing 会使训练速度变慢约 4x（2.4s→10s/step），总训练时间从 ~4h 增加到 ~17h。

### 5. Registry
bs8_nmin2_seed42_r2 仍在运行，**不需要更新 registry 为 failed**。建议保持当前 PREPARING/RUNNING 状态，等它自然完成或 OOM 后再更新。

---
