# prep llama3 download and audit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_llama3-download-and-audit_20260519T025256_result.json`
- **Structured JSON:** [`f6dfe5b4cb07f3b20613.json`](../../sessions/f6/f6dfe5b4cb07f3b20613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成，以下是完整报告。

---

## 1. 两台服务器模型清单

| 服务器 | 模型目录 |
|--------|----------|
| westd-34887 | llama-3.1-8b (15G), mistral-7b, openvla-7b-finetuned, qwen2.5-14b |
| westd-41718 | llama-3.1-8b, qwen2.5-14b |

**LLaMA-3-8B 不在任何一台服务器上，需要下载。**

## 2. 代码兼容性评估

### 核心发现：零代码修改即可支持 LLaMA-3-8B

**predictor.py** — 所有维度从 `model.config` 动态读取：
- `config.hidden_size` → down 投影输入
- `config.intermediate_size` → up 投影输出
- `config.num_hidden_layers` → predictor 数量
- `_patch_mlps` 通过 `model.model.layers[i].mlp.{gate_proj,up_proj,down_proj,act_fn}` 打 patch，这是标准 LlamaForCausalLM 结构，3-8B 和 3.1-8B 完全相同

**核心脚本兼容性：**

| 文件 | 模型路径方式 | 需要修改？ |
|------|-------------|-----------|
| `train.py` | `--model_name_or_path` CLI arg | **否** — 传参即可 |
| `train_bce_kl_targets.py` | `--model_name_or_path` CLI arg | **否** |
| `benchmark_eval.py` | `--model_name_or_path` CLI arg | **否** |
| `evaluate.py` | `--model_name_or_path` CLI arg | **否** |
| `predictor.py` | 维度从 model.config 推断 | **否** |
| `data_utils.py` | 无模型依赖 | **否** |

**辅助脚本**（约15个 debug/diag 文件）硬编码了 `MODEL_PATH = "/root/autodl-tmp/models/llama-3.1-8b"`，但这些不是核心实验流水线，暂不需要改。

## 3. 架构对比表

| 参数 | LLaMA-3-8B | LLaMA-3.1-8B | Mistral-7B |
|------|-----------|-------------|-----------|
| hidden_size | 4096 | 4096 | 4096 |
| intermediate_size | 14336 | 14336 | 14336 |
| num_attention_heads | 32 | 32 | 32 |
| num_key_value_heads | 8 | 8 | 8 |
| num_hidden_layers | 32 | 32 | 32 |
| vocab_size | 128256 | 128256 | 32000 |
| FFN 结构 | SwiGLU (silu) | SwiGLU (silu) | SwiGLU (silu) |
| max_position_embeddings | 8192 | 131072 | 32768 |
| rope_theta | 500000 | 500000 | 10000 |
| rope_scaling | 无 | llama3 extended (factor=8) | 无 |

**关键结论**：LLaMA-3-8B 与 3.1-8B 的 FFN 维度完全相同，predictor 参数量不变（2.37M/layer, 75.9M total）。差异仅在 RoPE 配置和上下文长度，对 sparsity predictor 训练/推理无影响。

## 4. 下一步行动

**需要下载 LLaMA-3-8B 到两台服务器**。模型约 15GB（与 3.1-8B 相同）。

下载命令：
```bash
export HF_ENDPOINT=https://hf-mirror.com
export HF_HOME=/root/autodl-tmp/.hf_cache
huggingface-cli download meta-llama/Meta-Llama-3-8B \
    --local-dir /root/autodl-tmp/models/Meta-Llama-3-8B
```

注意：meta-llama 模型需要 HF 账号授权（Meta license agreement）。如果遇到 401/403 需要配置 HF token。

## 5. GPU-hours 估计（全套 LLaMA-3 实验）

| 实验 | 预计时间 | GPU 数 |
|------|---------|--------|
| KL training (1000 steps) | ~3-4h | 1 |
| BCE training (1000 steps) | ~2-3h | 1 |
| C1 ablation (BCE+KL targets) | ~2-3h | 1 |
| Dense + baseline eval (PPL + 5 tasks) | ~2-3h | 1 |
| Predictor eval (per-token + TEAL) | ~3-4h | 1 |
| **总计** | **~12-17 GPU-hours** | 可双服务器并行缩短到 ~8h |

是否现在启动下载？

---
