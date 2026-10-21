# check llama docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_docred_progress_20260514T175425_result.json`
- **Structured JSON:** [`d33dfa45ce0b0451196a.json`](../../sessions/d3/d33dfa45ce0b0451196a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 进度

| 实验 | 已完成 | 总数 | 进度 | 运行时间 |
|------|--------|------|------|----------|
| `llama_docred_full_s1` (cuda:0) | 572 | 998 | **57.3%** | 3h 13m |
| `llama_docred_unconstrained` (cuda:1) | 661 | 998 | **66.2%** | 3h 19m |

### 预估完成时间

- **full_s1**: 572 docs / 193 min ≈ 2.96 doc/min → 剩余 426 docs ≈ **144 min (~2.4h)**，预计约 **2.5h 后完成**
- **unconstrained**: 661 docs / 199 min ≈ 3.32 doc/min → 剩余 337 docs ≈ **101 min (~1.7h)**，预计约 **1.7h 后完成**

### GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 86% | 17,089 / 97,887 MiB (17.5%) |
| cuda:1 | 89% | 17,089 / 97,887 MiB (17.5%) |

两块卡 GPU 利用率健康（86-89%），显存占用约 17GB。

### 修复版 violation_checker_docred.py

**已就绪。** 确认包含：
- `strip()` 归一化（6 处）
- `ENTITY_TYPE_ALIASES` 字典 + 查找（line 20, 35）

### 日志状态

- **full_s1**: 有频繁的 grammar-first fallback 触发（semantic mask 消除了所有 grammar-valid tokens），说明 constrained decoding 在某些 step 回退到纯语法约束。功能正常但值得后续关注 fallback 频率。
- **unconstrained**: 正常运行，仅有 pad_token_id 设置提示。

### 异常

无严重异常。full_s1 的 grammar-first fallback 频率较高（连续 skip_count 递增），后续分析时可统计 fallback 比例评估对输出质量的影响。

---
