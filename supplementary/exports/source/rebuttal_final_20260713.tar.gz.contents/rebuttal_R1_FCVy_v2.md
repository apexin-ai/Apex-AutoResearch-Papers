We thank Reviewer FCVy for recognizing the relevance and novelty of the addressed issue.

**Code and data are already publicly released**

Our code, data, and reproduction scripts are publicly available at the anonymous repository linked in the abstract footnote (https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/):

1. Reproduction scripts: `python exp001_hb_synthetic.py` for Table 1; `bash run_table1.sh` for end-to-end reproduction
2. Figure generation: `draw_fig2.py`, `draw_fig3.py`, `figures/` directory
3. Global correction baseline: `compute_global_cm` function in `exp001_hb_synthetic.py` — directly comparable to EC-HTE
4. Environment setup (`requirements.txt`) and preprocessed data (`data/`)

**Revision**: the Conclusion now includes an explicit code-release statement listing reproduction scripts, preprocessed data, and figure generation code.

**Two appendix navigation improvements are in the uploaded revision; two more planned for camera-ready**

The main findings are self-contained in the 8-page main text (Theorem 1, Proposition 5, Algorithm 1, Tables 1–2, Figures 2–5). Changes already in the uploaded revision:

1. **Appendix roadmap** added (first paragraph of the appendix): algorithm details (App. A), full proofs (Apps. B–D), DGP specifications (App. E), real-data case studies (Apps. M, V), bias identity validation across nine LLMs (Apps. N–O, W–X), robustness analyses (remaining)
2. **All 38 appendix pointers verified precise** — no generic "see the appendix" references remain

Camera-ready plan:

3. Move secondary results and extended tables to the public code repository
4. Merge closely related appendices to reduce fragmentation
