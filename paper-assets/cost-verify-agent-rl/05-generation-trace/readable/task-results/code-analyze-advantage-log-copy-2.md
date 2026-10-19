# code analyze advantage log

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-advantage-log_20260517T160047_result.json`
- **Structured JSON:** [`18918a5dde66f7abc34a.json`](../../sessions/18/18918a5dde66f7abc34a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本完善完成，dry-run 全部通过。关键结果：

**Analysis 3 修复后**：
- Step return 完美遵循 γ^k 衰减：**R² = 1.0000, gamma = 0.9500**（与理论一致）
- Advantage magnitude 衰减：R² = 0.6368, gamma_fit = 0.8877（中等拟合，说明 advantage 大致跟随 return 但受 batch 归一化影响）

**总体结论**：
| 指标 | 值 | 含义 |
|------|-----|------|
| Sign vs Outcome | r=0.317 | 中等，非主导 |
| Sign vs Local Quality | r=0.432 | 更强 |
| Advantage vs Return (continuous) | r=0.901 | 极强 |
| Return decay R² | 1.000 | 理论验证通过 |
| Within-ep variance (fail) | 6.9e-5 | 失败 episode 内部几乎无分化 |

**结论**：step_independent 模式下 advantage 主要由 local quality (step_return) 决定，sign misattribution 不是主导模式。但失败 episode 内部方差极低（6.9e-5 vs 总方差 0.0026），说明**失败 episode 内部信号极弱**——所有失败窗口获得几乎相同的负 advantage，无法区分"差一点成功"和"完全错误"。

脚本位于 `/root/cost-verify-agent-rl/scripts/analyze_advantage_log.py`，可视化输出在 `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/analysis/`。

---
