# ssh model dataset prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_model_dataset_prep_20260517T070038_result.json`
- **Structured JSON:** [`a771bbd6df4ceb756ffa.json`](../../sessions/a7/a771bbd6df4ceb756ffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载稳定 ~3.3MB/s (100MB/2.6GB)，ETA ~12分钟。所有信息已收集完毕。

---

## Phase 1 准备状态汇报

### 1. 代码参数化：已支持 ✓

`iterative_train.py` 已有：
- `--model_name` (default: `EleutherAI/pythia-410m`)
- `--data_dir` (default: `data/wikitext103`)
- `--dataset` (logging 用)

模型加载完全通用（`AutoModelForCausalLM.from_pretrained`），pad_token 有 fallback 处理。**无需代码改动。**

### 2. HF cache 已有模型

| 模型 | 大小 | 状态 |
|------|------|------|
| EleutherAI/pythia-410m | 872MB | ✓ 可用 |
| gpt2-medium | 1.5GB | ✓ 可用（bonus） |
| gpt2-large | 3.1GB | ✓ 可用（bonus） |
| facebook/opt-1.3b | ~2.6GB | 下载中 (100MB, ETA ~12min) |

### 3. OPT-1.3B 下载：进行中

PID 245459 后台运行，速率 ~3.3MB/s，预计 ~12 分钟完成。

### 4. C4 数据：已就绪 ✓

`data/c4_5k/` 已存在，格式与 WikiText 一致（HF Arrow，train/eval/prompts 子目录）：
- Train: 4,500 samples
- Eval: 500 samples  
- Prompts: 500 samples

**注意规模差异**：WikiText 5k 有 716,506 train / 5,000 prompts，C4 仅 4,500 train / 500 prompts。如需公平对比，C4 train set 可能需要扩大或 WikiText 需要缩小。

### 5. 磁盘空间：充足

147GB 可用 (42% 使用)。

### 6. 总结

**Status: Ready（待 OPT-1.3B 下载完成，~12min）**

唯一潜在问题：C4 vs WikiText 训练集规模差 159x（4.5K vs 716K），prompts 差 10x（500 vs 5000）。实验公平性可能需要：
- 扩大 C4 到 ~5000 prompts + 更多 train samples，或
- 缩小 WikiText 到与 C4 对齐的规模

这取决于实验设计意图——是否需要 Director 决定？

---
