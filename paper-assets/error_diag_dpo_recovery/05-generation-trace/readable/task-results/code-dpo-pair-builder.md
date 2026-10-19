# code dpo pair builder

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-pair-builder_20260512T231039_result.json`
- **Structured JSON:** [`d32ce1c193996ac4ccd8.json`](../../sessions/d3/d32ce1c193996ac4ccd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部自测通过。验证 `build_dpo_pairs.py --help` 也已通过。

产出总结：

1. **`src/build_dpo_pairs.py`** — 更新：添加了 `--gamma` CLI 参数、输出增加 `gamma_e`/`task_type`/`metadata` 字段、summary 显示 γ_e 列
2. **`src/etadn_discount.py`** — 新建：`ETADNConfig` dataclass、`phi()`/`compute_discount_weights()`/`get_gamma_for_error_type()`、三种 DPO loss 变体（`uniform_dpo_loss`/`single_gamma_dpo_loss`/`etadn_dpo_loss`）、4 项自测全部通过

注：`dmpo_loss.py` 中已有 turn-level 的 `phi_weighted_logps` 用于 trainer 内部，`etadn_discount.py` 提供的是独立的 token-level DPO loss 接口，两者互补。

---
