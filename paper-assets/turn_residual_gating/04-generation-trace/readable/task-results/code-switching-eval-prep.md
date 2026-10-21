# code switching eval prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_switching_eval_prep_20260525T214123_result.json`
- **Structured JSON:** [`7eb0262a175a9783ff6b.json`](../../sessions/7e/7eb0262a175a9783ff6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功，脚本运行正常。结果显示 switch_k3 在 turn 4（切换后第一个 AR turn）GAR 跳到 0.0736（接近 pure_ar 的 0.0660），验证了脚本逻辑正确。

汇总：

1. **脚本**：复用已有 `/root/turn_residual_gating/src/eval_switching.py`（无需新写）
2. **Checkpoint**：`/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2`（含 gate_params.pt + lora/）
3. **Eval 数据**：`/root/turn_residual_gating/data/eval_200/eval_200.json`
4. **预估运行时间**：dry-run 2 个对话 14s → 50 个对话 × 7 个 condition (pure_tf, pure_ar, k1-k5) ≈ **25-30 分钟**

**完整提交命令**：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/turn_residual_gating/src/eval_switching.py --checkpoint-path /root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2 --data-path /root/turn_residual_gating/data/eval_200/eval_200.json --output-path /root/turn_residual_gating/results/switching_tg_s42_v7 --max-conversations 50 --switch-points 1 2 3 4 5 --max-new-tokens 150
```

Dry-run 初步观察：switch_k3 在切换点后 GAR 立即跳升到接近 pure_ar 水平（turn_4: 0.074 vs pure_ar 0.066），而非渐进衰减，初步支持瞬时分布偏移假说。完整 N=50 实验会给出更可靠的统计结论。

---
