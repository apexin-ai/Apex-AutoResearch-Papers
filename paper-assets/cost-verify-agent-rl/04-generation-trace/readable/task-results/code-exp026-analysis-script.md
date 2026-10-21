# code exp026 analysis script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp026_analysis_script_20260515T120823_result.json`
- **Structured JSON:** [`ba3e23dc0c1ec2a724b7.json`](../../sessions/ba/ba3e23dc0c1ec2a724b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，通过合成日志验证通过。

使用方式：
```bash
python artifacts/analyze_exp026.py --log /path/to/exp026.log --output artifacts/
```

输出：
- `artifacts/exp026_summary.json` — 关键统计（best success、convergence step、collapse/KL/pg_loss 检测）
- `artifacts/exp026_training_curves.png` — 6 子图（success_rate、pg_loss、entropy、KL、reward_mean、action_is_valid）

服务器上需要 matplotlib，本地一般已有。

---
