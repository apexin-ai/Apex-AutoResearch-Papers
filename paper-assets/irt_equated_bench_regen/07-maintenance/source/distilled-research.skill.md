---
name: distilled-research
description: "LLM benchmark contamination检测与IRT高效评估领域的研究共识：标准测试床、方法谱系、实验设计模式、关键发现、研究空白"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [dekoninck2024constat, tao2026selfcritique, white2025livebench, li2024latesteval, maiapolo2024tinybenchmarks, balloccu2024leak, golchin2024timetravel, li2024contamination, shi2024mink, wang2026fragility, zhou2026psnirt, chiang2024chatbot, wang2024mmlupro, liang2026dvd, zhang2024minkpp, habba2026growingpains, lalor2019irt, vania2021irt, hendrycks2021mmlu, kiela2021dynabench, chang2024survey, hardy2026scalability, zhang2024gsm1k, li2025atlas, chen2025irtnet]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 标准测试床

MMLU(7/25)、GSM8k(5/25)、ARC(4/25)、Hellaswag(4/25)是事实标准。WikiMIA是MIA专用(2/25)。**来源: ConStat, tinyBenchmarks｜置信度高**

## Contamination检测方法谱系

- **Performance-based↑**: 参考模型+benchmark统计检验，可量化δ和p值(ConStat r²=0.94)。5/8。
- **Entropy-based(RL)↑**: Self-Critique检测policy collapse，AUC=0.70 vs baseline~0.50。2/25。
- **Variant contamination↑**: DVD用generation variance检测语义变体。1/25但方向新。
- **Guided probing→**: 利用模型对数据集名记忆，92-100%准确率。1/8。
- **Perplexity/Min-K%↓**: 通用baseline但RL后接近随机。5/25。

**来源: ConStat, Self-Critique, Time Travel｜置信度高**

## IRT应用谱系

- **Anchor+p-IRT**: 100 items达~2%误差(tinyBenchmarks)
- **Fixed calibration**: Anchor校准新benchmark,ρ≥0.9(Growing Pains)
- **Neural IRT**: PSN-IRT和IRT-Net编码item/model参数(Zhou2026,Chen2025)
- **CAT**: Fisher信息选题减90% items(ATLAS)
- **Artificial crowds**: DNN代替人类响应(Lalor2019)

**支持度7/25｜置信度高**

## 实验设计共识

1. **Ground truth**: intentional contamination(fine-tuning注入)验证检测方法。4/8。**置信度高**
2. **模型集划分**: IRT论文按模型做train/test split；temporal split更严格。**置信度高**
3. **Bootstrap resampling**: 标准显著性方法(ConStat pivotal intervals, Time Travel 10K)。3/8。**置信度高**

## 关键发现

- **Contamination≠性能提升**: C-Eval+14%但MMLU不变；larger models获益更多。**来源:Li2024**
- **RL掩盖信号**: importance sampling+clipping是根本原因。**来源:Self-Critique,Wang2026**
- **100 items足够**: IRT可降低100-160×评估成本。**来源:tinyBenchmarks,GrowingPains,ATLAS**
- **Indirect leaking**: 42%GPT论文泄露4.7M样本。**来源:Leak,Cheat,Repeat**

## 研究空白

1. **IRT质量评估×contamination检测**结合——无论文同时做。**置信度高**
2. **RL后训练contamination**仅1/25涉及。**置信度高**
3. **Dynamic benchmark+IRT efficiency**整合缺失。**置信度中**
