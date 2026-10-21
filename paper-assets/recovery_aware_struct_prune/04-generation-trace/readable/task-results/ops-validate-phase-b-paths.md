# ops validate phase b paths

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_validate_phase_b_paths_20260516T084330_result.json`
- **Structured JSON:** [`3afcc0d1c399e8303a97.json`](../../sessions/3a/3afcc0d1c399e8303a97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase B 就绪状态报告

| 实验 | 服务器 | 模型路径 | 状态 |
|------|--------|----------|------|
| grpo_rasp_25 | westb-23072 | `sft_rasp_25/model.safetensors` | ✅ 存在 |
| grpo_standard_25 | westb-23072 | `sft_standard_25/checkpoint-1870/model.safetensors` | ✅ 存在 |
| grpo_rasp_qwen_math | westd-11672 | `sft_qwen_math_rasp_20/` | ⏳ SFT 训练中 68% (1899/2805, ETA ~14min) |
| grpo_standard_qwen_math | westd-11672 | `sft_qwen_math_standard_20/` | ⏳ SFT 训练中 66% (1849/2805, ETA ~15min) |

**脚本可用性：**
- `train_grpo_v5.py` — westb ✅ / westd ✅
- `eval_gsm8k.py` — westd ✅

**磁盘空间：**

| 服务器 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| westb-23072 | 250G | 232G | **19G** | 93% |
| westd-11672 | 250G | 225G | 26G | 90% |

### ⚠️ 风险项

**westb-23072 磁盘仅剩 19GB。** GRPO 训练会保存多个 checkpoint（每个 ~6-7GB），当前剩余空间不足以安全运行两组 GRPO 实验。建议在启动 Phase B 前清理 westb 旧文件释放空间，或配置 `save_total_limit=2` 限制 checkpoint 数量。

---
