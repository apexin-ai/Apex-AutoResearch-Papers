# infra transfer nli model to westd28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_transfer-nli-model-to-westd28034_20260518T183536_result.json`
- **Structured JSON:** [`dbe20a6af8d39343da52.json`](../../sessions/db/dbe20a6af8d39343da52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**1. 模型传输 — 无需传输**

`cross-encoder/nli-deberta-v3-base` 已完整缓存在 westd-28034 上：
- 路径: `/root/.cache/huggingface/hub/models--cross-encoder--nli-deberta-v3-base/`
- 7 个 blob 文件大小与 westd-29046 完全一致（含 737MB model.safetensors）
- refs/main → `6c749ce3425cd33b46d187e45b92bbf96ee12ec7`，symlinks 正确

**2. 离线加载验证 — 通过**

`HF_HUB_OFFLINE=1` 模式下 Tokenizer 和 Model 均加载成功。

**3. exp-008 tmux 状态 — 已退出**

`exp-008` session 存在但当前只有一个空闲 bash shell（PID 41744），原始进程已崩溃退出，scrollback 为空。**需要重新提交 exp-008。**

---
