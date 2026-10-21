# research vla model survey

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_model_survey_20260520T024303_result.json`
- **Structured JSON:** [`b848a67dc427e2346d26.json`](../../sessions/b8/b848a67dc427e2346d26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。调研了 18 个 VLA 模型，覆盖了所有候选 + 额外发现的 X-VLA、ECoT、LingBot-VLA。

**核心结论**：

大量模型（CogACT、LLARVA、TraceVLA、ECoT、OpenVLA-OFT）共享与 OpenVLA 相同的 2-layer MLP connector，无需重复测试。真正有新 connector 类型的模型只有几个：

**Top 5 推荐**：
1. **π0** — Linear projection connector，开源 + LIBERO 支持，与 MLP 形成最直接对比
2. **X-VLA** — Linear projection + soft prompts，LIBERO 98%，已有权重，0.9B 最小实验成本
3. **DeeR-VLA** — Perceiver Resampler (OpenFlamingo)，给失败的 RoboFlamingo 方案第二次机会
4. **RoboMM** — Cross-attention (decoder-side 融合)，与所有 projection-based connector 根本不同
5. **OpenVLA-OFT** — 同 connector 不同 action head，隔离 action generation 对压缩的影响

**可新增 connector 类型**：Linear projection（π0/X-VLA）和 Cross-attention（RoboMM/DeeR-VLA），加上已有的 Pixel-shuffle 和 MLP，可达 5 种 connector 覆盖。

结果已写入 `artifacts/vla_model_survey.md` 和 `memory.md`。

---
