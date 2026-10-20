# agent / loop_9.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`a535f67d2f0099566094.json`](../../sessions/a5/a535f67d2f0099566094.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-14T21:01:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（westb-13313），配置文件 `gpu_ids: ["cuda:0", "cuda:1"]`
- 论文数字唯一来源：`eval_end_to_end.py` 产出（trained-router: -10.70 [-15.25, -6.38]）；`eval_implicit_router.py` 的 -12.84 **不用于 Table 1**
- 唯一可用训练数据：`data/plan-004-implicit/implicit_sft.jsonl`（MD5: c9b59e04de78, 2040 samples）；`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏（D026）
- Qwen3 推理必须 `enable_thinking=False` + regex 清理 `&lt;think>` tags
- Classification head 路线已宣告失败（D025），不要再尝试 2-class classification
- Framing 定稿为 Option B（D033）：贡献 = empirical finding + diagnostic methodology，**不是** router 架构

### 2. 🖥️ 基础设施快照
- 服务器：**westb-13313**，2× RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/simgate-modular-routing`
- Python/环境：先 `detect_image` 探测，历史上用 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）或 AutoDL 默认环境
- 模型：Qwen3-1.7B LoRA，checkpoint 在 `checkpoints/plan-004-implicit/final_adapter`（⚠️ 勿与 `checkpoints/plan-002-generative-v1/final_adapter` 混淆）
- W&B / HF cache：`HF_HOME=/root/autodl-tmp/.hf_cache`，AutoDL 需 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1`
- 活跃进程：**无**（0 RUNNING 实验，0 活跃 Worker，0 活跃 Cron）
- cuda:0 和 cuda:1 均空闲

### 3. 📊 当前状态
**阶段：R3 审稿已提交，等待结果。**

- R2 得分 Borderline Accept - Findings (2.75/5)；3 Blockers（标题 scope / train-test split / penalty sensitivity）全部修复
- R3 得分 Weak Accept - Findings (3.25/5)，camera-ready 修复中（D049）
- 论文本地编译通过：7 页（正文 4p + 非计入 3p），0 warnings，22 bib entries
- ALFWorld 跨环境证据已写入 Limitations + Conclusion
- 全文数字一致性交叉验证通过
- 58 experiments 全部终态：22 success / 13 negative / 10 failed / 13 killed
- Registry 中 3 个 PREPARING 状态实验（plan-003-baseline, plan-001b-gpu1-rebalance, mvp-p1-signal）为历史遗留，非活跃
- **无等待中的 Worker 回调、Cron 或 Director 决策**

### 4. 📋 待办（条件触发式）
- R3 审稿结果返回 → 读 reviewer comments → 如有新 blockers，派 Worker 修复 + 更新 report.md → 汇报 Director
- Director 指示 camera-ready 修改 → 派 Worker 编辑 LaTeX + 本地编译验证
- 远程同步需求触发 → 派 Worker rsync 到 westb-13313 + 远程 pdflatex 编译验证
- 最终 PDF 视觉检查 → 派 Worker 用 `pdf_to_images` 渲染 + 逐页审查
- 5/23-24 到达 → ARR 提交流程（终稿冻结 + 格式检查 + 上传）

### 5. 🎯 战略上下文
- **核心发现**：death avoidance 占 ~90% routing signal（DAF 在 P=10→94.5% at P=200 单调递增，Pearson r=0.9698）。这是论文唯一 story，不是 router 性能。
- **决策链关键节点**：D013（framing pivot 到 death avoidance）→ D033（Option B 方法论贡献定稿）→ D046（撤销 pivot 回归 analysis paper）→ D048/D049（R2/R3 修复）
- **易判断错的事**：(1) Router balanced_acc=58.1% 看起来很差，但这 IS the finding——router near-random 证明 death avoidance dominates；(2) MATH 跨环境验证信号反转（D045/D046），MATH 结果只入 Discussion 不扩全量；(3) plan-003-baseline 等 PREPARING 实验是历史遗留，不需要推进
- **R3 后最可能的路径**：如果 Weak Accept 维持 → camera-ready 小修 → 5/25 前提交 ARR；如果新 blockers → 快速迭代（GPU 空闲可即时补实验）


---
