# exp oh to swe reverse transfer

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_oh-to-swe-reverse-transfer_20260516T044938_result.json`
- **Structured JSON:** [`054d6c5854d685b1bd61.json`](../../sessions/05/054d6c5854d685b1bd61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 均已更新。

**总结**：

OH→SWE 反向 transfer 实验成功。核心发现：

1. **conf≥2 子集：transfer 完全对称**
   - OH→SWE: GB 0.995, RF 0.995
   - SWE→OH: GB 0.992, RF 0.996
   - 两个方向几乎无差别

2. **all non-abstain：轻微不对称**
   - OH→SWE: GB 0.937, RF 0.953
   - SWE→OH: GB 0.967, RF 0.912
   - GB 在 SWE→OH 方向更强，RF 在 OH→SWE 方向更强

3. **OH stag rate (~20.9%) 不是问题** — 当用 conf≥2 过滤噪声标签后，两个方向性能相当

4. **对 rebuttal 的意义**：结构特征的跨 agent 迁移是对称的，不依赖于训练数据来自哪个 agent。Label confidence 过滤比训练数据的 class distribution 更重要。

---
