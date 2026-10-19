# analysis exp 003 eval ckpt6500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt6500_20260521T084710_result.json`
- **Structured JSON:** [`e8d7e7338d7f0a098eec.json`](../../sessions/e8/e8d7e7338d7f0a098eec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**ckpt-6500 SYCONScore = 0.1529，超越 vanilla baseline (0.134) 达 +14.1%。** Eval 完整（362/362 pairs）。

完整 trajectory 更新（含新发现的 ckpt-5500/6000 数据点）：

| Checkpoint | SYCONScore | 趋势 |
|-----------|-----------|------|
| ckpt-4500 | 0.1337 | 前 peak ≈ vanilla |
| ckpt-5000 | 0.1144 | ↓ regression |
| ckpt-5500 | 0.1144 | → 平坦 |
| ckpt-6000 | 0.0846 | ↓↓ 深度 regression |
| **ckpt-6500** | **0.1529** | **↑↑ 反弹，新 peak** |

**对 narrative 的影响**：
- "vanilla ceiling" narrative **被打破** — R3-only GRPO 可以超越 vanilla
- 不是单调 spike-regression，而是 **W-shape 非单调训练动态**（rise → dip → recovery）
- 但 ckpt-6000→6500 的 +80% 跳升（500 步内）波动过大，建议补 ckpt-7000/7500 eval 确认趋势持续性

报告已写入 `artifacts/exp-003/ckpt6500_analysis.md`。

---
