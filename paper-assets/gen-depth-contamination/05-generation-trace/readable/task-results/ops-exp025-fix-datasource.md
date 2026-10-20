# ops exp025 fix datasource

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025-fix-datasource_20260518T082513_result.json`
- **Structured JSON:** [`1770ab2e4ca227330b64.json`](../../sessions/17/1770ab2e4ca227330b64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，4 个 GPU 并行跑 Batch 1。

## Kill 结果
killed 6 个进程（4 python 训练 + 1 bash launcher + 1 nohup wrapper），无 tmux session

## 数据确认
- nucleus 数据路径: `/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_nuc09/`
- depth 文件: depth_0~5.jsonl，每个 5000 行，共 30000 条

## 脚本修改
- `scripts/exp025_pythia_filtering.py`: `DATA_DIR` 从 `data_exp020_pythia_greedy` → `data_exp020_pythia_nuc09`
- `scripts/run_exp025.sh`: 无数据路径变量，无需修改

## 清理
- 删除 `results/exp_025_pythia_filtering/`、`checkpoints/exp025*/`、`logs/exp025/`

## 重新提交
- Batch 1 已启动：4 个 GPU 分别跑 no_filter×3seeds + binary_ours×seed42
- 主进程 PID=15687，9 个 run 分 3 批串行执行

---
