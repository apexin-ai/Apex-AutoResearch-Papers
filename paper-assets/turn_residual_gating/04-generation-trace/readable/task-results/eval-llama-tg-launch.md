# eval llama tg launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama_tg_launch_20260520T200502_result.json`
- **Structured JSON:** [`be11e4a72e53e41a3f81.json`](../../sessions/be/be11e4a72e53e41a3f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载到 GPU（77GB/102GB VRAM），正在进行 gate 初始化和数据加载，训练步数即将开始记录。

---

## 总结

### Part 1: Llama Phase 1 GAR 诊断结果 ✓

| Turn | Avg GAR |
|------|---------|
| 1 | 0.0263 |
| 2 | 0.0183 |
| 3 | 0.0087 |
| 4 | 0.0055 |
| 5 | 0.0060 |
| 6 | 0.0035 |
| 7 | 0.0038 |
| 8 | 0.0037 |
| 9 | 0.0050 |
| 10 | 0.0026 |

- **T1→T10 decay: 90.1%**（Qwen 87.5%）— Llama 衰减更严重
- **T1→mid(3-8) drop: 80.2%** — PASS（阈值 ≥15%）
- 5 个 topic 一致表现：knowledge_qa, coding_help, creative_writing, math_reasoning, debate
- Registry: `llama_phase1_gar_diag` → **DONE (success)**

### Part 2: Chat Template 确认 ✓
- `turn_utils.py:9-10` 自动检测 `start_header_id` → `llama3` format
- 已有 `verify_llama_compat.py` 验证通过
- `train_phase2.py:46` 使用 `tokenizer.apply_chat_template()` — 无需手动指定

### Part 3: Llama TG 训练已提交 ✓
- **PID**: 199643
- **GPU**: NVIDIA RTX PRO 6000 Blackwell (102GB), 99% utilization
- **配置**: 与 Qwen v7 完全一致（threadgate, mse_target, gar_target=0.5, λ_gar=1, epochs=3）
- **Registry**: `llama_tg_training` → **RUNNING**
- **预估训练时间**: 4-8 小时（8B model, 8k samples × 3 epochs, seq_len 2048, single GPU Blackwell）

---
