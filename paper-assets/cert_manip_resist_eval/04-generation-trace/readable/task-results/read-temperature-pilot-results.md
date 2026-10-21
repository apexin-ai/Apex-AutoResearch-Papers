# read temperature pilot results

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_temperature-pilot-results_20260523T091857_result.json`
- **Structured JSON:** [`d42f7b40b3ea87ab5580.json`](../../sessions/d4/d42f7b40b3ea87ab5580.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验仍在运行。当前状态：

**进度：7/72 clean steps 完成 (~9.7%)**
- 当前步骤：`[8/72] gpt-4.1-nano t=0.3 mmlu r=1`
- 已耗时：~1150 秒 (~19 分钟)
- 每步约 150-165 秒

**实验配置：**
- 3 模型 (gpt-4.1-nano, gemini-3.5-flash, claude-3-haiku) × 4 温度 (0.0, 0.3, 0.7, 1.0) × 2 数据集 (mmlu, arc_challenge) × 3 repeats = **72 clean steps**（每步 300 pairs）
- 之后还有 attack phase：3 模型 × 4 温度 × 2 数据集 × 6 attacks × 50 samples

**已完成的 checkpoint 文件：**
- `gpt-4.1-nano__mmlu__t0.0__clean__r0/r1/r2.json`
- `gpt-4.1-nano__arc_challenge__t0.0__clean__r0/r1/r2.json`
- `gpt-4.1-nano__mmlu__t0.3__clean__r0.json`

**预估剩余时间：**
- Clean phase 剩余 ~65 步 × ~160s ≈ **173 分钟**
- Attack phase 额外 144 组 × 50 samples（时间取决于每组耗时）
- 总计预估还需 **3-4 小时**

实验远未完成，之前预估的"~20 分钟"严重低估了（实际是 ~28,800 API calls，非 36K，且受 rate limiting 和 HTTP 502 重试影响）。结果文件会在实验完成后生成在 `artifacts/results/plan001/` 下。

---
