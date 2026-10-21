# EMNLP 2026 ARR — OpenReview Submission Form Fields

## Title

Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains

## Abstract

LLM-generated text increasingly re-enters the web and seeds subsequent generation, and the resulting recursive chains progressively diverge from human-written text. We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as generation depth classification (gen-0/gen-1/gen-2+ rather than binary real-vs-synthetic). Studying eight base (pretrained) models from five families (0.6B-8B parameters), we identify a differential depth response (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary, consistent with a location shift in the token-level NLL distribution that approximately preserves distributional shape. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under eight-generator leave-one-generator-out (LOGO) evaluation and 0.764 on cross-model chains (five-generator subset), using a single 410M-parameter reference model. The depth signal degrades substantially under instruction tuning, which restricts current applicability to base models.

Word count: ~146

## Keywords

generation depth classification, LLM text detection, recursive generation chains, differential depth response, distributional profiling, text provenance, cross-generator generalization

## AI Assistance Disclosure Statement

We used AI writing assistants (Claude, GPT-4) for language polishing, code debugging, and LaTeX formatting during the preparation of this manuscript. All scientific contributions, including the problem formulation, experimental design, data analysis, and conclusions, are the authors' own work. AI tools were not used to generate experimental results or data.

## Responsible NLP Research Checklist

### A. Limitations

**A1. Did you discuss the limitations of your work?**
Yes. A dedicated Limitations section (unnumbered, after the Conclusion) discusses: (1) restriction to base models with instruct-tuned degradation quantified (OLMo-Instruct LOGO F1 = 0.338 vs. 0.763 base); (2) temperature sensitivity (reliable at t in [0.5, 0.9], substantial degradation at t = 1.0); (3) scale ceiling (largest generator 8.2B, frontier models untested); (4) prompt-type dependence (continuation F1 = 0.781 vs. elaboration 0.730); (5) 3-class resolution limit (5-class F1 drops to ~0.50); (6) English-only evaluation; (7) reference model dependency.

### B. Potential Risks

**B1. Did you discuss potential risks of your work?**
Yes. The Ethics Statement discusses that the method estimates generation depth, not author identity, with minimal privacy implications. We acknowledge the risk that depth estimation tools could be used to suppress legitimate machine-generated content and encourage deployment for provenance transparency rather than content removal.

### C. Compute Resources

**C1. Did you report the computational budget?**
Yes. Ethics Statement reports: 4x NVIDIA RTX 5090 GPUs (32 GB each), approximately 62 GPU-hours total. Software versions are fully specified (Python 3.12.3, PyTorch 2.10.0/CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0).

### D. Human Subjects

**D1. Did the research involve human subjects?**
No. All texts are LLM-generated from publicly available Wikipedia seeds. No human annotation, crowdsourcing, or human evaluation was conducted.

### E. Dataset and Licensing

**E1. Did you report dataset licenses?**
Yes. Ethics Statement reports: Wikipedia seed passages under CC BY-SA 3.0. All generator models under permissive licenses (Apache 2.0 for Pythia, OLMo, Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).

**E2. Did you provide dataset statistics?**
Yes. Appendix A provides full dataset statistics including sample counts per generator, depth, and prompt type.

### F. Code and Reproducibility

**F1. Will you release code and data?**
Yes. All code, data, and trained models will be released upon publication.

**F2. Did you provide sufficient detail to reproduce your results?**
Yes. The Method section specifies all feature definitions, classifier hyperparameters, evaluation protocols (LOGO, LOFO, cross-model), and decoding parameters (temperature 0.7, nucleus p = 0.9). Appendices provide ablations for sampling sensitivity, classifier choice, and feature selection.

### G. Existing Artifacts

**G1. Did you cite the creators of artifacts you use?**
Yes. All generator models (Pythia, OLMo, Qwen3, Llama 3.2, Mistral), evaluation tools, and relevant prior work are cited.
