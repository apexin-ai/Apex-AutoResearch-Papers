# Reference Audit Report

**Paper**: "Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility"
**Target**: CoRL 2026
**Audit date**: 2026-05-28
**Bib file**: `docs/paper/references.bib`
**Compiled tex files**: main.tex → abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total bib entries | 62 |
| Unique citations in compiled paper | 26 |
| Missing citations (cited but no bib) | 0 |
| Orphan bib entries (bib but not cited) | 36 |
| Incomplete entries (cited) | 1 |
| Author errors (cited) | 1 |
| Venue updates needed | 1 |

---

## Verdict: CONDITIONAL PASS

One critical author error (`zheng2025xvla`) must be fixed before submission. One incomplete author list (`chen2024fastv`) and one outdated venue (`black2025pi05`) should also be corrected.

---

## Critical Issues

### 1. [critical] `zheng2025xvla` — Wrong first author name

- **Bib says**: `Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others`
- **Actual** (per arXiv, GitHub, OpenReview, ICLR 2026 page): `Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and ...`
- **Action**: Replace first author "Yifu" → "Jinliang"; reorder remaining authors to match the published version.

---

## Warnings

### 2. [warning] `chen2024fastv` — Incomplete author list

- **Bib says**: `Chen, Liang and others` (1 author + "others")
- **Actual** (per arXiv 2403.06764, ECCV 2024): Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao
- **Action**: Expand to at least first 3 authors.

### 3. [warning] `black2025pi05` — Venue outdated (arXiv → CoRL 2025)

- **Bib says**: `@article{...} journal={arXiv preprint arXiv:2504.16054}, year={2025}`
- **Actual** (per PMLR v305): Published as conference paper at The 9th Conference on Robot Learning (CoRL), 2025.
- **Action**: Update to `@inproceedings` with `booktitle={Proceedings of the 9th Conference on Robot Learning (CoRL)}`.

### 4. [warning] 36 orphan bib entries

The following 36 entries exist in `references.bib` but are never cited in the compiled paper. They inflate the bib file and may confuse reviewers if `\nocite{*}` is accidentally enabled.

| # | Key | Title (abbrev) |
|---|-----|----------------|
| 1 | wang2025specprunevla | SpecPrune-VLA |
| 2 | feng2026seewhatmatters | See What Matters (ICML 2026) |
| 3 | zhang2025sparsevlm | SparseVLM |
| 4 | khaki2025sparsevila | SparseVILA |
| 5 | jabbour2025dontrun | Don't Run with Scissors |
| 6 | li2024roboflamingo | RoboFlamingo |
| 7 | brohan2023rt2 | RT-2 (Brohan) |
| 8 | ghosh2024octo | Octo |
| 9 | brohan2023rt1 | RT-1 |
| 10 | alayrac2022flamingo | Flamingo |
| 11 | chen2024internvl | InternVL |
| 12 | jaegle2021perceiver | Perceiver |
| 13 | oquab2023dinov2 | DINOv2 (2023 entry) |
| 14 | zhai2023siglip | SigLIP |
| 15 | yang2024qwen2 | Qwen2 |
| 16 | lipman2023flow | Flow Matching |
| 17 | li2024tokenpacker | TokenPacker |
| 18 | wen2024tinyvla | TinyVLA |
| 19 | ryoo2021tokenlearner | TokenLearner |
| 20 | meng2022adavit | AdaViT |
| 21 | chen2023sparsevit | SparseViT |
| 22 | ye2025fitprune | Fit and Prune |
| 23 | shi2024crossget | CrossGET |
| 24 | zhang2024fastervlm | [CLS] Attention FasterVLM |
| 25 | liu2024llava15 | LLaVA-1.5 |
| 26 | chen2024internvl25 | InternVL 2.5 |
| 27 | gao2024miniinternvl | Mini-InternVL |
| 28 | zitkovich2023rt2 | RT-2 (Zitkovich) |
| 29 | openxembodiment2024 | Open X-Embodiment |
| 30 | zhang2023h2o | H2O |
| 31 | xiao2024streamingllm | StreamingLLM |
| 32 | mees2022calvin | CALVIN |
| 33 | chi2023diffusionpolicy | Diffusion Policy |
| 34 | zeng2023transformers_tsf | Are Transformers Effective for TSF |
| 35 | bouthillier2024negative | Embracing Negative Results |
| 36 | oquab2024dinov2 | DINOv2 (2024 entry) |

