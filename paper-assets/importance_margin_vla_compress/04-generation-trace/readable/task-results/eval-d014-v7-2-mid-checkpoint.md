# eval d014 v7 2 mid checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d014-v7_2-mid-checkpoint_20260515T213222_result.json`
- **Structured JSON:** [`5d843cd55a87e8bde436.json`](../../sessions/5d/5d843cd55a87e8bde436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。汇总结果：

## v7.2 Mid-Checkpoint Eval 结果

| Checkpoint | clean action_loss | G3 ratio (vs BL 0.00408) | margin_median | preservation@eps0.01 | LED median@eps0.02 |
|---|---|---|---|---|---|
| step_010000 | 0.04257 | **10.43x** | 0.3973 | 0.9323 | 0.2687 |
| step_020000 | 0.03297 | **8.08x** | 0.4724 | 0.9027 | 0.3853 |

数据来源：
- `eval_results/eval_imm_v7_2_step010000.json` → `eps0.0_pruneFalse.action_loss`
- `eval_results/eval_imm_v7_2_step020000.json` → `eps0.0_pruneFalse.action_loss`
- G3 ratio = clean action_loss / baseline 0.00408
- preservation = `eps0.01_pruneFalse.preservation_rate`
- LED median = `eps0.02_pruneFalse.l_eps_delta_ratio_median`

## 趋势分析

**action_loss 在下降**：0.04257 → 0.03297（-22.5%，10K steps 间隔），但当前 step_020000 的 eval action_loss（0.0330）仍是 baseline（0.00408）的 **8.08 倍**，远超 G3 阈值（≤1.10x）。

**关键问题**：训练 train loss 在 step 20K 报 0.0028，但 eval action_loss 是 0.0330——两者差 10 倍以上。这可能是因为：
1. 训练集 vs 评估集的分布差异
2. 模型尚未充分收敛（当前 latest = step_028000，训练仍在进行）
3. eval 用的是 50 batches 采样，可能波动较大

**margin 和 preservation 表现**：margin_median 从 0.3973 上升到 0.4724，preservation@eps0.01 从 93.2% 略降到 90.3%，这些 IMM 指标相对健康。

**G3 预判**：以当前下降速率，即使训练到 final（假设 40K-50K steps），eval action_loss 难以降到 0.00449（1.10x baseline）以下。需要关注 final eval 是否有不同的计算方式或 batch size（500 vs 50）会带来显著差异。

---
