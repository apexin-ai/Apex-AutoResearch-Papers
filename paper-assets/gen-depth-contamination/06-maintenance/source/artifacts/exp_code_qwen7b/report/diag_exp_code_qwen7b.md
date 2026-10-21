# 诊断报告：exp_code_qwen7b

## 结论：实验已成功完成，EXIT_CODE=1 为误报

日志末尾明确输出：
```
20:10:29 [INFO] Pipeline complete.
EXIT_CODE=0
```

Python 进程正常退出（return_code=0）。报告的 EXIT_CODE=1 可能来自 job runner/wrapper 层（如 nohup、screen 或任务调度器的退出码处理逻辑），而非实验代码本身。

## 无 Traceback / 无错误

日志中没有任何 Traceback、Error、Exception、CUDA OOM 或 killed 信号。唯一的 warning 是 sklearn 的 feature name 警告（不影响结果）和 transformers 的 `torch_dtype` deprecation warning。

## Pipeline 各阶段完成情况

| 阶段 | 状态 | 时间 |
|------|------|------|
| Step 1: 模型加载 (Qwen2.5-7B) | 完成 | 09:31:16 - 09:31:30 |
| Step 2: Seed Data (depth_0) | 跳过（已存在） | 09:31:30 |
| Step 3: Depth Chain (depth 1-5) | 完成 | 09:31:30 - 19:53:xx |
| Step 4: Feature Extraction | 完成 | ~19:53 - 20:09 |
| Step 5: Analysis (AUC/JSD/Ordinal) | 完成 | 20:09 - 20:10:29 |

## 产出文件

**数据目录** (`data/exp_code_qwen7b/`):
- `depth_0.jsonl` (4.1 MB, seed data)
- `depth_1.jsonl` (4.4 MB)
- `depth_2.jsonl` (5.8 MB)
- `depth_3.jsonl` (5.7 MB)
- `depth_4.jsonl` (5.6 MB)
- `depth_5.jsonl` (5.5 MB)
- `features.csv` (8.8 MB)

**结果目录** (`results/exp_code_qwen7b/`):
- `pairwise_auc.json`
- `jsd.json`
- `ordinal_results.json`
- `feature_importance.json`
- `summary.txt`

## 实验结果摘要

K* = 2（AUC > 0.60 的最大 depth）

| 对比 | AUC | JSD |
|------|-----|-----|
| depth 0 vs 1 | 0.9051 ± 0.0043 | 0.0613 |
| depth 1 vs 2 | 0.7276 ± 0.0055 | 0.0423 |
| depth 2 vs 3 | 0.5368 ± 0.0145 | 0.0041 |
| depth 3 vs 4 | 0.5090 ± 0.0055 | 0.0032 |
| depth 4 vs 5 | 0.5139 ± 0.0128 | 0.0034 |

Ordinal Classification: MAE=1.2651, Accuracy=0.3423

Top-3 features: freq_entropy, surp_d2_mean, surp_d1_mean

## 建议

无需修复或重跑。建议排查 job runner 的退出码传递逻辑，避免后续实验产生类似误报。
