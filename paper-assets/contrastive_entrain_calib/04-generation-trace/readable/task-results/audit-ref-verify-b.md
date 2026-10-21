# audit ref verify B

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-B_20260526T103523_result.json`
- **Structured JSON:** [`03ff5c99688217f7cc17.json`](../../sessions/03/03ff5c99688217f7cc17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 52 entries verified. Here's the full report:

## Verification Results

```
[1]  zhang2026latentgrpo      | ✓  | Correct
[2]  zou2023repe              | ⚠️ | Cite key says 2023, but venue is ICLR 2025. Year field "2025" is correct; cite key is misleading
[3]  rimsky2024caa            | ✓  | Correct
[4]  shao2024grpo             | ⚠️ | Published at COLM 2024, not just arXiv. Consider updating venue
[5]  li2023iti                | ✓  | Correct
[6]  turner2023actadd         | ✓  | Correct
[7]  gao2023scaling           | ✓  | Correct
[8]  skalse2022hacking        | ✓  | Correct
[9]  casper2023openproblems   | ✓  | Correct (TMLR 2023)
[10] denison2024subterfuge    | ✓  | Correct
[11] sharma2023sycophancy     | ⚠️ | Cite key says 2023, year field 2024 is correct (ICLR 2024). Cite key misleading only
[12] shapira2026amplifies     | ✗  | WRONG first author name: "Ori" → should be "Itai Shapira"
[13] wang2025internal         | ⚠️ | Correct as arXiv 2025; note: accepted at AAAI 2026
[14] wei2024synthetic         | ✓  | Correct
[15] ackermann2026gradreg     | ⚠️ | Title abbreviated: "RLHF" should be "Reinforcement Learning from Human Feedback"
[16] obrien2025fewbadneurons  | ✓  | Correct (NeurIPS 2025 workshop)
[17] mckinney2023fragility    | ✗  | WRONG year + WRONG venue: should be 2022, "NeurIPS ML Safety Workshop" (not 2023 Deep RL)
[18] papadatos2024probepenalties | ✗ | TWO wrong first names: "Harris" → "Henry"; "Richard Freedman" → "Rachel Freedman"
[19] burns2023ccs             | ✓  | Correct
[20] sinii2025smallvectors    | ✓  | Correct
[21] consistency2025bctact    | ✓  | Correct
[22] beigi2025smart           | ✓  | Correct
[23] rafailov2023dpo          | ✓  | Correct
[24] ethayarajh2024kto        | ✓  | Correct
[25] luo2026craft             | ✓  | Correct; note: accepted at ICML 2026
[26] manheim2019goodhart      | ⚠️ | Year 2019 = last arXiv revision; original was 2018. Defensible but be aware
[27] wu2026rewardhacking      | ✓  | Correct
[28] he2023debertav3          | ✓  | Correct
[29] yang2025qwen3            | ✓  | Correct
[30] grattafiori2024llama3    | ✓  | Correct
[31] openai2025gpt41          | ✓  | Correct
[32] kelkar2026persona        | ✗  | WRONG first author name: "Ameya" → should be "Ishaan Kelkar"
[33] vennemeyer2025sycophancy | ✓  | Confirmed exists. Title, authors, arXiv ID all correct
[34] hu2022lora               | ✓  | Correct
[35] schulman2017ppo          | ✓  | Correct
[36] rajbhandari2020zero      | ✓  | Correct
[37] christiano2017rlhf       | ✓  | Correct
[38] pan2022effects           | ✓  | Correct
[39] marks2024geometry        | ✗  | WRONG venue: published at COLM 2024, NOT ICLR 2024
[40] kadavath2022language      | ✓  | Correct
[41] lin2022truthfulqa        | ✓  | Correct
[42] lightman2024verify       | ✓  | Correct
[43] touvron2023llama         | ✓  | Correct
[44] ouyang2022instructgpt    | ✓  | Correct
[45] bai2022training          | ✓  | Correct
[46] stiennon2020summarize    | ⚠️ | Title should be "...from Human Feedback" not "...with Human Feedback"
[47] ziegler2019finetuning    | ✓  | Correct
[48] hubinger2024sleeper      | ✓  | Correct
[49] perez2023discovering     | ✓  | Correct
[50] uesato2022solving        | ✓  | Correct (casing difference only, BibTeX handles it)
[51] hewitt2019designing      | ✓  | Correct
[52] belinkov2022probing      | ✓  | Correct
```

## Summary Statistics

| Category | Count |
|----------|-------|
| ✓ Correct | 39 |
| ⚠️ Minor issues | 7 |
| ✗ Errors requiring fix | 5 |

## Errors Requiring Fix (5)

1. **#12 shapira2026amplifies** — First author wrong: **"Ori Shapira" → "Itai Shapira"**
2. **#17 mckinney2023fragility** — Year wrong (**2023 → 2022**) + venue wrong (**"Deep RL Workshop" → "ML Safety Workshop"**)
3. **#18 papadatos2024probepenalties** — Two author names wrong: **"Harris" → "Henry" Papadatos**; **"Richard" → "Rachel" Freedman**
4. **#32 kelkar2026persona** — First author wrong: **"Ameya Kelkar" → "Ishaan Kelkar"**
5. **#39 marks2024geometry** — Venue wrong: **"ICLR" → "COLM" (Conference on Language Modeling)**

## Minor Issues Worth Considering (7)

- **#2 zou2023repe**: Cite key implies 2023; actual venue is ICLR 2025
- **#4 shao2024grpo**: Published at COLM 2024, bib only lists arXiv
- **#11 sharma2023sycophancy**: Cite key implies 2023; actual ICLR 2024
- **#13 wang2025internal**: Accepted at AAAI 2026; bib cites arXiv 2025
- **#15 ackermann2026gradreg**: Title abbreviates "Reinforcement Learning from Human Feedback" as "RLHF"
- **#26 manheim2019goodhart**: Year 2019 is last revision; original submission was 2018
- **#46 stiennon2020summarize**: Title word "with" should be "from"

## High-Risk Entry Status

- **#12 shapira2026amplifies**: EXISTS, but author name wrong
- **#15 ackermann2026gradreg**: EXISTS, minor title abbreviation
- **#25 luo2026craft**: EXISTS and verified ✓
- **#27 wu2026rewardhacking**: EXISTS and verified ✓
- **#32 kelkar2026persona**: EXISTS, but author name wrong
- **#17 mckinney2023fragility**: EXISTS, but year + venue wrong
- **#18 papadatos2024probepenalties**: EXISTS, but two author names wrong
- **#33 vennemeyer2025sycophancy**: **EXISTS and verified ✓** (false alarm from prior flag)

---
