# fix grpo standard v3 dead resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grpo_standard_v3_dead_resubmit_20260519T205839_result.json`
- **Structured JSON:** [`00f0c11f532888ff3378.json`](../../sessions/00/00f0c11f532888ff3378.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**死因**: v3 在 `load_dataset("mbpp")` 时崩溃 — `RuntimeError: Cannot send a request, as the client has been closed.`，AutoDL 网络未启用代理导致 HF Hub HTTP 客户端断开。

**修复**: v4 启动前加 `source /etc/network_turbo` + SSL 证书环境变量 (`REQUESTS_CA_BUNDLE`, `SSL_CERT_FILE`) + `HF_HUB_DISABLE_XET=1`。

**v4 状态**:
- PID: **139816**
- tmux session: `eval_mbpp_grpo_standard_20_v4`
- GPU: cuda:2 (12497 MiB)
- 数据集加载成功 (374 problems)，推理已开始 (MBPP: 0%)
- Registry: RUNNING
- Cron 监控: 每 8 分钟检查，job `0438fd58`

---
