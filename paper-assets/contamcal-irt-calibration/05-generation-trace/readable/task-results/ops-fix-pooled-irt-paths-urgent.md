# ops fix pooled irt paths urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-pooled-irt-paths-urgent_20260515T011237_result.json`
- **Structured JSON:** [`8baa61e91bbdcb08fb04.json`](../../sessions/8b/8baa61e91bbdcb08fb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果：

**脚本修改** — Phase 1 和 Phase 2 均已添加 `3B && s42` 条件分支，使用 `_v2_` 路径。

**v1 目录重命名**：
- `Qwen2.5-3B_d000_s42_aligned` → `_v1_..._DEPRECATED`
- `Qwen2.5-3B_d005_s42_aligned` → `_v1_..._DEPRECATED`
- `Qwen2.5-3B_d100_s42_aligned` → `_v1_..._DEPRECATED`

**dry-run 验证**：
- `3B d000 s42` → eval DONE（正确命中 `d000_v2_s42_aligned`）
- `3B d100 s42` → SFT MISSING（`d100_v2_s42_aligned` 目录存在但为空，eval 尚未完成）
- 0.5B/1.5B 全部不受影响
- 无 v1 旧路径被匹配：`ls -d *_s42_aligned` 只返回 v2 目录

备份文件保存在 `run_pooled_irt_n16.sh.bak`。

注意：`d100_v2_s42_aligned/` 目录是空的（无 `eval_results.json`），需要补跑 3B d100 v2 的 aligned eval 才能在 pooled IRT 中纳入该配置。

---
