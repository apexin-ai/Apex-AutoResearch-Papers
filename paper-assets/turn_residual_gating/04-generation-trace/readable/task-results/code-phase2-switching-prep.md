# code phase2 switching prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_switching_prep_20260525T062236_result.json`
- **Structured JSON:** [`6ee982aaff653756577b.json`](../../sessions/6e/6ee982aaff653756577b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/turn_residual_gating/src/eval_switching.py`，语法检查通过。

运行命令（GPU 空闲后）：

**ThreadGate 模型：**
```bash
cd /root/turn_residual_gating/src && python eval_switching.py \
  --checkpoint-path /root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2 \
  --data-path /root/turn_residual_gating/data/eval_200/eval_200.json \
  --output-path /root/turn_residual_gating/results/switching_tg/
```

**Base 模型（无 LoRA/无 gate）：**
```bash
cd /root/turn_residual_gating/src && python eval_switching.py \
  --data-path /root/turn_residual_gating/data/eval_200/eval_200.json \
  --output-path /root/turn_residual_gating/results/switching_base/
```

脚本要点：
- 7 个条件：pure_tf、pure_ar、switch_k1-k5
- GAR 在每个 assistant turn 的 **mid-point token** 位置测量（content_start 和 content_end 的中点）
- Gate hooks 在 generate 时为 no-op（turn_features_ref 为 None），仅在 measurement forward pass 时激活
- 输出两个 JSON：`switching_results.json`（per-turn 平均）和 `switching_detail.json`（per-conversation 明细 + std）
- 最后打印 summary table 方便快速查看

---
