# OpenReview Submission Fields — CoRL 2026

## Title
How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation

## Abstract
Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance. We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, revealing that over 99% of safe episodes in Pi0-family models are action-collapse artifacts. We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance: ground-truth oracle refinement reduces CAR below unrefined baselines by redistributing collisions to unmonitored arm links, and SDF training supervision shows no statistically significant benefit beyond collision-free demonstrations alone. These findings suggest that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.

## Keywords
VLA safety, collision avoidance, action collapse, signed distance fields, evaluation metrics, robot manipulation, diffusion policy, safety benchmarks

## TL;DR
Over 99% of safe episodes in Pi0-family VLA models are action-collapse artifacts rather than genuine avoidance; EE-only SDF supervision provides no statistically significant benefit beyond collision-free demonstrations.

## Generative AI Disclosure
Large language models (Claude, Gemini) were used to assist with literature review, code debugging, experimental result analysis, and paper drafting. All scientific claims, experimental designs, and conclusions were determined by the authors. Generated text was reviewed and revised by the authors. Figure 1 overview illustration was generated using PaperBanana (Gemini-based code generation for matplotlib). All quantitative results, statistical analyses, and experimental code were produced by author-written scripts verified against raw evaluation logs.

## Supplementary Materials
- `main.pdf` — Full paper with appendix (17 pages: 8-page body + 1-page references + 8-page appendix)

## Dual Submission
This work has not been submitted to any other venue.
