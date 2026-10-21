# ops disk cleanup and prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_and_prep_20260517T192312_result.json`
- **Structured JSON:** [`9aca8a2674f7219e5deb.json`](../../sessions/9a/9aca8a2674f7219e5deb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。最终报告：

---

## 磁盘清理报告

### 1. 清理前后对比

| | Size | Used | Avail | Use% |
|---|---|---|---|---|
| **清理前** | 250G | 250G | 484K | 100% |
| **清理后** | 250G | 59G | 192G | 24% |

**总释放：~191GB**

### 2. 清理明细
- generalize/ 3个 DONE 实验 gen_1~gen_9 的 checkpoint/synthetic_data/trainer/（~90GB）
- alpha_sweep/ 11个 DONE 实验 gen_1~gen_9 同上（~80GB）
- pythia14b gen_1~gen_5 大文件 + 不完整 gen_7（~27GB）
- HF cache 中未使用的 gpt2-large + gpt2-medium（~4.6GB）
- 所有 metrics.json、gen_0、gen_10 均保留

### 3. Pythia-1.4B gen_6 checkpoint 状态
**完整**。包含 `model-00001-of-00002.safetensors`、`model-00002-of-00002.safetensors`、config.json、tokenizer 文件。metrics.json 记录了 gen_6 指标（ppl=406.49, mauve=0.029, eff_rank=104.4）。

EXIT_CODE 确认崩溃原因：`Error while serializing: I/O error: No space left on device (os error 28)`（gen_7 保存 checkpoint 时磁盘满）。

### 4. iterative_train.py resume 支持
**不支持自动 resume**。脚本从 gen_0 开始，无 `--start_gen` 参数。恢复需要修改脚本添加 resume 逻辑（检测已有 gen 并从 gen_6/checkpoint 加载模型继续 gen_7~10）。

### 5. C4 数据目录
`/root/autodl-tmp/distrib_canary_collapse/data/c4_5k/`（含 train/, eval/, prompts/）

### 6. 模型本地路径
- Pythia-1.4B: `/root/autodl-tmp/.hf_cache/pythia-1.4b-local/`（5.5GB）
- Pythia-1B: `/root/autodl-tmp/.hf_cache/pythia-1b-local/`（2.0GB）

### 7. 推荐启动命令

**Pythia-1.4B 恢复**（需先给 iterative_train.py 添加 `--start_gen` 支持）：
```bash
cd /root/autodl-tmp/distrib_canary_collapse
python iterative_train.py \
  --model_name results/generalize/pythia14b_wiki_a100_s42/gen_6/checkpoint \
  --data_dir data/wikitext103_5k \
  --output_dir results/generalize/pythia14b_wiki_a100_s42 \
  --num_generations 10 --steps_per_gen 5000 \
  --synthetic_ratio 1.0 --seed 42 --batch_size 4 \
  --start_gen 7
```

**C4 seed-43 新实验**：
```bash
cd /root/autodl-tmp/distrib_canary_collapse
python iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/pythia-1b-local \
  --data_dir data/c4_5k \
  --output_dir results/generalize/pythia1b_c4_a100_s43 \
  --num_generations 10 --steps_per_gen 5000 \
  --synthetic_ratio 1.0 --seed 43 --batch_size 4
```

> **注意**: Pythia-1.4B 恢复需要先修改 `iterative_train.py` 添加 `--start_gen` 参数，使其跳过已完成的 gen 并从指定 checkpoint 加载模型。当前脚本不支持此功能。

---
