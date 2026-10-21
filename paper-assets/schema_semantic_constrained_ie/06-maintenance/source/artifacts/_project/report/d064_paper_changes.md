# d064 Paper Changes — 998-doc Beam Data Update

Date: 2026-05-19

## Summary

Updated LaTeX files with d064 DocRED 998-doc beam-4 results (Qwen, Llama). Greedy baselines and Mistral 998-doc data are pending (\TBD placeholders).

---

## Changes by file

### 1. main.tex

| Line | Old | New |
|------|-----|-----|
| L18 | *(not present)* | `\newcommand{\TBD}[1]{\textcolor{red}{#1}}` |
| L82 | `and a DocRED subset across three models` | `and the full DocRED dev set across three models` |

**Note:** L82 was already updated in a prior edit; \TBD definition added in this session.

### 2. appendix_beam_search.tex

#### Table rows (tab:beam-search)

| Row | Old data | New data |
|-----|----------|----------|
| L35 Qwen DocRED Greedy | `0 & 0 & 8.69 & 2.08 & 59.08 & 8.33` | `0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1}` |
| L36 Qwen DocRED Beam | `0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37` | `0 & 0 & 0 & 0.01 & 84.00 & 44.46` |
| L43 Llama DocRED Greedy | `0 & 0 & 1.58 & 6.85 & 55.35 & 6.12` | `0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1}` |
| L44 Llama DocRED Beam | `0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47` | `0 & 0 & \textbf{0} & \textbf{0} & 85.23 & 47.17` |
| L51 Mistral DocRED Greedy | `0 & 0 & 28.37 & 0.34 & 51.60 & 4.19` | `0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1}` |
| L52 Mistral DocRED Beam | `0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70` | `0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1}` |

#### Discussion paragraph

| Location | Old | New |
|----------|-----|-----|
| L60-61 | `On DocRED (full 998-document dev set), beam search eliminates DR for both Qwen (8.69%→0%) and Llama (1.58%→0%), with CF reductions of 74% and 86% respectively. Llama DocRED shows the largest R-F1 gain (+3.4 pp)...` | `On DocRED (998 documents), beam search achieves DR=0% for both Qwen (CF=0.01%) and Llama (CF=0%); Llama attains zero violations across all four constraint metrics (ET=RV=DR=CF=0%).` |
| L66 | `On DocRED (96 relation types, 998 documents), beam search reduces DR by 25% relative (28.4%→21.4%)...` | `\TBD{On DocRED (96 relation types, 998 documents), Mistral beam results pending.}` |

#### Parse failure / CI paragraph

| Location | Old | New |
|----------|-----|-----|
| L101 | `With DR=0 across 998 DocRED dev documents for both calibrated models, the Clopper-Pearson 95% CI upper bound is ≈0.3%, confirming statistical reliability.` | `With DR=0% across the full 998-document DocRED dev set for both calibrated models, the zero-DR result is validated at full evaluation scale.` |

### 3. section5_runtime.tex

| Line | Old | New |
|------|-----|-----|
| L13 | `and a DocRED 50-document subset, and` | `and DocRED (998 docs), and` |

**Note:** Already updated in a prior edit.

### 4. appendix_tcr.tex

| Line | Old | New |
|------|-----|-----|
| L82 | `DocRED 50-doc subset: DR→0%` | `DocRED (998 docs): DR→0%` |

---

## Previously applied changes (found already in files)

These were applied in a prior session and confirmed correct:
- appendix_beam_search.tex L23: caption "50-document subsets" → "full dev set (998 documents)"
- appendix_beam_search.tex L34/L42/L50: row labels "DocRED (50)" → "DocRED (998)"
- appendix_beam_search.tex L58: "50 documents" → "998 documents"
- appendix_beam_search.tex L100: parse failure data updated to 998-doc range
- appendix_beam_search.tex L155: "50 DocRED documents" → "998 DocRED documents"
- New table tab:beam-docred-lora added with LoRA + beam-4 DocRED 998-doc data
- section5_runtime.tex L13: DocRED reference updated
- main.tex L82: DocRED reference updated

## Remaining TBD items

1. **Qwen greedy 998-doc** — ~2.5h ETA from task start
2. **Llama greedy 998-doc** — ~1h ETA (Option C running)
3. **Mistral 998-doc** — not in d064 scope
4. **Discussion Mistral DocRED** — pending Mistral 998-doc data
