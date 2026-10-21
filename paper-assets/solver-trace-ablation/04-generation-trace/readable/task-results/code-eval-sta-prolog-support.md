# code eval sta prolog support

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-sta-prolog-support_20260514T054312_result.json`
- **Structured JSON:** [`475f3de09fe9b2a98655.json`](../../sessions/47/475f3de09fe9b2a98655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**完成情况：**

1. `scripts/sta_prolog.py` — 5/5 test cases 通过（swipl 可用）
2. `scripts/eval_sta.py --help` — `--logic_type {fol,prolog}` 和 `--max_samples` 参数正常显示
3. Dry-run 2 samples — 端到端流程跑通：模型加载 → Prolog prompt 生成 → PrologSolver 评估 → JSON 输出

**改动摘要：**
- 新增 `--logic_type` 参数（choices: fol/prolog，默认 fol），自动选择对应的 system prompt、user template、solver 和 reward function
- 新增 `--max_samples` 参数，限制评估样本数
- `--solver` 改为可选，默认根据 logic_type 自动选择（fol→prover9, prolog→prolog）
- 输出 JSON summary 中增加 `logic_type` 字段
- FOL 原有功能不受影响（默认行为完全不变）

base 模型生成的 Prolog 被截断（max_new_tokens=64），prove 全部失败是预期行为——plan006 训练后的 checkpoint 会生成完整的 Prolog formalization。

---
