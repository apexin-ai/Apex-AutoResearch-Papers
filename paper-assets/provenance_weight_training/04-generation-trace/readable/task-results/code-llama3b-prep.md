# code llama3b prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama3b-prep_20260516T083741_result.json`
- **Structured JSON:** [`edc4acf209fcb8249dfa.json`](../../sessions/ed/edc4acf209fcb8249dfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型配置正确：LlamaForCausalLM, 3072 hidden, 28 layers, 128K vocab。

## 总结

### 1. 模型下载：成功
- 路径：`models/meta-llama/Llama-3.2-3B/`
- 来源：`unsloth/Llama-3.2-3B` via ModelScope（meta-llama 需要 HF token，unsloth 无门禁）
- 大小：~6.4GB（2 个 safetensors + tokenizer）
- 架构：LlamaForCausalLM, hidden=3072, 28 layers, vocab=128256

### 2. q-score 复用：确认可用
- `data/scored_data.jsonl`：371,499 行，q_score 字段存在，值在 [0,1] 范围
- TF-IDF+LR detector 基于文本特征，不依赖生成模型，直接复用

### 3. 脚本路径
| 脚本 | 路径 |
|------|------|
| Uniform | `scripts/run_llama3b_uniform_seed42.sh` |
| Adaptive τ=0.8 | `scripts/run_llama3b_adaptive_seed42.sh` |
| Adaptive τ=0.9 | `scripts/run_llama3b_adaptive_tau09_seed42.sh` |

所有脚本相对 Qwen 模板的改动：`--model_name models/meta-llama/Llama-3.2-3B` + `--gradient_checkpointing`，batch_size 保持 4（96GB GPU 足够容纳 3B bf16 训练 ≈40GB）。

### 4. Dry-run：跳过
4 张 GPU 全在跑实验（3 个训练 + 1 个 eval），无空闲 GPU。参数解析验证通过（`--help` 正常返回）。

### 5. ρ=0.2 数据生成
- 脚本：`scripts/prepare_rho02_data.py` + `scripts/run_prepare_rho02.sh`
- **注意**：人类数据仅 164,889 条，ρ=0.2 需要 80% 人类数据，总行数调整为 206,111（而非 371,499）。206K 行 × 2048 tokens ≈ 422M tokens，覆盖 200M tokens 训练需求。
- 运行命令：`bash scripts/run_prepare_rho02.sh`
- τ=0.9 脚本使用 `data/scored_data_rho02.jsonl` + `--contamination_ratio 0.2`

---
