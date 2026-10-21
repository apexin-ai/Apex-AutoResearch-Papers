# code llama70b script adapt

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama70b-script-adapt_20260517T073247_result.json`
- **Structured JSON:** [`f5c729f1950d014e3f90.json`](../../sessions/f5/f5c729f1950d014e3f90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All scripts validated. Here's the summary:

---

## 产出

### 创建的文件（均在 `/root/schema-dag-extraction/scripts/`）

| 文件 | 用途 |
|------|------|
| `run_d051_count_curves_llama70b.py` | Count curves 实验（FewRel + Few-NERD），支持 LLaMA chat template + TP=2 |
| `run_bcs_controlled_llama70b.py` | BCS-controlled extreme batch 实验，支持多 count_key |
| `run_llama70b_cross_model.sh` | 一键启动所有实验的 shell 脚本 |

### 相比原版的关键修改

1. **Chat template**：自动检测 LLaMA 模型并 `apply_chat_template`（原 `run_d051` 缺失此功能）
2. **tensor_parallel_size=2**：适配 2×RTX PRO 6000
3. **CLI 参数化**：`--model_path`, `--tensor_parallel_size`, `--gpu_mem`, `--max_model_len` 均可配置
4. **模型路径**：默认 `neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8`（如 westd 有本地缓存可通过 `LLAMA70B_MODEL_PATH` 环境变量覆盖）

### 在 westd 上运行

```bash
# 如果模型已下载到本地缓存
export LLAMA70B_MODEL_PATH=/path/to/local/Meta-Llama-3.1-70B-Instruct-FP8

# 一键启动
bash scripts/run_llama70b_cross_model.sh

# 或分步运行
python3 scripts/run_d051_count_curves_llama70b.py --dataset fewrel --seed 42 --counts "8,16,32,64,80"
python3 scripts/run_bcs_controlled_llama70b.py --stage all --count_keys "count_8,count_16"
python3 scripts/run_d051_count_curves_llama70b.py --dataset fewnerd --seed 42
```

### 兼容性注意事项

- **Prompt 格式**：使用通用英文 prompt（非 Qwen 专属），LLaMA chat template 由 vLLM tokenizer 自动处理
- **Structured output**：vLLM 的 JSON constrained decoding 对 LLaMA 3.1 同样适用，无需额外适配
- **FP8**：`neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8` 是原生 FP8 量化权重，vLLM 直接支持，无需额外量化参数
- **VRAM 预估**：70B FP8 ≈ 70GB，2×48GB = 96GB，`gpu_memory_utilization=0.90` 下约用 86GB，留有余量

---