**Note**: Some orphans (SigLIP, Qwen2, Flow Matching, DINOv2) are cited in non-compiled draft files (`background.tex`, `sections/introduction.tex`). If those sections were previously part of the paper, the references may have been left behind after restructuring.

**Action**: Either cite these in the compiled paper or remove from `references.bib`.

---

## Info

### 5. [info] Venue format inconsistency

Minor inconsistency in booktitle formatting among cited entries:

- **With "Proceedings of..." prefix**: `abnar2020quantifying` ("Proceedings of the 58th Annual Meeting of the ACL"), `jiang2026lightvla` ("Proceedings of the IEEE...ICRA"), `kim2024openvla` ("Proceedings of the 8th CoRL")
- **Without prefix**: `bolya2023tome` ("International Conference on Learning Representations (ICLR)"), `chen2024fastv` ("European Conference on Computer Vision (ECCV)"), `rao2021dynamicvit` ("Advances in Neural Information Processing Systems (NeurIPS)")

This is cosmetic and depends on the bibliography style (`corlabbrvnat.bst`), but standardizing would be cleaner.

### 6. [info] Duplicate orphan entries

- `oquab2023dinov2` and `oquab2024dinov2` — same DINOv2 paper, different years (2023 as article vs 2024 as TMLR). Neither is cited.
- `brohan2023rt2` and `zitkovich2023rt2` — same RT-2 paper, different first authors. Neither is cited.

**Action**: Remove duplicates if cleaning orphans.

---

## Truthfulness Verification (7 references checked)

| Key | Title match | Author match | Year match | Venue match | Status |
|-----|-------------|--------------|------------|-------------|--------|
| bolya2023tome | ✅ | ✅ | ✅ 2023 | ✅ ICLR 2023 (Oral) | **Verified** |
| kim2024openvla | ✅ | ✅ | ✅ 2024 | ✅ CoRL 2024 | **Verified** |
| black2025pi05 | ✅ | ✅ | ✅ 2025 | ⚠️ Now CoRL 2025, bib says arXiv | **Outdated venue** |
| zheng2025xvla | ✅ | ❌ First author wrong | ✅ 2026 | ✅ ICLR 2026 | **Author error** |
| shukor2025smolvla | ✅ | ✅ | ✅ 2025 | ✅ arXiv 2506.01844 | **Verified** |
| jiang2026lightvla | ✅ | ✅ | ✅ 2026 | ✅ ICRA 2026 | **Verified** |
| chen2024fastv | ✅ | ⚠️ Only 1/7 authors | ✅ 2024 | ✅ ECCV 2024 (Oral) | **Incomplete** |

No hallucinated citations detected. All 7 checked references correspond to real, published papers.

---

## Complete List of Cited References (26)

| # | Key | Section(s) |
|---|-----|-----------|
| 1 | abnar2020quantifying | appendix |
| 2 | black2024pi0 | introduction, method, experiments |
| 3 | black2025pi05 | method, experiments |
| 4 | bolya2023tome | introduction, related_work, appendix |
| 5 | chen2024fastv | related_work |
| 6 | cheng2026vlaiap | introduction, related_work |
| 7 | gao2025compressorvla | related_work |
| 8 | jiang2026lightvla | related_work |
| 9 | kim2024openvla | introduction, method, experiments |
| 10 | kim2025openoft | method, experiments |
| 11 | lewis2020bart | method, appendix |
| 12 | li2023blip2 | related_work |
| 13 | li2024cogact | appendix |
| 14 | liang2022evit | introduction, related_work |
| 15 | liu2023libero | method, experiments |
| 16 | liu2023llava | related_work |
| 17 | liu2025vlapruner | introduction, related_work |
| 18 | rao2021dynamicvit | introduction, related_work |
| 19 | shang2024prumerge | related_work |
| 20 | shi2016subpixel | related_work |
| 21 | shukor2025smolvla | introduction, method, experiments |
| 22 | su2024roformer | appendix |
| 23 | xu2025vlacache | introduction, related_work |
| 24 | yang2025efficientvla | introduction, related_work |
| 25 | yin2022avit | related_work |
| 26 | zheng2025xvla | introduction, method, experiments |
