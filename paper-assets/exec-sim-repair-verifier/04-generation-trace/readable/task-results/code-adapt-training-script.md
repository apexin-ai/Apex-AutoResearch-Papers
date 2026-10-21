# code adapt training script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adapt-training-script_20260516T045559_result.json`
- **Structured JSON:** [`e18cd9ce2b738b3f68ed.json`](../../sessions/e1/e18cd9ce2b738b3f68ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件写好了：`train_unified.py`

**新模型 DeepSeek-Coder-6.7B-Instruct 的关键差异和注意事项：**

| 差异点 | Qwen3 | DeepSeek-Coder-6.7B-Instruct |
|--------|-------|------|
| Chat template 格式 | ChatML (`<\|im_start\|>...<\|im_end\|>`) | `### Instruction:\n...\n### Response:\n` |
| 特殊参数 | `enable_thinking=False` | 无 |
| EOS token | `<\|im_end\|>` / `<\|endoftext\|>` | `<\|EOT\|>` |
| LoRA target modules | q/k/v/o_proj | 同（LLaMA架构） |
| context length | 32K | 16K |

**脚本设计要点：**
1. `detect_model_family()` 根据模型名自动选择配置
2. `get_chat_template_kwargs()` 只给 Qwen3 传 `enable_thinking=False`
3. `_try_apply_chat_template()` 兼容不支持 system role 的模型（自动 merge 到 user message）
4. tokenizer/pad_token 处理对两者都安全
5. 训练启动时打印一条格式化后的 sample prompt 用于人工验证模板是否正确

**eval 脚本（`eval_cwm_baseline.py`）也有 Qwen 特有逻辑**（`<|im_end|>` 作为 stop token），如果要用 DeepSeek 评估需要同样适配。需要的话我可以接着改。

---
