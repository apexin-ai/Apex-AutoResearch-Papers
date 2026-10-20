# code llama scripts prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_scripts_prep_20260523T213358_result.json`
- **Structured JSON:** [`38281a35b2ba44c32043.json`](../../sessions/38/38281a35b2ba44c32043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，所有依赖路径已验证存在。

**脚本 1: `/root/turn_residual_gating/scripts/p1_llama_ss_train.sh`**
- Llama-3.1-8B + ThreadGate + scheduled sampling (ss-max-ratio=0.3)
- 超参与 Qwen SS (`d048_ss_s42.sh`) 完全一致
- 输出: `runs/p1_llama_ss_s42`

**脚本 2: `/root/turn_residual_gating/scripts/p2_llama_gradient_conflict.sh`**
- 对 Llama TG checkpoint (`runs/phase2_llama_tg_s42`) 做 NTP vs GAR 梯度冲突分析
- 10 samples, cosine similarity per gate layer
- 输出: `results/p2_llama_gradient_conflict/gradient_conflict_analysis.json`

**路径验证:**
- Llama 模型 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` ✓
- Llama TG checkpoint `gate_params.pt` + `lora/adapter_model.safetensors` ✓
- 数据集 `data/ultrachat_8k` ✓

---
