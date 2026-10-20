---
name: distilled-research
description: "LLM结构化剪枝与恢复训练的领域研究共识——评估协议、基线选择、方法论趋势、研究空白"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [self_healing_2025, grasprune_2026, bonsai_2025, pat_2025, rac_2025, restorelcc_2025, murphy_debiased_cka_2024, rl_squeezes_2026, p2_law_2025, hape_2026, slimllm_2025, wandapp_2025, davari_cka_reliability_2023, llm_pruner_2023, gao_reward_overoptimization_2023, lachance_thesis_2024, paser_2025, kornblith_cka_2019, raghu_svcca_2017, klabunde_similarity_survey_2025, grasp_2020, resp_2025, opsd_2026, doing_more_with_less_2026, gprune_llm_2026]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 评估协议共识

**必选指标三件套**: WikiText-2 PPL + 5-7个zero-shot任务(ARC-C/E, HellaSwag, WinoGrande, PIQA, BoolQ, OBQA) + 推理吞吐量。支持度: 15/25篇。来源: GRASPrune, LLM-Pruner, SlimLLM。置信度: 高。

**推理任务指标正在分化**: 2025年后的reasoning剪枝论文用MATH-500/AIME/GSM8K替代传统zero-shot。支持度: 5/25篇(RAC, Self-Healing, RESP, OPSD, Doing More With Less)。置信度: 高。

**统计报告普遍单次运行**: 仅1/7篇精读论文报告多次运行(RL Squeezes用256 samples/problem)，其余均为单次。领域接受但审稿人越来越关注。置信度: 高。

## 基线选择模式

**必引基线**: LLM-Pruner(7/25篇引用)、Wanda(5/25)、SparseGPT(4/25)、FLAP(5/25)。这四个构成structured pruning的"标准对比组"。置信度: 高。

**恢复方法基线**: LoRA是默认recovery baseline(RestoreLCC, LLM-Pruner, Bonsai PPA均用)。DoRA和LoFiT为新晋对比项。置信度: 中。

## 方法论趋势

**上升趋势——Reasoning-Aware剪枝(2025-2026)**: 标准剪枝校准基于输入分布，但推理模型的decode输出远超输入。RAC证明CoT-aware校准在50% sparsity下保留90%准确率(vs C4校准74.4%)。Self-Healing证明RLVR恢复>95%(vs SFT ~80%)。置信度: 高。来源: RAC, Self-Healing, RESP。

**上升趋势——Post-pruning Recovery作为独立研究方向**: P2 Law建立了恢复训练的scaling law，PASER研究数据选择，RestoreLCC提出激活空间注入。恢复不再是剪枝的附属步骤。支持度: 5/25篇。置信度: 高。

**稳定趋势——全局预算优化取代逐层决策**: GRASPrune、Bonsai、GPrune-LLM都强调全局决策优于逐层独立剪枝。支持度: 4/25篇。置信度: 中。

**消退趋势——简单magnitude剪枝**: 已沦为最弱baseline，所有2025+论文都能大幅超越。置信度: 高。

## 竞品核心声明汇总

**Competitors**: GRASPrune(预算内优化>后处理mask)、Bonsai(无梯度=2-3x省内存)、PAT(同步剪枝调优>顺序执行)、RestoreLCC(目标激活注入>通用PEFT)。

**Foundation**: Self-Healing(RLVR>SFT恢复reasoning)、RAC(decode-aware校准是必须的)、RL Squeezes(RL压缩+SFT扩展=互补机制)。

## 共同局限(出现频率)

1. **评估范围窄**: 仅标准benchmark，缺乏instruction-following/safety/multilingual评估(4/8篇)
2. **模型家族偏向LLaMA**: 大多数仅测LLaMA-7B/13B(6/8篇)
3. **缺乏统计显著性**: 单次运行无误差线(6/8篇)
4. **大规模验证缺失**: 70B+模型几乎无覆盖(7/8篇)

## 研究空白

**剪枝×恢复一体化**: 多数论文做pruning或recovery，PAT是唯一同步方案，但仅处理传统任务。Reasoning模型的一体化pipeline空白。置信度: 高。

**表征相似性指导剪枝**: CKA/SVCCA在6篇论文中研究，但从未被系统用于指导LLM剪枝决策。Lachance thesis 2024在小模型上初步尝试。置信度: 中。

**结构化剪枝×Reasoning恢复**: RAC做非结构化+reasoning、Self-Healing做结构化+RLVR，但结构化剪枝后用reasoning-aware方法恢复的系统研究几乎为零。置信度: 高。
