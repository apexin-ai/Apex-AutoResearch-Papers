# agent / loop_17.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`88eef92a96e9cffc2bea.json`](../../sessions/88/88eef92a96e9cffc2bea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: session_continuation
updated: '2026-05-28T09:00:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 14 张：westd-27271 cuda:0/1, cqa1-33015 cuda:0/1/2/3, westd-41074 cuda:0/1/2/3, westd-38929 cuda:0/1/2/3
- cqa1-33015 磁盘 /autodl-pub 已用 ~91%，无法降至 80%（其他租户占用），本项目仅 ~104G
- π0.5 实验必须用 strict 评估模式（lenient 数据不入论文，D265 教训）
- 实验硬截止 May 28 20:00 BJT (12:00 UTC)，CoRL 2026 Paper May 29 提交
- cqa1 上 transformers 需 >=4.45（旧版缺 qwen2_5_vl 模块会崩溃）
- **新规**：所有部署前必须 `nvidia-smi --query-compute-apps=pid --format=csv,noheader -i {GPU_INDEX}` 确认 GPU 干净

### 2. 🖥️ 基础设施快照
- **westd-27271**: 工作目录 /root/autodl-tmp/importance_margin_vla_compress, 磁盘充裕(819G/879G)
- **cqa1-33015**: 同上路径, 磁盘紧张(/autodl-pub 91%)
- **westd-41074**: 同上路径, 磁盘充裕(812G/879G)
- **westd-38929**: 同上路径, 磁盘 593G/879G(29%用)
- 所有服务器用 aml-train 镜像: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 日志目录: ~/runs/importance_margin_vla_compress/

### 3. 📊 当前状态（09:00 UTC）

**4-seed 覆盖**: 18/18 ALL COMPLETE ✅

**s46 (5th seed) 进度**: 4/18 done, 13/18 running, 1/18 abandoned (l2norm k=0.7)

**s46 已完成**:
- L2norm k=0.9 = 80.6% | L2norm k=0.75 = 73.2%
- Random k=0.85 = 44.8% | Attn k=0.85 = 50.4%

**15 实验 RUNNING（全部有 cron 监控, 共 15 crons）**:

| # | exp_id | 服务器 | GPU | PID | 启动时间(UTC) | 预计完成 |
|---|--------|--------|-----|-----|---------------|---------|
| 1 | OV_random_k095_goal_v4 | cqa1 | cuda:2 | 147681 | 05:47 | ~12:30+ (OV) |
| 2 | OV_l2norm_k095_s43_w27 | w27 | cuda:0 | 545112 | 05:57 | ~12:30+ (OV) |
| 3 | random_k07_s46_w41 | w41 | cuda:1 | 744875 | 06:37 | ~09:30-10:00 |
| 4 | attn_k09_s46_cqa1 | cqa1 | cuda:1 | 163026 | 06:25 | ~09:00-09:30 |
| 5 | attn_k07_s46_cqa1 | cqa1 | cuda:3 | 163384 | 06:26 | ~09:00-09:30 |
| 6 | random_k09_s46_w38 | w38 | cuda:1 | 253682 | 06:27 | ~09:30-10:00 ⚠️共享 |
| 7 | l2norm_k05_s46_cqa1 | cqa1 | cuda:0 | 168016 | 06:33 | ~09:00-09:30 |
| 8 | attn_k05_s46_w38 | w38 | cuda:1 | 261876 | 06:34 | ~09:30-10:00 ⚠️共享 |
| 9 | random_k075_s46_w38 | w38 | cuda:0 | 363188 | ~07:30 | ~10:00-10:30 |
| 10 | attn_k075_s46_w38 | w38 | cuda:2 | 363743 | ~07:30 | ~10:00-10:30 |
| 11 | l2norm_k085_s46_w41 | w41 | cuda:3 | 859388 | 08:30 | ~11:00-11:30 |
| 12 | l2norm_k095_s46_w27 | w27 | cuda:1 | 616102 | 08:55 | ~11:25-11:55 |
| 13 | random_k095_s46_w41 | w41 | cuda:0 | 898746 | 08:55 | ~11:25-11:55 |
| 14 | random_k05_s46_w41 | w41 | cuda:2 | 899098 | 08:55 | ~11:25-11:55 |
| 15 | attn_k095_s46_w38 | w38 | cuda:3 | 457257 | 08:55 | ~11:25-11:55 |

**GPU 分布**:
| Server | cuda:0 | cuda:1 | cuda:2 | cuda:3 |
|--------|--------|--------|--------|--------|
| w27 | OV l2norm s43 | L2norm k0.95 s46 | — | — |
| w38 | Random k0.75 s46 | Random k0.9 s46 + Attn k0.5 s46 ⚠️ | Attn k0.75 s46 | Attn k0.95 s46 |
| w41 | Random k0.95 s46 | Random k0.7 s46 | Random k0.5 s46 | L2norm k0.85 s46 |
| cqa1 | L2norm k0.5 s46 | Attn k0.9 s46 | OV Goal v4 | Attn k0.7 s46 |

**14/14 GPU 全满**

### 4. 📋 待办（条件触发式）
- cqa1 实验（attn_k09, attn_k07, l2norm_k05）预计最先完成 ~09:00-09:30 → harvest + 部署 attn_k075/random_k075 等剩余 s46
- w38:cuda:1 共享两实验，预计稍慢 ~09:30-10:00
- 11:00 UTC 前：交付最终 consolidation table（含所有可用 s46 数据）
- 2 个 OV 实验可能超过 12:00 UTC 截止

### 5. 🎯 战略上下文
**核心结论链（4-seed confirmed）**:
- peak margin at k=0.9: L2norm 80.4% vs Random 33.6% = ~46.8pp gap
- crossover at k≈0.7: L2norm 63.5% ≈ Random 64.4%
- Attn cliff: k=0.95(77.8%) → k=0.85(51.0%) → plateau ~50-53% for k≤0.75
- s46 实验收窄 error bar，加固以上三个 claim

**s46 early signals（与 4-seed mean 对比）**:
- L2norm k=0.9 s46=80.6% vs 4-seed mean=80.4% → 一致 ✅
- L2norm k=0.75 s46=73.2% vs 4-seed mean=70.0% → 偏高但在 transition zone 高方差范围内
- Random k=0.85 s46=44.8% vs 4-seed mean=44.9% → 几乎完全一致 ✅
- Attn k=0.85 s46=50.4% vs 4-seed mean=51.0% → 一致 ✅


---
