# code compounding sweep 5models

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compounding_sweep_5models_20260516T024122_result.json`
- **Structured JSON:** [`c8936ef6c16967fa09d6.json`](../../sessions/c8/c8936ef6c16967fa09d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个脚本全部创建完毕，语法检查通过。

| 脚本 | 模型 | KV heads | 注意力 patching | Profile 文件 |
|------|------|----------|----------------|-------------|
| `run_yi_compounding_sweep.py` | Yi-1.5-9B | 256 (32×8) | `eval_ppl.patch_attention` | `yi15_hires_bf16_2bitonly_profiles.json` |
| `run_gemma2_compounding_sweep.py` | Gemma-2-9B | 336 (42×8) | `patch_attention_gemma2` + BOS prepend | `gemma2_hires_bf16_2bitonly_profiles.json` |
| `run_codellama_compounding_sweep.py` | CodeLlama-7B | 1024 (32×32 MHA) | `eval_ppl.patch_attention` | `artifacts/codellama_profiles_hires.json` |
| `run_phi3_compounding_sweep.py` | Phi-3-medium-14B | 400 (40×10) | `eval_ppl.patch_attention` | `artifacts/phi3_medium_profiles_hires.json` |
| `run_internlm2_compounding_sweep.py` | InternLM2-7B | 256 (32×8) | 内嵌 `patch_attention_internlm2` (fused wqkv) | `artifacts/internlm2_profiles_hires.json` |

每个脚本都支持 `--gpu` 参数，k 值范围 `[0,2,4,8,16,32,64,128,256]`（超过 total heads 的自动跳过），输出 JSON 到 `artifacts/`。Gemma-2 的 BOS prepend 和 InternLM2 的 fused wqkv splitting 已做对应适配。

---
