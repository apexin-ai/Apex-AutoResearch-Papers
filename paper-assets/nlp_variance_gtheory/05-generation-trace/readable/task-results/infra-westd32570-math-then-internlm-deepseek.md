# infra westd32570 math then internlm deepseek

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd32570_math_then_internlm_deepseek_20260521T152933_result.json`
- **Structured JSON:** [`814c020dfb1d79646538.json`](../../sessions/81/814c020dfb1d79646538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部部署完成。

---

**产出汇总：**

### 1. 模型路径（已下载完毕）
- InternLM: `/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2_5-7b-chat` (8 safetensors, ~14.5GB)
- DeepSeek: `/root/autodl-tmp/.hf_cache/deepseek-ai/deepseek-llm-7b-chat` (2 pytorch_model.bin, ~13.5GB)
- model_paths.py HF key: `internlm/internlm2_5-7b-chat`, `deepseek-ai/deepseek-llm-7b-chat`

### 2. 生成的文件
- **Design matrix**: `results/exp002/design_matrix_new_models.csv` (2,880 条件)
- **10 个 shard 文件**: `shard_{internlm,deepseek}_{mmlu,arc,hellaswag,gsm8k,math}.csv` (各 288 条件)
- **`scripts/auto_start_new_models.sh`**: 3 轮调度，4 GPU 并行
  - Round 1: MMLU + ARC (4 parallel)
  - Round 2: HellaSwag + GSM8K (4 parallel)
  - Round 3: MATH (2 parallel)
- **`scripts/math_then_new_models.sh`**: 每 2 分钟检查 MATH 完成状态

### 3. 监控部署
- Monitor PID: **174350** (运行中)
- 日志: `results/exp002/math_then_new_models.log`

### 4. MATH 当前进度 (23:33 CST)
| Model | Lines | Progress |
|-------|-------|----------|
| Llama | 47,800 | 83% |
| Mistral | 46,600 | 81% |
| Qwen | 32,200 | 56% |
| Gemma | 23,000 | 40% |

### 5. 时间预估
- **MATH 全部完成**: ~02:30 CST（Gemma 最慢）
- **InternLM + DeepSeek 全 5 benchmarks**: 基于原始 4 模型运行时间，MC benchmarks (MMLU/ARC/HellaSwag) 约 30-40min/round，GSM8K 约 2h，MATH 约 3h → 新模型全部完成预计 ~08:30-09:00 CST

---
