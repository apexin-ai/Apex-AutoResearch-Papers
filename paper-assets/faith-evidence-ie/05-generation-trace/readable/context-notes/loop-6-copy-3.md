# reviewer / loop_6.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`8ec1807d34b0e2c9e10f.json`](../../sessions/8e/8ec1807d34b0e2c9e10f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T09:41:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- **r1 的 rel_f1=0.0483 是评估 bug，不是模型失败**。rsft_trainer 的 `--eval_max_docs 50` 只在 50 docs 上生成预测，但 gold triples 用了全量 985 docs 的 12275 条，recall 被人为压到 ~3.5%。s44 全量 eval 实际通过 MVP-2（rel_f1=0.4655）。D037 pivot 基于错误数据，需撤回。
- r1 registry 里的 conclusion=negative 和 failure_mode="relation_ontology_collapse_to_freetext" 是基于上述 bug 的误判，**不要引用这些作为 RSFT 失败的证据**。
- CED reranker POC（PID 178055）仍在 GPU 0 运行，不要 kill——它作为增强方案仍有价值，但不再是"唯一活路"。

### 2. 🖥️ 基础设施快照
- 服务器：`rtx5090-4x`（root），4× RTX 5090 32GB。另有 `bjb2-12179`（root）未使用。
- 工作目录：`/root/autodl-tmp/freige`（代码），`/root/autodl-tmp/` 为数据盘根
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/autodl-tmp/models/Qwen3-4B`，SFT adapter：`/root/autodl-tmp/sft_output`
- 数据：`/root/autodl-tmp/data/docred/`（train_annotated + dev）
- HF cache：`/root/autodl-tmp/.hf_cache`
- RSFT 输出：`rsft_output/`(r1/seed42), `rsft_output_s43/`, `rsft_output_s44/`, `rsft_output_r2a/`, `rsft_output_r2b/`
- RSFT 训练数据：`rsft_filtered/rsft_train.jsonl`(2718), `rsft_filtered/rsft_train_clean.jsonl`(2548), `rsft_filtered_topk3/rsft_train.jsonl`(8037)
- 活跃进程：PID 178055（CED reranker POC，GPU 0，16.6 GB）
- GPU 1/2/3 空闲

### 3. 📊 当前状态
**刚发现并报告**：r1 的 0.0483 是 50-doc eval bug，s44 全量 eval 通过 MVP-2（rel_f1=0.4655, evi_f1=0.8087）。已通过 reviewer_post_to_director 发送 CRITICAL 报告，等待 Director 响应。

Registry 关键状态：
- `mvp2_rsft_r2a` / `mvp2_rsft_r2b`：ANALYZING（训练完成，待全量 eval）
- `mvp2_ced_reranker_poc`：QUEUED（PID 178055 实际在 GPU 0 运行，~54%+）
- `mvp2_rsft_train_r1`：DONE/negative（**错误结论，需 Director 修正**）
- `mvp2_eval_rsft_s44`：PREPARING（**实际已完成**，结果在 `/root/autodl-tmp/eval_results/rsft_s44/metrics.json`）
- `mvp2_rsft_train_r1_s43`：ANALYZING（训练完成，未做全量 eval）
- `mvp2_rsft_ced_scoring_topk3`：PENDING（**实际已完成**，8037 samples，registry 未更新）

### 4. 📋 待办
- Director 回应 eval bug 报告 → 确认 D037 撤回 → 协助更新 r1 conclusion 和 ROADMAP
- r1 全量 dev eval 结果出来 → 核实是否与 s44 一致（预期 rel_f1 ~0.46）
- r2a/r2b 全量 dev eval 完成 → 对比 r1/s44，判断 1-epoch / LoRA-scaling 修改的增量效果
- CED reranker POC 完成 → 审查结果，判断 reranker 能否在 RSFT 基础上进一步提升
- Agent 修复 rsft_trainer eval bug（gold triples 须限制为 eval_max_docs 对应的子集）→ 核实修复正确性

### 5. 🎯 战略上下文
- **MVP-2 实际上已通过**：RSFT s44 全量 eval rel_f1=0.4655（+5.98pp vs SFT），evi_f1=0.8087（+1.08pp），edcr 从 0.7118 降至 0.6350。CED 通过 rejection sampling 成功提升了关系抽取和证据质量。
- **GRPO 确实失败**（D031/D033）：6 个 checkpoint 全量 eval 均 <0.014 rel_f1，这是真的 catastrophic forgetting。但 RSFT 与 GRPO 不同——RSFT 成功了。
- **最易判断错的事**：看到 r1 registry 的 conclusion=negative / rel_f1=0.0483 不要相信——这是 50-doc eval bug。必须看 `/root/autodl-tmp/eval_results/rsft_s44/metrics.json` 的全量结果。
- **决策链**：D002(MVP-1 PASS) → D031(GRPO 判死) → D037(RSFT "失败" pivot，**需撤回**) → 实际 RSFT PASS
- r2a/r2b 作为 ablation 仍有价值但不再是"救命实验"。3 seed 训练指标方差 <0.04%，模型稳定。


---
