# fix d068 story review fixes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d068-story-review-fixes_20260527T073903_result.json`
- **Structured JSON:** [`0d0fefe1c8d315379d68.json`](../../sessions/0d/0d0fefe1c8d315379d68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，0 errors，17 pages。改动摘要：

**1. 措辞降级**（6处）：Abstract、Introduction（正文+contributions）、Results（2处）、Conclusion 中所有 "irrelevant" / "does not affect" 改为 "showed no detectable effect under the conditions tested" / "did not detectably affect ... in our experiments"。Results 中 Random OCC/Depth 的 p>0.4 注明 "observed under v1 codebase"。

**2. LoRA-specificity caveat**：Discussion 中 Practical guideline 前新增一段，指出所有实验使用 LoRA adapters，full fine-tuning 是否有相同 interaction pattern 是 open question，低秩约束可能放大对 dual-objective landscape 的敏感性。

**3. Related Work 扩展**：Section 2.1 新增 SpatialVLA/DepthVLA/OccVLA 只报告 task success 未报告 safety metrics 的具体指出。Section 2.2 新增 PCGrad 和 CAGrad 各 1-2 句展开描述，BN sensitivity 文献（Li et al., Schneider et al.）各 1-2 句展开，以及 LoRA + auxiliary task interaction 的文献空白段落。

**4. Intro motivation 前移**："single-factor ablations cannot detect interactions" 核心论点从第3段移至第2段末尾（gap-identification 之后），原位置改为 "As argued above, single-factor designs cannot detect such interactions" 的简化回引。

---
