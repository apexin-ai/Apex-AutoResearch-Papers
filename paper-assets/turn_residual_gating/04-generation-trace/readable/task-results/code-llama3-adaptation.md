# code llama3 adaptation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama3_adaptation_20260519T155007_result.json`
- **Structured JSON:** [`1363cb389ada5b34a54c.json`](../../sessions/13/1363cb389ada5b34a54c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是总结：

---

## 架构差异清单：Qwen2.5-7B vs Llama-3.1-8B

| 特征 | Qwen2.5-7B | Llama-3.1-8B |
|------|-----------|-------------|
| hidden_size | 3584 | 4096 |
| num_hidden_layers | 28 | 32 |
| num_attention_heads | 28 | 32 |
| num_key_value_heads | 4 (GQA 7:1) | 8 (GQA 4:1) |
| intermediate_size | 18944 | 14336 |
| vocab_size | 152064 | 128256 |
| chat format | ChatML (`<\|im_start\|>`) | Llama3 (`<\|start_header_id\|>`) |
| pad_token | `<\|endoftext\|>` | None (需设为 eos) |
| 层路径 | `model.model.layers` | `model.model.layers` **（相同）** |
| attn projections | q/k/v/o_proj | q/k/v/o_proj **（相同）** |

**关键结论：现有代码几乎完全兼容 Llama-3，不需要 threadgate_llama.py。**

## 新增文件

| 文件 | 用途 |
|------|------|
| `src/config_llama.py` | Llama 模型路径配置 |
| `src/run_phase1_gar_llama.py` | Phase 1 GAR 诊断（原版 hardcoded Qwen 路径） |
| `src/verify_llama_compat.py` | 兼容性验证（已全部 PASS） |

## 无需修改的文件

- `threadgate.py` — hook 路径 `model.model.layers` 通用
- `gar.py` — attention 权重捕获通用
- `turn_utils.py` — 已内建 llama3 格式支持
- `train_phase2.py` — 通过 `--model` 参数切换
- `eval_phase2_gar.py` — 通过 `--model` 参数切换

## 启动命令模板

```bash
LLAMA=/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/
cd /root/turn_residual_gating/src

# Phase 1: GAR 诊断
python run_phase1_gar_llama.py --model $LLAMA

# TG 训练 (v7: MSE + gate_div)
python train_phase2.py \
  --model $LLAMA \
  --gate-type threadgate \
  --output-dir /root/turn_residual_gating/checkpoints/tg_llama_s42 \
  --gar-loss-mode mse_target --gar-target 0.3 \
  --lambda-gar 2.0 --lambda-gate-div 1.0 \
  --dry-run  # 先 dry-run 验证

# LoRA-only baseline
python train_phase2.py \
  --model $LLAMA \
  --gate-type none \
  --output-dir /root/turn_residual_gating/checkpoints/lora_llama_s42 \
  --dry-run

# Eval
python eval_phase2_gar.py \
  --model $LLAMA \
  --gate-type threadgate \
  --checkpoint-dir /root/turn_residual_gating/checkpoints/tg_llama_s42 \
  --baseline-results /root/turn_residual_gating/results/phase1_gar_results_llama.json \
  --gate-profile
```

---
