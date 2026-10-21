# diag westd eval accuracy issue

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-eval-accuracy-issue_20260515T183951_result.json`
- **Structured JSON:** [`155fbf3213c76fbf7ca6.json`](../../sessions/15/155fbf3213c76fbf7ca6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因确认：westd 使用了错误版本的 eval 脚本，不包含 chat template。**

### 关键差异对比

| | westb eval | westd eval |
|---|---|---|
| **Prompt 构造** | `tokenizer.apply_chat_template(messages)` → `<｜User｜>q<｜Assistant｜>` | 纯文本: `"Solve...Put your final answer in \boxed{}.\n\nQuestion: {q}\n\nAnswer:"` |
| **与 SFT 训练格式匹配** | 匹配（SFT 使用 chat template） | **不匹配** |
| **EOS rate** | 0.99 | ≈0（几乎所有 sample 生成到 4096 tokens 才停） |
| **Avg gen len** | ~180 tokens | ~4096 tokens |
| **准确率** | 57%/64% | 2.5%/0% |

### 因果链

1. SFT 训练使用 chat template 格式（`<｜User｜>...<｜Assistant｜>...`）
2. westd eval 脚本（`/root/autodl-tmp/recovery_aware_struct_prune/src/eval_gsm8k.py`）是一个简化版本，不使用 `apply_chat_template`，直接用纯文本 prompt
3. 模型收到不认识的 prompt 格式 → 不知道何时停止 → 生成到 max_new_tokens (4096)
4. 4096 tokens 的退化输出中 answer extraction 几乎无法提取正确答案

### 建议

1. **Kill 当前 eval 进程**（PID 55353, 55286）— 结果无意义
2. **将 westb 的 eval_gsm8k.py 同步到 westd** — 即 `/root/recovery_aware_struct_prune/src/eval_gsm8k.py` → `/root/autodl-tmp/recovery_aware_struct_prune/src/eval_gsm8k.py`
3. **重跑 eval**，使用正确脚本

需要我执行修复操作吗？

---
