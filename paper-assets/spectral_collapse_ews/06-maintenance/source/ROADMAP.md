# spectral_collapse_ews — Research Dashboard

> 最后更新: 2026-05-25 21:49 UTC | 更新原因: Round 4 review 3.0 → 三线并行修复计划 (D040)

## 核心方向
递归合成训练中嵌入空间的谱坍缩三阶段模式（decompression → onset → acceleration），SLV 作为计算廉价的坍缩监测器，以及临界混合比 r_crit ∈ (0.25, 0.3] 的相图刻画。GPT-2-medium 跨架构验证证明发现的通用性。详见 paper_framing.md。

## 当前进展
- **阶段**: Research 完成 → 审稿迭代中（Round 4 得分 3.0，目标 3.5+）
- **Round 4 识别 3 个系统性问题**: 统计严谨性 / 实验规模 / Framing 错配
- **三线并行修复已启动** (D040):
  - Agent: bootstrap CIs + 计算分析 + GPT-2-medium r=0 多seed全10代
  - Paper Agent: framing 重定位（标题/narrative/controller claim/MP bias/记号统一）
- **实验**: 28 total（20 success），0 RUNNING → 2 即将启动
- **审稿修复**: Round 1-3: 27/27 addressed | Round 4: 10 issues open, action dispatched
- **论文**: 编译 PASS，11页（正文≤8页），format aligned

## 近期任务
- [ ] Agent: 验证 GPT-2-medium 参数量和训练代数 (1.5)
- [ ] Agent: Bootstrap CIs on all SLV trajectories (1.1)
- [ ] Agent: Table 3 mixed-ratio comparison at r=0.2 (1.2)
- [ ] Agent: r_crit(T) 敏感性分析 T=5,7,10 (1.3)
- [ ] Agent: 奇异值分布可视化 Gen 0 vs Gen 2 (1.4)
- [ ] Agent: GPT-2-medium r=0 seed43 + seed44 全10代 (2.1, 2.2)
- [ ] Paper Agent: Framing 修复（标题/narrative/controller/MP bias/记号/Table 1/refs）
- [ ] 提交 Round 5 审稿（修复完成后）

## GPU 预算
rtx6000-diagprobe: 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB each)
- cuda:0: → GPT-2-medium r=0 seed43（待启动）
- cuda:1: → GPT-2-medium r=0 seed44（待启动）
- 累计 ~300 GPU-hours

## Round 4 审稿回溯·系统性问题

### SYSTEMIC #1: Statistical rigor (MF-1, SF-4, SF-5, R1-W1)
r_crit 缺 bootstrap CI、记号不一致、T-依赖性未分析。
→ Agent 做 bootstrap CIs + r_crit(T) 分析; Paper Agent 统一记号

### SYSTEMIC #2: Experimental scope (MF-2, SF-1, R4-m1, R4-m2)
跨架构单 seed 3-gen 不够、Table 3 只 r=0、参数量存疑。
→ Agent 做 GPT-2-medium 多 seed 10-gen + Table 3 mixed-ratio; Paper Agent 修 Table 1

### SYSTEMIC #3: Framing mismatch (MF-3, R4-W1, R4-W3)
EWS 标题暗示实时监测、controller claim 过宽、decompression 机制未解释。
→ Paper Agent 全面 reframe; Agent 提供 SV 分布数据支持

## 跨架构验证矩阵 (GPT-2-medium) — 扩展中
| r | 实验 | 状态 | Seeds |
|---|------|------|-------|
| 0 | exp_020 + new seed43/44 | ✅+🔄 | 1→3 |
| 0.25 | exp_023 | ✅ | 1 |
| 0.30 | exp_022c | ✅ | 1 |
| 1.0 | exp_021 | ✅ | 1 |

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D040 | 2026-05-25 | Round 4 fresh review 3.0: 启动三线并行修复——bootstrap CI + | exp_020, exp_022c |
| D039 | 2026-05-24 | exp_020 确认：GPT-2-medium 三阶段谱坍缩模式完全复现（SLV 峰值 Gen 2  | exp_020, exp_023, exp_022c |
| D038 | 2026-05-23 | GPT-2-medium cross-architecture validation (exp_02 | exp_020, exp_018 |
| D037 | 2026-05-23 | exp_017 完成：保持 Table 3 r=0.2 为 single seed (seed42) | exp_017, exp_007 |
| D036 | 2026-05-21 | P2 种子实验 (r=0.2/44, r=0.5/44) 降为 best-effort/camera | exp_013, exp_014 |
| D035 | 2026-05-20 | exp_012 完成后 cuda:0 启动 r=0.25 seed43（堵 cross-seed m | exp_009, exp_012 |
| D034 | 2026-05-20 | r_crit non-decreasing condition 改为基于 cross-seed me | exp_012, exp_008 |
| D033 | 2026-05-20 | 2.43× acceleration claim 改用绝对速率 1.67±0.18%/gen（Rev | exp_001, exp_010 |
| D032 | 2026-05-20 | cuda:0 接力改为 r=0.3 seed43（撤回 r=0.15 方案） | exp_008, exp_010 |
| D031 | 2026-05-19 | 撤回 D030：r_crit bound 维持 (0.25, 0.3]，r=0.25 仍为 Type | exp_009 |


