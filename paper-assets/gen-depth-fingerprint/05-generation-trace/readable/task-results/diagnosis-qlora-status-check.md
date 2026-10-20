# diagnosis qlora status check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_qlora_status_check_20260519T090046_result.json`
- **Structured JSON:** [`7346b4af6ac25c434254.json`](../../sessions/73/7346b4af6ac25c434254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**4 个 QLoRA 实验全部失败**，错误相同：`TypeError: expected str, bytes or os.PathLike object, not NoneType`

### 根因

Backbone 路径 `/root/autodl-tmp/models/qwen3-0.6b` 是 HuggingFace Hub cache 结构，实际模型文件在子目录：
```
/root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/
```

`AutoTokenizer.from_pretrained("/root/autodl-tmp/models/qwen3-0.6b")` 在顶层目录找不到 `vocab.json`/`tokenizer.json`，导致 `vocab_file=None`，触发 TypeError。

### 各实验状态

| 实验 | 状态 | 错误 |
|------|------|------|
| exp_055 (OLMo instruct) | **失败** | tokenizer 路径错误 |
| exp_056 (Qwen instruct) | **失败** | tokenizer 路径错误 |
| exp_055b (OLMo base) | **失败** | tokenizer 路径错误 |
| exp_056b (Qwen base) | **失败** | tokenizer 路径错误 |

GPU 全部空闲（4x RTX 5090, 0% 利用率, 0MiB 显存）。

### 修复方案

将 `--backbone` 路径改为实际模型目录：
```
/root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/
```

或在 `qlora_instruct.py` 第 227 行加一层路径探测逻辑。需要修复后重新启动全部 4 个实验。

---
