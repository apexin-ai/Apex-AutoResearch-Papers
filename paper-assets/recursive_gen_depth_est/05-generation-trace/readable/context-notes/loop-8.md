# director / loop_8.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`8090f30f124635850062.json`](../../sessions/80/8090f30f124635850062.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T17:05:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本地 GPU 只能用 gpu-6000pro-2 的 cuda:0/cuda:1；云 GPU 只能用 westd-48862 的 cuda:0/cuda:1
- plan_023 理论分析质量门控 (C003): EDD 上界必须 mathematically rigorous，否则只写 Discussion 一段。写入论文前必须 post_to_reviewer 审查
- 云服务器 westd-48862 按时计费，绝不允许空闲
- 14B 下载不要再用 aria2c（两次 TLS failure），必须用 `huggingface-cli download`
- prompted_gen_gpt2xl_001 registry 已从 failed 修正为 success（server restart desync 导致的误标）

### 2. 🖥️ 基础设施快照
- **本地服务器**: gpu-6000pro-2, 工作目录 /root/autodl-tmp/recursive_gen_depth_est
- **云服务器**: westd-48862, SSH `ssh -p 48862 root@connect.westd.seetacloud.com`, 密码存 `westd_48862_ssh_password`, 工作目录 /root/autodl-tmp
- Python: 两台均 Python 3.10, PyTorch 2.11.0+cu128, CUDA 12.8
- 模型: gpu-6000pro-2 `/root/autodl-tmp/models/` (Pythia-1.4B, OLMo-1B, GPT-2 XL, Qwen2.5-14B 下载中 shards 5-8)
- HF 下载: `HF_ENDPOINT=https://hf-mirror.com`
- 活跃进程 (gpu-6000pro-2): wild_data_features cuda:0, plan_021 instruct cuda:1, 14B hf download 后台
- 活跃进程 (westd-48862): plan_024 downstream cuda:0, plan_025 learned estimator cuda:1

### 3. 📊 当前状态
D038 Strong Accept 冲刺全面展开。4 张 GPU 全部在跑：

| 服务器 | GPU | 实验 | 预计完成 |
|--------|-----|------|---------|
| gpu-6000pro-2 | cuda:0 | wild_data_features_001 (plan_015) | ~1h |
| gpu-6000pro-2 | cuda:1 | qwen25-1p5b-instruct-001 (plan_021) | ~3-4h |
| westd-48862 | cuda:0 | downstream_benchmark_001 (plan_024) | ~2-3h |
| westd-48862 | cuda:1 | learned_estimator_001 (plan_025) | ~30min |

已完成本轮：plan_018 baselines ✅ (RF 78.2% >> all detectors), plan_020 bootstrap CIs ✅, plan_023 theory draft ✅ (已按 Reviewer 要求降级形式化), plan_016 prompted gen ✅ (69.5%), plan_025 CPU 版结果 (XGBoost 67.2% vs RF 66.4%), Table 1 CI 更新 ✅。

Agent 队列: 已清空，等待实验回调。OpenAI key 已申请（plan_026 GPT-4o-mini），等用户提交。

### 4. 📋 待办（条件触发式）
- wild_data_features_001 完成 → 分析 C4/FineWeb depth 分布，cuda:0 转 14B pipeline（如下载完成）或其他待排实验
- plan_021 instruct 完成 → 分析 instruct model depth signal，cuda:1 转 14B pipeline
- plan_024 downstream 完成 → 分析 HellaSwag/ARC/PIQA 结果，判断 depth-filtered 是否优于 unfiltered
- plan_025 GPU 版完成 → 汇总 learned estimator 全部配置结果
- 14B 下载完成 → 立即在释放的 GPU 上提交 14B pipeline (plan_014)
- OpenAI key 到位 → 派 Agent 启动 plan_026 GPT-4o-mini 递归链
- 所有 D038 实验完成 → 派 Paper Agent 整合新结果写入论文 + 提交 R10 审稿

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 Main Conference, ARR May 25 截稿 (8天)
- **核心决策链**: D037 Manager 自查补缺 → D038 用户批准全 5 项优化并行冲刺 Strong Accept
- **论文定位**: Task formalization + systematic empirical study（不是 method paper）
- **最强结果**: plan_018 证明现有检测器做 ordinal depth 远不如我们 (Combined 74.2% vs RF 78.2%)
- **plan_025 已确认特征瓶颈**: XGBoost/MLP/Prototypical 均 ≤+0.8pp vs RF，分类器不是瓶颈，特征设计是贡献
- **易错点**: 
  - Theory section 不要 overclaim（Theorem → Hypothesis），已有 C003 约束
  - Fast-DetectGPT 在 pythia_nucleus d1 有数值溢出 (mean=28515.7)，论文中必须标注或排除
  - 用户明确说 GPT-3.5-turbo 太烂，plan_026 已改为 GPT-4o-mini
  - prompted_gen 69.5% vs BOS 83.3%: 是 "signal attenuated but present"，不是 failure
  - γ 拟合用 0.75 而非 0.80（Reviewer 指出 0.80 系统性偏高）


---
