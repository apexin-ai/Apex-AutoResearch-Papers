# submit crossover s025 s035 v4d

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_crossover-s025-s035-v4d_20260514T002131_result.json`
- **Structured JSON:** [`dc394a666463a5a17930.json`](../../sessions/dc/dc394a666463a5a17930.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 tmux sessions 全部存活。

---

## 报告

### 1. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell 96GB | 36.5 GB | 85% | **s025 实验运行中** |
| 1 | RTX PRO 6000 Blackwell 96GB | 30.6 GB | 92% | **s035 实验运行中** |
| 2 | RTX PRO 6000 Blackwell 96GB | 29.5 GB | 70% | **v4d 实验运行中** |
| 3 | RTX PRO 6000 Blackwell 96GB | 22.2 GB | 96% | **random_r2 运行中** |

### 2. random_r2 进度
- PID 32187 运行中，已运行 ~53 分钟
- 进度：**33/50 problems**（66%）
- 输出目录暂空（结果在全部完成后一次性写入）

### 3. 三个 importance masking 实验提交状态

| 实验 | GPU | Sparsity | tmux session | 状态 |
|------|-----|----------|-------------|------|
| mvp_v4_legacy_s025 | cuda:0 | 0.25 | `mvp_v4_legacy_s025` | **已启动，processing 1/50** |
| mvp_v4_legacy_s035 | cuda:1 | 0.35 | `mvp_v4_legacy_s035` | **已启动，processing 1/50** |
| mvp_ii_profiling_v4d | cuda:2 | 0.4 | `mvp_ii_profiling_v4d` | **已启动，processing 1/50** |

**关键决策**：直接使用 `--masking_method importance`（默认值），走 `compute_dense_forward_with_importance()` + `output_attentions=True` 路径。96GB Blackwell GPU 有充足显存（当前峰值 36GB），不会复现之前在小 GPU 上的 OOM 问题。

**实验命令**（三个相同模板，仅 GPU/sparsity/output_dir 不同）：
```bash
CUDA_VISIBLE_DEVICES={0,1,2} python -m pacs.profiling.run_profiling \
  --model_path .../DeepSeek-R1-Distill-Qwen-7B \
  --data_path .../math500.json \
  --output_dir {对应目录} \
  --max_new_tokens 2048 --min_phase_length 10 \
  --sparsity_levels {0.25,0.35,0.4} \
  --masking_method importance
```

**日志路径**：`/tmp/mvp_v4_legacy_s025.log`、`/tmp/mvp_v4_legacy_s035.log`、`/tmp/mvp_ii_profiling_v4d.log`

---
