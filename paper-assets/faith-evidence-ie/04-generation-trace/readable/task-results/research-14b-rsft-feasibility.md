# research 14b rsft feasibility

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_14b_rsft_feasibility_20260519T065359_result.json`
- **Structured JSON:** [`07be218b614f785b93c7.json`](../../sessions/07/07be218b614f785b93c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

## 14B RSFT Pipeline 显存可行性评估

### 当前 GPU 状态
| GPU | 已用 | 空闲 | 占用者 |
|-----|------|------|--------|
| 0 | 29.6 GB | 2.4 GB | 某 python 进程 |
| 1 | 16.1 GB | 15.6 GB | 14B SFT ZeRO-3 (rank 0) |
| 2 | 25.2 GB | 6.7 GB | 14B SFT ZeRO-3 (rank 1) |
| 3 | 5.4 GB | 26.1 GB | 某 python 进程 |

### 代码量化支持：已就绪，无需改代码

| 模块 | 参数 | 默认值 | 实现 |
|------|------|--------|------|
| `rsft_generate.py` | `--quantize` | OFF | NF4 + double quant |
| `rsft_trainer.py` | `--quantize` | OFF | QLoRA (NF4) |
| `eval/inference.py` | `--quantize` | **ON** | NF4 + double quant |

`bitsandbytes` 0.49.2 已安装。Qwen3-14B 权重已下载在 `/root/autodl-tmp/models/Qwen/Qwen3-14B`。

### 显存估算

**Qwen3-14B 各精度占用：**
- bf16: ~28GB 权重 → 加上 KV cache/adapter 约 30GB+ → 单卡 32GB **放不下**
- 4-bit NF4 (double quant): ~7-8GB 权重

### 方案总表

| 步骤 | 单卡方案 (4-bit) | 预估显存 | 2-GPU 方案 (bf16) | 推荐 |
|------|-----------------|---------|-------------------|------|
| **Candidates gen (N=8)** | `--quantize` 单卡 | ~9-10GB | 无必要 | **单卡 4-bit** |
| **CED scoring** | NLI 模型单卡 | ~1.5GB | — | **单卡** |
| **RSFT training** | `--quantize` QLoRA 单卡 | ~16-22GB | DeepSpeed ZeRO-3 bf16 | **单卡 QLoRA** |
| **Eval** | 默认已 4-bit 单卡 | ~9-10GB | 无必要 | **单卡 4-bit** |
| **No-evidence eval** | `--quantize --no_evidence` | ~9-10GB | 无必要 | **单卡 4-bit** |

### 关键结论

1. **所有步骤单卡 4-bit 均可行**，不需要 2-GPU 方案。代码已全部支持 `--quantize`，无需改代码。

2. **RSFT training 注意事项**：4B 脚本用 `per_device_batch_size=4`。14B QLoRA 训练 activations 更大，可能需要把 batch_size 降到 **2**（配合 `gradient_accumulation_steps=8` 保持 effective batch=16）。如果 batch_size=4 OOM，这是第一个调的旋钮。

3. **Candidates generation**：4B 脚本未加 `--quantize`（4B bf16 仅 ~8GB）。14B 必须加 `--quantize`，否则 28GB 权重+KV cache 单卡爆。

4. **14B SFT no-evidence eval**：单卡 4-bit 可行（~9-10GB），`inference.py` 默认 quantize=True，直接跑即可。

5. **并行策略**：14B SFT 训练完释放 GPU 1+2 后，4 卡各跑一个 shard 做 candidates generation（和 4B 脚本一样 `SHARD=0..3`），每卡 ~9-10GB，14B 也能 4 卡并行生成。

6. **不推荐 2-GPU bf16 方案**：虽然 `rsft_trainer.py` 支持 `--deepspeed`，但 4-bit QLoRA 单卡够用，避免分布式的额外复杂度。

---
