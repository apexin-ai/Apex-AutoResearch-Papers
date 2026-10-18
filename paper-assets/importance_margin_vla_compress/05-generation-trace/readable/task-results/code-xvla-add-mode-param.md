# code xvla add mode param

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_xvla-add-mode-param_20260521T022105_result.json`
- **Structured JSON:** [`7f942e9c700e92411a19.json`](../../sessions/7f/7f942e9c700e92411a19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器文件内容一致，`--mode` 参数已就位（默认 `l2_norm`，choices `[l2_norm, random]`）。

修改总结：
- **`parse_args()`**: 添加 `--mode` 参数，默认 `l2_norm`，choices `["l2_norm", "random"]`
- **`install_vision_pruning()`**: 新增 `mode` 参数，`l2_norm` 走原有 topk 逻辑，`random` 用 `torch.randperm` 随机选 k 个 token 并 sort 保持位置顺序
- **`summary["mode"]`**: 从硬编码 `"l2_norm_prune"` 改为 `args.mode`，反映实际使用的模式
- 已部署到 cqa1-33015 和 westd-38929

---
