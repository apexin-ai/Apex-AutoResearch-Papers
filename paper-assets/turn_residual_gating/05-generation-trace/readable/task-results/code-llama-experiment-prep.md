# code llama experiment prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_experiment_prep_20260520T183713_result.json`
- **Structured JSON:** [`90d8b984cc8d1e4b515e.json`](../../sessions/90/90d8b984cc8d1e4b515e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--model` 参数在 eval_phase2_gar.py 中正确用于 tokenizer 和模型加载。一切就绪。

---

## 汇报

### 1. Llama-3 模型状态：✅ 已缓存
- 路径：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- 4 个 safetensors 分片，总计 ~16GB，下载于 2026-05-19

### 2. 四个实验脚本就绪状态

| 实验 | 脚本 | 状态 |
|------|------|------|
| Plan_009: Phase 1 GAR 诊断 | `scripts/launch_llama_phase1_gar_diag.sh` | ✅ 就绪 |
| Plan_010: ThreadGate 训练 | `scripts/launch_llama_tg.sh` | ✅ 就绪 |
| Plan_011: LoRA-only 训练 | `scripts/launch_llama_lora.sh` | ✅ 就绪 |
| Plan_012: Eval | `scripts/launch_llama_eval.sh` | ✅ 已创建 |

### 3. 参数校验

**超参与 Qwen v7 完全一致**（对比 `launch_tg_s123.sh`）：
- `--gar-loss-mode mse_target`, `--gar-target 0.5`, `--lambda-gar 1.0`
- `--lambda-gate-div 1.0`, `--min-gate-std 0.05`, `--init-bias 1.5`
- `--gate-lr-multiplier 10`, `--max-seq-len 2048`, `--epochs 3`
- Seed 用 42（Qwen v7 用 123，有意区分）

**模型路径**：所有脚本均正确指向 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`

**数据路径**：`data/ultrachat_8k` 存在（~64MB）

**代码兼容性**：`train_phase2.py` 和 `eval_phase2_gar.py` 都支持 `--model` 参数覆盖默认 Qwen 路径，无需改代码。

### 4. 小问题（不影响运行）
- `launch_llama_lora.sh` 中 `--gate-type none` 但仍传了 `--init-bias 1.5 --gate-lr-multiplier 10` 等 gate 参数——无害，train_phase2.py 会忽略

### 5. 预估 GPU 时间
- Phase 1 GAR 诊断：~0.5-2h（纯推理，5 组对话 × 10 轮）
- ThreadGate 训练：~8h（3 epochs, 8k samples）
- LoRA-only 训练：~4h（无 gate 计算，更快）
- Eval：~1h（6 组评估）

**总计约 13-15h GPU 时间**，可串行执行（Phase 1 先跑确认 GAR 衰减存在，再启动训练）。

---
