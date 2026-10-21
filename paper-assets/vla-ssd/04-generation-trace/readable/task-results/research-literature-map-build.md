# research literature map build

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-map-build_20260515T204701_result.json`
- **Structured JSON:** [`a7c6ce1c63d2baaaf257.json`](../../sessions/a7/a7c6ce1c63d2baaaf257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已写入。覆盖 5 个方向共 21 篇论文：

**Direct Competitors (9篇)**
- Grant 2026 (`2603.19233`) — 最直接竞争者，behavioral intervention on 6 VLA models，"encoded but not used"
- Swann 2026 (`2603.19183`) — SAE on OpenVLA，Stanford
- Rizzardo 2026 (`2603.05487`) — feature-observability/controllability
- Häon 2025 (`2509.00328`) — CoRL 2025，mechanistic interpretability + activation steering
- Molinari 2025 (`2509.24559`) — world model probing on OpenVLA
- Lu 2025 (`2502.04558`) — symbolic state probing on OpenVLA + LIBERO
- Fang 2025 (`2506.09930`) — intention vs execution probing
- LIBERO-CF (`2602.17659`) — counterfactual benchmark，OpenVLA-OFT 0.4% success rate
- LangGap (`2603.00592`) — VLAs ignore language 系统性诊断

**Method (3篇)**: Kriegeskorte 2008 (RSA), Kornblith 2019 (CKA), Alain 2017 (linear probing)

**Background (2篇)**: Prismatic VLMs, VLA survey 2025

**Evaluation (4篇)**: LIBERO + LIBERO-Plus/PRO/Para

**Architecture (4篇)**: OpenVLA, RT-2, Octo, π0

核心 novelty gap：**没有任何一篇做过 trained vs untrained VLA representation comparison**。Grant 2026 比较不同架构（cross-model），我们比较同一架构 trained vs untrained（training effect isolation）。两项工作互补。

---
