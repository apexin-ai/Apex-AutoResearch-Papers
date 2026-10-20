# gpu 5090 check and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090_check_and_fill_20260521T071506_result.json`
- **Structured JSON:** [`bfa6a69f9aeac3e7e260.json`](../../sessions/bf/bfa6a69f9aeac3e7e260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 5090 GPU 状态报告

| GPU | VRAM | GPU Util | 实验 | 模型 | 进度 | ETA |
|-----|------|----------|------|------|------|-----|
| **cuda:0** | 30170/32607 MiB | 75% | FewNERD MF4v2 seed456 | `qwen3-8b-fewnerd-exp021-merged` (fine-tuned) | **76%** (228944/301184) | ~22 min |
| **cuda:1** | 30080/32607 MiB | 69% | E2 pretrained FewNERD (seed42) | `Qwen2.5-7B-Instruct` (pretrained) | 运行中，与 cuda:3 重复 | ~数小时 |
| **cuda:2** | **2 MiB** | **0%** | **空闲** | — | E2 pretrained CoNLL 已完成 (EXIT_CODE=0) | — |
| **cuda:3** | 30044/32607 MiB | 63% | E2 pretrained FewNERD (seed42) | `Qwen2.5-7B-Instruct` (pretrained) | **27%** (82296/301184) | ~3h |

### 关键发现

1. **cuda:2 已空闲**，可立即使用。

2. **cuda:1 和 cuda:3 运行重复实验**：同一命令（e2_pretrained_fewnerd, seed42, Qwen2.5-7B-Instruct），写入同一 output dir (`output/e2_pretrained_fewnerd/`)，共享同一日志文件。存在数据竞争/覆盖风险。output dir 目前为空（两者都在采样阶段）。

3. **cuda:0 即将完成**（~22min），之后也会空闲。

4. **E2 pretrained CoNLL 实验已完成**：report.json 显示 verdict=MARGINAL，greedy_f1=0.538，oracle_f1=0.628，结构化信号微弱优于表面信号（rho_advantage=0.012）。

5. **CoNLL MF4 s123/s456 均失败**：VLLM engine core initialization error（因 GPU 被占满无法启动）。

### 可用资源

- **cuda:2**：立即可用
- **cuda:0**：~22min 后可用
- **可用模型**：FewNERD fine-tuned (`checkpoints/qwen3-8b-fewnerd-exp021-merged`)，pretrained Qwen2.5-7B-Instruct
- **cuda:1/cuda:3 重复问题**需要决策：是否 kill 其中一个以释放 GPU

---
