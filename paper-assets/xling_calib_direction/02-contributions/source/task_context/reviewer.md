---
loop: 1
reason: max_wall_time
updated: '2026-05-21T05:58:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-13176` 的 GPU 白名单未在 constraints.yaml 中定义（文件未创建），但 4× RTX 6000 PRO 96GB 全部属于本项目
- `run_plan_001.sh` 的 MODEL_PATH 已修正为 `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4`（之前 Llama4 也有 hyphen 路径 bug，已修）
- Procrustes 对齐要求 EN 和 target 来自**同一 split**（同一 MMLU items），`for_eval/` 中 EN 必须指向 eval split（plan_001 已修正，plan_002 本来就正确）
- Method.tex 中 "Qwen3-8B" 是**错误名**（实际 Qwen3-235B），语言列表含 th/my/am/zu/yo/si/km 与代码不符——这些 critical 尚未修正

### 2. 🖥️ 基础设施快照
- 服务器：`westd-13176(root)`，代码 `/root/xling_calib_direction`，Python `/root/miniconda3/bin/python3`，conda base
- 模型下载中：
  - Llama4: `/root/autodl-tmp/models/Llama4-Scout-W4A16/` — PID 53308, ~45GB/66GB, 5 .incomplete
  - Qwen3: `/root/autodl-tmp/models/Qwen3-235B-A22B-GPTQ-Int4/` — PID 53359, ~22GB/125GB, 16 .incomplete
- 激活（MVP）：`/root/xling_calib_direction/activations/`（Qwen2.5-7B 8层×6语言）
- 激活（MVP003）：`/root/xling_calib_direction/activations_mvp003/`（Llama3.1-8B）
- 结果 CSV：`results/probing_controls.csv`, `results/linproj_sensitivity.csv`, `results/linproj_procrustes_sensitivity.csv`, `results/cka_results.csv`
- CKA 矩阵：`results_cka_mvp001/`, `results_cka_mvp003/`
- P0 脚本：`run_plan_001.sh`（Qwen3）、`run_plan_002.sh`（Llama4）均已部署
- 磁盘：350GB total, ~155GB used, ~196GB free
- probing_controls_v2.py 可能仍在运行（PID 47972），上次检查 CPU 89.8%

### 3. 📊 当前状态
**刚完成**：
- B1+B2+M007 修复正式验证 → 全 PASS
- Procrustes sensitivity 审查 → PASS（280 行 CSV 完整）
- Partial correlation pilot 审查 → Simpson's Paradox 发现（Llama ρ=+0.41, p=0.006），Qwen 不显著
- Method.tex 审查 → 6 个 warning/critical（模型名、语言列表、ECE bins、量化方式、Procrustes 方程方向、few-shot 描述）
- Related Work 审查 → CaCLR 被写成既定事实（plan_003 未执行）、缺 Pires/Wu&Dredze 引用
- Novelty 提升方案评估 → CKA partial correlation 是最强杠杆（+0.5），control task finding 次之（+0.3）

**Registry**：
- `plan_013_probing_controls_v2`: PREPARING/failed — 有新实例可能在跑（PID 47972）
- `plan_013`: DONE/success — CV+PCA(100) 版本，selectivity 0.262@L27
- `mvp_001/002/003`: 全 DONE

**等待中**：两个模型下载完成 → plan_002（Llama4 先完成）/ plan_001（Qwen3 后完成）

### 4. 📋 待办
- Llama4 下载完成（~45→66GB）→ 验证 14 shards 完整 → 审查 plan_002 dry-run → 正式审批
- Qwen3 下载完成（~22→125GB）→ 验证 32 shards + GPTQ backend → 审查 plan_001 dry-run
- plan_002/001 激活提取完成 → 独立核实激活文件数量和 split 对齐（EN eval 和 target eval 是否同 MMLU items）
- plan_001/002 transfer_eval 完成 → 交叉验证 CSV 数字 vs registry metrics
- plan_011 CKA partial correlation（大模型版）→ 如果双模型显著 → novelty 锁定；如果仅单模型 → 需标注 architecture-dependent
- plan_003 CaCLR 结果出来 → 如果正面 → related_work.tex §3.4 需重写；如果负面 → 验证 β sweep 是否 fair trial
- Method.tex 下一版提交 → 重新审查模型名/语言列表/ECE bins 是否已修正

### 5. 🎯 战略上下文
- 项目目标 EACL 2027 ARR（Aug 3 deadline），74 天余量，GPU 预算充足
- 决策链：D001(7B MVP) → D004(MVP PASS) → D005(Dream 3/6) → D009(Re-dream 4/3/3, P0 批准) → 当前执行 P0
- **核心 novelty 瓶颈**：Dream 审稿 2.5/5，novelty 占 40% 扣分。CKA partial correlation (plan_011) 是 pivot point——pilot 显示 Llama 显著但 Qwen 不显著，大模型复现是关键
- **易错判断**：
  1. 不要因为 Qwen pilot partial correlation 不显著就否定 CKA 故事——n=40 underpowered，per-layer median ρ=0.80 方向一致
  2. Mean-shift 对 AUROC 恒等于 0（rank-invariance proof），不要再审 mean-shift AUROC 改善
  3. "28% low-resource capacity artifacts" 在 method.tex 和 related_work.tex 都出现但来源不清，审查时要追问具体计算基础
  4. CaCLR 结果在 related_work.tex 被预写为负面——如果 plan_003 正面，需要大改
  5. 两个 Procrustes sensitivity 进程的双写问题已解决（CSV 281 行完整），不用再追
