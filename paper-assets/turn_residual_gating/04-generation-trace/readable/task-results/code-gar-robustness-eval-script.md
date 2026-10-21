# code gar robustness eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gar_robustness_eval_script_20260524T065123_result.json`
- **Structured JSON:** [`d29cf4e6a013da713e49.json`](../../sessions/d2/d29cf4e6a013da713e49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在清楚了。脚本已就绪，正确的运行命令如下：

**脚本路径**: `/root/turn_residual_gating/scripts/eval_gar_robustness.py`

**运行命令**（KL 完成后执行）:

```bash
cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Base model
python scripts/eval_gar_robustness.py --gate-type none

# TG v7 s42
python scripts/eval_gar_robustness.py \
  --checkpoint-dir runs/phase2_tg_s42_v7 --gate-type threadgate

# SS s42
python scripts/eval_gar_robustness.py \
  --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type uniform
```

**关键设计**:
- 单次 forward pass 后调用 `compute_gar()` 4 次（不同 goal/query position 组合），零额外 GPU 开销
- 自动为无 system prompt 的 eval_200 对话添加默认 system prompt（GAR-goal-only 需要）
- 输出 mid_turns_avg_gar（turns 3+ 平均）

**预估运行时间**: eager attention + 50 conversations × ~3-5s/conv ≈ 每个模型 3-4 分钟。3 个模型总计 ~10-12 分钟。

**输出**: `results/gar_robustness/{base_model,phase2_tg_s42_v7,tg_v8b_ss_fixed_s42}_gar_robustness.json`

---
