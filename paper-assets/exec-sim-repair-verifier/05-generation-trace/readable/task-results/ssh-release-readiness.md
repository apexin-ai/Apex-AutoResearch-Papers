# ssh release readiness

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_release-readiness_20260520T125103_result.json`
- **Structured JSON:** [`7e3fb8a50c63a0e680fb.json`](../../sessions/7e/7e3fb8a50c63a0e680fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 检查结果

### 检查 1: Auto-eval 监控进程 — 全部正常

| 进程 | PID | 状态 | 运行时长 |
|------|-----|------|----------|
| s123-v2 train | 925638 | ALIVE | 7h08m |
| s456-v2 train | 949112 | ALIVE | 3h47m |
| s123-v2 monitor | 957333 | ALIVE | 1h45m |
| s456-v2 monitor | 957406 | ALIVE | 1h45m |

4× RTX 5090 全部 98-99% 利用率，训练正常进行。Monitor 每 5 分钟检查一次，训练进程结束后自动触发 `eval_deepseek_cwm_s{123,456}_v2.sh`。**无需操作。**

### 检查 2: W5 回归数据路径匹配 — 兼容

`w5_mixed_effects_v2.py` 通过 `--eval_dirs` 接收逗号分隔的目录路径，从目录名推断 metadata：
- formulation: 包含 `cwm`/`traj`/`cls`
- model: 包含 `qwen`/`deepseek`
- seed: `s(\d+)` 模式
- complexity: 包含 `func` → function，否则 → repo

查找预测文件优先级：`eval_*_predictions.jsonl` > `predictions_*.jsonl` > `results_incremental.jsonl` > `predictions.jsonl`

现有 eval 目录命名（如 `deepseek_cwm_repo_s123_test`）和文件格式（`eval_repo_cwm_predictions.jsonl`）均能被正确解析。**路径匹配无问题。**

### 检查 3: Figure 2 数据输入 — 硬编码 DATA dict

`plot_figure2_v2.py` 使用硬编码 `DATA` dict，当前填充状态：

| 粒度 | 公式 | Qwen | DeepSeek |
|------|------|------|----------|
| func | CLS | **0.0** | **0.0** |
| func | CWM | **0.0** | **0.0** |
| func | TRAJ | **0.0** | **0.0** |
| repo | CLS | 84.83 ✓ | 84.38 ✓ |
| repo | CWM | **0.0** | **0.0** |
| repo | TRAJ | 73.61 ✓ | **0.0** |

9/12 个数据点仍为 placeholder。DeepSeek CWM repo 的 s123/s456 eval 完成后可填充 `repo/CWM/deepseek`，其余缺失数据需对应实验完成后手动更新 DATA dict。

**结论**: 3 项检查均无阻塞问题。两组 DeepSeek CWM 训练 + 自动 eval 正常运行中，完成后需手动将结果数字回填 `plot_figure2_v2.py` 的 DATA dict。

---
