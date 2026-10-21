# fix spatial s47 data issues

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_spatial-s47-data-issues_20260524T133535_result.json`
- **Structured JSON:** [`b6285b35ce878d7bffaa.json`](../../sessions/b6/b6285b35ce878d7bffaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## Item 2: K2mean JSON 覆写 bug

**根因**：`evaluate.py` output_file 默认值逻辑不区分 `baseline_mode=single` vs `mean`，两者都写入 `eval_{benchmark}_vla_only_seed{seed}.json`。

**修复**：
- **代码**：在 4 台服务器（cqa1-32758、bjb2-28827、bjb1-32546、bjb2-40593）的 `evaluate.py` 第 834 行添加 `mode_str` 逻辑——`baseline_mode=mean` 时输出文件名为 `eval_{benchmark}_k{K}mean_seed{seed}.json`
- **Registry**：`eval-supp-spatial-k2mean-s47` notes 已更新，标注 SR=82% (164/200)，per-task 数据不可恢复

## Item 3: 两个 Adaptive Spatial s47 配置

| 实验 | Checkpoint | K | norm | SR | 角色 |
|------|-----------|---|------|-----|------|
| `eval-supp-adapt-tau025-spatial-s47` | 3-suite (`crm_smolvla_3suite_v1`) | 10 | 0.2 | **81.5%** | **Table 1 canonical config** |
| `eval-supp-spatial-adapt-tau025-s47` | 4-suite (`crm_unified_4suite_r4`) | 2 | — | 79.0% | Supplementary variant |

Table 1 Adaptive Spatial = **80.8±1.1%**（seeds 42/45/46 三种子均值），3-suite + K=10 + norm=0.2 是 canonical 配置。两个实验的 registry notes 已标注。

## Item 4: VLA-only K 值验证

- **命令传入** `--K 2`，但 **实际执行 K=1**
- 原因：代码 line 819 `if args.mode == "vla_only" and args.baseline_mode == "single": args.K = 1` 强制覆盖
- JSON 确认 `baseline_mode: "single"`，无 K 字段记录
- 其他 suite 的 VLA-only 全部显式传 `--K 1`，仅此实验命令不一致但结果正确
- Registry notes 已更新说明

---
