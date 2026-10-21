# code prewrite reviewer scripts

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prewrite_reviewer_scripts_20260517T234542_result.json`
- **Structured JSON:** [`e0d7e17957ffd5b12708.json`](../../sessions/e0/e0d7e17957ffd5b12708.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写入并通过语法验证：

- `scripts/stronger_text_encoder_comparison.py` — 用 BGE-large-en-v1.5 (768d) 替代 MiniLM-L6，对 4 个模型跑 HS vs Text paired bootstrap，输出 precision diff + Holm-Bonferroni 校正
- `scripts/multi_split_robustness.py` — 5 个 random seed 划分，每个 split 独立跑 HS vs Text bootstrap，汇总全局 HB 校正 (5 splits × 4 models = 20 tests)

两者都使用 moving-average windowed features（与 `selectivity_corrected_layers.py` 一致），对 5120d 的 32B 模型 lbfgs 失败时 fallback 到 liblinear。

---
