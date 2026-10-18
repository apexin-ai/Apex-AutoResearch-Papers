# agent / loop_14.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`94a2e460db23f1155978.json`](../../sessions/94/94a2e460db23f1155978.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T18:24:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- AutoDL 代理下 `load_dataset("allenai/c4")` 会静默挂死，必须用 FineWeb 或预下载
- EDD 报告必须附 bootstrap CI + p-value（D027）
- Cohen's d 用 d_z（差值 SD 做分母），不用 pooled SD
- 模型下载与训练不得并发操作同一目录
- submit_training_job 命令必须自带环境激活（如 `source /root/miniconda3/bin/activate && python train.py`），不要假设 .venv

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 /root/autodl-tmp/recursive_gen_depth_est
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/autodl-tmp/recursive_gen_depth_est/data/（含 GPT-2 XL / OLMo-1B / Pythia-1.4B 各深度生成数据）
- HF cache：/root/autodl-tmp/.hf_cache
- W&B project：recursive_gen_depth_est（entity 从 project config 加载）
- 活跃进程：cross_scale_llama3_base_001 (PID 561301, cuda:0, RUNNING)
- Cron 监控：cross_scale_llama3_base_001 活跃（reconcile 确认 still running）

### 3. 📊 当前状态
- **刚触发**: cross_model_reverse_chain_001 (cuda:1) 进程正常退出，状态 ANALYZING
- **已派 Worker**: `worker_analysis_cross_model_reverse_chain_001_20260516T142302` 正在分析该实验（读日志 + W&B metrics + 判断 conclusion + 更新 registry）
- **仍在跑**: cross_scale_llama3_base_001 (cuda:0, PID 561301) — Llama-3.1-8B base cross-scale probe
- **等待回调**: 上述分析 Worker 完成后需要处理结果（on-worker-done + on-experiment-done 后续流程）
- **cuda:1 空闲**: reverse_chain 跑完后 cuda:1 已释放，分析 Worker 完成后应安排下一个实验

### 4. 📋 待办（条件触发式）
- Worker `analysis_cross_model_reverse_chain_001` 回调到达 → 读 conclusion：
  - success → 更新 report.md，向 Director 汇报（reverse chain 验证 N4 cross-model claim），安排 cuda:1 下一个实验
  - negative → 按 red-section 产 Framing 调整提案，向 Director 汇报，不动 paper
  - failed → 按 on-experiment-failed skill 诊断
- cross_scale_llama3_base_001 cron 回调 → 同样走 on-experiment-done 流程
- cuda:1 空闲 → 查 experiment_plan.yaml 下一个待跑实验（可能是 wild_data_calibration_005 FineWeb 替代 C4，ROADMAP 提到准备中）

### 5. 🎯 战略上下文
- **项目阶段**: Phase 2 写作 + ARR 审稿，DDL = EMNLP ARR May 25（剩 9 天）
- **核心贡献**: Depth Degradation Atlas + EDD metric + feature universality
- **3×3 矩阵已 9/9 完成**，当前实验是补充性的（cross-scale + cross-model reverse chain）用于加强 generalization claim
- **D030 决策**: R4 审稿回应策略是全面降级 overclaiming + 补 Llama-3.1-8B base 数据
- **cross_model_reverse_chain_001 的意义**: 验证 reverse chain (GPT2XL→OLMo→Pythia) 下 depth signal 仍可迁移，直接支撑 N4 cross-model generalization claim。已有正向证据: cross_model_loo 均值 66.4%
- **易错点**: 
  - EDD 声明已降级（D026/D027）——Pythia 显著、OLMo 边际、GPT-2 XL 不显著，不能说"三模型均显著"
  - cross-strategy claim 已被 D021 推翻降级为 RF-only，不要再用 LR z-score 做 cross-strategy 论证
  - DCOL 路线已彻底放弃（5 个版本全失败），不要再尝试


---
