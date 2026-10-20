# ops launch gpt2m s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_gpt2m_s43_fp32_20260521T051456_result.json`
- **Structured JSON:** [`ebbb72b2ce6d0e99ead8.json`](../../sessions/eb/ebbb72b2ce6d0e99ead8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功启动：

- 模型加载完成（292 weights, 瞬间完成）
- **cuda:1**: 90% utilization, 6031 MiB — Generation 0 (baseline) 训练中
- 配置: GPT-2-medium, seed=43, fp32, α=1.0, 10 generations × 5000 steps

之前阻塞原因是 HF Hub 网络请求（AutoDL 未开 network_turbo），加 `HF_HUB_OFFLINE=1` 后从本地缓存秒加载。

---
