# infra exp 050b icl fix deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp-050b-icl-fix-deploy_20260518T213215_result.json`
- **Structured JSON:** [`3eb6858a871c2f47c919.json`](../../sessions/3e/3eb6858a871c2f47c919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验确认正在运行：
- **0 个 400 错误**（overflow 问题已修复）
- 18 个 200 OK 请求已完成
- 正确排除 5 个 ICL 样本，评估 199 个 FOLIO 问题
- 所有请求正常通过

部署成功完成。总结：

| 项目 | 状态 |
|------|------|
| vLLM max-model-len | 16384 ✓ |
| 模型 | Mistral-7B-Instruct-v0.3 ✓ |
| GPU | cuda:2, 87961 MiB ✓ |
| port | 8002 ✓ |
| enforce-eager | ✓ |
| FLASHINFER_SAMPLER=0 | ✓ |
| 实验参数 | k=12, temp=0.7, max-tokens=4096, seed=42 ✓ |
| context overflow | 已修复（0 个 400 错误） |
| Registry | exp-050b-mistral-icl-oracle → RUNNING ✓ |
| tmux session | exp050b ✓ |

---
