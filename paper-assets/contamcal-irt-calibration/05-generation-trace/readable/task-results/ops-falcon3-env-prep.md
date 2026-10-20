# ops falcon3 env prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-env-prep_20260522T035733_result.json`
- **Structured JSON:** [`cc043f6f45ec8dd0e4e1.json`](../../sessions/cc/cc043f6f45ec8dd0e4e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ModelScope 下载进行中，约 1-2MB/s，预计 1-2 小时完成。所有信息已收集完毕。

---

## 报告

### 1. GPU 配置
- **1 张 NVIDIA GeForce RTX 4090 D**，24564 MiB (24GB)
- 当前空闲，无 GPU 进程

### 2. 磁盘空间
- `/root/autodl-tmp/`：总 169GB，已用 141GB，**剩余 29GB**
- Falcon3-7B 权重 ~14GB + checkpoint ~2.5GB = ~16.5GB，剩余空间足够

### 3. 模型下载
- HF 下载超时（xethub 代理不稳定），已切换 **ModelScope**
- PID 646342 正在下载，速度 ~1-2MB/s，预计 1-2 小时
- 下载路径：`/root/autodl-tmp/.hf_cache/tiiuae/Falcon3-7B-Base/`

### 4. Falcon3-7B-Base 架构参数

| 参数 | 值 |
|------|-----|
| Architecture | **LlamaForCausalLM** (model_type=llama) |
| Hidden size | 3072 |
| Num layers | 28 |
| Num attention heads | 12 |
| Num KV heads | 4 (GQA) |
| Head dim | 256 |
| Intermediate size | 23040 |
| Vocab size | 131072 |
| Max position embeddings | 32768 |
| torch_dtype | bfloat16 |

### 5. LoRA target modules
Falcon3 使用 LlamaForCausalLM 架构，线性层名称与 Qwen 系列相同：
- `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **与 `train_sft.py` 的 DEFAULT_LORA_CONFIG 完全兼容**，无需 `--lora-targets` 覆盖

### 6. 代码适配问题

**有一个必须修复的问题：chat_template**

`train_sft.py` 第 ~143 行：
```python
if tokenizer.chat_template is None:
    if "llama" in args.model_name.lower():
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE
    else:
        raise ValueError(...)
```

Falcon3-7B-Base 的 tokenizer **没有 chat_template**，且模型名 `tiiuae/Falcon3-7B-Base` 不含 "llama"，会触发 ValueError。

**解决方案**（任选一）：
- **A**: 修改条件为 `if "llama" in args.model_name.lower() or "falcon3" in args.model_name.lower():`，因为 Falcon3 底层就是 Llama 架构，Llama3 chat template 可用
- **B**: 改为检查 `config.model_type == "llama"` 而非模型名字符串匹配（更通用）

**其他兼容点（无问题）**：
- `pad_token`：脚本已处理 `pad_token = eos_token` ✅
- `trust_remote_code=True`：已设置 ✅
- QLoRA / gradient checkpointing：7B bf16 (~14GB) + LoRA 在 24GB 4090 上偏紧，建议使用 `--gradient-checkpointing`；如仍 OOM 可加 `--load-in-4bit` ✅
- `--batch-size 2 --grad-accum 8`（相比默认 bs=4）可进一步降低显存 ✅

---
