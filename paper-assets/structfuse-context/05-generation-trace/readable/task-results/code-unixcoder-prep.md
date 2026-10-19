# code unixcoder prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unixcoder_prep_20260516T053732_result.json`
- **Structured JSON:** [`e44c24ebe7b2260d27cd.json`](../../sessions/e4/e44c24ebe7b2260d27cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**修改内容：**

1. **`contrastive_model.py`**:
   - `__init__` 新增 `lora_target_modules: list[str] | None = None` 参数
   - `_apply_lora` ��增 auto-detect 逻辑：RoBERTa/UniXcoder → `["query", "value"]`，Qwen/StarCoder → `["q_proj", "v_proj"]`
   - `dtype=torch.float16` 保持不变（当前 transformers 版本中 `dtype` 是正确参数名，`torch_dtype` 反而 deprecated）

2. **`train.py`**:
   - `parse_args()` 添加 `--lora-target-modules` 参数（`nargs="*"`, 默认 None = auto-detect）
   - `StructFuseEncoder` 实例化时传入 `lora_target_modules=args.lora_target_modules`

3. **UniXcoder 模型下载**: `microsoft/unixcoder-base` 已缓存到 `/root/autodl-tmp/.hf_cache`（125.9M params）

**验证结果：**
- UniXcoder + LoRA 加载成功，trainable params = 1.38M
- LoRA 正确应用到 `encoder.layer.*.attention.self.query/value`
- 现有 Qwen 逻辑未受影响（auto-detect 按 `model_type` 分流）

---
