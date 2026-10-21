# code exp006 graduated filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_graduated_filtering_20260513T072850_result.json`
- **Structured JSON:** [`e728c181d07c81ea31b8.json`](../../sessions/e7/e728c181d07c81ea31b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 dry-run 通过。

## 报告

### 1. 创建的文件

| 文件 | 说明 |
|------|------|
| `scripts/exp006_filtering_strategies.py` | 6 种过滤策略 (NoFilter, BinaryOurs, BinaryDrayson, Graduated, SurprisalBased, DSIR)，统一 `FilterStrategy` 接口 |
| `scripts/exp006_continued_pretraining.py` | LoRA CPT pipeline，加载 Qwen2.5-1.5B + 过滤策略 + WeightedRandomSampler 训练 |
| `scripts/exp006_evaluate.py` | lm-eval-harness 评估 (MMLU + HellaSwag)，支持 base model 和 LoRA adapter |
| `scripts/run_exp006.sh` | 主控脚本，遍历 strategy × seed × alpha，支持断点续跑 |
| `scripts/exp006_analyze.py` | 结果聚合、paired t-test、alpha sensitivity 分析 |

### 2. 依赖检查

全部已安装，无需额外安装：
- `lm_eval` 0.4.11, `peft` 0.19.0, `datasets` 4.8.4, `scipy` 1.17.1, `lightgbm` 4.6.0, `sklearn` 1.8.0

### 3. 数据检查

- `features.csv`: 30000 行, 17 列 (doc_id, depth, 15 features)
- `depth_0.jsonl` ~ `depth_5.jsonl`: 各 5000 条，格式 `{"text": "...", "doc_id": N}`
- 无 `depth_*/` 目录（数据是 flat jsonl 文件）

### 4. dry-run 结果

4 个 Python 脚本 `--help` 全部正常解析参数，无 import 错误。

### 5. 估算 GPU 时间

| 配置 | 数量 |
|------|------|
| 非 graduated 策略 | 5 strategies × 5 seeds = 25 runs |
| graduated α sweep | 5 alphas × 5 seeds = 25 runs |
| **总计** | **50 runs** |
| 单次 (train + eval) | ~25 min (15 min train + 10 min eval) |
| **总 GPU 时间** | **~20.8 小时** |

---
