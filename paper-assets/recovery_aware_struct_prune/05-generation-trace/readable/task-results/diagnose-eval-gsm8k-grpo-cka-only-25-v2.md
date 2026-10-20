# diagnose eval gsm8k grpo cka only 25 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_grpo_cka_only_25_v2_20260521T044916_result.json`
- **Structured JSON:** [`7d1bb4cd20776ba10bda.json`](../../sessions/7d/7d1bb4cd20776ba10bda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了。诊断结果如下：

---

## 诊断报告

### 失败根因

**`checkpoint-100` 子目录不存在。** 模型文件（`config.json`, `model.safetensors`, `tokenizer.json` 等）直接在 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/` 下，没有 `checkpoint-100` 子目录。

Transformers 找不到本地路径后，尝试将其解释为 HuggingFace repo ID，触发 `HFValidationError`：
```
OSError: Repo id must be in the form 'repo_name' or 'namespace/repo_name':
'/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/checkpoint-100'
```

崩溃位置：`src/eval_gsm8k.py:464` — `AutoTokenizer.from_pretrained(args.model_path)`

### checkpoint 路径

- `grpo_cka_only_25/checkpoint-100` → **不存在**
- `grpo_cka_only_25/` → **存在**，包含完整模型文件（`model.safetensors` 10.8GB, `config.json`, `tokenizer.json` 等）

GRPO 训练似乎将最终 checkpoint 直接导出/合并到了父目录，而非保留 `checkpoint-*` 子目录结构。

### 磁盘状态
- 根分区：5.1G/30G (17%) — 正常
- 数据盘：18G/879G (3%) — 正常

### GPU 状态
- 4× NVIDIA RTX PRO 6000 (96GB each)
- GPU 0/1/3 空闲可用
- GPU 2 被另一进程占用 (26.7GB, PID 320740)

### 修复命令

```bash
python src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 \
  --max_samples 1319 --seed 42
```

去掉路径末尾的 `/checkpoint-100` 即可。

---
