# check gradient checkpoint versions

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gradient-checkpoint-versions_20260527T091018_result.json`
- **Structured JSON:** [`86747799eaa396923031.json`](../../sessions/86/86747799eaa396923031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**所有 5 个 checkpoint 都是用 v2 代码训练的。** `detach_ln_s3` 名字虽然没有 "v2" 后缀，但确认是 v2 代码训练。

### 证据

#### 1. 代码一致性
两台服务器的 `finetune.py` **完全相同**（57288 bytes），都包含 v2 关键特征：
- `resume_step` 修复（L1235）
- `gradient_step_idx` 替代 `batch_idx` 做 cutoff 判断
- `clean_cutoff` 标志

#### 2. 时间线

| Checkpoint | 服务器 | 训练启动 (Beijing) | 代码最后修改 (Beijing) | 间隔 |
|-----------|--------|-------------------|----------------------|------|
| mvp_occ_s3_v2 | 10894 | 05-26 04:42 | 05-25 12:33 | +16h |
| full_occ_ln_s3_v2 | 10894 | 05-26 04:42 | 05-25 12:33 | +16h |
| ablation_occ_detach_s3_v2 | 10894 | 05-26 04:43 | 05-25 12:33 | +16h |
| **detach_ln_s3** | **34685** | **05-26 16:45** | **05-25 21:46** | **+19h** |
| vanilla_v2_s1 | 34685 | 05-26 16:45 | 05-25 21:46 | +19h |

所有训练都在 v2 代码更新之后启动。

#### 3. `detach_ln_s3` 为何没有 "v2" 后缀
- v1 系列用了 seed 0-2（`detach_ln_s0/s1/s2`），全部在 **05-24 01:10-01:11** 启动
- v2 显式命名系列从 `detach_ln_v2_s0` 开始，在 **05-27 02:08** 启动
- `detach_ln_s3` 是 seed 3（v1 从未使用过），在 **05-26 16:45** 启动——时间上完全在 v2 时代
- 纯粹是命名不一致，不是代码版本问题

#### 4. 补充证据
- `detach_ln_s3` 和 `vanilla_v2_s1` 在 34685 上同时启动（16:45:54 vs 16:45:59），属于同一批实验
- 梯度分析脚本 `run_gradient_analysis_5cond.sh` 明确标注这两个需要从 34685 SCP 过来
- 所有 5 个实验的 trainable params 完全一致（occ_head: 1,213,313, total: 279,977,608）

**梯度分析中 "Detach LN v2" 标签是正确的。**

---
