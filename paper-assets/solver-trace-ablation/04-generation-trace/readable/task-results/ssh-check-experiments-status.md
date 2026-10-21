# ssh check experiments status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-experiments-status_20260513T235534_result.json`
- **Structured JSON:** [`e76053eeb4265982b42f.json`](../../sessions/e7/e76053eeb4265982b42f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告（数据来源：SSH 日志，westd-39279）

### 进程状态
- **PID 84901 (plan001)** 和 **PID 85790 (plan005)**：均已终止（PROCESSES_DEAD）
- **GPU**：双卡空闲（0% utilization, 0 MiB），无 tmux session
- **两个实验均已正常完成**（EXIT_CODE=0）

---

### plan001-exec-only-s42-r2 ✅ DONE

| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| 训练时长 | 1h02m57s (7.55s/it) |
| **overall prove_rate** | 0.6743 |
| **overall mean_isr** | 0.6678 |
| last50 prove_rate | 0.8525 |
| last50 isr | 0.8525 |
| **last100 prove_rate** | **0.8650** |
| **last100 isr** | **0.8612** |
| parse_rate | 1.0 |

---

### plan005-sta-low-s42 ✅ DONE（registry 需更新为 DONE）

| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| 训练时长 | 1h11m37s (8.59s/it) |
| **overall prove_rate** | 0.5658 |
| **overall mean_isr** | 0.1682 |
| last50 prove_rate | 0.7700 |
| last50 isr | 0.2559 |
| **last100 prove_rate** | **0.7725** |
| **last100 isr** | **0.2299** |
| parse_rate | 1.0 |

---

### 对比（last100）

| 指标 | plan001 (exec-only) | plan005 (sta-low) | 差异 |
|------|-------|-------|------|
| prove_rate | **0.8650** | 0.7725 | **-0.0925 (-10.7%)** |
| isr | **0.8612** | 0.2299 | **-0.6313 (-73.3%)** |

**结论**：plan005 (sta-low) 的 prove_rate 比 exec-only 低 ~10%，isr 大幅低 73%。STA-low 配置显著拖累了 ISR 表现。

---

### 代码就绪状态
- `scripts/train_grpo.py` ✅ 存在 (14758 bytes)
- `configs/` ✅ 5个配置文件就绪：
  - `grpo_exec_only.yaml`, `grpo_exec_sta.yaml`
  - `grpo_prolog_exec_only.yaml`, `grpo_prolog_exec_sta.yaml`
  - `grpo_random_reward.yaml`

---
