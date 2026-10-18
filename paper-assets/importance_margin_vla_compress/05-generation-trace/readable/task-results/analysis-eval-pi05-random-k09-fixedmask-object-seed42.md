# analysis eval pi05 random k09 fixedmask object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k09_fixedmask_object_seed42_20260521T201008_result.json`
- **Structured JSON:** [`07060ba6b5d7d8decafe.json`](../../sessions/07/07060ba6b5d7d8decafe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**实验失败，无 eval 数据。**

**根因**：模型加载成功后，创建 preprocessor 时 `AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 尝试联网下载 tokenizer，但 AutoDL 网络未启用（未 `source /etc/network_turbo`），报 `[Errno 101] Network is unreachable`。0 个 episode 被执行。

**修复方案**：重跑前需要：
1. 启动网络加速：`source /etc/network_turbo`
2. 或者更好的方案：预下载 tokenizer 到本地路径，eval 脚本改用本地路径加载（避免 eval 依赖网络）

Registry 已更新为 DONE/failed。

---
