# reviewer / loop_4.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`54745971f4e16bc28ea0.json`](../../sessions/54/54745971f4e16bc28ea0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T10:49:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：cuda:0 + cuda:1（westd-16980 双卡 RTX PRO 6000 Blackwell 97.9GB）
- `phase2_docred_semantic_only` 的 submit 命令写了 `--device cuda:0` 但 registry 记录 `gpu: cuda:1`——实际通过 CUDA_VISIBLE_DEVICES 映射到物理 cuda:1，nvidia-smi 已验证两进程分别占不同 GPU。下一个"我"不要误判为越界
- 论文数字源头：`artifacts/_project/paper/` 是最新版，`artifacts/` 根目录下同名 tex 文件是**过期副本**（section2 仍有 3.73 错误数字），不要从根目录读
- `section3_violation_landscape.tex:52` 的 DR=12.80% 应为 12.84%，尚未修复

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (root)，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python3`，conda base 环境
- 模型：Qwen3-8B `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`，Llama-3.1-8B-Instruct `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- 数据：SciERC `data/processed_data/test.json` (551)，DocRED `data/docred/dev.json` (998)
- 活跃进程：PID 170502 (unconstrained, cuda:0)，PID 172859 (semantic_only, cuda:1)
- Llama 命令已就绪：`artifacts/llama_submit_commands.md`

### 3. 📊 当前状态
刚完成 Llama dry-run 验证审查（两个 worker 都 PASS，零代码修改）和 DocRED 进度监控审查。

Registry RUNNING：
- `phase2_docred_unconstrained`：485/998 (48.6%)，~3.3h 后完成
- `phase2_docred_semantic_only`：328/998 (32.9%)，~4.6h 后完成

**已发 WARNING**：输出 JSONL 行数 > 日志计数（unconstrained 570 vs 485，semantic_only 392 vs 328），可能有前次运行残留数据，Agent 需在 metrics 计算前去重。

等待中：无 pending cron/worker 回调。两个 DocRED 实验完成后会有 on_complete 通知。

### 4. 📋 待办
- `phase2_docred_unconstrained` 完成 → 核实 metrics，关键对比：Phase 2 unconstrained DR vs Phase 0 的 18.7%（验证 grammar_only DR=26.17% 升高是否因 pipeline 差异）
- `phase2_docred_semantic_only` 完成 → 核实 metrics，对比 SciERC semantic_only DR↓24% vs DocRED 的实际降幅
- 两个都完成 → 审查完整 DocRED 4 条件消融表一致性（unconstrained / grammar_only / semantic_only / full_s1）
- Llama SciERC 实验启动 → 检查 GPU 分配、registry 登记、是否用了 submit_training_job
- Llama full_s1 完成 → 对比 Qwen vs Llama fallback count（dry-run 显示 Llama 1 sample 就 2 次 fallback，可能显著高于 Qwen）
- 3 个 placeholder 填充 → 核实 Abstract/Conclusion/Table 4 数字与 registry 一致
- §3 line 52 修复 → 确认 12.80%→12.84%

### 5. 🎯 战略上下文
- 核心结论：OntoCoDec 在 SciERC (7 rels) 上 DR↓94%，DocRED (96 rels) 上 DR↓61%——效果随 schema 复杂度递减，根因是 constraint tightness（DocRED avg 0.842 vs SciERC 0.333）
- 论文 framing 已从 "Guaranteed Compliance" 调整为 "Near-Complete Type Compliance"，所有章节需统一此措辞
- **最易判断错的事**：DocRED grammar_only DR=26.17% > Phase 0 unconstrained 18.7%。这不是 bug——grammar 层消除 RV 后迫使模型用合法 relation name，但这些 relation 的 domain/range 约束模型的 entity type 不匹配，暴露了更多 DR。Phase 2 unconstrained baseline 是公平对比基准，不要用 Phase 0 的 18.7%
- **JSONL 去重风险**：输出文件可能有前次运行残留，metrics 计算前必须确认去重
- 文献对比结论：无任何论文在 DocRED 上报告 constrained decoding violation rate，我们的结果是首个 benchmark


---
