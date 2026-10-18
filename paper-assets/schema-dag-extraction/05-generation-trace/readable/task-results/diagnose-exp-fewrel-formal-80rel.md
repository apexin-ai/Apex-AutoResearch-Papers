# diagnose exp fewrel formal 80rel

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_fewrel_formal_80rel_20260515T133657_result.json`
- **Structured JSON:** [`2b6d467c1aad0d2f6a9c.json`](../../sessions/2b/2b6d467c1aad0d2f6a9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**失败根因**：实验**未失败**。Python 脚本正常跑完，日志最后打印 `===== 80-rel ALL DONE =====`。EXIT_CODE=129 (SIGHUP) 来自外层 shell/tmux 在脚本结束后收到 HUP 信号（SSH 会话断开），不是 Python 进程被杀。

**完成度**：100%。exp1（8-rel × 25 random + high/low BCS）和 exp2（16-rel × 25 random + high/low BCS）全部跑完，产出文件完整：
- `predictions_exp1.json` (22MB), `eval_exp1.json`
- `predictions_exp2.json` (5.5MB), `eval_exp2.json`
- 预处理和配置文件齐全

**结论**：无需重跑，无需修复。所有结果已在 `/root/schema-dag-extraction/artifacts/fewrel_formal_full/`。EXIT_CODE=129 是误报——脚本本身返回 0，只是包裹它的 shell 被 SIGHUP 了。

---
