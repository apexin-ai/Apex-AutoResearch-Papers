# research codebert feasibility

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_codebert_feasibility_20260516T044826_result.json`
- **Structured JSON:** [`1cc39fd20690b8e12aab.json`](../../sessions/1c/1cc39fd20690b8e12aab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 复用评估

- **train.py 可直接复用**: 基本可以，CLI 参数已支持 `--model-name` 和 `--max-seq-length`
- **需要修改的地方**:

| 文件 | 位置 | 问题 | 改动 |
|------|------|------|------|
| `contrastive_model.py` L93 | `target_modules=["q_proj", "v_proj"]` | Qwen 专用名称，CodeBERT (RoBERTa) 的 attention 层叫 `query`/`value` | 改为可配置参数，或按 model_type 自动选择 |
| `contrastive_model.py` L63 | `dtype=torch.float16` | 非标准 HF 参数（标准是 `torch_dtype`），Qwen 自定义代码接受但 RoBERTa 会忽略 → 模型以 fp32 加载 | 改为 `torch_dtype=torch.float16` |
| `contrastive_model.py` L61 | `_apply_lora` 签名 | LoRA target_modules 硬编码在方法内 | 增加 `lora_target_modules` 参数透传 |

- **改动量估计**: **小**（~15 行改动，集中在 `contrastive_model.py`）

## CodeBERT 配置

| 属性 | 值 |
|------|-----|
| Model | `microsoft/codebert-base` |
| Architecture | RobertaModel |
| Hidden size | 768 |
| Num layers | 12 |
| Max position | 514 |
| Vocab size | 50265 |
| LoRA target_modules | `["query", "value"]` |

## 训练时间估算

- 当前 GPU: 2× RTX PRO 6000 Blackwell (98GB)，当前已用 ~71GB/卡
- 剩余 VRAM: ~27GB/卡，**CodeBERT 绰绰有余**
- **VRAM 需求**: ~2-3GB（125M fp16 模型 + batch_size=8 × seq_len=512 的 activations）
- **单 run GPU 时间**: ~15-30 min（参数量 24x 少 + seq_length 4x 短，可大幅提高 batch_size 进一步加速）
- **3 strategies × 1 seed 总计**: ~1-1.5h
- 可与现有 Qwen 训练**并行**跑在同一张卡上（VRAM 充足）

## 关键风险

1. **LoRA target_modules 不匹配**（致命）— 当前硬编码 `q_proj`/`v_proj`，CodeBERT 用 `query`/`value`，不改会直接报错
2. **HuggingFace 不可达** — 服务器无法直接访问 huggingface.co，需要 `source /etc/network_turbo` 开代理或用 ModelScope 下载
3. **序列截断 512 vs 2048** — 训练数据按 2048 token 设计，CodeBERT 只支持 514，长上下文会被大幅截断，可能影响效果（这是架构级限制，不是 bug）
4. **`dtype` 参数兼容性**（非致命）— 模型会以 fp32 加载而非 fp16，Accelerator 的 mixed_precision 会处理但初始内存占用更大

---
