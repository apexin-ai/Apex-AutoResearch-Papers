# code plan003 local inference infra

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003_local_inference_infra_20260520T134426_result.json`
- **Structured JSON:** [`78a3c433f617b598b994.json`](../../sessions/78/78a3c433f617b598b994.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。产出 3 个文件：

| 文件 | 说明 |
|------|------|
| `artifacts/scripts/serve_qwen3.sh` | vLLM serving，支持 `8b`/`32b`/`both` 模式，含 health check polling（5min 超时） |
| `artifacts/scripts/download_models.sh` | AutoDL 环境模型下载，HF CLI 优先，速度 <500KB/s 自动 fallback ModelScope，已有模型跳过 |
| `artifacts/local_model_client.py` | Phase 1 + Phase 2 pipeline，复用 `harness.run_episode` / `judge.judge_episode`，通过注入 per-model `AsyncOpenAI` client（不同 port）实现路由，cross-judge 8B↔32B-AWQ |

核心设计：`local_model_client.py` 在每个 model 循环开始时将 `harness._client` / `judge._client` 替换为指向对应 vLLM port 的 `AsyncOpenAI` 实例，复用现有 episode/judge 逻辑，输出写入 `artifacts/local_study/`。

---
