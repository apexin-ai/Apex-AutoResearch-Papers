# ops git sync check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_git-sync-check_20260526T121341_result.json`
- **Structured JSON:** [`ba6478b71d2af01859ad.json`](../../sessions/ba/ba6478b71d2af01859ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有三个 SSH 端点都无法连接。

## 报告

### 1. 远程服务器 git 仓库状态
**无法连接。** 三个 SSH 端点均连接失败：
- `autodl-5090` (bjb1:21071) — 连接被拒
- `bjb2-11496` (bjb2:11496) — 连接被拒
- `westb-25965` (westb:25965) — 连接被拒

AutoDL 实例可能已关机或重启导致端口变更。**需要去 AutoDL 控制台确认实例状态，如果已重启请更新 `~/.ssh/config` 中的端口号。**

### 2. 最新 commit hash
无法获取（服务器不可达）。

### 3. 本地 code/ 目录状态
- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/`
- **不是 git 仓库**
- 包含 14 个文件（13 个 .py + 1 个 .tex + 1 个 .csv + 1 个 .json + 图表文件），关键实验脚本：
  - `exp_b3_prompted_diversity.py` — prompted diversity 实验
  - `run_spider_sc.py` — Spider SC 实验
  - `theta_crit_sweep.py` — theta 临界值扫描
  - `aggregate_scaling_results.py` / `plot_scaling_curve.py` — scaling 分析
  - `analysis_mbr_selection.py` / `ner_lp_f1_correlation.py` — 结果分析
  - `zeroshot_prompts.py` — zero-shot prompts

### 4. 本地项目根目录
项目根目录有完整的结构（docs/, artifacts/, checkpoints/, anon_repo/ 等），但 code/ 子目录未纳入 git 管理。

### 5. 执行的同步操作
无——服务器不可达，未能执行任何 commit/push 操作。

**下一步**：请到 AutoDL 控制台检查 autodl-5090 实例是否在线，如果端口已变更请告知新端口。

---
