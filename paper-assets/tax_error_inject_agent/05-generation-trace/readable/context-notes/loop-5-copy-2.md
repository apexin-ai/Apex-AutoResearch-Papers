# reviewer / loop_5.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`a1084b70e231b36b0f6f.json`](../../sessions/a1/a1084b70e231b36b0f6f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T11:53:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3 only（C001 约束）。任何进程越界立即 critical。
- Reviewer 只读：不执行实验、不修改文件、不直接回 Paper Agent。唯一输出渠道 `reviewer_post_to_director`。
- method.tex L42 当前仍写 "seed=42 only"，与 Table 2 的 3-seed 数据矛盾——已标 critical 给 Director，但尚未修复。如果看到 Paper Agent 提交新版本，**首先检查这一行是否改了**。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python3`（conda base，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- Checkpoint 目录：`/root/autodl-tmp/tax_error_inject_agent/checkpoints/`
- Eval 结果目录：`/root/autodl-tmp/tax_error_inject_agent/eval_results/`
- 论文本地路径：`projects/tax_error_inject_agent/docs/paper/`（用 Read）
- 活跃进程：无。4 GPU 全部空闲。
- 无 W&B 配置（不检查 W&B）。

### 3. 📊 当前状态
**刚完成**：D023 叙事重构后全文审查（dual regime 替代 threshold-plateau）+ Round 2 Action Matrix 独立审视。两份报告已 post 给 Director。

**关键审查结论**：
- 全文 "dual regime" 叙事一致，无残留旧表述 ✓
- Table 1 / Table 2 / Recovery / Per-operator 数据全部通过 eval 文件交叉验证 ✓
- 1 critical（method.tex seed 描述矛盾）、1 warning（Appendix per-task gap 未标 seed=42）
- Round 2 Action Matrix 可行，补充了 MF-1 criterion(3) 应改 "diagnostic" 而非 "binary vs graded"、method.tex L42 遗漏

**Registry**：77 个实验全在 PREPARING（项目不用 RUNNING/DONE 状态区分）。Random 50% s0/s123 eval 指标未写入 registry 但 eval 文件已在服务器上。

**等待**：Director 决策 Round 2 修改方案 → Paper Agent 执行 → 提交审查。可能还有 recovery eval 多 seed 补跑（我建议补但非阻塞）。

### 4. 📋 待办
- Paper Agent 提交 Round 2 修改版 → 审查 MF-1/MF-2/MF-3/SF 修改，**首查 method.tex L42 是否修复**
- Director 决定补跑 recovery eval 多 seed → 监控 GPU 合规（cuda:0-3）+ 验证结果一致性
- 新版 Figure 1 生成后 → 检查是否包含 individual seed 散点（非 error bar）
- 提交 Review Director Round 3 前 → 最终全文数据一致性扫描

### 5. 🎯 战略上下文
**核心结论**：TaxEI unpaired error injection 对 ALFWorld 无统计显著效果（-8.6pp, p=0.054）。两个竞争假设：task structure vs recovery pairing confound。

**D023 关键发现**（dual regime）：25% 注入 deterministic harm（TaxEI SD=1.2pp），50% 注入 training lottery（SD≈12pp，70.2% 异常出现在 TaxEI s0 和 Random s123 两个条件）。这替代了旧的 "shared 12.8pp threshold + plateau" 叙事。

**易错点**：
- 不要把 70.2% 异常归因于 TaxEI 特有行为——Random 也出现了，是高剂量通用现象
- full-scale（9,029 samples）和 fixed-size（4,358 samples）的方差 pattern 完全不同，不要混淆：full-scale TaxEI SD=8.6 > Random 7.0 > Vanilla 3.3，但 fixed-size 25% TaxEI SD=1.2 < Vanilla 3.3
- PALADIN "~30pp" 估计在 Discussion 中无明确来源，可能被 reviewer 追问
- Appendix per-task cross-analysis 的 "6.4pp at each dose" 只在 seed=42 成立，多 seed 下不成立（25% gap=8.5pp, 50% gap=2.1pp）


---
