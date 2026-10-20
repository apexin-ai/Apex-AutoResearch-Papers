# code v2 gradient analysis script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-analysis-script_20260526T160534_result.json`
- **Structured JSON:** [`3ff8dbcf64bab3877950.json`](../../sessions/3f/3ff8dbcf64bab3877950.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署并验证通过。

**`run_gradient_analysis_v2.py`** — 分析脚本：
- 参数：`--checkpoint_dir`, `--condition_name`, `--seed`, `--num_samples`(默认200）, `--output_dir`, `--data_dir`, `--occ_data_dir`, `--gpu`
- 自动检测 `occ_detach`（condition 含 "detach"/"vanilla" → True）和 `occ_norm`（含 "bn" → bn，否则 ln）
- 自动检测 Vanilla（无 OCC head checkpoint → 跳过 OCC 梯度计算）
- 方法论完全匹配 v1：逐层 backbone 参数梯度、L2 norm、cosine similarity、conflict rate
- 输出 `{condition}_gradient_stats.json` + `{condition}_gradient_raw.json`

**`plot_gradient_analysis_v2.py`** — 可视化脚本：
- 4 panel：(a) action grad norms, (b) OCC grad norms, (c) cosine similarity, (d) ratio vs Vanilla
- 可选 `--v1_results_dir /root/autodl-tmp/analysis/gradient_same_seed/` 生成 v1 vs v2 对比 CSV
- 输出 PDF + PNG

**运行示例**（v2 checkpoint 到位后）：
```bash
cd /root/occsafe_vla/openvla-oft
OUT=/root/occsafe_vla/artifacts/gradient_v2

# 1. Vanilla
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/vanilla_retrain_s0/.../50000_chkpt \
  --condition_name "Vanilla v2" --seed 42 --output_dir $OUT

# 2. Full OCC LN v2
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/.../50000_chkpt \
  --condition_name "Full OCC LN v2" --seed 42 --output_dir $OUT

# 3. Detach LN v2
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s0/.../50000_chkpt \
  --condition_name "Detach LN v2" --seed 42 --output_dir $OUT

# 4. 生成图 + v1对比
python3 /root/occsafe_vla/scripts/plot_gradient_analysis_v2.py \
  --results_dir $OUT \
  --v1_results_dir /root/autodl-tmp/analysis/gradient_same_seed/ \
  --output $OUT/gradient_analysis_v2_combined.pdf
```

---
