# code gpt2 factual recall fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2-factual-recall-fix_20260513T084751_result.json`
- **Structured JSON:** [`58b8c02f294efeebee6d.json`](../../sessions/58/58b8c02f294efeebee6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交。

**修复总结：**

- **Bug**：`run_factual_recall.py` L400/L407 直接传 `(model2, dl2, factual_recall_metric, config)` 给 `run_edge_pruning` / `run_acdc`，但这两个函数签名是 `(ac_task, config)` —— 需要 auto_circuit 的 `PatchableModel` + `PromptDataLoader`
- **Fix**：新增 `_build_ac_task()` 辅助函数（L304），将 TransformerLens 模型包装为 `PatchableModel`，将 `FactualRecallDataset` 转为 auto_circuit 的 `PromptDataset` + `PromptDataLoader`
- **验证**：Edge Pruning dry-run 通过（32491 edges scored），ACDC 运行正常（进度条推进中）
- **EAP-IG 缓存**：`cache_eap_ig_fr.json` 存在，可复用
- **实验**：`gpt2_factual_recall_k3_v2` 已注册并提交到 westd-pro6000 cuda:1，日志在 `~/runs/min_necessary_circuit_css/gpt2_factual_recall_k3_v2.log`

---
