# infra mvp deploy v3

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_deploy_v3_20260514T085424_result.json`
- **Structured JSON:** [`208cf360f8b3b3965295.json`](../../sessions/20/208cf360f8b3b3965295.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP 50×8 启动成功，已开始处理 Problem 1/50。

---

## 完整产出报告

### 1. 6 项关键修复验证
| # | 验证项 | 结果 |
|---|--------|------|
| 1 | autoformalize.py CRITICAL RULES for quantifiers | ✅ 1 处 |
| 2 | premise_formalizer.py CRITICAL RULES for quantifiers | ✅ 1 处 |
| 3 | premise_formalizer.py max_tokens=512 | ✅ (非 1024) |
| 4 | vocab_normalizer.py split('_') 过滤 | ✅ parts[-1] 逻辑存在 |
| 5 | autoformalize.py ThreadPoolExecutor 并发 | ✅ |
| 6 | premise_formalizer.py PCV 文件存在 | ✅ |

### 2. 服务状态
- **vLLM**: ✅ 运行中，模型 DeepSeek-R1-Distill-Qwen-14B
- **Formalization API**: ✅ 可达 (http://47.94.22.126)，deepseek/deepseek-v3.2 在列

### 3. Dry-run 报告 (mvp_report.json)
```
Config: 2 problems × 2 chains
SVS accuracy: 1/2 = 50%
SC accuracy:  1/2 = 50% (delta=0)
Formalization rate: 69/89 = 77.53%
P1 (autoformalization > 50%): PASS
P2 (IC discrimination): FAIL (all chains SAT, no discrimination)
Cost: $0.036 (171 calls, 129K tokens)
```

### 4. ForAll vs Exists 比例
**ForAll: 14, Exists: 1** — CRITICAL RULES 修复生效，ForAll 占 93%

### 5. UNSAT 情况
所有 4 chains 均 ic_sat=True（无 UNSAT）。P2 因此 FAIL——2 problem 样本太小无法产生统计区分。

### 6-7. 完整 MVP
- **PID**: 31169
- **Config**: 50 problems × 8 chains = 400 total chains
- 启动日志确认：50 problems loaded, chain sampling 已开始，vLLM 200 OK

---
