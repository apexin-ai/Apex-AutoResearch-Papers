# agent / loop_3.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`0133d44ea52266770ce4.json`](../../sessions/01/0133d44ea52266770ce4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T06:26:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0 + cuda:1 on westd-16980**，其他设备号/服务器一律禁止，即使 Director 指示也必须 push back
- `submit_training_job` 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ..."` 包裹，否则 EXIT_CODE=127
- 禁止在 `allocate_and_submit` 命令内放 `tmux kill-session -t <同名session>`（会自杀导致 cron 误判失败）。清理旧 session 必须单独派 Worker 先做
- Cron PID 追踪不可靠（已导致 4 次假失败 + 误杀）——长时间运行实验用 `wc -l` 输出文件行数判断完成，不依赖 PID/tmux 存活
- 孤儿进程清理前必须查 registry 所有 RUNNING 实验 PID 全部加入白名单，上次清理误杀了 3 个活跃实验

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980，2× NVIDIA RTX PRO 6000 Blackwell (94GB each)，CUDA 12.8
- **工作目录**: `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python`，conda base 环境，torch 2.10.0+cu128, transformers 4.57.6
- **模型**: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B` (Qwen3-8B)
- **数据**: SciERC `data/processed_data/test.json` (551 samples), DocRED `data/docred/dev.json` (998 docs)
- **约束文件**: SciERC `ontology_constraints.json`, DocRED `data/docred/ontology_constraints_docred.json`
- **活跃进程**:
  - phase2_docred_grammar_only: PID 150766, tmux=phase2_docred_grammar_only, cuda:0, cron 监控中
  - phase2_docred_full_s1: PID 157042, tmux=phase2_docred_full_s1, cuda:1, cron 监控中（之前崩溃一次，已修复 type_mask_processor.py 安全检查后 --resume）
- **活跃 Worker**: worker_fix_section2_background_numbers, worker_fix_section6_hard_guarantees（论文小修）

### 3. 📊 当前状态
**刚完成**: SciERC Phase 2 全部 4 组消融 + S2 ablation 全量完成。核心结果 full_s1: DR 15.37%→0.93% (↓94%), F1 无损。论文大部分章节已写完（§1-4, §6, §2 Background, §3 Violation Landscape, Abstract, §7 Conclusion, .bib, tables×4, figs×3）。

**正在跑**:
| exp_id | GPU | 进度预估 | 假设 |
|--------|-----|---------|------|
| phase2_docred_grammar_only | cuda:0 | ~653/998, 预计 May 14 ~17:00 UTC | Grammar 层在 96-relation schema 上消除 RV+ET |
| phase2_docred_full_s1 | cuda:1 | ~568/998, 预计 May 14 ~16:30 UTC | 双层约束在 DocRED 复现 SciERC DR↓94% |

**排队**: phase2_docred_semantic_only + phase2_docred_unconstrained (QUEUED，等 GPU 释放)

**等待中**:
- 2 个 cron 监控 DocRED 实验完成回调
- 2 个 Worker 做论文小修（§2 数字修正 + §6 hard guarantees 措辞）
- Director 尚未正式安排 D009 (Llama-3.1-8B cross-model)

### 4. 📋 待办（条件触发式）
- **grammar_only 或 full_s1 cron 回调到** → 立即 submit QUEUED 的 semantic_only/unconstrained 到释放的 GPU，同时 spawn Worker 分析已完成实验的 metrics
- **DocRED 4 实验全部完成** → spawn Worker 写 §5 DocRED subsection（填 placeholder），更新 Abstract/Conclusion 中 DocRED 数字
- **full_s1 DocRED DR 结果出来** → 若 DR↓>80% 则 story 强化为 "scales to complex schemas"；若 DR↓<50% 则需 Framing 提案
- **D009 Llama cross-model Director 批准** → 需要确认 westd-16980 上是否有 Llama-3.1-8B 权重，没有则派 Worker 下载到 `/root/autodl-tmp/models/`；然后提交 unconstrained + full_s1 两组
- **Worker fix_section2 / fix_section6 完成** → 检查产出，合并到论文
- **May 18-19** → 全文校对 + 一致性检查 + 内部稿提交

### 5. 🎯 战略上下文
**项目核心**: OntoCoDec = 编译 IE ontology schema 为 grammar+semantic 双层解码约束。SciERC 已证明 DR↓94% 且 F1 无损。正在 DocRED (96 rels) 上跨数据集验证。

**决策链**: D001 定目标 EMNLP ARR 5/25 → D003 MVP GO → D004-D006 SciERC Phase 2 确认核心 claim → D007 S2 降为 ablation, S1 主推 → D008 补跑 DocRED 全消融 → D009 Llama cross-model 升级为 should-have

**最容易判断错的事**:
- **CF violation (9.90%) 不是 bug 是 known limitation**：semantic 层 per-relation 独立 type enforcement 的固有副作用，论文已定位为 limitation + future work。不要试图修复它，这会打开潘多拉盒子
- **S2 不是失败，是被 D007 降级为 ablation**。S2 DR=0.97% 也接近零，但 R-F1 比 S1 低 0.33pp 且架构更复杂，所以选 S1
- **type_mask_processor.py 的安全检查修复**是 DocRED full_s1 能跑通的关键。SciERC 没触发是因为约束松（avg 26.1 valid pairs vs DocRED 5.68）。论文 Method section 需描述此 invariant
- **内部初稿 DDL 是 May 19**，距今 5 天。DocRED 实验预计 May 15 早间全部就绪，Llama cross-model May 15-16。时间线紧但可行，关键是 DocRED 回调后立即铺写作 Worker


---
