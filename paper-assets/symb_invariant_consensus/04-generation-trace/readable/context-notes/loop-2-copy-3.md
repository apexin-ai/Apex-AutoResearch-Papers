# reviewer / loop_2.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`d1e547bcbe488c70d912.json`](../../sessions/d1/d1e547bcbe488c70d912.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T18:55:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 只有 cuda:0**（单卡 RTX PRO 6000 Blackwell 98GB），`execution.gpu_ids=[0]`，越界即 CRITICAL
- **v3 运行期间禁止任何非实验进程向 vLLM 发请求**——之前诊断脚本洪泛把 KV cache 挤到 99.6%、吞吐降 31%，又有 rescore_full.py 违规被我 flag。这是事故后硬规则
- **memory.md 不可被覆写为分析报告**——本轮已发生一次（worker 用 rescore 报告覆盖了整个 memory.md），已报 CRITICAL，Director 已恢复
- **P5 "120→80 翻转" 声明不可靠**——`old_sica_known: 120` 是硬编码假设值（rescore_pure.py L10），实际 checkpoint 显示旧 SICA 也选了 80。不要引用这个作为 A+C scorer 的实证

### 2. 🖥️ 基础设施快照
- **服务器**: westd-32608, root, `/root/symb_invariant_consensus`
- **Python**: `/root/miniconda3/bin/python`（conda base，不用 venv）
- **vLLM**: PID 129131, port 8000, QwQ-32B FP16, max_model_len=16384, gpu_memory_utilization=0.90
- **模型**: `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`（ModelScope 嵌套路径）
- **主实验**: PID 129992, `sica_aime30_v3` RUNNING, log: `/root/runs/symb_invariant_consensus/sica_aime30_v2_resume.log`, output: `results/aime30_v2.json`
- **数据**: AIME `data/aime2024_subset.json` (30题), MATH `data/math500_subset.json` (50题), ProofWriter `data/proofwriter_subset.json` (10题)
- **磁盘修复代码**（v3 未加载，v4 生效）: scorer.py (A+C), z3_maxsat.py (comprehensive parser + Int-first + sort unification), trace_generator.py (answer fallback + logic prompt), pipeline.py (domain routing)

### 3. 📊 当前状态
**sica_aime30_v3**: 20/30 完成，P21 (GT=294) 正在 trace 生成中，ETA ~111 min（10 remaining）

20/30 汇总: **SICA=SC=14/20 (70%), 0pp gap**。20/20 题 SICA=SC 完全一致。
- C1 extraction ≥50%: ✅ 74.4%
- C2 contradictions ≥5: ✅ 10+ 题有矛盾
- C3 SICA ≥ SC+2pp: ❌ 0pp，结构性问题（旧 scorer + 旧 parser）

本轮已发 ~17 条审查报告给 Director，覆盖：资源竞争 CRITICAL、scorer/parser 代码审查、rescore 分析、memory.md 覆写 CRITICAL、P5 翻转质疑、Int/Real sort fix、answer extraction fix、ProofWriter 适配、v4 准备状态汇总。

### 4. 📋 待办
- **v3 完成（30/30）→** 立即做 D003 最终评估（C1/C2/C3），确认 PASS/INCONCLUSIVE/FAIL，报 Director
- **v4 启动后 →** 验证修复代码确实被加载（检查 import 时间戳 vs 进程启动时间），特别关注 answer extraction fallback 是否增加了 SC votes
- **v4 P5/P7/P10/P20 完成 →** 重点审查这 4 题（非 unanimous SC + 高矛盾率），看 A+C scorer + 新 parser 是否产生 SICA≠SC
- **MATH-500 rerun →** 验证 math 域路径未被 ProofWriter 适配影响（pipeline.py domain routing）
- **ProofWriter 10 题 →** 验证 LOGIC_PROMPT + normalize_logic_answer 正确工作
- **若 v4 仍 0pp →** 这是 SICA 方法论的根本局限（QwQ-32B 在可解题上 SC 太集中），需要报 Director 准备 FAIL 路径决策

### 5. 🎯 战略上下文
**决策链**: D001(MVP方案) → D002(拒绝CRD回归SICA) → D003(三档判定标准) → D004/D005(MATH+AIME双管齐下) → D006(kill MATH优先AIME) → D007(parser是根因，v3收traces，v4重打分)

**核心结论**: SICA 0pp gap 的根因是**双重的**：(1) 旧 z3 parser 丢失 41-100% 约束（P7: 72→1），MAX-SAT 无材料可用；(2) 旧 scorer 忽略 excluded constraints，即使检测到矛盾也不影响答案选择。两个修复都在磁盘上等 v4。

**最容易判断错的事**:
- **不要因为 20/20 SICA=SC 就判 SICA 方法失败**——当前 v3 用的是 BUG 代码，真正的验证是 v4
- **不要套人类工时直觉**——"30 题跑了 3 小时太慢" 不是问题，唯一的时间约束是 5/19 DDL vs GPU-hours
- **P5 "翻转" 是假的**——被多个 worker 和 memory.md 传播，实际 checkpoint 显示旧 SICA 也选 80
- **QwQ-32B 在可解题上 SC 极度集中**（12/12 或 11/12）——这不是 bug 而是 reasoning model 的本质特征，SICA 的价值只能在 SC 不集中的题目上体现（P5/P7/P10/P20）


---
