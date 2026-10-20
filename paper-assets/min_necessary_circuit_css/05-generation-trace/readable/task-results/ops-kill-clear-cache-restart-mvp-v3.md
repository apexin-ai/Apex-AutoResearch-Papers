# ops kill clear cache restart mvp v3

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_clear_cache_restart_mvp_v3_20260512T173459_result.json`
- **Structured JSON:** [`0f3290ad591c45d84bba.json`](../../sessions/0f/0f3290ad591c45d84bba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常运行中。汇报如下：

---

**执行结果汇报：**

1. **Kill 确认** — 旧进程 PID 275590 及 tmux session `mvp_pilot_gpt2_ioi` 已终止
2. **缓存删除确认** — 删除了 `cache_eap_ig.json` 和 `cache_edge_pruning.json`，确认无残留 cache 文件
3. **新 PID** — **279210**，tmux session: `mvp_pilot_gpt2_ioi_v3`，GPU: cuda:5
4. **日志确认** — 已从头计算，无 "Loading from cache" 字样：
   - Phase A (EAP-IG): 已完成，32491 edges scored，结果缓存到新 `cache_eap_ig.json`
   - Phase B (Edge Pruning): 正在运行，472/32491 edges，~24 it/s，预计 ~22 分钟完成

**额外修复**：首次启动因 HuggingFace 连接超时失败，加了 `HF_HUB_OFFLINE=1` 环境变量强制离线模式后正常启动（GPT-2 模型已在本地缓存）。

---
