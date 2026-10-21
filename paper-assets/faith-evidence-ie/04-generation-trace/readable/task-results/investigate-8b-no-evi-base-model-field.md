# investigate 8b no evi base model field

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_8b_no_evi_base_model_field_20260517T143505_result.json`
- **Structured JSON:** [`db0eead018d9054a9050.json`](../../sessions/db/db0eead018d9054a9050.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

代码逻辑清晰，关键在第 404-410 行：

```python
adapter_config = Path(args.model_path) / "adapter_config.json"
if adapter_config.exists():
    base_model_path = args.base_model
    adapter_path = args.model_path
else:
    base_model_path = args.model_path  # ← 完整模型时，直接用 model_path
    adapter_path = None                # ← adapter 不加载
```

**1. base_model 在 model_path 为完整模型时被完全忽略。** 当 `model_path` 目录下不存在 `adapter_config.json`（即为完整模型），代码将 `base_model_path = args.model_path`，`adapter_path = None`。`args.base_model` 不参与任何加载逻辑。

**2. metrics.json 中的 base_model 是参数记录，不是实际使用记录。** `metrics["config"] = vars(args)` 直接序列化所有命令行参数原始值，包括未被使用的 `--base_model` 默认值 `/root/autodl-tmp/models/Qwen3-4B`。

**3. 8B no-evidence eval 结果可信。** 实际加载的模型是 `--model_path` 指定的 8B 模型，metrics.json 中 `base_model` 显示 Qwen3-4B 只是默认参数值被记录，不影响推理。

---
