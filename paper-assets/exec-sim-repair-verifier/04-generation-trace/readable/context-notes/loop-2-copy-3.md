# reviewer / loop_2.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`8fb9fe7b60d55b63aca4.json`](../../sessions/8f/8fb9fe7b60d55b63aca4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-12T15:32:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud-westd-4x5090 项目 GPU 白名单：**cuda:2, cuda:3**。cuda:0/1 属于其他项目，越界使用必须 CRITICAL 打回
- westd-48478 和 seetacloud-westd-4x5090 是**同一台物理机**，不要当两台算力
- seetacloud 根分区仅 **3.6GB free**（89%），所有 checkpoint/输出必须写入 `/root/autodl-tmp/`，否则磁盘爆满
- 代码路径是 `/home/sonny/exec-sim-repair-verifier/`，**不是** `/root/exec-sim-repair-verifier/`（Agent 已因此错误导致 repo-level-v2 提交失败）
- ssh_read_only 不支持管道符 `|`，多条件 grep 需拆成多次调用

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**（root）：4× RTX 5090 32GB，代码 `/home/sonny/exec-sim-repair-verifier/`，conda `/root/miniconda3/`，数据盘 `/root/autodl-tmp/` (151GB free)
- **home-1x5090**（sonny）：1× RTX 5090 32GB，代码 `/home/sonny/exec-sim-repair-verifier/`，8B 模型 `/home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B`
- 4B 模型：seetacloud HF cache `/root/autodl-tmp/.hf_cache/` 或 `/root/.cache/huggingface/hub/Qwen/Qwen3-4B`
- W&B：大部分实验 `--no_wandb`，不检查 W&B
- **活跃进程**：截至 handoff 时 **0 个训练进程**，全部 5 张 GPU 空闲

### 3. 📊 当前状态
刚完成的审查：
- **cls8b-seed456** 完成（88.31%），3-paired 8B scaling 分析已发给 Director（gap +2.42pp）
- **cwm8b-seed456** 完成（86.24%），确认 8B CWM 退化（86.96% < 4B CWM 87.19%）
- **error-overlap 分析**已审查（94.7% agreement，CLS mutation detection 优势）
- **repo-level-cls-v2 / repo-level-cwm-v2**：Agent 提交失败（路径错误 `/root/` vs `/home/sonny/`），已发 CRITICAL×2，至今未修复重启
- **数据不一致已发现**：worker_analysis_cls8b-seed456 汇总的 seed42/123 数字与 eval JSON 不符（差 ~1pp），已通知 Director

Registry: repo-level-cls-v2 和 repo-level-cwm-v2 为 PREPARING（从未成功启动），cls8b-seed456 为 RUNNING 待更新为 DONE，其余全 DONE

### 4. 📋 待办
- Agent 修复路径并重提交 repo-level-cls-v2/cwm-v2 → **立即核实**：(1) 路径 `/home/sonny/...`，(2) GPU 白名单 cuda:2/3，(3) output_dir 指向 `/root/autodl-tmp/`，(4) nvidia-smi 确认进程启动
- repo-level-cls 训练到 save_steps 时 → 检查磁盘空间（根分区 3.6GB 随时爆）
- repo-level 双完成 → Pillar 1 go/no-go 决策审查（F1 diff ≥3pp → 全力推 EMNLP，1-3pp → 加 seeds，<1pp → kill C1）
- cls8b-seed456 registry 更新为 DONE → 核对数字是否用了正确的 eval JSON（90.48/89.37/88.31，不是 worker 汇总的错误数字）
- home GPU 0 空闲 → 应被分配新任务（CWM per-instance prediction 提取 或额外 seed）
- 论文写作阶段开始 → 检查 paper_provenance.yaml 覆盖率，执行合规检查（Agent 是否看过 red-section skill）

### 5. 🎯 战略上下文
**核心结论链**：CLS > CWM，优势随复杂度/模型增大而扩大
- 4B 函数级：CLS 88.43 vs CWM 87.19（+1.25pp, one-sided p=0.025, 5-paired）
- 8B 函数级：CLS 89.39 vs CWM 86.96（+2.42pp, t(2)=11.4, 3-paired）
- CWM 8B 退化（86.96 < 4B 87.19）= generation 天花板证据
- **repo-level 是 Pillar 1 的决胜战场**，至今 0 步完成（反复被 bug/路径错误/进程被杀阻断）
- TOST ±2pp 等价检验通过 (p=0.007) 支撑 Pillar 2（函数级 CLS≈TRAJ）

**最容易判断错的事**：
1. Worker 汇总数字不可信——必须回溯 eval JSON 原始文件核对。已发现 8B 3-paired 汇总有 ~1pp 偏差
2. repo-level 训练每个需 ~15h（cls）和 ~23h（cwm），ARR deadline 2026-05-25 仅剩 13 天，是真正的 GPU-time 硬约束
3. 不要被"实验太多跑不完"的人类直觉误导——只看 GPU-hours 是否够。但当前 GPU 空转问题是真的 critical
4. seetacloud cuda:0/1 不属于本项目——即使空闲也不能用，之前有 GPU 越界事故教训（D024）
5. error-overlap 分析仅有 2 CLS + 2 CWM seeds 的 per-instance predictions，论文需要至少 1 对 matched-seed predictions


---
