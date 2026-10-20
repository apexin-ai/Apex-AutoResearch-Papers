# reviewer / loop_12.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`c015c06d4ae9d2f6d8c2.json`](../../sessions/c0/c015c06d4ae9d2f6d8c2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-22T21:50:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16639:cuda:0-3, westd-14391:cuda:0。越界进程必须立即 CRITICAL 打回
- D061 alphabetical tiebreaking 是唯一正确标准：`sorted(tied)[0]`。trace 文件中的 `sc_answer` 字段使用旧 insertion-order tiebreaking，**不可直接引用**——必须从 vote distribution 重算
- 论文 SC baseline 必须全表统一到 D061 值，不能混用 stored 和 D061
- Reviewer 只读、只通过 `reviewer_post_to_director` 输出，不执行实验、不修改文件

### 2. 🖥️ 基础设施快照
- **westd-16639** (4× RTX PRO 6000 96GB)，代码根 `/root/symb_invariant_consensus`
  - cuda:0: vLLM Qwen2.5-14B port 8001 → PW seed456 (PID 663049 runner)
  - cuda:1: vLLM LLaMA-8B port 8006 → PW chain seed123→456→789 (PID 685307)
  - cuda:2: vLLM Mistral-7B port 8003 → PW seed789 (PID 510987 runner)
  - cuda:3: vLLM Qwen2.5-14B port 8005 → PW seed123 rerun (PID 685233)
  - 磁盘：根 35% (20G free), 数据盘 66% (121G free)
- **westd-14391** (1× RTX PRO 6000 96GB)，代码根 `/root/symb_invariant_consensus`
  - cuda:0: vLLM LLaMA-8B port 8000 → PW seed42, chain monitor `/tmp/monitor_chain.log`
  - FOLIO seed789 刚完成 (204/204)，PW seeds 42→123→456 链式执行中
  - 磁盘充裕 (225G free)

### 3. 📊 当前状态
**我本轮完成的审查：**
1. Qwen PW seed123 数据损坏发现（161/600 空响应）→ CRITICAL，已安排 cuda:3 重跑
2. 论文跨表 SC baseline 不一致（Table 1 vs Table 3 混用新旧 tiebreaking）→ CRITICAL
3. Zero-shot DeBERTa combo D061 重算：LLaMA 所有 combo gains 失去显著性 → CRITICAL（bridge case 论点失效）
4. Table 1 Qwen3 FOLIO SC/SICA 填反 + Qwen14B FOLIO 两列来源错误 → CRITICAL
5. Sign test 从 5+/10− p=0.30 更新为 8+/7−/1tie p=1.00
6. 75.49% 级联审计（7 处 SC 列 + 3 处 Oracle Δ 需更新）
7. BR 重算 Qwen14B: 3.93→3.85（微调，不影响结论）
8. RoBERTa/BART multi-NLI: D061 已正确，无需修改
9. DRC 表: FOLIO 行正确，PW SC only 39.17→39.33
10. Figure 6+7 重生成完成

**ROADMAP V18 剩余：**
- D061 changelist 21 处确认修改 + 17 处待确认（`artifacts/d061_changelist.json`）
- Multi-NLI 表 DeBERTa 3 行 Δ 更新 + caption SC
- 最终编译 + submit_paper_to_review → 5/24
- May 25 EMNLP ARR 提交

**多 seed 实验进度：**
- Mistral PW: 4 seeds 全部完成 ✓（Δ 全负，SCB 确认）
- Qwen FOLIO: 4 seeds 全部完成 ✓（mean Δ=-1.24±0.86）
- Qwen PW: seed42 (baseline), seed456 运行中, seed789 排队, seed123 重跑中
- LLaMA FOLIO: seed123 完成, seed789 刚完成, seed456 排队
- LLaMA PW: seed123 运行中 (cuda:1), seed42 运行中 (14391), seed456/789 排队

### 4. 📋 待办（条件触发式）
- 新 worker_done 到达 → 检查结果，重点关注 D061 changelist 剩余 17 处修改是否落地
- Qwen PW seed456/789/123-rerun 完成 → 验证无空响应，核查 SC/SICA 与 baseline 方差是否合理（seed123 原始结果 SC=52.5% 是异常值，正常应 ~74%）
- LLaMA PW seeds 完成 → 核查 SC 是否与 D061 值 72.50% 一致（而非旧 70.00%）
- Paper Agent 最终编译通知 → 触发全文 consistency check：所有表格 SC/Δ/p 是否统一到 D061
- `submit_paper_to_review` 触发 → 按 §5 审查模式 B 做对抗审查

### 5. 🎯 战略上下文
- **D061 是本轮最大的系统性问题**：trace 文件 `sc_answer` 用 insertion-order tiebreaking（Unknown 优先），D061 用 alphabetical（False 优先）。影响所有 SC baseline、combo Δ、sign test、BH 校正、Spearman 相关。D152 决策统一到 D061，但 changelist 有 38 处需改，截至 handoff 时约 21 处已确认、15 处已 patch。
- **LLaMA bridge case 已死**：D061 后 zero-shot combo 在 LLaMA 上全部不显著（+0.83pp p=0.359）。论文 solutions.tex 需改叙事——从"gradient"改为"binary split"（只有 Mistral 获益）。FT combo 对比反而更强（14× vs 旧 3.5×）。
- **易错点**：`r["sc_answer"]` 是旧值，`sc_answer(votes)` 才是 D061。任何读取 trace sc_answer 的脚本产出都是旧 tiebreaking 数据。
- **Qwen3 FOLIO Δ=+1.47 是 SCB 反例**：修正后这是 Table 1 中少数 SICA > SC 的格。但 sign test 整体仍平衡（8+/7−/1tie p=1.00），SCB 叙事成立。
- **39.33% vs 39.17%**：r11 脚本有 2 问 ID fix (Q4→Q8)，多 1 题正确。Paper 部分表用 39.17（无 fix），部分用 39.33（有 fix），需统一。


---
