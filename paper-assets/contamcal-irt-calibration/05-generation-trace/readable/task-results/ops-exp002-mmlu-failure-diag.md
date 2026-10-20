# ops exp002 mmlu failure diag

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-mmlu-failure-diag_20260514T102538_result.json`
- **Structured JSON:** [`129365808087fd67345a.json`](../../sessions/12/129365808087fd67345a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因确认。**

`run_batch.py` 传给 `compute_signals.py` 的 `--model-path` 是：
```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42
```

但 `adapter_config.json` 在子目录：
```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/adapter_config.json
```

`signal_minkpp.py` 和 `signal_selfcritique.py` 的 `load_model_and_tokenizer` 检查 `os.path.join(model_path, "adapter_config.json")` —— 在顶层目录找不到，就走 `else` 分支尝试把它当全量模型加载。但该目录里根本没有模型权重文件（只有 `lora_adapter/` 和 `train_config.json`），所以 `AutoModelForCausalLM.from_pretrained()` 失败。

stderr 中的 transformers 模型架构列表是 `from_pretrained` 在抛错前打印的 "registered model types" 信息，真正的错误（如 `OSError: ... is not a local folder and is not a valid model identifier`）被截断了。

## 诊断总结

| 项目 | 详情 |
|------|------|
| **失败原因** | `--model-path` 指向 checkpoint 根目录，但 LoRA adapter 在 `lora_adapter/` 子目录 |
| **受影响任务** | 所有 9 个任务的 minkpp 和 selfcritique 信号（embedding 不加载模型所以不受影响） |
| **arc_challenge** | 正在跑（PID 347959），会遇到同样问题 |
| **gsm8k** | 已失败，同样原因 |

## 修复方案

`run_batch.py` 的 `checkpoint_path` 函数需要追加 `/lora_adapter`：

```python
def checkpoint_path(model_name: str, dosage: str) -> str:
    return f"{CHECKPOINT_ROOT}/{model_name}_{dosage}_{SEED}/lora_adapter"
```

或者修改 `signal_minkpp.py` / `signal_selfcritique.py` 的 `load_model_and_tokenizer`，在顶层找不到 `adapter_config.json` 时自动检查 `lora_adapter/` 子目录。

前者更直接。需要修复后重跑全部 9 个任务（embedding 结果可保留，加 skip 逻辑只重跑 minkpp + selfcritique 更高效）。

---
