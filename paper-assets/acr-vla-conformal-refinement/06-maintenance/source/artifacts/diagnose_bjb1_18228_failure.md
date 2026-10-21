# bjb1-18228 批量实验诊断报告

**日期**: 2026-05-21 09:21 UTC

## 结论：非进程异常退出，是监控层面的误报

三个被标记为"失败"的实验全部正常完成。`evaluate.py` 不包含 W&B logging 或 sentinel 文件写入逻辑，因此监控系统检测不到完成信号。

## 各实验日志摘要

| 实验 | 日志行数 | 最终状态 | Overall Success Rate | JSON 输出 |
|------|---------|---------|---------------------|-----------|
| norm005-seed58 | 52 | 正常完成 | 16.0% (16/100) | eval_obs_only_object_norm005_seed58.json ✓ |
| norm01-seed57 | 52 | 正常完成 | 19.0% (19/100) | eval_obs_only_object_norm01_seed57.json ✓ |
| norm003-seed59 | 52 | 正常完成 | 13.0% (13/100) | eval_obs_only_object_norm003_seed59.json ✓ |

每个日志末尾都有完整的 per-task success rate 汇总和 `[eval] Results saved to logs/...json` 确认行。无 Traceback、OOM、CUDA error、SIGHUP 或任何异常信号。

## 进程状态

| PID | 实验 | 状态 |
|-----|------|------|
| 599925 (seed59) | norm003-seed59 | 已退出（正常完成） |
| 622479 (seed65) | norm005-seed65 | 运行中，已 46 分钟，当前在 task 4/10 (bbq_sauce)，28 行日志 |

## 系统健康

- **GPU**: 4x RTX 4090，全部正常。GPU 1 被 seed65 实验使用（3851MiB / 24564MiB, 25% util），其余 3 块空闲
- **Driver**: 580.105.08, CUDA 13.0
- **无 ECC 错误**

## 失败根因

**不是运行时失败。** 实验完成了评估并输出了 JSON 结果，但 `evaluate.py` 中没有：
1. `wandb.log()` 调用 → 无 W&B metrics
2. sentinel 文件写入 → 监控系统无法检测完成

这与 bjb2-28827 的 SIGHUP 问题不同。

## 建议

- **不需要重跑** — 三个实验都有完整的 JSON 结果
- 直接从 JSON 文件提取结果即可：`/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_*.json`
- seed65 正在正常运行中，预计还需 ~40 分钟完成
