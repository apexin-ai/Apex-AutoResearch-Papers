# ops libero eval pipeline v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_libero_eval_pipeline_v2_20260516T200753_result.json`
- **Structured JSON:** [`38ff109b7c19a089c951.json`](../../sessions/38/38ff109b7c19a089c951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。**成功率 6/10 = 60%，pipeline 正常工作。**

结果摘要：

| Episode | Task | Result | Steps |
|---------|------|--------|-------|
| 0 | pick up black bowl between plate and ramekin → plate | FAIL | 220 (timeout) |
| 1 | pick up black bowl in top drawer of cabinet → plate | PASS | 137 |
| 2 | pick up black bowl next to cookie box → plate | FAIL | 220 |
| 3 | pick up black bowl next to plate → plate | PASS | 92 |
| 4 | pick up black bowl next to ramekin → plate | FAIL | 220 |
| 5 | pick up black bowl on cookie box → plate | PASS | 84 |
| 6 | pick up black bowl on ramekin → plate | FAIL | 220 |
| 7 | pick up black bowl on stove → plate | PASS | 180 |
| 8 | pick up black bowl on wooden cabinet → plate | PASS | 113 |
| 9 | pick up black bowl between plate and ramekin → plate | PASS | 75 |

Action 统计（合理范围 ±1）：
- Per-dim mean: [0.096, 0.091, -0.124, -0.002, -0.008, -0.023, -0.141]
- Per-dim range: xyz在[-0.75, 0.97], rotation在[-0.2, 0.3], gripper在[-1.04, 1.04]

**分析**：
1. **Pipeline 已验证可用** — 不是 0%，模型在产出有意义的动作并成功完成任务
2. **60% vs 期望的 >80%** — 这只是 10 episodes、1 个 seed、libero_spatial suite。官方 benchmark 用 50 episodes × 10 tasks。高方差下 60% 与 ~80% 的真实水平一致
3. 失败的 episode 都是跑满 220 步 timeout，说明机器人在动但没能及时完成（不是静止不动或乱动）
4. LIBERO 无需额外安装 — LIBERO-Plus (`/root/LIBERO-plus/`) 已包含所有标准 benchmark（libero_spatial/object/goal/10/90）

如果需要更可靠的数字，可以用 `evaluate_libero_plus.py` 跑 50 episodes × 多 seed 的完整 eval。

---
