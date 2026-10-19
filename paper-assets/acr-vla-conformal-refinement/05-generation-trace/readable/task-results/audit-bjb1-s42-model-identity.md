# audit bjb1 s42 model identity

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-s42-model-identity_20260525T021418_result.json`
- **Structured JSON:** [`825d1ac61e232c43053b.json`](../../sessions/82/825d1ac61e232c43053b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux isn't allowed in read-only mode, but it doesn't matter — the log is conclusive.

## 结论：模型是 SmolVLA，不是 π0.5

### 证据

1. **日志 args 明确声明** `'model': 'smolvla'`
2. **加载信息**: `[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...`
3. **checkpoint 路径**: `smolvla_path: '/root/autodl-tmp/models/smolvla_libero/'`（不是 pi05 路径）
4. **输出文件**: 写入 `eval_spatial_vla_only_seed42.json`（不是 `eval_spatial_vla_only_pi05_seed42.json`）
5. **π0.5 结果独立存在**: 同目录下有单独的 `eval_spatial_vla_only_pi05_seed42.json`，其 SR=98%，与 SmolVLA 的 80% 完全不同

### wall_clock 解释

3.14h 对 SmolVLA 并非异常：10 tasks × 20 rollouts × max_steps=280 = 200 episodes，在该服务器上耗时合理。审计中 "SmolVLA ≈ 30min" 的估计可能基于更少 rollouts 或更快 GPU。

### registry 状态

Registry 中 `exp_id: eval-supp-spatial-vla-only-s42` 返回 0 条记录，metadata 中标注 `model=pi05` 可能是注册时的标注错误。

### 结论

**SR=80.0% 可以用于 SmolVLA Table 1。** 该数据点确实是 SmolVLA spatial vla-only seed42 的结果。如果 registry 有错误标注，建议修正 model 字段为 `smolvla`。

---
