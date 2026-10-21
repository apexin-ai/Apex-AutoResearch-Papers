# paper writing experiments framework

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_framework_20260513T215537_result.json`
- **Structured JSON:** [`8a9aa99804fc5f265cc8.json`](../../sessions/8a/8a9aa99804fc5f265cc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/_project/paper/experiments.tex`。结构：

- **§5.1 Setup** — 完整写好，包含所有具体数字（K=10, H=5, 337K params, 26,737 samples, 50 epochs, α=0.1 等），引用与 method section 一致
- **§5.2 Main Results** — Table 2 占位（SmolVLA / ReconVLA / ACR-VLA × 2 suites），分析文字用 `\textbf{XX.X}` 占位
- **§5.3 Ablation Studies** — Table 3 占位（A3/A4/A5/A7 四个 ablation），K sensitivity 用 figure placeholder，每个 ablation 有独立段落解释 what it tests
- **§5.4 Analysis** — 三部分占位：per-task breakdown table、CGS feature visualization figure、when does ACR-VLA help most 的定性分析框架

待实验数据就绪后，替换所有 `\textbf{--}` 和 `\textbf{XX.X}` 即可。

---
