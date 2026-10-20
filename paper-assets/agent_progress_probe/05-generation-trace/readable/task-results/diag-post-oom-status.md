# diag post oom status

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_post-oom-status_20260514T141017_result.json`
- **Structured JSON:** [`710560774c6bc88673e1.json`](../../sessions/71/710560774c6bc88673e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 0% | 0 MiB / 32607 MiB | **空闲** |
| cuda:1 | 8% | 719 MiB / 32607 MiB | **在用** (fewshot_probe.py, PID 57051) |

### 2. openhands-fewshot-probe
- **状态**: 刚启动 ~5 分钟（PID 57040），运行在 cuda:1
- 已保存 3 个 checkpoint（5%/10%/20% 比例），但 `fewshot_results.json` 尚未生成
- 日志当前为空（还在初始化或加载数据阶段）
- tmux session `openhands-fewshot-probe` 存活

### 3. 2×2 交叉评估 — **已完成**

结果 (`cross_label_eval_results.json`):

| 模型 | 标签方案 | macro_F1 | accuracy | F1_stag | F1_prog |
|------|----------|----------|----------|---------|---------|
| probe_001 | 3LF (safe) | **0.885** | 0.941 | 0.805 | 0.965 |
| without_ob | 3LF (safe) | 0.543 | 0.851 | 0.167 | 0.918 |
| probe_001 | 2LF (safe) | 0.491 | 0.965 | 0.000 | 0.982 |
| without_ob | 2LF (safe) | 0.496 | 0.985 | 0.000 | 0.992 |

**关键发现**: probe_001 在 3LF 标签下远优于 without_ob（macro_F1 0.885 vs 0.543），主要差距在 stagnation 识别（0.805 vs 0.167）。2LF 下两者都无法检测 stagnation（F1=0）。

### 4. train-without-ob — **已完成** (EXIT_CODE=0)
- 最终测试结果 (without OB, conf≥2, 2LF): macro_F1=0.951, accuracy=0.976, F1_stag=0.916, F1_prog=0.986
- 已保存到 `/root/autodl-tmp/agent_progress_probe/checkpoints_without_ob`
- 进程已退出，无残留

---
