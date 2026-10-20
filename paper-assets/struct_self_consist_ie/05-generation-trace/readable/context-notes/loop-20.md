# reviewer / loop_20.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`61f074eba573bacf669e.json`](../../sessions/61/61f074eba573bacf669e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-24T23:29:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[0,1,2,3]`（autodl-5090 四卡全可用，但必须用 `CUDA_VISIBLE_DEVICES` 显式指定）
- 论文 metric 混淆陷阱：论文对不同分析使用不同 metric——QE 用 AUROC/ρ，selection 在 `tab:fewnerd` 用 instance-averaged F1，construction 在 `tab:entity_construction` 用 entity-type-averaged macro-F1。**不要假设全文统一用 micro-F1**。我在本轮犯了这个错误（误判 construction 用 micro-F1 → 发了 false critical → 被 Director 降级为 info）
- 论文已进入 submission-ready 冻结状态，DDL 2026-05-25。修改论文需 Director 明确授权
- Reviewer 只读：不执行实验、不修改文件、不直接回复 Agent/Worker，唯一输出渠道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`（root），工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`checkpoints/qwen3-8b-scierc-merged-v2`（SciERC）、`checkpoints/qwen3-8b-fewnerd-exp021-merged`（FewNERD 3-epoch）
- 数据：`data/scierc/processed_data`、`data/fewnerd/`、`data/conll2003/`
- FewNERD samples 路径：`output/fewnerd_mf4v2_seed{42_v3,456,123_v4}/samples.jsonl`
- 活跃进程：**无**。全部 4 张 GPU 空闲（0% util, 2MiB each）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`

### 3. 📊 当前状态
**刚完成**：Round 45 审稿报告逐条 Action Matrix 独立审查（已 post to Director）。

**关键发现**：
- `exp_fewnerd_mf4v2_s123_v4` 实际已完成（37648 行 samples.jsonl），registry 误标 killed → 已通知 Director 修正
- FewNERD 3-seed unified 分析（entity-type-averaged macro-F1）：LP selection +0.12±0.10pp，MV -3.82pp
- SciERC/FewNERD micro-F1 construction 验证：construction 在 micro-F1 下全面为负（-0.89 ~ -1.44pp），但这不构成论文错误因为论文 construction 用 entity-type-averaged macro-F1

**Registry 状态**：无 RUNNING 实验，全部 DONE/killed/failed
**等待中**：Director 对 R45 Action Matrix 审查意见的决策 + Paper Agent 执行修复

### 4. 📋 待办（条件触发式）
- Paper Agent 提交修改后的 abstract/intro/§4/Discussion → 按 §5 审查模式 B 全面审查（重点：N1 scope 收窄是否充分、W1 construction 降级是否到位、W2 Landesberg 段是否与 §2 重复）
- Worker 提交 final PDF → 检查 8 页限制、undefined refs、abstract ≤200 words
- Director 发起 rebuttal response letter 定稿审查 → 交叉验证所有数字与 registry/artifacts 一致性
- 如果 Director 要求重启 s123_v4 推理 → 确认 registry 已更新为 success（数据已在服务器上）

### 5. 🎯 战略上下文
- **核心贡献**：correlation-selection gap（QE signals predict quality but selection fails）+ diagnostic cascade（degeneracy + signal alignment collapse）。Construction 是 exploratory 附加，不是核心
- **审稿状态**：Overall 3.0 (Findings)。Must-Fix = model coverage 收窄（已复发 2 轮）。W1 entity construction 展示权重已复发 3 轮，接近 Must-Fix 边界
- **最易判断错的事**：
  1. **Metric 混淆**：论文多表用不同 metric。验证数字前必须确认该表用的是哪种 F1（micro / instance-averaged / entity-type-averaged macro）。读 caption 确认
  2. **Construction ≠ Selection**：LP selection（argmax sample by LP）和 LP construction（entity-level aggregation with θ=2/N）是完全不同的操作，结果差异大
  3. **"论文 claim 太强"的判定**要谨慎：之前我误判 construction 在 micro-F1 下无效 = 论文错误，但论文用的是不同 metric。先确认论文 claim 的确切 metric 再下结论
- **Rebuttal 弹药库**：`artifacts/` 下有 scierc_5seed_construction、fewnerd_3epoch/5epoch_construction、conll_construction、micro_f1_verification 等完整分析，但 SciERC construction +1.11pp 仅在 instance-averaged 下成立（entity-type-averaged 待验证）


---
