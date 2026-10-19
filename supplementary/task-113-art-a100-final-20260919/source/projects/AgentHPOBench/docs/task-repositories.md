# Task Repositories

AgentHPOBench stores task adapters and benchmark metadata, not third-party source trees. Run:

```bash
python3 scripts/clone_repositories.py
```

The command clones every upstream repository at the audited commit in `configs/repositories.json`. For the five experiment snapshots that contained small runtime compatibility changes, it also checks and applies the corresponding patch from `patches/upstream/`. Existing destinations are verified against the same commit and expected patched tree. The command stops instead of silently accepting revision drift or additional worktree changes.

## Provenance Audit

All 30 repositories are commit-pinned. Eighteen revisions were recovered from retained Git metadata. The other twelve were audited against upstream history by comparing every retained source file:

- Six snapshots exactly match a complete upstream tree. Chronos matches a historical commit; the other five match their listed upstream HEAD at audit time.
- TabM is a source-only subset: all 97 retained upstream-tracked files match the pinned commit, while large upstream experiment-output directories were not retained.
- TimeXer, HyperbolicCV, iTransformer, TimeMixer, and SimpleRL-Reason match the pinned commit plus the published compatibility patch.

The compatibility patches make optional dependencies lazy, support newer NumPy/SciPy versions, or expose environment overrides needed by the benchmark. They do not change task search spaces, budgets, metrics, or datasets.

## Repository Manifest

| # | Task | Upstream | Revision | Reproduction note |
|---:|---|---|---|---|
| 1 | `llm_c_fineweb10b` | [karpathy/llm.c](https://github.com/karpathy/llm.c) | `f1e2ace` | Pinned checkout |
| 2 | `torch_conv_kan_cifar10` | [IvanDrokin/torch-conv-kan](https://github.com/IvanDrokin/torch-conv-kan) | `7a0e83c` | Pinned checkout |
| 3 | `open_r1_math500` | [huggingface/open-r1](https://github.com/huggingface/open-r1) | `1416fa0` | Pinned checkout |
| 4 | `agent_lightning_room_selector` | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | `c746af2` | Pinned checkout |
| 5 | `uni2ts_lsf_etth1` | [SalesforceAIResearch/uni2ts](https://github.com/SalesforceAIResearch/uni2ts) | `7a4e77c` | Pinned checkout |
| 6 | `timesfm_etth1_long_horizon` | [google-research/timesfm](https://github.com/google-research/timesfm) | `d720daa` | Pinned checkout |
| 7 | `modernbert_mnli_accuracy` | [AnswerDotAI/ModernBERT](https://github.com/AnswerDotAI/ModernBERT) | `c6d9423` | Pinned checkout |
| 8 | `cifar10_airbench94` | [KellerJordan/cifar10-airbench](https://github.com/KellerJordan/cifar10-airbench) | `4c1b6d1` | Pinned checkout |
| 9 | `noisygl_cora_uniform30_gcn` | [eaglelab-zju/NoisyGL](https://github.com/eaglelab-zju/NoisyGL) | `b6ac057` | Pinned checkout |
| 10 | `tabmini_molecular_biology_promoters_auc` | [RicardoKnauer/TabMini](https://github.com/RicardoKnauer/TabMini) | `385961e` | Pinned checkout |
| 11 | `binary_diffusion_adult_rf` | [vkinakh/binary-diffusion-tabular](https://github.com/vkinakh/binary-diffusion-tabular) | `101825d` | Pinned checkout |
| 12 | `xlstm_parity` | [NX-AI/xlstm](https://github.com/NX-AI/xlstm) | `032a6fb` | Pinned checkout |
| 13 | `vbll_yacht_rmse` | [VectorInstitute/vbll](https://github.com/VectorInstitute/vbll) | `142f21e` | Exact tree |
| 14 | `tabm_california_rmse` | [yandex-research/tabm](https://github.com/yandex-research/tabm) | `28e47ae` | Audited source subset |
| 15 | `timexer_pjm_168_24_mse` | [thuml/TimeXer](https://github.com/thuml/TimeXer) | `7601190` | Commit + compatibility patch |
| 16 | `ablkit_hwf_reasoning_accuracy` | [AbductiveLearning/ABLkit](https://github.com/AbductiveLearning/ABLkit) | `46803a9` | Pinned checkout |
| 17 | `tunedgnn_cora_gcn_accuracy` | [LUOyk1999/tunedGNN](https://github.com/LUOyk1999/tunedGNN) | `23f9604` | Exact tree |
| 18 | `verl_grpo_gsm8k` | [volcengine/verl](https://github.com/volcengine/verl) | `59f53cc` | Pinned checkout |
| 19 | `forest_diffusion_iris_f1fake` | [SamsungSAILMontreal/ForestDiffusion](https://github.com/SamsungSAILMontreal/ForestDiffusion) | `818ac3b` | Exact tree |
| 20 | `var_imagenet256` | [FoundationVision/VAR](https://github.com/FoundationVision/VAR) | `78b9539` | Pinned checkout |
| 21 | `align_anything_ragen_bandit` | [PKU-Alignment/align-anything](https://github.com/PKU-Alignment/align-anything) | `3f9decc` | Pinned checkout |
| 22 | `chronos_t5_tiny_monash_weather_wql` | [amazon-science/chronos-forecasting](https://github.com/amazon-science/chronos-forecasting) | `3211108` | Exact historical tree |
| 23 | `hyperboliccv_cifar100_accuracy` | [kschwethelm/HyperbolicCV](https://github.com/kschwethelm/HyperbolicCV) | `fe1646d` | Commit + compatibility patch |
| 24 | `itransformer_ettm2_96_mse` | [thuml/iTransformer](https://github.com/thuml/iTransformer) | `c2426e6` | Commit + compatibility patch |
| 25 | `timemixer_ettm2_96_mse` | [kwuking/TimeMixer](https://github.com/kwuking/TimeMixer) | `e246105` | Commit + compatibility patch |
| 26 | `art_2048_win_rate` | [OpenPipe/ART](https://github.com/OpenPipe/ART) | `4cbfa15` | Pinned checkout |
| 27 | `open_r1_multimodal_mathvista_accuracy` | [EvolvingLMMs-Lab/open-r1-multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal) | `232b7ba` | Pinned checkout |
| 28 | `rankup_utkface_mae` | [pm25/semi-supervised-regression](https://github.com/pm25/semi-supervised-regression) | `7ed6d26` | Exact tree |
| 29 | `sparsetsf_ettm1_96_mse` | [lss-1138/SparseTSF](https://github.com/lss-1138/SparseTSF) | `b8c2740` | Exact tree |
| 30 | `simple_rl_reason_qwen25_05b_math500` | [hkust-nlp/simpleRL-reason](https://github.com/hkust-nlp/simpleRL-reason) | `cf1c785` | Commit + compatibility patch |

Each task directory contains a `baseline.json` describing its dataset, baseline, metric, paper anchor, and execution scripts. Some datasets require manual acceptance or download, including ImageNet. Model weights are not redistributed. Every upstream repository remains subject to its original license and usage terms.
