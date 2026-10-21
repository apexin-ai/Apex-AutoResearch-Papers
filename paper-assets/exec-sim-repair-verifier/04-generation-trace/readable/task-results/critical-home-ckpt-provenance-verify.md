# critical home ckpt provenance verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_home-ckpt-provenance-verify_20260514T203053_result.json`
- **Structured JSON:** [`7a2261595e32677f3b57.json`](../../sessions/7a/7a2261595e32677f3b57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有证据收集完毕。

---

## 溯源结果

### 1. checkpoint-3000 的 transformers 版本

**不是 4.57.6，是更新的版本（极可能是 5.8.0）**。

证据链：
- `training_args.bin` 中 `_transformers_version` 属性 **完全不存在**
- `__dict__` 包含 `trackio_bucket_id`、`trackio_static_space_id` 两个字段——在整个 transformers 4.57.6 包中 **零匹配**（grep 搜遍 `/home/sonny/.local/lib/python3.10/site-packages/transformers/`，无此字段）
- westd 当前安装的是 transformers 4.57.6（dist-info 日期 April 16），但 checkpoint 创建于 May 13——**训练环境与当前环境不一致**

### 2. checkpoint 来源

| 属性 | 值 |
|------|-----|
| `output_dir` | `/root/autodl-tmp/checkpoints_repo_cls_8b/` |
| `run_name` | `repo-cls-qwen3-8b-lora` |
| `base_model` | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` |
| PEFT | LoRA r=16, alpha=32, peft 0.19.1 |
| home 文件 mtime | 1778707807 |
| westd 文件 mtime | 1778707807（完全一致） |
| adapter_model.safetensors 大小 | 61,380,432 bytes（两端一致） |

Home 上的 checkpoint 是 westd 的**精确拷贝**（大小+mtime 均匹配）。训练在 AutoDL 环境下完成（路径含 `/root/autodl-tmp/`），westd 可能在训练后被重装/回滚了 transformers 版本。

### 3. 当前 eval 进程

GPU 上有一个 eval 在跑，但**不是**用的 8B checkpoint：

```
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-600 \
  --model_name Qwen/Qwen3-4B \
  --split val --max_seq_length 5120
```

这是 **4B 模型 seed123** 的 eval，与 8B ckpt-3000 无关。

### 4. 结论

**Reviewer 的怀疑成立。** Home 上 89.50% val eval 使用的 `checkpoints_repo_cls_8b_westd/checkpoint-3000` 确实是用 transformers 5.8.0（或其他 >4.57.6 版本）训练的。关键证据是 training_args 中存在 `trackio_bucket_id`/`trackio_static_space_id` 这两个 4.57.6 中根本不存在的字段。

**该 eval 结果不可信**，需要用 transformers 4.57.6 重新训练 checkpoint 后重新评估。

---
