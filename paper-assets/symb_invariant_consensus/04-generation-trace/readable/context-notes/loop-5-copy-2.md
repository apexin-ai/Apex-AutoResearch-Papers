# agent / loop_5.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`cfaa269999a3a0ef5016.json`](../../sessions/cf/cfaa269999a3a0ef5016.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-16T04:41:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- **只能用 westd-32608:cuda:0**，gpu_ids=[0]，白名单外的 GPU 一律 push back
- **max_tokens ≤ 4096 (14B 模型)**：max_model_len=8192，超过会 400 错误（QwQ-32B 时代用 10240/12288，14B 不适用）
- **sica_folio30 (QUEUED) 已废弃**：spec 里写的 QwQ-32B + max_tokens=12288，不可直接启动，需要更新 spec 或作废
- **vLLM 独占**：实验运行期间禁止其他进程向 port 8000 发请求
- **May 19 UTC 是 EMNLP 生死线**：D012 MVP 未 pass → 放弃 EMNLP，切 AAAI 2027 (Aug 1)

### 2. 🖥️ 基础设施快照
- **服务器**: westd-32608, root@, 工作目录 `/root/symb_invariant_consensus`
- **Python**: `/root/miniconda3/bin/python` (conda base), 激活命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**: Qwen2.5-14B-Instruct @ `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`
- **vLLM**: PID 174291, port 8000, max_model_len=8192, gpu_mem_util=0.85, 27.6 GiB
- **QwQ-32B** (已停用): `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`
- **数据**: `data/proofwriter_30.json` (30q) + `data/folio_30.json` (30q)
- **活跃进程**: sica_d012_14b PID 177178, tmux session=sica_d012_14b, cuda:0
- **⚠️ 无 cron 注册**: sica_d012_14b 没有 cron 监控，需要手动 poll 或注册 cron
- **磁盘**: 根分区 16GB free, /root/autodl-tmp 232GB free

### 3. 📊 当前状态
**刚完成**: D016 C0 预检 (sica_d016_c0_precheck) SUCCESS — Qwen2.5-14B-Instruct 多候选率 46% (FOLIO 40%, PW 50%)，远超 20% 阈值，SC accuracy 73%。Director 批准了全量 D012 评估。

**正在运行**: `sica_d012_14b` — 全量 D012 MVP 评估，ProofWriter-30 + FOLIO-30 合并 60 题，K=12，Qwen2.5-14B-Instruct。用 `run_full_mvp.py --mode vllm` 跑。提交时间 04:05 UTC。**没有 cron 监控**，这是第一优先修复项。

**QUEUED 但废弃**: `sica_folio30` — QwQ-32B spec，不再适用，应标记 killed 或更新。

**Worker 池**: 0 个运行中 Worker（失职状态，但当前只有 1 GPU 且在跑实验，非 GPU 任务应该铺起来）。

### 4. 📋 待办（条件触发式）
- **立即** → 为 sica_d012_14b 注册 cron 监控（或手动 poll 确认进程存活）
- **立即** → sica_folio30 标记 killed（spec 过时，已被 sica_d012_14b 覆盖）
- **sica_d012_14b 完成 → 结果分析**:
  - C0 ≥ 20% 且 C1 ≥ 50% 且 C2 ≥ 5 且 C3 ≥ SC+2pp → **D012 PASS**，向 Director 汇报 success，开始铺论文写作
  - 任一 FAIL → 按 red-section 产 Framing 调整提案，汇报 Director，**不默默跑下一个**
- **D012 PASS → 铺论文骨架** → spawn writer workers（intro/method/experiments 并行）
- **D012 FAIL + C0 still high but C3 < SC+2pp → 检查是否 72B-AWQ 能救**（memory.md 提到的备选）
- **非 GPU 并行任务可以现在铺**: 文献扫描 (literature-scan)、论文 framing 更新、experiment plan 整理

### 5. 🎯 战略上下文
**核心决策链**: D010(AIME 0pp)→D011(MATH预判同)→D012(逻辑域MVP标准)→D013(MaxSAT结构失效)→D014(根因=缺answer assertion)→D015(FOLIO也0%多候选)→D016(模型pivot到14B)→C0 PASS(46%)→**现在: 全量D012评估中**

**项目命运取决于 sica_d012_14b 这一个实验**。QwQ-32B 已全域 FAIL，14B 是最后的 pivot。C0 已 PASS (46% >> 20%)，关键看 C3 (SICA > SC+2pp)。

**易错点**:
- 不要把 sica_folio30 (QwQ-32B, QUEUED) 当成待启动实验——它已被 sica_d012_14b 覆盖
- 14B 的 max_tokens=4096，不是 QwQ 时代的 10240/12288
- sica_d012_14b 用的 `run_full_mvp.py` 同时跑 PW+FOLIO，不需要分开启动
- 如果 vLLM (PID 174291) 挂了，实验会持续 400 报错但进程不退出——需要检查 vLLM 健康
- **D012 的 4 个指标全部要 PASS**，不是只看 accuracy gap


---
