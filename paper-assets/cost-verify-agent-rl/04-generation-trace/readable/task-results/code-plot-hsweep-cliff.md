# code plot hsweep cliff

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plot_hsweep_cliff_20260517T074115_result.json`
- **Structured JSON:** [`722ec50f2070e231dfe9.json`](../../sessions/72/722ec50f2070e231dfe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**1. 数据格式发现**
- Metrics 在 Ray worker 日志中，格式为 `step:N - key:value - ...`
- tee'd 日志在 `/root/runs/cost-verify-agent-rl/hsweep-h{H}-seed{N}.log`（带 ANSI+Ray pid 前缀）
- 关键字段：`val-env/AlfworldSG/success:np.float64(X)` 和 `train/AlfworldSG/success:np.float64(X)`
- Val eval 在 step 0 和每 5 steps（test_freq=5）

**2. 脚本路径**
- `/root/cost-verify-agent-rl/scripts/plot_hsweep_cliff.py`（356 行）

**3. 验证结果**
- 语法检查通过
- `--demo` 模式：输出 PDF（32KB）+ PNG（316KB），5 条 h 曲线正确生成
- 真实数据模式：正确读取了 `hsweep-h2-seed1`（当前 step 0-4，val 只有 step 0）

**用法**：
```bash
# Demo 模式（合成数据）
python plot_hsweep_cliff.py --demo --output_dir ./figures/

# 真实数据（数据跑完后）
python plot_hsweep_cliff.py --output_dir ./figures/
```

---
