# analyze eval llama sft s43 no evidence r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_llama_sft_s43_no_evidence_r2_20260520T182543_result.json`
- **Structured JSON:** [`cec32b55bfdd45e60559.json`](../../sessions/ce/cec32b55bfdd45e60559.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

## eval_llama_sft_s43_no_evidence_r2 结果

| Metric | Value |
|--------|-------|
| **ign_f1** | **0.3391** |
| ign_precision | 0.4274 |
| ign_recall | 0.2811 |
| f1 | 0.3579 |
| precision | 0.4603 |
| recall | 0.2927 |
| evi_f1 / evi_f1_joint | 0.0 (no-evidence 模式，符合预期) |
| edcr | 0.0 |
| format_ok | 835/985 (84.8%) |
| truncated | 378/985 (38.4%) |
| n_predictions | 14,538 |
| n_documents | 985 |
| inference_time | 7,755s (~2h09m) |
| EXIT_CODE | 0 |
| no_evidence 参数 | true (已确认) |

## 跨 seed/setting 对比

| Experiment | ign_f1 | format_ok | truncated | 备注 |
|---|---|---|---|---|
| s42 SFT **with-evidence** (r3) | — | — | — | registry 未找到独立条目 |
| s43 SFT **with-evidence** (r3) | **0.5142** | — | — | |
| s44 SFT **with-evidence** (r3) | **0.4802** | 985/985 | 240 (24.4%) | |
| s42 SFT **no-evidence** (std_r2) | **0.5219** | 88.7% | 219 (22.2%) | |
| **s43 SFT no-evidence (r2, 本次)** | **0.3391** | 84.8% | 378 (38.4%) | |
| s44 SFT no-evidence | **0.3326** | 94.5% | 411 (41.7%) | 已知异常低 |

## 关键发现

1. **s43 no-evidence ign_f1=0.3391，与 s44 的 0.3326 同样异常低**，远低于 s42 的 0.5219（差距 -0.1828）。
2. **s43 evidence→no-evidence 降幅 = -0.1751（-34%）**，而 s42 的 no-evidence 反而比 s43/s44 的 with-evidence 还高。
3. **截断率 38.4% 偏高**（s42 仅 22.2%），但低于 s44 的 41.7%。截断与低 ign_f1 高度相关——s42 截断低→ign_f1 高，s43/s44 截断高→ign_f1 低。
4. **format_ok 84.8% 是三个 seed 中最低的**（s42: 88.7%, s44: 94.5%），说明 s43 模型在 no-evidence 格式上表现最差。
5. recall 极低（0.2811）是 ign_f1 低的主因——模型漏掉了大量关系，可能是因为截断导致后半段预测丢失。

---
