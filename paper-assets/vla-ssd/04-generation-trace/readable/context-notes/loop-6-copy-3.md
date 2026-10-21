# reviewer / loop_6.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`c7366bffc54e9bd74643.json`](../../sessions/c7/c7366bffc54e9bd74643.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-16T10:17:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-19183 的 GPU 白名单未在 constraints 中明确指定，但实验均使用 cuda:0 和 cuda:1（双卡实例）
- 论文数据必须溯源到 registry 中的 exp_id，不可凭记忆引用数字
- untrained 模型是"random LLM + preserved SigLIP"（projector 冻结），不是完全随机初始化——审查时注意 L0 trained=untrained 是正确的
- paper_provenance.yaml 已重建（非 stale），claims C001-C003 有 tier1 evidence。但 ablation 结果（P0-P4）尚未注册

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，代码 `/root/vla-ssd/`，数据 `/root/autodl-tmp/vla-ssd/`
- Python：conda base `/root/miniconda3/bin/python`
- 模型：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b` (trained) + `openvla-7b-untrained`
- 数据：`/root/autodl-tmp/vla-ssd/data/libero/libero_goal/` + `libero_spatial/`
- Features：`/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_{goal,spatial}/`
- 结果：`/root/autodl-tmp/vla-ssd/results/` (rsa/, functional_validation/, ablations/, figures/)
- Ablation 脚本：`/root/vla-ssd/scripts/ablations/`
- 活跃进程：无（双卡空闲）
- W&B：本项目未配置

### 3. 📊 当前状态
刚完成 P0-P4 全部 ablation 审查：
- **P0 cosine metric**: PASS，inverted-U 完美复现 (r>0.989 profile correlation)
- **P1 seed robustness**: PASS，peak R²=0.655±0.002 稳健，peak layer=10.6±2.7（平台 L8-L16）
- **P3 per-DOF**: PASS，inverted-U 在 xyz/rpy/gripper 全复现
- **P4 permutation**: PASS，所有层 p<0.001

已发给 Director 的 warnings（未修复）：
1. experiments.tex L139 + discussion.tex L14："untrained image_mean drops to near-zero at L10-L13" — 实际 L10=-0.33/L11=-0.28（负数非 near-zero），L12=0.52/L13=0.44（正数）。应缩窄为 L10-L11
2. discussion.tex L11："R² peak (L8) precedes RSA peak (L12) by four layers" — seed ablation显示 peak 在 L9-L16 浮动（mean=10.6），offset 不稳健。建议弱化

Registry: 所有实验 DONE，无 RUNNING/PREPARING（plan010_action_probe_spatial 和 plan010_rsa_spatial 仍 PREPARING 但实际结果已在 plan_010_libero_spatial 条目中）。P0-P4 ablation 结果在服务器但未注册。

论文状态：Round 3 scored 8/10，无 new criticals，接近收敛。

### 4. 📋 待办
- Paper Agent 提交 Round 4（含 ablation appendix + 上述 warning 修复）→ 按 §5 模板评分
- Director 要求审查 ablation 注册条目 → 核对数字与 JSON 一致
- P2 demo sensitivity ablation 如启动 → 审查脚本正确性（50→25→10 demos 递减）
- 论文终稿提交前 → 全文数字 vs registry 最终交叉验证
- fig1 architecture diagram 如加入 → 检查 8-page 限制是否溢出

### 5. 🎯 战略上下文
- **核心结论链**: D041(Method B RSA) → D042(framing rewrite) → D043(C3 narrative: "modest gain, redistribution dominates")
- **三个 Core Claims 全部有双 benchmark 支撑**: C1 vision dominance, C2 inverted-U, C3 redistribution > creation
- **最容易判错的事**:
  1. 不要因为 plan_011 报告 "peak L8" 就认为 P1 结果 (peak L9-L10) 是 inconsistency — 两者差异在 seed noise 范围内，profile 是平台不是尖峰
  2. untrained_image_mean 的 per-layer profile 不是单调递减 — L10-L11 有个负数 dip 然后 L12+ 恢复到正值，论文的 "near-zero at L10-L13" 措辞有误
  3. per_dof "full" RSA (~0.18) 远低于主分析 full RSA (~0.63) 是方法差异不是 bug（per-DOF 用单维 action distance）
  4. CoRL DDL: abstract 2026-05-26, paper 2026-05-29。剩余 ~4 GPU·h 但双卡空闲，P1 已用完最大的 ablation 预算


---
