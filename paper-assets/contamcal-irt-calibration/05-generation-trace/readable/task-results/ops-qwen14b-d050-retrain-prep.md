# ops qwen14b d050 retrain prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-d050-retrain-prep_20260520T221003_result.json`
- **Structured JSON:** [`5455cc744963d7b6d9b3.json`](../../sessions/54/5455cc744963d7b6d9b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前进度：**

1. **Gemma-2 MMLU eval (cuda:1, PID 437235)**：仍在运行，进度 64% (9053/14042)，~20 it/s，预计 ~4 分钟后完成
2. **Qwen-14B d050_s0 adapter 状态**：已确认为空（目录 `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0/lora_adapter/` 存在但无任何文件）
3. **重训脚本已创建**：`/root/contamcal-irt-calibration/scripts/seed0/retrain_qwen14b_d050_s0.sh`
   - CUDA_VISIBLE_DEVICES=1
   - lora-r=16, lora-alpha=32, lr=5e-5, batch-size=1, grad-accum=16
   - gradient-checkpointing 已启用
   - 训练后自动验证 adapter 存在性

4 分钟后我会再次检查 eval 是否完成，完成后立即启动重训。

---
