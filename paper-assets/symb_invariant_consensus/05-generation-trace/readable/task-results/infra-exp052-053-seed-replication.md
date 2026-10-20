# infra exp052 053 seed replication

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp052-053-seed-replication_20260518T231815_result.json`
- **Structured JSON:** [`62bbcfbc1b254d79cb53.json`](../../sessions/62/62bbcfbc1b254d79cb53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | GPU | Seed | Port | tmux session | 状态 |
|------|-----|------|------|-------------|------|
| exp-052 | cuda:2 | 123 | 8002 | `exp052` | RUNNING, vLLM 已加载 (87952MiB) |
| exp-053 | cuda:3 | 456 | 8003 | `exp053` | RUNNING, vLLM 已加载 (87952MiB) |

两个 vLLM server 正在加载模型，命令中 `sleep 120` 后会自动启动 `run_full_mvp.py`。配置：K=12, temperature=0.7, max-tokens=4096, FOLIO-204, Mistral-7B-Instruct-v0.3，`VLLM_USE_FLASHINFER_SAMPLER=0` + `--enforce-eager`。Registry 已更新为 RUNNING。

---
