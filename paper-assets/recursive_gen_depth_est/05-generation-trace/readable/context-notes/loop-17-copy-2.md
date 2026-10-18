# reviewer / loop_17.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`ab395e951e403e15a09f.json`](../../sessions/ab/ab395e951e403e15a09f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-23T19:43:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `gpu-6000pro-2`，GPU 白名单需从 `execution.gpu_ids` 读取，审查训练实验时必须核对 CUDA_VISIBLE_DEVICES 是否越界
- 论文 FPR 数据：结论段已改为 "15–34%" raw / "below 7%" calibrated，不可回退到旧版 "2–3%"（此前因 RedPajama 6.98% 触发过 CRITICAL）
- Abstract 硬限 200 words（EMNLP 2026）
- Limitations 只能有一个，放正文，appendix 不能有 limitations section
- fig_confusion_matrix 已移回附录，Figure 5 现在是 fig_transfer_comparison——不要误认为正文有 confusion matrix

### 2. 🖥️ 基础设施快照
- 服务器：`gpu-6000pro-2`，远程代码根目录 `/root/autodl-tmp/recursive_gen_depth_est`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 论文目录：`docs/paper/`，编译产物 `main.pdf`（27 页，8 页正文 + Limitations + References + Appendix）
- Registry：`registry.yaml`，150 实验（95 success, 14 negative, 17 failed）
- 活跃进程：无。全部实验已完成，GPU 空闲。Director 此前确认不再跑新实验。

### 3. 📊 当前状态
刚完成最终图表审查：确认 2 张新图（fig_feature_trajectory 提升为 Figure 3，fig_transfer_comparison 新画为 Figure 5）数据一致、布局合理、PASS。

论文处于投稿前终态：
- 正文 8 页，5 图 5 表，§6 Discussion 压缩为单段
- 模拟审稿预测：Overall 3.0（Findings 线）
- 无 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调或 Cron

### 4. 📋 待办
- Director 要求最终 consistency scan → 已完成并 PASS，无 pending action
- 若 Director 再次要求审查 → 注意 8 个仍未引用的 orphaned appendix sections（app:depth4_ext, app:detector_baselines, app:zeroshot_prompt, app:e2e, app:ref_ablation, app:learned_estimator, app:multi_tau, app:domain_bias），优先级低但审稿人可能注意到
- 若论文修改涉及 Discussion → 建议加一句 FPR 到 "Deployment considerations" 段（目前 FPR 只在 Limitations 提及，Discussion 无覆盖）
- 若 Contribution 3 措辞被问到 → 建议 "Accumulation robustness" 改为 "Accumulation characterization"（claim 强度与证据更匹配）

### 5. 🎯 战略上下文
- 论文核心结论：(1) perplexity tail features 主导 depth signal，(2) strategy effect > model effect，(3) scale attenuation at 14B
- 7B self-reference ceiling（52.1%, EDD=0）是关键发现，已整合到 Discussion 但未进 Abstract——审稿人可能追问
- **易错点 1**：本地 workspace 和远程服务器可能有同名文件但版本不同（论文在本地，代码/数据在远程）。断言"未修改"前必须双边核对
- **易错点 2**：Explore agent 曾报告不存在的文本位于特定行号——永远用 Grep/Read 独立验证，不信 agent summary
- **易错点 3**：cross-strategy 数据（64.9/59.0/53.3）是从附录表按模型取均值计算的派生值，不是 registry 直接记录的——修改附录表会连锁影响 Figure 5


---
