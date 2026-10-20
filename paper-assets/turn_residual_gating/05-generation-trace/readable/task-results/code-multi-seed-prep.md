# code multi seed prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_prep_20260520T183721_result.json`
- **Structured JSON:** [`37ce06f0b02867a9aaed.json`](../../sessions/37/37ce06f0b02867a9aaed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已就绪。汇报：

### 脚本状态：就绪 ✓

**修复了两个问题：**
1. 两个脚本补加了 `cd /root/turn_residual_gating`（原脚本用相对路径但没有 cd）
2. `launch_lora_s123.sh` 的 `--lambda-gate-div` 从 1.0 → 0.0，`--min-gate-std` 从 0.05 → 0.0，与原始 LoRA-only s42 配置一致

**参数对比确认：**

| 参数 | TG s123 vs TG s42 原始 | LoRA s123 vs LoRA s42 原始 |
|------|----------------------|--------------------------|
| gate-type | threadgate ✓ | none ✓ |
| gar-loss-mode | mse_target ✓ | mse_target ✓ |
| gar-target | 0.5 ✓ | 0.5 ✓ |
| lambda-gar | 1.0 ✓ | 1.0 ✓ |
| lambda-gate-div | 1.0 ✓ | 0.0 ✓ (已修复) |
| min-gate-std | 0.05 ✓ | 0.0 ✓ (已修复) |
| init-bias | 1.5 ✓ | 1.5 ✓ |
| gate-lr-multiplier | 10 ✓ | 10 ✓ |
| max-seq-len | 2048 ✓ | 2048 ✓ |
| epochs | 3 ✓ | 3 ✓ |
| seed | 123 ✓ | 123 ✓ |

**输出路径**：`runs/phase2_tg_s123_v7` 和 `runs/phase2_lora_only_s123`，均不存在，不会覆盖现有 checkpoint。

**预估 GPU 时间**：原始 v7 TG 耗时 ~5.9h，LoRA-only ~5.7h，合计 ~12h（串行）。

---
