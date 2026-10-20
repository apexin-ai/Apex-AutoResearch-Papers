# GPU 诊断报告 — 2026-05-19 09:03 UTC

## Part 1: GPU 状态总览

| GPU | 利用率 | 显存占用 | PID | 实验 | 状态 |
|-----|--------|----------|-----|------|------|
| cuda:0 | 0% | 0MiB / 24564MiB | — | retrain-depth-ext | **COMPLETED** (08:53 完成) |
| cuda:1 | 0% | 0MiB / 24564MiB | — | exp_code_qwen7b (PID 110240) | **CRASHED** (EXIT_CODE=1 @ 00:32Z) |
| cuda:2 | 97% | 15927MiB / 24564MiB | 96340 | exp_code_llama8b | **RUNNING** — depth 2 生成中, 97% (1366/1375) |
| cuda:3 | 97% | 14571MiB / 24564MiB | 107037 | exp_code_mistral7b | **RUNNING** — depth 1 生成中, 57% (786/1375) |

### 逐卡详情

**cuda:0 — IDLE**
- retrain-depth-ext 已于 08:53 完成，无残留进程
- 仅有 `tail -f` 监听进程 (PID 111051)

**cuda:1 — IDLE (exp_code_qwen7b CRASHED)**
- PID 110240 不存在，进程已退出
- 退出码: 1，时间: 2026-05-19T00:32:30Z
- 崩溃原因: `RuntimeError: Cannot send a request, as the client has been closed.` (huggingface_hub httpx 客户端关闭)
- 另有 tmux session `exp_code_pythia1b4` 存在但无 GPU 进程活跃

**cuda:2 — exp_code_llama8b (RUNNING)**
- 父进程 PID 96335 (bash wrapper)，实际 python PID 96340
- 启动时间: 04:43，已运行 ~4.3h
- 当前进度: depth 2 生成，1366/1375 batches (97%)，即将完成 depth 2
- 参数: Llama-3.1-8B, 5000 samples, max_depth=5, batch_size=4, continuation mode

**cuda:3 — exp_code_mistral7b (RUNNING)**
- PID 107037 活跃
- 启动时间: 07:50，已运行 ~1.2h
- 当前进度: depth 1 生成，786/1375 batches (57%)
- 参数: Mistral-7B-v0.3, 5000 samples, max_depth=5, batch_size=4, continuation mode

---

## Part 2: retrain-depth-ext 结果

实验已成功完成。从 depth 0-4 扩展到 depth 5-7，K*=7（所有 pair AUC > 0.6 阈值）。

### Pairwise AUC（5-fold GroupKFold CV）

| Pair | Mean AUC | Std | 95% CI | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 |
|------|----------|-----|--------|--------|--------|--------|--------|--------|
| 0v1 | **0.9837** | 0.0019 | [0.9821, 0.9854] | 0.9832 | 0.9821 | 0.9837 | 0.9823 | 0.9873 |
| 1v2 | **0.8971** | 0.0025 | [0.8949, 0.8993] | 0.8923 | 0.8988 | 0.8986 | 0.8991 | 0.8967 |
| 2v3 | **0.8098** | 0.0052 | [0.8052, 0.8144] | 0.8086 | 0.8074 | 0.8180 | 0.8024 | 0.8128 |
| 3v4 | **0.7600** | 0.0082 | [0.7528, 0.7672] | 0.7534 | 0.7617 | 0.7753 | 0.7566 | 0.7531 |
| 4v5 | **0.7459** | 0.0091 | [0.7379, 0.7538] | 0.7429 | 0.7562 | 0.7521 | 0.7300 | 0.7482 |
| 5v6 | **0.7017** | 0.0068 | [0.6958, 0.7076] | 0.7006 | 0.7077 | 0.7104 | 0.6915 | 0.6984 |
| 6v7 | **0.6410** | 0.0039 | [0.6376, 0.6445] | 0.6419 | 0.6349 | 0.6464 | 0.6390 | 0.6430 |

### Pairwise JSD

| Pair | JSD |
|------|-----|
| 0v1 | 0.230050 |
| 1v2 | 0.103924 |
| 2v3 | 0.075049 |
| 3v4 | 0.065398 |
| 4v5 | 0.060509 |
| 5v6 | 0.034998 |
| 6v7 | 0.017652 |

### 趋势分析
- AUC 单调递减: 0.984 → 0.897 → 0.810 → 0.760 → 0.746 → 0.702 → 0.641
- JSD 单调递减: 0.230 → 0.104 → 0.075 → 0.065 → 0.061 → 0.035 → 0.018
- depth 4→5 过渡 (AUC 0.746) 与 depth 3→4 (AUC 0.760) 差异较小，退化趋于平缓
- depth 6→7 (AUC 0.641) 仍高于阈值 0.6，JSD 仅 0.018，接近收敛

### 结果文件位置
- 数据: `/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/depth_{0-7}.jsonl`
- 特征: `/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv`
- 结果: `/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/`
  - `pairwise_auc.json`, `jsd.json`, `summary.json`

---

## Part 3: 日志摘要

| 实验 | 日志路径 | 状态 |
|------|----------|------|
| exp_code_llama8b | `~/runs/gen-depth-contamination/exp_code_llama8b.log` | depth 2 生成 97%，正常运行 |
| exp_code_mistral7b | `results/exp_code_mistral7b.log` (tee 输出) | depth 1 生成 57%，正常运行。注: `~/runs/` 下无此日志 |
| exp_code_qwen7b | `~/runs/gen-depth-contamination/exp_code_qwen7b.log` | **CRASHED** — httpx client closed error, EXIT_CODE=1 |

---

## 待处理事项

1. **exp_code_qwen7b 需要重启** — cuda:1 空闲，崩溃原因为 HuggingFace Hub httpx 客户端意外关闭（可能网络瞬断）
2. **cuda:0 空闲可用** — retrain-depth-ext 已完成，可安排新任务
