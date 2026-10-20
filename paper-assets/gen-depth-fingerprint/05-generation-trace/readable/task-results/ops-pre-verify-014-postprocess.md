# ops pre verify 014 postprocess

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pre-verify-014-postprocess_20260515T032425_result.json`
- **Structured JSON:** [`ab76aed785dbdc03bfba.json`](../../sessions/ab/ab76aed785dbdc03bfba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕。以下是预验证报告。

---

## 预验证报告：plan-014 后处理流水线

### 1. 文件/路径状态

| 检查项 | 状态 | 说明 |
|--------|------|------|
| `extract_features.py` | ✅ | 存在，单生成器特征提取 |
| `extract_features_multi.py` | ✅ | 支持 `--model-name` 增量模式，自动合并已有CSV |
| `cross_generator_eval.py` | ⚠️ | LOGO 存在，但 family 列表需更新 |
| `classify_multi.py` | ⚠️ | LOGO 存在，但 `MODEL_FAMILIES` 需更新 |
| Pythia-410M 模型 | ✅ | `/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c...` 完整 |
| qwen3-8b 生成数据 | ✅ | `data/qwen3-8b/generations_shard0_recovered.jsonl` — 3418 行，持续增长 |
| 5 生成器特征文件 | ✅ | `data/features_all_models.csv` — 23032 行，5 生成器齐全 |
| 5 生成器原始数据 | ✅ | pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b 全在 `data/` 下 |

### 2. 需修复的问题（3 处代码改动）

**问题 A**：`cross_generator_eval.py` 第 130 行 — family-out 列表硬编码了 5 个生成器
```python
# 当前
non_pythia = ["olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]
# 需改为
non_pythia = ["olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
```

**问题 B**：`classify_multi.py` 第 39-44 行 — `MODEL_FAMILIES` 缺少 qwen3-8b
```python
# 需添加
"qwen3-8b": "qwen",
```

**问题 C**：`extract_features_multi.py` 第 25 行 — `ALL_GENERATORS` 缺少 qwen3-8b（仅影响全量模式，`--model-name` 增量模式不受影响）
```python
ALL_GENERATORS = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-1.7b", "qwen3-0.6b", "qwen3-8b"]
```

### 3. 数据注意事项

- `data/qwen3-8b/` 下同时存在 `generations_shard0.jsonl`（416 行旧数据）和 `generations_shard0_recovered.jsonl`（3418 行）
- `discover_data()` 的 glob `generations_shard*.jsonl` 会匹配两者，但 `load_records` 按 `(seed_id, depth)` 去重，不会重复
- plan-014 完成后确认最终文件名——如果最终输出仍为 `_recovered` 后缀，不影响流水线

### 4. 命令模板

**Step 1：特征提取（增量模式，直接合并到 features_all_models.csv）**
```bash
cd /root/gen-depth-fingerprint
python extract_features_multi.py \
  --model-name qwen3-8b \
  --output data/features_all_models.csv \
  --batch-size 8 \
  --device cuda:0
```

**Step 2：LOGO 3-class 评估（6 生成器）**
```bash
cd /root/gen-depth-fingerprint
python cross_generator_eval.py
```
（读取 `data/features_all_models.csv`，输出 `data/cross_generator_results.json` + `data/cross_generator_report.md`）

**Step 3（可选）：classify_multi.py 5-class LOGO 评估**
```bash
cd /root/gen-depth-fingerprint
python classify_multi.py --input data/features_all_models.csv
```

### 5. 结论

流水线基本就绪，plan-014 完成后需要先做 **3 处代码改动**（问题 A/B/C），然后按 Step 1 → Step 2 顺序执行即可。预计特征提取耗时取决于 qwen3-8b 最终数据量（当前 3418 行，每行需 GPU 推理）。

---
