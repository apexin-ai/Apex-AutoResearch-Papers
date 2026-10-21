# research scaling narrative analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scaling-narrative-analysis_20260520T040340_result.json`
- **Structured JSON:** [`8a1e9f276b99e4488268.json`](../../sessions/8a/8a1e9f276b99e4488268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已写入 `artifacts/scaling_version_analysis.md`。`register_artifact` 工具当前不可用，文件已在标准 artifacts 目录下。

---

**核心结论：**

1. **倾向判断：建议以 Version B（Non-monotonic）为默认写作方案**
   - A 要求严格单调（7B<14B<32B degen），任何一个反转即被否证；B 兼容任何结果
   - B 的 "measure, don't predict" 信息与论文 diagnostic positioning（D154: cross-config degen ρ=0.052, p=0.81）一致
   - 若数据恰好单调，B→A 只需一段改写；反向改写代价更大

2. **共识点（两个版本共享）**：degeneracy gates construction 在全部 9 个条件中成立，不受版本选择影响。

3. **7B 数据判断标准**：
   - **Degen pattern** 是主判据：7B<14B<32B→选A；任何反转→选B；近似相等(Δ<3pp)→选B(lite)
   - **Construction Δ 必须反向跟踪 degen**：最低 degen 的 scale point 应有最大正 construction。若不跟踪→gating 假说需修正
   - **7B degen <10%** 强烈支持 A；**>15%** 偏向 B
   - **Greedy F1 单调但 degen 非单调** = Version B 最强证据

4. **Fallback**：若 pattern 模糊，用混合叙事——"scale 有弱趋势，但训练 recipe（LoRA rank 3× shift）和 epoch（11%→31%）的影响更大"。

---
