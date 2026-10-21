# agent / loop_2.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`961e133fd66d8904e3f7.json`](../../sessions/96/961e133fd66d8904e3f7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-12T14:09:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：home-1x5090 cuda:0 / seetacloud-westd-4x5090 cuda:0,1,2,3 / westd-48478 cuda:2,3。**westd-48478:cuda:2,3 分配但从未成功跑过实验，状态不明——提交前必须先 SSH 探测可用性**
- seetacloud-westd-4x5090 account=root，home-1x5090 account=sonny，westd-48478 account=sonny
- 8B 模型在 5090 上单卡可跑（bs=2, grad_accum=16），但 **GPU 上有残留进程时必 OOM**——提交前检查 nvidia-smi
- per-test accuracy vs traj accuracy 是**不同粒度对比**（1890 tests vs 1032 variants），不能直接声称 per-test > traj。clustered bootstrap 已证明 variant-level gap 不显著 (p=0.646)。论文中只能 claim diagnostic granularity 优势，不能 claim accuracy 优势
- HF cache 在 seetacloud 必须设 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则根分区爆满

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**：4×RTX 5090, root@, `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`（conda base，不用 venv）
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-{4B,8B,32B}`
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/{train,val,test,traj_train,traj_test}.jsonl`
  - 活跃: cls-seed0 (cuda:1 RUNNING), cls-seed789 状态待确认
- **home-1x5090**：1×RTX 5090, sonny@, `/home/sonny/exec-sim-repair-verifier`
  - Python: 系统 python3（无 conda）
  - 模型: HF cache 默认路径
  - 活跃: cls-seed789 (cuda:0 RUNNING)
- **westd-48478**：sonny@，cuda:2,3 分配但**从未跑过实验**，基础设施未验证

### 3. 📊 当前状态
**刚做完**：cls8b-seed123 OOM 诊断→Worker 清理 GPU 0→重试→成功 (accuracy 89.4%)。已更新 registry + 向 Director 汇报 8B cls-cwm 2-seed gap=2.62pp。

**RUNNING**：
- `cls-seed789` (home-1x5090:cuda:0) — 补 4B cls 第 4 seed，用于 5-paired comparison
- `cls-seed0` (seetacloud:cuda:1) — 补 4B cls 第 5 seed，同上

**等待中**：
- cls-seed789 / cls-seed0 完成 → 做 5-seed paired bootstrap（cls vs traj）
- per-test-majority-voting 结果：之前派了 Worker 分析但 Worker 池已归零，结果可能需要重新提取
- westd-48478:cuda:2,3 空闲——已在汇报中向 Director 标记，等 Director 决策

### 4. 📋 待办
- cls-seed789 + cls-seed0 两个都完成 → 做 5-seed paired bootstrap (cls vs traj at variant level)，更新 traj-level-finetuned notes
- 5-paired 完成 → 汇总所有 scaling 数据（4B/8B × cls/cwm × multi-seed），产出 Table 1 数据
- per-test-majority-voting 若 Worker 未返回结果 → 重新派 Worker SSH 读取 `/home/sonny/exec-sim-repair-verifier/eval_majority_voting.json`
- Director 对 westd-48478 空闲 GPU 有指示 → 按指示铺实验；无指示 → 再次催问
- seetacloud cuda:0 空闲（cls8b-seed123 完成后释放）→ 如有新实验可铺立即提交

### 5. 🎯 战略上下文
**核心结论链**：
- D007: CWM ≈ cls 在函数级（negative）→ pivot to complexity-dependent advantage
- D015: 8B scaling 确认 cls 优势随模型增大扩大（gap 0.9pp@4B → 2.62pp@8B）
- 但 traj vs per-test 的 accuracy 优势被 clustered bootstrap 推翻（D014: gap 不显著 p=0.646）

**最容易判断错的事**：
1. **不要声称 per-test accuracy > traj accuracy**——这是苹果橘子比较，已被 bootstrap 否定。Per-test 的优势是 diagnostic granularity（知道哪个测试失败），不是 raw accuracy
2. cwm8b-seed123 notes 里的 "seed123=3.50pp" 是错的（用了 cls seed42 vs cwm seed123），正确 seed-matched gap 是 2.42pp
3. 8B CWM 几乎不受 scaling 影响（4B 87.51% → 8B 87.33%），**CWM 的瓶颈是生成任务复杂度本身**，不是模型容量——这是 complexity hypothesis 的核心论据
4. ROADMAP 说 repo-level 是"最后机会"——如果 repo-level 也 null，Plan B 是 EMNLP Findings/workshop（scope 收缩到 C3 oracle frontier + null results + efficiency）
5. ARR May 25 只剩 13 天，0 容错


---
