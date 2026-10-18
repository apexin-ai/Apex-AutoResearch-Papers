# code prep longctx eval scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_longctx_eval_scripts_20260516T023901_result.json`
- **Structured JSON:** [`65c28481aa90aa06b391.json`](../../sessions/65/65c28481aa90aa06b391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建：

**`run_llama8b_8k_eval.py`** — Llama-3.1-8B 8K context eval
- 模型路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B`
- Profile 文件: `llama_hires_bf16_2bitonly_profiles.json` + `llama_profiling_results.json`
- 输出: `artifacts/llama8b_8k_eval_results.json`

**`run_mistral7b_8k_eval.py`** — Mistral-7B-v0.3 8K context eval
- 模型路径: `/root/autodl-tmp/models/Mistral-7B-v0.3`
- Profile 文件: `mistral_hires_bf16_2bitonly_profiles.json` + `mistral_profiling_results.json`
- 输出: `artifacts/mistral7b_8k_eval_results.json`

**相比模板的关键改动：**
1. 添加 `--gpu` 参数（`argparse`），用法: `python run_llama8b_8k_eval.py --gpu 1`
2. 使用 merged profiles（hires 2-bit + standard 4/8-bit），与项目中 Llama/Mistral 已有脚本一致
3. `max_2bit=2`（Llama/Mistral 惯例，Qwen 用 `max_2bit=8`）
4. 去掉了 Qwen 脚本中硬编码的 `results_2k_reference`，因为两个模型的 2K 参考值不同
5. 记录 `heads_2bit` 和 `heads_8bit` 列表，便于分析分配细节

---
