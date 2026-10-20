# reviewer / loop_25.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_25.md`
- **Structured JSON:** [`84789554f07af4746006.json`](../../sessions/84/84789554f07af4746006.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: idle_timeout
updated: '2026-05-24T19:49:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977，项目 gpu_ids 需从 constraints.yaml 确认（之前有越界事故）
- 论文 DDL: EMNLP 2026 via ARR，2026-05-25（明天）
- experimental_setup.tex 中 "three cross-family models" 应为 "four"（含 Falcon3），已标 warning 但截至本轮仍未修复
- Phi-4 per-seed 数据在 westd server，cqa1 无法直接验证——Figure 3 和 Figure 4 对 Phi-4 s123 数值不一致（见§4待办）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，远程代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文源码：`docs/paper/`（main.tex 入口），图表脚本：`docs/paper/figures/` + `figures/paper/`
- 审计数据：`artifacts/data_audit_part3_crossseed_volume.md`（Phi-4/Gemma-2/OLMo-2 per-seed 数据标注 "westd only"）
- 活跃进程：无（registry 无 RUNNING 实验）
- 备份：3 个 tar.gz，共 7.8G；`/root/democalib/` 3.1G 非 git 数据仍在服务器上

### 3. 📊 当前状态
刚完成 Figure 3 (baseline_vulnerability) 重设计后的数据一致性审查。发现 3 处 cross-seed 数据错误（Phi-4/Falcon3/Qwen-7B）→ 已被 Agent 修复 → 我已复核确认修复正确。同时发现 Phi-4 跨图一致性问题（Fig3 vs Fig4 mean 不匹配）→ 已 post warning 给 Director。

registry: 433 总实验，无 RUNNING/PREPARING。项目处于论文提交最终阶段。

此前完成的审查：
- 全文 claim-data 一致性（PASS）
- ARC heatmap + domain gamma 修复复核（PASS）
- 匿名化 + 格式合规 + 补充材料 checklist（PASS，附 minor issues）

### 4. 📋 待办（条件触发式）
- Director 确认 Phi-4 s123 精确值 → 验证 Figure 3 range 上界（+1.83）和 Figure 4 mean（+0.50）哪个需修正。如 s123=+1.15 → Fig3 改 (-0.17, +1.15)；如 s123=+1.83 → Fig4 改 mean=+0.73
- Agent 修复 "three cross-family models" → "four" → 确认 experimental_setup.tex 更新
- 提交完成后 → 进入等待审稿状态，切换到 rebuttal 准备模式
- 收到 ARR reviewer comments → 加载 `rebuttal.skill.md`，逐条审查 reviewer 意见并辅助 response letter

### 5. 🎯 战略上下文
- 论文核心贡献：(1) dose-response taxonomy（Immune/Benefit/Collapse/V-recovery），(2) DiD 排除 item-level memorization，(3) ContamCal IRT 框架的 domain-level γ_d 分析
- Social Sciences γ_d < 0（99.7% posterior probability）是最强 domain-level finding；pooled γ 不显著是 dilution masking 的证据
- 最容易判断错的事：
  - Table 1 的 Phi-4 Δacc "±0.5pp" 是定性描述（≈0），不是精确数值——s42 实际是 -0.17pp
  - cross_seed_ranges（Figure 3）是 raw min/max of per-seed values，cross_seed CI（Figure 4）是 BCa bootstrap CI on the mean——两者概念不同，不能直接比较 bound
  - "86% (6/7)" ARC direction agreement 包含 LLaMA-3.1（7 families），不含 Falcon3 ARC（因为 Falcon3 ARC 在 main table 里不是 cross-benchmark 分析的一部分）——这个已验证正确但容易误查
  - Appendix F 的 internal label 仍为 `tab:s1_pipeline` / `tab:s1_domain`（未改），但对读者不可见（section ref 已改为 `sec:s2_only_pipeline`）——不需要修


---
