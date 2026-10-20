# infra exp006 fix and restart

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006_fix_and_restart_20260513T210046_result.json`
- **Structured JSON:** [`4c8da9f0284ff467ca2c.json`](../../sessions/4c/4c8da9f0284ff467ca2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bc 安装成功，验证通过（`50*25/60 = 20.8`）。

## 汇总

| 项目 | 状态 |
|------|------|
| **崩溃原因** | `bc: command not found`，第 68 行 `est_hours=$(echo "scale=1; $total_runs * 25 / 60" \| bc)` |
| **bc 用途** | 仅用于打印预估 GPU 时间，不影响训练/评测逻辑 |
| **已完成 run** | 1/50+（仅 base_model 评测，0 个 strategy run） |
| **Resume 支持** | 有，脚本检查 `eval_results.json` 存在则跳过 |
| **修复** | 已安装 bc，验证通过 |

### 重启命令

直接重新运行即可，base_model 会被自动跳过：

```bash
cd /root/autodl-tmp/gen-depth-contamination && \
nohup bash scripts/run_exp006.sh --strategy all --seeds "42 123 456 789 1024" \
  > ~/runs/gen-depth-contamination/exp_006_graduated_filtering.log 2>&1 &
```

不需要改脚本。预计 ~50 个 run × 25min ≈ 20.8h。

---
