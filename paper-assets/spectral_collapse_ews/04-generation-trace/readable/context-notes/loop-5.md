# director / loop_5.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`ca5c4e59dbcc1fde50c4.json`](../../sessions/ca/ca5c4e59dbcc1fde50c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-21T01:24:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1（项目配置白名单）
- r_crit 定义已改为 cross-seed mean trajectory（D034），严禁回退到 ε tolerance 方案（会级联影响 r=0.25 分类）
- Table 数据必须从 registry/results JSON 提取，禁止手工填写（M012 教训：r=0.5 D-4 曾错填 Gen 5 值）
- EMNLP 2026 main text ≤ 8 pages（limitations + refs 不计入）；当前 ~7.5p main + limitations on p8 + refs p9-10

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/spectral_collapse_ews
- 模型：EleutherAI/pythia-410m-deduped（HuggingFace pretrained）
- 数据：/root/spectral_collapse_ews/data/（50K OpenWebText subset + eval_5k.jsonl）
- Checkpoint：/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/
- 论文本地：projects/spectral_collapse_ews/paper/
- 活跃进程：exp_014 (tmux=exp_014, cuda:0, r=0.25 seed43)；exp_013 (cuda:1, r=0 seed44)
- 无 W&B / 无 Git remote

### 3. 📊 当前状态
所有不依赖新数据的论文改进已完成（α sensitivity、§3.3 压缩、Significance 提升、overclaim 修复、Neural Collapse 定位、D034 cross-seed mean 定义、D-4 方差句、controller non-triviality）。等两个实验出数据。

Registry RUNNING:
- **exp_013**: r=0 seed44 pure collapse, cuda:1, ~Gen 6-7, ETA May 21 晚。第三 seed，Table 1 升 3-seed mean±std
- **exp_014**: r=0.25 seed43, cuda:0, ~Gen 1-2, ETA May 22 上午。堵 cross-seed mean 方法论不对称（D035）

磁盘：21GB 可用（exp_012 中间 checkpoint 已清理）。

### 4. 📋 待办
- exp_014 Gen 0-3 完成 → 检查 r=0.25 EMA 违反是否跨 seed 复现（关键验证：若复现则 r_crit bound 稳固；若不复现需要重新评估 cross-seed mean 定义）
- exp_013 完成 → Table 1 升级 3-seed mean±std + HellaSwag eval seed44（cuda:1 上跑，~2.5h）+ Limitations 更新为 "three seeds complete"
- exp_014 完成 → Table 3 r=0.25 行升级 2-seed mean±std + 验证 cross-seed mean 下 r=0.25 仍为 Type II
- 两个都完成 → Phase E final pass: Discussion/Conclusion/Abstract 数字对齐 + 编译验证 ≤ 8p + 提交 Reviewer 最终审查
- α sensitivity 需要在 exp_014 完成后对 r=0.25 cross-seed mean 也重新验证

### 5. 🎯 战略上下文
- **核心结论**：Spectral collapse 在 iterative synthetic training 中呈三阶段（decompression→onset→acceleration），r_crit ∈ (0.25, 0.3] 分隔 Type II（transitional）和 Type III（stable）。Signal attenuation paradox 使 reactive controller 在 r ≥ r_crit 时完全失效。
- **决策链**：D029 收紧 r_crit → D031 维持 (0.25, 0.3] → D033 绝对速率替代 2.43× → D034 cross-seed mean 定义（ε 撤回）→ D035 补 r=0.25 seed43
- **易错点**：(1) r=0.3 seed43 个体 EMA 违反 0.83 点——但 cross-seed mean 通过，不要被个体 seed 数据误导回 ε 方案；(2) D-4 cross-seed 方差极大（r=0.3: .342 vs .122），不要把 D-4 的 seed 差异当 bug——这是 SLV/D-4 正交性的实证；(3) Reviewer 预估 Overall 3.0-3.5，冲 4.0 的关键是 exp_014 堵住方法论不对称 + Phase E 写作质量
- **DDL**：May 25 ARR，还有 ~4 天


---
