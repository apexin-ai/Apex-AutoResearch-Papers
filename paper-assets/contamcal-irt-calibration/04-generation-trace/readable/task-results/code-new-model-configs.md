# code new model configs

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_new-model-configs_20260518T083612_result.json`
- **Structured JSON:** [`293040502b57a7e80b80.json`](../../sessions/29/293040502b57a7e80b80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 代码修改 (`exp001/train_sft.py`)
1. **L21**: 添加 `AutoConfig` import
2. **L74-79**: 新增 `CHATML_TEMPLATE`（ChatML 格式），用于无 chat_template 的 base 模型（OLMo-2 等）
3. **L81-83**: 新增 `MODEL_TARGET_MODULES` 映射，Phi3 架构使用 `qkv_proj, o_proj, gate_up_proj, down_proj`
4. **L159**: chat_template fallback 从 `raise ValueError` 改为自动注入 ChatML 模板
5. **L185-187**: LoRA `target_modules` 改为按 `model_type` 自动选择，未知架构回退到默认 7 模块

### 配置脚本
- `exp001/configs/run_phi4_example.sh` — bs=1, grad_accum=16（~55GB VRAM）
- `exp001/configs/run_olmo2_7b_example.sh` — bs=2, grad_accum=8（~25GB VRAM）

### 兼容性
| 模型 | LoRA target_modules | chat_template | 状态 |
|------|-------------------|---------------|------|
| Phi-4 (phi3) | `qkv_proj, o_proj, gate_up_proj, down_proj` | 内置（ChatML 变体） | 就绪 |
| OLMo-2-7B (olmo2) | 默认 7 模块（完全匹配） | 自动注入 ChatML | 就绪 |

### 待办
- 两个模型的权重文件未完全下载（phi-4 缺 safetensors 分片，OLMo-2 仅有 1/6），训练前需补全下载

---
