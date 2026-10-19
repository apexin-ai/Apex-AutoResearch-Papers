# code classify errors v2

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify_errors_v2_20260512T172641_result.json`
- **Structured JSON:** [`52a5fac28cda4c3694c7.json`](../../sessions/52/52a5fac28cda4c3694c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，结果汇总：

**数据统计**:
- 加载 3119 条 expert 轨迹，48 条 model 轨迹（27 条失败）
- 匹配成功 23/27（85%），4 条未匹配（expert 数据缺少对应 trial）

**匹配结果**:
- Task type 分布：pick_heat_then_place (9), pick_clean_then_place (6), pick_cool_then_place (4), pick_two_obj (3), pick_and_place (1)
- Correction span：min=6, max=27, mean=11.0

**关键发现**:
- 21/23 条在 step 1 就 diverge（模型第一步就去了错误位置），说明绝大多数是 **planning error**——模型对物品位置的初始搜索策略与 expert 不同
- 仅 2 条在 step 2-3 diverge（task_id=0 和 task_id=9）
- 所有失败轨迹都跑满了 40 步上限，而 expert 平均只需 ~11 步

**4 条未匹配的 trial**:
- `pick_clean_then_place_in_recep-Ladle-None-Cabinet-16/trial_T20190910_022155_266935`
- `pick_and_place_simple-Potato-None-Microwave-30/trial_T20190907_015922_868391`
- `pick_heat_then_place_in_recep-Cup-None-Cabinet-12/trial_T20190907_210928_389193`
- `pick_two_obj_and_place-SaltShaker-None-Drawer-12/trial_T20190907_175527_049563`

这些 trial ID 不在 expert SFT 数据中，属于数据覆盖不全。

**输出格式** 正确：每行 JSONL 含 task_id、task_type、game_file、divergence_step、correction_span、expert/model action at divergence。脚本已就绪，可加 `--dry_run` 去掉后用 14B-AWQ 模型做实际分类。

---
