# ops check nomarker seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_nomarker_seed42_20260516T151515_result.json`
- **Structured JSON:** [`e91251096627b966799c.json`](../../sessions/e9/e91251096627b966799c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：崩溃（启动即失败）**

PID 281395 已不存在，无 checkpoint，无 eval_results。日志显示训练脚本在加载 tokenizer 时立即报错退出：

```
huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct'
```

**原因**：新版 `huggingface_hub` 的 `validate_repo_id` 不再接受本地绝对路径作为 `from_pretrained` 的参数。`/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct` 被当作 repo id 校验，因含 `/` 前缀而失败。

**修复方向**：在 `train/train_sft.py:148` 处，对本地路径走 `local_files_only=True` 或先用 `os.path.exists()` 判断是否为本地路径再传给 `from_pretrained`。更简单的做法是升级代码中加载逻辑，或降级 `huggingface_hub` 到兼容版本。

GPU 当前被 PID 279483 占用（36.5 GB），cuda:0 不空闲。

---
