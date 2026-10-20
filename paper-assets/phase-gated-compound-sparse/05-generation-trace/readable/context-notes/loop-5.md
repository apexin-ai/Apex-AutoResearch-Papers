# director / loop_5.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`aae8412239d11116bf90.json`](../../sessions/aa/aae8412239d11116bf90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T16:48:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 cuda:0-3（4 张 RTX 6000 Pro），不可越界
- GSM8K profiling DS importance 数据已退化（II_low 全 0.0），**不可引用 DS GSM8K importance 数据**直到诊断完成确认是 code bug 还是真实特性
- Appendix B multiplicative G 已更新为校准值（G_× ≈ 51-183×），带脚注标注非精确值——不可声称为精确 n=500 计算
- Paper Agent 文本修改 15/15 已完成，"discrimination collapse" 已全文重命名为 "importance discrimination collapse"（不是 "importance score flattening"）
- headline 数值已修正为 "3-17× where both strategies show significant phase gradients (s≥0.25)"——禁止回退到 "3-39×"

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，account: root
- 工作目录：/root/autodl-tmp/pacs
- GSM8K profiling 脚本：`run_profiling_gsm8k.py`（统一版，min_phase_length=10, n=50, seed=42, save_generations）
- GSM8K 数据：`gsm8k_test.json`（1319 题）
- 论文 tex：本地 workspace `projects/phase-gated-compound-sparse/docs/paper/`
- n=500 数据：`artifacts/n500_analysis/table2_n500_full.csv`
- 活跃进程：QW GSM8K profiling cuda:2 (importance) + cuda:3 (random)，DS 已完成/失败释放 cuda:0,1
- BibTeX artifact: art_20260515_3e608b（ThinK/ForesightKV/PQQP/LKV）

### 3. 📊 当前状态
**刚做完**：Round 8 Action Matrix D071 全部派发并执行——Paper Agent 15/15 文本修改 done，引用填入 done，Appendix B G 值更新 done。

**正在进行**：
- GSM8K profiling QW：cuda:2,3 运行中（random 38/50 时的快照，应接近完成）
- GSM8K DS 诊断：已派 Agent 在 cuda:0 跑 n=3 diagnostic run，查 II_low=0 是 code bug 还是短序列退化
- QW importance 输出目录可能为空（需 Agent 确认）

**等待回调**：
- Agent 诊断 DS II_low=0 根因
- Agent 报告 QW profiling 最终结果
- RESET_BOTH 已批准但 handoff 先于执行——新 session 启动后需立即跟进 Agent 回复

### 4. 📋 待办
- QW GSM8K 完成 + QW II_low 非零 → QW 数据可用于 cross-dataset claim；DS 退化放 Appendix 讨论
- QW GSM8K 也退化（II_low=0）→ GSM8K phase modulation 整体弱于 MATH-500，降级为 Appendix limitation（"partially replicates"）
- DS 诊断确认是 code bug → 修复后 cuda:0,1 重跑 DS profiling
- DS 诊断确认是真实特性（短 trace phase segmentation 退化）→ 不重跑，诚实报告
- GSM8K 最终数据就绪 → Paper Agent patch 新 section/appendix + consistency check → 提交 Group C Round 9
- Round 9 提交后 → 审稿期间 GPU 铺 ablation（sparsity range 扩展 s=0.40/0.50 等）

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 ARR，截稿 2026-05-25（~9 天）
- 经过 8 轮内审，从 Borderline → Weak Reject，核心阻碍：单 benchmark + construct validity（PPL vs accuracy）+ additive null 矛盾
- D071 是转折点：additive null 正面论证已写入、novelty argument 重写完成、pilot 移 Appendix——文本层面回应了全部 R8 concerns
- GSM8K 是唯一能改变分数的新实验证据——但 DS 退化意味着可能只有 QW 数据可用
- **最容易判断错的事**：如果 QW 也退化，不要试图"修复"或硬凑数据。诚实报告 "GSM8K phase modulation weaker" 比造假数据强得多——审稿人尊重诚实的 negative finding
- **另一个坑**：Paper Agent 已经把 "cross-model" 全文替换为 "cross-training-paradigm"——不要回退
- 决策链：D063(threshold story) → D067(R6 matrix) → D069(R7 matrix) → D070(skip N1b) → D071(R8 matrix, 当前)


---
