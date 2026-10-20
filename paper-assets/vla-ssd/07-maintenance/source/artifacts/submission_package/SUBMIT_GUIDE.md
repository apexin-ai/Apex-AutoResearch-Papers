# CoRL 2026 OpenReview Submission Guide

## Pre-Submission Checklist

- [x] main.pdf — 42 pages (8 body + appendix), zero Type 3 fonts
- [x] supplementary_code.tar.gz — analysis code archive
- [ ] Author list confirmed
- [ ] Conflict of interest list confirmed
- [ ] All co-authors have OpenReview accounts

## Step 1: Access Submission Portal

1. Go to the CoRL 2026 OpenReview submission page (link will be posted on the CoRL website)
2. Log in with your OpenReview account (create one at openreview.net if needed)
3. Click **"Submit a New Paper"** or equivalent button

## Step 2: Fill in Required Fields

### Title

```
Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis
```

### Abstract

```
When vision-language models are fine-tuned for robotic action prediction, which representational changes are associated with training and which are inherited from the pretrained backbone? We compare trained and reference checkpoints of three Vision-Language-Action models across four LIBERO task suites via layer-wise probes, attention profiling, and counterfactual perturbations. We find that VLM-to-VLA fine-tuning is associated with a consistent exit-layer collapse in action-probe decodability ($\Delta R^2 = 0.16$--$0.46$) that is absent in VLA-to-VLA transitions ($\Delta R^2 < 0.10$) and in three NLP instruction-tuning controls ($\Delta R^2 = 0.000$), suggesting this reorganization is specific to action-oriented training rather than a generic fine-tuning artifact. Complementary analyses reveal that trained VLAs develop substantial sensitivity to instruction content while the dominant attention patterns at early layers largely pre-exist in pretrained backbones. These findings provide a cross-architecture decomposition of instruction routing in fine-tuned VLAs, disentangling training-associated representational changes from inherited structure.
```

### Keywords

```
Vision-Language-Action models, Representational analysis, Instruction routing, Cross-architecture comparison, Fine-tuning analysis, Attention profiling, Action probing, Robotic manipulation
```

### PDF Upload

Upload `main.pdf` from this directory.

### Supplementary Material

Upload `supplementary_code.tar.gz` from this directory.

### Authors

**[ACTION REQUIRED]** Add all authors in order. Each author needs:
- Full name (must match OpenReview profile)
- Email address (must match OpenReview account)
- Affiliation
- OpenReview profile ID (format: `~Firstname_Lastname1`)

### Conflicts of Interest

**[ACTION REQUIRED]** Declare conflicts:
- Advisors, co-advisors, postdoc supervisors
- Current and recent (< 3 years) collaborators
- Current and recent institutional colleagues
- Anyone whose objectivity could reasonably be questioned

Enter as **domain names** (e.g., `university.edu`) or **OpenReview profile IDs**.

### Subject Areas / Topics

Select the most relevant from:
- Representation Learning
- Imitation Learning / Learning from Demonstrations
- Foundation Models for Robotics
- Vision-Language Models
- Robot Manipulation

### Paper Type

Select: **Research paper** (full paper, 8-page body)

## Step 3: Review and Submit

1. **Preview the PDF** in OpenReview's viewer — confirm all figures render correctly
2. **Verify page count**: body must be exactly 8 pages (excluding references and appendix)
3. **Double-check author order** — cannot be changed after deadline
4. **Read the submission agreement** and check the consent box
5. Click **Submit**

## Step 4: Post-Submission Verification

Within 10 minutes of submitting:

1. **Open your submission page** — confirm status shows "Submitted"
2. **Download the uploaded PDF** and verify:
   - Open the PDF and spot-check figures (especially Figure 2 heatmap, Figure 4 counterfactual bars)
   - Confirm 8 body pages
   - Run `pdffonts main.pdf | grep "Type 3"` — should return nothing
3. **Check supplementary** — confirm the .tar.gz is downloadable
4. **Verify author list** — all authors appear with correct names and affiliations
5. **Save the submission URL** and share with all co-authors

## Troubleshooting

| Issue | Fix |
|-------|-----|
| PDF upload fails | Check file size < 50MB (current: ~1.4MB, well within limit) |
| "Author not found" | Author must create OpenReview account with matching email first |
| Figures look blurry | This is OpenReview's preview renderer; download PDF to verify |
| Supplementary rejected | Check file size limit (usually 100MB); verify .tar.gz is valid |

## File Inventory

| File | Size | Description |
|------|------|-------------|
| `main.pdf` | 1.4 MB | Camera-ready paper (42 pages, 0 Type 3 fonts) |
| `supplementary_code.tar.gz` | 139 KB | Analysis code |
| `SUBMIT_GUIDE.md` | This file |
| `README.txt` | Submission package description |
| `anticipated_rebuttal_v2.md` | Pre-prepared rebuttal notes (do NOT upload) |
