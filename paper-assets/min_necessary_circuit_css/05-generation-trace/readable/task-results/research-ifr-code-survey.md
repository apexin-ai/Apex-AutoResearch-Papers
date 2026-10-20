# research ifr code survey

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ifr-code-survey_20260513T021046_result.json`
- **Structured JSON:** [`9e04b3c60ce70b03d810.json`](../../sessions/9e/9e04b3c60ce70b03d810.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心发现：

**IFR = Information Flow Routes** (Ferrando & Voita, EMNLP 2024)，基于 ALTI 的归因方法，单次前向传播即可完成，比 ACDC 快 ~100x。

**项目现状比预期好**：
- `ifr_discovery.py` (TransformerLens 版) 已在服务器上
- `artifacts/ifr_scoring.py` (HuggingFace 版，支持 Llama/Qwen2/Gemma2) 已在本地
- `phase2_configs.yaml` 全部 16 个实验已规划
- 服务器依赖齐全，无需额外安装

**主要集成工作**：
1. 部署 `ifr_scoring.py` + `run_phase2_experiment.py` 到服务器
2. `circuit_discovery.py` 添加 IFR normalizer
3. `css.py` 添加 IFR 二值化策略
4. 下载 3 个目标模型 (Qwen-2.5 0.5B, Gemma-2 2B, Llama-3.1 8B)

**风险点**：IFR 非因果性（但作为 K=3 ensemble 的多样性视角是其价值）、同层头共享 score、Gemma-2 残差流近似、8B 模型 EP 显存可能紧张。

---
