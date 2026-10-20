# infra qwen vllm deploy

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen-vllm-deploy_20260514T103741_result.json`
- **Structured JSON:** [`d32f5fcf337a877d64b3.json`](../../sessions/d3/d32f5fcf337a877d64b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

## Qwen2.5-14B vLLM 部署 + Dry-run 报告

### 部署
- **Qwen vLLM**: cuda:2+3, port 8002, PID 41276, TP=2, max-model-len 4096
- **DeepSeek vLLM**: 未受影响，cuda:0+1, port 8001
- **mvp_003**: 正常运行中 (9/50)

### Dry-run 结果 (3 ProofWriter depth-5 × 4 chains)

| 验证项 | 结果 | 状态 |
|--------|------|------|
| Chain 格式兼容性 | 12/12 chains 采样成功，答案提取正常 | **通过** |
| Premise formalization | 56/56 (100%) | **通过** |
| Claim formalization rate | 77/178 = 43.26% (threshold 50%) | **未达标** |
| Z3 sandbox 稳定性 | 无 crash，正确检测 SAT 与 inconsistency | **通过** |
| Cost | 408 calls, 285K tokens, $0.00 (本地 vLLM) | - |

### 关键问题
Formalization rate (43.26%) 低于 50% 目标。原因是 Qwen2.5-14B 同时承担 chain generation 和 formalization 两个角色，formalization 能力弱于 mvp_003 使用的远程 DeepSeek-V3.2。正式实验建议 formalization 仍走更强的模型 API。

---
