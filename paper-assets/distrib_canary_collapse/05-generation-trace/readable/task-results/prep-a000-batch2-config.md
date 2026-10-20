# prep a000 batch2 config

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_a000_batch2_config_20260516T112622_result.json`
- **Structured JSON:** [`d6155f794adfe74f9ae9.json`](../../sessions/d6/d6155f794adfe74f9ae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕，汇总报告：

---

## α=0.0 Batch 2 预备验证

### 1. synthetic_ratio=0.0 安全性

**安全。** `iterative_train.py:112` 有显式处理：

```python
if synthetic_ratio <= 0.0:
    return real_dataset  # 返回纯真实数据，不混合
```

历史验证：a000_s42 已成功完成（`all_metrics.json` 存在，11 个 gen 目录齐全）。

### 2. 磁盘占用

| 实验 | 总大小 |
|------|--------|
| a000_s42 (α=0.0) | 1.6 GB |
| a075_s42 (α=0.75) | 1.6 GB |

α=0.0 和 α=0.75 占用相同——因为 synthetic_data 仍然会生成（用于计算 metrics），只是不参与训练混合。gen_0~9 各 ~6-7MB（synthetic_data + metrics），gen_10 ~1.6GB（含 checkpoint）。

### 3. 磁盘余量

```
/dev/md0  250G  37G used  214G available  15%
```

两个实验需要 ~3.2GB，**214GB 余量完全充足**。

### 4. 完整启动命令

基于 a000_s42 和 a075_s43 的 config.json 参数：

**a000_s43 (cuda:0):**
```python
mcp__agent-ml-research__ssh_execute(
    server="westd-19828",
    account="root",
    command="cd /root/autodl-tmp/distrib_canary_collapse && CUDA_VISIBLE_DEVICES=0 nohup python iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --dataset wikitext-103-v1 --synthetic_ratio 0.0 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a000_s43 --seed 43 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 > results/alpha_sweep/a000_s43/train.log 2>&1 &"
)
```

**a000_s44 (cuda:1):**
```python
mcp__agent-ml-research__ssh_execute(
    server="westd-19828",
    account="root",
    command="cd /root/autodl-tmp/distrib_canary_collapse && CUDA_VISIBLE_DEVICES=1 nohup python iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --dataset wikitext-103-v1 --synthetic_ratio 0.0 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a000_s44 --seed 44 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 > results/alpha_sweep/a000_s44/train.log 2>&1 &"
)
```

注意：启动前需先 `mkdir -p results/alpha_sweep/a000_s43 results/alpha_sweep/a000_s44`（否则 nohup 的 log 重定向会失败）。且须确认 a075_s43/s44 已完成（检查 EXIT_CODE 文件），再释放 GPU。

---
