# analysis pass fail trace diff

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pass_fail_trace_diff_20260522T041601_result.json`
- **Structured JSON:** [`6b2adb42da91f5f25b48.json`](../../sessions/6b/6b2adb42da91f5f25b48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果汇总：

## MF-3 Pass/Fail Trace Diff 分析结果

### 1. Section-Level Diff（29 个配对 problem）
| Condition | Code diff | Test diff | Trace diff |
|-----------|-----------|-----------|------------|
| full_trace | 10.4% | 0% | **89.6%** |
| exception_only | 17.1% | 0% | **82.9%** |
| ae_only | 13.7% | 0% | **86.3%** |
| no_trace | 100% | 0% | 0% |

Test diff 恒为 0（同一 problem 的 test 完全相同），trace 占据绝大多数 diff。

### 2. Trace 内部分类
| Condition | Diagnostic ratio | Detail |
|-----------|-----------------|--------|
| exception_only | **100%** | 93.5% exception + 6.5% structural marker |
| full_trace | 0.3% | 99.7% 是 code-induced runtime context（不同代码产生不同 trace） |
| ae_only | 2.0% | 大量 `[fallback: full locals]` 在 pass/fail 中都出现 |

### 3. Diagnostic Feature → Verdict Prediction
| Condition | Accuracy | Coverage |
|-----------|----------|----------|
| exception_only | **99.3%** | **100%** |
| ae_only | **98.7%** | 75.5% |
| full_trace | 100% | 5.9%（只有 `[No trace available]` 标记可判） |
| no_trace | - | 0%（无任何 feature 可用） |

### 关键发现
- **exception_only**: 100% 的 trace diff 都是 diagnostic 内容，仅凭 exception 有无即可 99.3% 准确率预测 verdict → exception tokens 是唯一的 verdict-discriminative signal
- **ae_only**: actual/expected 值匹配/不匹配预测准确率 98.7%，但 token 级占比低（大量 locals dump 噪声）
- **full_trace**: trace 占 diff 的 90%，但几乎全部是 code-induced（不同 solution → 不同执行路径），diagnostic marker 占 < 1%。信号极稀疏但确定性。
- **no_trace**: 完全无 diagnostic feature → 模型必须做 code reasoning

产出：
- JSON: `/root/trace-verdict-study/artifacts/pass_fail_diff/pass_fail_diff_results.json`
- 图表: `pass_fail_diff_analysis.{pdf,png}`, `diff_decomposition.{pdf,png}`
- 脚本: `/root/trace-verdict-study/analysis/pass_fail_trace_diff.py`

---
