# prep check tost instruct scripts

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_check-tost-instruct-scripts_20260520T025814_result.json`
- **Structured JSON:** [`15ba0d174a16026835c6.json`](../../sessions/15/15ba0d174a16026835c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇报如下：

---

## P5: TOST 脚本

### 修改前状态

| 脚本 | Seed | Equivalence Margin | 状态 |
|------|------|--------------------|------|
| `scripts/tost_equivalence.py` | 无（统计测试，不涉及seed） | `d_bound = 0.20` hardcoded | ❌ |
| `scripts/tost_per_generator.py` | 无 | `d_bound = 0.20` hardcoded | ❌ |
| `tost_multi_margin.py` | 无 | `MARGINS_PCT = [1,2,3,5]` hardcoded（by design，专测多margin） | 设计如此 |
| `bootstrap_downstream_ci.py` | `[42, 123, 456]` hardcoded（5个variant全用同一组） | N/A | ❌ |
| `run_downstream.sh` | `SEEDS="42 123 456"` hardcoded | N/A | ❌ |
| `finetune_downstream.py` | `--seed` argparse | N/A | ✅ 已参数化 |

### 修改详情

1. **`scripts/tost_equivalence.py`** — 添加 argparse: `--data-path`, `--margin`(default=0.20), `--alpha`(default=0.05), `--output`
2. **`scripts/tost_per_generator.py`** — 同上: `--data-path`, `--margin`, `--alpha`, `--output`
3. **`bootstrap_downstream_ci.py`** — 添加 argparse: `--seeds`(default=[42,123,456]), `--base-dir`, `--n-boot`, `--random-seed`
4. **`run_downstream.sh`** — `SEEDS` 改为 `${2:-42 123 456}`，可通过第2个位置参数覆盖

所有修改已验证 `--help` 正常运行。

---

## P6: Instruct LOGO 脚本

### 脚本路径
- `scripts/p1c_instruct_logo_f1.py` — hardcoded 版本（7-gen LOGO，instruct 模型写死）
- `analyze_7gen_logo.py` — **已参数化**版本（argparse: `--base-features`, `--instruct-features`, `--instruct-model-name`, `--output`）

### Generator 列表状态

**`p1c_instruct_logo_f1.py`**: hardcoded
- base 6-gen 从 `data/features_all_models.csv` 加载（olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b）
- instruct 模型写死为 `"qwen3-1.7b-instruct"`，文件路径写死为 `data/features_qwen3-1.7b-instruct.csv`
- 比较逻辑写死 `"qwen3-1.7b-instruct"` vs `"qwen3-1.7b"`

**`analyze_7gen_logo.py`**: 已参数化
- `--base-features`（base CSV 路径）
- `--instruct-features`（instruct CSV 路径）
- `--instruct-model-name`（instruct 模型名）

### 当前支持 generators
7 个：olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b + qwen3-1.7b-instruct

### 扩展到 5+ generators 需要的修改
`analyze_7gen_logo.py` 已经足够灵活——只需将更多 instruct CSV concat 到 base CSV 即可。具体：
- 数据层面：将多个 instruct 模型的 features CSV 合并到一个 CSV（或修改脚本接受多个 `--instruct-features` 路径）
- 现有代码结构中 `logo_3class()` 和 `binary_f1_logo()` 按 `model_name` 自动 LOGO，无需改核心逻辑
- `vs_base_comparison` 部分（instruct vs base 对比）目前只支持单对对比，多 instruct 模型时需改为循环
- 已有 instruct CSV：`qwen3-0.6b-instruct`, `qwen3-1.7b-instruct`, `olmo-2-0425-1b-instruct`, `llama-3.2-3b-instruct`，共 4 个可用

---
