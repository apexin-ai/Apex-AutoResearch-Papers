# analysis 4seed fisher readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4seed-fisher-readiness_20260516T202005_result.json`
- **Structured JSON:** [`991ff679d5b4a83c290e.json`](../../sessions/99/991ff679d5b4a83c290e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本验证通过，3-seed 结果完全匹配已知数据。

**需要为 4-seed 做的准备**：seed45 完成后，需在 `magnitude_curve_data.json` 的 `seed_comparison` 中添加 seed45 条目。脚本本身已经支持 `--seeds 42 43 44 45`。

当前问题：脚本从 `magnitude_curve_data.json` 读取而非直接从服务器 raw JSON。seed45 完成后的工作流是：

1. 从服务器获取 seed45 的 obs-only-norm02 和 argmin 的 successes/total
2. 在 `magnitude_curve_data.json` 的 `seed_comparison.obs_only_norm02` 和 `seed_comparison.argmin` 中各加一条 seed45 记录
3. 运行：
```bash
python3 pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44 45
```

**总结**：

| 项目 | 状态 |
|------|------|
| 脚本路径 | `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pooled_fisher_test_v2.py` |
| 逻辑 | 从 JSON 读真实 counts，无 ×2 bug，支持任意 seed 数 |
| 3-seed 验证 | p(one-sided)=0.1102 ✓ |
| seed45 后操作 | 更新 `magnitude_curve_data.json` 加入 seed45 两条记录 → 跑上述命令 |

脚本就绪，无需修改。seed45 完成后更新数据文件即可直接调用。

---
