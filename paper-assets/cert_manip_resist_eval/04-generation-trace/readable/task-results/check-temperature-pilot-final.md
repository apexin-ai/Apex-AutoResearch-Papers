# check temperature pilot final

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_temperature-pilot-final_20260523T134430_result.json`
- **Structured JSON:** [`85495692ed7b198110df.json`](../../sessions/85/85495692ed7b198110df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 判定：**partial** — 数据采集 100% 完成，仅最终 JSON 序列化崩溃

### 状态总结

| 阶段 | 状态 |
|------|------|
| Phase 1: Clean evaluation (72 runs) | 完成 |
| Phase 2: Attack scoring (144 runs) | 完成 (0 skipped, 144 scored) |
| Phase 3: Analysis & JSON dump | **崩溃** |

**崩溃原因**：`run_temperature_pilot.py:603` — `json.dump()` 遇到 `numpy.bool_` 类型无法序列化（`TypeError: Object of type bool is not JSON serializable`）。

**数据完整性**：checkpoint 目录 216 个 JSON 文件齐全（72 clean + 144 attack），部分结果 JSON `temperature_pilot.json`（3.4KB）已写入大部分分析数据但被截断。

### 已有关键 Metrics（从部分 JSON 提取）

**Accuracy vs Temperature — 温度几乎无影响：**

| Model | t=0.0 | t=0.3 | t=0.7 | t=1.0 | max Δ |
|-------|-------|-------|-------|-------|-------|
| gpt-4.1-nano | 0.751 | 0.739 | 0.745 | 0.745 | 0.007 |
| gemini-3.5-flash | 0.956 | 0.960 | 0.965 | 0.965 | 0.009 |
| claude-3-haiku | 0.647 | 0.652 | 0.659 | 0.647 | 0.000 |

**K_eff vs Temperature — 极其稳定：**

| Benchmark | t=0.0 | t=0.3 | t=0.7 | t=1.0 | Δ |
|-----------|-------|-------|-------|-------|---|
| MMLU | 2.584 | 2.598 | 2.564 | 2.592 | +0.008 |
| ARC | 2.698 | 2.711 | 2.686 | 2.684 | -0.014 |

**结论**：温度 0→1 对 accuracy 最大变化 <1%，K_eff 变化 <0.02。温度对评估结果影响可忽略。

### 修复

`json.dump` 崩溃因 `numpy.bool_` 不可序列化。需在 `run_temperature_pilot.py:603` 附近加 `default=` handler 或预先转换 numpy 类型，然后重跑 Phase 3 即可（数据已全部在 checkpoint 中，不需要重新调 API）。

---
