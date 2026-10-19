---
loop: 6
reason: max_wall_time
updated: '2026-05-17T20:53:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13953 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- eval_info.json 中的数据可能是 per-task 而非 suite 级——之前因此报告了错误的 76% SR（D045）。只信 suite 级 pc_success 汇总或自行从 successes 数组计算全 suite 平均
- connector_lora 模式的 eval/probe 脚本已修复（从 checkpoint config 读取 freeze_mode/lora_rank/lora_scale），修复前 LoRA 权重会被 strict=False 静默丢弃，eval 结果完全无效
- v7.3 训练脚本必须带 `--lambda_drift 0.0`（Reviewer 要求，LoRA 天然限制 drift，drift reg 冗余）
- `submit_training_job` 命令必须自带环境激活（如 `source /root/miniconda3/bin/activate && ...`），不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953，SSH: `ssh root@connect.westb.seetacloud.com -p <port>`
- 工作目录：`/root/acib`（远程代码），本地 artifacts: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/`
- Python：服务器上 `/root/miniconda3/bin/python`
- 模型 checkpoint：
  - Baseline: HF cache `lerobot/smolvla_libero`（注意 `/root/autodl-tmp/models/smolvla_libero/model.safetensors` 与 HF cache 版本不同，max_diff=6.3e-3）
  - v7.2 seed1: `/root/autodl-tmp/acib_v7.2_connector_scorer/checkpoint-20000`
  - v7.2 seed2: `/root/autodl-tmp/acib_v7.2_connector_scorer_seed2/checkpoint-20000`
- 数据集：`/root/autodl-tmp/libero_dataset`（273K samples）
- 活跃进程（截至 handoff）：
  - PID 40598 (cuda:0): v7.2 α=0.0 eval，libero_10 约 50% 完成
  - PID 44022 (cuda:1): v7.2 α=1.0 eval，libero_10 约 50% 完成
  - Cron 已注册：acib_v72_eval_alpha00, acib_v72_eval_alpha10（interval=120s）

### 3. 📊 当前状态
v7.2 eval 在跑最后一个 suite (libero_10)，预计 ~1-1.5h 完成。3/4 suites 已有结果：

| Suite | α=0.0 | α=1.0 | Baseline |
|-------|-------|-------|----------|
| spatial | 59.4% | 61.0% | 66.0% |
| object | 65.6% | 66.2% | 67.8% |
| goal | 78.6% | 78.0% | 76.4% |
| libero_10 | 进行中 | 进行中 | 54.2% |
| avg(3) | 67.9% | 68.4% | 70.1% |

Registry RUNNING: acib_v72_eval_alpha00, acib_v72_eval_alpha10。
Registry DONE(success): acib_v72_connector_scorer_seed1/seed2（训练完成，Probe A PASS）。
所有代码就绪待 GPU：v7.3 LoRA, connector-only ablation, drift sweep, contrastive_grad_scale。
Paper framing 初稿已写入 paper_framing.md。
Literature map 已有 16 篇论文。

### 4. 📋 待办（条件触发式）
- **Cron 回调 eval_alpha00/alpha10 完成** → 收集 libero_10 suite 级 pc_success → 更新 registry 标 DONE → 立即启动 cuda:0 `run_v73_connector_lora.sh` + cuda:1 `run_connector_only.sh` → 用 `submit_training_job` 注册 cron 监控 → 汇报 Director 完整 4-suite 结果
- **v7.3 LoRA 训练完成 (~3h)** → Probe A (`run_v73_eval_probe_a.sh`) → α=0.0 spatial sanity (`run_v73_eval_alpha00_spatial.sh`) → α=1.0 full eval (`run_v73_eval_alpha10.sh`)
- **Connector-only 训练完成 (~3h)** → eval α=0.0 4 suites (`run_connector_only_eval.sh`)，不需要 α=1.0（无 scorer）
- **v7.3 eval α=0.0 spatial** → 必须精确 = baseline 66.0%（LoRA scale=0 保证），如果不是则代码有 bug
- **v7.3 Probe A cos < 0.8** → PASS，继续 eval pipeline；cos > 0.8 → LoRA rank 太低或训练不足
- **4-suite avg ≥ baseline - 2pp (64.1%)** → MVP PASS → 启动论文写作 + 补充实验（perturbation, token dropping, seed2）
- **Director 审阅 paper_framing.md** → 等待方向性调整意见

### 5. 🎯 战略上下文
**核心结论链**：
- D038: joint training 梯度污染损坏 base policy（α=0.0 仍回退 -7.8pp）
- D041: scorer-only (v7.1, 123K params) 容量不足，仅 global bias
- D042/D043: v7.2 connector+scorer Probe A PASS（cos 0.593, true spatial conditioning）
- D045: v7.2 α=0.0 回退 -2~7pp 不是 bug——connector drift (0.4%) 是根因，action expert 对 connector 输出极度敏感
- **v7.3 LoRA 是结构性解决方案**：α=0.0 时 scale=0 精确恢复 baseline，消除 Goldilocks 问题

**易踩的坑**：
1. eval_info.json 格式不统一——有的有 pc_success 字段，有的只有 successes 数组，需要兼容处理
2. 不要用 `/root/autodl-tmp/models/smolvla_libero/model.safetensors` 做 baseline 权重对比——它与 HF cache 版本不同（差异 296.6）
3. GPU utilization 经常报 0%/1% 是正常的——LIBERO rollout 是 CPU 密集的，GPU 仅推理时短暂使用。不要因此误判 GPU 空闲
4. drift_loss 没有被 print 到训练日志中（logging 遗漏），但它确实在参与梯度更新（已验证）
5. connector-only 模式的 Probe A 无意义（scorer 不被调用，hook 短路返回），不要对 connector-only checkpoint 跑 probe
