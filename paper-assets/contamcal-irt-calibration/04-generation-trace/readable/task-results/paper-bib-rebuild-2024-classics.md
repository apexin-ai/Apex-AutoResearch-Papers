# paper bib rebuild 2024 classics

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib_rebuild_2024_classics_20260517T055840_result.json`
- **Structured JSON:** [`7bbd45122d13147b20b2.json`](../../sessions/7b/7bbd45122d13147b20b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。验证结果总结：

**严重错误（7 处）**：
1. `dekoninck_2024_constat` — 作者全错（应为 Dekoninck/Müller/Vechev，非 Nelissen/Nijssen/Davis）
2. `oren2024proving` — 两个作者拼错/搞混（Ladhak≠"Laesecke"，Hashimoto≠"Cotterell"）
3. `lalor2024irt` — **完全虚构**，Lalor 在 AAAI 2024 无此论文
4. `lalor_2024_irt_nlp` — 合著者错误（已修正为 EACL tutorial 实际 presenters）
5. `li_2024_atlas` — 作者和年份全错（实为 2025 年 Peiyu Li 等人）
6. `lyu2025atlas` — 同一 arXiv ID，也是错误作者
7. `dong_2024_cdd` — 缺 2 位作者

**轻微问题（2 处）**：
- `ercikan_2008_dif_cancellation` — 年份应为 2009（PARE vol 14）
- `white_2024_livebench` — 发表版标题改为 "Contamination-Limited"

**确认正确**：`deng_2024_tsguessing`, `polo_2024_tinybenchmarks`, `zhang_2024_minkpp`, 以及全部 pre-2024 经典条目。

输出文件：`artifacts/bib_rebuild_2024_classics.bib`

---
