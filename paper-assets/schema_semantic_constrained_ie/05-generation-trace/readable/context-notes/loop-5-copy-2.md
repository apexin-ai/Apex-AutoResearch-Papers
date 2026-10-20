# agent / loop_5.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`8e536b522e02ec40ae41.json`](../../sessions/8e/8e536b522e02ec40ae41.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T13:17:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格限于 westd-16980 的 cuda:0 和 cuda:1，config gpu_ids=[0,1]，用其他卡必须 push back Director
- submit_training_job 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹，否则 EXIT_CODE=127
- 重提交实验前必须先单独清理旧 tmux session（不能在 allocate_and_submit 命令内放 tmux kill-session，会自杀）
- DocRED 输出 JSONL 有前次运行残留风险（行数 > processed 计数），分析前必须按 doc_id 去重
- phase2_docred_unconstrained 输出 570 行 vs 日志 485 processed — Worker 分析中应处理此问题

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda base, Python 3.12.3）
- torch 2.10.0+cu128, transformers 4.57.6, XGrammar v2
- Qwen3-8B：`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
- Llama-3.1-8B-Instruct：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`（已验证兼容，零代码修改）
- GPU：2× NVIDIA RTX PRO 6000 Blackwell (94GB each), CUDA 12.8
- 活跃进程：phase2_docred_semantic_only (PID 172859, cuda:1, cron 监控中)
- 活跃 Worker：`worker_analysis_phase2_docred_unconstrained_20260514T131355`（分析 unconstrained 结果）

### 3. 📊 当前状态
- **刚完成**：phase2_docred_unconstrained 进程结束 → 状态 ANALYZING，Worker 正在分析结果（注意去重问题）
- **RUNNING**：phase2_docred_semantic_only (cuda:1, PID 172859)，日志显示 392 行输出 / 328 processed，目标 998 docs，预计还需数小时
- **QUEUED（等 GPU）**：4 个 Llama 实验 — llama_scierc_unconstrained, llama_scierc_full_s1, llama_docred_unconstrained, llama_docred_full_s1
- **cuda:0 当前空闲**（unconstrained 刚跑完），semantic_only 完成后 cuda:1 也释放
- **论文写作**：§1/§2/§3/§4/§6/§7/Abstract/Tables/Figs/.bib 已完成，缺 §5 DocRED subsection（等实验结果）和 §5 Cross-model（等 Llama）
- **DDL**：EMNLP ARR May 25，内部稿 May 19（距今 5 天）

### 4. 📋 待办（条件触发式）
- Worker `worker_analysis_phase2_docred_unconstrained` 回调 → 更新 registry metrics + report.md，汇报 Director DocRED unconstrained baseline 结果
- phase2_docred_semantic_only cron 完成回调 → spawn Worker 分析（同样注意去重）→ 汇报 Director → DocRED 消融表 4/4 齐全
- DocRED 4 实验全部 DONE → spawn Worker 写 §5 DocRED subsection（填 placeholder）+ 更新 Abstract/Conclusion 中的 DocRED 数字
- cuda:0 空闲 + Llama QUEUED → 向 Director 请示启动 Llama 实验（D009 should-have），先跑 SciERC 两组（unconstrained + full_s1）
- Llama SciERC 完成 → Llama DocRED 两组 → §5 Cross-model subsection
- 所有实验完成 → 全文校对 + 一致性检查 → May 19 内部稿

### 5. 🎯 战略上下文
- **核心结论链**：D001(EMNLP) → D002(GO) → D003(Research) → D006(S1主推,S2降级) → D008(DocRED全消融) → D009(Llama cross-model should-have)
- **论文核心 claim**：grammar+semantic 双层约束近乎消除违规且零 F1 代价。SciERC DR↓94%, DocRED DR↓45.5%
- **最易判断错的事**：DocRED DR 只降 45.5%（vs SciERC 94%）不是负面结果——根因是 constraint tightness scaling（memory.md 有详细分析），论文 framing 为 "effectiveness scales inversely with constraint tightness"，这是 contribution 不是 weakness
- **CF violation 上升**（unconstrained 0.08% → S1 9.90%）是 semantic 层固有副作用（per-relation 独立 type enforcement），论文写为 limitation + future work
- **Cron PID 追踪历史上 4 次假失败**，对长时间实验不要盲信 cron 判定，用 `wc -l` 输出文件行数交叉验证
- **grammar_only baseline DR 高于 unconstrained**（DocRED: 26.17% vs 18.7%）是因为 grammar 强制合法 relation name 改变了 triple 分布，不是 bug


---
