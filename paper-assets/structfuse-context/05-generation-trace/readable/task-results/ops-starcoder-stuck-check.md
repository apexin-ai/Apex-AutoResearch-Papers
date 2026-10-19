# ops starcoder stuck check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_starcoder_stuck_check_20260516T155944_result.json`
- **Structured JSON:** [`0c2a95352d32d199c43a.json`](../../sessions/0c/0c2a95352d32d199c43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到原因了。代码在 early stopping 后还有一个 **final eval + final checkpoint save** 阶段：

```python
# ── final save ───────────────────────────────────────────────
if accelerator.is_main_process:
    final_metrics = evaluate(accelerator.unwrap_model(model), val_loader, accelerator)
    _print_flush(f"[Final eval] {final_metrics}")
    ...
    _save_checkpoint(...)
```

## 结论：进程卡在 final eval 阶段

**状态**：
- PID 129747：`R` (running)，运行 13h54m
- GPU 1：100% 利用率，占用 54GB 显存
- 日志最后输出 `Early stopping triggered at step 1500` @ 23:41（~14 分钟前）
- 之后应立即输出 `[Final eval] {...}` 但一直没有

**判断**：进程没有完全死掉（GPU 在算），但 final eval 运行了 14+ 分钟——训练时同样的 evaluate() 函数在每个 eval step 只需几十秒。说明 final eval 异常缓慢或陷入某种低效循环。

**StarCoder embed_s43 最终 metrics**（来自 eval@500，即 best checkpoint）：
| 指标 | 值 |
|------|-----|
| val_loss | **0.5229** (best) |
| R@1 | **0.4885** (best, @step 1000) |
| R@5 | 0.9535 |
| R@10 | 1.0 |

**重要 checkpoints 已保存完毕**：
- `best_by_val_loss/` (step 500)
- `best_by_recall_at_1/` (step 1000)

**建议**：可以安全 kill PID 129747。所有有价值的 checkpoint 已保存，final checkpoint 只是冗余备份。Wrapper 519791 还活着，kill 训练进程后它应该能启动链中的下一个 run。

是否 kill？

---
