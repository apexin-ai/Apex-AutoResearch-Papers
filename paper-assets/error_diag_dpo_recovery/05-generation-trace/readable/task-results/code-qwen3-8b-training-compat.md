# code qwen3 8b training compat

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3-8b-training-compat_20260513T095710_result.json`
- **Structured JSON:** [`c18325960955d2efb0bc.json`](../../sessions/c1/c18325960955d2efb0bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已返回。

## 汇报

### Step 1: 模型加载 + forward pass — 通过
| 项目 | 结果 |
|------|------|
| vocab_size | 151,643 |
| 参数量 | 8.2B |
| forward pass | logits shape `[1, 2, 151936]` |
| 状态 | ALL CHECKS PASSED |

模型用 float32 在 CPU 上加载成功，无 OOM。注意 `torch_dtype` 参数已 deprecated，新版应改用 `dtype`。

### Step 2: train_dpo.py 兼容性分析

脚本**没有 `--device` 参数**。只有 `--gpu`（int, default=0），内部硬编码 `device = torch.device(f"cuda:{args.gpu}")`。无法直接用 CPU 跑训练。

### Step 3: 1-step CPU 训练 — 跳过

train_dpo.py 不支持 CPU 模式，跳过。如需 CPU 验证训练流程，需要改代码把 device 逻辑改为可配置。

### Step 4: 数据文件

`/tmp/v9_early_pairs.jsonl` 存在，21 行。

### 兼容性问题总结
1. **模型本身与 transformers 兼容，加载和推理无问题**
2. **train_dpo.py 硬编码 CUDA**，无 CPU fallback — GPU 空闲后可直接跑，不需要改动
3. **logits 维度 151,936** 与 tokenizer vocab_size 151,643 有差异（模型 embedding 层做了 padding 到 64 的倍数），这是正常行为，不影响训练
4. `torch_dtype` deprecation warning — 建议后续改为 `dtype`，非阻塞

---
