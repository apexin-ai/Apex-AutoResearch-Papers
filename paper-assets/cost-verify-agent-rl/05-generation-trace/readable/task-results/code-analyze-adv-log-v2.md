# code analyze adv log v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-adv-log-v2_20260517T204257_result.json`
- **Structured JSON:** [`89d4fc5905b24ff562f8.json`](../../sessions/89/89d4fc5905b24ff562f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果摘要：

**关键发现（与预期不符）**：
- **r(sign, outcome) = 0.12** — sign misattribution 很弱，不是预期的 >0.95
- P(adv>0 | success) = 0.43, P(adv>0 | failure) = 0.30 — 差异小
- 分布 overlap = 0.81 — 两组分布高度重叠
- Magnitude decay: γ=0.97, R²=0.54 — 中等衰减
- Sign rate std = 0.12 across positions（但样本量不均）

产出文件：
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis.pdf`
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis.png`
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis_summary.json`

脚本位于 `/root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`。

注意：这些数据**不支持**原始 sign misattribution 假设（r 仅 0.12）。可能原因：(1) outcome 判定阈值 `max_ret > 1.0` 不匹配实际数据分布（23/120 episodes 被判为 success）；(2) z-score 归一化跨 batch 而非 episode-internal，削弱了 episode-level 效应；(3) h=2 实验的 window 数远超 2（实际 0-14），说明数据来源可能不是纯 h=2 配置。需要确认实验配置和 outcome 定义。

---
