# analysis bf16 importance s015

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_importance_s015_20260514T061847_result.json`
- **Structured JSON:** [`95fc43cd3249a9804d1c.json`](../../sessions/95/95fc43cd3249a9804d1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bf16_importance_s015 实验结果

**总体: PASS, 0 NaN**

### Interaction Index (s=0.15)

| Phase | Mean | Median | CI 95% | Winsorized Mean | Skewness | Outliers |
|-------|------|--------|--------|-----------------|----------|----------|
| high | **-0.1502** | 0.0058 | [-0.2946, -0.0554] | -0.0624 | -14.99 | 2 |
| mid | **+0.4473** | 0.0807 | [+0.2680, +0.6687] | +0.3248 | 4.72 | 5 |
| low | **+2.4058** | 0.3983 | [+1.4788, +3.6677] | +1.2789 | 9.54 | 5 |

### Perplexity (s=0.15)

| Phase | Dense | Attn-only | KV-only | Both |
|-------|-------|-----------|---------|------|
| high | 1.169 | 1.486 | 1.448 | 1.591 |
| mid | 1.227 | 1.514 | 2.597 | 3.454 |
| low | 1.229 | 1.615 | 8.920 | 12.508 |

### Phase Stats
- high: 21,086 tokens / 387 segments
- mid: 13,306 tokens / 191 segments
- low: 27,748 tokens / 397 segments
- **Total: 50 problems processed**

### Null / NaN 统计
- **NaN: 0** — bf16 完全消除了 fp16 的 NaN 问题
- **null: 11** — 均为某些 problem 缺少对应 phase 的 segments（10x `ii_mid=null`, 1x `ii_high=null`），属正常行为（该 problem 的 token 全部落入其他 phase）

### Pass/Fail Tests
- CI overlap test: **PASS** — low vs mid CI 不重叠
- Sign reversal test: **PASS** — high II<0, mid II>0
- Overall: **PASS**

### 与 fp16 版本的关键区别
- **NaN 消除**: fp16 版本在 Layer 27 存在 NaN 偏差，bf16 完全没有 NaN
- 梯度模式一致：high→mid→low 的 II 递增趋势保持，sign reversal 成立
- warnings 列表为空，日志无错误，EXIT_CODE=0

---
