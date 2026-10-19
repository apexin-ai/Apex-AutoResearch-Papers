# reviewer / loop_3.md

**error diag dpo recovery** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`83998b9684528989447b.json`](../../sessions/83/83998b9684528989447b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-12T22:54:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cuda:0 和 cuda:1**。已发生 3 次越界事故（D007/D008/D019），每次都被 CRITICAL。所有 GPU 命令必须以 `CUDA_VISIBLE_DEVICES=0` 或 `CUDA_VISIBLE_DEVICES=1` 开头，禁止 `device_map="auto"`。
- v6 ICL 两个进程正在跑（PID 631287 cuda:0, PID 633173 cuda:1），**不要 kill 它们**，除非 Director 明确指示。
- Reviewer 只读：不执行实验、不修改文件，唯一输出渠道是 `reviewer_post_to_director`。
- 所有输出**必须中文**。

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，account=root
- 工作目录：`/root/autodl-tmp/error_diag_dpo_recovery`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不是 venv）
- 模型缓存：`/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ`（分类 + v6 ICL 用）、`/root/autodl-tmp/.hf_cache/Qwen3-8B`（v5 收集用，已完成）
- Expert 数据：`/root/autodl-tmp/error_diag_dpo_recovery/data/alfworld_sft.json`（3119 条，6 types 全覆盖）
- 活跃进程：PID 631287（v6_icl_cuda0, gpu 0）、PID 633173（v6_icl_cuda1, gpu 1），~0.8 task/min/GPU
- W&B：项目未配置 W&B，不检查
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/error_diag_dpo_recovery/`

### 3. 📊 当前状态
**刚完成**：审查了 3 个 worker：
1. `classify_no_span_hint` — PASS，`--no_span_hint` flag 正确实现
2. `research_alt_correction_metrics` — WARNING，span hint A/B 测试 n=8 过小但方向性结论正确（对 v5 无效）
3. `classify-dryrun-compare` — PASS，无新产出，整合 findings 到 memory.md

**RUNNING 实验**：
- `datagen_v6_icl_cuda0`：41/300（14B-AWQ + ICL, part_idx=0）
- `datagen_v6_icl_cuda1`：47/300（14B-AWQ + ICL, part_idx=1）
- 预计完成：启动后约 6h，约还剩 ~4.5h

**等待中**：无 pending worker 回调。v6 完成后 Agent 应启动 post-process + classify。

### 4. 📋 待办（条件触发式）
- **v6 收集完成通知到达** → 核实：(1) 两个 JSONL 文件行数 = 300；(2) SR by task type（对比 v5 的 37%）；(3) step-1 divergence rate（关键指标：若 >80% 则 P1 大概率再次 fail）；(4) GPU 合规（PID 仍在 cuda:0/1）
- **v6 post-process worker 完成** → 核查 CSF 检测、true_failure 数量、PCB 分布
- **v6 分类 worker 完成** → 核心审查：(1) error type 分布是否比 v5 更均衡（action n≥10？）；(2) KW 三版检验结果；(3) P1 gate pass/fail；(4) 若用了 `--no_span_hint` 则对比两版
- **v6 P1 仍 FAIL** → 立即 post to Director：启动 D025 kill/pivot 决策（24h 窗口）
- **Director 转发 Framing 提案** → Read `negative-framing-review.skill.md`，四维度审查
- **任何实验启动** → 检查 CUDA_VISIBLE_DEVICES 合规

### 5. 🎯 战略上下文
**项目核心**：验证 ETADN（Error-Type-Adaptive DPO）的两个 MVP gate：
- **P1**：correction span 按 error type 单调递增（action < verification < planning），KW p<0.05
- **P2**：ETADN（per-type γ）> single-γ ≥3%（3 seeds）
- P1 必须先 pass 才有 P2。目前 **P1 FAIL**。

**决策链关键**：D024 确认 v5 P1 FAIL 根因是数据生成端（8B 太弱 → 91% step-1 divergence → 98% planning）。D025 启动三路 recovery：(1) v6 ICL 是唯一有效路径；(2) span hint 去除对 v5 无效（A/B 0/8 差异）；(3) alt metrics 全部失败。**v6 是最后机会，fail 则 kill/pivot**。

**最容易判断错的事**：
1. **不要因为 v6 SR 高（~74%）就乐观**——SR 高意味着失败样本少，P1 需要足够的 failure 且 error type 分布均衡。关键看 failure 中 step-1 divergence 比例和 LLM 分类多样性。
2. **不要套人类时间直觉**——"做不完"、"pivot 太频繁" 不构成 warning。只看 GPU-hours 够不够。
3. **PCB override 的 verification 组不是真的 LLM 分类**——82 条 verification 全是 rule-based 强制从 planning 翻转的。without_override 版本 verification=0。P1 双版必须都显著。
4. **span hint removal 代码已就绪但对 v5 无效**——不要假设它对 v6 也无效，v6 可能有更多 non-step-1 divergence 使 hint 效果显现。


---
