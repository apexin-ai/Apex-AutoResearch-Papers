# reviewer / loop_11.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`c8b4535b7c50575ef2e3.json`](../../sessions/c8/c8b4535b7c50575ef2e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-17T07:39:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：gpu-6000pro-2 的 cuda:0 和 cuda:1（仅此两张）
- 论文源文件真源在 LOCAL `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`（已完成 remote→local 合并，后续只改 local）
- REMOTE `/root/autodl-tmp/recursive_gen_depth_est/paper/` 是历史残留，不再作为编辑目标
- mixed_depth_corpus_001 registry conclusion="success" 是 Agent 覆写——脚本实际输出 "PARTIALLY CONFIRMED"（max per-class Δ=2.43pp > 2pp）。论文必须用 macro-recall (-1.62pp) 作 claim 依据
- ensemble_reference_001 的 d1v2_auc=0.9989 是错误指标（实际计算 d0-vs-rest），论文不得引用

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/models/pythia-1.4b`
- 数据：`/root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl`（20K samples, 19 features）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：**无**（所有实验完成，GPU 空闲，Director 已批准释放 GPU）
- 编译 PDF：LOCAL `/home/ubuntu/.../docs/paper/main.pdf`（19 pages, 0 errors）

### 3. 📊 当前状态
刚完成投稿前最终评估（中稿率 55-65% Findings）。全部实验完成（87 total, 53 success, 9 negative）。论文 v8 final corrected 就绪。R8 审稿 5 个 fix 已应用并验证（McCullagh/CCNet bib, em-dash cleanup, "We find that", curation 措辞）。

Registry: 无 RUNNING 实验。second_seed_replication_001 status 字段可能仍标 RUNNING（metrics/conclusion 已填，但 status 未改 DONE）——cosmetic issue。

等待中：Director 决定是否释放 GPU + 发起 ARR 提交流程。

### 4. 📋 待办
- Director 批准提交 → 确保最终 PDF 是 LOCAL 编译版，核查 page count / anonymization
- 若 AC 要求 re-review → 重点关注 Attack A (scale limitation) 和 Attack C (practical utility)
- 若有新 worker 改论文 → 验证改动未回退 R5-R8 修复（此前已发生过 diverge 事故）
- mixed_depth appendix 如需写 defense → 用 "macro-recall Δ=-1.62pp; individual variations from held-out sample composition" 措辞

### 5. 🎯 战略上下文
- 项目核心结论：递归生成在文本中留下可量化的 perplexity tail fingerprint（p90_ppl + var_surprisal 主导），RF 可达 70-85% 四类准确率，EDD=4
- 决策链：D011 Plan A → D027 EDD 降级（p-value 分层）→ D029 domain bias 诚实化 → D034 目标 Findings → D035 补 6 个实验
- **最易判断错的事**：论文有 local/remote 两份 tex。REMOTE 是 R5-R7 精修但无 final fixes；LOCAL 是合并后的唯一正确版本。不要再改 remote 的 paper/ 目录
- **最易踩的坑**：Agent 倾向将 borderline 结果标 "success"（mixed_depth 事件）。任何 pre-registered threshold 未达标的实验，即使有合理 rationalization，结论也应标 partial/negative
- Abstract 不得超过 ~150 words / 不得引用 §4.4 / 不得有 em-dash（这三个 bug 在本轮反复出现过）


---
