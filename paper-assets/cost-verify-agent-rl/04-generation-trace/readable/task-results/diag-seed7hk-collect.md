# diag seed7hk collect

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_seed7hk_collect_20260523T230135_result.json`
- **Structured JSON:** [`7a3fc0bc76038584c76f.json`](../../sessions/7a/7a3fc0bc76038584c76f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**完成状态：Crash（第 1 轮即失败，后续 2 轮未执行）**

日志仅显示一次 `Starting: seed7hk-step5-fix, eval_seed=0`，没有 `ALL_DONE` 标记。

### 错误原因

```
ValueError: Unsupported model: /root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf
```

出错位置：`ctx_manager.py:35` 的 `get_special_tokens(tokenizer)` —— 该函数不识别 checkpoint 的 `tokenizer.name_or_path`（值为本地路径而非模型名）。

### 3 轮 success rate

无数据。seed=0 在 validation rollout 阶段 crash，seed=1 和 seed=2 未启动。

### 修复方向

`get_special_tokens()` 通过 `tokenizer.name_or_path` 匹配模型类型，但 HF 格式 checkpoint 的 `name_or_path` 是本地路径而非 `"Qwen/Qwen2.5-..."` 之类的标准名称。需要修改该函数，使其支持本地路径的 checkpoint（例如通过 tokenizer config 中的 `model_type` 或 vocab size 来判断模型类型）。

---
