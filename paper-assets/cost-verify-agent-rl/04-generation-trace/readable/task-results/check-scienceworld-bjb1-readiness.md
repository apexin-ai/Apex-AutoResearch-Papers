# check scienceworld bjb1 readiness

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scienceworld_bjb1_readiness_20260524T033129_result.json`
- **Structured JSON:** [`c44e3740d5779b1d0337.json`](../../sessions/c4/c44e3740d5779b1d0337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-17606 ScienceWorld 环境检查报告

| 检查项 | 状态 | 详情 |
|--------|------|------|
| ScienceWorld 包 | ✅ 已安装 | `scienceworld 1.2.3` |
| Java 环境 | ✅ 可用 | OpenJDK 11.0.30, `/usr/bin/java` |
| ScienceWorld 配置文件 | ✅ 存在 | 6 个配置（Cell A + Cell C v1-v6），但**无 Cell D 配置** |
| ScienceWorld SFT checkpoint | ❌ 缺失 | `qwen3_scienceworld_sft/huggingface/` 和 `scienceworld_sft/` 均不存在 |
| RAGEN 代码 | ✅ main 分支 | 最新 commit: `3a6b48b` (trajectory-level token cap) |
| 磁盘空间 | ✅ 充足 | `/root/autodl-tmp/` 剩余 **101GB**（250GB 用了 150GB） |

### 缺少的组件

1. **ScienceWorld SFT checkpoint** — Cell A 配置引用 `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface`，Cell C v6 引用 `/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface`，两个路径在 bjb1 上都不存在。需要从 westd-47453 拷贝过来或重新训练。

2. **Cell D 配置文件** — 现有配置只有 Cell A 和 Cell C 系列，需要新建 Cell D 的 YAML 配置。

---
