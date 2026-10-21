# analysis compile paper tables 20260516

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile_paper_tables_20260516_20260516T123831_result.json`
- **Structured JSON:** [`cd8ecc70d75bc2d2c3f9.json`](../../sessions/cd/cd8ecc70d75bc2d2c3f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。6 张表已编译到 `artifacts/paper_results_tables.md` 并注册为 `art_20260516_382ed5`。

汇总:
- **Table 1**: 3 模型 × 2 数据集 zero-shot violation 全景，Mistral DR 最高（56–57%），Qwen/Llama 中等（13–26%）
- **Table 2**: Constrained decoding 在所有 6 组均大幅降低 DR（−8.25 至 −43.54 pp），R_F1 变化 ≤ ±1.18 pp
- **Table 3**: FT + OntoCoDec 组合，DR 降至 0.00–0.20%，|ΔR_F1| ≤ 0.51 pp
- **Table 4**: 消融显示 semantic layer 贡献主要 DR 降幅（Qwen −69%, Llama −41%），grammar layer 对 FT 模型几乎无效
- **Table 5**: Post-hoc filtering 在 5/6 ZS 组提升 R_F1，但 Mistral DocRED 的 73.7% 拒绝率导致 F1 下降；constrained decoding 优势在结构性保证
- **Table 6**: Schema prompt 降低 DR 31–62%，但残余 DR（5.78–12.84%）仍存在，R_F1 未在 Phase 0 实验中计算

---
