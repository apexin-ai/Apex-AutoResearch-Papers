# Citation Verification Report

Generated: 2026-05-16

---

## grant2026
- **Status**: TRUE
- **Title**: Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models
- **Authors**: Bryce Grant, Xijia Zhao, Peng Wang (Case Western Reserve University)
- **Year**: 2026
- **URL**: https://arxiv.org/abs/2603.19233
- **BibTeX**: Already in references.bib (correct as-is)
- **Notes**: Verified. Applies activation injection, SAEs, and linear probes to 6 VLA models (80M-7B params) across 394K+ rollout episodes. Finds visual pathway dominates action generation across all architectures. Existing bib entry matches.

---

## swann2026
- **Status**: TRUE
- **Title**: Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models
- **Authors**: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager (Stanford University)
- **Year**: 2026
- **URL**: https://arxiv.org/abs/2603.19183
- **BibTeX**:
```bibtex
@article{swann2026,
  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy III, Monroe and Schwager, Mac},
  journal   = {arXiv preprint arXiv:2603.19183},
  year      = {2026},
}
```
- **Notes**: Verified. Trains SAEs on OpenVLA hidden layers; finds most features are memorized sequences but some are interpretable, general, steerable motion primitives. **Missing from references.bib — needs to be added.**

---

## rizzardo2026
- **Status**: FALSE (hallucinated author name)
- **Actual Title**: Observing and Controlling Features in Vision-Language-Action Models
- **Actual Authors**: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
- **Year**: 2026
- **URL**: https://arxiv.org/abs/2603.05487
- **Correct BibTeX**:
```bibtex
@article{buurmeijer2026,
  title     = {Observing and Controlling Features in Vision-Language-Action Models},
  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
  journal   = {arXiv preprint arXiv:2603.05487},
  year      = {2026},
}
```
- **Notes**: The paper exists and matches the described topic (feature observability/controllability in VLAs, tested on pi0.5 and OpenVLA). However, **there is no author named "Rizzardo"** on this paper. The citation key `rizzardo2026` and the attribution "Rizzardo et al." are hallucinated. Must be corrected to `buurmeijer2026` / "Buurmeijer et al." in all paper text. **Missing from references.bib — needs to be added with correct attribution.**

---

## hou2026
- **Status**: TRUE
- **Title**: LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models
- **Authors**: Yuchen Hou, Lin Zhao
- **Year**: 2026
- **URL**: https://arxiv.org/abs/2603.00592
- **BibTeX**:
```bibtex
@article{hou2026,
  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
  author    = {Hou, Yuchen and Zhao, Lin},
  journal   = {arXiv preprint arXiv:2603.00592},
  year      = {2026},
}
```
- **Notes**: Verified. Constructs LangGap benchmark showing VLAs largely ignore language instructions; data augmentation partially closes the gap. Referenced in paper_framing.md as "Hou 2026 (LangGap)". **Missing from references.bib — needs to be added.**

---

## black2024_pi0
- **Status**: TRUE
- **Title**: pi0: A Vision-Language-Action Flow Model for General Robot Control
- **Authors**: Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky (Physical Intelligence)
- **Year**: 2024
- **URL**: https://arxiv.org/abs/2410.24164
- **BibTeX**:
```bibtex
@article{black2024_pi0,
  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},
  journal   = {arXiv preprint arXiv:2410.24164},
  year      = {2024},
}
```
- **Notes**: Verified. Flow matching VLA from Physical Intelligence. **Missing from references.bib — needs to be added.**

---

# Summary

| Citation Key | Status | Action Required |
|---|---|---|
| grant2026 | TRUE | None (already in bib, correct) |
| swann2026 | TRUE | Add to references.bib |
| rizzardo2026 | **FALSE** (hallucinated author) | Rename to `buurmeijer2026`, fix all text references |
| hou2026 | TRUE | Add to references.bib |
| black2024_pi0 | TRUE | Add to references.bib |

## Critical Fix Required
`rizzardo2026` must be renamed to `buurmeijer2026` everywhere. The paper "Observing and Controlling Features in Vision-Language-Action Models" (arXiv:2603.05487) is real, but is authored by Buurmeijer, Amo Alonso, Swann, and Pavone — not "Rizzardo".
