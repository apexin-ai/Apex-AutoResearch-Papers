# research paper provenance check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-provenance-check_20260516T010247_result.json`
- **Structured JSON:** [`ea33f6a30c7361cb62ad.json`](../../sessions/ea/ea33f6a30c7361cb62ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册为 `art_20260516_ccbd50`。

**核心结论**：

- **Paper 数字一致性**: 全部 30+ 个关键数字与 registry 匹配，0 critical/0 warning。唯一一处 LLaMA count=16 Δ 四舍五入差异 (23.9 vs 24.0pp) 属于 cosmetic。
- **硬约束合规**: C001 (40-rel pool 描述) ✅、C002 (3.4× 仅基于 16/80) ✅、Claim 3 (SDGD 仅作 negative result) ✅
- **Provenance 缺口**: 31 个 DONE 实验中仅 8 个完全具备所有字段。23 个缺 `log_path`/`checkpoint_path`，其中分析类实验 (bootstrap CI, error taxonomy 等) 的 `checkpoint_path` 本身不适用。建议提交前至少补全论文直接引用的实验 (exp012_llama_fewrel_ch2, exp012_llama_8b_r2, exp_fewrel_formal) 的 `log_path`。
- **paper_checklist.yaml** 不存在，建议创建。

---
