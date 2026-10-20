# ssh 7b pipeline auto check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-pipeline-auto-check_20260520T002625_result.json`
- **Structured JSON:** [`bb3de56888c32ca59418.json`](../../sessions/bb/bb3de56888c32ca59418.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整信息已获取。

## 总结

### Pipeline 完整性

`run_fewnerd_qwen25_7b_pipeline.sh` 包含 5 个阶段：

| 阶段 | 脚本 | 状态 |
|------|------|------|
| Phase 1: QLoRA Training | `llamafactory-cli train` | ✅ 包含 |
| Phase 2: Export/Merge LoRA | `llamafactory-cli export` | ✅ 包含 |
| Phase 3: 3-seed N=8 Inference | `code/run_mvp_pilot.py` (seed 42/123/456) | ✅ 包含 |
| Phase 4: Signal Analysis | `code/analyze_fewnerd_results.py` | ✅ 包含 |
| Phase 5: Entity Construction | `code/wnut17_entity_construction.py` | ✅ 包含 |

### 缺少的步骤

Pipeline **不包含** ROADMAP "准备就绪的工具" 中列出的以下脚本：

- `artifacts/compute_signals.py` — 用的是 `analyze_fewnerd_results.py` 替代
- `artifacts/bootstrap_construction.py` — 用的是 `wnut17_entity_construction.py` 替代
- **`artifacts/format_for_scaling.py`** — **完全缺失**，pipeline 结束后需手动跑

也就是说 pipeline 完成后，signal 和 construction 会自动跑完，但 **format_for_scaling.py 需要手动触发** 才能生成 scaling curve 数据点。

### 7B 当前进度

- Step: **18283/20590** = **88.8%**
- Loss: 0.0066, eval_loss: 0.0385
- 速度: ~2.3s/it
- 剩余训练: ~2307 steps × 2.3s ≈ **1.5 小时**
- 训练完成后还有 export + 3-seed inference + signals + construction，预计额外 2-3 小时

---
