# code plot hsweep cliff and gsweep check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plot-hsweep-cliff-and-gsweep-check_20260517T162113_result.json`
- **Structured JSON:** [`97f70f4c73c3e710b11c.json`](../../sessions/97/97f70f4c73c3e710b11c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种模式都零错误运行通过。

---

## 产出汇总

### 任务 1: plot_hsweep_cliff.py

**状态**: 调通，零 warnings。

**修复内容**（3 处）：
1. `plt.rcParams.update()` 移到 `plt.subplots()` 之前，确保字体配置生效
2. ax1 errorbar 添加 `label='Step-level'`，修复空 legend 警告
3. `extract_curves` 中 `np.nanmean/nanstd` 加 `warnings.catch_warnings()` 过滤 all-NaN 列的 RuntimeWarning；collapse annotation 条件加 `len(valid_points) >= 4` 防越界

**测试结果**：
- 真实数据（h=2, 2 seeds）: `figures/hsweep_cliff.pdf` (20KB) + `.png` (134KB)
- demo 模式（h=2/5/10/20/full, 3 seeds each）: 全部 h 值曲线正确

**后续添加数据**: 只需在 `/root/runs/cost-verify-agent-rl/` 放 `hsweep-h{H}-seed{N}.log` 文件，重跑即可。

### 任务 2: launch_gsweep.sh

**结论**：
- **没有 auto-chain 机制**。脚本是单次运行器（`./launch_gsweep.sh &lt;gamma_label> &lt;seed>`），γ=0.5 完成后**不会**自动启动 γ=0.8
- **没有 `TORCH_COMPILE_DISABLE=1`**
- westd-47453 上只有一个 tmux session `gsweep_g050_h5_seed1` 在跑 γ=0.5，没有 watchdog 进程
- 两台服务器脚本内容一致

**建议**: 如需 auto-chain + `TORCH_COMPILE_DISABLE=1`，可参考 bjb1 的 hsweep_watchdog 模式添加。需要我实现吗？

---
