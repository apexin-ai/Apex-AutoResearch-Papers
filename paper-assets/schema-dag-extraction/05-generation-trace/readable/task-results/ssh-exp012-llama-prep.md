# ssh exp012 llama prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012-llama-prep_20260515T082428_result.json`
- **Structured JSON:** [`89d3f223ac7f2347f1af.json`](../../sessions/89/89d3f223ac7f2347f1af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No `.incomplete` files — download was interrupted, not active. Here's the full report:

---

## exp-012 兼容性报告

### 1. LLaMA 下载状态：**不完整**
- 已下载：13/15 safetensors 分片
- **缺失**：`model-00007-of-00015.safetensors`、`model-00015-of-00015.safetensors`
- config.json / tokenizer.json / tokenizer_config.json / hf_quant_config.json 均已就位
- 无活跃下载进程，需手动恢复

### 2. 代码兼容性：**完全兼容，无需改代码**

| 检查项 | 结果 |
|--------|------|
| model_path 传递 | `run_experiment.py` → `run_extraction()` → `vLLM LLM(model=...)` — 纯参数传递，无 hardcode |
| Qwen3-specific 逻辑 | 无。"Qwen3" 仅出现在注释和 help text 中，无条件分支 |
| vLLM 初始化 | `LLM(model=..., dtype="bfloat16", gpu_memory_utilization=0.95, enforce_eager=True, max_model_len=4096, trust_remote_code=True)` — 模型无关 |
| FP8 量化 | `hf_quant_config.json` 使用 nvidia modelopt FP8 格式，vLLM 0.20.2 自动检测，无需额外 `--quantization` 参数 |
| tensor_parallel | 代码默认 tp=1。FP8 70B ≈ 70GB，98GB GPU 可 fit（剩余 ~28GB 给 KV cache） |
| chat template | 代码用 `llm.generate(prompts)` 传原始文本，不走 chat template。LLaMA 和 Qwen3 行为一致 |
| prompt 格式 | 纯英文指令文本，无模型特定标记 |
| 输出解析 | `guided_json` 约束解码，模型无关 |
| compute_type_embeddings.py | 使用 `AutoModelForCausalLM` + `AutoTokenizer`，完全模型无关 |

### 3. Decision Point：BCS embeddings

根据 D010 发现，extraction model 的 embeddings 与 BCS-F1 相关性更强。两个选项：

- **Option A（快速）**：复用 Qwen3 embeddings (`artifacts/type_embeddings.pt` + `artifacts/sim_matrix.pt`)。BCS 值不反映 LLaMA 的类型混淆模式，但可以先跑 exp1 验证 pipeline，BCS correlation 分析后补。
- **Option B（严谨）**：先用 LLaMA 计算 Few-NERD embeddings。需要 GPU（当前被 exp-008 占用）。

**建议**：先用 Option A 跑 exp1+exp2，同时生成 LLaMA embeddings，之后再做 BCS reanalysis。exp1 的 count baseline 不依赖 BCS 分组，exp2 的 low/high BCS 分组虽基于 Qwen3 embeddings，但结果仍有 cross-model 对比价值。

### 4. 恢复下载命令

```bash
# 先恢复下载缺失分片
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

huggingface-cli download neuralmagic/Llama-3.3-70B-Instruct-FP8-dynamic \
  --local-dir /root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/ \
  --resume-download
```

### 5. Launch 命令草案

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
COMMON="--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path $MODEL --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp012"

# exp1: Count Baseline
echo "===== [$(date)] exp-012 exp1 ====="
python3 src/run_experiment.py --mode exp1 $COMMON

# exp2: Confusability Controlled
echo "===== [$(date)] exp-012 exp2 ====="
python3 src/run_experiment.py --mode exp2 $COMMON

echo "===== [$(date)] exp-012 done ====="
```

### 6. 需要 GPU 后执行（LLaMA embeddings）

```bash
python3 src/compute_type_embeddings.py \
  --model_path /root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/ \
  --types_file configs/few_nerd_types.json \
  --output_path artifacts/llama70b_fewnerd_embeddings.pt
```

### 下一步
1. 恢复 LLaMA 下载（缺 2 个分片）
2. 等 exp-008 释放 GPU
3. 可选：先算 LLaMA embeddings，再跑 exp-012；或用 Qwen3 embeddings 先跑

---
