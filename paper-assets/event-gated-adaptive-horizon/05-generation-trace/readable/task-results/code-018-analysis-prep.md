# code 018 analysis prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_018-analysis-prep_20260516T044808_result.json`
- **Structured JSON:** [`1cd28173d5d5fe00b415.json`](../../sessions/1c/1cd28173d5d5fe00b415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出物：

**1. 分析脚本** `scripts/analyze_018_full_sgs.py` — 已部署到服务器并通过 dry-run 验证
- 用 008d 代替 018 测试，正确输出 CIVO_PRESENT（NVE 4.13x, 4 consecutive checkpoints）
- 008f 正确判定 CIVO_ABSENT（NVE 1.02x）
- 016e 正确判定 CIVO_PRESENT（NVE 10.42x）
- 生成了 eval curves 和 NVE trajectories 的 PDF/PNG 图表（~20KB/90KB）

**2. 判断标准文档** `artifacts/_project/report/018_analysis_criteria.md`
- 三行决策表：NVE<1.5x → gradient-level / NVE>1.5x → representation-level / transient → partial
- 参考实验对比逻辑（018 vs 008d/016e/008f）
- 完整运行命令

018 训练完成后运行：
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
python scripts/analyze_018_full_sgs.py \
  --logdir-018 logdir/exp_018_full_sgs_walker_s1 \
  --logdir-008d logdir/exp_008d_subsample_on_h8 \
  --logdir-008f logdir/exp_008f_no_dt_embed_subsample_on_h8 \
  --logdir-016e logdir/exp_016e_sgs_walker_s1 \
  --baseline-logdir logdir/baseline_s1 \
  --output-dir artifacts/018_analysis
```

---
