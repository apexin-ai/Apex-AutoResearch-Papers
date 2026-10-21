# agent / loop_10.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`7cb7605ac58d85c163ad.json`](../../sessions/7c/7cb7605ac58d85c163ad.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T00:20:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `autodl-simgate:cuda:0` 和 `autodl-simgate:cuda:1`（westb-13313），禁止使用其他 GPU
- 论文 Table 1 数字必须来自 `eval_end_to_end.py`，不可用 `eval_implicit_router.py` 的数字（-12.84 已废弃，正确值 -10.70）
- 唯一可用训练数据文件：`data/plan-004-implicit/implicit_sft.jsonl`（MD5: c9b59e04de78, 2040 samples）。`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏（D026），绝对不可使用
- Qwen3 推理必须 `enable_thinking=False` + `re.sub` 兜底清理 `&lt;think>` tags，否则 eval 结果不可靠
- Checkpoint 路径：`checkpoints/plan-004-implicit/final_adapter` = ablation-b（成功的 router）。`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败），两者 eval metrics 相似易混淆

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，账号 root，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python 环境：conda base（aml-train 镜像），`/root/miniconda3/bin/python`。不要创建 venv
- GPU：2× RTX 5090 32GB（cuda:0, cuda:1），当前均空闲
- 活跃进程：无。0 tmux session，0 cron 任务
- Worker 池：0（report.md 注"后端无可用账号"）
- AutoDL 注意：pip/git 前 `source /etc/network_turbo`；HF 下载设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1`

### 3. 📊 当前状态
**论文阶段**：R3 审稿已提交（D049, Weak Accept - Findings 3.25/5），等待 R3 结果。R2 的 3 个 Blockers 全部修复完成（标题 scope / train-test split / penalty sensitivity）。本地编译通过：7 页（正文 4p + 非计入 3p），0 warnings，22 bib entries。

**实验全部终态**：58 experiments — 22 success / 13 negative / 10 failed / 13 killed，0 RUNNING / 0 PREPARING。所有 plan 级实验要么 DONE 要么 planned（未启动的 P1/P2 优先级：plan-002 router SFT, plan-005 routing pattern analysis, plan-006/008/009/010 均 planned 但非 critical path）。

**上一轮完成项**：
- alfworld-counterfactual-full 完成（det 27.4% vs int 3.0%），结果写入 Limitations + Conclusion
- 修复 2 处断引用 + 全文数字一致性验证通过
- R2→R3 所有修复（B1-B3, S1-S8）已完成并提交

**等待中**：无 Worker / Cron 回调。等待 R3 审稿结果返回。

### 4. 📋 待办（条件触发式）
- R3 审稿结果返回 → 读 review 内容，分叉：Accept → camera-ready 准备；Revision requested → 按 action matrix 逐条修复
- Director 要求远程同步 → spawn Worker rsync 本地→westb-13313 + 远程 pdflatex 编译验证
- Director 要求最终 PDF 视觉检查 → spawn Worker 用 paper-visual-review skill
- 5/23 到达 → 终稿锁定 + ARR 提交流程（需 Director 确认）
- Director 要求补充实验（如 plan-005 routing pattern analysis）→ 两张 GPU 空闲可立即启动
- 收到 `[WRITE HANDOFF]` → 立即写 handoff，不做其他事

### 5. 🎯 战略上下文
**核心结论链**：D013（pivot to analysis paper）→ D033（Option B: 方法论贡献 framing）→ D046（撤销 method paper pivot，回归 analysis paper）→ D049（R3 camera-ready）。论文贡献 = counterfactual 分析方法论 + death avoidance empirical finding（DAF=90.41%, r=0.9698）。Router 本身 balanced_acc=58.1±0.8%（仅比随机高 8pp）IS the finding，不要描述为"成功的 router"。

**易错点**：
1. 不要把 router 的 near-random performance 描述为失败——这正是 C1 的核心证据（death avoidance 主导，router 几乎无非死亡信号可学）
2. plan-004 v5（implicit routing）conclusion=negative，logit 级 balanced_acc=79% 但 generation 级退化到 41%——根因是 ga=1 导致 effective batch=4 过拟合。ablation-b 用 ga=8（effective batch=32）无此问题
3. Oracle routing 仅比 always-det 好 2.89 分（-6.58 vs -9.47），96.2% episode 也选 det——这直接支撑 C1
4. 文献新颖性已确认（12 篇扫描无 direct competitor），但论文必须有 dedicated Related Work section 对标 Toolformer/ART/Chameleon/CogRouter
5. MATH track（plan-009）和 ALFWorld 均为 exploratory，MATH 反转信号（D045）否定了统一 router 前提，只作 Discussion 素材


---
