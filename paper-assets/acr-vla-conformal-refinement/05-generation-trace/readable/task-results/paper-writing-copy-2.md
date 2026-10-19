# paper writing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260515T193525_result.json`
- **Structured JSON:** [`3bf43d8187dd590fafdb.json`](../../sessions/3b/3bf43d8187dd590fafdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 已写入 `artifacts/_project/paper/related_work.tex`。

结构概要：
- **VLA Robustness**: training-time (RobustVLA, SRPO, DiG-Flow, TT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2)。定位 ACR-VLA 为 selection + correction 的组合，plug-and-play，无需 retraining。
- **Conformal Prediction in Robotics**: CP 基础 (Angelopoulos, CGS) + 机器人应用 (Conformalized Teleoperation, CP-Loop, ACP+CBF)。明确 ACR-VLA 用 CP 做 scoring/selection，不声明 corrected output 的 coverage guarantees。
- **Residual Policy Learning**: Silver → TRANSIC → PLD → DRC 的 magnitude control 演进。ACR-VLA 用最简单的 L2 norm clipping，且是 supervised offline training 而非 RL。
- **Uncertainty Quantification for VLAs**: DiU (single-pass) vs ACR-VLA (multi-sample)；SAFE (failure detection)；VLA calibration。包含 negative result：per-DOF conformal features 作为 CRM 输入未能提升性能。

所有引用均来自指定 cite key 列表，未编造任何引用。ReconVLA 正确描述为 conformal prediction method。

---
