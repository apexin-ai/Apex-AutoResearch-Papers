# prep c2 s43 and c1 commands

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_c2_s43_and_c1_commands_20260525T032255_result.json`
- **Structured JSON:** [`f633f9d1686bb2285691.json`](../../sessions/f6/f633f9d1686bb2285691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码检查和命令准备完成。汇总：

## 代码确认

- `--intervention_mode` 支持 `none` / `predictive` / `reactive`，两者逻辑相同——都监控 `--intervention_metric` 的 gen-over-gen 相对下降，超过 `--intervention_threshold` 时触发，将 α 从 `--synthetic_ratio` 切换到 `--intervention_alpha`
- `distinct_1` 是有效的 downstream metric（metrics.py 中由 `compute_distinct_n` 计算）
- reactive 和 predictive 的区别纯粹是语义层面：predictive 用 canary metric（token_entropy），reactive 用 downstream metric（distinct_1）

## 5 组实验命令

| # | 实验 | 模型 | 模式 | N | 预估时间 | VRAM |
|---|------|------|------|---|---------|------|
| 1 | C2-s43 | OPT-1.3B | 无干预, α=0.50 | 10 | 12-14h | 12-14G |
| 2 | C1-GPT2m-pred | GPT-2-medium | predictive/token_entropy | 5 | 2-2.5h | 6-8G |
| 3 | C1-GPT2m-react | GPT-2-medium | reactive/distinct_1 | 5 | 2-2.5h | 6-8G |
| 4 | C1-OPT1.3B-pred | OPT-1.3B | predictive/token_entropy | 5 | 5-7h | 12-14G |
| 5 | C1-OPT1.3B-react | OPT-1.3B | reactive/distinct_1 | 5 | 5-7h | 12-14G |

## 注意

- `a050_s43_fp32` 目录已存在（只有 config.json，之前失败的），所以 C2-s43 用 `a050_s43_fp32_v2`
- `a050_s42_fp32` 正在运行（到 gen_3），不要干扰
- 磁盘 61G 可用，顺序执行 5 组总共 ~41G peak，可以支撑
- 启动前需 `mkdir -p` 输出目录（nohup redirect 需要目录存在）

完整命令已写入 `artifacts/c2_c1_launch_commands.json`。

---
