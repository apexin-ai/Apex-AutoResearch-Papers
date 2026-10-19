# exp029_seed6_ood_eval_v2 诊断报告

## 结论：评估实际上已成功完成，被 cron 误判为失败

### OOD 评估结果（134 tasks, valid_unseen, τ=0.4）

| 指标 | 值 |
|------|-----|
| **success / pass@1** | **29.1%** (39/134) |
| num_actions | 36.57 |
| action_is_effective | 97.3% |
| action_is_valid | 63.2% |
| manager_invalid_action | 2.7% |
| response_length | 5605.4 |
| best@4 | 78.1% |
| best@16 | 99.4% |

### 失败根因

**wandb teardown BrokenPipeError** — 评估完成后，进程退出时 wandb SDK 的 atexit hook 在关闭连接时触发 `BrokenPipeError: [Errno 32] Broken pipe`（`service_client.py:123 → asyncio/streams.py:364`）。这导致进程以非零退出码结束。

cron 监控逻辑：检测到进程死亡 5 次 + 未发现 sentinel 文件 + W&B 数据可能未完整同步 → 自动判定为失败。

**实际上评估已完整跑完**，所有 134 个 OOD 任务都有结果，日志最后打印了完整的 metrics dict。

### Traceback

```
File "wandb/sdk/lib/service/service_connection.py", line 73, in teardown_atexit
  conn.teardown(hooks.exit_code)
  ...
File "wandb/sdk/lib/service/service_client.py", line 123, in close
  await self._writer.wait_closed()
File "asyncio/streams.py", line 364, in wait_closed
  await self._protocol._get_close_waiter(self)
BrokenPipeError: [Errno 32] Broken pipe
```

### Checkpoint 和 Symlink 状态

- **Checkpoint 存在且完整**: `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf/`（含 model.safetensors 3.8GB, config.json, tokenizer 文件）
- **config.json**: `model_type: qwen3`, `Qwen3ForCausalLM` — 模型正确识别
- **Symlink 正确**: `/root/autodl-tmp/checkpoints/qwen_exp029_seed6_step15_hf -> /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf`（v1 的 `ValueError: Unsupported model` 问题已修复）
- **W&B run**: `kjrzoopp` (project: cost-verify-agent-rl, user: xiaoyucorynne)

### 修复建议

1. **无需 v3** — 评估已完成，结果有效。直接从日志提取 metrics 即可。
2. **防止复发**：eval-only 脚本应在打印 metrics 后、wandb.finish() 前写 sentinel 文件，确保即使 wandb teardown 崩溃也不会被误判。
3. **W&B BrokenPipeError**: wandb 0.26.0 的已知问题，发生在 Ray worker 进程退出时。可忽略或升级 wandb。
4. **cron 监控改进**：对 eval-only 任务，应检查日志中是否有 metrics 输出作为成功判定的备选信号。
