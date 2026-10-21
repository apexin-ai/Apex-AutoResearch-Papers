# code fix inference sft adapter guard

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-inference-sft-adapter-guard_20260515T214544_result.json`
- **Structured JSON:** [`382a98cad2c2ad2dca51.json`](../../sessions/38/382a98cad2c2ad2dca51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器上没有 git 仓库，无法执行 git commit + push。

**已完成的工作：**

修改已直接在服务器上生效。Diff（第 297-305 行，新增）：

```python
    if adapter_config.exists() and args.sft_adapter is None:
        raise ValueError(
            f"model_path '{args.model_path}' is a LoRA adapter (adapter_config.json found), "
            f"but --sft_adapter is not set. RSFT/DPO/GRPO adapters are trained on SFT-merged "
            f"model and MUST be evaluated with --sft_adapter pointing to the SFT adapter directory. "
            f"Add: --sft_adapter /path/to/sft_output"
        )
```

插入位置：adapter 检测块（L288-295）之后、`load_model_and_tokenizer` 调用（L306）之前。

**验证结果：**
- `py_compile` 语法检查通过
- 用 `--model_path /root/autodl-tmp/rsft_output`（含 `adapter_config.json`）且不传 `--sft_adapter` 触发测试 → 正确抛出 `ValueError`

**Git commit + push 无法执行** — `/root/autodl-tmp/freige` 不是 git 仓库。如需版本控制，需要先 `git init` 或将代码关联到远程 repo。

---
