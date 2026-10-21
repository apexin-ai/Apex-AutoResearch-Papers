# GPU 状态排查报告

**时间**: 2026-05-15 00:46 UTC+8
**服务器**: cqa1-21977 (6× RTX 4090D, 24GB each)

## GPU 状态总表

| GPU | 显存使用 | GPU-Util | PID | 进程 | 状态 |
|-----|---------|----------|-----|------|------|
| cuda:0 | 14367/24564 MiB | 34% | 385407 | `train_sft.py` Qwen2.5-1.5B_d025_s42 | **占用** (训练中, 2.5h) |
| cuda:1 | 5857/24564 MiB | 53% | 398887 | `evaluate.py` Qwen2.5-1.5B_d100_s42_aligned | **占用** (评估中, 1h) |
| cuda:2 | 3695/24564 MiB | 36% | 396024 | `evaluate.py` Qwen2.5-0.5B_d100_s42_aligned | **占用** (评估中, 1.3h) |
| cuda:3 | 0/24564 MiB | 0% | — | — | **空闲** |
| cuda:4 | 0/24564 MiB | 0% | — | — | **空闲** |
| cuda:5 | 22382/24564 MiB | 32% | 405520, 406027 | `train_sft.py` 3B_d000_v2 + `evaluate.py` 0.5B_d025_para_aligned | **占用** (两进程) |

## 僵尸进程处理

- **PID 398501** (GPU 3): `evaluate.py` Qwen2.5-0.5B_d025_s42_aligned (已标 failed 的 exp_001_eval_05B_d025_aligned)
  - 进程状态 Rl，占 3686MiB，但输出目录 1 小时无新写入，疑似卡死
  - 输出目录已有: correctness_matrix.json, eval_results.json, item_responses.json (数据可能不完整)
  - **已 kill -9**，GPU 3 显存释放至 0MiB

## 与预期不符

- **cuda:0**: 预期空闲，实际有 PID 385407 训练 Qwen2.5-1.5B_d025_s42 (运行 2.5h, 14.3GB)
- **cuda:1**: 预期 PID 336750 (eval_15B_aligned_batch)，实际是 PID 398887 (eval_1.5B_d100_aligned)

## 可用 GPU

- **cuda:3** — 空闲，24GB 可用
- **cuda:4** — 空闲，24GB 可用
