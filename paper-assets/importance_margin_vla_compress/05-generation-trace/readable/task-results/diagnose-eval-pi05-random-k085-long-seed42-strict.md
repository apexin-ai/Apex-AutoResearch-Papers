# diagnose eval pi05 random k085 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_long_seed42_strict_20260527T030030_result.json`
- **Structured JSON:** [`57c4b676384d4c5375f3.json`](../../sessions/57/57c4b676384d4c5375f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

### Root Cause

**网络不可达** (`[Errno 101] Network is unreachable`)。脚本在初始化阶段加载 tokenizer 时，`transformers` 库尝试从 HuggingFace Hub 查询 `google/paligemma-3b-pt-224` 的 model_info（`is_base_mistral` 检查），但服务器没有外网访问。脚本在启动后 ~9 分钟就崩溃，根本没进入 eval 循环。

关键调用链：
```
main() → make_pre_post_processors() → from_pretrained() → AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224") → model_info() → HTTP GET → Network is unreachable
```

### 是否可直接重试

**不能直接重试。** 这不是 transient error——服务器本身没有外网。需要以下修复之一：

1. **设置 `HF_HUB_OFFLINE=1`**（推荐）：让 transformers 跳过所有网络请求，只用本地缓存。前提是 tokenizer 文件已在本地缓存中。启动命令改为：
   ```bash
   HF_HUB_OFFLINE=1 python -u eval_pi05_pruning_libero.py ...
   ```

2. **设置 `TRANSFORMERS_OFFLINE=1`**：效果类似，专门控制 transformers 库。

3. 如果 tokenizer 文件不在本地缓存，需要先在有网络的环境下载好，再拷贝过去。

### Success 条件确认

脚本使用的是 **strict** 条件（第 383 行）：
```python
if done:
    task_successes += 1
```
只检查 `done`，没有 `reward > 0.5` 的宽松条件。确认是 strict 版本。

---
