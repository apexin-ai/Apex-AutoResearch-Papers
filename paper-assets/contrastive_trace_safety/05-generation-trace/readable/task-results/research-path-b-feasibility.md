# research path b feasibility

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_path_b_feasibility_20260517T055940_result.json`
- **Structured JSON:** [`596960ee6f6455fee1da.json`](../../sessions/59/596960ee6f6455fee1da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/path_b_feasibility/report.md`

核心结论:

**可行，预计 1.5 天完成。** 主要发现:

1. **HarmThoughts 数据集已耗尽** — R1-32B 的 100 条和 QwQ 的 95 条 jailbreak+CP traces 是数据集上限，扩展必须自行生成
2. **硬件充裕** — 2× RTX PRO 6000 Blackwell (98GB)，32B fp16 只需 64GB，可双卡并行生成
3. **Prompts 充足** — 695/776 个未用过的 jailbreak queries 可用
4. **关键瓶颈是 Annotation** — 需要对 ~15000 新 sentences 标注 16 类安全标签。推荐用 LLM API (Claude) 标注 + 抽检，备选方案是用现有 8525 条标注数据训练本地分类器
5. **时间线**: 生成 ~1.5h, Annotation 2-4h, 提取 <20min, 余量充足

---
