# director / loop_8.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`ec4c44e083154fce3c5f.json`](../../sessions/ec/ec4c44e083154fce3c5f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-19T09:52:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-33015 cuda:0,1,2,3 + westd-27271 cuda:0,1，共 6 张
- 论文是 **ANALYSIS/DIAGNOSTIC paper**，不是 METHOD paper（D075）。Smart Compress 是诊断实验，不是方法贡献。任何写作/实验决策必须符合这个定位
- 标题已改为观察性（"Vision Connectors and VLA Token Compressibility"），全文因果语言已降级为 "co-occurs with" / "associated with"，不要回退到因果 framing
- CogACT 数据已修正：97.8% 是错误的（张冠李戴），正确数据是 74.8%→74.2%（保留率 99.2%），来自 EfficientVLA
- seed43 M=16/M=128 不需要做（D078），实验矩阵已 sufficient
- 正文 ≤ 8 页（CoRL 限制），当前恰好 8 页

### 2. 🖥️ 基础设施快照
- **cqa1-33015**：4× RTX 4090D 24GB，工作目录 `/root/autodl-tmp/importance_margin_vla_compress`
  - SmolVLA 训练/eval 全在这台
  - Python: `/root/miniconda3/bin/python`
- **westd-27271**：2× RTX PRO 6000 Blackwell 98GB，工作目录 `/root/autodl-tmp/importance_margin_vla_compress`
  - OpenVLA entropy 数据在 `eval_results/openvla_attention_entropy_real.json`
  - SmolVLA entropy 数据在 cqa1 `eval_results/smolvla_attention_entropy_perlayer_fixed.json`
- **论文本地路径**：`projects/importance_margin_vla_compress/docs/paper/`（main.tex, references.bib, 各 section .tex）
- **活跃进程**（handoff 时刻）：
  - cqa1:0,1,2 — seed44 M=32/64/96 eval（PID 762596/763351/764777）
  - cqa1:3 — M=32 official 训练刚完成，eval 可能已启动（Agent 正在处理）
  - westd:0 — MLP adapter control 训练（tmux `mlp_adapter_control`，~step 25K/100K，sps=3.5）
  - westd:1 — M=128 seed44 训练（PID 459645，~step 40K+/100K）

### 3. 📊 当前状态
**刚做完**：Round 3 审稿报告处理（weak reject 4-5/10），论文 16 项修改全部完成（§4.3 瘦身、标题/语言降级、surprise hook、Design Implications、entropy causal chain、GridS 定位、CogACT 数据修正、4 缺失引用、proofread 13 处 -ing 修复、cross-suite 讨论、latency→memory reframe、Section 3 标题、frozen params、术语修正、offline metric 论证）。

**正在等待的关键实验**：
| 实验 | 位置 | 状态 | 预计剩余 | 重要性 |
|------|------|------|---------|--------|
| seed44 M=32/64/96 eval | cqa1:0,1,2 | RUNNING eval | ~2-3h | 3-seed 数据→appendix |
| M=32 official eval | cqa1:3 | 训练刚完成，eval 待启动 | ~4-5h | **MF-2 关键**：增益能否在强 baseline 复现 |
| MLP adapter control | westd:0 | 训练中 ~25% | ~5-6h | **MF-1/SF-3 最关键**：capacity vs re-encoding |
| M=128 seed44 | westd:1 | 训练中 ~40% | ~3-4h | bonus |

**Agent 队列**：正在处理 M=32 official 完成回调 + 我派的全卡状态检查

### 4. 📋 待办（条件触发式）
- seed44 M=32/64/96 eval 完成 → 更新 Table 8 为 3-seed mean±std，放 appendix
- M=32 official eval 完成 → **关键分叉**：
  - SR > 62% → re-encoding 在强 baseline 有增量，MF-2 解决，写入正文
  - SR ≈ 59% → re-encoding 只补偿训练不足，需诚实承认，Claim 4 scope 限定
  - SR < 55% → 异常，调查
- MLP adapter eval 完成 → **最关键分叉**：
  - MLP ≈ 45% → capacity 不解释提升，re-encoding 是机制 → MF-1/SF-3 彻底解决，写入正文作为新 control
  - MLP ≈ 55-60% → 任何参数都帮忙 → Claim 4 需大改
- M=128 seed44 eval 完成 → 更新 appendix 3-seed passthrough 数据
- 所有实验完成 → post_to_reviewer 评估最终证据链 → submit_paper_to_review Round 4
- westd 空闲后 → 考虑 OpenVLA cross-suite eval（LIBERO-Spatial/Goal，回应 MF-3 不对称）

### 5. 🎯 战略上下文
- **核心决策链**：D075（METHOD→DIAGNOSTIC）→ D076（§4.3 瘦身）→ D077（CoRL 三项强化）→ D078（实验矩阵已充分）→ D079（MLP adapter 最高优先级）
- **三轮未解决的核心问题**：scale confound（MF-1）。MLP adapter 是最后一张牌——如果结果好（MLP≈45%），这是论文最强新证据；如果结果不好（MLP≈60%），Claim 4 需要根本性重写
- **CoRL 天花板**：Reviewer 评估即使全部修复到位，6/10 是天花板（纯 analysis + sim-only）
- **易错点**：
  - references.bib 的 orphan 条目反复出现（Agent 多次重新添加被删除的条目），每次 Agent 改 bib 后都要 grep 检查
  - `sections/` 目录下是旧 draft 文件，`main.tex` include 的是顶层 `.tex` 文件，不要混淆
  - registry 与实际 GPU 状态经常漂移，每次催促都要 Agent SSH 确认实际进程
  - 4 篇竞品全部只测 MLP-projector VLAs，我们的 pixel-shuffle cliff-edge 分析确实无人做过（Claim 2 安全）
  - GridS (See What Matters) 不分析 pixel-shuffle 机制，只提 continuous resampling 方案，定位为互补


---
