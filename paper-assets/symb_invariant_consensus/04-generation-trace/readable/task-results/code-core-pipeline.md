# code core pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_core-pipeline_20260515T085018_result.json`
- **Structured JSON:** [`2e3880ffa43ac57fb653.json`](../../sessions/2e/2e3880ffa43ac57fb653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。写入的文件清单：

| 文件 | 功能 |
|------|------|
| `requirements.txt` | 依赖声明 |
| `sica/__init__.py` | 包标记 |
| `sica/constraint_extractor.py` | LLM 约束提取（含 MockLLM、ExtractionStats） |
| `sica/z3_maxsat.py` | Z3 MAX-SAT 求解（ConstraintDeduplicator + MaxSATSolver + parse/equivalence 工具函数） |
| `sica/scorer.py` | 不变量共识打分 |
| `sica/trace_generator.py` | Trace 生成（vLLM/API/Mock 三模式） |
| `sica/pipeline.py` | 端到端编排 |
| `baselines/__init__.py` | 包标记 |
| `baselines/self_consistency.py` | SC@K majority vote baseline |
| `run_mvp.py` | MVP 实验入口（支持 --mode/--k/--output） |

Mock 模式下 5 题 pipeline 完整跑通，extraction rate 100%，结果已保存至 `results/mvp_results.json`。accuracy 20% 是预期的——MockLLM 对所有题返回相同的 mock 约束和答案（x=7），只有第一题答案匹配。接入真实 LLM 后会产出有意义的结果。

---
