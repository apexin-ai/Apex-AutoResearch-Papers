# agent / loop_18.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`47ead1ff1911652ffb71.json`](../../sessions/47/47ead1ff1911652ffb71.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-24T00:23:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5（6张），westd-19828 cuda:0-1（2张），共 8 张。超出必须 push back Director
- 精度：≤3B 模型强制 fp32（D079），>3B 用 bf16
- 1.4B 措辞约束：只能说 "consistent across"，不能说 "scale-invariant"（D189）
- γ-comparison 已废弃（D192），shape comparison 是唯一路线
- P_max 6/8 = mauve pair 结构，非信号饱和（D194）
- D102 分析参数：downstream=mauve, threshold=true_3sigma_d105, n_perm=5000

### 2. 🖥️ 基础设施快照
- **westd-17855**（6× RTX PRO 6000 Blackwell 98GB）
  - 工作目录：`/root/autodl-tmp/distrib_canary_collapse/`
  - Python：`/root/miniconda3/bin/python`，conda base
  - HF_HOME：`/root/autodl-tmp/.hf_cache`，TRANSFORMERS_OFFLINE=1
- **westd-19828**（2× RTX PRO 6000 Blackwell 98GB）
  - 同上路径和环境配置
- 模型：`/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`（两台服务器都有）
- 数据：`data/wikitext103_5k`（相对项目目录）
- 活跃进程（reconcile 确认）：
  - scale_14b_t15_a075_s42_fp32: PID 793171, westd-19828:cuda:0
  - scale_14b_t15_a060_s42_fp32_v2: PID 679656, westd-17855:cuda:0
  - scale_14b_t15_a050_s42_fp32_v3: PID 680095, westd-17855:cuda:1
  - scale_14b_t15_a045_s42_fp32: PID 680608, westd-17855:cuda:5
  - scale_14b_t10_a075_s43_fp32: PID 719178, westd-17855:cuda:2
  - scale_14b_t10_a060_s43_fp32: PID 719252, westd-17855:cuda:3
- **westd-19828:cuda:1 空闲**（scale_14b_t10_a050_s43_fp32 失败后释放）
- **westd-17855:cuda:4 状态不明**：report 列 scale_14b_t10_a045_s42_fp32 (PID 679204) 但 reconcile 未出现该 cron，需要下一轮确认

### 3. 📊 当前状态
我刚处理 scale_14b_t10_a050_s43_fp32 的失败回调。日志仅 6 行（模型加载成功→Generation 0→无声死亡，无 Traceback）。已派诊断 Worker `worker_diagnose_scale_14b_t10_a050_s43_fp32_20260522T202840` SSH 到 westd-19828 查 dmesg OOM / GPU 状态 / tmux 环境，**尚未回调**。

Registry 状态：
- RUNNING 6-7 个实验（全部 1.4B scale verification）
- PREPARING 5 个（14b_t10_a060_s43、14b_t10_a075_s43、14b_t10_a050_s43、t15_a050_s42_fp32、qwen35_dryrun_launch）
- 已完成 184 个（success 127, negative 4, failed 23, killed 30）

**未汇报 Director**——诊断 Worker 未回调，等结果后一并汇报。

### 4. 📋 待办（条件触发式）
- Worker `worker_diagnose_scale_14b_t10_a050_s43_fp32_20260522T202840` 回调 → 根据 root_cause 决定：(a) 可修复则重提交到 westd-19828:cuda:1；(b) 不可修复则汇报 Director
- 任何 T=15 cell 完成（cron 回调）→ D102 分析 + 更新 registry + 汇报 Director
- T=10 a075_s43 / a060_s43 完成 → D102 分析，与 s42 cross-seed 对比
- **westd-19828:cuda:1 空闲 → 失败诊断修复后立即重提交**，GPU 空着是失职
- westd-17855:cuda:4 状态 → 需确认 scale_14b_t10_a045_s42_fp32 是否还活着（cron 里没看到）
- 所有 8 cells 完成 → 综合 D102 分析 → 写 1.4B Discussion 段落 → 汇报 Director

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR June（DDL ~2026-06-15，距今 24 天），目标 3.5 (Borderline Conference)
- **核心叙事**：α×T 2D 相图 + binary detection pattern + metric structure + 检测下界理论。从"方法论文"转为"现象发现论文"（D192）
- **1.4B 是 additive evidence**，不是 core claim。410M 20/20 相图已完成 ✅，1.4B 8 cells 用于支撑 "consistent across scales" 措辞
- **1.4B T=10 已知结果**：a050 s42 → PermG 4/8（弱于 410M 的 6/8），a060 s42 → PermG 4/8（sync-dip 在 1.4B 消失！），a075 s42 → PermG 5/8。整体趋势：1.4B 压平了相图，检测灵敏度降低但机制有效
- **易错点**：
  - 不要混淆 s42 和 s43 结果——1.4B seed variance 很大（α=1.0 时 s42=2/8 vs s43=6/8）
  - scale_14b_t10_a050_s43_fp32 的 spec command 缺少 conda 环境包装（`bash -c "source conda..."`），这可能是失败根因——成功的实验都有完整包装
  - westd-19828 上之前同 cell 的 s42 实验 (`scale_14b_t10_a050_s42_fp32_19828`) 因 `TypeError: NoneType.__format__`（metrics['effective_rank']=None）失败过，后在代码修复后以 v2 重跑成功。当前 s43 的失败模式不同（无声死亡），但可能相关
  - Reviewer #90 场景预评估：A(30%) positive / B(55%) mixed / C(15%) weak。t10_a075 ≥6/8 排除 C；t10_a050 测试 onset boundary


---
