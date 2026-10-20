# director / loop_2.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`520d4594457079f5ff23.json`](../../sessions/52/520d4594457079f5ff23.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T01:42:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-22162 的 cuda:0~3（项目配置白名单），严禁跨项目抢卡
- importance 指标修复前的所有 v1-v4 系列 II 结果**不可引用**（D013：NaN 中毒 + 位置偏差导致伪影）
- D010 的 "strategy-dependent direction reversal" 结论**暂停**，需 v5 修复后数据重新验证
- float32 实验已取消（位置偏差不是精度问题），不要重启

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/pacs
- Python：aml-train 镜像，conda 环境 `/root/miniconda3/bin/python`
- 核心代码：`interaction_index.py`（importance 修复 commit `20182ec` + v2 NaN skip commit `5488041`）、`run_profiling.py`（robust stats）
- 模型：GPT-2（HF cache）；Qwen2.5-7B 下载中（ModelScope，不走 proxy）
- HF_HOME：/root/autodl-tmp/.hf_cache
- 4× RTX 6000 Pro 96GB，GPU 预算 ~250h 已用 ~2.9h

### 3. 📊 当前状态
**刚做完**：importance 指标根因修复（位置归一化 + NaN 层跳过），sanity check 通过（importance kv_ppl=1.37 < random=6.77）。

**v5 验证实验**（4 卡并行，各 ~30min，Agent 空闲 180min 说明应已全部完成）：
- mvp_v5_fixed_s015 (cuda:2) — sparsity=0.15
- mvp_v5_fixed_s020 (cuda:0) — sparsity=0.20
- mvp_v5_fixed_s025 (cuda:3) — sparsity=0.25
- mvp_v5_fixed_s030 (cuda:1) — sparsity=0.30

**Registry 状态预期**：v5 四个实验可能仍标 RUNNING（Agent 空闲未更新），需检查实际完成情况并更新。

**Qwen2.5-7B 下载**：可能已完成或仍在进行，需检查。

### 4. 📋 待办
- 启动后立即检查 v5 四个实验完成状态 → 收集结果、更新 registry
- v5 结果齐出 → 画 II-vs-sparsity 曲线（s=0.15/0.20/0.25/0.30），对比 importance vs random
- importance kv_ppl < random kv_ppl 在多数 sparsity 点成立 + II 符号反转显著 → MVP pass 标准评估
- 如果 strategy-dependent reversal 成立 → complete_mvp → post-mvp-kickoff（paper_framing + experiment_plan + dream_simulate）
- 如果 reversal 不成立 → 需再次 pivot，时间极紧（截稿 5/25，剩 11 天）
- Qwen 下载完成 → 跨模型复现验证（MVP pass 标准第 3 条）

### 5. 🎯 战略上下文
**决策链**：D009（random masking 系统性混淆）→ D010（pivot to strategy-dependent reversal）→ D011（float16 NaN）→ D012（暂停 importance 实验）→ D013（根因确认：位置偏差 + NaN 中毒，暂停所有结论）

**核心判断点**：v5 修复后结果是本项目的 make-or-break。sanity check 已显示修复有效（importance kv_ppl 1.37 vs random 6.77），但完整 50-sample bootstrap 的 II 符号和 CI 才是最终判据。

**易错点**：
1. 不要把 v1-v4 的 II 数值与 v5 混用——v1-v4 全部因 NaN+位置偏差无效
2. Random baseline 数据来自 mvp_v4_random_r2（seed=42, 50 samples），这组数据不受 importance 修复影响，仍然有效
3. Reviewer 提过 v5_s015/s025 的 spec 中 seed=null（v5_s020/s030 是 seed=42），如果结果异常先查可复现性
4. EMNLP 2026 ARR 截稿 5/25，剩 11 天——如果 v5 验证通过需立即进入 research 阶段全速推进


---
