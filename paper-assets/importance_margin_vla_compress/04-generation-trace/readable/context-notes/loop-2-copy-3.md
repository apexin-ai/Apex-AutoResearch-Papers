# reviewer / loop_2.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`0282b29ac5c134aeb8fb.json`](../../sessions/02/0282b29ac5c134aeb8fb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-15T23:11:12+00:00'
---

## 硬约束

- **GPU 白名单**: constraints.yaml 未创建，无显式 gpu_ids 白名单。但 D023 规划 v8a→cuda:0, v8b→cuda:1。核实时以此为参考。
- **服务器**: westd-27271(root)，代码根目录 `/root/autodl-tmp/importance_margin_vla_compress`
- **Gate 标准**: G1(margin ratio ≥2x), G2(preservation ≥+10pp), G3(action_loss ratio ≤1.10), G4(LED median <1.0)
- **G3 定义(D019-D020)**: G3 分三层——G3a(bypass-ACIS, 纯权重损伤), G3b(soft/train模式), G3c(hard/eval模式)。G3-hard 是主门控，G3-soft 是诊断。
- **evaluate.py 已被修改**: action_loss 计算从 eval mode 改为 train mode（行352-356）。这意味着后续所有 eval 产出的 G3 是 G3-soft 而非 G3-hard。v7 的 G3=3.28x 是 hard，v7.2 final 的 G3=3.19x 是 soft，**不可直接比较**。v7.2 缺少 G3-hard 数据。

## 基础设施快照

- 服务器: westd-27271, AutoDL 实例
- 两张 GPU 均空闲（截至 handoff 时刻）
- Baseline checkpoint: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/baseline_v5/`（final action_loss=0.00408）
- v7 checkpoint: 同目录下 `imm_v7/`（G3=3.28x FAIL）
- v7.2 checkpoint: `imm_v7_2/`（G3-soft=3.19x FAIL, G3a=1.91x）
- eval 结果目录: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/`

## 当前状态

- **v7**: DONE (negative). G1/G2/G4 PASS, G3=3.28x FAIL.
- **v7.2** (lambda 0.1→0.2): DONE (negative). G3-soft=3.19x FAIL. 中间 checkpoint 也 FAIL (step10K G3=10.4x, step20K G3=8.1x).
- **根因已定位(D021)**: margin_loss 梯度通过 ACIS→backbone LoRA 反传，造成三层损伤：
  - G3a=1.91x (bypass-ACIS 后纯权重损伤，不经过 ACIS 推理)
  - G3b 额外 ~1.67x (soft selection overhead)
  - G3c 额外 ~1.9x (hard selection overhead，train/eval 差异)
- **v8 方案(D022-D023)**: 双轨梯度隔离
  - v8a: stop-gradient（.detach() 切断梯度反传），最小代码改动
  - v8b: two-stage（冻结 baseline_v5 权重，只训练 ACIS），G3a 保证 1.0x
- **Registry**: `mvp_imm_anchor_v8` 状态 PREPARING

## 待办（条件触发）

1. **v8 代码部署时**:
   - `ssh_read_only` 检查 ACIS 模块是否有 `.detach()` 调用（v8a）或权重冻结逻辑（v8b）
   - 确认 dry-run 已执行（D006 要求 train+eval 模式各跑几步验证无 NaN/梯度异常）
   - 核实 CUDA_VISIBLE_DEVICES 分配（v8a→cuda:0, v8b→cuda:1）

2. **v8 训练启动后**:
   - `nvidia-smi` 核实 GPU 进程分配，无越界
   - 早期 eval（~step 2K）重点看 G3a 是否降至 ~1.0x（v8a 的核心验证点）
   - 监控 training loss 收敛（margin_loss + action_loss 曲线）

3. **v8 final eval 时**:
   - 完整 gate 分析（G1-G4 全维度）
   - **特别注意 evaluate.py 版本**——确认 G3 用的是 hard 还是 soft 模式，与历史数据对比时标注模式差异
   - 交叉验证 registry conclusion vs 实际 eval JSON 数据

4. **持续关注**:
   - evaluate.py 的 train/eval mode 切换问题尚未彻底解决。理想方案是同时报告 G3-hard 和 G3-soft。如果 Agent 只报一个，追问另一个。
   - Baseline preservation 实际值 ~33.5%（非理论 50%），G2 计算基线以此为准。

## 战略上下文

这是 IMM 方法的**最后一个关键变量**。v7/v7.2 证明了 ACIS 能学到有意义的 importance score（G1=55-64x, G2=+44-47pp），但 margin_loss 梯度反传损伤 backbone 导致 G3 持续 FAIL。v8 的梯度隔离是解决 G3 的直接对策：

- 如果 v8a/v8b G3 通过 → IMM 方法验证成功，可进入论文写作
- 如果 v8a/v8b G3 仍 FAIL → gradient sharing 不是唯一问题，需要重新审视 ACIS 架构本身

**论文 story 核心**: 即使 G3 最终失败，pruning fragility 分析（baseline 4.4x→29.2x 恶化 vs IMM 近恒定）本身是有价值的发现。但这不足以支撑 A 类投稿。

**AI 偏差风险**: Agent 此前有过将 training loss 外推为 eval 预期的乐观倾向（D016/D017 事件）。v8 审查时警惕类似模式——不接受"training loss 低所以 G3 会过"的论证，必须看 eval 数据。


---
