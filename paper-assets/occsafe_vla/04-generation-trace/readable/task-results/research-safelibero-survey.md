# research safelibero survey

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_safelibero-survey_20260520T040530_result.json`
- **Structured JSON:** [`74a3f7452efc09294472.json`](../../sessions/74/74a3f7452efc09294472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/projects/occsafe_vla/artifacts/safelibero_survey.md`。

核心结论：

- **SafeLIBERO** 由清华 VLSA 团队提出（arXiv 2512.11891），从 LIBERO 的 4 个 suite 各选 4 个任务，加入障碍物构造 32 个安全评估场景（1600 episodes）
- **CAR 检测方式**：不用 MuJoCo contact force，而是监控障碍物 L1 位移 > 0.001 判定碰撞，实现极简
- **VLA baseline 安全性极差**：OpenVLA-OFT CAR 15.13%，π₀.₅ CAR 18.69%——80%+ episode 发生碰撞
- **AEGIS 是当前 SOTA**（CAR 77.85%, TSR 68.13%），但依赖 VLM 在线推理 + GroundingDINO，推理开销大
- **Long suite 是薄弱环节**：AEGIS TSR 仅 43.75%，是我们的差异化机会
- **获取简单**：MIT 许可，HF 直接下载 638MB，`conda create -n libero python=3.8.13` 即可搭建

---
