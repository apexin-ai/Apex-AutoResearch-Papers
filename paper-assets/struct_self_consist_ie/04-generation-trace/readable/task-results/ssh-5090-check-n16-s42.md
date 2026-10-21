# ssh 5090 check n16 s42

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_check_n16_s42_20260521T145133_result.json`
- **Structured JSON:** [`44435188db3f21cd25ce.json`](../../sessions/44/44435188db3f21cd25ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：FewNERD N=16 s42

**进程**: 运行中 (PID 32118, cuda:0, 启动 19:23, 已运行 ~3.5h)

**阶段**: vLLM batch generation（无中间进度输出）
- Prompt rendering 已完成 (37648/37648, 耗时 1m34s)
- 进入 vLLM 推理阶段后脚本不输出进度，完成后才一次性写 `samples.jsonl` + `report.json`
- 输出目录 `output/fewnerd_n16_s42/` 目前为空（正常，脚本在生成全部完成后才写入）

**GPU 状态**:
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 (本实验) | 80% | 30726/32607 MiB |
| 1 (fewnerd_mf4v2_s42) | 85% | 30204 MiB |
| 2 (fewnerd_mf4v2_s123) | 81% | 30230 MiB |
| 3 (e2_pretrained_fewnerd_s456) | 67% | 29946 MiB |

**预估**: n_samples=16 × 37648 instances = 602,368 次生成。参考 n=8 的 fewnerd_mf4v2_seed42 前一次运行（约 1h 完成），n=16 大约需要 4-6h 总时长，预计还需 ~1-2.5h 完成。

4 卡全满，都在跑实验，状态正常。

---
