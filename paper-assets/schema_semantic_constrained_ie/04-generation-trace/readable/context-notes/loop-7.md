# director / loop_7.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`a8c3ad0ff716d418a781.json`](../../sessions/a8/a8c3ad0ff716d418a781.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-17T07:19:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 westd-16980 和 westd-21461 两台服务器。westd-37397 已关机移除，不要尝试连接
- Qwen3-8B-ms 模型**只在 westd-16980**（`/root/autodl-tmp/models/Qwen3-8B-ms`）。westd-21461 只有 Mistral。不要在 westd-21461 上跑 Qwen/Llama 实验
- 禁止设 `fix_mistral_regex=True`——会把 Qwen regex 替换成 Mistral tekken regex 导致结果错误
- Worker 启动实验前必须 `ps aux | grep` 检查是否已有同名进程（已两次出现双进程写同一文件 bug，M001）
- GTC (Layer 3) 已确认无效（D036），不要再跑任何 GTC 实验

### 2. 🖥️ 基础设施快照
- **westd-16980**: 2×GPU，conda base env，`/root/miniconda3/bin/python`，项目目录 `/root/schema_semantic_constrained_ie`
  - Qwen3-8B-ms: `/root/autodl-tmp/models/Qwen3-8B-ms`
  - Llama ZS: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Llama FT checkpoints: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged` 等
  - 活跃进程: Llama DocRED beam 50 (PID 424211, tmux `llama_docred_beam`, cuda:0)
  - cuda:1: 空闲
- **westd-21461**: 2×GPU，只有 Mistral 模型，cuda:0/1 空闲

### 3. 📊 当前状态
**刚做完**：
- Beam search 4 组全部完成：Qwen SciERC 551 (DR=0%), Llama SciERC 551 (DR=0%), Qwen DocRED 50 (DR=0%), Mistral DocRED 50 (DR=21.4%)
- Stability 3 seeds 确认 std=0（greedy 完全确定性）
- GTC Layer 3 实验确认无效（D036），已清理归档
- Appendix beam_search.tex 包含完整 4-row 表格 + GTC 失败分析段落
- Rebuttal v2 全部修正完成（CF 9.90, DR 1.95, beam qualification, sampling, stability）
- LaTeX \ref 断裂已修复（sampling + beam appendix 已 \input）
- Group C fresh review 已提交（apr_20260516T210044_o9ce），等报告

**RUNNING**：
- w10_llama_docred_beam_50 (PID 424211, westd-16980 cuda:0, ~30-50min ETA)

### 4. 📋 待办
- Llama DocRED beam 50 cron 回调 → 收集结果 → 更新 appendix beam table 加第 5 行
- Group C fresh review 报告回来 → Read `review-report-action` skill → Holistic Pass + Per-Comment Action Matrix
- Llama DocRED beam 完成后 → beam 矩阵 5/5 done → post_to_reviewer 讨论最终 claim 强度
- 所有 beam 数据就绪 → 考虑是否 re-submit_paper_to_review 让 Group C 看最新版
- 论文最终稿就绪 → log_decision D037 → 提交 ARR

### 5. 🎯 战略上下文
- **核心结论**：Grammar 层消除 ET/RV，Semantic 层消除 DR，两层互补（8/8 FT ablation 一致）。Beam search 是唯一能同时降低 CF+DR 的方法（CF↔DR 互斥已被 GTC 实验证实）
- **Beam search 是本轮最大收获**：calibrated models beam→DR=0%（2 models × 2 datasets），远超"future work"预期。但保持 appendix 定位不升级 main contribution（Reviewer 建议：覆盖不完整，避免 overclaiming）
- **Group C 审稿的核心问题是 overclaiming**，不是实验不足。修好 framing + 强 rebuttal 比补实验更有效
- **R² dual-factor**：保留 n=4 R²=0.886（τ̄ × RV_baseline），Mistral 作为 boundary condition
- **易错点**：(1) Agent 经常启动重复进程写同一文件；(2) Paper Agent 连续出现数据错误（任何 patch 后必须经 Reviewer 核实）；(3) "calibrated" 术语无正式定义——论文中用 "models with reasonable entity type accuracy" 替代
- **距 DDL May 25 还有 8 天**，时间充裕。瓶颈是 Group C 报告 + 最终定稿质量


---
