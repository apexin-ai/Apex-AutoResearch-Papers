---
loop: 7
reason: idle_timeout
updated: '2026-05-16T16:16:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `autodl-5090:cuda:0/1/2/3`（4× RTX 5090 32GB），禁止触碰其他设备
- **训练数据量混淆（critical confound）**: Vanilla=4,358 samples vs TaxEI/Random=9,029 samples——汇报和论文中必须标注，不能暗示性能差异纯由注入方法导致
- **LLaMA detection_rate 是假阳性**：21-36% 全部由 "go back to X" 中的 "back" 触发关键词匹配，非真实错误检测。**绝不可引用此指标**
- **v1 forward pass 数据已作废**（turn-level aggregation bug），只能引用 v2 trajectory-level 数据
- `submit_training_job` 命令必须用 `bash -c "source /root/miniconda3/bin/activate && ..."` 包裹
- Eval 并行：每卡独占一个 eval（~16.8GB/eval），**禁止两个 eval 共享同一张 GPU**
- 48 个 PREPARING 状态实验中大量是 stale（已有 conclusion 但未转 DONE），不要误以为它们需要执行

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **模型 base**: Qwen3-8B / LLaMA-3.1-8B-Instruct（路径在各实验 spec 中）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **网络**: `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + SSL cert 设置
- **活跃进程**: 无。0 RUNNING 实验，0 Worker，0 Cron
- **GPU 状态**: 4× RTX 5090 全部空闲

### 3. 📊 当前状态
**刚完成**: LLaMA-3.1-8B 3-seed 跨模型验证全套（clean + injected + recovery），Recovery eval Qwen 15/15 全部完成，paper_framing.md 已升级为"跨模型训练不稳定性"叙事。

**Registry**: 192 实验，144 DONE（131 success / 5 negative / 7 failed / 1 killed），48 PREPARING（大部分 stale），0 RUNNING。

**等待中**:
- Dream review `dream_20260516T153939` 结果——决定是否可启动论文写作
- Scale-up datagen 状态待确认（~405/1000 trajectories）
- 48 个 PREPARING 实验需清理（大量已有 conclusion 但卡在 PREPARING）

**无活跃 Worker / Cron / 进程。所有 4 张 GPU 空闲 = 违反 L1 红线（除非确认全部下游阻塞等 Director 决策）。**

### 4. 📋 待办（条件触发式）
- Dream `dream_20260516T153939` 返回 → 分析审稿反馈 → 若通过则向 Director 汇报并申请启动 Paper Agent 写作
- Dream 指出 claim 缺陷 → 按 red-section 产出 Framing 调整提案 → Director 审批
- Director 批准写作 → Read `paper-plan` skill → spawn 多 Worker 并行写各章节
- Scale-up datagen 确认状态 → 若仍在跑则继续监控；若停滞则诊断/重启
- 48 个 stale PREPARING 实验 → 批量 `update_registry(status=DONE)` 清理
- LLaMA 统计检验待补：Levene's test（TaxEI SD=8.6% vs Random SD=2.1%）、bootstrap CI

### 5. 🎯 战略上下文
**核心结论链**:
- D033: taxonomy 标签零收益（TaxEI=Random=58.3%，完全一致）
- D035-D038: 剂量响应无安全剂量，25% 是 taxonomy penalty 峰值（-7.3pp）
- D041: Recovery rate ≈ clean success rate——模型靠 resilience 而非检测/恢复
- D043: Recovery-paired SFT 适得其反（50.2% < baseline 58.3%），Claim 7 定论
- D047: **跨模型核心发现**——TaxEI SD=8.6pp vs Random SD=2.1pp，结构化注入跨架构不稳定

**Paper framing**: Negative result paper。核心叙事="结构化错误注入跨模型导致训练不稳定，Random 稳定，taxonomy 标签零收益"。9 claims 中 7 有完整支撑，Claim 8 降级为 Discussion（WebShop 不适配），Claim 9（跨模型）已完成。

**易踩坑**:
- 不要把 LLaMA TaxEI s123 的异常低值（61.7% clean / 59.6% recovery）当 bug——它是 seed variance，但论文必须讨论（1/3 seed catastrophic）
- 50% dose-response 的 s0/s123 值在 TaxEI 和 Random 间完全对调——不是数据错误，permutation p=0.13
- Worker 假完成历史严重（vanilla-s123 经历 5 次），新 Worker 必须轮询到进程结束+验证输出文件
- Cron EXIT_CODE=129 是 tmux SIGHUP 误报，判断训练成功应检查 checkpoint 完整性
