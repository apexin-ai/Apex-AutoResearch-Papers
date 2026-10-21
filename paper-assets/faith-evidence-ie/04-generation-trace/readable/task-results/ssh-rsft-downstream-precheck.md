# ssh rsft downstream precheck

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-downstream-precheck_20260515T042359_result.json`
- **Structured JSON:** [`d5c3dc00fa9d7c6e9267.json`](../../sessions/d5/d5c3dc00fa9d7c6e9267.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成。汇总报告如下：

---

## RSFT 下游流水线预检报告

### 1. 生成进度（仍在运行中）

| Shard | 行数 | 文档数 (÷8) |
|-------|------|------------|
| shard_0 | 4,928 | 616 |
| shard_1 | 5,320 | 665 |
| shard_2 | 5,288 | 661 |
| shard_3 | 4,608 | 576 |
| **合计** | **20,144** | **2,518 / 3,027 (83%)** |

根目录有一个旧的 `generations.jsonl`（2,416 行 = 302 docs），是之前单卡运行的残留数据。Shard 数据无重复（每个 doc_id 正好 8 条记录）。

### 2. rsft_score_filter.py — 2 个阻塞项

**阻塞 A: `load_generations()` 不支持多 shard 输入**
- 代码只读 `input_dir / "generations.jsonl"` 单文件（第 181 行）
- 如果 `--input_dir /root/autodl-tmp/rsft_generations`，会读到根目录旧数据（302 docs），**不是 shard 数据**
- **修复**：生成完成后需先合并 shard，或修改 `load_generations()` 支持 `shard_*/generations.jsonl` glob

**阻塞 B: NLI 模型路径 + HF_HOME 未配置**
- `/root/autodl-tmp/models/nli-deberta-v3-base/` 不存在
- 模型在 HF cache: `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7/`（完整，含 model.safetensors）
- 但服务器 `HF_HOME` **未设置**，HuggingFace 默认找 `~/.cache/huggingface/`，找不到缓存会尝试联网下载
- **修复**：运行时 `export HF_HOME=/root/autodl-tmp/.hf_cache`，或 `--nli_model_path` 指定 snapshot 完整路径

**无阻塞项：**
- 去重：shard 数据干净，每 doc 8 条，无重复。合并时排除根目录旧文件即可
- 代码逻辑正确：打分 → 硬阈值过滤 → top_pct 分组选择 → 转 SFT 格式，pipeline 连贯

### 3. rsft_trainer.py — 无阻塞项

- `--bf16` 默认 True，`--quantize` 默认 False（不会触发 RTX 5090 CUBLAS 错误）
- 输入格式 `{"input", "output", "ced_score"}` 与 score_filter 输出完全匹配
- Base model `/root/autodl-tmp/models/Qwen3-4B/` 存在 ✓
- SFT adapter `/root/autodl-tmp/sft_output/` 存在（含 adapter_model.safetensors） ✓
- DocRED eval 数据 `/root/autodl-tmp/data/docred/dev.json` 存在 ✓
- WeightedSFTTrainer 按 CED score 加权采样逻辑正确

### 4. 磁盘空间 — 充足

- 数据盘：250GB 总量，已用 62GB，**剩余 189GB (75%)**
- 当前生成数据 259MB，预估完成后 ~350MB
- 完全不构成问题

### 5. 阻塞项清单及建议修复

| # | 阻塞项 | 修复方案 |
|---|--------|---------|
| 1 | score_filter 不读 shard 子目录 | 合并：`cat shard_*/generations.jsonl > all_generations.jsonl`，然后修改 `--input_dir` 指向合并文件所在目录；或修改 `load_generations()` 加 glob 逻辑 |
| 2 | HF_HOME 未设置，NLI 模型路径不对 | 运行前 `export HF_HOME=/root/autodl-tmp/.hf_cache` |

需要我现在修复这两个阻塞项吗？

---
