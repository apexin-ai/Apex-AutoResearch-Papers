# d153 gpu3 deepseek cls s456 fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_d153-gpu3-deepseek-cls-s456-fix_20260519T120035_result.json`
- **Structured JSON:** [`e54dafd698afffa7845a.json`](../../sessions/e5/e54dafd698afffa7845a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

## 报告

### DeepSeek CLS s456 训练状态: **RUNNING**
- PID 828872 存活，子进程 PID 828877 在 GPU 3 运行
- GPU 3: 99% 利用率，17206MiB 显存占用
- 进度: **step 14/549 (3%)**，~8.7s/step
- 训练数据: 5829 samples (40 dropped for exceeding max_seq_length)
- ETA: 约 **1.3 小时**完成全部 549 steps (3 epochs)
- output_dir 暂无 checkpoint（刚启动 ~2 分钟）
- Registry 已从 PREPARING → QUEUED → RUNNING

### CLS Checkpoint Ablation 进度: **已完成**
Worker 1 的三个 ablation eval 目录均已存在：
- `cls8b_s42_ckpt2200_test` ✓
- `cls8b_s42_ckpt3600_test` ✓
- `cls8b_s42_ckpt6633_test` ✓

### GPU 全局状态
| GPU | 利用率 | 显存 | PID | 备注 |
|-----|--------|------|-----|------|
| 0 | 88% | 27714MiB/32607MiB | 778334 | 其他任务 |
| 1 | 73% | 17420MiB/32607MiB | 828376 | 其他任务 |
| 2 | 95% | 23780MiB/32607MiB | 825036 | 其他任务 |
| 3 | 99% | 17206MiB/32607MiB | 828877 | **deepseek-cls-repo-s456** |

---
