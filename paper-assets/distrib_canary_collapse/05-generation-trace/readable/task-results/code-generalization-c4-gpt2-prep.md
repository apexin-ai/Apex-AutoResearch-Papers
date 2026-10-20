# code generalization c4 gpt2 prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_generalization_c4_gpt2_prep_20260515T083604_result.json`
- **Structured JSON:** [`acf884601f0e669fe7a3.json`](../../sessions/ac/acf884601f0e669fe7a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**环境准备结果：**
- **C4 数据集** — 已下载并准备好 `data/c4_5k/`（train:4500, eval:500, prompts:500），从 allenai/c4 第一个 json.gz 分片提取
- **GPT-2-medium** — 已缓存（355M params, vocab 50257）
- **脚本兼容性** — `iterative_train.py` 已完全支持 `--model_name` 和 `--data_dir` 参数，**无需任何修改**

**关键发现：**
- wikitext103_5k/train 实际包含完整 WikiText-103 训练集（~1.8M 样本），而 C4 子集仅 4500 样本。每代训练 5000 steps × bs=4 = 20k 访问时，C4 样本会被遍历 ~4.4 次 vs WikiText 仅覆盖 ~1.1%。这可能影响对比公平性，已在报告中标注。

**产出文件：** `artifacts/generalization_prep.md`，包含：
- 4 个完整训练命令（2 数据 × 2 α）
- 时间估算：每个实验 ~3.5-4.5h，串行 2 组 ~8h
- 推荐先跑 B 组（WikiText + GPT-2-medium），因为与现有 Pythia baseline 直接可比且模型更小更快

---
