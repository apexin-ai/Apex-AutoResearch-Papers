# code eval parser symmetry fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-parser-symmetry-fix_20260513T004034_result.json`
- **Structured JSON:** [`5a0dfbd74c9b2cf46024.json`](../../sessions/5a/5a0dfbd74c9b2cf46024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两台服务器（home-1x5090, seetacloud-westd-4x5090）的文件完全一致，MD5 匹配，语法验证通过。

修改总结：

**`eval_repo_cwm.py`** — 3 处改动：
1. `parse_cwm_prediction` ambiguous 情况从 `return 0` 改为 `return -1`（L89）
2. `run_inference` 中增加 `-1 → majority_class` fallback 逻辑（L161-164），与 CLS 对称
3. summary JSON 增加 `n_cwm_unparseable` 字段（L315, L323）

**`eval_repo_cls.py`** — 3 处改动：
1. `run_inference` 中增加 `was_unparseable` 标记，写入 result dict（L153, L167）
2. `main()` 中 `n_unparseable` 计算从错误的 `gen_text == ""` 改为 `r.get("unparseable", False)`（L280）
3. summary JSON 增加 `n_cls_unparseable` 字段（L289）

两边 fallback 逻辑现在完全对称：parse 失败 → 返回 -1 → majority_class 替换 → 记录 unparseable 标记。

---
