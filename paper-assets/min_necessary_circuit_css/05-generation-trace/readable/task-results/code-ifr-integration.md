# code ifr integration

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ifr-integration_20260512T112315_result.json`
- **Structured JSON:** [`db8c9d2821092f849da2.json`](../../sessions/db/db8c9d2821092f849da2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。创建了以下内容：

- **`ifr_discovery.py`** — 基于 ALTI 的 IFR circuit discovery，使用 `run_with_cache` 缓存 residual stream activations，对每对 (source, destination) 计算 proximity score `max(||x_v||₁ - ||y_u - x_v||₁, 0)`。Source 粒度到 per-head（不同 head 输出不同 → 不同 score），destination 粒度到 per-layer（同层所有 head 共享 `resid_pre` → Q/K/V edges 同分）。通过 `names_filter` 只缓存必要的 hook points 以控制显存。
- **`css.py`** — `binarize_scores` 新增 `method="ifr"` 分支，使用 top-N 策略（与 EAP-IG 相同）
- **`config.py`** — 新增 `LargeModelConfig(MVPConfig)`: methods=`["eap_ig", "edge_pruning", "ifr"]`, 默认 Qwen2.5-0.5B, `num_samples=50`
- **`circuit_discovery.py`** — `_NORMALIZERS` 和 `run_all_methods` 注册了 IFR

---
