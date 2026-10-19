# Response to Reviewer FCVy (R1)

We thank Reviewer FCVy for recognizing the relevance and novelty of the addressed issue.

**Q1 (Software/Reproducibility): "Will you release the code? Can you include the function for the global correction as well?"**

Our code and data are already publicly released: the anonymized repository is linked in footnote 1 of the abstract (submitted PDF). It contains:

- Full reproduction scripts for all experiments (e.g., `python exp001_hb_synthetic.py` for Table 1, `bash run_table1.sh` for full reproduction)
- Figure generation scripts (`draw_fig2.py`, `draw_fig3.py`, `figures/` directory)
- Global correction is implemented as the `Global` baseline in every experiment script (the same baseline reported in Table 1), so users can directly compare global vs. EC-HTE correction
- `requirements.txt` for environment setup
- Preprocessed data files in `data/`

We apologize if the footnote link was not sufficiently prominent. We will make the code availability more visible in the camera-ready version (e.g., a dedicated "Code Availability" paragraph).

**Q2 (Appendix organization): "High number of appendices, difficult to get main findings."**

We appreciate this feedback. The main text (Sections 1–6, 8 pages) is designed to be self-contained: it presents the bias identity (Theorem 1), diagnostic (Proposition 1), method (Algorithm 1), and main results (Tables 1–2, Figures 2–5) without requiring the appendix. The 21-page appendix provides full proofs, robustness validations across 8 conditions, and details for reproducibility, following standard practice for theory-heavy papers at *ACL venues. We will add a roadmap at the beginning of the appendix in the camera-ready to improve navigability.
