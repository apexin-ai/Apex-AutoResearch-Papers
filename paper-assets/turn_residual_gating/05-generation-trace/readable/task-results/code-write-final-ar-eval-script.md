# code write final ar eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write_final_ar_eval_script_20260522T233302_result.json`
- **Structured JSON:** [`5dc4276bcf4e75dcbe9d.json`](../../sessions/5d/5dc4276bcf4e75dcbe9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建：`/root/turn_residual_gating/scripts/d048_final_ar_eval.sh` (241行, 7475字节, 可执行)。

**路径验证结果**：

| 条件 | Checkpoint 路径 | lora/ | gate_params.pt | --gate-type |
|------|----------------|-------|----------------|-------------|
| Base | 无 (不传 --checkpoint) | - | - | `none` |
| TG | `runs/phase2_tg_s42_v7` | ✓ | ✓ | `threadgate` |
| UG | `runs/phase2_ug_s42` | ✓ | ✓ | `uniform` |
| LO | `runs/phase2_lora_only_s42` | ✓ | 无 (正确) | `none` |
| PCGrad | `checkpoints/tg_v9_pcgrad_s42` | ✓ | ✓ | `threadgate` |
| SS | `runs/d048_ss_s42` | ✓ | ✓ | `threadgate` |

**Base model 支持方式**：`eval_attention_steering.py` 第86行先检查 `if checkpoint_dir:` 再加载 LoRA，第95行 `if gate_type in ("none", "baseline") or not checkpoint_dir:` 跳过 gate 加载。不传 `--checkpoint` + `--gate-type none` 即可评估裸基模型。

**脚本结构**：6个条件顺序执行 → 内联 Python 计算 bootstrap 95% CI (`curve[2:]`, B=10000) + paired Wilcoxon (4组对比) → 结果同时打印到 stdout 并保存到 `results/d048_final_ar/d048_summary_ci_wilcoxon.json`。

---
