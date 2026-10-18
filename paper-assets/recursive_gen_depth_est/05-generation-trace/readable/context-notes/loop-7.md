# director / loop_7.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`c55082a27c7bee1e1792.json`](../../sessions/c5/c55082a27c7bee1e1792.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T11:58:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 / cuda:1（2× RTX PRO 6000 96GB）
- 13B 实验（plan_014）必须用 FP16 无量化，之前 7B QLoRA 结果矛盾已被废弃
- plan_010（DCOL ablation）已取消，DCOL v1-v6 全部失败，不要再尝试
- plan_015（wild-data calibration）已推迟到 AAAI 窗口，当前不做
- 论文 8 页硬限，新实验结果只能进 Appendix + 主文 1-2 句引用，不可扩主文
- cross-strategy pipeline Claim 3 措辞必须是 "+11.5pp improvement"，不可写 "≥70% universal recovery"（2/3 模型个体 <70%）
- 引用必须经 WebSearch 验证真实性（之前 schaeffer2025 arXiv ID 错误差点导致 desk reject）

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 /root/recursive_gen_depth_est/
- 模型下载：HF_ENDPOINT=https://hf-mirror.com（HF 直连不稳定，用镜像 + aria2c 16 连接）
- 13B 模型：Qwen2.5-14B，下载到 /root/recursive_gen_depth_est/models/（aria2c 下载中，shard 1/8 开始）
- 3×3 数据：/root/recursive_gen_depth_est/data/ 下按 {model}_{strategy}/ 组织
- 论文 LaTeX：本地 workspace /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ 下 paper/ 目录
- GPU 健康数据暂无缓存（get_gpu_health 返回 "no data yet"），需 Agent SSH 后刷新
- 活跃进程：qwen25_14b_scale_001（cuda:0，模型下载中）、prompted_gen_gpt2xl_001（cuda:1，d2 stage）

### 3. 📊 当前状态
**刚完成**：
- Dream 审稿分析（dream_20260517T075852，三档 best=3.0 / median=3.0 / worst=2.5）
- Manager 自查指令的完整回应（已 director_reply_to_user）
- experiment_plan.yaml 更新：新增 plan_018/019/020，同步 plan_014/016/017 的 registry_id
- ROADMAP 更新为当前冲刺状态
- D036 决策记录：补充 Binoculars/Fast-DetectGPT baseline
- 已派 Agent 执行 3 个任务（Binoculars/Fast-DetectGPT baseline + MLP baseline + Table 1 CIs）

**RUNNING 实验**：
- qwen25_14b_scale_001（plan_014）：13B FP16 Qwen2.5-14B，cuda:0，模型下载中，预计还需 ~18h
- prompted_gen_gpt2xl_001（plan_016）：GPT-2 XL topic-seeded ecological validity，cuda:1，d2 stage，预计 2-4h

**等待中**：
- Agent 回复（刚派的 Binoculars/Fast-DetectGPT + MLP + CI 任务，Agent idle 时派出）
- plan_016 完成回调 → cuda:1 释放后可跑 plan_018 的 GPU 推理部分

### 4. 📋 待办（条件触发式）
- Agent 回复 baseline 任务进展 → 审批实验方案，确保 Binoculars/Fast-DetectGPT 正确校准为 ordinal bin
- prompted_gen_gpt2xl_001 完成 → 检查结果：acc≥70% 则强 ecological validity claim；acc 50-70% 则 "signal persists with attenuation"；acc<50% 则写为 limitation
- qwen25_14b_scale_001 完成 → 同理：acc≥70% 强 scale claim；acc 55-70% "scale-dependent attenuation"；acc<55% 需调整 framing
- plan_018 (Binoculars/FD-GPT) 完成 → 预期 negative（它们做不好 ordinal depth），写入论文作为 "existing detectors cannot solve ordinal depth" 的证据
- 所有补充实验完成 → 派 Paper Agent 执行：(a) 结果写入 Appendix，(b) 引用扩充到 30+，(c) 调整 d0 膨胀措辞，(d) Section 6 合并到 Section 4
- Paper Agent 完成 → submit_paper_to_review R10

### 5. 🎯 战略上下文
**核心定位**：Task formalization + systematic empirical study，不是 method paper。RF/LR 是工具不是贡献，Atlas/EDD/feature universality/strategy interaction 才是。

**Main vs Findings 分水岭**：Dream 三档都认为 Binoculars/Fast-DetectGPT baseline 是最关键缺口。补上这个（预期 negative result）+ 13B/prompted gen 结果好 → 有竞争力冲 Main。没有这个 baseline → 审稿人直接问 "why not just recalibrate existing detectors?"

**易错点**：
- plan_017 (cross_strategy_pipeline_001) 在 registry 已 DONE，但 plan 文件之前没有 registry_id — 已修复，但注意 strategy classifier 只有 57.8%（远低于预期 >90%），论文 claim 必须诚实
- Dream worst case 想象的数字（14B 55%、prompted 50%）是悲观想象，不是实际结果，不要被这些数字影响判断
- 论文页数极紧（8 页刚好），任何新内容只能进 Appendix
- R9 审稿修复全部完成并经 Reviewer 验证，不要重复做
- review_issues.yaml 有 ~70 个 issue 的完整追踪记录，处理审稿报告时先读它


---
