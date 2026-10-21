# infra exp052 053 westd16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp052-053-westd16639_20260519T000740_result.json`
- **Structured JSON:** [`76aa438cf30756279e3d.json`](../../sessions/76/76aa438cf30756279e3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无需部署 — exp-052 和 exp-053 已在 westd-16639 上正常运行。**

```
服务器确认: westd-16639 [是] (hostname: autodl-container-63d6438985-33e7e5f9)

exp-052 (cuda:2, seed=123):
  vLLM port 8002: OK (Mistral-7B, --enforce-eager)
  log 最后活动: 2026-05-19 08:08:30, 持续 200 OK 响应
  intermediates 文件数: 3
  GPU compute: 96%
  状态: SUCCESS ✓ — 已在运行

exp-053 (cuda:3, seed=456):
  vLLM port 8003: OK (Mistral-7B, --enforce-eager)
  log 最后活动: 2026-05-19 08:08:29, 持续 200 OK 响应
  intermediates 文件数: 3
  GPU compute: 96%
  状态: SUCCESS ✓ — 已在运行

tmux sessions:
  - exp032 (cuda:0, Qwen2.5-14B, ProofWriter)
  - exp033 (cuda:1, Qwen3-14B, ProofWriter)
  - seed-replication (cuda:2+3, 包含 exp052/053 的 vLLM + 实验进程)
```

`seed-replication` session 于 07:40 启动，已运行约 30 分钟，两个实验都在活跃处理 FOLIO 数据。不需要重复部署。

---
