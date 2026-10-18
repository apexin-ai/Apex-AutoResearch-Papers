# code prep cross arch scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_cross_arch_scripts_20260514T012405_result.json`
- **Structured JSON:** [`dbbdd0e349cae2560c0b.json`](../../sessions/db/dbbdd0e349cae2560c0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 修改的文件

**eval_ppl.py** — 1 处关键改动：
- 删除 `from transformers.models.qwen2.modeling_qwen2 import apply_rotary_pos_emb` 硬编码 import
- 新增 `_get_rotary_fn(model)` 函数，根据 `model.config.model_type`（qwen2/llama/mistral）动态 import 对应的 `apply_rotary_pos_emb`
- `patch_attention` 中调用 `_get_rotary_fn` 获取 RoPE 函数，通过闭包默认参数传入 `make_forward`

### 新增的文件

**run_llama_pipeline.py** 和 **run_mistral_pipeline.py** — 结构相同，4 phase pipeline：
1. **Profile**: `FullBitwidthProfiler` 在 {2,4,8}-bit 上 profiling，结果单独保存到 `{model}_profiling_results.json`
2. **Solve**: `enforce_monotonicity` → `solve_mckp_constrained(budget=0.25, max_2bit=8, l0_exclude_2bit=True)` + uniform 4-bit baseline
3. **Eval**: WikiText-2 PPL 三组（baseline / MCKP / uniform）
4. **Summary**: 打印 table + bit distribution + L0 allocation，完整结果保存到 `{model}_results.json`

支持 `--dry-run` 只打印 config 不跑 GPU。

### 兼容性确认
- `apply_rotary_pos_emb` 动态 import 对 qwen2/llama/mistral 三种 model_type 均验证通过
- `orig_attn.scaling` 在 transformers 4.57.6 的 Llama/Mistral attention 中均存在
- `model.model.layers[i].self_attn.{q,k,v,o}_proj` 结构三种架构一致
- profiler 的 `num_hidden_layers`/`num_key_value_heads` 从 config 自动读取，无需手动设
- solver.py 未修改

---
