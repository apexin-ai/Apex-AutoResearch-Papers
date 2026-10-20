# code prep rrrf pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_rrrf_pipeline_20260516T033708_result.json`
- **Structured JSON:** [`9f7e443b2a6181a212f9.json`](../../sessions/9f/9f7e443b2a6181a212f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全面检查完成。以下是汇总：

---

## RRF + IRT 代码就绪状态

### exp-003 (RRF 聚合) — ✅ 代码就绪

- `rrf_aggregation.py` (16KB, 今日更新): s1+s2+s4 三信号 RRF 融合，alpha=16 blocklist，`--generate-exposure` 模式直接输出 exp-006 所需的 `exposure_scores.json`
- 已有一份旧的 `/root/autodl-tmp/exp003/exposure_scores.json`，但只覆盖 0.5B (d000/d005/d100)，需要重新生成

### exp-006 (IRT Calibration) — ✅ 代码就绪

- `run_exp006.py` (29KB): 完整 pipeline — 4PL+gamma IRT + 7 baselines + evaluation
- `run_irt_calibration.py` (24.5KB): Stan NUTS fitting 核心
- `baselines.py`, `evaluate_calibration.py`, `joint_fit.py` 均存在
- Stan 模型已编译 (`contam_irt_4pl_simple` 2.9MB binary)
- CmdStan 2.38.0 ✓
- 支持 `--pool-scales 0.5B 1.5B 3B` / `--signals-dir` / per-benchmark gamma_k
- 已在 0.5B+1.5B pooled 上跑过 30+ 次 (结果目录存在)

---

## 输入数据 Gap — 瓶颈在 3B s42

### 0.5B s42 — ✅ 完整
- Eval: d000/d005/d025/d100 × aligned 全有
- Signals: d000/d005/d025/d100 全有 merged (s1+s2+s4)

### 1.5B s42 — ✅ 完整
- Eval: d000/d005/d025/d100 × aligned 全有
- Signals: d000/d005/d025/d100 全有 merged

### 3B s42 alpha=32 — ❌ 严重缺失

| Dosage | Eval (aligned) | Signals (s1+s2+s4) | 两者都有? |
|--------|---------------|-------------------|----------|
| d000 | `d000_s42_v3_aligned` ✓ | **无 signal dir** | ❌ |
| d005 | `d005_s42_a32_aligned` **空目录** | **无 signal dir** | ❌ |
| d025 | `d025_v3_s42_aligned` ✓ | `d025_v3_s42` ✓ 完整 | ✅ |
| d100 | `d100_a32_s42_aligned` **空目录** | **无 signal dir** | ❌ |

**4 个 dosage 中只有 d025 同时有 eval + signals。**

注：`d005_s42` 和 `d100_s42` signal dirs 存在但属于 alpha=16 blocklist，RRF 代码会跳过。

---

## 需要完成的工作

1. **3B s42 eval** (3 cells): d005_a32、d100_a32 aligned eval 需要跑完，d000 需确认 `d000_s42_v3` 还是 `d000_a32` 是最终版本
2. **3B s42 signals** (3 models): d000_v3、d005_a32、d100_a32 各需计算 s1+s2+s4 × 3 benchmarks = 共 27 个信号文件
3. **重跑 exp-003** RRF 生成包含全部 scale 的 `exposure_scores.json`
4. **跑 exp-006** pooled IRT (0.5B+1.5B+3B)

## 运行时间预估（数据就绪后）

| 步骤 | 时间 | 资源 |
|------|------|------|
| exp-003 RRF 聚合 | 2-5 分钟 | CPU |
| exp-006 IRT per benchmark | 15-30 分钟 | CPU (4 chains NUTS) |
| exp-006 全 3 benchmarks + baselines | 1-2 小时 | CPU |
| joint_fit 消融 | +30 分钟 | CPU |

**结论：代码完全就绪，瓶颈是 3B s42 的 eval (2 个空目录) 和 signals (3 个 dosage 完全缺失)。一旦数据补齐，RRF → IRT 全链路 ~2-3 小时可跑完。**

---
