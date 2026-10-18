# write table3 integration d036

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_table3_integration_d036_20260516T023123_result.json`
- **Structured JSON:** [`5b827d2e790b961fdac8.json`](../../sessions/5b/5b827d2e790b961fdac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining "amplification" references are either about **merge amplification** (SDGD pipeline issue, different concept) or have already been rewritten to the new "stable sensitivity / wider range" framing. The conclusion in discussion.tex references "merge amplification" correctly.

---

**修改摘要**

**修改文件 (5个)**：
1. `docs/paper/results.tex`
2. `docs/paper/abstract.tex`
3. `docs/paper/introduction.tex`
4. `docs/paper/main.tex`
5. `artifacts/_project/paper/results.tex`

**关键叙事变化**：

| 旧叙事 | 新叙事 |
|--------|--------|
| BCS 效应随 pool 增大 **3.4× 放大** | BCS--accuracy slope **跨 pool 一致** (permutation p=0.436) |
| 31.2pp vs 9.1pp = amplification | 31.2pp vs 9.1pp = 80-rel pool 的 **BCS range 更宽** (0.46–0.68 vs 0.65–0.90) |
| Extreme-batch Δ 作为 Panel B | **Quartile Δ** 作为辅助列（-7.42pp, -3.92pp, +0.35pp） |

**Table `within_pool` 重构**：
- 合并为单表：左侧 Regression（slope/CI/r/p），右侧 Quartile Δ（Δ/CI）
- 底部注脚：Permutation test p=0.436
- Caption 明确说明 80-rel (n=25) underpowered、80-pool quartile Δ CI 跨零原因（BCS range 窄）

**具体行变更**：
- `results.tex:18` — figure caption 去掉 "3.4× amplification"，改为 slope consistency + wider range
- `results.tex:88-91` — 去掉 amplification 解释，改为 per-unit sensitivity 一致 + range 差异
- `results.tex:92-122` — 重写 within-pool 段落和表格
- `abstract.tex:2` — "amplify 3.4×" → "slope consistent (permutation p=0.44), wider range → larger gaps"
- `introduction.tex:12,18` — findings/contributions 中同步更新
- `main.tex:42-44` — limitations 从 "amplification uncertainty" 改为 "cross-pool slope consistency"
- `main.tex:157` — appendix factorial 段落同步更新

---
