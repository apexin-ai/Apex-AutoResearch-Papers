# 诊断报告: EXIT_CODE=127 失败 (2026-05-18)

## 结论

**EXIT_CODE=127 来自第一次启动时 `python: command not found`，三个实验已被重新启动且正在正常训练中。**

## 根因

agent-ml-research wrapper 使用以下模式启动训练:

```bash
bash -c 'bash -c "source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && python training/pretrain_weighted.py ..."'
```

`source /root/miniconda3/bin/activate` 在嵌套 `bash -c` 中未能正确激活 conda 环境，导致 `python` 不在 PATH 中。

**直接证据** (`detect_remove_q03_seed42.log` 和 `detect_remove_q07_seed42.log` 的完整内容):
```
bash: line 1: python: command not found
EXIT_CODE=127
```

三个实验的第一次运行都以相同方式失败。

## 时间线

| 事件 | 时间 (Beijing) |
|------|---------------|
| 第一次启动 (wrapper) | ~22:15 |
| epoch_matched_dr_seed123 失败 | 22:15:06 |
| epoch_matched_dr_seed456 失败 | 22:15:09 |
| detect_remove_q01_seed42 失败 | 22:27:26 |
| 第二次启动 (手动 tmux) | 22:48 |

## 第二次启动方式 (当前正在运行)

使用绝对路径 `/root/miniconda3/bin/python` 代替 `python`，绕过了 conda activate 问题:

```bash
cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=X WANDB_MODE=disabled \
  /root/miniconda3/bin/python training/pretrain_weighted.py ... \
  2>&1 | tee ~/runs/provenance_weight_training/<name>.log
```

## 当前训练状态

| 实验 | GPU | 当前步数 | 总步数 | 进度 | 预计剩余 |
|------|-----|---------|--------|------|---------|
| epoch_matched_dr_seed456 | cuda:1 | 293 | 2532 | 12% | ~1h18m |
| epoch_matched_dr_seed123 | cuda:0 | 293 | 2532 | 12% | ~1h18m |
| detect_remove_q01_seed42 | cuda:3 | 292 | 6103 | 5% | ~3h23m |

GPU 利用率: 4 块 GPU 均 97-99%，内存 ~42GB/98GB。

## Checkpoint 状态

三个实验的 output 目录中仅有 `config.json` 和 `step_metrics.jsonl`，**尚无模型 checkpoint** (训练未到达 save_steps)。

```
/root/autodl-tmp/output/models/epoch_matched_dr_seed456/  → config.json, step_metrics.jsonl (1070 lines, step 264)
/root/autodl-tmp/output/models/epoch_matched_dr_seed123/  → config.json, step_metrics.jsonl (1070 lines)
/root/autodl-tmp/output/models/detect_remove_q01_seed42/  → config.json, step_metrics.jsonl (1060 lines)
```

## Eval Metrics

尚无。训练仍在进行中，eval 在训练完成后执行。

## 修复建议

1. **当前无需操作** — 三个实验已在正常运行，等待完成即可
2. **清理 stale exit files** — `/tmp/agent-ml-exit/` 中的 `.exit` 文件包含旧的 127 退出码，会误导监控系统
3. **修复 wrapper 脚本** — 后续提交任务时应使用 `/root/miniconda3/bin/python` (绝对路径) 而非依赖 `source activate && python`
4. **注意**: 当前运行不带 wrapper trap，训练完成后不会写入 `.exit` 文件，监控系统可能无法自动检测完成状态

## 其他发现

- `detect_remove_q07_seed42_r2` 也在运行中 (cuda:2, tmux session 创建于 20:11)
- `eval_all` tmux session 存在 (在 cuda:0 上执行之前实验的 eval)
- 服务器所有 4 块 GPU 均被占满
