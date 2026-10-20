# experiment llm judge strengthened followup

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llm-judge-strengthened-followup_20260515T023433_result.json`
- **Structured JSON:** [`4e2f96e79973cdd61c4c.json`](../../sessions/4e/4e2f96e79973cdd61c4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 进程状态
- **Claude few-shot/cot/few-shot-cot** (PID 215405) — 仍在运行，few-shot 已完成，正在跑 cot（8%）
- **GPT-5.5 zero-shot** (PID 216929) — 仍在运行，77% (1400/1824)
- **GPT-5-mini** — OpenRouter 不支持该模型，已杀掉

### 已有结果

| 变体 | macro_f1 | f1_stag | f1_prog | fails | cost | 状态 |
|------|---------|---------|---------|-------|------|------|
| Claude zero-shot (baseline) | 0.6625 | 0.6055 | 0.7195 | 0 | $11.66 | ✅ |
| **Claude few-shot** | **0.7514** | **0.6828** | **0.8199** | 0 | $36.08 | ✅ 完成 |
| Claude CoT | 0.6250 | 0.4500 | 0.8000 | 0 | $1.43 | 🔄 8% |
| Claude few-shot-cot | — | — | — | — | — | ⏳ 排队 |
| GPT-5.5 zero-shot | 0.7604* | 0.7348* | 0.7860* | 315 (22.5%) | $8.87 | 🔄 77% |
| GPT-5-mini | — | — | — | — | — | ❌ model_not_found |

\* 部分结果，最终可能有变化

### 关键发现
1. **Few-shot 显著提升 Claude**：macro_f1 从 0.6625→0.7514（+13.4%），但成本 3.1x
2. **GPT-5.5 macro_f1 略高**(0.7604)但 parse failure 率 22.5% — 有效覆盖低；呈"保守判断"模式（stag recall 0.94 vs prog recall 0.67）
3. 还有 3 个变体未完成（Claude CoT、few-shot-cot、GPT-5-mini），需等进程结束或重跑

---
