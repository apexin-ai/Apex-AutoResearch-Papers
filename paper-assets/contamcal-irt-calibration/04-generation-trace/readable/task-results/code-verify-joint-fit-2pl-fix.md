# code verify joint fit 2pl fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-joint-fit-2pl-fix_20260515T094757_result.json`
- **Structured JSON:** [`e9c0d8463a19964bc307.json`](../../sessions/e9/e9c0d8463a19964bc307.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 项修复已验证通过：

| # | 修复项 | 状态 |
|---|--------|------|
| 1 | L171: `extract_results(fit, y, model_type)` — 不再硬编码 `"4pl_gamma"` | **PASS** |
| 2 | L263-265: `--model-type` argparse 参数，含 4 个 choices | **PASS** |
| 3 | L281: `run_joint_fit()` 传入 `model_type=args.model_type` | **PASS** |
| 4 | L185-202: `has_cd` guard — 2PL 时跳过 `c`/`d` 提取，`p_clean` 用纯 logistic | **PASS** |

`--help` 输出正确显示 `--model-type {4pl_gamma,2pl_gamma,vanilla_4pl,4pl_gamma_wider}`。

无硬编码 `"4pl"` 残留问题（L5 注释、L131 默认值、L185 条件判断、L263-264 argparse 均为合理引用）。

无需补修，修复已完整持久化。

---
