# code prep llama lora only

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_llama_lora_only_20260521T194426_result.json`
- **Structured JSON:** [`31ea1a0a3123d9ad0634.json`](../../sessions/31/31ea1a0a3123d9ad0634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 占用 66GB/97GB (99%)，dry-run 有 OOM 风险，跳过 dry-run。

---

## 产出汇总

**脚本路径**: `/root/turn_residual_gating/scripts/launch_llama_lora_only_s42.sh`

**启动命令**: `bash scripts/launch_llama_lora_only_s42.sh 2>&1 | tee logs/llama_lora_only_s42.log`

**关键参数对比**:

| 参数 | Llama TG (s42) | Llama LoRA-only (s42) | Qwen LoRA-only (s42) |
|------|---------------|-----------------------|----------------------|
| gate_type | threadgate | **none** | none |
| model | Llama-3.1-8B | Llama-3.1-8B | Qwen-2.5-7B |
| lambda_gate_div | 1.0 | **0.0** | 0.0 |
| min_gate_std | 0.05 | **0.0** | 0.0 |
| lr | 2e-4 | 2e-4 | 2e-4 |
| gar_target | 0.5 | 0.5 | 0.5 |
| lambda_gar | 1.0 | 1.0 | 1.0 |
| init_bias | 1.5 | 1.5 | 1.5 |
| epochs | 3 | 3 | 3 |
| seed | 42 | 42 | 42 |

**预估训练时间**: ~6 小时（Llama TG 用了 7.3h，去掉 gate 计算开销估算；Qwen LoRA-only 用了 5.7h，Llama 8B 稍大）

**dry-run**: 跳过——GPU 当前被 v7_tg_s123 占满（66GB/97GB, 99%）。等 v7 训完后可用 `--max-steps 2` 验证。

**注意**: 已有 `scripts/launch_llama_lora.sh` 内容基本相同但 `lambda_gate_div` 和 `min_gate_std` 未归零，输出目录为 `phase2_llama_lora_s42`。新脚本更规范，建议用新脚本。

---
