# eval kill and restart

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kill_and_restart_20260516T075228_result.json`
- **Structured JSON:** [`dd5914bf61eb1f027dae.json`](../../sessions/dd/dd5914bf61eb1f027dae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry run 失败。** TypeError 已修复（0 次出现），但所有 episode 均因 `jaxtyping.TypeCheckError` 失败。

错误详情：

```
jaxtyping.TypeCheckError: Type-check error whilst checking the parameters of openpi.models.model.Observation.
```

调用链：`evaluate_libero_plus.py:374 → run_episode:317 → meta_brain.infer(obs_dict)`

根因：图像维度格式不匹配。日志显示输入是 `f32[1,3,224,224]`（NCHW），但 jaxtyping 注解期望 `*b h w c`（NHWC）格式。实际维度映射为 `h=3, w=224, c=224`，说明 channel 维被错误地当作了 height。

所有 7 个 perturbation 类型的 episode 均 100% 失败（0/0），共触发 7 次 TypeCheckError（每个 perturbation 各 1 次）。

---

**最终结果：**

1. **Kill 结果：** 旧进程已全部终止（ps 无残留 evaluate_libero_plus 进程）
2. **Dry run 结果：** 失败 — TypeError 已修复，但新出现 `jaxtyping.TypeCheckError`（图像 NCHW→NHWC 维度不匹配）
3. **未重启 3 路评估** — dry run 未通过，不执行 Step 3

需要在 `meta_brain.infer()` 中将图像从 NCHW 转为 NHWC（`images.permute(0, 2, 3, 1)`），或在 `evaluate_libero_plus.py` 构造 `obs_dict` 时调整维度顺序。

---
