# Final Submission Checklist (EMNLP 2026 via ARR)

## A. ARR Submission Requirements

### Paper Format
- [ ] Page limit: 8 pages (long) or 4 pages (short) for main content, unlimited for references and appendix
- [ ] Template: official ACL 2023+ style files (`acl.sty` from `https://github.com/acl-org/acl-style-files/`)
- [ ] Option: `\usepackage[review]{acl}` for review submission
- [ ] Font: Times, 11pt (enforced by `\documentclass[11pt]{article}`)
- [ ] Margins: unmodified from template defaults
- [ ] Line numbers: enabled (automatic with `[review]`)

### Anonymization
- [ ] Author field: `\author{Anonymous}` only
- [ ] No self-citations that reveal identity (check phrasing like "our previous work" vs "Author et al.")
- [ ] No institution-identifying information in text, headers, or footers
- [ ] Repository URL uses anonymous service (anonymous.4open.science or similar)
- [ ] Acknowledgements section removed or absent
- [ ] No identifying metadata in PDF properties: `grep -i "author" main.pdf` (use `pdfinfo`)
- [ ] Figures/images contain no identifying watermarks or institution logos

### File Preparation
- [ ] Main PDF compiled without errors
- [ ] No overfull hbox warnings exceeding 1pt
- [ ] All fonts embedded: `pdffonts main.pdf` shows no "no" in Emb column
- [ ] Supplementary material (if separate): clearly labeled, within size limits
- [ ] PDF file size within ARR limits (typically 10-20 MB)

## B. Responsible NLP Checklist

### Limitations Section
- [ ] `\section*{Limitations}` present in paper (required, not optional)
- [ ] Addresses: scope limitations, dataset limitations, methodological assumptions
- [ ] Does NOT count toward page limit

### Ethics Statement
- [ ] `\section*{Ethics Statement}` present if applicable
- [ ] Addresses: data privacy, potential misuse, societal impact
- [ ] Does NOT count toward page limit

### Reproducibility Checklist (from checklist.tex)
- [ ] Model specifications: architecture, size, version (Section 4.5)
- [ ] Hyperparameters: temperature, seed, decoding strategy (Section 4.5)
- [ ] Dataset details: source, splits, sampling strategy (Section 4.1)
- [ ] Evaluation metrics: exact definitions (Section 4.4)
- [ ] Compute resources: GPU type, runtime estimates (Section 4.5)
- [ ] Software versions: vLLM, embedding models (Section 4.5)
- [ ] Statistical testing: bootstrap parameters, CI methods (throughout)
- [ ] Code availability: stated with URL (Introduction footnote)

## C. Content Quality Checks

### Numerical Consistency
- [ ] Abstract numbers match Results section
- [ ] Introduction findings match Results section
- [ ] Conclusion claims match Results section
- [ ] Table values match in-text references
- [ ] Figure descriptions match visual content

### Citations
- [ ] All `\cite` keys exist in `references.bib`
- [ ] All `.bib` entries are cited in text (no orphans in final)
- [ ] No fabricated/hallucinated citations
- [ ] Publication venues and years are correct
- [ ] Author names spelled correctly
- [ ] arXiv preprints marked appropriately (not as conference papers)

### Writing Quality
- [ ] No AI-style markers: em-dashes, -ing phrase endings, "leverage"/"utilize"
- [ ] All acronyms defined on first use (including in Abstract)
- [ ] Consistent notation throughout
- [ ] No broken cross-references (`??` in compiled PDF)
- [ ] No TODO/FIXME/XXX markers remaining

## D. Camera-Ready Specific (Post-Acceptance)

- [ ] Switch `[review]` → `[final]`
- [ ] Add real author names and affiliations
- [ ] Replace anonymous repo URL with real URL
- [ ] Add Acknowledgements section
- [ ] Update "will be released upon acceptance" → "available at"
- [ ] Add ACL Anthology ID if provided
- [ ] Check camera-ready page limit (may differ from submission)
- [ ] Upload to ARR/OpenReview camera-ready portal by deadline

## E. Pre-Upload Final Steps

- [ ] `latexmk -pdf main.tex` compiles cleanly
- [ ] Full proofread of compiled PDF (not just source)
- [ ] Co-authors have reviewed and approved
- [ ] Supplementary code/data package prepared (if required)
- [ ] All files named per ARR conventions
