# director / loop_14.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`a39986e9cbd5b0e0828d.json`](../../sessions/a3/a39986e9cbd5b0e0828d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-21T10:32:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5, westd-19828 cuda:0-1（共 8 卡），严禁使用其他 GPU
- ≤3B 模型用 fp32，>3B 用 bf16（D079）
- predict-then-verify: v1 committed score = 3/5 为 primary，v2 未 commit = 4/5 仅作 sensitivity analysis（M057）
- α=0.25 T=20 不在锁定预测文件中，不得标记 EXACT_MATCH（M056）
- TY=7/8 已被 D143 retract，论文不得引用
- CSD 仅限 Discussion 章节（D142）
- 17855↔19828 SSH 不通
- FPR 不再是 zero：s45 出现 2/8，累积 2/32=6.25%，措辞用 "near-zero FPR"（D167）
- R²=1.000 已从论文移除（同义反复），改报 R²=0.883（D168/F7-C1）
- "first-principles" 已改为 "parametric explanation"（F7-C5）

### 2. 🖥️ 基础设施快照
- 服务器：westd-17855 (6×RTX PRO 6000 Blackwell 98GB) + westd-19828 (2×RTX PRO 6000 Blackwell 98GB)
- SSH: connect.westd.seetacloud.com（端口见 ~/.ssh/config）
- 工作目录：/root/autodl-tmp/distrib_canary_collapse/
- Python：/root/miniconda3/bin/python（conda base，不用 venv）
- HF_HOME=/root/autodl-tmp/.hf_cache, TRANSFORMERS_OFFLINE=1
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/
- Phase Diagram 脚本：`scripts/phase_diagram/run_t{05,15,25}_a{045,050,060,075}_s42.sh &lt;GPU_ID>`
- Worker 池在 Loop 14 session 中已耗尽（10+ workers），新 session 应恢复

### 3. 📊 当前状态
**刚完成**：R7 审稿提交 + R7 审稿报告处理 + Paper Agent 8 项修复全部完成。D37-D α_c closed-form 理论完成（D165）。GPT-2m s43 fp32 = 6/8 确认 2-seed consistent（D166）。

**RUNNING 实验**（Agent 最后报告时，可能有变化需验证）：
- 17855:0 a000_s47_fp32 (null seed #6)
- 17855:1 phase_diagram_t05_a045_s42 (PID 493673, Phase Diagram 第一组)
- 17855:2 phase_diagram_t05_a050_s42 (PID 497281, Phase Diagram 第二组)
- 17855:3 scale_69b_a100_s43_bf16 (cross-seed)
- 17855:4 a052_s43_fp32 (boundary multi-seed)
- 17855:5 a046_s43_fp32 (boundary multi-seed)
- 19828:0 a000_s48_fp32 (null seed #7)
- 19828:1 a000_s46_fp32 (null seed #5)

**4 方向突破进展**：
1. Phase Diagram (α×T): T=5 α=0.45 + α=0.50 在跑，代码全部就绪（12 组脚本），等 GPU 释放继续
2. Spec Curve: ✅ 完成
3. TE/MI: ✅ 完成（D162，仅 2/8 对支持"高MI低TE"）
4. Detection Lower Bound: ✅ v2 完成（D164，α_c(T=10)=0.487）

**Paper Agent**：R7 Action Matrix 8 项修复全部完成（C1 R²→0.883, C2 five families, C5 parametric, C7 2pp, C8 Limitations 3点等）。编译通过。

### 4. 📋 待办（条件触发式）
- Phase Diagram T=5 α=0.45/α=0.50 完成 → 立即 5method 分析 + 汇报结果。α_c theory 预测 T=5 α_c≥1.0（不可检测），如果 0/8 → 理论验证 ✓，如果 >0/8 → 理论需修正
- a046_s43/a052_s43 完成 → 释放 GPU 给 T=5 α=0.60 和 α=0.75
- scale_69b 完成 → 释放 GPU 给 Phase Diagram T=15
- a000_s46/s47/s48 (null seeds) 完成 → 计算最终 FPR CI。如果累积 <5% → "FPR controlled at nominal α=0.05"；如果 >5% → 加 caveat
- T=5 四组全部完成 → 开始 T=15（4组），最后 T=25（4组）。总计 ~82.8 GPU-hours
- Phase Diagram 全部完成 → 绘制 α×T 2D 热力图（论文核心 figure）→ Paper Agent patch 入论文 → R8 提交
- Paper Agent 修复已完成但未重新提交 Reviewer（Director 指令：factual 修正不改 framing）。下次 resubmit 应在 Phase Diagram 结果集成后

### 5. 🎯 战略上下文
- **核心转型**：论文从"方法论文"(3.0 Findings) 转为"现象发现论文"(Mapping the Detectability Landscape)。用户批准，R7 Reviewer 确认方向正确
- **Phase Diagram 是最高价值方向**：一张 α×T 2D 热力图就能改变审稿人认知。T=5 的 α_c≥1.0 预测是关键验证点
- **D165 α_c closed-form 是理论亮点**：α_c(T) = α_∞ + A·T^{-1/(2β)}, β=0.208, 与经验拟合 Δγ=0.002 收敛。但已被 Reviewer 指出不能称 "first-principles"（已修为 "parametric"）
- **最容易判断错的事**：(1) 不要在论文恢复 R²=1.000（已确认为同义反复，D168）；(2) T=5 如果出现 >0/8 检测，不要恐慌——可能意味着理论需要 refinement 而非失败；(3) FPR 不再是 zero（D167），s46/s47/s48 结果可能进一步升高或确认为 marginal；(4) C4 cross-domain 数据不足（只有 α=1.0 一个 C4 点），不要 overclaim cross-domain validation
- **168 个决策记录**在 decisions.yaml，最近关键：D165 (closed-form), D166 (gpt2m 2-seed), D167 (FPR non-zero), D168 (R7 action matrix)
- **57 个错题本**在 mistakes.yaml，最近关键：M056 (predict-then-verify post-hoc), M057 (v1 vs v2 score), M058 (detection bound hardcoded data)


---
