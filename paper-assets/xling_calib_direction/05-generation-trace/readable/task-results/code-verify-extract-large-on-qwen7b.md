# code verify extract large on qwen7b

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_extract_large_on_qwen7b_20260520T214532_result.json`
- **Structured JSON:** [`1763da795c7c5427c3f4.json`](../../sessions/17/1763da795c7c5427c3f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 验证报告

| 项目 | 结果 |
|------|------|
| **1. 语法检查** | SYNTAX OK，`--help` 正常 |
| **2. Dry-run** | 成功。Hook 正常触发（"Layer access path: model.model.layers"），checkpoint 在 sample 5/10 各保存一次，6 个 .pt 文件全部生成 |
| **3. 格式兼容性** | 完全兼容。shape=(10, 3584)，dtype=float32，字段名 `activations`/`labels` 与原版一致 |
| **4. 数值对比** | Layer 0: max_diff=0, Layer 12: max_diff=0, **Layer 27: max_diff=441.4** |
| **5. 测试文件** | 已清理 |

### 发现的问题

**Layer 27（最后一层）数值不一致**：HuggingFace `output_hidden_states` 在最后一个位置返回的是经过 `model.model.norm()` (final LayerNorm) 的输出，而 hook 捕获的是 norm 之前的原始输出。已通过实验验证 `norm(hook_raw) vs hs[28]: max_diff=0.000000`。

**影响**：仅影响最后一层。前面和中间层完全一致（max_diff=0）。

**修复建议**：在 `extract_activations_large.py` 中，如果 `layer_idx == n_model_layers - 1`（最后一层），对 hook 输出额外应用 `model.model.norm`，以保持与原版输出的一致性。或者不修，因为原版的行为其实也不完全"纯粹"（最后一层混入了 norm），用 hook 版的 pre-norm 输出反而在语义上更一致（所有层都是 layer 的直接输出）。

**需要决策**：保持 pre-norm（hook 版当前行为，所有层语义统一）还是改为 post-norm（与原版一致）？

---
