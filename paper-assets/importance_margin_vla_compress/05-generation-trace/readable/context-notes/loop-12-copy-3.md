# reviewer / loop_12.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`15f060cd5a3c3b06d2a2.json`](../../sessions/15/15f060cd5a3c3b06d2a2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-22T18:19:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- **`--gpu` flag 是假的**：`eval_pi05_pruning_libero.py` line 151 `DEVICE = "cuda:0"` 硬编码，`args.gpu` 只用于日志。所有 π0.5 eval 部署必须用 `CUDA_VISIBLE_DEVICES=N` 环境变量，不能靠 `--gpu`
- **`n_episodes` 是 per-task**：传 500 会 IndexError（每个 task 只有 50 个 init_states）。正确用法 `--n_episodes 50`（50 × 10 tasks = 500 total）
- **SmolVLA Object baseline = 59.2%（seed42）/ 59.6%（seed43）**，不是 44.8%。paper_framing.md 仍有 ~10 处残留旧数字，Agent 需 systematic fix
- **Attention pruning actual keep ratio ≠ configured k**：k=0.95 configured → actual keep = 690/768 = 89.8%。Paper 必须用 actual keep ratio 比较，不用 configured k
- **nvidia-smi GPU util% 不可信**：LIBERO eval 是 CPU-heavy simulation，GPU util 经常 0-1%。判断 GPU 是否在用看 VRAM 占用（>2GB = 有模型加载），不看 util%

### 2. 🖥️ 基础设施快照
- **westd-38929** (4×GPU): `/root/autodl-tmp/importance_margin_vla_compress`
  - cuda:0: π0.5 L2norm k=0.85 Long s42 | cuda:1: π0.5 L2norm k=0.7 Long s42 (刚部署) | cuda:2: SmolVLA Random k=0.95 Long s42 | cuda:3: π0.5 Random k=0.95 Long s42
- **westd-27271** (2×GPU used): `/root/autodl-tmp/importance_margin_vla_compress`
  - cuda:0: X-VLA Goal L2 k=0.7 | cuda:1: X-VLA Random chain (12 exps queued in tmux `xvla_spatial`)
- **westd-41074** (4×GPU): `/root/autodl-tmp/importance_margin_vla_compress`
  - cuda:0: π0.5 L2norm k=0.3 Goal s42 | cuda:1: Long L2 k=0.9 | cuda:2: Attention k=0.9 chain | cuda:3: OpenVLA VTC M64 training (v6, **关键路径**, ETA 5/23 16:30)
- **cqa1-33015** (4×GPU): `/root/autodl-tmp/importance_margin_vla_compress`
  - cuda:0: OpenVLA baseline Spatial (已跑 ~45h) | cuda:1: π0.5 Random k=0.7 Goal s42 | cuda:2: π0.5 Random k=0.5 Goal s42 | cuda:3: π0.5 L2norm k=0.95 Long s42 (链式: → k=0.9 → k=0.85)

### 3. 📊 当前状态
**刚完成**：Director 触发的深度分析（5 问题全部回答），发现并上报 SmolVLA baseline 错误（44.8%→59.2%），导致 Claim 4 VTR 叙事重构（D172: "+15pp boost" → "near-lossless recovery"），审查了 paper_framing.md 并标注 10 处需更正位置。ROADMAP D171（2-axis）+ D172（Claim 4 reframe）审查通过。Abstract v1 已起草。

**RUNNING 实验**：约 29 个，主力是 π0.5 Goal/Long 各 keep ratio × L2norm/Random。X-VLA Goal/Spatial k=0.95 仍在跑。OpenVLA VTC M64 训练中。

**等待**：无 pending worker 回调。GPU 14/14 满载。

### 4. 📋 待办（条件触发式）
- **π0.5 Goal/Long 实验完成** → 核实 SR 数据 vs registry，检查 cross-suite degradation pattern 是否符合 2-axis 预测（Goal/Long 应比 Object 退化更多但可控）
- **X-VLA Goal/Spatial k=0.95 完成** → 核实是否 catastrophic（预期 Goal catastrophic, Spatial moderate）。如果 Spatial 也 catastrophic → 强化 Claim 5
- **OpenVLA VTC M64 训练完成（ETA 5/23 16:30）** → 这是 Claim 4 最终定级的关键。SR>0% → Claim 4 stays; SR=0% → Claim 4 降级为 supplementary finding，建议 paper 转 pure analysis
- **SmolVLA Long baseline 完成** → 核实 SmolVLA cross-suite baseline pattern（Object 59.2%, Spatial 44.6%, Goal 60.8%, Long ?）
- **Abstract 审查请求** → 加载 `paper-quality-lessons` skill，按模式 B 审查
- **paper_framing.md 44.8% 残留修复完成** → 复查确认 10 处全部更正，特别是 RC4 response 和 Claim 4 统计论证

### 5. 🎯 战略上下文
**项目核心**：VLA vision token pruning robustness 由 connector architecture × task complexity 决定（D171 2-axis framework）。5 models, 4 LIBERO suites, CoRL 2026 投稿。

**决策链**：D162(drop π0) → D166(expand 4 suites) → D168(OpenVLA Object-only) → D169(X-VLA cross-suite catastrophic) → D171(4-class→2-axis) → D172(VTR reframe: recovery not boost)

**最容易判断错的事**：
1. **SmolVLA baseline**：paper_framing 里 44.8% 和 59.2% 共存，Agent 可能引用错的。Reviewer 已验证 59.2% (seed42, westd-27271) 是正确值
2. **VTR 叙事**：旧叙事 "+15pp re-encoding boost" 已被推翻。任何暗示 VTR "超越 baseline" 的说法都是错的。正确说法是 "recovers to baseline from 0%"
3. **Attention k vs actual keep**：configured k=0.95 看起来很保守，但 actual keep=89.8%。和 L2norm k=0.9 (actual=90%) 对比时几乎相同——scoring method 是次要的，compression ratio 才是决定因素
4. **GPU 占用判断**：不要用 nvidia-smi util%，用 VRAM。LIBERO eval GPU util 常为 0% 但进程活跃
5. **Claims 强度排序**：1(2-axis) ✅ > 5(cross-suite) ✅ > 2(pixel-shuffle) ✅ > 3(CV scaling) ✅ > 4(VTR) ⚠️。Claim 4 是最薄弱环节，M64 结果决定其命运


---
