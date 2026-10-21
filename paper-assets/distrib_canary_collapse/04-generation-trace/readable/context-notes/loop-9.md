# director / loop_9.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`0b9ff8a738fc6f667aba.json`](../../sessions/0b/0b9ff8a738fc6f667aba.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-17T08:14:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19828 的 cuda:0 和 cuda:1，仅此两张卡
- C003 约束：禁止引用 α≤0.50 TY Granger 显著率（seed 不稳定，已证伪）
- C004 约束：禁止未确认状态下 kill 运行中进程/rm -rf 实验目录
- 论文唯一真源：本地 `docs/paper/`（D046），远程是同步副本。Paper Agent 改本地，Agent 负责 SCP 到远程编译
- 5-method 分析必须用 `run_5method_analysis.py`（family=8, n_perm=5000, q=0.05）。`analyze_alpha_sweep.py` 使用不同参数，输出已隔离到独立文件（M001 教训）
- 磁盘权威数字：s42=0/8, s43=6/8, s44=3/8（Reviewer raw p-value 铁证，Worker B 4/8,7/8,4/8 已废弃）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com), root, 2×GPU
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- 论文本地路径：`projects/distrib_canary_collapse/docs/paper/`
- 模型 cache：HF cache 含 pythia-1b, pythia-410m, gpt2-medium, facebook/opt-1.3b
- 数据：`data/wikitext103_5k/`（主数据集），`data/c4_5k/`（C4 subset，4500 samples/500 prompts）
- 活跃进程：
  - cuda:0: generalize_pythia410m_wiki_a100_s42 (PID 247554, ~6-8h, 启动约 07:00 UTC)
  - cuda:1: generalize_opt1b_wiki_a100_s42 (PID 249384, ~10-15h, 启动约 07:00 UTC)
- 磁盘：147GB 可用 (42%)

### 3. 📊 当前状态
**刚完成**：
- D053 α=0.50 三 seed 定稿（VERSION B: stochastic boundary）
- 写作打磨 8 项（Intro 重写、Contribution framing、dose-response 叙事、Related Work 补段、run-on 拆分、K=3 FPR 统一 37.5%、method.tex L30 修复、Table 1 三 seed mean±std）
- 泛化实验框架预写（experiments.tex §4.5 Table shell + limitations.tex confound 声明 + Contribution 4 placeholder）
- LaTeX 编译通过：22 页, 0 errors, cross-references 收敛

**Paper Agent 队列中**：Discussion + Limitations 深度打磨 6 项（broader implications 段落、ECE 机制解释、data domain 扩展、architecture limitation、calibration 段落改写、15 处 em-dash 清理）——可能已完成或正在处理，接手后先确认

**RUNNING 实验**：
- generalize_pythia410m_wiki_a100_s42 (cuda:0, ~13:00-15:00 UTC 完成)
- generalize_opt1b_wiki_a100_s42 (cuda:1, ~17:00-22:00 UTC 完成)

**排队**：generalize_pythia1b_c4_a100_s42（两个完成后 cuda:0 启动，~4-5h）

**Round 2 审稿提交**：apr_20260516T204821_ea5t 待用户审批，但内容已大量更新（a050_s44 + 写作打磨 + 泛化框架），完成后需重新提交

### 4. 📋 待办（条件触发式）
- Paper Agent 回复 Discussion/Limitations patch → Reviewer 验证 → Agent SCP 同步 + 编译
- Pythia-410M 完成回调 → Agent 跑 `run_5method_analysis.py` (family=8) → 汇报 per-method counts → 填 Table 5 第一行
- OPT-1.3B 完成回调 → 同上 → 填 Table 5 第二行
- 两者都完成 → cuda:0 启动 Pythia-1B + C4 实验
- C4 完成 → 填 Table 5 第三行 → 撰写 §4.5 results 段落
- 三个泛化实验全部完成 → 评估 claim 强度（能否升级 Contribution 4 为正式 claim）→ 移除 [TBD] 占位 → 重新提交 Round 2
- 用户如果对泛化结果不满意 → 可能需要加更多 α 点或 seeds

### 5. 🎯 战略上下文
- **核心结论**：单方法 FPR 62.5-100%（Pitfall 1），K=4/5 consensus 是唯一 sweet spot（Pitfall 2），α=0.50 seed-dependent boundary 证明需要多 seed（Pitfall 3）
- **决策链**：D027(reframe 方法论) → D043(EMNLP target) → D050(claim 定稿) → D052(α=0.50 seed effect) → D053(三 seed 确认 stochastic boundary)
- **用户刚说"都加"**（模型+数据集），这是用户明确要求，不可砍
- **Reviewer 评级**：borderline-to-accept。写作打磨已做两轮结构性改进，泛化实验是从 borderline 推向 accept 的关键增量
- **易错点**：
  1. 不要用 `analyze_alpha_sweep.py` 做 5-method 分析（family size 不同，M001）
  2. 论文数字改动后必须 SCP 到远程再编译，本地改≠远程改
  3. C4 subset 只有 4500 samples（vs WikiText 716K），这是 acknowledged confound 不是 bug
  4. α=0.50 PermG 数字只信 Worker A (0/8, 6/8, 3/8)，不信 Worker B
  5. em-dash 是审稿人最敏感的 AI 写作标志，每次 Paper Agent 改完都 grep "---" 验证


---
