# Experiment Progress Check — 2026-05-16 08:25 UTC

## Running Experiments

### 1. acc_ds_s015_8k_v2 (PID 287691, CUDA:0)
- **Status**: Running, near completion
- **Progress**: 47/50 (正在生成第47题)
- **Running accuracy**: 20/46 = **43.5%**
- **Started**: 07:19 UTC (~66 min ago)
- **Estimated remaining**: ~5-15 min (3 problems left)
- **Notes**: 大部分问题正常完成（6-27s），偶尔超时（175s，pred=None）

### 2. acc_ds_s030_8k_v2 (PID 288901, CUDA:2)
- **Status**: Running, progress slow
- **Progress**: 25/50 (正在生成第25题)
- **Running accuracy**: 2/24 = **8.3%**
- **Started**: 07:30 UTC (~55 min ago)
- **Estimated remaining**: ~50-70 min (25 problems left, 大量超时)
- **Notes**: Problem 18-24 连续7题 pred=None（全部 ~177s 超时）。s030 剪枝率过高（224 heads pruned），模型推理能力严重退化，几乎无法输出有效答案。

## Completed Experiment

### acc_qw_dense_n100 (tmux session, started 05:35)
- **Status**: ✅ Completed (EXIT_CODE=0)
- **Final accuracy**: 48.0% (24/50)
- **Total time**: 1004s (~17 min)
- **Output**: `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_dense_n51_100.json`

## GPU Utilization

| GPU | Utilization | Memory Used | Memory Total | Process |
|-----|------------|-------------|--------------|---------|
| cuda:0 | 72% | 15,659 MiB | 97,887 MiB | acc_ds_s015_8k_v2 |
| cuda:1 | **0%** | **0 MiB** | 97,887 MiB | **空闲** |
| cuda:2 | 70% | 15,603 MiB | 97,887 MiB | acc_ds_s030_8k_v2 |
| cuda:3 | **0%** | **0 MiB** | 97,887 MiB | **空闲** |

## Anomalies

1. **s030 accuracy 极低 (8.3%)**: 相比 s015 的 43.5%，s030 剪枝率翻倍后准确率断崖式下降。大量问题输出 pred=None（token 耗尽未得出答案），说明 30% 稀疏度下 DeepSeek-R1 的推理链被严重破坏。
2. **cuda:1 和 cuda:3 完全空闲**: 无任何 Python 进程占用，可立即调度新实验。
3. **acc_qw_dense_n100 已静默完成**: tmux session 仍存在但进程已退出。
