# code d003 d004 code alignment

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d003-d004-code-alignment_20260515T130140_result.json`
- **Structured JSON:** [`4878a4911f5696799a79.json`](../../sessions/48/4878a4911f5696799a79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改已验证：

**train_probes.py**:
- L606-607: `save_results` 中 best_layer 严格用 `results[k]["per_task_mean_rho"]` 选择（去掉了 pooled fallback），加 D002 注释
- pooled ρ 仍计算并存为 `best_pooled_rho`

**analyze_results.py**:
- L121: 新增 `DINO_GATE_THRESHOLD = 0.554` 常量 (D004)
- L362-363: `delta_pass` 加入 `p_value_perm < 0.05` 条件 (D003)
- L376: 第三准则改为固定阈值 `vla_mean_rho >= 0.554` (D004)，不再动态比较 VLA vs DINO
- L397-403: 判定逻辑重写 — FAIL: rho_pass 或 delta_pass 不满足; PASS: 两者满足且 VLA ≥ 0.554; CONDITIONAL: 两者满足但 VLA < 0.554 (D003)
- L406-409: 效果量评估 — PASS 后若 VLA-DINO Δρ < 0.05 标记 `contribution_warning` (D004)
- 旧的 `subtask_auc_pass`/`third_criterion`/`vla_ge_dinov2` 键已移除（grep 返回空），subtask AUC 仅作为补充记录

**analyze_mvp_DEPRECATED.py**: 已有 DEPRECATED 标记和 `raise SystemExit`，无需改动。

---
