# v9d 崩溃诊断报告

**日期**: 2026-05-20
**实验**: 8b_cell_c_episode_v9d (8B Cell C episode-level GRPO, FSDP2+CPUOffload, 4×96GB GPU)
**服务器**: westd-47453

## 崩溃历史

| Run | EXIT_CODE | 原因 |
|-----|-----------|------|
| v9  | 无记录    | 早期运行，无 exit trap |
| v9b | 1         | SFT checkpoint 被删 (HFValidationError) |
| v9c | 1         | vLLM prompt 长度 = max_model_len (16384)，无输出空间 |
| v9d | 运行中    | 从 global_step_10 恢复 |

## 关键发现：无 SIGHUP

**原报告称 EXIT_CODE=129 (SIGHUP)，但所有日志均显示 EXIT_CODE=1。** 不存在 SIGHUP 崩溃。所有崩溃均为应用层错误。

## v9c 崩溃根因

```
ValueError: The decoder prompt (length 16384) plus the number of requested output tokens
(at least 1) is longer than the maximum model length of 16384.
```

- 发生在 `vllm_rollout_spmd.py:383 generate_sequences()` → vLLM `input_processor.py:370 _validate_prompt_len()`
- 原因：agent_proxy 的 `max_prompt_length=15360`，但多轮对话 prompt 可超此限制并达到 vLLM 的 `max_model_len=16384`
- 随机性问题——取决于特定 episode 的对话轮数和 action 长度

## v9d 当前状态

- **已自动重启**（15:56:53 UTC），从 `global_step_10` 恢复
- SFT checkpoint 通过 symlink 修复：`checkpoint-231` → `/root/autodl-tmp/models/Qwen3-8B`
- 模型、优化器状态、RNG、lr_scheduler 均从 checkpoint 加载
- wandb run: `aeml21w9`
- 磁盘：106GB 可用
- 剩余：20 步 (step 11-30)

## 风险

v9c 的 prompt 长度崩溃可能在 v9d 重现——config 中 `max_prompt_length=15360` 和 `max_model_len=16384` 未变。如果某个 episode 的多轮对话 prompt 恰好达到 16384 token，训练会再次崩溃。

## 建议

若 v9d 因相同原因再次崩溃：
1. 将 `max_prompt_length` 降至 14336（留 2048 token 给输出）
2. 或将 `max_model_len` 提升至 32768（需确认显存足够）
3. 或在 agent_proxy 层做更严格的 prompt truncation