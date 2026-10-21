# diagnose 10894 disk failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_disk_failure_20260527T071604_result.json`
- **Structured JSON:** [`f21060f74803c7bc2cab.json`](../../sessions/f2/f21060f74803c7bc2cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### full_occ_ln_v2_s0d 失败原因
与 detach_ln_v2_s0c_r2 相同：**磁盘满 (os error 28)**。在 step 20000 checkpoint 保存时 tokenizer.save() 失败。

### 磁盘状态
`/root/autodl-tmp` **250G/250G = 100%**，仅剩 1.7MB。checkpoints 占 229G (91.6%)。

### 在跑实验
两个都还活着：
- pid 481426 (s1c_r2, cuda:0) — 运行 6h39m
- pid 481643 (s2_r2, cuda:1) — 运行 6h39m

**但它们下次保存 checkpoint（step 30000）时会因磁盘满失败。**

### 可清理空间

| 类别 | 大小 | 说明 |
|------|------|------|
| 不完整 checkpoint（s0d + s0c 的 20000 step） | ~5G | 立即可删，无价值 |
| 旧实验 checkpoint（9个目录） | ~126G | 需确认是否还需要 |

### 建议
1. **紧急**：立即删除两个不完整的 20000_chkpt（~5G）
2. **仍然不够**——需要额外清理至少 30G 旧实验 checkpoint 才能保证在跑实验能正常保存下一个 checkpoint
3. 清理后可从 step 10000 resume 两个失败实验（非 cutoff 实验，不受 C002 约束）

需要我执行清理操作吗？

---
