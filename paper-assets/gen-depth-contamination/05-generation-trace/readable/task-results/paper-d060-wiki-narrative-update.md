# paper d060 wiki narrative update

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d060-wiki-narrative-update_20260518T003048_result.json`
- **Structured JSON:** [`46924476a3f761598cf0.json`](../../sessions/46/46924476a3f761598cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有更新完成。总结：

**paper_framing.md 改动：**
1. Core Claims 子弹点：新增 "Wikipedia K*=1 (scorer-controlled)" 和 "Domain 是 K* 的唯一主导因素" 两条；第一条加了三级域阶梯表述；One-wash 扩展覆盖 Wikipedia
2. Story Spine "Our framing"：从 "2/2 models, 少数 K*=1" 改为三级域阶梯（Wiki=1, C4=2, arXiv=3，含 5/5 models），加 "domain 是唯一主导因素" 语句
3. Headline result template：改为三级域阶梯叙事，arXiv 更新至 "5 models, 4 families"
4. Reviewer Concern #4：从 "只有 2 个模型" 更新为 5 模型 4 架构族
5. Reviewer Concern #7：追加 D060 证据——Qwen same-family scorer confound 在 Wikipedia 上的具体表现和控制方法

**tex 文件：**
- `experiments_c1.tex`、`discussion.tex`、`introduction.tex`、`appendix_extended.tex` 已正确反映 D060 发现，无需修改
- `tab_domain_model_kstar_full.tex`：dagger 脚注从模糊描述改为具体数据（Qwen-1.5B→K*=2, Pythia→K*=1, Δ=-2.4pp）

---
