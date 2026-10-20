# CoRL 2026 Abstract Submission

## Title

Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis

## Abstract

When vision-language models are fine-tuned for robotic action prediction, which representational changes reflect training and which are inherited from the pretrained backbone? We conduct a cross-architecture representational analysis of three Vision-Language-Action models across four LIBERO task suites, using layer-wise action probes, attention profiling, and counterfactual instruction perturbations to compare trained and reference checkpoints. We find that VLM-to-VLA fine-tuning produces a consistent exit-layer collapse in action-probe decodability that is absent in VLA-to-VLA transitions and in NLP instruction-tuning controls, suggesting this reorganization is specific to action-oriented training. Complementary analyses reveal that trained VLAs develop substantial sensitivity to instruction content while the dominant attention patterns at early layers largely pre-exist in pretrained backbones. These findings provide a cross-architecture decomposition of instruction routing in fine-tuned VLAs, disentangling training-associated representational changes from inherited structure.

## Keywords

1. Vision-Language-Action models
2. Representational analysis
3. Instruction routing
4. Cross-architecture comparison
5. Fine-tuning analysis
6. Attention profiling
7. Action probing
8. Robotic manipulation
