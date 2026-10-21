# code d024 gate revision

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d024-gate-revision_20260516T013251_result.json`
- **Structured JSON:** [`1e38de661947ee1a7b27.json`](../../sessions/1e/1e38de661947ee1a7b27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 修改总结

**analyze_gate.py**:
- `evaluate_gate()` 新增 `bypass: dict | None` 参数
- G3 不变 — 使用 standard eval 的 `eps0.0_pruneFalse` action_loss / baseline（决定 PASS/FAIL）
- 新增 G3a — bypass eval action_loss / baseline，仅在提供 `--bypass` 时出现，标注 `"Legacy metric. Distribution mismatch confound under gradient isolation."`，不影响 overall 判定
- 移除了无 perturbed conditions 时的 early-exit error（clean-only 数据仍能评估 G3/G3a）
- `main()` 新增 `--bypass` CLI 参数
- 报告标题更新为 `D015/D024`，verdict 下方注明 G3a 不影响 overall

**run_v8_final_eval.sh**:
- Phase 3 新增 `--bypass eval_results/eval_imm_v8_bypass_final.json`

**dry-run 结果**（v8 step 2000 数据）:
- `G3_action_loss_ratio`: 9.2893（standard / baseline，FAIL — 早期 checkpoint 预期）
- `G3a_bypass_ratio`: 14.3300（bypass / baseline，FAIL，仅供参考）
- G1/G2/G4: N/A（trajectory 数据无 perturbed conditions）
- 两个字段均正确出现在 JSON 和文本报告中

---
