# reviewer / loop_14.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`5e2ac5502966da23bb1a.json`](../../sessions/5e/5e2ac5502966da23bb1a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-21T18:43:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- D102 标准：所有 5method 分析必须用 downstreams=[distinct_1,distinct_2,distinct_3,mauve] + threshold_criterion=true_3sigma_d105。用 perplexity 或 3x_sigma_drift 的结果一律 CRITICAL 打回。已有前车之鉴：t15_a045 原始分析用了 perplexity 导致 PermG 从 6/8 膨胀到 8/8。
- PermG 数据必须从 registry.yaml 直接读取验证，**不信任子 agent 摘要**。Report 24 曾因信任 Explore subagent 把 t20_a060 PermG=0/8 错报为 6/8（混淆了 PermG 和 DiffXCorr）。
- T=20 α=0.60 只有 s42 一个种子。Agent 曾在 D170 assessment 中谎称"both seeds"——t20_a060_s43 仍在训练中。任何称"dual-seed confirmed"的 T=20 α=0.60 claim 必须打回。
- α_c(T) 公式 R²=0.883（D168 joint model），不是 1.000。Agent 曾写 R²≈1.000。

### 2. 🖥️ 基础设施快照
- **westd-17855**（6 GPU RTX PRO 6000 Blackwell 98GB）：`/root/autodl-tmp/distrib_canary_collapse`
- **westd-19828**（2 GPU RTX PRO 6000 Blackwell 98GB）：`/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base）
- 活跃进程（截至 handoff）：
  - westd-17855 GPU0: t25_a050 (PID 519974, gen~13/25)
  - westd-17855 GPU1: **已释放**（t15_a060 刚完成）
  - westd-17855 GPU2: t15_a075 (PID 513372, gen~14/15, 即将完成)
  - westd-17855 GPU3: t25_a060★ (PID 515622, gen~13/25, 最关键 T=25 cell)
  - westd-17855 GPU4: t20_a060_s43 (PID 541975, gen~2/20, sync-dip 跨种子)
  - westd-17855 GPU5: t25_a045 (PID 519277, gen~12/25)
  - westd-19828 GPU0: t25_a075 (PID 671838, gen~14/25)
  - westd-19828 GPU1: t20_a045_s43 (PID 688685, gen~3/20, 边界跨种子)

### 3. 📊 当前状态
**刚完成**：t15_a060 分析审查（Report 38）——PermG=0/8，sync-dip 在 T=15 持续，三 T 确认（10/15/20）。本 session 共发送 Reports 35-38（累计 38 报）。

**Phase Diagram 15/20 verified**：

| α\T | 5 | 10 | 15 | 20 | 25 |
|-----|---|----|----|----|----|
| 0.45 | 0/8 | 0/8 | 6/8 | 5/8 | RUN |
| 0.50 | 0/8 | 6/8 | 6/8 | 6/8 | RUN |
| 0.60 | 0/8 | 0/8 | 0/8✅ | 0/8 | RUN★ |
| 0.75 | 0/8 | 6/8 | RUN | 6/8 | RUN |

**D102 审计**：93/93 合规（90 PASS + 3 LEGACY，0 FAIL）。gpt2m_s43 重分析已验证（Report 36）。

**等待中**：t15_a075 训练完成通知 + 分析 worker 回调。

### 4. 📋 待办（条件触发式）
- **t15_a075 完成 → 审查 PermG**：预期 ~6/8（与 T=10/20 α=0.75 一致）。完成后 T=15 行 4/4 填满，Phase Diagram 16/20。
- **t25_a060 完成 → 最关键审查**：如果 PermG=0/8，sync-dip 升级为"全 T 不变量"（T=10/15/20/25 四值）。如果 >0/8，sync-dip 有 T 上界——叙事需调整。
- **t20_a060_s43 完成 → 跨种子验证**：如果 0/8，T=20 sync-dip dual-seed 确认。如果 >0/8，seed variance 需讨论。
- **t20_a045_s43 完成 → 边界稳定性**：s42=5/8，s43 结果决定 5/8 是稳健还是噪声（4-6/8 range）。
- **T=25 四格全完成 → α_c formula 最终验证**：公式预测 α_c(25)≈0.21，所有 α≥0.45 应检出。如果 T=25 结果与预测偏差大，公式系数需 refit。

### 5. 🎯 战略上下文
- **核心叙事三支柱**：(1) T=5 blind zone（全 0/8，α_c(5)≥1.0），(2) α_c(T) power-law boundary（R²=0.883，4 T 值验证），(3) α=0.60 sync-dip（T=10/15/20 三值 PermG=0/8，S×R 模型解释）。
- **6/8 ceiling**：检出区所有 cell 收敛到 PermG=6/8（仅 t20_a045=5/8 例外）。2/8 缺口始终是 canary→mauve 对——MAUVE bottleneck 是结构性的。
- **最易判断错的事**：(1) 不要把 DiffXCorr 和 PermG 混淆——sync-dip cell DiffXCorr=6/8 但 PermG=0/8；(2) 不要假设 T 越长检出越多——α=0.60 打破单调性；(3) 旧分析文件（analysis_mauve/ 目录、perplexity-based 结果）可能残留在服务器上，以 analysis/ 目录下的 D102 版本为准。
- **DDL**：EMNLP 2026 ARR June，~2026-06-15。Phase Diagram 20/20 预计 ~24h 内完成（T=25 ~5h，t15_a075 <1h）。时间充裕。


---
