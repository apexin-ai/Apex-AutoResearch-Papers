# code prep factorial seed2 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-factorial-seed2-config_20260518T044838_result.json`
- **Structured JSON:** [`c8dbba256141684f10c1.json`](../../sessions/c8/c8dbba256141684f10c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

| 项目 | 值 |
|------|-----|
| **配置文件** | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_episode_adv_seed2.yaml` |
| **seed.train** | `43`（seed 1 = `10000`，注意：非 42，base.yaml 默认值） |
| **seed.val** | `123`（与 seed 1 一致） |
| **experiment_name** | `factorial-h2-episodeadv-seed2` |
| **起始 checkpoint** | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` ✅ 已确认存在 |
| **checkpoint 输出** | `/root/autodl-tmp/checkpoints/factorial-h2-episodeadv-seed2/` ✅ 独立目录，已创建 |
| **磁盘空间** | `/root/autodl-tmp/` 250G 总容量，129G 可用（49% 使用） |
| **dry-run** | ✅ 通过，YAML 解析正确 |

**需确认**：seed 1 配置中没有显式 seed 字段，继承 base.yaml 默认值 `seed.train: 10000`。如果希望 seed 对比有意义（如 42 vs 43），需要回头给 seed 1 也显式设 seed。当前 seed 2 = 43 与 seed 1 = 10000 的差异已经满足"不同 seed"的要求。

---
