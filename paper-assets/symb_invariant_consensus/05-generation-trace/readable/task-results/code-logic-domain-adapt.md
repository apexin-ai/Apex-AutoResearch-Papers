# code logic domain adapt

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_logic_domain_adapt_20260515T220820_result.json`
- **Structured JSON:** [`877350659087612add26.json`](../../sessions/87/877350659087612add26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码适配完成，ProofWriter-30 就绪。

**修改总结：**

| 修改 | 文件 | 内容 |
|------|------|------|
| 1 | `run_full_mvp.py` | 新增 `folio_path` 参数到 `load_all_problems()`，加载 FOLIO 数据 |
| 2 | `run_full_mvp.py` | SICA/SC 正确率判定：proofwriter/folio 用 `normalize_logic_answer()` 比较，math 用 `is_equiv()` |
| 3 | `baselines/self_consistency.py` | 逻辑域分组使用 `_group_logic_answers()`（大小写无关精确匹配） |
| 4 | `run_full_mvp.py` | 新增 `--folio-data` 和 `--no-folio` 参数 |

**验证结果：**
- vLLM 正常运行（QwQ-32B, max_model_len=16384）
- 1 题 ProofWriter K=2 smoke test 通过（SICA=True V, SC=True V）
- 数学域逻辑未受影响（分支仅在 dataset=proofwriter/folio 时触发）

---
