# reviewer / loop_20.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`de4bf09dcd0e689617df.json`](../../sessions/de/de4bf09dcd0e689617df.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-21T17:32:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593=cuda:0; bjb1-18228=cuda:0-3; bjb1-32546=cuda:0-5; bjb2-28827=cuda:0-5
- evaluate.py L576 已修复（随机 nn.Linear → ValueError 检查），三台服务器已同步。**不要回退这个修复**
- merge 必须用 `scripts/merge_precompute_cache.py`（greedy_cover 去重），**绝对不要用 `train_crm.py --auto`**（原 `_try_merge()` 无法处理混合粒度 partial 文件）
- π0.5 eval 必须传 `--obs_dim 2048`（默认 960 会报错）
- SmolVLA 所有 LOCKED 结果不可更改：Object Plan A 18.3%±2.1%, Spatial Plan A 35.0%±1.0%
- π0.5 baseline LOCKED：Object 81.5%±0.5% (seeds 42/43/44), Spatial 84.2%±1.0% (seeds 42/43/45)

### 2. 🖥️ 基础设施快照
- **bjb1-32546** (6×4090): `/root/acr-vla-conformal-refinement`, conda base `/root/miniconda3`
  - 当前：9 个 Object precompute 进程 (s1-s9)，GPUs 0/2/3 双载
- **bjb2-28827** (6×4090): 同上路径，6 个 Spatial precompute 进程 (s0-s5)
- **bjb1-18228** (4×4090): 同上路径，1 个 Spatial precompute 进程 (s6, cuda:3)，**GPU 0/1/2 空闲**
  - merge 脚本在此：`/root/acr-vla-conformal-refinement/scripts/merge_precompute_cache.py`
  - object/ cache 为空（需 rsync 汇聚），spatial/ 只有本地 s6 的 14 个 partial
- **bjb2-40593** (1×4090D): 1 个 Object precompute (s0), `--benchmark object spatial`（spatial 部分冗余，bjb2-28827 已覆盖）
- Cache: `/root/autodl-tmp/crm_cache_pi05/{object,spatial}/`
- 模型: `/root/autodl-tmp/models/pi05_libero_finetuned/`
- pipeline-auto (PID 790737) **已死**，无自动 merge 风险，也无自动触发机制

### 3. 📊 当前状态
刚完成本轮监控。17/17 precompute shard 全部运行中，无死进程。

**Object precompute (10 shards)**:
- bjb1-32546 s2/s5/s6/s7/s8/s9: 81-87%, ~30-43min
- bjb1-32546 s1/s3/s4: 70-79%, ~50-77min
- bjb2-40593 s0: 74%, ~104min（最慢，batch_size=1）

**Spatial precompute (7 shards)**:
- bjb1-18228 s6: 81%, ~50min
- bjb2-28827 s0-s5: 66-69%, ~100-114min（**全局瓶颈**）

**已发送给 Director 的 CRITICAL**:
1. 论文 Appendix Table 3 Spatial Plan A fast-path=84% → 应为 2.4%（copy-paste 错误）
2. Conclusion "larger VLAs are untested" 与 Appendix H π0.5 数据矛盾
3. Object cache s5/s6 混合粒度已清理完成

Registry 显示 0 RUNNING（进程是 nohup 直启，未通过 submit_training_job 注册）。

### 4. 📋 待办（条件触发式）
- **Object precompute 全部完成** → rsync s0 (bjb2-40593→bjb1-18228) + s1-s9 (bjb1-32546→bjb1-18228) → dry-run merge → merge
- **Spatial precompute 全部完成** → rsync s0-s5 (bjb2-28827→bjb1-18228)，s6 已在本地 → dry-run merge → merge
- **两个 benchmark merge 完成** → `python src/train_crm.py --benchmark object spatial --cache_dir ... --obs_dim 2048 --epochs 50`（bjb1-18228 cuda:0）
- **CRM training 完成** → π0.5 Plan A eval: 3 seeds × 2 benchmarks，需传 `--obs_dim 2048 --mode acr_vla`
- **论文 P0 修复** → 验证 Table 3 fast-path 值和 Conclusion limitations 措辞是否已改

### 5. 🎯 战略上下文
- 目标：CoRL 2026 DDL May 29。π0.5 cross-VLA 验证是 Appendix H 的核心内容
- π0.5 baseline 已 LOCKED (81-85% SR)，ceiling effect 明显——CRM 改进空间有限（vs SmolVLA 10-30%）。如果 π0.5 Plan A 提升 <2pp，属于预期（论文已用 "headroom analysis" framing）
- **易错点 1**：bjb1-32546 上 s5/s6 cache 之前有混合粒度污染，已清理。但 bjb2-40593 s0 也有混合粒度（save_every=100 和 500 共存），merge 脚本能处理但 dry-run 验证必做
- **易错点 2**：跨服务器 rsync 前必须清空 bjb1-18228 的 `object/` 目录（有旧 partial 残留，Worker 已标记）
- **易错点 3**：bjb2-40593 配了 `--benchmark object spatial`，object 完成后会自动跑 spatial s0。但 bjb2-28827 已覆盖 spatial s0-s5，这个冗余 spatial 无害但会占 GPU ~8h。precompute 完成后如果需要该 GPU 做 eval，需 kill 掉


---
