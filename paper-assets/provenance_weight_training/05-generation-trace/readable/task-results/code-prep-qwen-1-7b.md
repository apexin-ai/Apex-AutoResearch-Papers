# code prep qwen 1 7b

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_qwen_1_7b_20260518T130517_result.json`
- **Structured JSON:** [`9baaad675957b7453e93.json`](../../sessions/9b/9baaad675957b7453e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Qwen3-1.7B 验证实验准备报告

### 1. 模型位置
- `/root/autodl-tmp/provenance_weight_training/models/Qwen/Qwen3-1.7B/` (完整，2 shard)
- 已创建符号链接 → `/root/provenance_weight_training/models/Qwen/Qwen3-1.7B`

### 2. 训练脚本兼容性
- 脚本路径：`/root/provenance_weight_training/training/pretrain_weighted.py`
- `--model_name models/Qwen/Qwen3-1.7B` 即可切换，无需改代码

### 3. 数据
- 训练集：`data/scored_data.jsonl` ✓ (371,499 examples, ρ=0.4)
- 评估集：`data/human/eval_holdout.jsonl` ✓

### 4. Dry-run 结果

| 模式 | 训练步骤 | Loss | 退出码 | 备注 |
|------|---------|------|--------|------|
| uniform | 2/2 ✅ | 8.742 | 0 | 正常完成 |
| adaptive | 2/2 ✅ | step1=10.6, step2=12.36 | 1 | 训练正常，checkpoint 保存报错 |

**GPU 显存**：
- 峰值 allocated: **43.67 GB**，reserved: **43.89 GB** (forward+backward, batch_size=4, seq_len=2048)
- 加 optimizer 估计 ~55 GB
- GPU: 4× RTX PRO 6000 Blackwell (98 GB each)，显存充裕
- **无 OOM 风险**，batch_size=4 安全

**Adaptive checkpoint 保存错误修复**：已有 0.6B 脚本都带 `--save_only_model`，1.7B 脚本也必须加。

### 5. 推荐训练参数

```bash
python training/pretrain_weighted.py \
    --model_name models/Qwen/Qwen3-1.7B \
    --data_path data/scored_data.jsonl \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --max_steps 6103 \
    --bf16 \
    --save_only_model \
    --save_total_limit 3
```

与 0.6B 参数一致，98 GB 显存下无需降 batch_size。

### 6. Binoculars scoring 进度
- **252,031 / 371,499 (67.8%)**，31.9 samples/s，ETA ~62 分钟

---
