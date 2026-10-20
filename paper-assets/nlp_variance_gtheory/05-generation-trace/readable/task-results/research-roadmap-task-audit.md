# research roadmap task audit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_roadmap_task_audit_20260522T113644_result.json`
- **Structured JSON:** [`84f7e1c4f5c1899f2b85.json`](../../sessions/84/84f7e1c4f5c1899f2b85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务清理结果

### 已完成（确认）

| 任务 | 证据 |
|------|------|
| Phase 1: 数据收集 | ROADMAP ✅ |
| Phase 2: Paper Agent 修订 + Reviewer 审查 | ROADMAP ✅, review_issues 17/17 resolved |
| exp-001 (4-model MMLU) | experiment_plan: done |
| exp-001b (item resampling) | experiment_plan: done |
| exp-002 (8×5 推理, 2.3M records) | D012 确认 40/40 完成 |
| exp003_scale_3b, exp003_scale_7b | registry: success |
| Round 4 全部修订 | review_issues.yaml: FR4-MF1~3, SF1~7 全部 resolved |

### 可立即推进（无外部依赖）

| 优先级 | 任务 | 预估工作量 | 说明 |
|--------|------|-----------|------|
| **P0** | Figure 3 标注修复 + "nearly double" 微调 | ~1h | 纯写作，Paper Agent 可直接执行 |
| **P0** | exp003_scale_72b 审批 + 启动推理 | ~0.5h + 2.5h GPU | PENDING 等待人工审批，模型下载状态需确认 |
| **P0** | exp-004 剩余分析项清理 | ~2-3h | 大量子分析已在 Round 4 修订中完成（bootstrap CI、LOMO、permutation test 等），需盘点哪些 (a)-(q) 尚未执行 |

### 阻塞中

| 任务 | 阻塞原因 |
|------|----------|
| Scale validation → Paper Agent patch | 等 exp003_scale_72b 完成 |
| Re-submit to ARR (continue mode) | 等 Figure 3 修复 + scale validation patch 全部完成 |
| exp-005 (14B scale) | P1, 需 ≥48GB 不同 GPU 类型，非投稿必需 |
| exp-006 (Fine-tuning G-study) | P1, 200 GPU·h，非投稿必需 |
| exp-007 (LayerCast) | P2，非投稿必需 |

### 需清理的异常

- **report.md 中 22 个 exp002_deepseek/internlm 子任务仍显示"准备中"**，但 D012 确认 8×5 已全部完成。这些是过时条目，应清理。
- **report.md 告警 "exp-002: 已被终止"** 与 D012 "40/40 完成" 矛盾，可能是注册表状态未同步。
- **exp-002 在 experiment_plan.yaml 仍标 "running"**，应更新为 done。

### 建议推进顺序

1. **Figure 3 标注修复**（最快闭环，无依赖）
2. **审批 exp003_scale_72b** → 确认 72B 模型下载状态 → 启动推理
3. **盘点 exp-004 剩余分析项**（许多已在 Round 4 中完成，避免重复劳动）
4. 全部完成后 → re-submit ARR

---
