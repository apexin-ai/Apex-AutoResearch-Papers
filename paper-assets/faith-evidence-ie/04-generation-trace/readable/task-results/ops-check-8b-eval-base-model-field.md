# ops check 8b eval base model field

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_8b_eval_base_model_field_20260516T131007_result.json`
- **Structured JSON:** [`a68ba20f64170a0497dc.json`](../../sessions/a6/a68ba20f64170a0497dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：`base_model` 字段不影响实际模型加载。Ign-F1=0.5079 确认来自 8B 模型。**

代码逻辑（`inference.py` 第 407-415 行）：

```python
adapter_config = Path(args.model_path) / "adapter_config.json"
if adapter_config.exists():
    base_model_path = args.base_model   # 只有 model_path 是 adapter 时才用 base_model
else:
    base_model_path = args.model_path   # 完整模型时直接用 model_path，忽略 base_model
```

本次 eval 的实际加载路径：
1. `model_path` = `/root/autodl-tmp/models/Qwen/Qwen3-8B`（完整模型目录，无 `adapter_config.json`）
2. 走 `else` 分支 → `base_model_path = args.model_path` = **Qwen3-8B**
3. `AutoModelForCausalLM.from_pretrained("Qwen3-8B")` → 加载 8B 基座
4. 然后合并 SFT adapter `/root/autodl-tmp/sft_output_qwen3_8b_no_evidence`

metrics.json 中的 `base_model: Qwen3-4B` 来源：argparse 的 `--base_model` 默认值（第 382 行硬编码为 Qwen3-4B），因为本次 eval 没有显式传 `--base_model`，所以记录了默认值。但这个值**从未被使用**——它只在 model_path 指向 adapter 时才会被读取。

`metrics["config"] = vars(args)` 把所有 argparse 参数（含未使用的默认值）原样写入 metrics.json，造成了误导。

---
