# code plan 005 analysis prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-005-analysis-prep_20260515T054226_result.json`
- **Structured JSON:** [`dcf447645cd772b43b72.json`](../../sessions/dc/dcf447645cd772b43b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。脚本 `analyze_prompt_types.py` 已部署到服务器，包含以下功能：

| 分析模块 | 内容 |
|----------|------|
| **Per-type depth signal** | 每种 prompt type 内部 5-fold CV 分类 F1 + 7 个特征与 depth 的 Spearman 相关 |
| **LOPTO** | Leave-one-prompt-type-out：用 2 种训练，测 held-out 类型的 depth 分类泛化性 |
| **Depth decay** | 每种 prompt type 的 7 个特征随 depth 的线性衰减斜率对比 |
| **Feature distributions** | 各特征在不同 prompt type × depth 的分布统计 |

输出：`data/prompt_type_features.csv`（特征）+ `data/prompt_type_results.json`（完整结果）+ stdout summary table。

用法：
```bash
# 全量运行（数据就绪后）
python analyze_prompt_types.py --device cuda:0

# 快速测试
python analyze_prompt_types.py --dry-run

# 跳过特征提取（已有 features CSV 时）
python analyze_prompt_types.py --skip-extraction
```

---
