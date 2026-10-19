# code dmpo trainer

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dmpo-trainer_20260512T112303_result.json`
- **Structured JSON:** [`3578525bcfe31b25b976.json`](../../sessions/35/3578525bcfe31b25b976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。创建的文件：

| 文件 | 说明 |
|---|---|
| `src/dmpo_loss.py` | `compute_phi`, `compute_phi_weights`, `phi_weighted_logps` 三个核心函数 |
| `src/dmpo_trainer.py` | `ETADNTrainer(DPOTrainer)` — 重写 `_compute_loss`，用 `_aggregate_logps` 替换 token-sum 为 φ-weighted turn-level 聚合 |
| `src/tests/test_phi.py` | 33 个单元测试全部通过 |

关键实现细节：
- φ(0,T,γ) = 1.0 对所有 γ，Σφ > 1（不是概率分布）
- γ=1 特殊处理返回 1/T（设计选择），公式 L'Hôpital 极限实际是 (T-t)/T
- γ→0 时全部权重集中在第一个 turn
- `turn_ids` 和 `gamma` 在 `_non_model_keys` 中，不会传给 model forward
- dmpo/etadn 模式不支持 `precompute_ref_log_probs=True`（ref logps 需要同样的 φ 加权，运行时计算）
- `turn_ids` 对齐 `input_ids`，在 `_aggregate_logps` 中做 `[..., 1:]` shift 以匹配 `per_token_logps`

---
