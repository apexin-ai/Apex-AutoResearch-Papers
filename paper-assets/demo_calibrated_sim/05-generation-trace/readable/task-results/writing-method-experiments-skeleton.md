# writing method experiments skeleton

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-experiments-skeleton_20260513T081507_result.json`
- **Structured JSON:** [`cc276b1c797ad6cc8045.json`](../../sessions/cc/cc276b1c797ad6cc8045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 section 骨架已完成并注册：

**§3 Method** (`artifacts/section_method_draft.md`)：
- §3.1 Task Environment — τ-bench retail, 16 tools, reward 定义
- §3.2 BCP — 6 variants 定义 + 选择 rationale，引用 seshadri2026lost/haq2026dialect
- §3.3 DPO Training — Fix B 细节、LoRA 配置表、三版 DPO 演进表（dpo-001→003 metrics）
- §3.4 Evaluation Protocol — H-gate 三假设、480 episodes scale、merged model serving（引用 diag-lora-merge bug）

**§4 Experiments** (`artifacts/section_experiments_draft.md`)：
- §4.1 Setup — Qwen-7B 配置 + Llama/Mistral 排除原因
- §4.2 FM1-FM3 — Table 1 全数据（mvp-004）、FM3 用 hgate-dpo003-merged 4-run 主证据，外部文献锚定
- §4.3 DPO+BCP Reversal — Table 2 聚合、方向反转对比表（gap -0.091→+0.064）、10/12 expansion、overcorrection amplification
- §4.4 Cross-Scale — Qwen-14B 占位符 Table 3
- §4.5 Analysis — completion 高方差、DPO quality 演进、vLLM LoRA bug、统计局限

所有数字均标注 exp_id 来源，Qwen-14B 结果用 `[PENDING: qwen14b-bcp-001]` 占位。

---
