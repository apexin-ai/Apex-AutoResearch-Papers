# director / loop_10.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`210720a079a6036ebeaf.json`](../../sessions/21/210720a079a6036ebeaf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-21T20:50:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41074 (4×H800), westd-38929 (4×H800), westd-27271 (2×GPU), cqa1-33015 (4×GPU)。不得使用白名单外 GPU。
- AutoDL 服务器必须 `source /etc/network_turbo` 或 `HF_HUB_OFFLINE=1`，否则 HF tokenizer 下载失败（刚因此丢了 3 个实验 6h）
- `eval_pi05_pruning_libero.py` line ~82 的 `os.environ["CUDA_VISIBLE_DEVICES"]` 覆盖已删除（M062），部署后必须 `nvidia-smi` 验证进程在目标 GPU 上
- π0.5 random k=0.9 = 10.8% 是**真实数据**，不是 bug（D150）。Registry suspect 标记已清除。不要再派人调试这个。
- SmolVLA seed43 四实验是 cron 误报（M061），registry 已改为 DONE/success。不要重跑。
- 论文 57.2% vs 59.2% SmolVLA baseline 不是错误——两个 eval protocol，附录已解释

### 2. 🖥️ 基础设施快照
- **westd-41074**: GPU0: k=0.95 v2 (PID 627788), GPU1: fixed-mask k=0.9 v2 (PID 629619), GPU2: VTC M96 ~71% (PID 68539), GPU3: VTC M64v6 ~22% (PID 59671)
- **westd-38929**: GPU0-3: π0.5 Spatial cross-suite (baseline DONE 97.2%, 其余 3 个 L2/random finishing)
- **westd-27271**: GPU0: OpenVLA L2norm k=0.9 (PID 306599), GPU1: VTC M32 ~73%
- **cqa1-33015**: GPU0-2: SmolVLA official sweep (all expected 0%), GPU3: 待轮转
- Paper: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`，8 pages main text，CoRL 2026 template，编译通过
- Round 5 审稿已提交 (apr_20260521T175329_325c)，等用户在飞书审批卡片确认

### 3. 📊 当前状态
刚处理完 Reviewer #54 报告：fixed-mask 否定时间不一致性假说（D150），k=0.95≈80% 中间结果确认 cliff。正在等：
- **fixed-mask k=0.9 full 500ep** (~2-3h)：目前 T0=12% T1=26% T2=3%，方向明确（temporal inconsistency 被否定）
- **k=0.95 full 500ep** (~1.5h)：目前 ~80% (200ep)，确认 k=0.95→k=0.9 ~70pp cliff
- **Spatial L2norm k=0.5 和 k=0.3** (~10min)：接近完成
- VTC M96/M32 训练完成 (~13h) → 需要部署 eval
- Agent + Reviewer 都刚 RESET，新 session 需要 onboard

### 4. 📋 待办
- fixed-mask 500ep 完成 → 写入论文作为 negative diagnostic（"temporal consistency is NOT the mechanism"）
- k=0.95 完成 → 与 k=0.9=10.8% 形成 sharp cliff 数据，写入 §4.4 π0.5 section
- Spatial 完成 → 更新 paper_framing，派 Paper Agent 写入 appendix cross-suite table
- VTC M96/M32 训练完成 (cron 回调) → 立即在训练 GPU 上部署 eval（LIBERO-Object 500ep）
- k=0.85 待部署 → westd-41074 GPU0 或 GPU1 空出后立即跑（填 k=0.7→k=0.9 random curve gap）
- Round 5 审稿报告回来 → 按 review-report-action skill 处理（先 Holistic Pass 再逐条 Action Matrix）
- 全部新数据就绪后 → 派 Paper Agent patch 新发现进论文 → 重新提交审稿
- 最终提交前 → 跑 reference-audit skill 验证引用真实性

### 5. 🎯 战略上下文
- **CoRL 2026**: Abstract DDL May 26 (4 days), Paper DDL May 29 (7 days)
- **核心 story**: Vision connector 决定 VLA token compressibility 的四类谱系（CV 0.038→0.314）。Analysis + Method paper。
- **最重要的新发现** (D149→D150): π0.5 random k=0.95→k=0.9 存在 ~70pp cliff，fixed-mask 否定了 temporal inconsistency，真正原因是 critical token sensitivity + 未解释的非单调恢复 (k=0.7=75.5%)。这强化了 "uniformly critical ≠ pruning safe" 的 story。
- **易判断错的事**: (1) π0.5 random k=0.9=10.8% 看起来像 bug 但不是——已双种子+代码审计+fixed-mask 三重验证 (2) SmolVLA cron on_failed 是误报——结果在磁盘上 (3) paper 的 57.2% vs 59.2% 是两个 eval protocol 不是 typo
- **决策链**: D139(uniformly critical) → D147(SmolVLA official cliff) → D148(full sweep 0%) → D149(k=0.9 real, deploy fixed-mask) → D150(fixed-mask negates temporal inconsistency, cliff confirmed)
- **VTC 是论文第三个 contribution**: M96/M32 新训完的模型还没 eval，这是 DDL 前最后一批实验


---
