# code implement split softmax

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement_split_softmax_20260523T000457_result.json`
- **Structured JSON:** [`88572d733c4b87d78b9b.json`](../../sessions/88/88572d733c4b87d78b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：
- **语法检查**: 3 个文件全部 OK
- **Import 检查**: `SplitSoftmax` 和 `get_system_prompt_token_len` 导入正常
- **模块检测**: Qwen2 和 Llama 的 `eager_attention_forward` / `repeat_kv` 均存在
- **Tokenizer 集成**: system prompt 长度计算正确（11 tokens for "You are a helpful assistant."）
- **Module-level patching**: patch 和 restore 均工作正常
- **数学验证**: rescaling 后 attention weights 总和仍为 1.0，sp_scale=1.4142（k=0.5 时放大系统 prompt 注意力），conv_scale=0.5858（衰减会话 token 注意力）

### 创建的文件

1. **`src/split_softmax.py`** — `SplitSoftmax` 类，通过 monkey-patch `eager_attention_forward` 实现 post-softmax rescaling（无需复制完整 forward）
2. **`src/eval_split_softmax.py`** — 评估脚本，支持 `--mode tf/gen`、`--k-values` 扫描、与 attention_steering 输出格式一致
3. **`scripts/d048_split_softmax_eval.sh`** — TF+Gen 评估，扫 k={0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0}，base model 和 TG s42 v7 checkpoint 各一组

---
