# director / loop_1.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`e7e63fed0d7139a26d8a.json`](../../sessions/e7/e7e63fed0d7139a26d8a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T04:27:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：home-1x5090 cuda:0 + seetacloud-westd-4x5090 cuda:0/1/2/3（共 5 张）
- home-1x5090 SSH 用户 sonny（非 root），sudo 需要密码，Docker 已装好
- seetacloud SSH: `ssh -p 48478 root@connect.westd.seetacloud.com`
- trace-then-judge 实验已被 D009 kill（方法论缺陷：trace 模板泄漏 mutation type），不要重启
- SWE-bench 数据必须同步收集 classification labels + execution output（CWM target），不能只存 pass/fail
- Repo-level go/no-go 标准（D008）：≥3pp+p<0.05 → 推进 / 1-3pp → 加 seeds / <1pp → kill C1 pivot Plan B

### 2. 🖥️ 基础设施快照
- **home-1x5090**（implicit5638.xyfu.me, user=sonny）
  - 工作目录：`/home/sonny/exec-sim-repair-verifier`
  - Docker v29.1.3 已安装，sonny 在 docker 组
  - 数据：`data/train.jsonl`(15290) `val.jsonl`(1896) `test.jsonl`(1890)，函数级 HumanEval/MBPP
  - Checkpoints：`checkpoints_seed{42,123,456}/best/`（classification），`cwm_checkpoints/best/`（CWM）
  - 活跃进程：traj-level-finetuned PID 2311569（cuda:0，~2h），SWE-bench 全量 PID 2312582（CPU/Docker，250 instances，~8-15h）
- **seetacloud-westd-4x5090**（connect.westd.seetacloud.com:48478, user=root）
  - 环境搭建 Worker 已派出（可能已完成），需确认 Python/CUDA/模型是否就绪
  - 4 张 cuda:0-3 待分配实验

### 3. 📊 当前状态
刚处理完：Dream 成功（best=weak accept, median=borderline, worst=reject）、CWM negative（函数级 null）、multi-seed 确认 null robust、D007 pivot 到 complexity-dependent、D009 kill trace-then-judge、GPU 扩到 5 张、SWE-bench pipeline 4 个 critical 修复完成。

Registry 状态：
- traj-level-finetuned: RUNNING（home cuda:0，PID 2311569）
- SWE-bench 全量数据构建: 运行中（CPU，PID 2312582，2/240 instances）
- multi-seed-core: DONE (success)，3 seeds mean F1 88.4±1.0
- cwm-baseline: DONE (negative)，F1 diff <0.2pp
- mvp-b-train P/R 值第 4 次要求修复，可能已处理

等待中：seetacloud 环境搭建完成回调、traj-level 训练完成回调、SWE-bench 全量数据完成（8-15h）

### 4. 📋 待办
- traj-level-finetuned 完成 → eval + 汇报 per-test vs trajectory-level 对比 → home cuda:0 接 per-test-precision-recall(1h) + block-corr-empirical(1h) + CWM seed123/456(2h)
- seetacloud 环境就绪 → 并行启动：cuda:0 model-size-scaling(8B)、cuda:1 llm-judge-baseline、cuda:2 per-test-majority-voting、cuda:3 待数据
- SWE-bench 全量数据完成 → repo-level classification + CWM 训练（分配到空闲卡）→ go/no-go 决策（D008 标准）
- repo-level F1 diff ≥3pp → 全力推进 EMNLP Main；<1pp → pivot Plan B（C3 frontier + null results + efficiency = Findings）
- mvp-b-train P/R 修复确认 → 如仍未修，第 5 次催

### 5. 🎯 战略上下文
- 决策链：D001(MVP设计) → D002(MVP-A pass) → D003(P2P ~1%) → D004(story reframe) → D005(post-MVP priorities) → D006(MVP pass) → D007(complexity-dependent pivot) → D008(repo-level go/no-go) → D009(kill trace-then-judge)
- **核心判断**：这是第三次 pivot（granularity → reformulation → complexity-dependent），Reviewer 标记为"高风险投机性前进"。repo-level 是最后机会。如果 repo-level 也 null，接受 Plan B（Findings/workshop）
- **Dream 三档共识**：无论结果如何都必须补 related work（15-20+篇）和 model diversity（DeepSeek-Coder/CodeLlama）。这两项已通过 GPU 扩容部分解决（8B scaling），但跨家族模型还没加入计划
- **易踩的坑**：(1) Agent session 因服务器重启频繁丢失，派单后要确认 found=true (2) ROADMAP GPU 状态不要写"在跑"除非亲自确认 (3) trace-then-judge 不能重启（D009）(4) SWE-bench 数据的 test 字段必须是函数代码不是名称字符串
- **时间线**：ARR May 25（~12 天），关键路径 = SWE-bench 数据(8-15h) → repo-level 训练(12h) → eval → 写作(5-7d)，0 容错


---
