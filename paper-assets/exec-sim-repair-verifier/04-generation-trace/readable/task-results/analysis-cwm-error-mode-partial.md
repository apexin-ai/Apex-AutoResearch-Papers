# analysis cwm error mode partial

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-error-mode-partial_20260514T094439_result.json`
- **Structured JSON:** [`9a54b6e92849237db047.json`](../../sessions/9a/9a54b6e92849237db047.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### CWM Error Mode 分布 (v11, n=500, max_new_tokens=1024)

| | Count | % |
|---|---|---|
| **Unparseable** | 376 | **75.2%** |
| Parseable correct | 53 | 10.6% |
| Parseable wrong | 71 | 14.2% |

### Error 归因 (167 个错误)

- **57.5%** — unparseable 默认为 majority class (PASS)，但实际是 FAIL
- **38.3%** — 可解析但预测错误（PASS→FAIL 幻觉）
- **4.2%** — 可解析但 FAIL→PASS

### 关键机制

1. **Token 预算耗尽**：模型生成 ~3400 chars 的 pytest 执行 trace（dots、warnings、file paths），在到达 `passed/failed` verdict 之前就用完了 1024 tokens。76.9% 的 unparseable 输出**不含任何** pass/fail 关键词
2. **混合关键词**：22.9% 的 unparseable 同时含 pass 和 fail 关键词（trace 中自然存在）
3. **幻觉偏差**：可解析时模型倾向于幻觉 failures — PASS 样本只有 24.7% 正确率

### CLS vs CWM 对比

CLS 8B ckpt400 = **84.5%** acc，CWM ≈ **58%** — **~26pp gap**，主要由 75% unparseable 率驱动。

**对 C1 claim 的支撑：强**。生成式方法的三个固有困难（token 开销、解析脆弱性、幻觉偏差）直接解释了 CWM 的劣势。

报告已写入 `artifacts/cwm_error_mode_analysis.md`。

---
