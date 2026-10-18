# deploy westd27271 long 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_long_20260522_20260522T215021_result.json`
- **Structured JSON:** [`d73e5b87152b19a05a6f.json`](../../sessions/d7/d73e5b87152b19a05a6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。总结：

- **问题根因**：`make_pre_post_processors` 中的 tokenizer 加载尝试联网校验 HuggingFace（AutoDL 默认无代理），导致进程挂起
- **修复**：添加 `HF_HUB_OFFLINE=1` 强制使用本地缓存 + `source /etc/network_turbo` 作为备选
- **当前状态**：两个 π0.5 L2norm 实验在 westd-27271 上正常运行
  - GPU 0: k=0.3, seed42, libero_10 (Long), 50 episodes
  - GPU 1: k=0.5, seed43, libero_10 (Long), 50 episodes
  - 已通过首条 episode 验证，VRAM ~10.6GB，无错误

---
