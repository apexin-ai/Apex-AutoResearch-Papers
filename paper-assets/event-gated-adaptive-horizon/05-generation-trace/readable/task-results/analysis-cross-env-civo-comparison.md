# analysis cross env civo comparison

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_env_civo_comparison_20260525T033401_result.json`
- **Structured JSON:** [`536224babcbbbf899406.json`](../../sessions/53/536224babcbbbf899406.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成并注册。以下是结果：

---

## LaTeX Table

```latex
\begin{table}[t]
\centering
\caption{Cross-environment CIVO comparison. \textbf{Trigger}: trained dt\_emb + subsample ON + $H{=}8$; \textbf{Control}: dt\_embed\_dim$=$0 (no dt\_emb) + subsample ON + $H{=}8$. NVE Peak reports the maximum Normalized Value Excess across all seeds. CIVO is flagged when any seed exceeds NVE $\geq 1.5\times$.}
\label{tab:cross_env_civo}
\begin{tabular}{llccc}
\toprule
Environment & Configuration & Eval Return & NVE Peak & CIVO \\
\midrule
\multirow{3}{*}{Walker Walk}
 & Baseline ($\Delta t{=}1$) & $787.7 \pm 230.8$ & --- & --- \\
 & Trigger (trained dt\_emb) & $140.6 \pm 111.5$ & $4.72\times$ & \cmark~(5/5) \\
 & Control (no dt\_emb) & $373.8 \pm 111.9$ & $1.41\times$ & \xmark~(0/4) \\
\midrule
\multirow{3}{*}{Cheetah Run}
 & Baseline ($\Delta t{=}1$) & $593.9 \pm 60.4$ & --- & --- \\
 & Trigger (trained dt\_emb) & $26.3 \pm 36.0$ & $70.64\times$ & \cmark~(2/2) \\
 & Control (no dt\_emb) & $86.9 \pm 13.6$ & $0.20\times$ & \xmark~(0/2) \\
\midrule
\multirow{3}{*}{Cartpole Swingup}
 & Baseline ($\Delta t{=}1$) & $673.3 \pm 142.0$ & --- & --- \\
 & Trigger (trained dt\_emb) & $236.3 \pm 29.7$ & $0.06\times$ & \xmark~(0/3) \\
 & Control (no dt\_emb) & \multicolumn{3}{c}{\emph{running (exp\_062)}} \\
\bottomrule
\end{tabular}
\end{table}
```

---

## CSV

```
Environment,Configuration,Eval Return (mean),Eval Return (std),Seeds (eval),NVE Peak (max),CIVO
Walker Walk,Baseline (dt=1),787.7,230.8,4,—,—
Walker Walk,Trigger (trained dt_emb),140.6,111.5,3,4.72×,Yes (5/5)
Walker Walk,Control (no dt_emb),373.8,111.9,3,1.41×,No (0/4)
Cheetah Run,Baseline (dt=1),593.9,60.4,5,—,—
Cheetah Run,Trigger (trained dt_emb),26.3,36.0,2,70.64×,Yes (2/2)
Cheetah Run,Control (no dt_emb),86.9,13.6,2,0.20×,No (0/2)
Cartpole Swingup,Baseline (dt=1),673.3,142.0,3,—,—
Cartpole Swingup,Trigger (trained dt_emb),236.3,29.7,3,0.06×,No (0/3)
Cartpole Swingup,Control (no dt_emb),—,—,0,—,RUNNING
```

---

## 关键发现

| 环境 | CIVO 触发? | NVE 严重程度 | 备注 |
|---|---|---|---|
| Walker Walk | **Yes** (5/5 seeds) | 4.72× | 100% 复现，中等 NVE |
| Cheetah Run | **Yes** (2/2 seeds) | 70.64× | NVE 极高，不可自修复 |
| Cartpole Swingup | **No** (0/3 seeds) | 0.06× | trained dt_emb 未触发 CIVO，但 eval 仍显著下降 (236 vs 673) |

**exp_062 (Cartpole Control)** 仍在运行，registry 无 metrics。服务器上也未找到日志目录。

---
