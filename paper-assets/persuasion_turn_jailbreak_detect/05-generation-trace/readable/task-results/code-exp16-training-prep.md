# code exp16 training prep

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-training-prep_20260519T160522_result.json`
- **Structured JSON:** [`4acc972239d8cd723ac8.json`](../../sessions/4a/4acc972239d8cd723ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部创建并验证通过。

---

### 汇报

**脚本路径：**

| 脚本 | 路径 | 功能 |
|------|------|------|
| 数据合并 | `scripts/prepare_mixed_data.py` | 从 Qwen 取 125jb+125bn，Llama 取 125jb+125bn，归一化格式后 stratified split 为 350/74/76 |
| 批量训练 | `scripts/run_exp16_training.sh` | 9 个配置（3 variant × 3 seed），自动运行 Stage 1 + Stage 2 |
| 批量评估 | `scripts/eval_exp16.py` | 9 个 checkpoint × 7 个测试集，输出 summary table |

**数据格式差异（已在脚本中处理）：**
- Qwen user turns 有 `persuasion_strategy` 字段
- Llama jailbreak turns 用 `intended_strategy`（脚本重命名为 `persuasion_strategy`）
- Llama benign turns 无策略字段（脚本默认设为 0）
- 统一输出字段：`conversation_id`, `turns`, `label`, `source`(qwen/llama), `original_source`, `attack_type`

**MLM→classifier 兼容性修正：**
MLM 保存 HF `save_pretrained` 格式，classifier 的 treatment 模式期望 DeBERTaMultiTask `model.pt` — 不兼容。训练脚本中 MLM variant 改用 `--mode baseline --model_name {mlm_ckpt}` 通过 `AutoModel.from_pretrained` 加载。

**测试数据路径：**

| 测试集 | 路径 |
|--------|------|
| mixed_test (in-domain) | `data/mixed_llm/test.jsonl` |
| qwen_test | `data/plan_002_splits/test.jsonl` |
| dd_ood | `data/dd_ood_perturbed/perturbed.jsonl` |
| aa_ood | `data/actorattack_ood/actorattack_all.jsonl` |
| llama_dd | `data/cross_llm/dd_llama.jsonl` |
| llama_aa | `data/cross_llm/aa_llama.jsonl` |
| toxicchat | `data/mhj/toxicchat_plan002_eval.jsonl` |

**预估 GPU 时间（单 GPU）：**

| Variant | Stage 1 | Stage 2 (GRU) | 单 seed | 3 seeds |
|---------|---------|---------------|---------|---------|
| vanilla | — | ~10 min | ~10 min | ~30 min |
| MLM-only | ~12 min | ~10 min | ~22 min | ~66 min |
| 9-class | ~15 min | ~10 min | ~25 min | ~75 min |
| **总计** | | | | **~2.5–3h** |

---
