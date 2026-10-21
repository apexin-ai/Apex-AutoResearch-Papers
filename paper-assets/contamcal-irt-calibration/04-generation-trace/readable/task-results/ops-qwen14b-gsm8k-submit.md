# ops qwen14b gsm8k submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-gsm8k-submit_20260520T052859_result.json`
- **Structured JSON:** [`42eaa4fb48d74d7e4a10.json`](../../sessions/42/42eaa4fb48d74d7e4a10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**阻断性问题：**

1. **服务器只有 1 块 GPU（cuda:0）**，nvidia-smi 只返回 index 0，且当前 98% 利用率、21.3GB/24.5GB 显存占用。**不存在 cuda:1。**

2. **Qwen2.5-14B_d100_s42 checkpoint 不存在。** checkpoints 目录中 14B 只有 d000_s42 和 d005_s42。没有 d100 相关目录。

3. **脚本 `run_gsm8k_qwen14b_s42.sh` 不存在。** `scripts/gsm8k_s42/` 是空目录。

4. **GPU 0 被占用（98% util, 21.3GB）。** 无法提交新任务。

### 已确认的部分

| 检查项 | 结果 |
|--------|------|
| d000_s42 adapter_model.safetensors | 275MB ✓ |
| d000_s42 lora_alpha | 32 ✓ |
| d100_s42 checkpoint | **不存在** |
| run_gsm8k_qwen14b_s42.sh | **不存在** |
| cuda:1 | **不存在**（仅 1 块 GPU） |
| cuda:0 | 被占用（98%, 21.3GB） |

需要确认：
- d100 s42 训练是否完成？如果是 s123 而非 s42，checkpoint 路径是什么？
- eval 应在哪台服务器/哪块 GPU 执行？
- 脚本是否需要新建？

---
