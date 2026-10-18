# diagnose eval pi05 random k07 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k07_long_seed42_strict_20260527T081917_result.json`
- **Structured JSON:** [`30fcc86b35305c0660c3.json`](../../sessions/30/30fcc86b35305c0660c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断与重跑总结

**失败原因**：cqa1-33015 无出站网络。`transformers` 的 `_patch_mistral_regex` 在初始化 `google/paligemma-3b-pt-224` tokenizer 时调用 `huggingface_hub.model_info()` 尝试连接 HF Hub，触发 `httpx.ConnectError: [Errno 99] Cannot assign requested address`。tokenizer 文件本身已缓存在 `/root/autodl-tmp/.hf_cache/hub/models--google--paligemma-3b-pt-224/` 中。

**修复**：在运行命令中添加 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，阻止所有网络调用。

**重跑状态**：
- exp_id: `eval_pi05_random_k07_long_seed42_strict_v2`
- 服务器: cqa1-33015, cuda:0 (空闲)
- PID: 109152, tmux session: `eval_pi05_random_k07_v2`
- 日志已开始写入，模型加载中（已成功跳过 tokenizer 网络调用阶段）
- Registry 已更新：原实验 `failure_reason` 已记录，新实验状态 RUNNING

---
