# infra research phase prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_research-phase-prep_20260514T140739_result.json`
- **Structured JSON:** [`2da0b10572228c84abd4.json`](../../sessions/2d/2da0b10572228c84abd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇报

### 1. 模型下载状态

| 模型 | 来源 | 路径 | model.safetensors | 状态 |
|------|------|------|-------------------|------|
| OLMo-1B | `allenai/OLMo-1B-hf` (ModelScope CDN) | `/root/autodl-tmp/models/olmo-1b/` | 4.4GB (float32) | 完整 (8 文件) |
| GPT-2 XL | `openai-community/gpt2-xl` (hf-mirror wget) | `/root/autodl-tmp/models/gpt2-xl/` | 6.0GB (float32) | 完整 (8 文件, safetensors header 验证通过) |

注：使用 `allenai/OLMo-1B-hf` 而非 `allenai/OLMo-1B`，因为后者需要 `hf_olmo` 自定义代码，前者是原生 transformers 格式（model_type=`olmo`）。

### 2. LoRA target_modules

| 模型 | model_type | 参数量 | vocab_size | BOS/EOS/PAD | Attention 模块类型 | LoRA targets |
|------|-----------|--------|-----------|-------------|------------------|-------------|
| OLMo-1B | `olmo` | 1.18B | 50280 | None / 50279 / 1 | `nn.Linear` | `q_proj`, `k_proj`, `v_proj`, `o_proj` |
| GPT-2 XL | `gpt2` | 1.56B | 50257 | 50256 / 50256 / None | `Conv1D` | `c_attn`, `c_proj` |

Pipeline 脚本中 OLMo 选用 `q_proj,v_proj`（与 Pythia 的 q/v-only 策略一致），GPT-2 XL 选用 `c_attn,c_proj`。

### 3. 脚本适配清单

**新增文件（服务器上）：**
- `scripts/run_pipeline_olmo.sh` — MODEL_PATH=/root/autodl-tmp/models/olmo-1b, TARGET_MODULES=q_proj,v_proj, 数据→data/olmo/, checkpoints→checkpoints/olmo/
- `scripts/run_pipeline_gpt2xl.sh` — MODEL_PATH=/root/autodl-tmp/models/gpt2-xl, TARGET_MODULES=c_attn,c_proj, 数据→data/gpt2xl/, checkpoints→checkpoints/gpt2xl/

**修改文件（服务器上）：**
- `scripts/generate_next_depth.py` — 新增 `--top_k` (default=50), `--decoding_strategy` (choices: nucleus/topk/temp_only, default=nucleus)；generation 逻辑按策略动态构建 gen_kwargs

**lora_finetune.py** — 服务器版本已有 `--target_modules` 参数（逗号分隔），无需修改。

### 4. Dry-run 验证

- `python scripts/generate_next_depth.py --help` — 显示 `--top_k`, `--decoding_strategy {nucleus,topk,temp_only}` 参数
- `python scripts/lora_finetune.py --help` — 显示 `--target_modules` 参数
- 两个模型均可通过 `AutoModelForCausalLM.from_pretrained` 在 CPU 上成功加载

---
