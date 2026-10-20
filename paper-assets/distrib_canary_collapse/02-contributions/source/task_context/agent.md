---
loop: 18
reason: idle_timeout
updated: '2026-05-24T00:34:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-17855 (cuda:0-5) + westd-19828 (cuda:0-1)，共 8 张，不可用白名单外 GPU
- D102 分析必须用 `run_5method_analysis_d102.py`（mauve+true_3sigma），禁用旧脚本（M063）
- 训练命令必须包含 `HF_HOME=/root/autodl-tmp/.hf_cache` + `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1`，缺一不可（M060，Director 警告 no third time）
- ≤3B 模型必须 fp32（D079）
- 410M 用 non-deduped，1.4B 用 deduped——各 scale 内部一致，跨 scale 用 "consistent across" 不用 "scale-invariant"（D202）
- Cron 系统对本项目有反复误判历史（sentinel 路径不在 cron 检测范围），收到 failed 回调时必须先 tail 日志确认

### 2. 🖥️ 基础设施快照
- **westd-17855** (6× RTX PRO 6000 Blackwell 98GB)
  - 工作目录: `/root/autodl-tmp/distrib_canary_collapse/`
  - Python: `/root/miniconda3/bin/python`, 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 1.4B 模型: `/root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped`
  - HF_HOME: `/root/autodl-tmp/.hf_cache`
  - 磁盘: 816GB free (3%)
- **westd-19828** (2× RTX PRO 6000 Blackwell 98GB)
  - 同样路径结构，但 1.4B 模型在 `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`
  - 磁盘: 817GB free (2%)
- **活跃进程** (reconcile 确认):
  - t10_a045_s43: 17855:cuda:4, PID 738796
  - t15_a050_s43: 17855:cuda:1, PID 750075
  - t15_a060_s43: 17855:cuda:0, PID 749427
  - t15_a045_s43: 17855:cuda:5, PID 762806
  - t15_a075_s43: PID 857058 (服务器未确认，reconcile 显示 running 但 get_project_resource_usage 未列出)

### 3. 📊 当前状态
**刚做完**：处理 cron 失败回调。scale_14b_t10_a075_s43_fp32 和 scale_14b_t10_a050_s43_fp32 被 cron 误判为 failed，实际都完成了 10/10 gens。已修正 registry → success，已派 D102 Worker（worker_d102_scale_14b_t10_a075_s43_fp32_20260523T082232 + worker_d102_scale_14b_t10_a050_s43_fp32_20260523T082237）。

**Worker 池** (5 active, 0 GPU / 5 CPU):
- worker_ops_d102-t10-a075-s43 (先前派发的 D102)
- worker_ops_d102-t10-a050-s43 (先前派发的 D102)
- worker_ops_deploy-t10-a050-s44-cuda2-17855 (正在部署 s44 实验到 17855:cuda:2)
- worker_d102_...a075_s43...T082232 (我刚派的 D102)
- worker_d102_...a050_s43...T082237 (我刚派的 D102)

**注意**：可能有重复 D102 Worker（先前的 ops 版本 + 我新派的）。如果先前 Worker 已完成分析，我的 Worker 会重复跑一遍但不会造成数据问题。

**等待中**：
- D102 Worker 回调 → 提取 PermG 值 → 更新 registry metrics → 汇报 Director
- Director 回复：3 张空闲 GPU 应提交什么实验
- 4 个 RUNNING 实验的 cron 完成回调

### 4. 📋 待办
- D102 Worker 回调到达 → 读取 PermG 结果 → update_registry(metrics) → 对比 s42 parent 值（a075 s42=5/8, a050 s42=4/8）→ 汇报 Director C3 cross-seed 一致性
- t10_a045_s43 完成 → 最后一个 T=10 s43 → D102 分析 → T=10 s43 全行完成 → 可以出 C3 T=10 cross-seed 结论
- T=15 s43 batch (4 experiments) 完成 → D102 分析 → C3 T=15 cross-seed 结论
- Director 指示空闲 GPU 任务 → 提交（17855:cuda:3, 19828:cuda:0, 19828:cuda:1 空闲；cuda:2 已有部署 Worker）
- 所有 C3 完成 → 更新 ROADMAP 标记 C3 完成 → 论文 Table 17 更新

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 ARR June (DDL ~2026-06-15, 距今 22 天)，目标 3.5 Borderline Conference
- **核心 story**: α×T 2D 相图 + binary detection pattern + metric structure + 检测下界理论
- **当前阶段**: 1.4B Scale verification（C1-C4 s42 行全 PASS，正在跑 C3 cross-seed s43）
- **关键 pattern** (D206): onset attenuation -3/8 (α-invariant), sync-dip +6/8, strong gap 0
- **易错点**:
  1. Cron 系统对 `results/scale/` 路径下的 sentinel 检测不稳定，反复误判 — 收到 failed 回调先查日志再定论
  2. 不要混淆 ops: 前缀 Worker 和 d102: 前缀 Worker — 可能已有先前 session 派发的同类 Worker，检查 worker pool 避免重复
  3. t15_a075_s43 状态不明 — reconcile 显示 running 但 resource usage 未列出，可能在 19828 上，需要 SSH 确认
  4. 19828 上的 1.4B 模型路径与 17855 不同（`.hf_cache` vs `.ms_cache`），部署实验时要根据服务器选对路径
