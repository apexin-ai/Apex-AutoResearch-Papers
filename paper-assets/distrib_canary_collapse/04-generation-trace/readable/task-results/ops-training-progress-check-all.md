# ops training progress check all

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training_progress_check_all_20260519T125120_result.json`
- **Structured JSON:** [`c1ab66661e0d6d675f41.json`](../../sessions/c1/c1ab66661e0d6d675f41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### westd-17855 (磁盘: 200G 剩余, 44%)

| GPU | 实验 | VRAM | GPU利用率 | 进度 | 当前状态 |
|-----|------|------|----------|------|---------|
| 0 | alpha_sweep_a060_s43_fp32 | 7.5/98G | 70% | gen 0/10 | 刚启动11min，gen_0 featurizing 22% |
| 1 | qwen35_08b_wiki_a100_s42_v2 | 34.8/98G | 69% | gen 10/10 | 最后一代训练中，step 2088/5000 (42%) |
| 2 | padding_robustness_a100_s42_fp32 | 14.5/98G | 67% | gen 7/10 | 训练中 step 2041/5000 (40%) |
| 3 | alpha_sweep_a025_s43_fp32 | 14.5/98G | 60% | gen 7→8/10 | gen 7 生成合成数据中 |
| 4 | alpha_sweep_a025_s44_fp32 | 14.5/98G | 73% | gen 7→8/10 | gen 7 生成合成数据中 |
| 5 | alpha_sweep_a075_s42_fp32 | 14.5/98G | 73% | gen 7/10 | 训练刚开始 step 106/5000 (2%) |

### westd-19828 (磁盘: 27G 剩余, 90%) ⚠️

| GPU | 实验 | VRAM | GPU利用率 | 进度 | 当前状态 |
|-----|------|------|----------|------|---------|
| 0 | gen_gpt2m_a100_s43_fp32 | 62.7/98G | 100% | gen 9/10 | 训练中 step 3022/5000 (60%) |
| 1 | smollm3_3b_wiki_a100_s42_v3 | 64.4/98G | 100% | gen 7/10 | 训练中 step 2088/5000 (42%) |

### 状态总结

- **全部 8 个实验正常运行**，无 crash/hang/OOM
- **qwen35** 接近完成（最后一代 42%），预计 ~1h 内跑完
- **gen_gpt2m** 也接近尾声（gen 9/10, 60%），预计 ~2-3h
- **a025_s43/s44** 进度同步，均在 gen 7 数据生成阶段
- **a060_s43** 刚启动，还在 gen 0
- ⚠️ **westd-19828 磁盘 90%（仅剩 27G）**，需关注，gen_gpt2m 和 smollm3 完成后输出可能继续增长

---
