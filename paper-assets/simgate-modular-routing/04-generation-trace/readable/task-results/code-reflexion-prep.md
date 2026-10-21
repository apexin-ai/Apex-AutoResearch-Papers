# code reflexion prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reflexion-prep_20260517T110425_result.json`
- **Structured JSON:** [`9abd9f11b4b08d9bf85d.json`](../../sessions/9a/9abd9f11b4b08d9bf85d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/reflexion_prep_report.md`。

**总结：**

- 服务器上**没有任何 Reflexion 相关代码**，需要从零实现
- 需要新增 1 个文件（`src/reflexion_baseline.py`，~200 行）、修改 1 个文件（`src/llm_agent.py`，~50 行新增）、1 个启动脚本
- 核心改造点：在 `run_episode_internal()` 外面套 trial loop，每次失败后用 LLM 生成 self-reflection，下一次 trial 注入 prompt
- 对照组设计：reflexion vs retry-only（纯重试无 reflection），隔离 reflection 的真实效果
- 当前 internal death rate 49%，目标降到 <20%。如果降不到，是有力的 negative result（支持 routing > self-correction 的论点）
- 预计实验时间 ~6-12 小时（单/双 GPU），等 72B scaling 实验完成后立即可启动

---
