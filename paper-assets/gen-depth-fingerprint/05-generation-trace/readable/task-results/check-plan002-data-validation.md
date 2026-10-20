# check plan002 data validation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan002-data-validation_20260514T232053_result.json`
- **Structured JSON:** [`1024df5fe31df44e7839.json`](../../sessions/10/1024df5fe31df44e7839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据中没有 model 字段。根据文件位置和 MVP 阶段背景，这应该是 Pythia-2.8B 的数据。

## 数据完整性验证结果

### 1. Qwen3-1.7B shard0 深度检查

| 指标 | 结果 |
|------|------|
| 总行数 | 2,291 |
| Unique seeds | 498 |
| JSON 错误 | 0 |
| 重复条目 | **0** |
| 深度缺口 | **0** |
| 完整 5 层 seeds | 398 |
| 不足 5 层 seeds | 100 |
| 深度分布 | d0:498, d1:492, d2:468, d3:435, d4:398 |

**结论：shard0 数据完整，无重复、无缺口。** 之前报告的 199 条 skipped 是正常的深度递减衰减（高深度生成失败/跳过），不是 SIGHUP resume 导致的完整性问题。深度逐层递减的 pattern（498→492→468→435→398）符合预期。

### 2. 全模型合并文件验证

| 模型 | 行数 | Seeds | 文件大小 | 错误 | d0 | d1 | d2 | d3 | d4 |
|------|------|-------|---------|------|-----|-----|-----|-----|-----|
| pythia-2.8b | 4,609 | 995 | 4.74MB | 0 | 995 | 989 | 924 | 879 | 822 |
| pythia-1b | 4,555 | 995 | 4.71MB | 0 | 995 | 993 | 912 | 851 | 804 |
| olmo-2-1b | 4,713 | 995 | 5.24MB | 0 | 995 | 988 | 947 | 905 | 878 |
| qwen3-0.6b | 4,538 | 996 | 4.75MB | 0 | 996 | 986 | 938 | 840 | 778 |
| qwen3-1.7b | 4,617 | 996 | 4.99MB | 0 | 996 | 983 | 941 | 875 | 822 |

**关键发现：**
- **5 个模型全部 0 JSON 错误**，数据格式完整
- Pythia-2.8B 数据在根目录 `/root/gen-depth-fingerprint/data/generations.jsonl`（MVP 阶段产物，无 model 字段，字段为 `id/seed_id/depth/text/token_count`）
- 所有模型 depth 0 覆盖 995-996 seeds，逐层递减到 d4 的 778-878，这是正常的深度生成衰减
- OLMo-2-1B 在高深度保留率最好（d4:878/995=88.2%），Qwen3-0.6B 最差（d4:778/996=78.1%）
- Qwen3 系列 seeds 为 996，Pythia/OLMo 为 995（差 1 个 seed，可能是 seed 集划分差异）

---
