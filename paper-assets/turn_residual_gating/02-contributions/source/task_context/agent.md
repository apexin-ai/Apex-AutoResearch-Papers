---
loop: 0
reason: cron_callback_pending
updated: '2026-05-25T23:30:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单须从 `get_project_status` 的 `execution.gpu_ids` 获取
- 论文目标 EMNLP 2026 ARR（DDL 2026-08-03），正文严格 8 页限制（不含 references/limitations）
- Abstract ≤ 200 words（当前 192，改动时注意不超）
- appendix.tex float specifier 已统一为 `[t]`，主文 `[H]` 不动
- 论文 anonymous repo URL 固定为 `https://anonymous.4open.science/r/turn_residual_gating-8703/`

### 2. 🖥️ 基础设施快照
- 本地论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/`
- 编译命令：`cd paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
- 产出目录：`projects/turn_residual_gating/artifacts/`
- westd-20861:cuda:0 — GPU 空闲（实验已完成）

### 3. 📊 当前状态 — ⚠️ 需立即处理

**`phase2_switching_lasttok` 实验已完成，状态 ANALYZING，需分析推进到 DONE。**

背景：
- 原 `phase2_tf_ar_switching` 用 mid-turn GAR 测试 switching，结果 INCONCLUSIVE（TF-AR gap < 1 SE）
- 改用 last-token position (content_end - 1) 重跑，dry-run (n=2) 显示 Δ≈0.2（vs mid-turn Δ≈0.004）
- 完整跑：N=50, switch k=1..5, pure TF/AR, PID 13615, 已正常退出
- 结果路径：`/root/turn_residual_gating/results/switching_tg_s42_v7/`（last-token results 覆盖了旧文件，mid-turn 已备份为 `_midturn.json`）
- 日志路径：`~/runs/phase2_switching_lasttok.log`

**你需要做：**
1. SSH 到 westd-20861，读取 results/switching_tg_s42_v7/ 下的 JSON 结果
2. 分析 last-token GAR 在 TF vs AR 条件下的差异，以及 switching 后的 drop pattern
3. 更新 registry：metrics + conclusion + status=DONE
4. 如结果 positive，写入 artifacts/switching_lasttok_analysis.md 并汇报 Director
5. 更新 ROADMAP 中 Phase 2 相关任务项

### 4. 📋 其他待办（Director 已批准并行）
- P1 写作修复：MF1/MF2/MF3/SF（不占 GPU，可用 Worker）
- P0-B: λ_GAR rescaling（等 GPU 空闲后）
- P0-C: phase1b_llama_complement（Llama PCGrad + UG）
- 数据一致性修复（β=3 GAR, gap 统计口径, N=20→N=50）

### 5. 🎯 战略上下文
- 核心结论：auxiliary attention losses 在 teacher forcing 下收敛但在 AR generation 下 collapse（exposure bias），scheduled sampling 是有效 remedy
- 论文 framing 是"exposure bias characterization + causal exclusion"
- switching 实验目标：如 last-token GAR 在 switch point 突然 drop → 支持 C3（instantaneous distribution shift, not gradual drift）
- 前置结论：mid-turn GAR 无差异 → exposure bias 选择性破坏 summary position attention，不影响 turn 中部
- 跨模型：Qwen gap ~1.3×, Llama ~2.9×
- 当前 34 页（含 appendix），正文 ≤8 页已确认
