# review paper draft r1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper-draft-r1_20260514T230848_result.json`
- **Structured JSON:** [`4d4976154f2f731ddf6d.json`](../../sessions/4d/4d4976154f2f731ddf6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告已写入 `artifacts/paper_review_r1.md` 并注册（id `art_20260514_1b897b`）。

## 关键发现

**编译**：✅ 通过，14 页（主体 6 + 参考 2 + 附录 6），主体远低于 8 页限制。

**P0（必修，2 项）**
- 6 个 `\cite` key 在 bib 中缺失：`proofwriter` `prontoqa` `thinkprm` `versaprm` `rprm` `metr-reward-hacking`，PDF 中显示为 `[?]`
- 修复后需重跑完整编译链确认

**P1（应修，4 项）**
- `fig:prolog-comparison`（Fig 4）有 `\label` 但全文无 `\ref` — 建议在 `appendix.tex:421` 附近补引用
- 两个附录表各有 2 个 `\label`（`tab:fol-detailed`+`tab:beta01-3seed`、`tab:prolog-detailed`+`tab:prolog-crosslogic`），删除未被引用的别名
- `math-shepherd` 在 bib 中但无引用
- `paper.tex` 是旧版（标题不同、`\input{discussion}` 文件不存在），建议连同 `paper.{aux,bbl,blg,log,out,pdf}` 一起删除

**P2**：节标签未被引用、Underfull hbox 警告、`writing_plan.yaml` 中 ProofWriter 旧描述。

**所有硬约束通过**：D051（无 2.4×）/ s44 标记为 gaming / 7-mode / ISR* 统一 / H7=0% under random / SFT 92.9% / 1.06× premise-matched / C006 区分 redundancy vs gaming。conclusion embedding 范围用的是 **68–97%**（不是 68–100%，但实证支持 97% 上限是正确的）。

---
