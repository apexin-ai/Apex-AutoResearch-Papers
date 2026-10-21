# diag grid b low failures

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grid_b_low_failures_20260516T000650_result.json`
- **Structured JSON:** [`57c0b6c6241c84fa8a51.json`](../../sessions/57/57c0b6c6241c84fa8a51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张 GPU 当前都被占用。以下是诊断报告。

---

## grid_b_low 连续 4 次失败诊断报告

### 一、各次失败根因

| 次数 | 实验名 | 根因分类 | 退出信号 | 进度 | 详情 |
|------|--------|---------|---------|------|------|
| **R1** | grid_b_low_seed42 | **infra bug** | Terminated (无 exit code) | 431/8477 (5%) | cron 框架 `reconcile_crons` 误判进程死亡并 SIGTERM。WANDB_MODE=disabled 导致 tmux wrapper PID 不匹配。训练可能曾完成部分 b 值，但 checkpoint 丢失。日志不在 registry 中。 |
| **R2** | grid_b_low_seed42_r2 | **script bug** | EXIT_CODE=1 | 0 步 | 通过 `bash -c "..."` 双引号提交，`$b` 被外层 shell 展开为空字符串。日志明确显示 `=== Training grid b= ===`，argparse 报错 `--grid_b_value: expected one argument`。 |
| **R3** | grid_b_low_seed42_r3 | **resource conflict** | EXIT_CODE=129 (SIGHUP) | 169/6103 (3%) | 未指定 GPU，落在 cuda:0 与 `contamination_60_seed42_r2` 冲突。速度从正常 ~2.15s/it 降至 ~3.34s/it，被终止。 |
| **R4** | grid_b_low_serial_seed42 | **resource conflict** | EXIT_CODE=143 (SIGTERM) | 76/6103 (1%) | 指定了 cuda:2 但与 `contamination_60_ess_only_seed42` 冲突。速度 ~4.50s/it（正常应 ~2.1s/it），双进程占满显存 93042/97887 MiB，仅完成 48 步。 |

### 二、成功脚本 vs 失败脚本对比

**成功脚本** (`run_grid_b_seed42.sh`，b=0.5~5.0）：
- `for b in 0.5 1.0 ...` + `--grid_b_value $b` — 直接 bash 执行，变量展开正确
- 有 `--eval_steps 500`
- 无 `WANDB_MODE=disabled`
- 无显式 `CUDA_VISIBLE_DEVICES`（但恰好在空 GPU 上运行）

**当前 R5 脚本** (`run_grid_b_low_serial.sh`，b=0.1~0.3）：
- ✅ 硬编码 3 个 b 值，不用 for 循环 — **R2 quoting 问题已修复**
- ❌ **无 `CUDA_VISIBLE_DEVICES`** — R3/R4 冲突问题未修复
- ❌ 无 `--eval_steps`（成功脚本有）
- ❌ 无 `--tau 0.8`（v2 脚本有，当前脚本没有）
- ⚠️ 无 `WANDB_MODE=disabled`（R1 的 cron 问题已不用担心，但也意味着需要 wandb 连接）

### 三、当前 GPU 状态

| GPU | 占用实验 | PID |
|-----|---------|-----|
| cuda:0 | contamination_60_seed42_r2 | 257977 |
| cuda:1 | contamination_60_uniform_seed42 | 250074 |
| cuda:2 | contamination_60_ess_only_seed42 | 265012 |
| cuda:3 | contamination_60_grid_b0_5_seed42 | — |

**所有 4 卡均被占用（各 ~46.5GB / 97.9GB）。当前无法提交 R5。**

### 四、残留 checkpoint 状态

- `output/models/grid_b0_1_seed42/` — 仅有 `config.json` + `step_metrics.jsonl`，无模型权重（save_steps=500，R3/R4 均未达到 500 步）
- `grid_b0_2_seed42/`、`grid_b0_3_seed42/` — 不存在

### 五、R5 重跑前置条件和建议

**前置条件：**
1. 等待至少 1 张 GPU 完全释放（registry 中 contamination_60_uniform_seed42 可能最先完成）
2. 清理残留 output 目录 `rm -rf output/models/grid_b0_1_seed42/`

**脚本修复建议（`run_grid_b_low_serial.sh`）：**
1. 添加 `export CUDA_VISIBLE_DEVICES=X`（X = 空闲 GPU 编号）
2. 添加 `--eval_steps 500` 与成功脚本对齐
3. 添加 `--tau 0.8` 与 v2 脚本对齐
4. 考虑添加 `WANDB_MODE=disabled` 避免 wandb 连接问题

**推荐 R5 提交命令模板**（待 GPU 释放后）：
```bash
# 假设 cuda:1 释放
CUDA_VISIBLE_DEVICES=1 nohup bash /root/provenance_weight_training/run_grid_b_low_serial.sh \
  > ~/runs/provenance_weight_training/grid_b_low_serial_seed42_r5.log 2>&1 &
```

其中 `run_grid_b_low_serial.sh` 开头需加入：
```bash
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
```
确保 GPU 绑定不被覆盖。

---
