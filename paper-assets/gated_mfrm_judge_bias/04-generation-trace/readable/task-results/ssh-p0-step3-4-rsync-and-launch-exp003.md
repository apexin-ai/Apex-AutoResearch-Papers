# ssh p0 step3 4 rsync and launch exp003

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_step3_4_rsync_and_launch_exp003_20260522T135505_result.json`
- **Structured JSON:** [`ebd2b4d77400d34099db.json`](../../sessions/eb/ebd2b4d77400d34099db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 3+4 执行完成。汇总：**

### Step 3: rsync 结果
| 数据 | 大小 | 状态 |
|------|------|------|
| exp003/ 代码 (4 .py) | 522KB | 同步成功 |
| exp002/results/ (exposure_scores.csv 等) | 252KB | 同步成功 |
| exp001/results/ (9 judge × judgments) | 25.6MB | 同步成功 |

注：judgment 数据实际路径是 `exp001/results/`（非 `outputs/`），已修正。

### Step 4: exp-003 启动状态
- **tmux session**: `exp003`，PID 126565
- **数据加载成功**: 8 models × 9 judges × 176 items = 5661 observations (44.7% sparsity)
- **当前阶段**: `mfrm_only` 模型 XLA 编译中（4 chains），编译完成后进入 MCMC 采样
- **GPU 显存**: GPU 0-1 已分配 ~73GB/98GB，GPU 2-3 待分配
- **日志**: `/root/gated_mfrm_judge_bias/exp003/run.log`

已设置 5 分钟后自动检查采样进度。

---
