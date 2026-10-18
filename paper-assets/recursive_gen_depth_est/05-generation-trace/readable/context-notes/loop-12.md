# agent / loop_12.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`fc4543da3b7dcd5cc089.json`](../../sessions/fc/fc4543da3b7dcd5cc089.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T04:52:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **gpu-6000pro-2 cuda:0, cuda:1**（config.execution.servers 白名单）
- cross_scale_qwen7b_001 当前占 cuda:0，cuda:1 空闲——**cuda:1 必须利用起来**
- AutoDL 代理下 `load_dataset("allenai/c4")` 会静默挂死，已踩坑两次（wild_data_calibration_002），必须用 FineWeb/hf-mirror.com 替代
- AutoDL 网络：pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1` + SSL 证书变量；大模型优先 ModelScope
- EDD 报告必须附 bootstrap CI + p-value（D027），Cohen's d 用 d_z（配对设计差值 SD 做分母）
- 论文 4-class (d0-d3) 是已确认设定；6-class (d0-d5) 取决于 plan_014 结果
- submit_training_job 命令必须自带环境激活（如 `source /root/miniconda3/bin/activate && python train.py`），GPU 编号始终从 0 开始

### 2. 🖥️ 基础设施快照
- **服务器**: gpu-6000pro-2（AutoDL），工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: `/root/autodl-tmp/.hf_cache`（HF_HOME）
- **数据**: `data/` 子目录（per-experiment），wild data 在 `data/wild_data/`
- **W&B**: 项目级配置（查 config 确认 entity/project）
- **活跃进程**: cross_scale_qwen7b_001（tmux session=cross_scale_qwen7b, cuda:0, PID 见 cron 记录）
- **活跃 Cron**: 1 个，监控 cross_scale_qwen7b_001（reconcile 确认 still running）
- **Worker 池**: 0（空！需要立即补充）

### 3. 📊 当前状态
**刚完成**: 本 session 是 handoff session，上一轮完成了：
- wild_data_calibration_004 (success): Web-crawl FPR ~20% 跨数据集一致（C4=20.2%, FineWeb=19.5%），WikiText FPR=0%
- multi_tau_ablation_001 (success): τ∈[0.5,0.9] depth signal 鲁棒，τ=1.1 崩溃（memorization-as-prerequisite 机制）
- zeroshot_qwen7b_500_001 (success): Qwen-7B zero-shot 30.4% << RF 78.2%，两 LLM failure mode 不同但都无法捕获深层递归信号
- R3 审稿修改 8/9 text issues resolved

**RUNNING**: cross_scale_qwen7b_001（plan_014，Qwen2.5-7B 4-bit QLoRA cross-scale probe，d0-d5 500 samples/depth，cuda:0）

**等待中**:
- cross_scale_qwen7b_001 cron 回调（完成后需分析 7B scale 的 depth signal + EDD）
- R3-N5 cross-strategy curation 未完成
- Rebuttal open items: W4 zero-shot 样本量, R2-W3 multi-τ

**Registry 总览**: 67 DONE (41 success / 4 negative / 7 failed / 15 killed) + 1 RUNNING = 68 total

### 4. 📋 待办（条件触发式）
- cross_scale_qwen7b_001 cron 回调（DONE/success）→ spawn worker 分析 7B 结果（4-class acc, 6-class acc, EDD, pairwise AUC）→ 与 1-1.5B 对比 → 更新 registry + report.md → 汇报 Director（若 4-class acc ≥60% 且 EDD 一致 → 支持 cross-scale claim；否则 → scope 限定为 1-1.5B）
- cross_scale_qwen7b_001 失败 → 读 log 诊断 → 可能需要调 batch size / gradient accumulation（7B 模型 OOM 风险）
- cuda:1 空闲 → 立即找可并行任务：R3-N5 cross-strategy curation 实验 / wild_data_calibration_002 重试（用 FineWeb 替代 C4）/ rebuttal 补充实验
- 所有 R3 issues resolved → spawn worker 做 final polish + bibliography audit → 准备 ARR 提交
- DDL May 25 到达前 3 天 → 触发 s3-backup + 最终检查流程

### 5. 🎯 战略上下文
**核心结论链**:
- D011: Plan A 激活——Atlas/EDD 为 primary contribution，DCOL 放弃（v1-v6 全败）
- D024-D027: EDD 叙事从硬阈值→连续 AUC 衰减曲线；三模型 EDD=4 但统计强度分层（Pythia 显著/OLMo 边际/GPT-2 XL 不显著）
- D028: Cross-strategy normalization 被推翻，降级为 RF-only finding
- D029: 域偏差从"无偏差"改为"depth dominates, residual exists"

**DDL 压力**: EMNLP ARR May 25，**剩 9 天**。Phase 2 写作 + R3 审稿同时推进。3×3 矩阵 9/9 完成是底气，cross_scale_qwen7b_001 是加分项（扩展 scale coverage）但非阻塞。

**易错点**:
1. 不要把 cross-strategy LOO (59.1%) 和 cross-τ LOO (46.7%) 混淆——前者跨策略，后者跨温度，不可直接比较
2. GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 不可直接对比（来自前项目教训，但本项目不涉及）
3. wild_data_calibration 的 FPR ~20% 是 web-crawl 固有现象（模板/SEO），不是模型问题——论文中要 frame 为 limitation 而非 failure
4. DCOL 已死（6 版本全败），不要再尝试——论文中作为 negative analysis 处理
5. τ=1.1 崩溃的根因是 memorization 消失而非特征漂移——论文叙事要用 "memorization-as-prerequisite" 而非 "feature drift"
6. **cuda:1 空闲是当前最大资源浪费**——下一个 session 第一件事就是给它安排任务


---
