# Reference Audit Report

**Date**: 2026-05-30
**Bib file**: `docs/paper/references.bib`
**Tex files**: `docs/paper/main.tex` + `docs/paper/sections/*.tex`

## Summary
- Total bib entries: 41
- Verified correct (web-searched): 16
- Issues found: 2
- Orphaned entries (in bib but not cited): 0
- Missing entries (cited but not in bib): 0

## Issues

### [sutton1999options]
- **Problem**: Journal field bundles volume number into journal name
- **Current**: `journal = {Artificial Intelligence 112}`
- **Suggested fix**: Split into separate fields:
  ```bibtex
  journal = {Artificial Intelligence},
  volume = {112},
  pages = {181--211},
  ```

### [bacon2017optioncritc]
- **Problem**: Bib key has typo — "optioncritc" is missing the letter 'i' before the final 'c'. Should be "optioncritic".
- **Current**: Key `bacon2017optioncritc` (used consistently in both .bib and all .tex files, so no compilation error)
- **Suggested fix**: Rename key to `bacon2017optioncritic` in both `references.bib` and all `\cite{}`/`\citep{}` occurrences in .tex files. This is cosmetic but improves hygiene.

## Style Note: Author Name Inconsistency

Some entries use abbreviated first names (e.g., `Sutton, R.S`, `Hafner, D`, `Hansen, N`) while others use full names (e.g., `Fujimoto, Scott`, `van Hasselt, Hado`, `Bishop, Chris M.`). BibTeX/natbib styles handle this, but standardizing to full names is recommended for consistency. Affected abbreviated-name entries:
- sutton1999options, hafner2020dreamerv1, hafner2021dreamerv2, sharma2017figar, janner2019mbpo, asadi2019combating, hansen2024tdmpc2, yu2020mopo, thrun1993issues, lu2018nondelusional, biedenkapp2021temporl, gumbsch2024thick, mattes2024hieros, henderson2018deep, lambert2020objective, agarwal2021precipice, li2025lsimagine

## Orphaned Entries
None. All 41 bib entries are cited in at least one .tex file.

## Missing Citations
None. All 41 citation keys in .tex files have corresponding bib entries.

## Verified Correct (16 web-searched references)

### Core references (required by audit spec)
- **sutton1999options**: ✅ Authors (Sutton, Precup, Singh), title, year (1999) all correct. Venue issue noted above (journal field format).
- **bacon2017optioncritc**: ✅ Authors (Bacon, Harb, Precup), title "The Option-Critic Architecture", AAAI 2017 — all correct. Key typo noted above.
- **hafner2020dreamerv1**: ✅ Authors (Hafner, Lillicrap, Ba, Norouzi), title "Dream to Control: Learning Behaviors by Latent Imagination", ICLR 2020 — all correct.
- **hafner2021dreamerv2**: ✅ Authors (Hafner, Lillicrap, Norouzi, Ba), title "Mastering Atari with Discrete World Models", ICLR 2021 — all correct.
- **hafner2025dreamerv3**: ✅ Authors (Hafner, Pasukonis, Ba, Lillicrap), title "Mastering Diverse Control Tasks through World Models" matches Nature publication title. Published in Nature, Volume 640, 2025 — year and venue correct.
- **hafner2025dreamerv4**: ✅ Authors (Hafner, Yan, Lillicrap), title "Training Agents Inside of Scalable World Models", arXiv:2509.24527, September 2025 — all correct.
- **hansen2024tdmpc2**: ✅ Authors (Hansen, Su, Wang = Nicklas Hansen, Hao Su, Xiaolong Wang), title correct, ICLR 2024 — all correct.
- **lu2018nondelusional**: ✅ Authors (Lu, Schuurmans, Boutilier = Tyler Lu, Dale Schuurmans, Craig Boutilier), title "Non-delusional Q-learning and Value-iteration", NeurIPS 2018 — all correct.
- **fujimoto2018td3**: ✅ Authors (Fujimoto, van Hoof, Meger), title "Addressing Function Approximation Error in Actor-Critic Methods", ICML 2018 — all correct.
- **vanhasselt2016double**: ✅ Authors (van Hasselt, Guez, Silver), title "Deep Reinforcement Learning with Double Q-Learning", AAAI 2016 — all correct.
- **nhu2025tawm**: ✅ Authors (Nhu, Son, Lin = Anh N. Nhu, Sanghyun Son, Ming C. Lin), title "Time-Aware World Model for Adaptive Prediction and Control", ICML 2025 — all correct.
- **wang2024elastic**: ✅ Authors (Wang, Beltrame = Dong Wang, Giovanni Beltrame), title "Reinforcement Learning with Elastic Time Steps", arXiv:2402.14961, 2024 — all correct.

### Additional spot-checked references
- **pertsch2020spirl**: ✅ Authors (Pertsch, Lee, Lim), CoRL 2020 (proceedings published 2021 in PMLR v155). Year 2020 = conference year, acceptable.
- **micheli2023iris**: ✅ Authors (Micheli, Alonso, Fleuret), "Transformers are Sample-Efficient World Models", ICLR 2023 — all correct.
- **gumbsch2024thick**: ✅ Authors (Gumbsch, Sajid, Martius, Butz), ICLR 2024 — all correct.
- **mattes2024hieros**: ✅ Authors (Mattes, Schlosser, Herbrich), ICML 2024 — all correct.
- **sharma2017figar**: ✅ Authors (Sharma, Lakshminarayanan, Ravindran), "Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning", ICLR 2017 main conference — confirmed "Published as a conference paper at ICLR 2017" on arXiv PDF.
- **wu2023daydreamer**: ✅ Authors (Wu, Escontrela, Hafner, Abbeel, Goldberg), CoRL proceedings 2023 (PMLR v205) — correct.
- **lyle2022capacity**: ✅ Authors (Lyle, Rowland, Dabney), ICLR 2022 — correct.
- **li2025lsimagine**: ✅ Authors (Li, Wang, Wang, Jin, Li, Zeng, Yang), ICLR 2025 Oral — correct.
- **benechehab2023multitimestep**: ✅ Authors and title correct. Remains arXiv preprint as of search — bib correctly lists as arXiv preprint.
- **tassa2018dmcontrol**: ✅ Remains arXiv preprint — bib correctly lists as arXiv preprint.
- **asadi2019combating**: ✅ Remains arXiv preprint — bib correctly lists as arXiv preprint.

## Not web-searched (accepted as-is based on standard knowledge)
- gu2023maniskill2, janner2019mbpo, yu2020mopo, thrun1993issues, biedenkapp2021temporl, henderson2018deep, lambert2020objective, agarwal2021precipice, chen2021redq, bishop1995noise, parr1998ham, dietterich2000maxq, bradtke1995smdp, kidambi2020morel, yu2021combo, hamrick2021planning, park2021timediscretization, hafner2022director
