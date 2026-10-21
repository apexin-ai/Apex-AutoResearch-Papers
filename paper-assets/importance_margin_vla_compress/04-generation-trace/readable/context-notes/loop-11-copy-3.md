# reviewer / loop_11.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`5b603de28529f9f07dec.json`](../../sessions/5b/5b603de28529f9f07dec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-21T17:43:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- Spatial suite 对比禁止用 LoRA baseline (6.2%) 作基准，必须用 official baseline 或 full-FT（C001 约束）
- SmolVLA official baseline 论文当前写 59.2%（来自 2026-05-18 首次评估，296/500），但新 seed42 评估为 57.2%（286/500）——在 seed43 完成前不要断言哪个"正确"，两者都在 Wilson CI 内
- **π0.5 random k=0.9 = 12.0% 是已确认的异常**（违反单调性：k=0.7=75.5%），已提 CRITICAL 报告 #40，结果确认前禁止写入论文
- westd-38929 GPU0 上有 PID 378383 同时占用 GPU0+GPU1（跨 GPU 进程），这不是 bug——它是 SmolVLA official 某个评估进程的 PyTorch 行为

### 2. 🖥️ 基础设施快照
- **cqa1-33015**: 4×24GB GPU。代码根 `/root/autodl-tmp/importance_margin_vla_compress`。HF cache `/root/autodl-tmp/.hf_cache`。当前 4 GPU 跑 SmolVLA official sweep 第二批（L2norm k=0.7/0.95, random k=0.9/0.5, 全 seed42）
- **westd-38929**: 4×H800 98GB。代码根同上。GPU0-1: SmolVLA official seed43 (baseline + random k=0.95)。GPU2: SmolVLA random k=0.5 seed43。GPU3: SmolVLA L2norm k=0.95 seed43 (PID 425225)
- **westd-41074**: 4×GPU。GPU0+GPU1 **空闲**。GPU2: VTC M96 训练 PID 68539 step ~66K/100K。GPU3: VTC M64 v6 训练 PID 59671 step ~16K/100K
- **westd-27271**: 2×GPU。GPU0: OpenVLA L2norm k=0.5 seed43。GPU1: VTC M32 训练 PID 921279 step ~67K/100K
- 论文本地路径: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`
- main.tex \input: abstract, introduction, related_work, experimental_setup, results, analysis, conclusion, appendix（background.tex 和 discussion.tex 不编译）

### 3. 📊 当前状态
**刚做完**：
- 提交报告 #40-#43：π0.5 random k=0.9 CRITICAL bug、SmolVLA official sweep 完整结果、资源汇总、baseline 不一致 warning
- SmolVLA official sweep seed42 在 cqa1 全部完成：baseline=57.2%, L2norm k=0.9/0.5=0%, random k=0.95=0%。Cliff-edge 架构性确认
- π0.5 k=0.9 两实验已完成：L2norm=98.2%（与 baseline 一致）, random=12.0%（CRITICAL 异常）
- Worker 执行了 `worker_debug_pi05-random-k09-bug` 但 registry/report 无新发现，代码审查未发现明显 bug

**RUNNING 实验** (registry 13 条，含多条 stale):
- SmolVLA official sweep: 4 条 seed43 在 westd-38929, 3 条 stale seed42 在 cqa1（结果已出但 registry 未更新）
- π0.5 k=0.9: 2 条 stale（结果已出，进程已退出）
- OpenVLA L2norm k=0.5 seed43: westd-27271 GPU0
- VTC 训练: M32 (~18h), M96 (~19h), M64v6 (~39h)

**等待**：Director 对 π0.5 random k=0.9 CRITICAL 报告的决策（重跑/代码修复/接受）

### 4. 📋 待办（条件触发式）
- SmolVLA official seed43 结果出来 → 验证是否全为 0% SR，计算 2-seed baseline mean±std，对比论文 59.2%
- Director 回复 π0.5 random k=0.9 bug → 根据决策（1）审查代码修复 或（2）审查 seed43 重跑结果 或（3）确认从论文中排除该数据点
- VTC M32/M96 训练完成（~19h 后）→ 审查 eval 部署、验证 SR 与 SmolVLA VTR 对比
- OpenVLA L2norm k=0.5 seed43 完成 → 计算 multi-seed mean（seed42=39.2%），更新论文表格
- cqa1 第二批 sweep 完成 → 验证 L2norm k=0.7/0.95 和 random k=0.9/0.5 均为 0%（预期），更新 appendix tab:smolvla_ablation
- Paper Agent 提交新版本（post Action Matrix 修改）→ 执行审查模式 B，特别关注：causal language 降级、SmolVLA official 数据更新、页数压缩

### 5. 🎯 战略上下文
- **核心论文 story**: Vision connector 类型决定 token compressibility。四类谱系（uniformly critical / threshold-graded / smooth graded / catastrophic cliff）由 CV 单次前向 pass 可诊断
- **CV 值**: π0=0.038, π0.5=0.055, X-VLA=0.151, OpenVLA=0.215, OFT=0.219, SmolVLA=0.314
- **W-C2 已完成**（最关键实验）：SmolVLA official checkpoint cliff-edge 确认，架构性非训练伪影
- **CoRL 2026 DDL**: Abstract May 26, Paper May 29
- **易判断错的事**:
  1. π0.5 的反直觉行为——random > L2norm 在 k=0.5/0.7，但 L2norm > random 在 k=0.9。k=0.9 random=12% 几乎确定是 bug，不要接受为"有趣的发现"
  2. SmolVLA 的 59.2% vs 57.2% 不是"数据错误"——是不同 seed 的正常变异，但论文必须保持一致性（选一个 or multi-seed mean）
  3. VTC M64 已重启为 v6（从 step 0 开始），registry 仍指向 v5——M64 会是最后完成的 VTC 训练（~39h），可能来不及 eval before DDL
  4. discussion.tex 和 background.tex 不在 main.tex 编译链中——这些文件的问题不影响提交


---
