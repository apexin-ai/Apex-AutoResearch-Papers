# verify exp008 dryrun real data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp008_dryrun_real_data_20260514T141556_result.json`
- **Structured JSON:** [`c55730b004b67fe02ff4.json`](../../sessions/c5/c55730b004b67fe02ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications complete. Here's the summary:

---

## 验证结果

### 1. exp-002 Signal 兼容性 — ✅ PASS
- d000 和 d005 各有 3 signal types × 3 benchmarks 的完整数据
- 数据格式（list of dicts with `s1_embedding`, `s2_minkpp`, `s3_constat`, `s4_selfcritique`）与 exp-008 `load_signals_from_dir()` 完全兼容
- **实测验证**：用 exp-002 d000/d005 的 mmlu 数据直接跑了 2-regime survival analysis，成功产出结果：
  - Embedding signal **survived**（AUC 0.505 → 0.953, ratio=1.89）
  - Min-K%++ / Self-Critique 未 survive

### 2. 模型/Adapter 路径 — ✅ 全部存在
| Regime | Path | Status |
|--------|------|--------|
| base | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/` | ✅ |
| sft_clean | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/` | ✅ |
| sft_contam | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/` | ✅ |
| rl_aligned | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/` | ✅ |

### 3. Dry-run — ✅ PASS
4-regime mock data dry-run 成功，pipeline 完整走通（参数解析 → mock 生成 → survival analysis → report 输出）。

### 4. 缺失数据
| Regime | Signal 数据 | 需要操作 |
|--------|------------|---------|
| sft_clean (d000) | ✅ 已有（exp-002） | symlink 到 exp-008 per-bench 子目录结构 |
| sft_contam (d005) | ✅ 已有（exp-002） | symlink 到 exp-008 per-bench 子目录结构 |
| **base** | ❌ 缺失 | GPU 计算：裸 Qwen2.5-0.5B，3 benchmarks × 3 signals |
| **rl_aligned** | ❌ 缺失 | GPU 计算：Qwen2.5-0.5B-Instruct，3 benchmarks × 3 signals |

**目录结构适配**：exp-002 存储为 `{model}/signals_merged_{bench}.json`（flat），exp-008 期望 `{regime}/{bench}/signals_merged_{bench}.json`（nested）。需 symlink 或 copy。

**GPU 时间估算**：2 regimes × 3 benchmarks × 3 signals，0.5B 模型。估计 2-3 小时（单 GPU）。

### 5. Full Run 前置条件清单
1. 为 base 和 rl_aligned 计算 signal（需 GPU，~2-3h）
2. 将 exp-002 的 sft_clean/sft_contam signals symlink 到 `exp008/signals/{regime}/{bench}/` 结构，**或**让 `run_exp008.sh` 自动重新计算（脚本有 `[SKIP]` 逻辑，但需要先放好文件）
3. Labels 转换（脚本 Step 0 自动处理）
4. 提交前检查目标 GPU 无冲突进程（C001 约束）
5. 注意：`run_exp008.sh` 的 `SIGNALS` 不含 constat，仅跑 embedding/minkpp/selfcritique

---
