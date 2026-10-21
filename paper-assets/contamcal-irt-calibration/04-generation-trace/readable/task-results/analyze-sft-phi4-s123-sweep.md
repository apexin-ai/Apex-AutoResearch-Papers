# analyze sft phi4 s123 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_sft_phi4_s123_sweep_20260520T011229_result.json`
- **Structured JSON:** [`e16659ac06166c1cee1b.json`](../../sessions/e1/e16659ac06166c1cee1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成 (DONE/success)。现在 `save_project_file` 不能直接写 report.md（自动生成），我确认下 report.md 是否需要手动更新。

根据工具描述，report.md 是 auto-generated 的，不在可写白名单中。registry 更新后 report 应该会自动刷新。

分析完成。结果总结：

**sft_phi4_s123_sweep — 全部成功**

- **5/5 dosage 完成**，全部 exit_code=0，无 error/OOM
- 服务器：westd-29999 cuda:0，总耗时 ~11.5h（May 19 21:40 → May 20 09:10）
- 配置：lora_r=16, lora_alpha=32, lr=5e-5, seed=123
- Train loss 跨 dosage 稳定：1.183 (d000) → 1.191 (d100)
- W&B 离线模式，无在线 run
- Checkpoint 路径：`/root/autodl-tmp/exp001/checkpoints/phi-4_d{000,005,025,050,100}_s123/`
- Registry 已标记 DONE(success)，含完整 metrics

**下一步**：对这 5 个 checkpoint 做 MMLU eval，验证 s123 是否复现 s42 的 immune pattern (Δacc ≈ ±0.54pp)。

---
