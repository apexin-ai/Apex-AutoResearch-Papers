# write n2 patch and discussion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_n2_patch_and_discussion_20260515T162335_result.json`
- **Structured JSON:** [`c6b5a41cc60dfa2d7e5b.json`](../../sessions/c6/c6b5a41cc60dfa2d7e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

**Task A — §5.4 补丁内容：**
- 添加 DeBERTa per-class F1 (d0=0.947, d1=0.378, d2=0.247, d3=0.656) 和 pairwise AUC (d0v1=0.981, d1v2=0.733, d2v3=0.755)
- 修正 architecture-independence 论述：两个 backbone 均为 masked-LM，区别在 attention mechanism（disentangled vs standard multi-head），1.2pp 差距排除换 PLM 追平 RF 的可能
- 强化 feature overlap 结论：明确"不是选错了 PLM，而是两种方法关注文本的不同层面"

**Task B — §6 新增内容：**
- 6.1 新增 ¶PLM and statistical features complementarity（orthogonal signals，非竞争关系）
- 6.1 新增 ¶Strategy-dependent degradation trajectories：三档分类（nucleus stable / temperature enhancement+reversal / top-k attenuation），禁止 soft sampling 合并；z-score 对 RF 无效、对 LR temp holdout d1v2 AUC 恶化（D014/D021）
- 6.2 新增 ¶d0 recall dominance：66.4% 被 d0≥98.5% recall 拉高，d1-d3 仅 55.4%，d2 最低 26.8%

两个 artifact 已注册（`art_20260515_1d7f7e`, `art_20260515_1560ed`）。

---
