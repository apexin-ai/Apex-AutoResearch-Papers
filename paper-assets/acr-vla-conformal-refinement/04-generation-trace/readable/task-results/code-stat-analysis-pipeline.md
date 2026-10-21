# code stat analysis pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stat-analysis-pipeline_20260515T164814_result.json`
- **Structured JSON:** [`d8697f4e6329874ab986.json`](../../sessions/d8/d8697f4e6329874ab986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个脚本已部署到 `/root/acr-vla-conformal-refinement/analysis/` 并通过 seed=42 数据试运行验证。

### 产出文件

**脚本:**
- `analysis/stat_analysis.py` — 六方对比表 + Fisher exact test + bootstrap CI + per-task breakdown
- `analysis/norm_sensitivity.py` — norm sensitivity curve 数据
- `analysis/visualize.py` — 论文级 bar chart + sensitivity curve (PDF+PNG)

**试运行输出:**
- `analysis/results/comparison.json` — 结构化统计结果
- `analysis/results/norm_sensitivity.json` — norm 曲线数据
- `analysis/figures/object_comparison.{pdf,png}` — 六方对比图
- `analysis/figures/norm_sensitivity.{pdf,png}` — norm sensitivity 图

### 当前状态
- seed=42 数据：obs_only(19%), perdof(11%), vla_only(12%), reconvla(12%), vla_mean(12.2%, 9/10 tasks) 都已入表
- argmin 和 scalar 没有找到对应的 log/JSON 文件，Fisher test 自动跳过
- obs_only_norm02 seed43 刚启动（0 tasks），脚本正确处理了空数据

### seed=43 完成后的使用方式

```bash
# 重新运行 stat_analysis（会自动发现新的 seed43 文件）
python analysis/stat_analysis.py --log-dir logs/ --output analysis/results/comparison.json

# 或手动指定 Fisher test 的两个方法文件
python analysis/stat_analysis.py --methods \
  obs_only:logs/eval_object_obs_only.json \
  obs_only:logs/eval_object_obs_only_seed43.json \
  argmin:logs/eval_object_argmin.json \
  argmin:logs/eval_object_argmin_seed43.json \
  --test-pair obs_only argmin

# 重新生成图表
python analysis/visualize.py --comparison analysis/results/comparison.json
```

---
