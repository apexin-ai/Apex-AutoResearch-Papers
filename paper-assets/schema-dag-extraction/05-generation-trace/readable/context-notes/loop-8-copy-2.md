# agent / loop_8.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`c9721ec25eafb9b3ac57.json`](../../sessions/c9/c9721ec25eafb9b3ac57.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-16T15:08:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cqa1-38874 的 cuda:0（gpu_ids 白名单只有这一张）
- 论文正文（Intro→Conclusion）必须 ≤8 页（ARR 2025 ACL format，Limitations 不计入）
- 当前 Conclusion 刚好卡在 p8 边缘——Worker `worker_paper_d048_final_compression_20260516T150745` 正在执行压缩，**结果未读取**
- exp-018 single_pass accuracy = 0.504（不是 0.8188），之前纠正过一次
- TOST equivalence margin = ±3pp（不是 ±5pp），全文已统一
- 31.2pp prose 引用限 ≤3 次（intro×1, results×2），其余用间接引用

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，SSH config 已配置
- 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：Qwen3-32B-FP8 via vLLM v0.20.2（需 `FLASHINFER_DISABLE_VERSION_CHECK=1`）
- 工作目录：`/root/schema-dag-extraction/`
- 数据：`/root/schema-dag-extraction/data/` (fewrel_parquet/, fewnerd/, maven/, docred/)
- Artifacts：`/root/schema-dag-extraction/artifacts/`
- 论文本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- 无活跃训练进程（论文收尾阶段）
- GPU cuda:0 allocated but idle（无实验需跑）

### 3. 📊 当前状态
**正在等待**：`worker_paper_d048_final_compression_20260516T150745`（页数压缩 Worker）——Conclusion 超出 p8 约半页，Worker 在压缩 Conclusion + Discussion。**结果未读取，这是你的第一件事。**

Registry 关键实验全部 DONE/success：
- exp_fewrel_factorial_tost: TOST 确认 additive separability (p=.003)
- exp_scs_name_def_ablation: name+def 无系统性改进
- exp_aggregation_monte_carlo: ~3× R² amplification confirmed
- exp_fewrel_contamination_check: 无 contamination 证据
- exp_confusability_batch_composition: directional +1.4pp, p≈0.19, not significant

D044-D048 全部论文修订已完成（结构重组、framing 校准、TOST 集成、31.2pp 削减、2.2pp 提升、因果语言校准等）。等压缩 Worker 回调后确认 ≤8 页即可向 Director 汇报 ready for submission。

### 4. 📋 待办
- `worker_paper_d048_final_compression` 回调 → 读取结果，确认 Conclusion 在 p8 内 → 向 Director 汇报 "ready for submission"
- 如果压缩不够（仍超 p8）→ spawn 新 Worker 继续压 §5 confidence gating / oracle routing 段落
- Director 如要求最终 PDF 视觉审查 → 用 pdf_to_images 渲染关键页面检查
- Director 如发新 Reviewer 审计结果 → 按指令修复

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 via ARR May 25 submission（距今 9 天）
- 核心发现：LLM IE 质量受 schema complexity 两个可加性 channel 影响——count（类型数量）和 confusability（类型语义相似度）。TOST 确认 additive separability。
- 论文 framing 演变：从 "confusability drives degradation" 调整为 "confusability shapes degradation"（因果→关联）；31.2pp extreme 降级为 methodological upper-bound，typical 2.2pp 为主锚点
- 易错点：
  - 不要把 FewRel pairwise r=0.187 加入 Table 2（Director 最终决定 omit，caption 有说明）
  - Abstract/Intro 的 r² 和 r 范围是双数据集版本（1.3-1.7%, 0.112-0.129），不含 FewRel
  - exp-018 batch composition 结果是 NOT significant（p≈0.19），论文用 "directional" 措辞
  - MAVEN 正方向是 centrality artifact，不是真正的 confusability 效应


---
