# investigate esj autodl5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_esj_autodl5090c_20260520T162024_result.json`
- **Structured JSON:** [`b62e8a114c504e3a62df.json`](../../sessions/b6/b62e8a114c504e3a62df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090-c 环境探查结果

### 1. run_esj.py
**不存在。** 整个 `/root` 下没有任何 `*esj*` 文件。需要从本地推送或创建。

### 2. 项目代码目录
- `/root/struct_self_consist_ie/` — **不存在**
- `/root/autodl-tmp/struct_self_consist_ie/` — **存在**，包含 code/data/checkpoints/output 等完整目录结构

### 3. FewNERD 数据
**存在**，路径：`/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/`
- train.json, dev.json, test.json, llmfactory_train.json, llmfactory_dev.json
- 另有 `data/fewnerd_n16_subset/test.json`

### 4. Qwen 模型

| 模型目录 | 大小 |
|---------|------|
| `checkpoints/qwen3-8b-fewnerd-exp021-merged` | 16G |
| `checkpoints/qwen3-8b-conll2003-merged` | 16G |
| `checkpoints/qwen3-8b-scierc-merged-v2` | 16G |
| `checkpoints/qwen25-7b-fewnerd-merged` | 15G |
| `checkpoints/qwen25-7b-wnut17-merged` | — |
| `checkpoints/qwen25-14b-fewnerd-merged-final` | 28G |
| `checkpoints/qwen25-14b-fewnerd-merged-ckpt36000` | — |
| `.hf_cache/` 下有 Qwen3-8B, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct (locks) | — |
| 另有 Llama-3.1-8B-Instruct | — |

checkpoints 总计 **142G**。

### 5. GPU 状态

| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX 5090 | 31101/32607 MiB | 99% |
| **cuda:1** | **RTX 5090** | **0/32607 MiB** | **0%** ✅ 空闲 |
| cuda:2 | RTX 5090 | 0/32607 MiB | 0% |
| cuda:3 | RTX 5090 | 0/32607 MiB | 0% |

### 6. Python/ML 环境
- Python: **3.12.3** (miniconda3, `python3` 不在 PATH 中，需用 `/root/miniconda3/bin/python`)
- PyTorch: **2.10.0+cu128**
- Transformers: **4.57.1**
- vLLM: **0.18.1**
- flash-attn: **未安装**

### 7. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 11G | 20G | 35% |
| /root/autodl-tmp | 350G | 224G | 127G | 64% |

**总结：cuda:1 空闲可用，Python/torch/vllm 环境就绪，FewNERD 数据和多个 Qwen checkpoint 已就位，磁盘充足。唯一缺失的是 run_esj.py 本身——需要创建或推送到服务器。**

---
