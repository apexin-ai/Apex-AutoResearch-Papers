# monitor gpu experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu-experiments_20260515T144846_result.json`
- **Structured JSON:** [`006afc692d7cd77e7ef4.json`](../../sessions/00/006afc692d7cd77e7ef4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## 状态报告 (2026-05-15 14:51 UTC)

### 实验进度

| 实验 | GPU | 进程 | 完成代数 | 当前状态 | 速度 | ETA (UTC) |
|------|-----|------|---------|---------|------|-----------|
| **gen_wiki_gpt2m_a100_s42_v3** | cuda:0 (100%, 55.5/98GB) | 117632 ALIVE | 3/10 | gen_3 训练中 step 1425/5000 (28.5%) | 2.05 it/s | **~22:20** |
| **alpha_sweep_a025_s43** | cuda:1 (44%, 14.4/98GB) | 121635 ALIVE | 3/10 done, gen_4 starting | gen_3 刚完成 (loss=2.51), gen_4 进入 synthetic gen 阶段 | 15.87 it/s | **~17:30** |

### 时间分析

- **GPT-2m (cuda:0)**: 每代约 55-60 min (含 synthetic gen ~17min + training ~41min)，剩余 ~7.5h。**原 ETA 17:00 UTC 严重低估**，实际要到 ~22:20 UTC。
- **alpha_sweep (cuda:1)**: 每代约 22-25 min (Pythia-410m 小得多)，剩余 ~2.8h。

### 接力计划

cuda:1 将先空出 (~17:30 UTC)，cuda:0 要到 ~22:20 UTC 才释放。

**gen_wiki_gpt2m_a025_s42** 接力命令已确认可行：
```bash
python -u iterative_train.py \
  --model_name gpt2-medium \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.25 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 32 \
  --seed 42 \
  --output_dir results/gen_wiki_gpt2m_a025_s42
```
- 脚本支持 `--model_name gpt2-medium` + `--synthetic_ratio 0.25`
- 数据目录 `data/wikitext103_5k/` 就绪 (含 train/eval/prompts)
- 如果想提前利用 cuda:1，alpha_sweep 完成后可以在 cuda:1 上启动此实验（不必等 cuda:0）

### 异常

- **无异常**。两个进程健康运行，GPU 利用率正常（cuda:0 满载符合 GPT-2m 模型大小，cuda:1 44% 符合 Pythia-410m 较小模型特征）。
- padding_side 警告为正常现象（decoder-only 模型 generate 时的标准 warning），不影响结果。

---
