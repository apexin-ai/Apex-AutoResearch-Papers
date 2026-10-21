# run exp015 d100 qc only

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp015_d100_qc_only_20260516T000013_result.json`
- **Structured JSON:** [`67f8a9868020b64255b7.json`](../../sessions/67/67f8a9868020b64255b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据验证通过：57,547 行 (50,000 base + 7,547 QC-pass contam)，格式正确。

**GPU 4 当前被 compute_signals (PID 659065, d025_s123) 占用，已运行 ~17h。** 根据 C001/C002/C005 约束，必须等它结束后才能提交 SFT 训练。

### 当前进度总结

| 步骤 | 状态 | 结果 |
|------|------|------|
| 数据准备 | 完成 | `/root/autodl-tmp/exp015/sft_data/sft_dosage_100_qc_only.jsonl` (57,547 条: 50k base + 7,547 QC-pass) |
| 训练脚本 | 确认 | `/root/contamcal-irt-calibration/exp001/train_sft.py`，默认 lora_alpha=32 |
| 0.5B 模型 | 确认 | `/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-0.5B/snapshots/060db6499f32faf8b98477b0a26969ef7d8b9987` |
| GPU 4 | **被占用** | PID 659065 `compute_signals` (d025_s123), 7064 MiB, 61% util, 已运行 17h |

### 阻塞项

GPU 4 上 `compute_signals` 仍在运行。待其完成后，提交命令为：

```bash
export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-0.5B/snapshots/060db6499f32faf8b98477b0a26969ef7d8b9987 \
  --data-path /root/autodl-tmp/exp015/sft_data/sft_dosage_100_qc_only.jsonl \
  --output-dir /root/autodl-tmp/exp015/checkpoints/Qwen2.5-0.5B_d100_qc_s1 \
  --gpu 0 --seed 1 --batch-size 1 --grad-accum 16 --max-seq-length 2048 \
  --lr 5e-5 --lora-alpha 32
```

需要你确认：是等 GPU 4 空闲后自动提交，还是先 kill 掉 compute_signals 进程？

---
