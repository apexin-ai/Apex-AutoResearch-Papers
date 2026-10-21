# westd-38929 巡检报告

**时间**: 2026-05-22 ~10:00 UTC

## GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 10614/97887 MiB | 13% | 运行中 |
| 1 | 1/97887 MiB | 0% | 空闲 |
| 2 | 1/97887 MiB | 0% | 空闲 |
| 3 | 1/97887 MiB | 0% | 空闲 |

## 实验进程状态

| GPU | PID | 实验 | 状态 | SR |
|-----|-----|------|------|-----|
| 0 | 227008 | eval_pi05_l2norm_k085_spatial_seed42 | **ALIVE** (Task 1/10, ~95%) | 进行中 |
| - | 48588 | eval_pi05_random_k085_spatial_seed42 | DEAD (正常完成) | **58.4%** |
| - | 68029 | eval_pi05_random_k0925_object_seed43 | DEAD (正常完成) | **30.0%** |
| - | 9126 | eval_pi05_random_k09_spatial_seed42 | DEAD (正常完成) | **54.6%** |
| - | 48423 | eval_pi05_l2norm_k09_spatial_seed42 | DEAD (正常完成) | **95.0%** |
| - | 999560 | eval_openvla_l2norm_k05_object_seed42_v4 | DEAD (**FAILED**) | N/A |

## 失败实验详情

**PID 999560** (eval_openvla_l2norm_k05_object_seed42_v4):
```
ImportError: huggingface-hub>=0.19.3,<1.0 is required for a normal functioning of this module, but found huggingface-hub==1.16.0.
```
原因：openvla 使用的 transformers 版本（`/root/autodl-tmp/openvla_deps/transformers`）与当前 huggingface-hub 1.16.0 不兼容。

## 已完成结果汇总（libero_spatial, pi05）

| 方法 | keep_ratio | SR |
|------|-----------|-----|
| l2norm | 0.90 | 95.0% |
| l2norm | 0.85 | 进行中 |
| random | 0.90 | 54.6% |
| random | 0.85 | 58.4% |

## 备注

- 无 tmux session
- 3 块 GPU 空闲可用
- 活跃实验预计还需约 80 分钟完成（已完成 2/10 tasks）
