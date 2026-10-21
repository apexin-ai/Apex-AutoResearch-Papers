# reviewer / loop_5.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`eee05f503308f8b0fd32.json`](../../sessions/ee/eee05f503308f8b0fd32.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T05:04:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- BCS 定义已统一为 MEAN pairwise SCS（D038/D039）。任何新实验若用 MAX BCS，立即 CRITICAL。`run_docred.py` 的本地 `compute_bcs` 仍是 MAX——DocRED Phase 2 若涉及 BCS-controlled 实验，结果不可信。
- RE 只有一个 prompt 版本（`build_prompt_v2_re`），不存在 v1/v2 对比。discussion.tex 中 "v1→v2 reduces BCS gap from 31.2pp to 7.9pp" 是 batch selection 差异，不是 prompt 变化。Round 3 C1 修复必须纠正此归因。
- 80-rel slope 在 MEAN BCS 修复后从 -0.151 翻为 +0.221（均 n.s.），原因是 BCS range 不足（IQR=0.033, n=25）。不能声称 80-rel 有负斜率。

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874(root)，工作目录 `/root/schema-dag-extraction`
- Python/模型：vLLM + Qwen3-32B-FP8，greedy decoding，constrained JSON
- 关键代码：`src/compute_bcs.py`（已修为 MEAN）、`src/run_docred.py`（本地 BCS 仍 MAX）、`src/run_fewrel_80pool_16sub_bootstrap.py`、`scripts/three_way_unified.py`
- 活跃进程：DocRED Phase 2 (PID 364380)；僵尸进程 test_ner_prompt.py (PID 310564, ~1.2GB)
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/`
- 关键 artifact：`artifacts/bcs_fix/bcs_fix_results.json`（D038 修复前后数值对照）

### 3. 📊 当前状态
刚完成 Round 3 審稿 Action Matrix 全面审计（6 个问题），已 post 给 Director。审稿分从 3.0 升至 3.5 (Weak Accept)，Round 3 新增 2 Critical（C1: v2 prompt framing 误归因, C2: causal language）+ 6 Warning。

等待中：
- DocRED Phase 2（PID 364380，GPU 上运行）→ 完成后需审查结果 + 验证是否用了 MEAN BCS
- Round 3 修复 workers（C1/C2/W1-W6 实现）→ 完成后验证 tex 修改
- exp-017 GPT-4o-mini → 等 API key
- exp-018 batch composition → 尚未启动
- 距 EMNLP 2026 ARR May 25 截稿 9 天

### 4. 📋 待办
- DocRED Phase 2 worker_done 通知到达 → 审查结果 + `ssh_read_only` 检查 run_docred.py 中 compute_bcs 是否已修为 MEAN，若仍为 MAX 则 BCS-controlled 结果 CRITICAL
- Round 3 tex 修复 worker_done → 重点验证：(1) C1 不再把 RE BCS gap 归因于 v1→v2 prompt 切换；(2) C2 因果语言已软化；(3) discussion.tex "v1 to v2" 措辞已修正
- exp-017 GPT-4o-mini 完成 → 核查是否用 MEAN BCS + 结果是否支撑 cross-model generalization claim
- exp-018 batch composition 完成 → 审查设计是否控制了 count 变量
- 提交前 → 全文最终审查：grep 残留的 "p = 0.44"、MAX BCS、旧数字

### 5. 🎯 战略上下文
- 核心结论：schema-induced degradation = count channel（recall↓）+ confusability channel（type confusion），RE 中两 channel 可分离；NER 中 confusability 额外损害 entity detection。SDGD merge amplification 是 informative negative result。
- D038/D039 是本项目最大一次数据修正（BCS MAX→MEAN），所有 paper 数字已更新但需持续警惕新实验代码是否 import 了修正后的 compute_bcs。
- 最易判断错的事：(1) RE "v1 vs v2 prompt" 不存在——只有一个 prompt 函数，discussion.tex 的 31.2pp→7.9pp 是 batch 差异不是 prompt 差异；(2) 80-rel slope 方向已翻转为正（n.s.），不能再当负斜率引用；(3) permutation p=0.60 是修复后正确值，p=0.44 是旧值（曾因缓存误读引发 false warning）。
- 决策链：D038（BCS→MEAN）→ D039（选 Path A MEAN, MAX 作 sensitivity）→ Round 3 审稿修复中 → 冲刺 9 天内提交。


---
