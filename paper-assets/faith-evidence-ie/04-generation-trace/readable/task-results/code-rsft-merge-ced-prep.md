# code rsft merge ced prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft_merge_ced_prep_20260515T043557_result.json`
- **Structured JSON:** [`1a3914c9ca993c594777.json`](../../sessions/1a/1a3914c9ca993c594777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码已审查完毕。汇报如下：

---

## 1. Merge 脚本

**`/root/autodl-tmp/freige/training/merge_shards.py` — 已存在，无需新写。**

用法：
```bash
cd /root/autodl-tmp && python -m freige.training.merge_shards \
    --shard_dir /root/autodl-tmp/rsft_generations \
    --output /root/autodl-tmp/rsft_generations/generations_merged.jsonl
```

去重策略：`(doc_id, generation_idx)` 为 key，last-wins（shard 覆盖 root）。会自动处理 shard_1 续传重复。

当前各 shard 行数：shard_0=5280, shard_1=5552, shard_2=5568, shard_3=5032, 总计 21432 行。

---

## 2. rsft_score_filter.py — 输入/输出/参数

**输入**: `--input_dir`（含 shard_* 子目录的目录），内部 `load_generations()` 自带合并 + 去重逻辑，所以可以跳过 merge_shards 直接指向 `/root/autodl-tmp/rsft_generations`。

**输出**（`--output_path` 目录下）：
- `rsft_train.jsonl` — 筛选后的 SFT 训练数据，字段：`{input, output, ced_score, doc_id, generation_idx, format_reward, f1_reward, combined_score}`
- `rsft_scores.jsonl` — 全量打分记录
- `rsft_report.json` — 统计报告

**关键参数**：
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--selection_strategy` | `top_pct` | threshold / top_k / top_pct |
| `--top_pct` | 25 | 每 doc 取 top 25% |
| `--format_threshold` | 0.5 | format_reward 硬阈值 |
| `--format_weight / f1_weight / ced_weight` | 0.2 / 0.4 / 0.4 | combined_score 权重 |
| `--nli_model_path` | `cross-encoder/nli-deberta-v3-base` | NLI 模型 |
| `--nli_device` | auto | 可指定 `cuda:0` |
| `--tau` | 0.5 | CED 阈值 |

---

## 3. rsft_trainer.py — 配置和格式

**输入格式**：JSONL，每行 `{input, output, ced_score(optional)}`。与 score_filter 的输出格式**匹配**。

**关键配置**：
- 支持 bf16 + QLoRA（4-bit nf4）
- base model: `/root/autodl-tmp/models/Qwen3-4B`
- SFT adapter: `/root/autodl-tmp/sft_output`（先 merge SFT adapter 再加新 LoRA）
- LoRA: r=16, alpha=32, 7 个 target_modules
- 支持 `--weighted_sampling`（用 ced_score 做 WeightedRandomSampler）
- 支持 accelerate 多卡
- 内置 TaskEvalCallback（eval_data_dir 指向 DocRED dev 时可跑 task eval）

---

## 4. 数据格式对齐 — **有一个关键 bug**

**generation → score_filter 格式不匹配：**

generation JSONL 的字段：`doc_id, generation_idx, prompt, output(string), raw_text, format_ok, truncated, gold_triples, sents`

但 `score_all_records()` 直接访问 `rec["parsed_triples"]`（第 ~280 行），这个字段在 generation 输出中**不存在**。`output` 是 JSON 字符串，不是已解析的 list。

**这会导致 `KeyError: 'parsed_triples'` 崩溃。**

修复方案：在 `load_generations()` 末尾或 `score_all_records()` 开头，对每条记录做：
```python
if "parsed_triples" not in rec:
    try:
        rec["parsed_triples"] = json.loads(rec["output"])
    except (json.JSONDecodeError, TypeError):
        rec["parsed_triples"] = []
```

score_filter → trainer 格式：`format_sft_training_data()` 输出 `{input, output, ced_score, ...}`，trainer 的 `load_rsft_data()` 读取 `s["input"]` 和 `s["output"]`。**格式对齐，无问题。**

---

## 5. CED 筛选资源需求

- NLI 模型：DeBERTa-v3-base，磁盘 715MB，VRAM **< 1GB**（fp32）
- **1 卡即可**，其余 3 卡完全空闲
- 预计 21K records × ~10 triples/record = ~210K NLI 推理，DeBERTa 在 RTX 5090 上单推理 < 1ms，估计 **15-30 分钟**完成全部打分

---

## 6. 需要修复的问题

| 优先级 | 问题 | 修复 |
|--------|------|------|
| **P0** | `rsft_score_filter.py` 缺少 `output` → `parsed_triples` 的解析步骤 | 在 `load_generations` 或 `score_all_records` 中添加 `json.loads(rec["output"])` |
| P2 | `--nli_model_path` 默认值是 HF hub ID，不是本地路径。本地缓存路径是 `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/...` | 运行时用 `--nli_model_path` 指定本地路径，或设 `HF_HOME=/root/autodl-tmp/.hf_cache` |

P0 bug 不修复的话 score_filter 跑不起来。需要我现在修复吗？

---
