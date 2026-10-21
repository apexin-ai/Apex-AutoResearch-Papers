# infra eval readiness check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-readiness-check_20260512T202335_result.json`
- **Structured JSON:** [`fa9c61f92936d5078da8.json`](../../sessions/fa/fa9c61f92936d5078da8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_readiness_report.md`。

**总结：**

**seetacloud CWM v6** — eval 基本就绪 ✅
- 训练正常（step 175/6633, ~15h 剩余），eval 回调正常运行
- `eval_repo_cwm.py` 可用，数据/依赖齐全
- 首个 checkpoint 预计在 step 500（~1h 后）
- 启动时需手动传 `--model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`

**home CLS** — ❌ 有 P0 阻塞问题
- 训练在跑（step 1606/6633），但 **checkpoint 目录完全为空**
- 日志中零条 "Saving"、零条 "eval_loss"——Trainer 的 eval/save 回调从未触发
- eval 脚本和数据都就绪，唯独缺 checkpoint
- **需要立即排查**：可能训练完成后只能靠末尾 `trainer.save_model()` 拿到一个最终模型，但如果 `load_best_model_at_end=True` 在没有 eval metric 的情况下报错，连最终模型也可能丢失

---
