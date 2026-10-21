# code review rsft pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_review_rsft_pipeline_20260515T025458_result.json`
- **Structured JSON:** [`b27c45666aa65f05c7be.json`](../../sessions/b2/b27c45666aa65f05c7be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是代码审查报告：

---

## RSFT 下一阶段代码审查报告

### 1. 数据流对齐状态

| 阶段 | 输出字段 | 下游读取 | 状态 |
|------|---------|---------|------|
| **generate → score_filter** | `doc_id, generation_idx, prompt, output, raw_text, parsed_triples, format_ok, truncated, gold_triples, sents` | `doc_id, generation_idx, parsed_triples, format_ok, gold_triples, sents, output, prompt` | ✅ 完全对齐 |
| **score_filter → trainer** | `input, output, ced_score, doc_id, generation_idx, format_reward, f1_reward, combined_score` | `s["input"], s["output"], s.get("ced_score", 1.0)` | ✅ 完全对齐 |

### 2. rsft_trainer.py 关键超参数

| 参数 | 默认值 | 备注 |
|------|--------|------|
| `--quantize` | **False** (`store_true`) | ✅ 满足禁止 quantize 约束 |
| `--lora_rank` | 64 | ✅ |
| `--lora_alpha` | 128 | ✅ |
| `--lora_dropout` | 0.05 | |
| `--bf16` | **True** (`store_true, default=True`) | ✅ 默认开启 |
| `--learning_rate` | 2e-5 | |
| `--num_epochs` | 3 | |
| `--per_device_batch_size` | 4 | |
| `--gradient_accumulation_steps` | 4 | effective batch = 4×4×4GPU = 64 |
| `--max_length` | 2048 | |
| `--weighted_sampling` | False (`store_true`) | 可选用 CED score 做加权采样 |
| `--deepspeed` | None | |
| target_modules | q/k/v/o/gate/up/down_proj | 全覆盖 |

### 3. 发现的问题

#### 问题 A: NLI 模型路径（中等风险）
`rsft_score_filter.py` 的 `--nli_model_path` 默认值是 `"cross-encoder/nli-deberta-v3-base"`（HF hub ID）。模型已在 HF cache 中 (`/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/`)，但**必须确保环境变量 `HF_HOME=/root/autodl-tmp/.hf_cache` 已设置**，否则会尝试重新下载。

**建议**：运行前执行 `export HF_HOME=/root/autodl-tmp/.hf_cache`，或显式传 `--nli_model_path /root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/&lt;hash>/`。

#### 问题 B: 无需手动合并 shard（信息）
`rsft_score_filter.py` 的 `load_generations()` 函数**已内置 shard 合并逻辑**：自动扫描 `input_dir/shard_*/generations.jsonl` + 根目录 `generations.jsonl`，按 `(doc_id, generation_idx)` 去重，shard 优先覆盖 root。**不需要先手动 merge。**

`merge_shards.py` 是独立工具，仅在需要单独的 merged 文件时使用。

#### 问题 C: Root generations.jsonl 使用旧生成配置
根据 `merge_shards.py` 注释：root `generations.jsonl` (2416行) 用旧参数 `top_k=20, T=0.6` 生成，shard 是修正后的 `top_k=0, T=0.7`。`load_generations` 的 last-wins 策略会正确处理重叠 doc_id，但若 root 中有 shard 未覆盖的 doc_id，这些旧配置样本会混入打分。

**影响**：如果 4 shard 已覆盖全部 doc，无问题。如果未覆盖，少量旧配置生成结果会参与打分（diversity 可能略低但不影响正确性）。

#### 问题 D: `--bf16` 不可关闭（低风险）
`argparse` 定义为 `action="store_true", default=True`，没有对应的 `--no-bf16`。bf16 训练永远开启。对 RTX 5090 来说这是正确行为，但严格来说参数定义不够规范。

### 4. 数据路径检查

所有硬编码路径均在 `/root/autodl-tmp/` 下：
- `DEFAULT_BASE_MODEL = "/root/autodl-tmp/models/Qwen3-4B"` ✅
- `DEFAULT_SFT_ADAPTER = "/root/autodl-tmp/sft_output"` ✅
- 无违规路径

### 5. Shard 当前状态

```
shard_0: 2320 lines
shard_1: 2600 lines
shard_2: 2584 lines
shard_3: 2112 lines
root:    2416 lines
total:   12032 (去重前)
```

### 6. 执行命令建议

```bash
# Step 1: 直接跑 score_filter（内置 shard 合并，无需手动 merge）
export HF_HOME=/root/autodl-tmp/.hf_cache
cd /root/autodl-tmp && python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_pct --top_pct 25

# Step 2: 训练（4 卡）
accelerate launch --config_file /root/autodl-tmp/freige/configs/accelerate_4gpu.yaml \
    -m freige.training.rsft_trainer \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output \
    --weighted_sampling
```

### 7. 结论

**无需修改代码即可执行。** 唯一需要确认的是运行时设置 `HF_HOME` 环境变量。数据流字段完全对齐，超参数默认值符合要求，shard 合并已自动处理。

---
