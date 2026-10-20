# infra exp055 deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp055-deploy_20260519T021752_result.json`
- **Structured JSON:** [`3842748de73a11c129b8.json`](../../sessions/38/3842748de73a11c129b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

**exp-055 Multi-Temperature Mistral-7B FOLIO-204 状态：**

| 项目 | 状态 |
|------|------|
| vLLM server | 运行中 (tmux: `exp055_vllm`, port 8002) |
| 实验进程 | 运行中 (tmux: `exp055_run`) |
| GPU cuda:2 | 87965/97887 MiB (90% utilization) |
| 模型 | Mistral-7B-Instruct-v0.3 |
| 配置 | T=0.3x4 + T=0.7x4 + T=1.2x4 = 12 traces/problem |
| 数据 | FOLIO 204 problems |
| Registry | RUNNING |

注意：因 `math500_subset.json` 和 `proofwriter_subset.json` 不存在，实际命令加了 `--math-data data/empty.json --pw-data data/empty.json`，仅跑 FOLIO 数据。

---
