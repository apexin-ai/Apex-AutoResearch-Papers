# ssh exp018 synthetic n20

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp018_synthetic_n20_20260523T085406_result.json`
- **Structured JSON:** [`1fc78d825fb1a5d0d714.json`](../../sessions/1f/1fc78d825fb1a5d0d714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-018 已提交并运行中。

**汇总：**
- 脚本：`/root/gated_mfrm_judge_bias/exp018/run_exp018.py`
- 改动：`N_MODELS=20`（exp-015 为 8），输出 `synthetic_n20.csv`/`summary_n20.json`，GPU `cuda:2`，新增 Wilcoxon Δτ 检验
- DGP 分布与 exp-015 完全一致：`θ~N(0,1)`, `c~|N(0,1.5)|`, `b~N(0,1)`, `d~N(0,0.5)`, `e` 30%/70% 分布, `ρ=0.6`
- 支持 resume（已完成的 seed 自动跳过）
- tmux 会话：`exp018`，服务器 `autodl-8gpu`，GPU 2
- Registry 状态：RUNNING，spec 已填充 provenance 信息

---
