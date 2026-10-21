# director / loop_3.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`26e50ebd7e637d2c25c5.json`](../../sessions/26/26e50ebd7e637d2c25c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T11:22:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只用 westd-16980 的 cuda:0 和 cuda:1，不越界
- `submit_training_job` 设 `CUDA_VISIBLE_DEVICES=1` 时进程只看到 logical cuda:0，命令必须用 `--device cuda:0`
- W1 CF fallback ablation 的 max_tokens 必须与原实验一致（SciERC=2048, DocRED=4096），否则变量污染
- mt6144 实验（llama_docred_*_mt6144）已使用 CF fallback 代码（代码修改 05:00 CST，提交 08:19 CST），不能用于纯 CF ablation 对比——两个变量都变了
- `dr_residual_analysis.md` 聚合数字（unconstrained DR=30.80%）与 registry（26.07%）不一致，rebuttal 中避免引用其聚合数字

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com)，账户 root
- 工作目录：`/root/schema_semantic_constrained_ie/`
- 论文路径：本地 `artifacts/_project/paper/`（latexmk 可本地编译）
- 活跃进程：
  - `llama_docred_unconstrained_mt6144` PID 246952 cuda:0（~22% 完成，ETA ~15:00 UTC）
  - `llama_docred_full_s1_mt6144` PID 247492 cuda:1（~19% 完成，ETA ~15:30 UTC）
- 审稿 review_chat_id: `oc_01fc90ae186a4ed432770f7601995139`

### 3. 📊 当前状态
**Round 1 审稿应对（Weak Reject）几乎全部完成：**
- 16 issues 中 15 resolved（W1-W14 + Q7-Q8），仅 W1 CF fallback ablation 剩余
- Paper Agent 完成全部写作修复：§3 pair-based 重写、runtime 表、Table 1 v2 统一、Limitations 扩展、prompt appendix、CF 双机制分析
- 论文编译通过 17 页，main body ≤8 页（Limitations 在 page 8 底部开始）
- W1 CF fallback 代码已实现（type_mask_processor.py +27 行），dry-run 通过

**Registry:**
- RUNNING: `llama_docred_unconstrained_mt6144`, `llama_docred_full_s1_mt6144`
- PREPARING: `w1_cf_fallback_scierc_pilot`, `w1_cf_fallback_docred`, `w1_cf_fallback_llama_scierc`, `w1_cf_fallback_llama_docred`

### 4. 📋 待办
- mt6144 两实验完成 → Agent 收集结果（DR/CF/parse_failures/R-F1）上报 → 注意 full_s1_mt6144 带 CF fallback 代码，解读时标注
- mt6144 结果收集后 → 立即启动 Phase 1: `w1_cf_fallback_scierc_pilot`（Qwen SciERC, cuda:0, max_tokens=2048, ~1.3h）
- Pilot 完成 → 对比原 full_s1（CF 9.90%, DR 0.93%）：CF 显著↓ → 审批 Phase 2（Qwen DocRED cuda:0 + Llama SciERC cuda:1 并行）；CF 无改善 → 转 rebuttal framing "explored but complementary trade-off"
- Phase 2 完成 → 填入 §7 W1 CF Mitigation 占位段落（已有 `% TODO [W1]` 注释块）+ DR-CF Pareto 分析
- 全部完成 → recompile → `submit_paper_to_review(recommended_review_mode="continue")` → Round 2 review → May 19 内部稿 → May 25 EMNLP ARR

### 5. 🎯 战略上下文
- **CF 有两个独立机制**：(1) registry type override（W1 修复目标），(2) grammar-first fallback（tokenizer 兼容性，Qwen 0 次 vs Llama DocRED 64/doc）。W1 只能修 (1)，Qwen 配置预期效果最大，Llama+DocRED 帮助有限——这不是失败，是更深的分析
- **W2 是 rebuttal 最强项**：代码实际做 pair-based enforcement，比论文原描述更严格。SciERC 0/7 rectangular, DocRED 76% non-rectangular。0 GPU 成本，纯写作修复已完成
- **Q8 FP analysis**：净 FP +0.2%（68 移除/71 新增），constraint 不引入系统性 FP bias
- **易错点**：Paper Agent session 和 Reviewer session 都是新 reset 的。Paper Agent 已有完整写作上下文（首次 8 项 + W4 Table 1 + 双机制分析 + 页数压缩）。给 Paper Agent 发 W1 结果时要提供完整数据，不能假设它记得之前的对话
- `review_issues.yaml` 是 16 issues 的完整追踪文件，状态准确


---
