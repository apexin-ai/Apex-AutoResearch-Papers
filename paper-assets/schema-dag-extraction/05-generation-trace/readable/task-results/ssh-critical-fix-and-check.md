# ssh critical fix and check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_critical-fix-and-check_20260515T170417_result.json`
- **Structured JSON:** [`1f76dd80eaa26a44829b.json`](../../sessions/1f/1f76dd80eaa26a44829b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### run_experiment.py 修改
- **不需要修改。** `run_experiment.py` 不直接调用 `llm.generate()`（grep 确认无匹配）
- 它通过 `from run_extraction import run_extraction` 委托给 `run_extraction.py`

### run_extraction.py
- **已包含 chat template 逻辑，不需要修改。**
- 第 220 行：`_needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])`
- 第 277 行：在 `llm.generate()` (第 288 行) 前对 prompts 做 `apply_chat_template`
- LLaMA 模型会自动触发 chat template 包装

### fewrel_40rel_r3 状态
- **PID 300803: DEAD**（进程不存在）
- **GPU: 0% utilization, 0 MiB / 97887 MiB** — 无任何 GPU 进程
- **日志**: `=== ALL DONE === EXIT_CODE=0`
- **artifacts/fewrel_40rel/**: 只有 `batch_config_exp1.json`, `preprocess_exp1.json`, `relation_sim_matrix.pt` — **无 predictions 文件**
- **结论: 已完成，但 fewrel_40rel 目录下没有 prediction 输出文件**（可能输出到了其他路径，或只完成了预处理阶段）

### exp012 启动命令
- 脚本: `scripts/run_exp012_llama8b.sh`
- 模型: `/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- **exp012 fewnerd 已经有结果了**: `artifacts/exp012/predictions_fewnerd_exp{1,2}_llama-3.1-8b-instruct.json`
- 完整命令:
```bash
bash /root/schema-dag-extraction/scripts/run_exp012_llama8b.sh
```
等价于分步执行:
```bash
python3 src/run_experiment.py --mode exp1 --dataset fewnerd --prompt_version v2 \
  --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt \
  --sim_matrix_path artifacts/sim_matrix.pt \
  --model_path /root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct \
  --model_name llama-3.1-8b-instruct --max_samples 1000 --max_model_len 4096 \
  --gpu_memory_utilization 0.90 --output_dir artifacts/exp012

python3 src/run_experiment.py --mode exp2 [同上参数]
```

**关键发现**: chat template 代码已经在 `run_extraction.py` 中实现，且对 llama 模型名自动启用。无需任何代码修改即可运行 exp012。

---
