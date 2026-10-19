# analysis exp 004 eval ckpt3500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-eval-ckpt3500_20260520T153847_result.json`
- **Structured JSON:** [`35c94e34833ab2cffb78.json`](../../sessions/35/35c94e34833ab2cffb78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

**exp-004-eval-ckpt3500**:
- **ToF=0.1326, NoF=0.9006, SYCONScore=0.2312** (n_total=362, n_valid=181, n_invalid=181)
- vs vanilla baseline: 0.2312 vs 0.1335 = **+73.2%**
- **Conclusion: success**

**Dip region 发现**: ckpt-3500 的 SYCONScore (0.2312) 高于两侧邻居 ckpt-3000 (0.2058) 和 ckpt-4000 (0.2140)，呈非单调振荡。dip 底部仍在 ckpt-3000，ckpt-3500 部分恢复后 ckpt-4000 再次下降，直到 ckpt-5000 才完全恢复。整个 dip region 所有 checkpoint 均远高于 vanilla baseline，说明 ACT 的校准增益在训练不稳定区间也保持稳健。

额外收获：同批次还评估了 ckpt-2500 (SYCONScore=0.2389)，已一并写入报告。

- **checkpoint_path**: `/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-3500`
- **log_path**: `~/runs/contrastive_entrain_calib/exp-004-eval-ckpt3500.log` (westd-28034)

报告已写入 `artifacts/exp-004-eval-ckpt3500/report/report_fragment_exp004_ckpt3500.md`。

---
