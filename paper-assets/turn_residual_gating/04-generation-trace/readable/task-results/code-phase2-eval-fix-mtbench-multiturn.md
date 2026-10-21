# code phase2 eval fix mtbench multiturn

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_eval_fix_mtbench_multiturn_20260518T062802_result.json`
- **Structured JSON:** [`dad286f233b081315c03.json`](../../sessions/da/dad286f233b081315c03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改/新建了 3 个文件，均已部署到服务器并同步到本地 artifacts：

**修复 1: `eval_phase2_mtbench.py`** — 训练模型现在通过 `load_model_with_gates()` 加载，生成时激活 LoRA + gate hooks + turn features。之前只加载了 LoRA，MT-Bench 评分无法反映 ThreadGate 效果。

**新建: `model_loader.py`** — 共享模块，核心组件：
- `load_gates()` / `register_gating_hooks()` — 与 eval_phase2_gar.py 逻辑一致
- `TurnFeaturesTracker` — 处理自回归生成时 KV cache 下的 turn features：prefill 阶段返回完整序列特征，decode 阶段逐 token 返回并通过 last-layer 触发位置递增
- `load_model_with_gates()` → 返回 `(model, tokenizer, GateContext)`，调用 `gate_ctx.prepare_generation()` 即可在 `model.generate()` 中启用 gating

**新建: `eval_phase2_multiturn.py`** — 5 个场景 × 8 turns，rule-based 评分：
- format_constraint（恰好 3 bullet points）
- ending_constraint（以 "END OF RESPONSE" 结尾）
- role_constraint（pirate 关键词检测）
- prohibition_constraint（禁止 "however"）
- topic_constraint（必须提及 climate 相关词）
- 输出 `instruction_retention_ratio = late_accuracy / early_accuracy`

---
