# director / loop_6.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`6493966a0301d7c97d99.json`](../../sessions/64/6493966a0301d7c97d99.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T20:53:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 westd-16980 和 westd-21461 两台服务器。westd-37397 已关机移除，不要尝试连接
- Qwen3-8B-ms 模型**只在 westd-16980** 上（`/root/autodl-tmp/models/Qwen3-8B-ms`）。westd-21461 只有 Mistral。不要在 westd-21461 上跑 Qwen 实验
- DocRED latency 数据只从 `/tmp/latency_benchmark_docred_results.json`。`/tmp/latency_benchmark_results.json` 是 SciERC 旧数据
- 禁止设 `fix_mistral_regex=True`——会把 Qwen regex 替换成 Mistral tekken regex 导致结果错误（D034）
- 模型名称是 Qwen3-8B（不是 Qwen2.5-7B）
- Agent 经常把已完成实验报告为失败（基于 exit code 而非输出完整性）——cron 报 FAILED 时先检查 output 文件 wc -l

### 2. 🖥️ 基础设施快照
- **westd-16980**: 2×GPU，conda base env，`/root/miniconda3/bin/python`，项目目录 `/root/schema_semantic_constrained_ie`
  - Qwen3-8B-ms: `/root/autodl-tmp/models/Qwen3-8B-ms`
  - Llama checkpoints: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged` 等
  - cuda:0: 空闲（SciERC sampling 已完成）
  - cuda:1: 空闲（DocRED sampling 已 kill——太慢，55x greedy）
- **westd-21461**: 2×GPU，同上 conda base env，只有 Mistral 模型
  - cuda:0, cuda:1: 空闲
- 4 张 GPU 全部空闲，保留备用

### 3. 📊 当前状态
**刚做完**：
- 全部 54 个原始实验完成（46 success / 1 negative / 3 killed / 4 misc）
- Group C 审稿报告已回：borderline（偏 Findings weak accept），2 must-fix + 9 should-fix
- Paper Agent 完成全部 Group C 修改（17 项 + 后续 Reviewer 发现的数据错误修正：SciERC PF=0、"76-99%"→"42-99%"、Abstract F1 来源标注、p-value 统一、EnriCo 描述修正）
- SciERC sampling 验证通过：ET=0%, RV=0%, DR=0.75%（vs greedy 0.93%）——constraint 在 stochastic decoding 下有效
- DocRED sampling 已 kill（18.8min/sample，完成需 13 天），用已有 36 docs 做 subset 验证即可
- Rebuttal 草稿 v1 完成（art_20260516_1f1860），需修正 2 处：(1) "41-72%"→"39-72%", (2) Q4 删除错误的 τ̄-only 回归引用，用 Reviewer 提供的 dual-factor 叙述替代
- 4 项 CPU 分析全部完成：Mistral tightness、parse failure sensitivity、OOV 替换案例、fuzzy matching 阈值
- RV=0.03% 根因确认：XGrammar v0.1.33 enum 编译 bug（5 triples，1 document "Souvlaki"）
- review_issues.yaml 已更新（30 条 issue，13 in_progress，14 resolved）

**RUNNING/PREPARING**：无。全部实验已完成。

### 4. 📋 待办
- DocRED sampling 36 docs violation analysis 可能未完成 → Agent 跑 violation checker 对比 greedy baseline → 结果补入 rebuttal
- Rebuttal 草稿 v1 两处修正未完成 → Agent 改 "41-72%"→"39-72%" + Q4 dual-factor 叙述 → 存为最终版 artifact
- Paper Agent 全部修改完成后 → 提交内部 Reviewer 做最终数据一致性审查
- Reviewer 通过后 → 更新 ROADMAP → submit_paper_to_review 正式交 Group C（推荐 mode=fresh，大改 framing 后）
- Sampling 结果（SciERC 完整 + DocRED subset）→ 补入论文 Appendix + rebuttal M7 段落
- 论文最终稿就绪 → log_decision D036

### 5. 🎯 战略上下文
- **核心结论已站住**：Grammar 层消除 ET/RV，Semantic 层消除 DR，两层互补不可替代（8/8 FT ablation 一致）。Composability 2×2 全部通过。3 模型泛化性已验证。
- **Group C 审稿的核心问题是 overclaiming**，不是实验不足。修好 framing + 强 rebuttal 比补实验更有效。
- **R² dual-factor**：保留 n=4 R²=0.886（τ̄ × RV_baseline），Mistral 作为 boundary condition（entity type misclassification 非 vocabulary confusion）。不报 n=6 R²。Abstract 已改 "varies predictably"→"dual-factor pattern"，§7 已改 "predictive framework"→"descriptive pattern"。
- **Sampling 验证**：SciERC 完整验证 constraint 在 sampling 下有效。DocRED 太慢已 kill，用 36 docs subset。Beam search 需 ~75 行代码改动，留 camera-ready。
- **易错点**：(1) Agent reset 后经常不知道哪些已完成，会尝试重做——用状态同步消息拦住；(2) Paper Agent 连续出现数据错误（SciERC PF 列、"76-99%"、error analysis scope），Reviewer 每次都能抓到——任何 Paper Agent patch 后必须经 Reviewer 核实再推进；(3) westd-21461 没有 Qwen 模型，不要在那边跑 Qwen 实验
- **距 DDL May 25 还有 9 天**，时间充裕。瓶颈是论文最终定稿 + rebuttal 质量。


---
