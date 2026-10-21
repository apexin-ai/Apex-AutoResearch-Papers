# code prepare unified ar n50 eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_unified_ar_n50_eval_20260522T235014_result.json`
- **Structured JSON:** [`769426b93685764776f0.json`](../../sessions/76/769426b93685764776f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`bash -n` 通过。脚本已创建。

---

## 报告

### Checkpoint 确认

| 条件 | 路径 | gate_params.pt | lora/ | --gate-type |
|------|------|:-:|:-:|-------------|
| TG v7 s42 | `runs/phase2_tg_s42_v7/epoch_2` | ✓ | ✓ | `threadgate` |
| UG s42 | `runs/phase2_ug_s42/epoch_2` | ✓ | ✓ | `uniform` |
| PCGrad s42 | `checkpoints/tg_v9_pcgrad_s42/epoch_2` | ✓ | ✓ | `threadgate` |
| LoRA-only s42 | `runs/phase2_lora_only_s42/epoch_2` | — | ✓ | `none` |
| SS v8b s42 | `runs/d048_ss_s42/epoch_2` | ✓ | ✓ | `threadgate` |

**路径修正**：任务给的 UG/LO 路径（`checkpoints/ug_s42/`、`checkpoints/lora_only_s42/`）不存在，实际在 `runs/phase2_ug_s42/` 和 `runs/phase2_lora_only_s42/`。

**gate-type 修正**：任务说 UG 用 `threadgate`，但 UG 的 `train_config.json` 明确是 `gate_type: uniform`，已有脚本 `d048_eval_existing_s42_ar_n50.sh` 和 `d048_final_ar_eval.sh` 也用 `uniform`。脚本中已按 `uniform` 设置。

### 脚本结构 (`scripts/unified_ar_n50_eval.sh`)

1. **Checkpoint 验证** — 启动前检查 5 个 checkpoint 完整性
2. **10 轮 AR eval** — 5 条件 × 2 GAR variants（ours + dongre），共 10 次 `eval_attention_steering.py --mode gen`
   - 有 gate 的条件（TG/UG/PCGrad/SS）：`--beta 0 3 5`
   - 无 gate 的条件（LO）：`--beta 0`
3. **Bootstrap 95% CI** — curve[2:] 计算 mid-turn GAR，B=10000
4. **Paired Wilcoxon** — TG vs LO / TG vs UG / SS vs TG / PCGrad vs TG
5. **输出** — 每条件的 JSON 在 `results/unified_ar_n50/{condition}/`，汇总在 `unified_summary_ci.json`

数据源：`data/eval_200/eval_200.json`，`--max-convs 50`，与 `d048_final_ar_eval.sh` 一致。

---
