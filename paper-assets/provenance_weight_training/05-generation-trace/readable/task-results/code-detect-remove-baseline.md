# code detect remove baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_detect_remove_baseline_20260516T002730_result.json`
- **Structured JSON:** [`8548adeaed3e18e7afd2.json`](../../sessions/85/8548adeaed3e18e7afd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 过滤统计

| 指标 | 值 |
|------|----|
| Threshold | 0.5 |
| Kept | 153,725 |
| Removed | 217,774 |
| Total | 371,499 |
| Removal rate | 58.6% |

## 过滤后文件

- 路径: `/root/provenance_weight_training/data/scored_data_filtered_q05.jsonl`
- 大小: 477MB（原始 930MB）
- 行数: 153,725

## 训练命令（可直接提交）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && \
python training/pretrain_weighted.py \
    --data_path data/scored_data_filtered_q05.jsonl \
    --output_dir output/models/detect_remove_baseline_seed42 \
    --weighting_method uniform \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --eval_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4
```

所有参数已通过 `--help` 验证，均可被 `pretrain_weighted.py` 正确解析。

## 训练时长预估

- 过滤后数据约 477MB / 930MB × 原始 token 总量，估算 ~90-100M tokens
- 目标 200M tokens → 需遍历数据约 2 轮
- 4× RTX PRO 6000 Blackwell (96GB)，Qwen3-0.6B 是小模型，batch_size=4 × grad_accum=4 = effective batch 64
- 预估 **1.5-3 小时**（取决于单卡吞吐，Blackwell 架构处理 0.6B 模型非常快）

---
