# research literature scan init

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-init_20260516T040326_result.json`
- **Structured JSON:** [`17980c310d003949c8ed.json`](../../sessions/17/17980c310d003949c8ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `literature_map.yaml`（28 篇论文，全部 2023–2026）。

**注意**：MCP `save_project_file` whitelist 不含 `literature_map.yaml`，已直接写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/literature_map.yaml`。MCP `read_project_file` 支持读取 `literature_map.yaml`，应能正常索引。

**分类分布**：
- direct-competitor (6)：LIBERO-Plus、RobustVLA、Eva-VLA、TT-VLA、Preserve-Pretrain、VLS
- method-component / LoRA routing (5)：LD-MoLE、L-MoE、LoRA-Mixer、SMoRA、HDMoLE
- method-component / VLA-LoRA (5)：OpenVLA-OFT、Accessible-VLA-LoRA、AdaMoE、FedVLA、ChatVLA-2
- method-component / activation probing (3)：EigenTrack、ICLR2024-hidden-states、Othello-GPT
- evaluation (3)：LIBERO、SimplerEnv、COLOSSEUM
- background (8)：π₀、OpenVLA、PaliGemma、Octo、RT-2、RialTo、Maniwhere、ARRO

**关键发现已映射到 Core Claims**：
- **Claim 1（Diagnosability）** ← LIBERO-Plus 的 7 维扰动分类 + ICLR 2024 hidden-states + Othello-GPT 线性可解码证据
- **Claim 2（Targeted > Uniform）** ← Accessible-VLA-LoRA 是 uniform baseline；AdaMoE/FedVLA 是 token-routed MoE 邻居
- **Claim 3（Param-Efficient Robustness）** ← 对手 RobustVLA（全 RL）、OpenVLA-OFT（full FT）、TT-VLA（test-time RL）均需更多算力或环境交互

**遗留待补**（已在 YAML 末尾注释）：VLA-specific activation analysis、π₀.₅ 论文、DR-LoRA、SEQR。

---
