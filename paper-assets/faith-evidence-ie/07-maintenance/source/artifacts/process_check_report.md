# 进程状态报告 — 2026-05-16T08:26Z

## 进程总览

| 进程 | PID | GPU | 状态 | 进度 |
|------|-----|-----|------|------|
| rsft_ced_s43_train_r3 | 277310 | cuda:1 | RUNNING | 48/510 steps (9.4%), ~5.8s/step |
| rsft_ced_s45_train_r3 | 277407 | cuda:2 | FAILED (OOM) | 模型加载阶段即崩溃 |
| eval_flat_nli_s44 | 270462 | cuda:0 | RUNNING | 80/247 batches (32.4%) |
| eval_flat_nli_seed45 | 272164 | cuda:3 | RUNNING | 55/247 batches (22.3%) |

## 详细状态

### 1. rsft_ced_s43_train_r3 — RUNNING

- **PID**: 277310 (python PID 277315)
- **GPU**: cuda:1, 28332 MiB used, 99% util
- **进度**: step 48/510 (~9.4%), ~5.8s/step
- **预计剩余**: ~45 min
- **Checkpoint**: `rsft_output_ced_s43/checkpoint-50` 已产生，checkpoint-507 尚未生成

### 2. rsft_ced_s45_train_r3 — FAILED (CUDA OOM)

- **PID**: 277407 — 已退出, exit code 1
- **退出时间**: 2026-05-16T00:21:27Z（启动后 ~15s 即崩溃）
- **tmux session**: 已不存在
- **失败原因**: `torch.AcceleratorError: CUDA error: out of memory` — 在 `AutoModelForCausalLM.from_pretrained()` 阶段
- **根因**: GPU 2 被残留进程 PID 276148 占满（31630 MiB）。该进程是之前的 `rsft-ced-s45-r2` 训练运行（wandb_run_name: `rsft-ced-s45-r2`），仍在活跃占用 GPU 2
- **修复**: 需先 kill PID 276148 释放 GPU 2，然后重新提交 rsft_ced_s45_train_r3

### 3. eval_flat_nli_s44 — RUNNING

- **PID**: 270462 (python PID 270467)
- **GPU**: cuda:0, 10846 MiB used, 53% util
- **进度**: 80/247 batches (32.4%), elapsed ~58 min
- **平均速度**: ~43s/batch
- **预计剩余**: ~2h
- **输出目录**: `eval_results/rsft_flat_nli_s44/`
- **metrics_v2.json**: 尚未生成（推理未完成）

### 4. eval_flat_nli_seed45 — RUNNING

- **PID**: 272164 (python PID 272169)
- **GPU**: cuda:3, 10850 MiB used, 50% util
- **进度**: 55/247 batches (22.3%), elapsed ~41 min
- **平均速度**: ~45s/batch
- **预计剩余**: ~2.4h
- **输出目录**: `eval_results/rsft_flat_nli_s45/`
- **metrics_v2.json**: 尚未生成（推理未完成）

## GPU 占用状态

| GPU | 显存占用 | 利用率 | 占用进程 |
|-----|---------|--------|---------|
| 0 | 10855 MiB | 53% | eval_flat_nli_s44 (PID 270467) |
| 1 | 28341 MiB | 99% | rsft_ced_s43_train_r3 (PID 277315) |
| 2 | 31639 MiB | 99% | **残留进程** rsft-ced-s45-r2 (PID 276148) |
| 3 | 10859 MiB | 50% | eval_flat_nli_seed45 (PID 272169) |

## 活跃 Tmux Sessions

- `eval_flat_nli_s44` — created 2026-05-16 07:27:39
- `eval_flat_nli_seed45` — created 2026-05-16 07:44:53
- `rsft_ced_s43_train_r3` — created 2026-05-16 08:21:12

（`rsft_ced_s45_train_r3` session 已不存在）

## 需要行动

1. **Kill 残留进程 PID 276148**（rsft-ced-s45-r2）释放 GPU 2
2. **重新提交 rsft_ced_s45_train_r3** 到 GPU 2
3. 两个 eval 预计 ~2h 后完成，届时提取 metrics_v2.json
