# infra check model data readiness

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_model_data_readiness_20260516T103212_result.json`
- **Structured JSON:** [`9e53bd12586bc71ae887.json`](../../sessions/9e/9e53bd12586bc71ae887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D077 资源就绪状态

### 1. LLaMA-3.1-8B ✅ 就绪（symlink 需修复）

实际路径 `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/`，文件完整：

| 文件 | 大小 |
|------|------|
| model-00001-of-00004.safetensors | 4.6GB |
| model-00002-of-00004.safetensors | 4.7GB |
| model-00003-of-00004.safetensors | 4.6GB |
| model-00004-of-00004.safetensors | 1.1GB |
| **总计** | **~15GB** |

config.json 确认：LlamaForCausalLM, hidden_size=4096, 32层, 8 KV heads, vocab_size=128256, bfloat16 — 正确。tokenizer.json / tokenizer_config.json / special_tokens_map.json / generation_config.json / model.safetensors.index.json 齐全。

⚠️ **快捷 symlink 损坏**：`/root/autodl-tmp/models/Meta-Llama-3.1-8B` → 指向不存在的 `...LLM-Research/Meta-Llama-3___1-8B`。代码应直接引用 `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/`，或修复 symlink。

### 2. Re-DocRED ✅ 就绪

路径 `/root/autodl-tmp/data/re-docred/`，含 3 个 JSON + metadata：

| 文件 | 大小 | 文档数 | 保留三元组 |
|------|------|--------|-----------|
| train_annotated.json | 12.8MB | 3,053 | 47,260 |
| dev.json | 2.1MB | 500 | 7,473 |
| test.json | 2.1MB | 500 | 7,547 |

- 格式：标准 DocRED 格式（vertexSet + labels），每个 label 含 `r`/`h`/`t`/`evidence` 字段
- mode 为 `evidence_only`：已过滤仅保留有 evidence 标注的三元组
- relation type 使用 Wikidata PID（P17, P131, P150 等），与 DocRED 96 类体系兼容
- 另有原始 repo clone：`/root/autodl-tmp/data/re-docred-repo/`（含 evaluation.py）

### 3. GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | **0MiB / 32GB** | 0% | 空闲 ✅ |
| 1 | 11,415MiB / 32GB | 49% | python (PID 319638) |
| 2 | 5,503MiB / 32GB | 36% | python (PID 324684) |
| 3 | 18,471MiB / 32GB | 64% | python (PID 322973) |

GPU 0 完全空闲，可用于 LLaMA-3.1-8B 实验（bf16 约需 ~16GB）。

### 4. 磁盘空间 ⚠️ 偏紧

```
/root/autodl-tmp: 250GB total, 204GB used, 47GB available (82%)
```

47GB 剩余。LLaMA-3.1-8B 已下载（15GB），Re-DocRED 数据很小（~17MB）。训练产出（checkpoints、logs）需要注意空间，LoRA checkpoint 每个约几百 MB 问题不大，但 full-finetune checkpoint 约 15GB/个会很紧。

---
