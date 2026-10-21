# diagnose exp 009 v3 post restart

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009_v3_post_restart_20260517T062050_result.json`
- **Structured JSON:** [`ec465330047602772948.json`](../../sessions/ec/ec465330047602772948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 进程状态

| 实验 | PID | 存活 | 死亡时间 |
|------|-----|------|----------|
| exp_009_dose_10pct_v3 | 93385 | **N** | ~13:07 (eval阶段 tokenizing 54%) |
| exp_009_dose_30pct_v3 | 93527 | **N** | ~13:08 (graduated_seed3 数据准备) |
| exp_009_dose_50pct_v3 | 93604 | **N** | ~13:06 (eval阶段 loglikelihood 30%) |

### GPU 状态

4 块 RTX 4090 (24GB) 全部空闲，0% 利用率，0 MiB 显存占用。

### 已完成进度

| 实验 | 已完成 | 剩余 |
|------|--------|------|
| 10pct | **11/15** | graduated_seed3 + seed4 全部 (4 cycles) |
| 30pct | **11/15** | graduated_seed3 + seed4 全部 (4 cycles) |
| 50pct | **10/15** | binary_ours_seed3(eval), graduated_seed3 + seed4 全部 (5 cycles) |

所有已完成结果均已持久化到 `results/exp_009_dose_response/ratio_*/` 目录（每个 seed×strategy 独立保存 JSON）。脚本支持自动 resume（检查 eval 文件是否存在即跳过）。

### 重启命令

```bash
# 在服务器上，用 tmux 分 3 个 pane 运行
tmux new-session -d -s exp009v3

# 10pct → cuda:1
tmux send-keys -t exp009v3 'cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5 2>&1 | tee -a ~/runs/gen-depth-contamination/exp_009_dose_10pct_v3.log' Enter

# 30pct → cuda:2
tmux split-window -t exp009v3
tmux send-keys -t exp009v3 'cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5 2>&1 | tee -a ~/runs/gen-depth-contamination/exp_009_dose_30pct_v3.log' Enter

# 50pct → cuda:3
tmux split-window -t exp009v3
tmux send-keys -t exp009v3 'cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=3 python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5 2>&1 | tee -a ~/runs/gen-depth-contamination/exp_009_dose_50pct_v3.log' Enter
```

预计耗时：10pct/30pct ~1h45m，50pct ~2h20m。需要我执行重启吗？

---
