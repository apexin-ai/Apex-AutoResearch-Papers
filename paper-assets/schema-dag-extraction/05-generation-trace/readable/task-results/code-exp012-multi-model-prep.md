# code exp012 multi model prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012-multi-model-prep_20260515T131112_result.json`
- **Structured JSON:** [`258b910ffafa48df727c.json`](../../sessions/25/258b910ffafa48df727c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改验证通过。

---

## 产出总结

### 模型选择：LLaMA-3.3-70B-Instruct-FP8

| 维度 | 详情 |
|------|------|
| 模型 | `meta-llama/Llama-3.3-70B-Instruct` (FP8, modelopt quantized) |
| 选择理由 | (a) 不同模型家族（Meta LLaMA vs Alibaba Qwen），满足差异化验证要求；(b) 已下载在服务器 68GB/15 shards；(c) 指令遵循能力与 Qwen2.5-72B 基准持平；(d) Qwen3-72B 未发布，不存在该选项 |
| FP8 方案 | W8A8 FP8 + FP8 KV cache（`hf_quant_config.json` 确认），vLLM 原生支持 |
| VRAM 预估 | ~68GB 模型权重 + KV cache，98GB VRAM 充裕（`gpu_memory_utilization=0.90` 留约 10GB headroom） |
| vLLM 兼容 | `LlamaForCausalLM` 架构，vLLM 一等公民支持，有官方 [Quick Start Recipe](https://docs.vllm.ai/projects/recipes/en/latest/Llama/Llama3.3-70B.html) |

### 代码修改

**`src/run_experiment.py`**：
- 新增 `--model_name` 参数（默认从 model_path 推导）
- 新增 `--gpu_memory_utilization` 参数（默认 0.95）
- 输出文件名包含 model_name（`eval_fewnerd_exp1_llama-3.3-70b-fp8.json`）
- `gpu_memory_utilization` 透传至 `run_extraction()`
- Help text 泛化（移除 Qwen3 硬引用）

**`src/run_extraction.py`**：
- `run_extraction()` 新增 `gpu_memory_utilization` 参数
- `LLM()` 初始化使用参数化 `gpu_memory_utilization`
- Docstring 泛化

**`scripts/run_exp012_llama.sh`**：
- 添加 `MODEL_NAME=llama-3.3-70b-fp8` 和 `--model_name` 传参
- `gpu_memory_utilization=0.90`（70B 模型留更多 headroom）

### 运行方式

```bash
# 在服务器上
bash scripts/run_exp012_llama.sh
```

输出文件将在 `artifacts/exp012/` 下，以 `*_llama-3.3-70b-fp8.json` 命名，与 Qwen3-32B 结果可直接对比。

---
