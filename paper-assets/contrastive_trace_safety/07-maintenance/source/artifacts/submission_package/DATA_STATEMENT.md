# Data and Model Usage Statement

## Datasets

### HarmThoughts
- **Source:** HuggingFace Hub (`ishitakakkar-10/HarmThoughts`)
- **License:** MIT License
- **Description:** Step-level annotated reasoning traces from multiple LLMs, with safety commitment point (CP) labels. Contains traces where models transition from safe deliberation to harmful content generation.
- **Usage:** Primary evaluation benchmark. Used under HuggingFace's Terms of Service. No modifications to the dataset were made; we use the provided train/validation/test splits (60/20/20 at trace level).
- **Ethical note:** The dataset contains model-generated reasoning traces that include harmful content. We use it solely for safety monitoring research — specifically, to detect when models commit to generating harmful output — not to generate or amplify harmful content.

### AdvBench
- **Source:** Zou et al., 2023. "Universal and Transferable Adversarial Attacks on Aligned Language Models." *Proceedings of the 37th Conference on Neural Information Processing Systems (NeurIPS 2023).*
- **License:** Apache 2.0
- **Description:** 520 harmful behavior prompts used to elicit model responses for cross-dataset evaluation.
- **Usage:** Used for cross-dataset volatility analysis (Appendix) with heuristic commitment point annotations. Only B-class (compliance) traces are used for probe evaluation.

## Models

### DeepSeek-R1-Distill-Llama-8B (R1-8B)
- **Source:** DeepSeek AI
- **License:** MIT License
- **Usage:** Hidden state extraction and probe evaluation (primary 8B model)

### DeepSeek-R1-Distill-Qwen-32B (R1-32B)
- **Source:** DeepSeek AI
- **License:** MIT License
- **Usage:** Hidden state extraction and probe evaluation (32B exploratory)

### QwQ-32B-Preview (QwQ-32B)
- **Source:** Qwen Team, Alibaba Cloud
- **License:** Tongyi Qianwen License (Apache 2.0 compatible for research)
- **Usage:** Hidden state extraction and probe evaluation (32B exploratory)

### OpenThinker-7B (OT-7B)
- **Source:** OpenThinker project
- **License:** Apache 2.0
- **Usage:** Hidden state extraction and probe evaluation (primary 7B model)

### Sentence Encoders (Text Baselines)
- **all-MiniLM-L6-v2** (384d): Apache 2.0
- **BGE-large-en-v1.5** (1024d): MIT License
- **Usage:** Text embedding baselines for HS vs. text comparison

## Ethical Considerations

This research aims to improve AI safety monitoring by detecting when reasoning models internally commit to generating harmful content. All experiments use publicly available models and datasets. No new harmful content was generated for this research; we analyze existing model behaviors. The safety probes developed here are intended as monitoring tools, not as mechanisms for censorship or content filtering.
