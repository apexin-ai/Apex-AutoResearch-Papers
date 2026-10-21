# D049 GPU Fill Deployment Report

**Time**: 2026-05-17 13:32-13:38 UTC

## Summary

| # | exp_id | 计划 GPU | 实际 GPU | 状态 | PID | 备注 |
|---|--------|----------|----------|------|-----|------|
| 1 | eval-random-selection-object-seed42 | bjb2-40593 cuda:0 | bjb2-40593 cuda:0 | **已在运行** | 395256 | 已运行 ~1.5h，无需重复部署 |
| 2 | eval-obs-only-object-norm02-k5-seed42 | bjb2-28827 cuda:1 | bjb1-18228 cuda:2 | **RUNNING** | 633662 | 原 GPU 被 perdof seed45 占用(29h)，另一 worker 已部署到 bjb1-18228 |
| 3 | eval-obs-only-object-norm02-k20-seed42 | bjb2-28827 cuda:2 | bjb1-18228 cuda:3 | **RUNNING** | 636638 | 原 GPU 被 perdof seed47 占用(~2h)。首次部署失败(EXIT_CODE=1)，已重新提交 |
| 4 | eval-obs-only-object-norm005-seed43 | bjb1-18228 cuda:0 | bjb1-18228 cuda:0 | **RUNNING** | 631667 | 按计划部署 |
| 5 | eval-perdof-object-norm02-seed45-r2 | bjb1-18228 cuda:1 | bjb1-18228 cuda:1 | **RUNNING** | 631687 | 按计划部署 |
| 6 | eval-obs-only-object-norm003-seed43 | bjb1-32546 cuda:0 | - | **已完成(DONE)** | - | Registry 显示已处于 DONE 状态，无需重新部署 |

## Random Selection Mode

bjb2-40593 上的 evaluate.py 已有完整 `random_selection` mode 实现（line 222: `select_action_random`）。从 K 个 candidate 中 `np.random.randint` 随机选一个，不使用 CRM score。其他服务器不需要此 mode。

## GPU 冲突详情

Director 指定的 GPU 中有 3 个被现有实验占用：

| 服务器 | GPU | 占用实验 | 运行时长 | 内存占用 |
|--------|-----|----------|----------|----------|
| bjb2-28827 | cuda:1 | eval-perdof-object-norm02-seed45 | 29h+ | 1923 MiB |
| bjb2-28827 | cuda:2 | eval-perdof-object-norm02-seed47 | ~2h | 5645 MiB |
| bjb1-32546 | cuda:0 | eval-obs-only-object-norm005-seed43-r2 | ~1.5h | 5182 MiB |

实验 2、3 改部署到 bjb1-18228 空闲 GPU。

## 注意事项

- bjb1-18228 现有 4 个 LIBERO 进程（达到上限），全部共享同一服务器
- bjb2-28827 cuda:1 上的 perdof seed45 已跑 29h（异常长），可能需要检查是否 stuck
- 已清理 bjb1-18228 上 2 个 stale tmux sessions（eval-perdof-object-norm02-seed45-deploy, eval-obs-only-object-norm005-seed43-r3）
