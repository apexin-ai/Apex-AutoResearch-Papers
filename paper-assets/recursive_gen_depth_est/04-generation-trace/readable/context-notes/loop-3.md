# director / loop_3.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`a28a6773d3fd24f94228.json`](../../sessions/a2/a28a6773d3fd24f94228.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T22:42:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1，不能越界
- DCOL baselines（CE/CORAL）必须用 DeBERTa-v3-large（D003 决策），不能用 base，否则模型规模混淆变量
- dcol_deberta_001 已因 embedding collapse 失败（D005），之前出现过僵尸进程未清理导致 v2 OOM 的事故——kill 实验时必须验证进程确实死亡（`ps -p PID` + `nvidia-smi`），不能只改 registry
- margin_lr 不能设太高（v1 用 1e-3 导致 collapse），v2 修正为 1e-4

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2 (connect.westb.seetacloud.com)
- 工作目录：/root/autodl-tmp/recursive_gen_depth_est
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/models/deberta-v3-large（DCOL + baselines 共用）
- 数据：各 pipeline 生成在 /root/autodl-tmp/recursive_gen_depth_est/data/ 下按 model-strategy 组织
- HF_HOME=/root/autodl-tmp/.hf_cache
- 需 `source /etc/network_turbo` 才能外网访问

### 3. 📊 当前状态
- **dcol_deberta_002**: 上一轮因 v1 僵尸进程 OOM 失败，发了紧急清理+重提交指令，但 Agent 随后被 reset，不确定是否成功执行。**第一件事检查 cuda:0 进程状态和 dcol_v2/v3 是否在跑。**
- **olmo_temp09_001**: 上一轮 RUNNING on cuda:1，应该已完成或接近完成
- **gpt2xl_temp09_001**: ANALYZING 阶段（feature extraction 完成，分类结果待收集）
- 3×3 矩阵 5/9 完成 + 至少 1-2 个在跑/分析中
- Baseline 代码全部就绪（CE, CORAL, DivEye, PPL regression, zero-shot LLM），均已适配 DeBERTa-v3-large

### 4. 📋 待办
- cuda:0 僵尸进程未确认清理 → 先 SSH 检查 cuda:0 进程，清理后重提交 DCOL v2（margin_lr=1e-4, L2 norm, cl_weight=1.0, seed=42）
- olmo_temp09_001 完成 → 收集 metrics，更新 registry；cuda:1 空出 → 提交 OLMo topk50 或 GPT-2 XL topk50
- gpt2xl_temp09_001 分类结果到手 → 更新 registry，与 baseline 对比
- 3×3 矩阵剩余 cells（OLMo topk50, GPT-2 XL topk50）按 GPU 可用性排入
- 全部 3×3 + topk50 跨模型结果到手 → 确认 "decoding strategy modulates signal strength" 是否通用，更新 paper_framing.md

### 5. 🎯 战略上下文
- **核心发现**：递归生成深度可通过统计特征检测，feature importance 跨模型跨策略完全一致（var_surprisal, p90_ppl 为 top features）
- **Framing 关键 nuance**：不能 claim "strategy-agnostic"——连续策略（nucleus/temp）信号强且稳定（~2pp 波动），硬截断（top-k）信号存在但显著衰减（-8.6pp）。Feature stability 是 robustness 的主要论据，不是精度稳定性
- **DCOL 是高风险实验**：v1 embedding collapse 已失败，v2 OOM 已失败，第三次必须确认进程清理干净再提交
- **决策链**：D001（项目启动）→ D003（baselines 统一用 large）→ D005（DCOL v1 collapse，修超参重跑）
- **易错点**：kill 实验时一定要 kill 实际 PID 而非 registry PID（可能是父进程，子进程仍活着）；AutoDL 磁盘根分区小，大文件放 /root/autodl-tmp/


---
