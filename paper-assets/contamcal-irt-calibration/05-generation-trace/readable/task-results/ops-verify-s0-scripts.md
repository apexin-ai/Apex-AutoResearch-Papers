# ops verify s0 scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-s0-scripts_20260519T232805_result.json`
- **Structured JSON:** [`1c8734b8b9f2b8ae5e5c.json`](../../sessions/1c/1c8734b8b9f2b8ae5e5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## s0 训练脚本验证结果

全部 4 个脚本就绪，覆盖 5 个 model family：

| 脚本 | Family | CUDA | seed | lora_alpha | lr | batch×accum | 状态 |
|------|--------|------|------|------------|-----|-------------|------|
| `sft_phi4_s0_sweep.sh` | Phi-4 | **0** | 0 | 32 | 5e-5 | 1×16 | ✅ |
| `sft_qwen14b_s0_sweep.sh` | Qwen2.5-14B | **1** | 0 | 32 | 5e-5 | 1×16 | ✅ |
| `sft_qwen7b_olmo2_s0_sweep.sh` | Qwen2.5-7B + OLMo-2-7B | **2** | 0 | 32 | 5e-5 | 2×8 | ✅ |
| `sft_gemma2_s0_sweep.sh` | gemma-2-9b | **3** | 0 | 32 | 5e-5 | 2×8 | ✅ |

**关键配置全部正确：**
- seed=0 ✅
- lora_alpha=32 ✅（符合 C006）
- CUDA_VISIBLE_DEVICES 显式设置 ✅（符合 C004）
- 数据路径统一 `/root/autodl-tmp/sft_data/sft_dosage_{d}.jsonl` ✅
- 输出命名 `{model}_d{dosage}_s0` ✅
- 离线模式 `HF_*_OFFLINE=1` ✅
- 已训完跳过逻辑（检查 `train_config.json`）✅

**GPU 分配：** Phi-4→GPU0, Qwen14B→GPU1, Qwen7B+OLMo2→GPU2, Gemma2→GPU3。每个脚本固定一张卡，与 s123 阶段的分配一致。

**无缺失 family。** 5 个 family 分布在 4 个脚本中（Qwen7B 和 OLMo2 合并在一个脚本顺序执行），4/4 脚本就绪。

---
