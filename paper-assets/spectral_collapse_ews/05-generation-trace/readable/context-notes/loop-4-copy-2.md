# agent / loop_4.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`1a6ca9ed62cc46df7ae5.json`](../../sessions/1a/1a6ca9ed62cc46df7ae5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-17T22:06:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1**（rtx6000-diagprobe），绝对不用其他设备号
- 服务器无外网：HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1，不要尝试 pip install 或 HF 下载
- submit_training_job 不支持 shell builtin：用绝对路径激活 conda（如 `source /root/miniconda3/bin/activate && python ...`）
- exp_005 已 killed (D018)，数据已备份，不要重启
- Controller 参数锁定：k=10, tau=0.002, per_gen mode（D015 确认）
- 论文 DDL: **May 25 EMNLP ARR Short Paper**，不接受 fallback 讨论

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (root@)，2× RTX PRO 6000 (98GB each)
- 工作目录：/root/spectral_collapse_ews
- Python 路径：需 `source /root/miniconda3/bin/activate`（具体 env 名由 Worker 确认过）
- 模型：Pythia-410M（本地缓存，离线模式）
- W&B：未配置（指标从 results/ 文件读取）
- 活跃进程：
  - exp_006 (adaptive k=10): PID 134913, cuda:0, Gen 3 生成中 (~70min/gen)
  - exp_004 (fixed_mix): PID 135411, cuda:1, Gen 2 生成中 (~100min/gen)
- Cron：2 个活跃（exp_004, exp_006），reconcile 确认均 still running
- 论文源码：/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/（Step 4 完成，14 citations clean）

### 3. 📊 当前状态
**刚做完**：
- Session-start 初始化（reconcile crons, read registry/roadmap/memory）
- 收到 WRITE HANDOFF 指令，正在写 handoff

**RUNNING 实验**：
- **exp_006** (adaptive k=10, cuda:0): Gen 3 生成中。论文主实验。Controller 至今未触发（delta 太小）。预计 Gen 5 是 MVP 关键判定点——若仍未触发则启动 contingency framing (D013: pivot to Claims 1-2 + Claim 4)
- **exp_004** (fixed_mix 50/50, cuda:1): Gen 2 生成中。Baseline 对照条件。比 exp_006 慢 (~100min/gen vs ~70min/gen)

**等待中**：
- exp_004/exp_006 cron 回调（预计 May 18 12:00-15:00 UTC 完成 10 gen）
- 第一个 GPU 释放后立即启动 linear_increasing (条件 c)
- Paper Step 5 Reviewer 审查待启动

### 4. 📋 待办（条件触发式）
- exp_006 Gen 5 cron 回调到达 → 检查 controller 是否触发。≥0.55 ratio = MVP 有望；仍=0.5 → 向 Director 汇报 contingency 触发条件满足，请求 framing pivot 决策
- exp_006 或 exp_004 完成 (10 gen) → spawn Worker 做 ppl paired comparison + spectral metrics 汇总 → MVP 判定（adaptive vs fixed_mix ≥3 ppl）
- 第一个 GPU 释放 → 立即 spawn Worker 启动 linear_increasing (条件 c，同总预算，r: 0.20→0.80)
- 四条件齐全 + MVP pass → complete_mvp() + 更新 experiment_plan.yaml + 启动 multi-seed (Phase 2)
- MVP fail (adaptive ≈ fixed_mix) → pivot framing: Claims 1-2 + Claim 4 (signal attenuation paradox as primary finding)
- Paper Step 5 Reviewer 完成 → 派 Worker 同步远程文件修正（消除 6.7× + T-t-1 残留，commit 2e5285f 后的遗留）

### 5. 🎯 战略上下文
**核心结论链**：
- D009: Phase 0 Go/No-go PASS → spectral collapse 确认可复现
- D013: 论文主线从 "adaptive controller" 后移到 "spectral EWS detection"，controller 降为 PoC
- D015: k=20→k=10（主参数），exp_005 killed
- D018: 撤销双实例，exp_005 killed 释放 cuda:1 给 exp_004

**最容易判断错的事**：
1. **Controller 大概率不会触发到 Gen 5**。50% real mixing 完全消除了 decompression peak，delta 近零。这不是 bug，是信号衰减悖论的实证。下一个"你"不要误以为 controller 没触发=实验失败——无论触发与否都是 publishable finding（D013 策略）
2. **exp_006 和 exp_004 进度差异**：exp_006 快 (~70min/gen) vs exp_004 慢 (~100min/gen)。exp_006 会先完成
3. **Phase 1 "decompression 延长" 不等于 collapse 未发生**：spectral 还在上升但 ppl/distinct_4 已退化。这是 HellaSwag-Spectral Asymmetry（论文可用发现）
4. **registry 里 exp_001/exp_005 状态显示 PREPARING 是 display artifact**——exp_001 实际 DONE(success)，exp_005 实际 killed。metrics 字段有完整数据。report.md 是准确的
5. **论文已完成 Step 4 全章节 + delta 公式修正**。下一步是 Step 5 Reviewer 审查，不要重复写章节


---
