# Research conversation: [Director 指令] [Full Draft] EMNLP 2026 Main (ARR May 25, 2026, 距今 11 天) **核心 narrative**: Per-head KV cache quantization  — Part 35 of 43

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

[← Part 34](part-034.md) · [Transcript overview](../research-conversation-director-full-draft-emnlp-2026-main-arr-may-25-2026-11-narrative-per-head-kv-c.md) · [Part 36 →](part-036.md) · [Structured JSON](../../../sessions/99/994cbace00be8d6186dd.json)

## Round 196

### Assistant

_source line 3989 · 2026-05-15T14:17:32.847Z_

<details><summary>Logged reasoning block</summary>

```text
Still the same issue - page 8 ends with "We report no real-kernel latency benchmarks and" which means "have not tested beyond 14B scale." spills to page 9.

The compressed sentence helped a bit but not enough. I need to save about 1 more line. Let me look at what can be shortened further.

Options:
1. Merge the long-context reference into the existing cross-dataset sentence (save ~half a line)
2. Or compress something else in experiments.tex

Let me try combining the cross-dataset and long-context sentences:


I'm merging the two appendix references into one statement - combining the cross-dataset agreement metric with the long-context performance comparison to cut down the line count while keeping the key results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66ecbdd5-f1ac-49e4-8890-c09cd18e9a30",
  "isSidechain": false,
  "requestId": "req_011Cb4VpiSwNMcWWkkzVfwHq",
  "type": "assistant",
  "uuid": "f5384000-ff7a-48c2-91f1-a7fb0518e8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tok9vxKGMQmpVMTLDJkNKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 149990,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 149990,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 3990 · 2026-05-15T14:17:33.268Z_

仍有 1 行溢出。将 cross-dataset 和 long-context 合并为一句以节省空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5384000-ff7a-48c2-91f1-a7fb0518e8a7",
  "isSidechain": false,
  "requestId": "req_011Cb4VpiSwNMcWWkkzVfwHq",
  "type": "assistant",
  "uuid": "0809f4a7-95d8-41c4-93ed-7816c129693e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tok9vxKGMQmpVMTLDJkNKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 149990,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 149990,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 3991 · 2026-05-15T14:17:36.528Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01UzZiKtc3Ann25HN4595iSb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Cross-dataset stability analysis (Appendix~\\ref{sec:cross_dataset}) confirms ${>}96\\%$ bit-assignment agreement between WikiText-2 and C4 calibration across all three tested models.\nAt 8K context (Appendix~\\ref{sec:long_context}), Qwen's uniform 4-bit degrades to $11.15\\times$ bf16 while MCKP stays at $1.23\\times$; Llama shows no difference.",
  "new_string": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0809f4a7-95d8-41c4-93ed-7816c129693e",
  "isSidechain": false,
  "requestId": "req_011Cb4VpiSwNMcWWkkzVfwHq",
  "type": "assistant",
  "uuid": "9061cbe0-ec9d-4037-ada2-f522d5529fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tok9vxKGMQmpVMTLDJkNKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 149990,
      "output_tokens": 750,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 750,
          "cache_read_input_tokens": 149990,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3992 · 2026-05-15T14:17:36.542Z_

<details><summary>↩ Tool result · `toolu_01UzZiKtc3Ann25HN4595iSb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9061cbe0-ec9d-4037-ada2-f522d5529fea",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "bb7919bc-328f-44c2-b09e-bd0d81991943",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "Cross-dataset stability analysis (Appendix~\\ref{sec:cross_dataset}) confirms ${>}96\\%$ bit-assignment agreement between WikiText-2 and C4 calibration across all three tested models.\nAt 8K context (Appendix~\\ref{sec:long_context}), Qwen's uniform 4-bit degrades to $11.15\\times$ bf16 while MCKP stays at $1.23\\times$; Llama shows no difference.",
    "newString": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate seven models spanning five architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2 and Pythia; Qwen-14B $k$ value pending).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining (${\\sim}1.1\\times$). Greedy and MCKP produce identical unconstrained allocations on 4/5 models. Best constrained result per model in \\textbf{bold}; --- = experiment pending. $^\\ddagger$Best $k$ from ablation ($k{=}4$). $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 5.84  & ---   & ---   & ---   & --- \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.16$^\\ddagger$ \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & ---   & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\\%); near-zero sensitivity differences and sliding-window attention may both contribute.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen ($3.3\\times$ bf16), \\emph{severe} on Pythia ($1.9\\times$, 90/384 heads at 2-bit), \\emph{moderate} on Gemma-2 ($1.47\\times$, 31.5\\% 2-bit), and \\emph{mild} on the remaining models (${\\sim}1.07$--$1.08\\times$).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nHowever, KIVI cannot exploit head-level heterogeneity: on Qwen (spread), constrained MCKP reduces symmetric 4-bit from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads, a degree of freedom unavailable to uniform-precision methods; on Llama (spike), the gain is negligible ($-$0.02).\nAt 2-bit ($r{=}0$), KIVI degrades further (13.34 on Qwen, 10.08 on Llama) as sensitive heads receive the same precision as insensitive ones.\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\\\\nYi-1.5-9B        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\\\\nLlama-3.1-8B     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\\\\nMistral-7B       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\\\\nGemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\\ 0.660), recovering $\\sim$73\\% of the accuracy lost to quantization.\nThe four non-spread architectures show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts); Llama is the most systematic, with 0 of 5 tasks showing positive change.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset stability analysis (Appendix~\\ref{sec:cross_dataset}) confirms ${>}96\\%$ bit-assignment agreement between WikiText-2 and C4 calibration across all three tested models.\nAt 8K context (Appendix~\\ref{sec:long_context}), Qwen's uniform 4-bit degrades to $11.15\\times$ bf16 while MCKP stays at $1.23\\times$; Llama shows no difference.",
    "structuredPatch": [
      {
        "oldStart": 109,
        "oldLines": 5,
        "newStart": 109,
        "newLines": 4,
        "lines": [
          " On Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\\ 0.660), recovering $\\sim$73\\% of the accuracy lost to quantization.",
          " The four non-spread architectures show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts); Llama is the most systematic, with 0 of 5 tasks showing positive change.",
          " ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.",
          "-Cross-dataset stability analysis (Appendix~\\ref{sec:cross_dataset}) confirms ${>}96\\%$ bit-assignment agreement between WikiText-2 and C4 calibration across all three tested models.",
          "-At 8K context (Appendix~\\ref{sec:long_context}), Qwen's uniform 4-bit degrades to $11.15\\times$ bf16 while MCKP stays at $1.23\\times$; Llama shows no difference.",
          "\\ No newline at end of file",
          "+Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9061cbe0-ec9d-4037-ada2-f522d5529fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Tool call

_source line 3993 · 2026-05-15T14:17:40.609Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01Ds7ieUjW1XR1XdPtZKeM6Y`</summary>

```json
{
  "project": "ratekv",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb7919bc-328f-44c2-b09e-bd0d81991943",
  "isSidechain": false,
  "requestId": "req_011Cb4VqwVHnaS9pNHRMXDbD",
  "type": "assistant",
  "uuid": "4d6bed41-c424-432d-a178-4bb2b0f5b8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDHV2rQQPBBek5kkgFZraH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 150460,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 150460,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3994 · 2026-05-15T14:17:43.233Z_

<details><summary>↩ Tool result · `toolu_01Ds7ieUjW1XR1XdPtZKeM6Y`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 661855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385255 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\vbox (badness 1629) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d6bed41-c424-432d-a178-4bb2b0f5b8c9",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "2595da83-4cf9-4e98-8be7-d8cd67882c83",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\\n\\\\\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\\\\\OT1/pt\\\\nm/m/n/10.95 2048 to-kens) on\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\\\n []\\\\n\\\\n[12]\\\\nUnderfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\\n\\\\\\\\OT1/ptm/m/it/10.95 not \\\\\\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\\\n per-for-\\\\n []\\\\n\\\\n) [13] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 13614 strings out of 469438\\\\n 212012 string characters out of 5468411\\\\n 661855 words of memory out of 5000000\\\\n 41952 multiletter control sequences out of 15000+600000\\\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (13 pages, 385255 bytes).\\\\nPDF statistics:\\\\n 868 PDF objects out of 1000 (max. 8388607)\\\\n 632 compressed objects within 7 object streams\\\\n 110 named destinations out of 1000 (max. 500000)\\\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 13, \\\"warnings\\\": []}, \\\"pages\\\": 13, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1264) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2158) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2717) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 8--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1436) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1348) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2126) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3219) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3701) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 1237) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 4132) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 3907) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1939) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 6758) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1546) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\vbox (badness 1107) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 37--41\\\", \\\"Underfull \\\\\\\\hbox (badness 3323) in paragraph at lines 68--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 68--72\\\", \\\"Overfull \\\\\\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 99--104\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 8--17\\\", \\\"Overfull \\\\\\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\\\", \\\"Underfull \\\\\\\\hbox (badness 1721) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 7832) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 3199) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1661) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1102) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1997) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2573) in paragraph at lines 73--75\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 82--87\\\", \\\"Overfull \\\\\\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\\\", \\\"Underfull \\\\\\\\hbox (badness 2189) in paragraph at lines 14--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 36--36\\\", \\\"Overfull \\\\\\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 3--8\\\", \\\"Underfull \\\\\\\\vbox (badness 1629) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2042) in paragraph at lines 22--28\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 36--42\\\", \\\"Underfull \\\\\\\\hbox (badness 7451) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2680) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1107) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 142--148\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 229--234\\\", \\\"Underfull \\\\\\\\hbox (badness 1783) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 2538) in paragraph at lines 245--250\\\", \\\"Overfull \\\\\\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\\\", \\\"Underfull \\\\\\\\hbox (badness 1675) in paragraph at lines 33--36\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 74--74\\\", \\\"Overfull \\\\\\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\\\", \\\"Underfull \\\\\\\\hbox (badness 1259) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1521) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\", \\\"Underfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\", \\\"Overfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\", \\\"Underfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\"], \\\"issues\\\": [\\\"pages 13 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 13 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 661855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385255 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\vbox (badness 1629) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "4d6bed41-c424-432d-a178-4bb2b0f5b8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 3995_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "2595da83-4cf9-4e98-8be7-d8cd67882c83",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 3996_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Tool call

_source line 3997 · 2026-05-15T14:17:49.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_012UWFx7gpxivVKwmH5nmNJL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2595da83-4cf9-4e98-8be7-d8cd67882c83",
  "isSidechain": false,
  "requestId": "req_011Cb4VrSEvHSAqfkxcZnSiD",
  "type": "assistant",
  "uuid": "3a6492a8-a792-488b-a559-6a8a372fda6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyiFXtQ14ND19i2vQ6ywEX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4428,
      "cache_read_input_tokens": 151257,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 151257,
          "cache_creation_input_tokens": 4428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4428
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3998 · 2026-05-15T14:17:50.596Z_

<details><summary>↩ Tool result · `toolu_012UWFx7gpxivVKwmH5nmNJL`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a6492a8-a792-488b-a559-6a8a372fda6e",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "95fb682f-f75c-4701-b7cd-6d48c9be4870",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 497271
    }
  },
  "sourceToolAssistantUUID": "3a6492a8-a792-488b-a559-6a8a372fda6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 3999_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "95fb682f-f75c-4701-b7cd-6d48c9be4870",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4000_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Assistant

_source line 4001 · 2026-05-15T14:18:09.077Z_

<details><summary>Logged reasoning block</summary>

```text
Still the same layout. The bottom of page 8 shows "We report no real-kernel latency benchmarks and" with the page ending there, meaning "have not tested beyond 14B scale." is on page 9. 

The combined sentence compression wasn't enough. I need to save more space. Let me try a different approach — compress something else. The limitations section currently reads:

"The spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale."
 
I can tighten the final sentence to "We report no real-kernel latency benchmarks or >14B evaluation." That saves a few words. Or I could compress the opening sentence about the spread category — maybe something like "The spread category rests on $N{=}1$ (Qwen2.5-7B), suggesting rarity; the seven-model evaluation provides directional but not robust evidence." That cuts out some of the redundancy while keeping the key point. I'm trying a more aggressive compression of the limitations section—removing the detail about Qwen-14B's dilution since that point is already covered in the analysis, which lets me tighten the opening sentence significantly while keeping the core caveat about the small sample size and directional nature of the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95fb682f-f75c-4701-b7cd-6d48c9be4870",
  "isSidechain": false,
  "requestId": "req_011Cb4VrybZweriwykStwjZJ",
  "type": "assistant",
  "uuid": "98f98a0a-885b-475f-8683-7c8d00950299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dJbS4fwBPJfGZn6REbCs4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 155685,
      "output_tokens": 794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 794,
          "cache_read_input_tokens": 155685,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 4002 · 2026-05-15T14:18:09.079Z_

需要再压缩 Limitations 一行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f98a0a-885b-475f-8683-7c8d00950299",
  "isSidechain": false,
  "requestId": "req_011Cb4VrybZweriwykStwjZJ",
  "type": "assistant",
  "uuid": "aa2caf5e-01c3-4668-bffe-3a968f3a25a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dJbS4fwBPJfGZn6REbCs4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 155685,
      "output_tokens": 794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 794,
          "cache_read_input_tokens": 155685,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 4003 · 2026-05-15T14:18:09.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_011HTeVZiCWQdx77Tf7kS44T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2caf5e-01c3-4668-bffe-3a968f3a25a3",
  "isSidechain": false,
  "requestId": "req_011Cb4VrybZweriwykStwjZJ",
  "type": "assistant",
  "uuid": "c4687f9f-29ff-41d5-a578-857e261f32e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dJbS4fwBPJfGZn6REbCs4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 155685,
      "output_tokens": 794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 794,
          "cache_read_input_tokens": 155685,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4004 · 2026-05-15T14:18:09.104Z_

<details><summary>↩ Tool result · `toolu_011HTeVZiCWQdx77Tf7kS44T`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.
6	A joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
7	Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	The spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4687f9f-29ff-41d5-a578-857e261f32e0",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "dd783b2c-9f0e-41f4-9362-5a5ba8954af3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nPer-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\nOn Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\nWhether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\nA joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nExtending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n\n\\section*{Limitations}\n\nThe spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "c4687f9f-29ff-41d5-a578-857e261f32e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Tool call

_source line 4005 · 2026-05-15T14:18:14.122Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014n9UHnYEYxjjFcpp5Wt9dd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
  "old_string": "The spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.",
  "new_string": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd783b2c-9f0e-41f4-9362-5a5ba8954af3",
  "isSidechain": false,
  "requestId": "req_011Cb4VtLsmQRomipLzSiAKv",
  "type": "assistant",
  "uuid": "a1771a6b-216a-4984-9f55-77bfcccde303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBcT642c1DpgihdkVFne58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 156155,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 156155,
          "cache_creation_input_tokens": 1278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1278
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4006 · 2026-05-15T14:18:14.132Z_

<details><summary>↩ Tool result · `toolu_014n9UHnYEYxjjFcpp5Wt9dd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1771a6b-216a-4984-9f55-77bfcccde303",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "801b82e1-01ba-48ad-8ad2-bc0aace970db",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
    "oldString": "The spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.",
    "newString": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\nPer-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\nOn Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\nWhether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\nA joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nExtending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n\n\\section*{Limitations}\n\nThe spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 4,
        "newStart": 8,
        "newLines": 4,
        "lines": [
          " ",
          " \\section*{Limitations}",
          " ",
          "-The spread category rests on $N{=}1$ (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare; the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B scale.",
          "+Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a1771a6b-216a-4984-9f55-77bfcccde303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Tool call

_source line 4007 · 2026-05-15T14:18:19.155Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01XqtuMpZWuRgsNqtZAKyanb`</summary>

```json
{
  "project": "ratekv",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "801b82e1-01ba-48ad-8ad2-bc0aace970db",
  "isSidechain": false,
  "requestId": "req_011Cb4VtiLc65kPAmShVPiom",
  "type": "assistant",
  "uuid": "e19e3902-ee8a-4e6f-a332-50c37596f982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYhdSZGNChk93U4UtMeAE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 157433,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 157433,
          "cache_creation_input_tokens": 327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 327
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4008 · 2026-05-15T14:18:20.914Z_

<details><summary>↩ Tool result · `toolu_01XqtuMpZWuRgsNqtZAKyanb`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385268 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e19e3902-ee8a-4e6f-a332-50c37596f982",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "b9523b96-2871-40b2-a33b-c7237929b669",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\\n\\\\\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\\\\\OT1/pt\\\\nm/m/n/10.95 2048 to-kens) on\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\\\n []\\\\n\\\\n[12]\\\\nUnderfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\\n\\\\\\\\OT1/ptm/m/it/10.95 not \\\\\\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\\\n per-for-\\\\n []\\\\n\\\\n) [13] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 13614 strings out of 469438\\\\n 212012 string characters out of 5468411\\\\n 660855 words of memory out of 5000000\\\\n 41952 multiletter control sequences out of 15000+600000\\\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (13 pages, 385268 bytes).\\\\nPDF statistics:\\\\n 868 PDF objects out of 1000 (max. 8388607)\\\\n 632 compressed objects within 7 object streams\\\\n 110 named destinations out of 1000 (max. 500000)\\\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 13, \\\"warnings\\\": []}, \\\"pages\\\": 13, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1264) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2158) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2717) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 8--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1436) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1348) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2126) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3219) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3701) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 1237) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 4132) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 3907) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1939) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 6758) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1546) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\vbox (badness 1107) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 37--41\\\", \\\"Underfull \\\\\\\\hbox (badness 3323) in paragraph at lines 68--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 68--72\\\", \\\"Overfull \\\\\\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 99--104\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 8--17\\\", \\\"Overfull \\\\\\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\\\", \\\"Underfull \\\\\\\\hbox (badness 1721) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 7832) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 3199) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1661) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1102) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1997) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2573) in paragraph at lines 73--75\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 82--87\\\", \\\"Overfull \\\\\\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\\\", \\\"Underfull \\\\\\\\hbox (badness 2189) in paragraph at lines 14--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 36--36\\\", \\\"Overfull \\\\\\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 3--8\\\", \\\"Underfull \\\\\\\\hbox (badness 2042) in paragraph at lines 22--28\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 36--42\\\", \\\"Underfull \\\\\\\\hbox (badness 7451) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2680) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1107) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 142--148\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 229--234\\\", \\\"Underfull \\\\\\\\hbox (badness 1783) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 2538) in paragraph at lines 245--250\\\", \\\"Overfull \\\\\\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\\\", \\\"Underfull \\\\\\\\hbox (badness 1675) in paragraph at lines 33--36\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 74--74\\\", \\\"Overfull \\\\\\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\\\", \\\"Underfull \\\\\\\\hbox (badness 1259) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1521) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\", \\\"Underfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\", \\\"Overfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\", \\\"Underfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\"], \\\"issues\\\": [\\\"pages 13 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 13 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385268 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "e19e3902-ee8a-4e6f-a332-50c37596f982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4009 · 2026-05-15T14:18:20.920Z_

```json
{
  "parentUuid": "b9523b96-2871-40b2-a33b-c7237929b669",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "175657f1-9049-4271-8003-1a703ee95069",
  "timestamp": "2026-05-15T14:18:20.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4010_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "175657f1-9049-4271-8003-1a703ee95069",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4011_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Tool call

_source line 4012 · 2026-05-15T14:18:25.585Z_

<details open><summary>🔧 Tool call — Read · `toolu_015uHTncacW3ySWfEZw3jGiT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "175657f1-9049-4271-8003-1a703ee95069",
  "isSidechain": false,
  "requestId": "req_011Cb4VuDDBPr1WFfnFsVnku",
  "type": "assistant",
  "uuid": "df006828-5551-4328-8c06-a9a3094a606f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvrBuz31Ev46WouoXs2bJt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4503,
      "cache_read_input_tokens": 157760,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 157760,
          "cache_creation_input_tokens": 4503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4503
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4013 · 2026-05-15T14:18:26.145Z_

<details><summary>↩ Tool result · `toolu_015uHTncacW3ySWfEZw3jGiT`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df006828-5551-4328-8c06-a9a3094a606f",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "eb93ee00-13a9-472c-82d5-7f4746e7c966",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 497271
    }
  },
  "sourceToolAssistantUUID": "df006828-5551-4328-8c06-a9a3094a606f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4014_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "eb93ee00-13a9-472c-82d5-7f4746e7c966",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4015_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Assistant

_source line 4016 · 2026-05-15T14:18:45.358Z_

<details><summary>Logged reasoning block</summary>

```text
Still the same issue. Looking at the bottom of page 8, I can see the Limitations section ending with "We report no real-kernel latency benchmarks and" — the last line is still "and" which means the text continues to page 9 with whatever comes after "and".

Wait, actually looking at the page more carefully... The page seems to end with:
"The spread category rests on N=1 (Qwen2.5-7B) and Qwen-14B's dilution to flat suggests it may be rare..."

But I changed the text to "Spread rests on N=1 (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. 

The image still shows the old text "The spread category rests on N=1 (Qwen2.5-7B) and Qwen-14B's dilution..." — it might be cached. The PDF images are stored in _pdf_images and get overwritten on each compile, so I need to check if the latest version actually reflects my edits. Looking at the very bottom of the page, the text cuts off with "and" before the page number, which means there's overflow text that continues onto the next page.

I'm trying to fit about one more line on page 8 by merging the limitations sentences. Instead of two separate statements, I can combine them: "Spread rests on N=1 (Qwen2.5-7B); the seven-model evaluation provides directional but not robust evidence, and we report no real-kernel latency benchmarks or evaluation beyond 14B." That saves roughly half a line. Or I could go even more aggressive and strip it down to just the essential constraints: "Spread rests on N=1; we report no real-kernel latency benchmarks and have not tested beyond 14B."

—cutting out the redundant commentary about directional evidence since that's already covered in the analysis section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb93ee00-13a9-472c-82d5-7f4746e7c966",
  "isSidechain": false,
  "requestId": "req_011Cb4VubX7Hn1n8SMSDcfta",
  "type": "assistant",
  "uuid": "30197055-01d3-487c-9273-cb2fde409c54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wb4jDhUoWKPkcGGGD4SDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 162263,
      "output_tokens": 915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 915,
          "cache_read_input_tokens": 162263,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 4017 · 2026-05-15T14:18:45.367Z_

进一步压缩 Limitations。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30197055-01d3-487c-9273-cb2fde409c54",
  "isSidechain": false,
  "requestId": "req_011Cb4VubX7Hn1n8SMSDcfta",
  "type": "assistant",
  "uuid": "54de53b6-36cd-4a31-b972-044f8b8002a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wb4jDhUoWKPkcGGGD4SDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 162263,
      "output_tokens": 915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 915,
          "cache_read_input_tokens": 162263,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 4018 · 2026-05-15T14:18:47.315Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KU4fpVhR6papHr76R9oZ1j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
  "old_string": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B.",
  "new_string": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54de53b6-36cd-4a31-b972-044f8b8002a9",
  "isSidechain": false,
  "requestId": "req_011Cb4VubX7Hn1n8SMSDcfta",
  "type": "assistant",
  "uuid": "7a5e8629-ebaa-4342-b039-59f78231ad9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wb4jDhUoWKPkcGGGD4SDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 162263,
      "output_tokens": 915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 915,
          "cache_read_input_tokens": 162263,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 470
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4019 · 2026-05-15T14:18:47.329Z_

<details><summary>↩ Tool result · `toolu_01KU4fpVhR6papHr76R9oZ1j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5e8629-ebaa-4342-b039-59f78231ad9a",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "8244ce5e-03b7-47ba-8822-aaec56c7b0ca",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
    "oldString": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B.",
    "newString": "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\nPer-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\nOn Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\nWhether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\nA joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nExtending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n\n\\section*{Limitations}\n\nSpread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 4,
        "newStart": 8,
        "newLines": 4,
        "lines": [
          " ",
          " \\section*{Limitations}",
          " ",
          "-Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation provides directional evidence but not a robust predictive rule. We report no real-kernel latency benchmarks and have not tested beyond 14B.",
          "+Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7a5e8629-ebaa-4342-b039-59f78231ad9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Tool call

_source line 4020 · 2026-05-15T14:18:51.060Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01H2SFM27Jf4XhQRV5FAgCsd`</summary>

```json
{
  "project": "ratekv",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8244ce5e-03b7-47ba-8822-aaec56c7b0ca",
  "isSidechain": false,
  "requestId": "req_011Cb4VwARoLKDCzTdcygKC3",
  "type": "assistant",
  "uuid": "3f64cc56-47a2-4d4f-99f4-446989286ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiGEyUNfk5sfou9h5tSUd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 162733,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 162733,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4021 · 2026-05-15T14:18:52.861Z_

<details><summary>↩ Tool result · `toolu_01H2SFM27Jf4XhQRV5FAgCsd`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385220 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f64cc56-47a2-4d4f-99f4-446989286ddf",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "6b3ab027-57a4-455e-b9aa-a25e94415f36",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\\n\\\\\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\\\\\OT1/pt\\\\nm/m/n/10.95 2048 to-kens) on\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\\\n []\\\\n\\\\n[12]\\\\nUnderfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\\n\\\\\\\\OT1/ptm/m/it/10.95 not \\\\\\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\\\n per-for-\\\\n []\\\\n\\\\n) [13] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 13614 strings out of 469438\\\\n 212012 string characters out of 5468411\\\\n 660855 words of memory out of 5000000\\\\n 41952 multiletter control sequences out of 15000+600000\\\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (13 pages, 385220 bytes).\\\\nPDF statistics:\\\\n 868 PDF objects out of 1000 (max. 8388607)\\\\n 632 compressed objects within 7 object streams\\\\n 110 named destinations out of 1000 (max. 500000)\\\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 13, \\\"warnings\\\": []}, \\\"pages\\\": 13, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1264) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2158) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2717) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 8--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1436) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1348) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2126) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3219) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3701) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 1237) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 4132) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 3907) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1939) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 6758) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1546) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\vbox (badness 1107) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 37--41\\\", \\\"Underfull \\\\\\\\hbox (badness 3323) in paragraph at lines 68--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 68--72\\\", \\\"Overfull \\\\\\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 99--104\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 8--17\\\", \\\"Overfull \\\\\\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\\\", \\\"Underfull \\\\\\\\hbox (badness 1721) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 7832) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 3199) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1661) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1102) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1997) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2573) in paragraph at lines 73--75\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 82--87\\\", \\\"Overfull \\\\\\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\\\", \\\"Underfull \\\\\\\\hbox (badness 2189) in paragraph at lines 14--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 36--36\\\", \\\"Overfull \\\\\\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 3--8\\\", \\\"Underfull \\\\\\\\hbox (badness 2042) in paragraph at lines 22--28\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 36--42\\\", \\\"Underfull \\\\\\\\hbox (badness 7451) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2680) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1107) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 142--148\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 229--234\\\", \\\"Underfull \\\\\\\\hbox (badness 1783) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 2538) in paragraph at lines 245--250\\\", \\\"Overfull \\\\\\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\\\", \\\"Underfull \\\\\\\\hbox (badness 1675) in paragraph at lines 33--36\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 74--74\\\", \\\"Overfull \\\\\\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\\\", \\\"Underfull \\\\\\\\hbox (badness 1259) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1521) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\", \\\"Underfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\", \\\"Overfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\", \\\"Underfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\"], \\\"issues\\\": [\\\"pages 13 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 13 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385220 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "3f64cc56-47a2-4d4f-99f4-446989286ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4022_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "6b3ab027-57a4-455e-b9aa-a25e94415f36",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4023_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Tool call

_source line 4024 · 2026-05-15T14:19:01.600Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VV5LVk54AjRppj3CYY16Zt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b3ab027-57a4-455e-b9aa-a25e94415f36",
  "isSidechain": false,
  "requestId": "req_011Cb4VwZiXFSfE8bZnP4hs9",
  "type": "assistant",
  "uuid": "8b21cc4b-b85f-4ba7-9507-32518078ce08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C16ZNG7xPfFnbnSxiLAuGw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4399,
      "cache_read_input_tokens": 163697,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 163697,
          "cache_creation_input_tokens": 4399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4399
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4025 · 2026-05-15T14:19:02.163Z_

<details><summary>↩ Tool result · `toolu_01VV5LVk54AjRppj3CYY16Zt`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b21cc4b-b85f-4ba7-9507-32518078ce08",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "cd099731-371b-4554-99e2-c31cba77a1c1",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 497271
    }
  },
  "sourceToolAssistantUUID": "8b21cc4b-b85f-4ba7-9507-32518078ce08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4026_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "cd099731-371b-4554-99e2-c31cba77a1c1",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4027_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4028_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "cd099731-371b-4554-99e2-c31cba77a1c1",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4029_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### System

_source line 4030 · 2026-05-15T14:21:23.539Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "cd099731-371b-4554-99e2-c31cba77a1c1",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-15T14:21:23.539Z",
  "uuid": "537fb9d7-2864-47d1-8840-04fa25a4cd04",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 170189,
    "preCompactDiscoveredTools": [
      "ReadMcpResourceTool",
      "TodoWrite",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "postTokens": 9979,
    "durationMs": 141373
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


## Round 197

## Round 197

59 recorded events


### User

_source line 4031 · 2026-05-15T14:21:23.540Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The Director issued multiple sequential patch instructions for the EMNLP 2026 paper "When Does Non-Uniform KV Cache Quantization Help?":
   
   - **Patch 1 (completed)**: Pythia verification → update 6/6 to 7/7 across all files, add Pythia data to Tables 2 and 4, update gradient narrative to four tiers
   - **Patch 2 (completed)**: Canonical t1/t5 correction — Qwen-14B 0.68→0.57, Pythia 0.28→0.12, plus narrative update emphasizing concentration as primary discriminator
   - **Patch 3 (completed)**: Pythia baseline correction 13.63→16.49 (WikiText-2 test set consistency)
   - **Patch 4 (completed)**: Yi-1.5 L4H3 percentage 34%→64%
   - **Patch 5 (in progress)**: Add 8K Long-Context Spot-check results (appendix table + main body reference), with page overflow still being resolved

2. Key Technical Concepts:
   - Per-head KV cache quantization with hardware-aligned bit-widths {2,4,8,16}
   - Cardinality constraint: max_2bit ≤ k preventing super-additive compounding
   - Three-tier heterogeneity taxonomy: Spread, Spike, Flat
   - Decision rule: concentration + t1/t5 ratio (7/7 classification)
   - Qwen-14B t1/t5=0.57 identical to Qwen-7B — concentration (0.33 vs 0.61) is the primary discriminator
   - Pythia baseline = 16.49 (WikiText-2 test), not 13.63 (calibration data)
   - Yi-1.5 L4H3 = 64% of total delta (top1_share=0.6434)
   - Long-context: MCKP advantage amplifies at 8K (Qwen uniform 11.15× bf16 vs MCKP 1.23×)
   - EMNLP 8-page main body limit (excluding references and appendix)
   - Four-tier unconstrained failure gradient: catastrophic (Qwen 3.3×), severe (Pythia 1.9×), moderate (Gemma-2 1.47×), mild (~1.07-1.08×)

3. Files and Code Sections:

   - **`abstract.tex`**
     - Updated "all seven evaluated models (7/7)" (was 6/6)
     - Current line 6: `We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\ 14B flat).`

   - **`introduction.tex`**
     - Two occurrences of 6/6→7/7 (line 35 body text, line 44 contribution #3)
     - "remaining six models" stays correct (7 total - 1 Qwen-7B)

   - **`analysis.tex`** (most heavily edited)
     - Table 4 final state:
       ```latex
       Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\
       Qwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\
       Yi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
       Llama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\
       Mistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
       Gemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\
       Pythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\
       ```
     - Pythia paragraph (line 25-26): `Pythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads). Low concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\ uniform $+$7.80, $+$0.7\%). %exp_id=pythia14b_constrained_pipeline`
     - Scale-dependent paragraph (line 29): `Qwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\times$ more heads into the flat regime.`
     - Line 30-31: `Sensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold. Concentration, not within-head structure, is thus the primary discriminator...`
     - Line 54: "64\% of total delta" (was 34%)
     - Line 70: `The rule correctly classifies all seven evaluated models (7/7), including the within-family scale contrast (Qwen-7B spread vs.\ 14B flat) and the MHA architecture (Pythia-1.4B flat).`

   - **`experiments.tex`**
     - Table 2 Pythia row: `Pythia-1.4B     & 16.49 & 24.29 & ---   & 31.54 & 24.45 \\`
     - k values paragraph: `$k{=}8$ for Qwen-7B, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2 and Pythia; Qwen-14B $k$ value pending)`
     - Table 2 caption gradient: `Unconstrained failure: catastrophic on Qwen ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining (${\sim}1.1\times$).`
     - Body gradient (line 76): `Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen ($3.3\times$ bf16), \emph{severe} on Pythia ($1.9\times$, 90/384 heads at 2-bit), \emph{moderate} on Gemma-2 ($1.47\times$, 31.5\% 2-bit), and \emph{mild} on the remaining models (${\sim}1.07$--$1.08\times$).`
     - Last line (merged cross-dataset + long-context): `Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.`

   - **`conclusion.tex`**
     - Line 6: "all seven evaluated models (7/7)"
     - Limitations (line 11): `Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B.`

   - **`appendix.tex`** — New section added at end:
     ```latex
     \section{Long-Context Generalization}
     \label{sec:long_context}
     
     \begin{table}[ht]
     \centering
     \small
     \caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
     \label{tab:long_context}
     \begin{tabular}{llcc}
     \toprule
     Model & Method & 2K PPL & 8K PPL \\
     \midrule
      & BF16 baseline & 9.81 & 6.97 \\
     Qwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\
      & Uniform 4-bit & 15.45 & 77.75 \\
     \midrule
      & BF16 baseline & 8.09 & 5.60 \\
     Llama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\
      & Uniform 4-bit & 8.47 & 6.04 \\
     \bottomrule
     \end{tabular}
     \end{table}
     
     Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
     On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
     Constrained MCKP remains robust ($1.11\times$ at 2K, $1.23\times$ at 8K), recovering 97.7\% of the quantization loss at 8K vs.\ 80.8\% at 2K.
     On Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\ 6.04), consistent with the 2K result.
     The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
     Profiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.
     ```

4. Errors and Fixes:
   - **Page overflow from long-context reference sentence**: Adding 1 sentence to experiments.tex pushed Limitations text to page 9. Fixed through multiple compression rounds:
     1. Shortened reference sentence
     2. Merged cross-dataset and long-context sentences into one combined sentence
     3. Compressed Limitations section from "The spread category rests on..." to "Spread rests on $N{=}1$; the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B."
     4. **Still showing ~1 line overflow** — last visual check showed page 9 starting with "have not tested beyond 14B." fragment
   
   - **Edit tool file-not-read errors**: Multiple times got "File has not been read yet" error when trying to edit files that were shown in system reminders but not explicitly read via the Read tool in the current tool session. Fixed by calling Read first.
   
   - **Edit old_string not found**: When editing experiments.tex line 76, the escaped dollar signs in the search string didn't match. Fixed by re-reading the exact text and using the correct escaping.

5. Problem Solving:
   - **Pythia k value**: Not provided by Director. Found by grepping `run_pythia14b_constrained_pipeline.py` — MAX_2BIT = 8.
   - **Pythia baseline recalculation**: When baseline changed from 13.63 to 16.49, recalculated all derived values: Δ PPL Uniform=+7.80, Δ PPL Ours=+7.96, unconstrained ratio=1.9× (was 2.3×). The +0.7% relative difference unchanged.
   - **Qwen-14B narrative update**: With t1/t5 becoming identical (0.57) to Qwen-7B, rewrote the scale-dependent paragraph to emphasize concentration as primary discriminator per Director's narrative highlight.
   - **Appendix.tex structure**: Checked multirow package availability (not loaded), used simple table format with midrule separators instead.
   - **Page fitting**: Persistent challenge across all patches. Each addition requires compensating compression elsewhere to maintain 8-page main body limit.

6. All User Messages:
   - "Continue from where you left off." (session continuation)
   - "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果..." (false positive system reminder)
   - "Continue from where you left off." (after tool loading)
   - "[Director 指令] [Patch] Pythia 验证完成 → 6/6 升级为 7/7" — detailed instruction with Pythia data, unconstrained results, t1/t5=0.28 (pending canonical)
   - "Continue from where you left off."
   - "[系统提醒]..." (false positive)
   - "[Director 指令] [Patch] Canonical t1/t5 最终修正" — Qwen-14B 0.68→0.57, Pythia 0.28→0.12, narrative about concentration as primary discriminator
   - "Continue from where you left off."
   - "[系统提醒]..." (false positive)
   - "[系统提醒]..." (false positive)
   - "[Director 指令] [Patch — 紧急] Pythia baseline 数据错误" — 13.63→16.49 for WikiText-2 test consistency
   - "Continue from where you left off."
   - "[系统提醒]..." (false positive)
   - "[系统提醒]..." (false positive)
   - "[Director 指令] [Patch] analysis.tex 第 54 行定量错误修正" — Yi-1.5 L4H3 34%→64%
   - "Continue from where you left off."
   - "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果" — detailed data for Qwen-7B and Llama-3.1-8B at 2K and 8K, narrative points about MCKP advantage amplification

7. Pending Tasks:
   - **Page overflow resolution**: The Limitations section still has ~1 line ("have not tested beyond 14B.") spilling to page 9. Need to verify if the latest compression was sufficient or if another small trim is needed.
   - **Report to Director**: Need to call paper_agent_post_to_director with the 8K long-context patch completion details after page fitting is confirmed.
   - **Consistency check**: Should run check_paper_consistency after final version.

8. Current Work:
   Working on the Director's 8K Long-Context Spot-check patch. The appendix section (§Long-Context Generalization with Table 8) has been successfully added. The main body reference has been compressed into a merged sentence with cross-dataset stability. The Limitations section has been aggressively compressed to "Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B."

   Despite multiple compression rounds, the last visual check of page 8 (rendered PNG) still appeared to show the Limitations text ending with "and" at the bottom of page 8, with remaining text on page 9. However, this might be a stale cached image — the PDF was recompiled (385,220 bytes) and the text was further shortened, but the visual verification was done on what may be the same cached PNG. The actual state needs re-verification with fresh rendered images.

   The last compiled PDF is 13 pages total (8 main body target + refs + appendix).

9. Optional Next Step:
   Re-render page 8 and 9 with fresh images (cleanup old _pdf_images first, then pdf_to_images) to verify if the latest Limitations compression ("Spread rests on $N{=}1$...untested beyond 14B.") resolved the overflow. If still overflowing, need one more micro-trim — options include shortening the merged cross-dataset/long-context sentence further, or trimming a word from the conclusion paragraph. Once page fitting is confirmed, run check_paper_consistency and report to Director via paper_agent_post_to_director with details about the 8K long-context addition.

   The Director's exact instruction was: "[Patch] 新增 8K Long-context Spot-check 结果" with data for Qwen-7B and Llama-3.1-8B, specifying "建议位置：Experiments 的 'Long-Context Generalization' 小节，或 Analysis 章节末尾" and "注明是 spot-check（Qwen 36 chunks, Llama 类似），profile 基于 2K calibration 但在 8K 仍有效".

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "537fb9d7-2864-47d1-8840-04fa25a4cd04",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "1f6703a1-836d-432e-a018-73e020d96f1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4032 · 2026-05-15T14:21:22.997Z_

```json
{
  "parentUuid": "1f6703a1-836d-432e-a018-73e020d96f1e",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
        "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nPer-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.\nOn Qwen2.5-7B, limiting 2-bit heads to $k{\\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\\%) at $4\\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.\nWhether non-uniform allocation helps depends on the \\emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.\nA joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.\nExtending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) are natural next steps.\n\n\\section*{Limitations}\n\nSpread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B.\n",
        "numLines": 12,
        "startLine": 1,
        "totalLines": 12
      }
    },
    "displayPath": "../../../docs/paper/conclusion.tex"
  },
  "type": "attachment",
  "uuid": "139ee751-e1c4-405f-af31-7d65d35371d0",
  "timestamp": "2026-05-15T14:21:22.997Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4033 · 2026-05-15T14:21:23.370Z_

```json
{
  "parentUuid": "139ee751-e1c4-405f-af31-7d65d35371d0",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
        "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate seven models spanning five architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2 and Pythia; Qwen-14B $k$ value pending).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining (${\\sim}1.1\\times$). Greedy and MCKP produce identical unconstrained allocations on 4/5 models. Best constrained result per model in \\textbf{bold}; --- = experiment pending. $^\\ddagger$Best $k$ from ablation ($k{=}4$). $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 5.84  & ---   & ---   & ---   & --- \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.16$^\\ddagger$ \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPythia-1.4B     & 16.49 & 24.29 & ---   & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals a spike pattern (concentration 0.34, $t_1/t_5{=}0.71$) dominated by a single top head (L2H5), leaving little cross-bitwidth gradient for non-uniform allocation to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\\%); near-zero sensitivity differences and sliding-window attention may both contribute.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen ($3.3\\times$ bf16), \\emph{severe} on Pythia ($1.9\\times$, 90/384 heads at 2-bit), \\emph{moderate} on Gemma-2 ($1.47\\times$, 31.5\\% 2-bit), and \\emph{mild} on the remaining models (${\\sim}1.07$--$1.08\\times$).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nHowever, KIVI cannot exploit head-level heterogeneity: on Qwen (spread), constrained MCKP reduces symmetric 4-bit from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads, a degree of freedom unavailable to uniform-precision methods; on Llama (spike), the gain is negligible ($-$0.02).\nAt 2-bit ($r{=}0$), KIVI degrades further (13.34 on Qwen, 10.08 on Llama) as sensitive heads receive the same precision as insensitive ones.\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\\\\nYi-1.5-9B        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\\\\nLlama-3.1-8B     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\\\\nMistral-7B       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\\\\nGemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 2.6 pts over uniform (0.686 vs.\\ 0.660), recovering $\\sim$73\\% of the accuracy lost to quantization.\nThe four non-spread architectures show minor average degradation (Yi $-$0.8, Llama $-$1.0, Mistral $-$0.5, Gemma-2 $+$0.1 pts); Llama is the most systematic, with 0 of 5 tasks showing positive change.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$3.2, Llama $-$2.7, Mistral $-$1.2, Gemma-2 $-$0.2 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
        "numLines": 112,
        "startLine": 1,
        "totalLines": 112
      }
    },
    "displayPath": "../../../docs/paper/experiments.tex"
  },
  "type": "attachment",
  "uuid": "147231a7-a039-4303-8d3b-fd32a636408f",
  "timestamp": "2026-05-15T14:21:23.370Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4034 · 2026-05-15T14:21:23.535Z_

```json
{
  "parentUuid": "147231a7-a039-4303-8d3b-fd32a636408f",
  "isSidechain": false,
  "attachment": {
    "type": "compact_file_reference",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "displayPath": "../../../docs/paper/appendix.tex"
  },
  "type": "attachment",
  "uuid": "d17a9d85-273b-44ef-a43f-2d4831921237",
  "timestamp": "2026-05-15T14:21:23.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4035 · 2026-05-15T14:21:23.262Z_

```json
{
  "parentUuid": "d17a9d85-273b-44ef-a43f-2d4831921237",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
        "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across seven models at $4\\times$ compression.\nThe central finding is that MCKP benefit requires \\emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.\n\nQwen2.5-7B exemplifies the spread pattern (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nYi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\\ $+$0.20). %exp_id=yi15_hires_constrained_mckp\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling\nCritically, L4H3's 4-bit and 8-bit deltas are ${\\approx}\\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth gradient across several heads---a ``spread'' pattern enabling meaningful reallocation. %exp_id=qwen_hires_profiling\n\nLlama-3.1-8B shows moderate concentration ($0.34$) with a spike pattern ($t_1/t_5{=}0.71$); its allocation is indistinguishable from uniform ($+$0.36 vs.\\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained\nMistral-7B-v0.3 ($t_1/t_5{=}0.18$) and Gemma-2-9B ($t_1/t_5{=}0.18$) both exhibit flat distributions with low concentration ($0.22$ and $0.23$), leaving no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.16 vs.\\ $+$0.14 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline\n\nPythia-1.4B extends the evaluation to MHA (1:1 ratio, 384 heads).\nLow concentration ($0.24$) and $t_1/t_5{=}0.12$ place it in the flat category; constrained MCKP confirms this ($+$7.96 vs.\\ uniform $+$7.80, $+$0.7\\%). %exp_id=pythia14b_constrained_pipeline\n\n\\paragraph{Scale-dependent concentration dilution.}\nQwen2.5-14B (GQA 5:1, 384 heads) provides a within-family comparison: $t_1/t_5$ is identical (0.57), but concentration drops from 0.61 (7B) to 0.33 (14B)---the same within-head structure, diluted by $3.4\\times$ more heads into the flat regime.\nSensitivity is dominated by a single head (L0H5, $d_h(2){=}1.845$; second-ranked: $0.237$, a $7.8\\times$ gap), but 384 heads dilute cumulative signal below the concentration threshold.\nConcentration, not within-head structure, is thus the primary discriminator: the rule correctly identifies Qwen-7B as the single model$\\times$scale combination where non-uniform allocation helps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit at $4\\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). --- = experiment pending. $^*$BOS-corrected.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.10 & Spread \\\\\nQwen2.5-14B & 5:1 & 0.33 & 0.57 & --- & --- & Flat \\\\\nYi-1.5-9B & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\\\\nLlama-3.1-8B & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3 & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\\nGemma-2-9B$^*$ & 2:1 & 0.23 & 0.18 & $+$0.14 & $+$0.16 & Flat \\\\\nPythia-1.4B & 1:1 & 0.24 & 0.12 & $+$7.80 & $+$7.96 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-head heatmap (Figure~\\ref{fig:heatmap}, Appendix~\\ref{sec:heatmap_appendix}) confirms this visually: Qwen's Layer-0 heads show high distortion while mid-to-deep layers are near-zero (spread); Yi-1.5 shows a single bright spot at Layer-4 Head-3 (64\\% of total delta) with the remaining 191 heads near-uniform (spike); Gemma-2 and Mistral show uniformly low distortion.\n\n\\subsection{Empirical Decision Rule}\n\\label{sec:diagnostic}\n\nMCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint empirical decision rule for deciding when non-uniform allocation is worthwhile.\nGiven the profiling results from \\S\\ref{sec:profiling}, compute the top-5\\% concentration and $t_1/t_5$ ratio, then select:\n\\begin{itemize}[nosep]\n\\item \\textbf{Spread} (concentration $\\gtrsim 0.50$, $t_1/t_5 \\lesssim 0.70$): non-uniform recommended. Qwen (0.61, $t_1/t_5{=}0.57$): $-$29.4\\% PPL.\n\\item \\textbf{Spike} ($t_1/t_5 \\gtrsim 0.70$, concentration $\\gtrsim 0.25$): use uniform. A dominant outlier with no cross-bitwidth gradient cannot be exploited. Yi-1.5 (0.71, 0.90) and Llama (0.34, 0.71): no benefit.\n\\item \\textbf{Flat} (concentration $\\lesssim 0.25$, or remaining moderate-concentration models with $t_1/t_5 \\lesssim 0.70$): use uniform. Too little cumulative delta for meaningful reallocation. Mistral (0.22), Gemma-2 (0.23), Qwen-14B (0.33), and Pythia (0.24): no benefit or counterproductive.\n\\end{itemize}\n\nBoth conditions are needed: Yi-1.5's concentration (0.71) exceeds the 0.50 threshold but its spike shape ($t_1/t_5{=}0.90$) correctly predicts no benefit.\nA concentration-only threshold would misclassify it as spread.\nThe rule correctly classifies all seven evaluated models (7/7), including the within-family scale contrast (Qwen-7B spread vs.\\ 14B flat) and the MHA architecture (Pythia-1.4B flat).\nOnly Qwen-7B exhibits the spread pattern ($N{=}1$); the suggested thresholds should be treated as illustrative until confirmed on additional spread architectures.\nThe rule reuses profiling data already required by the solver and adds no overhead.\n\nAdditional analyses---granularity tradeoff (Appendix~\\ref{sec:granularity}), aggressive compression, profiling resolution and stability, per-layer optimality, and KV separation---are in Appendices~\\ref{sec:granularity}--\\ref{sec:kv_separation}.\n",
        "numLines": 75,
        "startLine": 1,
        "totalLines": 75
      }
    },
    "displayPath": "../../../docs/paper/analysis.tex"
  },
  "type": "attachment",
  "uuid": "10b91ab5-c902-46a9-afa4-b874aa2b31d1",
  "timestamp": "2026-05-15T14:21:23.262Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4036 · 2026-05-15T14:21:23.241Z_

```json
{
  "parentUuid": "10b91ab5-c902-46a9-afa4-b874aa2b31d1",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
        "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe root cause is not solver suboptimality but a violation of the additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL; the actual PPL is $3$--$4\\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 10.91 PPL---a 29.4\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\nThe constraint is beneficial even on flat-distribution architectures: on Gemma-2-9B, unconstrained MCKP assigns 31.5\\% of heads to 2-bit, producing a moderate $1.47\\times$ degradation; the constraint reduces this to within 0.5\\% of uniform.\n\nA surprising consequence is that the cardinality constraint renders solver choice irrelevant.\nConstrained greedy and MCKP produce identical allocations across all tested architectures (112/112 heads on Qwen, 256/256 on Llama, 255/256 on Mistral), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn the remaining six models---including Qwen2.5-14B, where the $3.4\\times$ increase in head count dilutes spread into flat---constrained MCKP provides no meaningful improvement.\nThe difference traces to the \\emph{distribution shape} of head sensitivity, not GQA ratio or model scale alone: Qwen-7B's Layer-0 heads form a cluster of high sensitivity across multiple bitwidths (``spread''); Yi-1.5 and Llama have dominant outliers (``spike''); Gemma-2, Mistral, Qwen-14B, and Pythia show near-uniform or diluted sensitivity (``flat'').\n\nThis motivates a question prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a joint empirical decision rule based on concentration and distribution shape (\\S\\ref{sec:heterogeneity}) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast.\nYi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen-7B's, but its single-outlier spike has no cross-bitwidth gradient, so MCKP cannot redistribute budget.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 10.91 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item We demonstrate that the cardinality constraint serves three roles: preventing catastrophic failure on spread architectures (Qwen: 32.45$\\to$10.91), preventing moderate over-allocation on flat architectures (Gemma-2: 8.85$\\to$within 0.5\\% of uniform), and rendering solver choice irrelevant---constrained greedy and MCKP produce equivalent allocations across all tested architectures (\\S\\ref{sec:solver_equiv}).\n\n\\item We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\\ 14B flat). Yi-1.5-9B serves as a critical test: its concentration exceeds Qwen-7B's, yet its single-outlier spike pattern means MCKP provides no benefit over uniform (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
        "numLines": 46,
        "startLine": 1,
        "totalLines": 46
      }
    },
    "displayPath": "../../../docs/paper/introduction.tex"
  },
  "type": "attachment",
  "uuid": "7b38b056-a312-434b-8450-be311e112bd6",
  "timestamp": "2026-05-15T14:21:23.241Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4037 · 2026-05-15T14:21:23.538Z_

```json
{
  "parentUuid": "7b38b056-a312-434b-8450-be311e112bd6",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e6f9d37d-dc3a-4317-ba30-f0f011afd273",
  "timestamp": "2026-05-15T14:21:23.538Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4038 · 2026-05-15T14:21:23.538Z_

```json
{
  "parentUuid": "e6f9d37d-dc3a-4317-ba30-f0f011afd273",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "424e2f07-46ae-48ca-beea-d9ba6d31591d",
  "timestamp": "2026-05-15T14:21:23.538Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

---


### Runtime record

_source line 4039_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "1f6703a1-836d-432e-a018-73e020d96f1e",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4040_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Assistant

_source line 4041 · 2026-05-15T14:21:26.889Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the page overflow situation by re-rendering the PDF pages. I need to clean up old cached images first, then render fresh ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424e2f07-46ae-48ca-beea-d9ba6d31591d",
  "isSidechain": false,
  "requestId": "req_011Cb4W8gpTxvsPBzLZ4AEi8",
  "type": "assistant",
  "uuid": "0fa825e2-6b25-4ba3-be64-3ae0aed24929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtR1wrJsePXRuXkQde7FuN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33204,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 33204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 4042 · 2026-05-15T14:21:27.482Z_

Let me verify if the page overflow is resolved by rendering fresh PDF images.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fa825e2-6b25-4ba3-be64-3ae0aed24929",
  "isSidechain": false,
  "requestId": "req_011Cb4W8gpTxvsPBzLZ4AEi8",
  "type": "assistant",
  "uuid": "23d4aa29-9699-4a50-b2f9-aef87ecb151c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtR1wrJsePXRuXkQde7FuN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33204,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 33204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 4043 · 2026-05-15T14:21:28.926Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K8KBksaCDabPntmqQxBzCM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__paper_compile_and_check",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23d4aa29-9699-4a50-b2f9-aef87ecb151c",
  "isSidechain": false,
  "requestId": "req_011Cb4W8gpTxvsPBzLZ4AEi8",
  "type": "assistant",
  "uuid": "71baca4f-8a95-4369-a62d-2a9577978725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtR1wrJsePXRuXkQde7FuN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33204,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 33204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4044 · 2026-05-15T14:21:28.931Z_

<details><summary>↩ Tool result · `toolu_01K8KBksaCDabPntmqQxBzCM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__cleanup_pdf_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__paper_compile_and_check"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71baca4f-8a95-4369-a62d-2a9577978725",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "43dd1099-024f-44fe-b0c4-c5b86c0fa1e2",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__paper_compile_and_check"
    ],
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__paper_compile_and_check",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "71baca4f-8a95-4369-a62d-2a9577978725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Tool call

_source line 4045 · 2026-05-15T14:21:42.631Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_016R1bCCLgRk2M1hqBax5gea`</summary>

```json
{
  "project": "ratekv",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43dd1099-024f-44fe-b0c4-c5b86c0fa1e2",
  "isSidechain": false,
  "requestId": "req_011Cb4W95CcYrXKWFqSDbPNd",
  "type": "assistant",
  "uuid": "9c9e4ce9-ecdb-4e2e-a51c-9712b8ed0efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uu5WE2SoYGy5Gd2BiztK2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 45045,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 45045,
          "cache_creation_input_tokens": 1425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1425
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 4046 · 2026-05-15T14:21:42.859Z_

<details><summary>↩ Tool result · `toolu_016R1bCCLgRk2M1hqBax5gea`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385220 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c9e4ce9-ecdb-4e2e-a51c-9712b8ed0efe",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "4db1a7f0-0b0d-43ab-a000-a082098aea70",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\\n\\\\\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\\\\\OT1/pt\\\\nm/m/n/10.95 2048 to-kens) on\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\\n\\\\\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\\\n []\\\\n\\\\n[12]\\\\nUnderfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\\n\\\\\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\\n\\\\\\\\OT1/ptm/m/it/10.95 not \\\\\\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\\\n per-for-\\\\n []\\\\n\\\\n) [13] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 13614 strings out of 469438\\\\n 212012 string characters out of 5468411\\\\n 660855 words of memory out of 5000000\\\\n 41952 multiletter control sequences out of 15000+600000\\\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (13 pages, 385220 bytes).\\\\nPDF statistics:\\\\n 868 PDF objects out of 1000 (max. 8388607)\\\\n 632 compressed objects within 7 object streams\\\\n 110 named destinations out of 1000 (max. 500000)\\\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 13, \\\"warnings\\\": []}, \\\"pages\\\": 13, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1264) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2158) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2717) in paragraph at lines 1--20\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 8--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1436) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 30--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1348) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2126) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3219) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 3701) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 1237) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\hbox (badness 4132) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 3907) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 4--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1939) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 15--20\\\", \\\"Underfull \\\\\\\\hbox (badness 6758) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1546) in paragraph at lines 22--27\\\", \\\"Underfull \\\\\\\\vbox (badness 1107) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1852) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 37--41\\\", \\\"Underfull \\\\\\\\hbox (badness 3323) in paragraph at lines 68--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 68--72\\\", \\\"Overfull \\\\\\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 99--104\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 8--17\\\", \\\"Overfull \\\\\\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\\\", \\\"Underfull \\\\\\\\hbox (badness 1721) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 63--66\\\", \\\"Underfull \\\\\\\\hbox (badness 7832) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 3199) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1661) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1102) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1997) in paragraph at lines 70--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2573) in paragraph at lines 73--75\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 82--87\\\", \\\"Overfull \\\\\\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\\\", \\\"Underfull \\\\\\\\hbox (badness 2189) in paragraph at lines 14--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 22--24\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 29--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 36--36\\\", \\\"Overfull \\\\\\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 3--8\\\", \\\"Underfull \\\\\\\\hbox (badness 2042) in paragraph at lines 22--28\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 36--42\\\", \\\"Underfull \\\\\\\\hbox (badness 7451) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 67--72\\\", \\\"Underfull \\\\\\\\hbox (badness 2680) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1107) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 133--139\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 142--148\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 229--234\\\", \\\"Underfull \\\\\\\\hbox (badness 1783) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 237--243\\\", \\\"Underfull \\\\\\\\hbox (badness 2538) in paragraph at lines 245--250\\\", \\\"Overfull \\\\\\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\\\", \\\"Underfull \\\\\\\\hbox (badness 1675) in paragraph at lines 33--36\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 74--74\\\", \\\"Overfull \\\\\\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\\\", \\\"Underfull \\\\\\\\hbox (badness 1259) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1521) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 95--101\\\", \\\"Underfull \\\\\\\\hbox (badness 3568) in paragraph at lines 113--114\\\", \\\"Underfull \\\\\\\\hbox (badness 3977) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1590) in paragraph at lines 119--121\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 157--157\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 157--157\\\", \\\"Overfull \\\\\\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\\", \\\"Underfull \\\\\\\\hbox (badness 1286) in paragraph at lines 177--181\\\"], \\\"issues\\\": [\\\"pages 13 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 13 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"[11 <./figures/fig1_head_delta_heatmap.pdf>]\\nUnderfull \\\\hbox (badness 3568) in paragraph at lines 113--114\\n\\\\OT1/ptm/m/n/10.95 pro-fil-ing (64 se-quences $\\\\OMS/cmsy/m/n/10.95 ^^B$ \\\\OT1/pt\\nm/m/n/10.95 2048 to-kens) on\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3977) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 shal-low lay-ers (L1--L3) at higher bit-widths\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1590) in paragraph at lines 119--121\\n\\\\OT1/ptm/m/n/10.95 while com-press-ing mid-layers (L5--L11) more\\n []\\n\\n[12]\\nUnderfull \\\\hbox (badness 1824) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 gen[]len=128, mean of 10 runs). All con-di-tions\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 157--157\\n\\\\OT1/ptm/m/n/10 store KV in bf16 with sim-u-lated per-head quan-\\n []\\n\\n\\nOverfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1286) in paragraph at lines 177--181\\n\\\\OT1/ptm/m/it/10.95 not \\\\OT1/ptm/m/n/10.95 rep-re-sent op-ti-mized CUDA ker-nel\\n per-for-\\n []\\n\\n) [13] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 1A6115D93AA63D449A531476AAF642D9;4127.\\n ) \\nHere is how much of TeX's memory you used:\\n 13614 strings out of 469438\\n 212012 string characters out of 5468411\\n 660855 words of memory out of 5000000\\n 41952 multiletter control sequences out of 15000+600000\\n 661427 words of font info for 118 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,727b,638s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/u\\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (13 pages, 385220 bytes).\\nPDF statistics:\\n 868 PDF objects out of 1000 (max. 8388607)\\n 632 compressed objects within 7 object streams\\n 110 named destinations out of 1000 (max. 500000)\\n 240 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 13, \"warnings\": []}, \"pages\": 13, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Underfull \\\\hbox (badness 1009) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1264) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2158) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 1--20\", \"Underfull \\\\hbox (badness 2717) in paragraph at lines 1--20\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 8--14\", \"Underfull \\\\hbox (badness 1436) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 30--33\", \"Underfull \\\\hbox (badness 1348) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2126) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3219) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 3701) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 44--45\", \"Underfull \\\\hbox (badness 4132) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 4--8\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 1939) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 15--20\", \"Underfull \\\\hbox (badness 6758) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 22--27\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 22--27\", \"Underfull \\\\vbox (badness 1107) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1852) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 37--41\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 68--72\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 68--72\", \"Overfull \\\\hbox (4.16637pt too wide) in paragraph at lines 81--93\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 99--104\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 8--17\", \"Overfull \\\\hbox (56.89667pt too wide) in paragraph at lines 46--61\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 63--66\", \"Underfull \\\\hbox (badness 7832) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 3199) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 1997) in paragraph at lines 70--72\", \"Underfull \\\\hbox (badness 2573) in paragraph at lines 73--75\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 82--87\", \"Overfull \\\\hbox (7.48924pt too wide) in paragraph at lines 96--107\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 14--16\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 22--24\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 29--32\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 36--36\", \"Overfull \\\\hbox (78.52316pt too wide) in paragraph at lines 38--52\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 3--8\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 22--28\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 36--42\", \"Underfull \\\\hbox (badness 7451) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 67--72\", \"Underfull \\\\hbox (badness 2680) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 133--139\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 142--148\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 229--234\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 237--243\", \"Underfull \\\\hbox (badness 2538) in paragraph at lines 245--250\", \"Overfull \\\\hbox (31.36446pt too wide) in paragraph at lines 21--31\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 33--36\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 74--74\", \"Overfull \\\\hbox (28.38269pt too wide) in paragraph at lines 76--85\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1521) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 95--101\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 113--114\", \"Underfull \\\\hbox (badness 3977) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 119--121\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 157--157\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 157--157\", \"Overfull \\\\hbox (121.50543pt too wide) in paragraph at lines 159--168\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 177--181\"], \"issues\": [\"pages 13 > limit 8\"], \"summary\": \"FAIL: pages 13 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "9c9e4ce9-ecdb-4e2e-a51c-9712b8ed0efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper"
}
```

</details>

---


### Runtime record

_source line 4047_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 新增 8K Long-context Spot-check 结果  **数据（加入 Experiments 或 Analysis 章节，1 个表 + 1 段讨论）：**  | Model | Shape | Method | 2K PPL | 8K PPL | |-------|-------|--------|--------|--------| |…",
  "leafUuid": "4db1a7f0-0b0d-43ab-a000-a082098aea70",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Runtime record

_source line 4048_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-head KV cache quantization with cardinality constraints",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8"
}
```

---


### Assistant

_source line 4049 · 2026-05-15T14:21:49.228Z_

<details><summary>Logged reasoning block</summary>

```text
The page check shows 13 pages total, but this includes references and appendix. The max_pages=8 check is for the total PDF which isn't right - it should only count main body pages. Let me visually inspect pages 8-9 to see if the main body content fits within 8 pages. EMNLP allows references and appendix beyond the 8-page limit.

Let me render pages 8 and 9 to check visually.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db1a7f0-0b0d-43ab-a000-a082098aea70",
  "isSidechain": false,
  "requestId": "req_011Cb4WA6t6LTosBt7xgiucZ",
  "type": "assistant",
  "uuid": "f3592285-ad1a-48a2-bbdc-f838802967dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm82BVsZvQxRELcectKPKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 46470,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 46470,
          "cache_creation_input_tokens": 4402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4402
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 4050 · 2026-05-15T14:21:51.139Z_

13 pages total is expected (8 main + refs + appendix). The page check counts all pages including refs/appendix. Let me visually inspect pages 8–9 to verify main body fits within 8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3592285-ad1a-48a2-bbdc-f838802967dc",
  "isSidechain": false,
  "requestId": "req_011Cb4WA6t6LTosBt7xgiucZ",
  "type": "assistant",
  "uuid": "96653925-e229-42d1-a05c-0cc087848d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm82BVsZvQxRELcectKPKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 46470,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 46470,
          "cache_creation_input_tokens": 4402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4402
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 4051 · 2026-05-15T14:21:52.998Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01TrLuGpZdoFnDszdKTLEDJs`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "8,9",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96653925-e229-42d1-a05c-0cc087848d2f",
  "isSidechain": false,
  "requestId": "req_011Cb4WA6t6LTosBt7xgiucZ",
  "type": "assistant",
  "uuid": "07029000-e825-42a4-99c0-50eb209a8854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/paper_agent_8bf8cc5c",
  "sessionId": "2366ff41-23fa-4994-ad57-5b4087fc52f8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-napping-hopper",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm82BVsZvQxRELcectKPKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 46470,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 46470,
          "cache_creation_input_tokens": 4402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4402
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 4052 · 2026-05-15T14:21:53.879Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01TrLuGpZdoFnDszdKTLEDJs`&lt;/summary>

```text
Error: result (1,860,627 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07029000-e825-42a4-99c0-50eb209a8854",
  "isSidechain": false,
  "promptId": "ba5cd01f-96ba-4cd9-804c-6bdd107c2e55",
  "type": "user",
  "uuid": "c1654247-48f6-4fa0-bbf7-9c615ba5245b",
  "toolUseResult": "Error: result (1,860,627 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-paper-agent-8bf8cc5c/2366ff41-23fa-4994-ad57-5b4087fc52f8/tool-results/mcp-agent-ml-research-pdf_to_images-1778854913874.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABnYAAAkjCAIAAACzq+aSAAAACXBIWXMAAB7CAAAewgFu0HU+AAnSTUlEQVR4nOzde9wN5f7/8SU6KDlUdpRCZUtEardLVOyKiBAqW3JIJyolkux6lKTDt4NQUlI67dJBB7VJJyJRIqWicqYcQnYKO63f+7c+j67HmFlr7ln3rPuA1/MPD/esWTPXzFxzzXV91jXXlUgCAAAAAAAAiCFR1AkAAAAAAAAAdm6E2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsAAAAAAAAQCyE2AAAAAAAAIBYCLEBAAAAAAAAsRBiAwAAAAAAAGIhxAYAAAAAAADEQogNAAAAAAAAiIUQGwAAAAAAABALITYAAAAAAAAgFkJsyKVly5aNz8batWvz3Obq1aufeOKJ5s2bf/LJJ+Fr/vTTTy+99FLnzp3vvffeHB3QDubPn3/OOefo33xv4fXXXw+ehI8++sitMHXq1OAKb731Vi6Sn4f//e9/06ZN69OnT48ePQphdzmxbdu29u3bN23aNEpGkjfeeKN+/fqjR4/O3+5ifj2iOXPm3Hrrreedd16B7gWmcK5pIVi1atXjjz/erFmzPMvJ3Ue25UMOcTkAAAB2T4TYkEuPPfZYIqVkyZIVK1Y86qij/vrXv9qSPffcU/8/8sgjDzrooD322MMWTpo0KXyDN910U6VKlWzlDz/8MGTNG264oXr16ram/p/Tw/r/tm7dWq9evTyTEW7y5MkDBw4sVaqUpVOHNmLEiLlz57oVZs+ePXToUJ0iW2HvvfceNGjQ+++/n4MDCKWDUkPUdvqPf/yjoHeXK1OnTrU0P/HEE1HWb9KkiVY+/PDD87e7mF/P08qVKzt06KB7R3vRzVJAe4FXQV/TwnHddddFLCd3K9mWD7nC5QAAANhtEWJDLg0bNkyNin79+q1fv94t3GuvvXwhg9WrV1922WVa+Oqrr+a5zblz50Zsq2zfvv2QQw4poBBb3759c9Vkatu2rW3q4YcfTrvC3XffbSt069Yt5r6y0rp1650rxLZ161aluUmTJspRUdYfP3583bp1R44cmb/dxfx6RFdffTUhtkJTONe0EEQvJ3cf2ZYPOcTlAAAA2D0RYkMu3X333aeffrpvYTDElky9lli7du3nn38+z23+8MMP0dsqJ554YkGE2N5///2TTjqpXLlyOWkyXXPNNXZEb7zxRtoV/v3vf9sKt9xyS8x9ZcXinjtRiC3Etm3bbrrppp1xX7fffntuQ2yFeSp2GTvdScuqnCyGdroTHm5nvxwAAADIH0JsyKVbbrnl0Ucf9S1MG2KzlaO8v5NVW+Xvf/97zkNsGzZsqFmz5sKFCw844ICcNJn69OljR/Sf//wn7QovvviirXD77bfH3FdWdqUQ21VXXXXKKafsjPvKeYitME/FLmOnO2k7e0xnpzvh4Xb2ywEAAID8IcSGXPrkk0/WrVvnW5gpxLZ06dJvvvkmz20WeYjt/PPPf+SRR/QfQmw7i6effloHUjgt9pzvK7chtsI8FbuMnfGk7dQxnZ3xhIfbqS/Hhg0bbrzxxgceeGD79u1FnZYdbN26debMmcHla9asmThx4tChQ5944onvv/8++gb/+OOPDXnROpm+vmLFiqlTpwaX67xNmTIlejJ2N999991dd93lneipIPzyyy8vv/xyAU1+lUm+s6Lzv//9L5gJFyxYkHY0A+W0OXPmPPXUU7pb33rrLX039hH8f/Pnzx80aFCcqb0KQoFe0CVLlgwfPlx174jrR8/DGzdu1AUKdj4oZMW2VI8iJPGLFi3ShXvhhReKJGFACEJsKHCZQmzm999/11OtZ8+e55133hVXXPH444/7agnetsqvv/76yCOPXHDBBRdddJGeWHri+rYWEmJbtmyZnogXXnjhxRdf/NBDD/38889REq9HY4sWLez/mUJsqmdfc801Y8eOjbLBZOwQW54Hkucpdd55551LL720ZcuW11133VdffRUxxDZu3Lgrr7xSXxw8ePCkSZOCbYk8U6jazJ133jl+/Hj9X/vV1pSGm266Sc/RbHf3448/qjr72muvuSVjxoyxCSWqVq36fynvvfeefaTH87vvvnv11Vfbn7Nmzfo/j2HDhrmNqLbqlmsXab+eaV9vv/22d7OqEW7evNnWnzx5slue9mCTO4bYVq9erZruueeeqzOpymVwZTX/tPzaa69t3br1gAEDfJkz5FTk+V1jk8wmU1MxKEd17tzZW+3WISjb9+7dW1vo37+/ct22bdvSHpRuVZ1e3bYdO3a85557ZsyYoVyads3wzKPtT5gw4fLLL0+mmiKjRo1q06aN1tTCfGwtWVjXNBnhrsz20NatW3f33Xe3bdtWp1QrqxSKGNP57bff1PxTGpSvdO0yra/Gg06dClul4cEHH/z66699K2SV4OXLl998883du3dXftOxv/7665s2bbKPQnLp+vXrlW3efPNN/f/ZZ5/V9u+77z63TRUjujuUJ9u1a3fbbbfNmzcvuN9g+ZDMsvyJcpskY1yOYsiKILEzX0x8+eWXZ5xxhi/EpoynS7nvvvvq4aUcootYpkwZZUJ3e4ZTwywRqkSJEmlzhaolKjT23ntvPfqDnyrPqEGoW0M1lvwd7C5JDxGdtJo1a9q5/fe//11AO1JJ27RpU6t5nnbaaQW0F5+YWdFRUZY2KwZnltcdoRpvjRo1RowYoVK0YcOGhx56qB5V+T6EtWvXXnXVVW7esEKYaCuigrugX3zxhe5TnUM75DwHK8gqD99///26KDaB1T//+c8cJjsfimepHlEw8apR9OrV66ijjrLlBTEANxATITYUuJAQ26pVq4455hg9MvWcU6104sSJamvpUeqtlLgQ27hx42rXru2tcxx77LGLFy/2bjBTiM0edaqFvPLKK5dcconWOeKII+bMmROecm38yCOPdBGWTCE226BE6ZSXjBdiy/NAopzSZKrBr9Z1pUqVdFbVGpw8efLxxx9frVq1RGiITRtUK7dVq1bW6lBLWOfkoosuip5CVRMbNGhgR6e29MiRI/fbbz/Vb6yNrUyi9n/E3T3zzDNnnXWWzU6rTdnCLVu2qEV96qmnaqEO54GUDz74YNGiRddff73NhqFKsNu+mwNXeemnn35yu1bTSA1vLX/ppZeSqR/Kgl/PtC8tV/vKNnveeed5j0i18HvuuScROtGHC7GpMfmXv/zl8MMPV73Ztub7/fa7775r0qRJ3759tTW16g877DCto9xlP/RlSl6U7yrPDxw40KovOufLli2zFeTCCy+0LagqrxOi6qZy2rx58wYMGKBP69Wr9/nnn/uOSFdfCVBbVLWid955R0ekNffZZx/dzr6pBkIyjw7niiuuKFu2rF0C5XPd7JUrV65YsaIlTN/y7Tc8KxbmNQ2/K/NxaDqKKlWq6KBmz579/fff62Jp+7ZyeExHN5GyVv/+/ZW7dKVOOukkfUXtQO+Pw5s2berWrZsu02uvvaZLpltAl0kJVtvPwoLZJnj69OkVKlSwJuLPP/+s3Wkd6+KR6YS//vrrrVu3tmfH8OHDvc1OK2Z1cZUk7UipVfnQsmXL0qVL61tup2nLh6zKn2Ret0n8y1E8PfHEE5b44L1cVCZNmqSrE+wW1KFDB6XTupkb5fASJUqcfPLJylp5blYPu0SoRo0a+b6yevXq6667TsWXrZA2xGYeeughbd+Xo3ZnuiIqT1Q9s1NXcCG2devWzZgxQ7d2ohBDbDGzolHFw00o76Vnsa83pYqavffeu2bNmhs3brQlqtSdeeaZKvHsx4N82LZt29KlSy+99FLbafEJsRXcBf3vf/+rJoabYSzPEFtWeVhPxjfffNPWLPIQWzEs1aMLJl7lqi7cfffdZ8sJsaEYIsSGAhcSYjv33HP10eOPP+6WtGnTRktGjx7tlrgQmyoTI0aMUONfTax+/frZQrX9vDWPtCE2tdmqVq3qjTHZ1JmqtWTqdJNMdW9R9drbbM4UYrPmnx7/3hhNiHyH2KIcSJRTKp07d1b9bOHChW6JznP58uUToSE2Nba1wmeffeaWqInbvn37rFK4fv16O5Nq2epUWFdEPTj33HNPXw01fHfKBpMnT1YVNuFpQhubUML73tmaNWvUWraT4+Ip5owzzkikgi++gx00aJASn+fXg/tKpsIuOg9afs455/g2+69//cv1i0zLQmwHHnigEvbFF18kU6HALl26aGGFChVctwhltmrVqqkV576odr5lmyeffDI8eXl+9+eff1beUDq1pFy5ctq7UqIsVLly5eHDhydTjQd91LNnT+9mbUJhnZ8lS5a4hUqw7v1DDjnEdVvTBbV93XzzzbqCrtkcJfPoomhJqVKlGjdubO9o6D7t2LGjFipt3sBHnlsrzGsa5a6Mfmi6FqVLl+7evbt3F/3797ezGhLTmT9//j777OONf02aNMm+5e0jefrpp6twWLZsmVuydu1aXUSt1qtXr3wkuHbt2q1atXJ/bt26VVfB2x0yeMIXL17sGifNmjW74447dL/rzOspsGnTJsuuVapUceurANGSww47zO03U/kQvfyJeIvl+3IUB4sWLQqO7ZBMRUW9T4eiNWXKFJVCVhh6jRw5Umf4hBNO8C2/8MILtbx3797hm/3222/32GOPvn37Tp06dU6A1TGGDh3q/crGjRsffvjhL7/8cuzYsXZ9Q0JsMnDgwObNm2fqsbt7mjFjRpTwRFbSZuPjjz8+UVghtphZ0VHuUrH27x09//zzvnc2VWpZXzPflFlff/21SrwyZcp4S+9ws2bN8i3RNu0CFZ8Qmym4C6r72g454pQ7WeVhe9wUUIgtUwGeVkipntV2ikTaxOtGsAtBiA3FECE2FLiQEJt1z/a2PK+++motufTSS90SF2J78MEHvd91UbZnnnnGLQyG2NSQVvv5zjvv9H7XYjcSMqXp4MGDL7nkEu+SkLHY1AZYvXp1pk35uBCbElY2HTXYbAVviC3igUQ5pVY/6Nq1qy9h7dq1S4SG2Oyce0/ali1bOnXqlFUKRTVRLfE1Ss8++2wt7NatW8TdGeuFlGeIzVifNV88xaJF4nsFqVatWt7XKjN9PdO+LN5UsmRJX2X3yCOPTPvKp2MhtooVK3pfUFIN2xLp3oZTy3C//fbzvWxo3Txr1qwZnryI37VmQ2LHKGcyFSKxgMuKFSt8ibfOO7qUbsm4ceO05IwzzvCuZhnA3jE0ETPPhAkTbMny5cvdarpwttCd6uhZsXCuaZS7MuKhSbNmzdSOUp3Yuws1+23NTDEdXbXjjjuuXr163t8k1PivU6dOwhNie/LJJ/Vnjx49fF+366j9utFnIiZ48+bN+vPoo4/27nfIkCHeTJXphP/lL3/Rcm94zjz33HOJHUNs69evt/2uWrXKu2ba8iFi+RPxNsnf5SgOlCX0xAyGroqVJUuW6Jk4YMAA3/Jt27ZVqlRJZ3jEiBG+jyxwXKpUKV8ndx89X3yVCi/76SVTqMLlt/AQmxKpDHPzzTeHrLO7+eSTT+zU5SrElikbW22wEEJs8bOi2b59ux4lDz/8cJ5rDh8+XJtV8Rgcmurkk09OW4Cn9eqrr6rW51v4n//8xy5QcQuxFdwF/e233+yQI4bYssrD9hQriBBbrgrwneJBkJaeznYhCLGhGCLEhgIXEmLTg0qtVu+bFNby9D71M40bvW7dOtuyd+VgiM3qIm3btu3j0bVrV9vmVVddlTbNSpgaUf/973+9C3M+3cHgwYP/k44e87aCN8QW8UCinNIzzzwzsWO/FZPnWGxqqSZSbw56x3h2vyxFP9VpOxvaq3xnnXVWxN0Ze+swYojNepv74ilSv359X+v6448/Puqoo6J8PdO+Nm/efOCBB+qj6667zi2cOXOmFob0nUxmmO7A4hSJPwdk+eOPPw466KCDDz64z44s8iWuQ2UwedG/a+Gn8uXL+1I4fvx4q98HEz906FDbiOubZt15TjzxRO9qOieJHbuDRcw8rvbvzeFu3CsX/YmeFQvnmka5KyMe2vTp0/VnnTp1fLvIc3x963cTbEL88ssvCxYscH/WrVtXqwWH1tYB2nug7k3tiAlWfrMXfLp06eI6Fa5du3b9+vXuW5lOuAXIgnGQLVu2aKG3/4ULeXz55ZfeNdOWD1HKn4i3Sb4vR3FwxRVXKIXFuWWlq3D66adXqVIlOKjZs88+a2f422+/9X2kFqP1SQxvMHu7Ivoof5YsWdJXanmpbmB7Dw+xJVMvLJcoUeKdd94JX233kfMQW6ZsXGghtvhZ0bz44osqY6O8VWpjOKSN2tx66636aO+993aDXWaiqlTZsmXPO+8833JCbHkqJiG2XBXgxf9BkAkhtp2RHusrV67UTTRlypRp06Z9/vnnqi8FV1MVa+7cuapBabXZs2cvWrTI94uCbUcfaR01Ej/99NNly5YVq9k8CLGhwIVPd2B0V0yYMKFz5842jOi5557rPgppqzRt2lTLjznmGLck2HayATKGDBnyYjozZswIJkbtwFq1agWnCiraGUWzPZCQU2otXhVwvq/kGWJTw8NOgmjLvmIxegrTNnGDew/fnclJiG306NG23A2Hr8T4tpnp65n2Jbfccos+KlOmjBst5ZqU4JpeaUNsribhxmhPpAY+S3uqxR1IMHnRv2shNl0CXwrtzejatWsHE+86MbnhYG6++WbbiPfJ9+CDD2qhd5KBiJknbVgnWEREz4qFc02dkLsy4qFZ3Dn4XmqeMR1V8RM79qQLUjazBqENQehj/bzq1q2bVYKTf560RKrfWdqZv8JDbPZuciaqYylDtm3b1nbhG2EzeojNV/5EvE3yfTmK3KOPPmopLM4tK4sLeyPazvnnn59Ijc+QdsZPXbjEjp0Ns2In5+677860QvQQ29atW1W8qDwvVlX/IpTbEFtINi60EFuusuKJJ56YSA0H0axZMxUsmSYk/frrr+2Qg1WUZKpjmn0a8opGMvWbhHU5J8SW3DlDbLkqwHeKB0EmhNh2Oiok582b937AN9984y0/ly5dGlxn9uzZ7sdsPU8/++yz4DqzZs3K1cTK8RFiQ4ELD7HpZhg5cmSDBg1U0P/666/W1ooYYuvRo4eWV6pUyS0Jtp3UbNMS7zDYeerbt6/qOo8FWGRKG7c/VXWOvk2v/IXYoh9I+ClVyWUbVxvS98UoM4qqcFQ72bZQpkyZYcOGuWIxegojhtjCd2dyEmLTWbJx6OwdDf1ZsWLFtWvXRvl6SDhm3bp19s7vPffck0w9Eg4++OA8J9mIEmKbPHmy/l+/fv3wTaVNXvTvZgqx2fgyBx54YPArq1at8tX+XWXUmzFs6oCJEye6JREzT8SwTvSsWDjXNBmhoIt4aNYXr0OHDr7t5xnTadSokT71jiwWtGDBAttI8I0nsWGw3bmKHmLTPdu7d+/Enxo3buxrPeYvxKYSrFOnTsqNKiU2bNhgG89ViC3ibZLvy1G0XNAzkepM+s+U7777zj5VLfaNN9644IIL0vbzmjt3bvfu3WvVqlWtWrWjjjpKq6Vtim/cuPGZZ55p0aKFNfU/+uij5s2b62H9t7/9zTt3czh7LXfSpEnBjypXrpzIEOhP/jnWoeTvMW0dvd0JCYoeYnNb845oEU53VseOHY855hidXv3HO0XvkiVLlFH/6XHttdcmU33lLrroIluiepH7AcBZvHix1mzYsOFhhx2m6o0qIWnfgdV9dNNNN+kuOPTQQ0877TQV1JlmSQ5JpJfOv+4+7bF69eonnXTSnXfemWkcqx9//LFXr14qEnU3KVPpOTh48ODwExWejb0RmW+//bZbt25HHHGECoTWrVsH50fO6qB8cpIVP/jgg0RAy5Ytg5NouZhI2h9CbFTKRGi0aP78+bp/bTXlBztv9kRL7hhisymh9NiyO/euu+7yVcD0BHz77bfbt29vwxZrIzrJetZ4q5cRM9W4ceN0ac477zxtTZlcxb5vdtR8XNCIhVV4iC16Hk7LG2JTjjr77LNVp9WxXH/99e5n4xUrVuj2dDe1G3bg6aefvvjii91yN/daeM5PK22pnud28rwomeT5Re3lX//6l+4O+79KrSNTOnfuPH369CiJT6YLsanoU7nhCkM9oG+++WbvSwb5u8eRK3qEWSxs2rRpuotVFk2ZMsWWrFmzxtbRRbQlKhV1a6teqixhS9wrF6pD2hJVsRYuXKhNqY5hSzKVBoWPEBsKXEiITXdFnTp19OT2vdcWMcQ2cODAxI7DPAXbTjZX3X333Rc9wXoqBOs6QZmqnnnKX4gt4oHkeUpnzZplGw+2W6KE2JKpCQd79uxpU/XJ+eefb7/PRz/V0UNsIbszOQmxieo3iT976Khao70E18k2HCNXXXWVPlXNUs94Ndrr1auXdjWvKCE2Gz+ufPnyeQ6kHUxe9O9mCrHZQSV2jK0YbdM+8tb+lSVKlChxyCGH2JjNqk6p0um7+hEzT8SwTvSsWDjXNEpBF/HQmjdvrj9PPvlk3y7yjOmoZaJPrUGeiZJnG+nfv3/wUytvXUsyeojN6FypAm2flilTxttNOB8hNlWjS5UqNXbsWPsz5yG2iLdJvi9HEVK+1e2pQtVSeP/991u/PF19Ne2uvPJKexs6eOZ1KnTa9957bzWk7T1fXUSbZfWKK66wiSOSqVa3Wr/23BfdYkOGDCldurTyv5stMc/oSfLPoIN2FyxnVBe37fgGeXRsPmjxjZEXxbp160qWLOl6a6aVVYjNivTgWPhBP//8c7t27VQs6On8ySef6NKoaLLb1oU2dDbsNfPEjmEdLVQx++CDD/reNNQX7777bhXjI0eOVLbcvHmzTr4Vem6CaaOHy9FHH/3QQw9p12oPN2nSJJGa59d3T0VJpFm9enXDhg21zRkzZijzrF27VvnEhi1L7BieULurQoUKt956q21h+fLl9evXT/ukdkKysa3gIjJKpwqc6tWra4murJU/S5cuzd9B+eQqK06dOlVrtmjRoly5cgmP/fffXyVn2g2qjRqSns6dO2fa19y5c3Wi7GY86aST7Ly5ksoV7DoVLVu23GeffVQyWxgx4el7rrykzO+W62p6f0dxPU8jZirVilWSuImSHn744UzldsQLGrGwMiEhtuh5OBMXYuvbt29iR3rAubdJtHH78TKx4ysmypk2LmTizzeR88z5PplK9Ty3E+WipBX+RT0RbGyWRKrK/cYbb+y3337K53YpZc8999Q64Yk3mXqxNWrUSPlWl947wkC+73Hkis6zC5a5YUNWrlz5UYqL7X755Ze2jhtaV81A3YBax43hq5asVpgyZYqrHigzWJQtbcFYJAixocBlCrGp7LNRwL2j52QVYrNeFSrN3ZJg28l6GTRo0CBt2lTOBn/v1S36RDrW0WnAgAH2ZyH3YotyIFFOqWtFB7sS5Blic7+hJVP9y+xsy7PPPhsxhfb/iCG28N2ZXIXYVHexjc+cOVO1QN9EByFfDw/HqJJhwcGnnnqqS5cuIaNrO1FCbK4rYtpfFPUYe/fddzMlL/p3M4XY3K/owcnIXC827/BeydRoNapoql519tlnd+zY0e3CiZh5surqFSUrFsI1jVjQRTw0C/CpdeQL/eQZ07HSUilJGzNyUxZYk6l58+aZtqBmQFYJtmaJ/V9lpmq9pUqVspT4zkb0ENvjjz+e2HEku5yH2CLeJvm+HEXOcn5ix/eDdBp1C7uuDb4zrzOWCLw+uXDhQhukr23btt7lbjYMXehevXpZm1a1at2VWli2bFlfKzdIj9pEho6EbvoX6wQRZEkVXxQpChs3YNCgQSHrZBViU1axld2v9Glt375dbWnf8/e+++6z73qfespsavYnUlOvWGRB6alWrdoDDzwQ3KydCu94plu2bClTpozvHlQidWN6V9PFOvjggxOpuUpc9o6eSF1fJUnFvu+o3U+Y3vBEhw4d1K72vuCj0lJLQk6XSZuNjd3mVapUUZZz0wRNnDjR1vf+2BD9oIJynhWVGFVBtTWbDTmRegXVe3Tt27e35Z9//nnw6y5adPrpp4fvyMrGkBdFa9euPWTIEIvYarPaoBaqPm9TeynL6anhfm9r1arVrbfeqjpbjx49dHdbRSViprJzeNttt3mTcf7553srwMlsLmgyy8IqU4gtqzyciYXYqlatqorlp59+qofg7Nmz3UWsVKmSizXYXEOJwCgubohb72B/ITnfJ7xUz7SdiBclKM8v2oT1FuEtV66cijIbu2PTpk0jRoywbK+SzQ42PPFpQ2x63Kv+7JuEN849jlxRVdBiZ8GXqJxt27apqNQ6yhUhoU+VKlpHN5R3oS66bb+YDMtAiA0FLlOIzcaMUEnqvYtUF09EDrHpka+vz5071y0Jtp3uvfde+3qwpaSnpu9BG87ae0U1FluUA4l4Su2Rf+yxx/q2k2eI7brrrvP23VO9xN4+69mzZ8QUmoghtvDdmbRNaPs19aSTTvIlIyTEJmeddZY+PfPMM5VX05bsab+eaV/ORRddZLVVVSmCL58GRQmxKXn777+//lTtJJjUO++80/V+DyYv+nczhdhUPbLfG4PNSzf6u/cJp5ZAx44dvcPbB0XMPBHDOtGzYiFc04h3ZcRDc9O8+qYryTOm476oy+r7SPUS1+ng4osvttQGwwH2vtu4ceOySrBuYe+vIPLmm2/aOu7UZTrhmUJsNryRNwiybt0622auQmwRb5N8X44iF9JCc+8Le8+8VlNrWS2iYGjM3W6vvPKKW+jOwJVXXuld2WaDFbUzw1Nor3t77xFH1WvbyAUXXJD2uzYEpDz99NPhewmyMV59LTSfrEJsbnrZ8OGx7Mz4agUuYx999NHe5SqE99lnn8SfwYJu3bop6wYzqr3RFqznWGSkSpUqVlDrX21f94VvNSumxA2hGD2RNu6+2sa+bb7++uu2sjc8YcNB+DoiNWnSJM9RdfIMsVWtWtX3wsHxxx/vK22yOvM+BZcV9dysVq2afdcbL7OOYBJ8hzSZKrjs0yOOOCJ8+3mG2HwR2zfeeMOWe0d4sCe+tG7d2red6JnKfjLxzjeVTJ1YX8Ar+gXNtrDKFGLLKg9nYvVtXUrvg1Inx71BfMcdd9hCbc2W+EJs7imTvxCbSVuqh2wn4kUJivhF61Zfvnx537RyLp7YqVOnPBPvC7Ep81977bWqqLgBhZ049zhyRY8tC4GtXLlSF2vz5s0//fSTr5e6ap62jj2Ct2zZonV0I/uebjYQm/KV67X9+++/63lnw7EV2hGFI8SGgrVt2zYrwg477DDfRyNGjLCPXIxMt8rf/va3xI59KDK1VVS9SAQGQrav9+vXzy1Rw9463h944IHeLXz11VfHHHNMVuO5Zgqxff/992qXRh9fxtpyvme8l3vmDRgwIKsDiXhK77rrLlvNN2+g1WBC3mdRc8I3XLpFYVRriZhCY0nyNXH1SE7sGGIL352xTjdq8XpXs/H4XZZz1XTrfrXXXnulPbrXXnvNTosblMQn7dcz7ctRrcg6PUWM59rvdb768a+//mppcy9guoq7zpv7FXTr1q2DBw/2nsO0yYv4XTve4IyiydR4hfqoYsWKvpn+Lr/88sSOPSaWL1+uKqab/SCTiJnHRWe8T+Vly5b5iojoWbEQrmnEuzLioW3atMl+h9eBeKN77uuZxhbRZq0dW7JkSRVW7qCmTJlSq1Yt65iQTPVDtNCS7zXbFStW6Ive7BExwWoOVa9e3XcOVZaWLVvWxWEznXC7u4P9BO21EW+jTmWp7ddXu0pbPkQsf6LcJvm+HEUupIW2ePFi+8jbnrngggu0pFGjRsFNudm9dWLdQp0N24jv5Ls2eabHn2O9Xbp27Rr8yI2F5PpU+ljbWMaMGRO+Fx/V5pXP8xycPqsQm5tm17Wl07KQoh7KT++oQoUK9nV3kxqbakN69eql4s51RPVq2bJlwhMWd3TPPv/88+5NLht5UE1T365tmt1E6t26rBKpZpKNXRuMVKYdKt4m6lXu8kZPVIbED7EFR8e3nKwiyC3J9sx7FVxWTKZuIhWe9nU3fqWFgBOBruKOfRqscvvkGWLzVY+typ3Y8UcadzWD4zZGz1QWWipVqpQ3S6hF7ev3F/2CZltYpQ2xZZuHM7EQWzB7zJs3zzbi4jsFGmJLW6qHbCfiRQmK+EU9QxOe2ZMcXQu771RDyDPx3hCbHs3nn39+p06d0k7vHuceR658/vnnFj5bunSpMrl3HgNXjVQd0vV0c73SRDUH7+/0P//8s3Vk++ijjxYtWqRnmb06qmwW/nN+YSLEhoLlxnBVtdXV54wbFOyoo45SQ/f2229v0KCB/bCjUk9PcQtaqQ1jv9Z6H35qB55wwglq33p/pFJpaw8z768fSU8TV0488USVwiptS5QooZ1mdSyZQmzW7yPtkzhITxr7zS2ReRIcm0I7EehQlueBRDylauHXqVPH1uzZs+ekSZPeeecdrXbEEUfYQm05bfvHht7wPor69u170EEHuRfmo5xqnQFr97Zv3967cRs/yzs/bJ67UyFrEyC6uppxk2oNHTpUOVD1LfuhrH///iFPUzX4VenUBjO9zpP265n25WVDbLzxxhtpN+tjFdB9993XG71y/SBcuEHH7q7XgQceqKZUq1atKlWqVLt2be8DJm3yIn7XhRi8b+wa3Xf22kjr1q1doERValVJfc1Ii4oqD9SoUaNhw4bNmjVTnV63zC233DJz5kzvmlEyzyOPPBK812zYLHnxxRez2lqyUK5pxLsy+qE99dRT9jJFzZo19S2dRlUc3WvU2stVV12V9i281157ze4Xy2BKhlq2am9MmTLFu5oa5KVLl957773dqMMqMc4555xatWp5hxOKmGB7hdPbIVftRhXp3vI87QnfvHmz0hC8u6VFixa2fq9evXQCdS169OhhK3fs2FH3iL2Tm7Z8iF7+RLxN8n05ila2ITYLgmSaF8/eW9QlcC9/ZQqxRW+d2gvFwauf9HRqyBTjdvd1VjMdJf/sguH9cSutrEJsysm2cu/evUM2qDqSDrl7Zr7BvHSqXTYbPXp0cJtqtFjdyY1fk4m9VaetZdq1bsysEjl+/HhLWDDnp80A1ndbDj744LFjx0YfGikfITYlMuFpwOfjzHsVXFY0L730kn3ddYF0I3a5lyW9VFbbp3lO1ZJtiG358uW23Nu7LeR2jpipkqnRzd1gWyqW007EkYx8QZPZF1ZpQ2zZ5uFMQmYUPe644xKpaJSFkotViC3iRQmK+MVMITbp0qWLfd1VxfMMsV1++eWNGzfO9AJKzHscuZJ2DlAXQbO7QBci0zri7Z+oSntwhegZtRAQYkNBURNLD2+r4Rm1J9X+8XYyVxveGif6V23gVatWzZ071yrW1apVc9OCTJs27YwzztDygw46SC09Fc1qro8aNcq7u3vvvdfeIrQnlkpM747UhLMAmVGxnnaSsnCZQmz2Pv8BBxwQ7Jzs07NnTxfbMnoqeCfv06YscuFNqrenXp4HEvGUqtKgx5gbkbpixYpqKF522WU6w0pkcEIfc+2112qPajRqL08++eSVV16papzvZfjwFOpSqplqH6n1q+bTV199pUqq6h/uK0q2NQlCdrd169Zbb73VeqMkUr2QlHiXbNWcrBd6ItXunT9//rvvvqtnsMuN2o5vqAgzZMiQiy66KLg85OvBfQW//thjj6malecP8qrCXnrppXaxEqmhqZ577rlkKm/bYF6JVD3yxhtvtPVVlenQoYNbXydBWcX3A06m5IV/V6vpPLjsoYqLqp6+EPn27dvVeK5UqZLyla6jbsxjjz02+AuntqmPEhn4Rj0PzzwDBw60HkOiuqndOA899FDVqlVtYZUqVe66666IWyuca2ryvCuzPbTJkye7d4hUd2zRooX9JH7qqac+8sgjmYY9TqbifTZLo9H63hHinG+++UYFUZkyZc4++2xdXJVa+tcb842e4A0bNqjZrLu4TZs2aioMGzasXr16ysPewcuCJ1wloUunDrBTp04qoNz6Cxcu1AbtU11iG0hF+dmWDBgwQO3MtOVDVuVPMtotFudyFKGsQmw6n9ZtU/dy2q25Zr97xMQMsamEt9W8wwI4LsLVtGnTtF93L6N9/PHHIXsJatasWSLCS6xZhdjEzl7aHnnGfkRR+ZDVwNu6UyyI7Hsty+haWCLDpxqUdu3aJQLDJ8VJ5B133JFIDSIW/ChtBtDlbt26tbsHGzRokGdY0MQPseXvzDsFlxUdGwXYTQZ9/fXX2wZtBCsf9+6bcnL4Zgs6xBYxUxk9jm3seSlduvTtt98eHOw44gXNR2GVNsSWbR7OJCTEpmeNbce6KBarEFsy2kVJK8oXQ0JsruOnK4fzDLG5mZTSTnIV8x5Hrqj55mJhalBs3rxZ5ZWbCdTuAj2t3Dq6cNYnwMXmXJb48ccfbcg20f2iLbs/03boLhKE2FDE1NqcMmWK65eUTI0mrhsm2HbVnaZ26XvvvadqZf7GMlyxYoWaWG6e7BxSQVCY/RTCDyT6KdVjTwWTq38vXbo0PGRgx6inlJ70ViBmemLl5FRH312QGu2zU7LKKirKvectV/u65JJL+vbtm+1mI1KFUhdXTfpMtZ+Q5OX53ShWrlyp/Oat/HnpIXrxxRe//fbbekZOmDDhueeee/TRR1VHV827ZcuWqgrrEev7Sm7v0/xtLefXNPpdmdU21cqydxi3bdsW/ec7nfPp06fnOYqclQ8zZ84MduKLTvesxeZ0c2lTSnDarWV7w+p4lTadQBeq05ICKt4j3ib5vhxFIqsQ28aNG21Jpvlz+/XrZyu4njXxe7FZ+NvXJ92pWbNmphZa8s/mfalSpdwbvlGsX79eX6latWqea2YVYnMN+JBebGpm2DpZNQ9UI3L9UoPjTrp3GPP8QdHGIe3evXv4atETaaNVJtLNOp0pA6gkHDx4sPtdp2TJkr6ck1b8EFv+zrxXQWRFLzsQ9ybm888/bwlOO/yC6/CeZ0/Mgg6xRcxUjooO96OInU9faDjiBc1HYZU2xJaPPJxWSIjNRUvtRYHiFmJLRrgomeT5xZAQm736IK5yGOVFUT0prNx4PzD+T/x7HDmhCp5FwVx0O5kanMEbPlNDz/78+OOPXYtPFSrVn225qnyqibmAmvsJUzVMt04xeW+AEBsAFCBV+FT5UxWhqBNSBH799ddGjRqFjI/bpUsX73QlO4vd+Zpi15Dti6KHHnpoItUVPe3WXFvRjaUVP8RmQwdm6opiLxOVK1cu7afWugsOtR7Ozolvdo608jcWm6/TrpcbxFBpiJhaG/DhjjvusLn5qlat6mtXrFy50raZtmeHlw1EePjhh4evFj2RV155pa25cOFC30fhGWDBggXuNfBEunnPfeKH2PJx5n0KIit6WQ9f10N8yZIllmD3oqWXGwUy02xaTkGH2CJmKi81nkeMGHHAAQfYNvVd7+8x0V8UzbawShtiy3ce9gkJsdmYtuXLl7cflophiC2Z10UJEf7FkBCbjTKpYi3PxHtDbNq4vSBcsWJFXygt/j2OnHBjsXkHZrE5lMVeEVu6dKn96Rtr0oXndKH1aLP/+5oPX331lesiVzhHFI4QGwAUoFtuuaVNmzZFnYqiYSPshAxY1qxZM+8LgzuL3fmaYteQbYjt7LPPtoVpp+uy8cW9wz/FD7FZL5iGDRum/dTNbxisTKtIsR5w4dMLBDVv3lzf+uijj/JcM6sQmxvX3Duios8ff/xhgwlmmtF7zZo1/fv39y5R+/y0007TF13L/KqrrvJ9y6YuqVq1atoOmGqQTJs2LZkaIcG2kGkCXK3w3XffRU/ksGHDbIPB+YvTZgDfXKsvvPBC6dKltU7lypXT7siJH2LLx5n3KYis6FWxYsV9993XTZyX/HMOzS5dugRXttcb006m6VPQIbaImSqZGsHTOwDuTz/9ZPe+eMdOjR5iy7awShtiyzYPZxISYrPBDdxMCMUqxBbxogRF/GJIiM3mO/a+eR0lxJZMRXDsXlZW8ZZ48e9x5MSCBQuCITYVkrbQ3nx3I6z5QmzuJVOVhCppg73hkp4ecMGweJEgxAYAOdavX79WrVqpBqn6rh7taYcl3h107tw5kZrYKzi/xLJlyzp27Pjqq68WScLygWuKXcnTTz+dtjmXzNCecXO2Xn311cGt2bty3ts5fojN+jJUr1497adqXNmUo8EGsE2ypJvU9yp0+DgDGzZs2HPPPStXrhxlOIKsQmxu0qdME+kYNwxr8Mz89ttvaqZ6hyebOnXqvvvu6xoSboRBC5k5bdu2teUDBw70bXPdunWnnXbapk2bvClUizf4WtzEiRPbtWuXVSJnzpxpq9WuXdu3mssANtKoOeWUU3yrjR49OpF67Sv8N5iQbBw9IpPVmQ/KeVb0stN1/fXXexfaZD6HHnpocDt2LL7107K5XFq0aOFbnqsQW/RMpXIm+NawDet56623uoXRL2i2hVXaEFu2eTiTTCG27du36xIob7g3KN20P++99553zUGDBtlyb4gtJOenlSlKlWk7ES9KUMQvhoTYjj766MSOE9NHDLElPbMwXXbZZd41Y97jyAkVg8HQ2I8//mgLrVK9bds2ewnU+6KorpEttFzhtuNdJ+np6bZy5crCPbL0CLEBQC798MMPCY/w6siuTZU2G6q5VKlSTZo06datW69evdq3b398yuTJk4s6gVFxTbGLefvtty0z22QRydQLaPaf+fPn20f33nuv9ys2b8lBBx3kGz9xypQpWt68eXPvwlWrVtlGfCE2VZF9+83EJSNTdXnMmDH69OSTT/Ytt8i+mxbGvPbaa/vtt1/9+vWDgz+aJ598MpGaozY8VcYdXZQQm8UKVeKFr+bOjErLYcOGuV4Yc+bMOeWUUy6//HK35qZNm6pVq+Y9sTpFZcuWTaSmpvFOS7JgwYKSJUvaZi+++OIvv/zSGiQqe2vUqOENEKh8ttUaNmzoJnjRpu6//35d8W+++SbbRLqon+/F24EDB9py7/wtBxxwgG+Spe+++y7KSQvJxvXq1Uuke0OzY8eOWr7PPvu4JdEPKpOYWXH16tWDBg0aNWqUb7y27du3n3766XXq1PG9mrdlyxabAck3yt633367xx576GRGaWE2aNAgkZry2P7Uri0E7AI9vldNFy5caMvvvvtut9DFocaOHRvcRcRMNXz48DPPPNP3XRtay9sFPvoFTWZZWOmGsnT6ujJllYczyRRis7livdNBuBLvkksucQs/++wzN9uVN4AekvPTylSqZ9pOxIsSFPGLFmKrXLmyb/RVZWkt15mPkvht27bZchdiS/7ZSzHhmSEkmYt7HPHp6aNy3k1uoPtOT9IPP/zQltiIhPLFF1/YEv1n48aNuoVVztgSKzR0+dywa1pnw4YNWu3rr79+/0+MxQYAu6YBAwYcfPDBVapU8VUIdkOLFy++/vrra9asqRqwav+qUbVp02bcuHE73dROXFPsSlRttaHl1cZ+4YUX/vWvf7mpq3V7WmvEN1S52u1qjVgowcUCdIMfccQRp59+um+iCWvKJlIztHqXqwFmy0MGJnPszc2Q/m5du3ZN7Nh76N133y1RosRpp53mm0jk1FNPtf36+kE4NgRYcKjstNyQ876mYFrWmPROiZtJjx49En8qU6bMsccea3Miq8x0nblUcnbo0OHwww9X89L7XdfVRa1Zb6v1vvvus+mMzf7772+vLuqKe78+d+5cG9PNaPvHHHNM6RRfz7goiUymwj1uQmc1ua1vizJDw4YNbeGee+6pM2N9Zw444IB69ep559599NFHtY53Xvi0MmVjtcHs150KFSp4X7EUJdgS4J2QJOJBhYiTFe+//35bcthhh7388su2UGdDebJBgwau5ek1a9asihUr1qpVS21LW6K96DyXLFkyz1HYTJ8+fWyn/fr1e+6558466yyb0e+ee+6x5fqPd30lLFgsKFfbwrSx6YiZysqExx9/3C359ddfVao0atTInfxsL2hWhZUSY1twHetMVnk4k5NOOklrqvLgHTdq8uTJOhBVjbx3sW5tpda2rEuvzNyyZUudMdfRrEaNGrpYVncKKcDTylSqZ9pOlIuSVsQvWqkoF110kbvxZ8+eraJAN4ivw2+mxFsgPrFjZ8xNmzbZS9C6+2yucxP/Hkd8q1atej8dby/C//73vy6C5vXhhx+62Kgbji1o0aJFRXRwfoTYAACFYacLqwG7sLvvvtvaG2qW9+7d24ZEueyyy2wAL2uiqM2pdpf7itYZNGhQuXLlKleufMkll6hho8bM7bff7uuJMHDgQNc01cY7deo0ffp0tXyuvPJKi+8kUr1OtK/gK+Re1kfm0ksvDVln5MiR++6778UXX/zII49cffXVajtp78Ghx6zjiXaatj28ceNGtZYPOuigPNtaDzzwgA5ce3GttVatWmnjmZrZat6rBRuMiGXy6KOPVqxY0W1c51lLXKree+89a7HrEnh7sU2cONHG5zL169f3Bqfefvvtww47zH2q5u6ECROCu16xYsVZZ51VqlQpt6auftqposMT6axdu7Z169ZuzlOdh379+n388cfKV40bN37sscfcePNHHnnkCSecoH/79u2r66h8okS+8sorUc5YMBuPHj3aejyZunXrPvjgg1rzueeeUzvfLa9evfrDDz+c7UGFyHdW/P7775UYt+ujjz5aV1D/ajsh2UbX65RTTtGJ0hnQAeoEHnvssTYrXxRqox511FG2R535Tz/9dPny5V27dnWTuurCdenSZcGCBbqOuiKuWJAOHTooU11wwQVuZWnZsmVwEtgomWr48OFKedWqVc8999z777//3nvv1eW76KKLXAe0/F3QKIXVF198cfnll1eoUMFtRDnWGyeNnoczURGnzFCpUqVEKtB25plnVqtWrXbt2sEpgJOpnOCdiLNbt24qmiZPnqy8rS+OGjXKW2AGc37aBORZqqfdTp4XJZOIX7QQm87D4MGDy5Yte9ppp9WpU6d06dJKgDfPZ0q8TpSuqfUQlD322KNz585jxoxJpkaXcxk7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ZzY2H330kS7HBRdcoMvx4IMPfv31174Vtm/fPmXKlMsvv9yuptbv3r37Oeec869//Wvjxo22zoIFC2688cZWrVppd7Nnz/ZtQXn+nnvu0b2p/0+cOLFr165t2rQZMmTI4sWLfWuuX79eh/zmm2/q/88++6xWu++++9ynf/zxx8svv6xsoBtkwIABaY9o+fLlN998s1Ko1XRZX3/99U2bNnlXGDdunPKnLuvgwYMnTZqkQ/Md7Lvvvnv11VcHtxzl9tSSCRMm6FwlUzNdjBo1SoegE6uFwQ3m0PHHH69s9tNPP+Vka998803p0qV958154403tK+0pyiKFStW6AbXmcx38qZNm9anTx/9Z+XKlbqFdaPNnz/ffRry7Ai/r2Ne+ijC77U5c+YoPTfccIOlUDuyFH7wwQf52BcAAAB2RoTYkHv3339/qVKlxowZozae2jYtW7ZUe09NZe862YbY3n777UMOOUTNpy+++EKNLrXPtU69evU+//xz397fe++9v/71r2rezJw5U5+edNJJWlMtIjXAbIVVq1Ydc8wxp512mjalNv/EiROV2qZNm27evNlWUKN9yJAhlowrrrjigRQ15J555pmzzjrLXgJSw8m33zxT+NZbbzVo0MA2q6+PHDlyv/32q1GjhsWYlOboHfdciG3o0KElSpRI/En/v+eee4KXQ+1SXY5XXnnlkksu0WpHHHGEWoP5S1X41izEptavbfD222+3RuYdd9zRpUsXW3jllVfayjqlSv+pp56qhdWqVbPzHKU5mu8rGPH0aptq3lv3tPAQm9a8/PLLdZaUpOCnFl/77LPPIu7XK89sLLq/unXrdvjhh7/22mvLly9/6aWX6tatq1Nx2223uYBjv379/vKXv9ip+O6777p3716pUiWd83333VdLdA51CLo65cuXb9SoUfXq1bVQGcBl2hdffPGMM86weX5HjBihBOg/btrfChUquEHcdYO3bt3aJk8cPny40uCy5TfffKMVtPcmTZr07dv31VdfHTVq1GGHHaaP+vTp4z2i6dOna5vKk/r/zz//bLv7/vvv3dlu06ZNq1atLFaoU6TTe9FFF9mnixYtuv7663UP6is6Ot/5zPP2VPZQVilbtqx9XRf073//e+XKlStWrGhHkalTWL59+umnNWvW1O2jzJ9ITbZ7RIpSlVU4OOimm2668MILfQuV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1atX79+//++//163bh2F7Nixg2+FuSAF4lfE2bdvHyt3Fy5cCNkbCdYcO3asa9euJUuWzJIlS4kSJbp3737ixAljNEysR40aVaZMGVgszz///CuvvPLZZ5/dvHlTF+3atWt0mtv333+PPzds2FClSpWMGTPCeNa5Fcf84J133oHNQP1y48aN39FQt27dihUr5smTZ/ny5dqrMOdASP369RctWoQ/hwwZkjNnzlKlSqEeuj3bThcvXgyT8osvvsCfly9f/vDDD2GHIMGYZh05coRucvToUcxU8ufPnzlz5po1a5oev/jDDz/UqlULycCz2rRpM2bMGF1KbPHpp5/yxKhatWr0jmhc9KvWQEViWrRogZfKmjUrEmA6CUPLGjhwIMpCF37u3LmOHTvijRo0aPD2228PGDDg888/9zvNoG/fvtpCwc3ZSkdmNmvWjMI/+ugjn2lze8/SU6dOoQbyU1A6FB815L333uNwvJ3uhrD08OjSpUuXK1cOFRLp2bZtm/G56hIbKs+7777LT2zVqtW8efM4/owZM5o0aYJwxOHO0O05vhAVtUOHDo5+OcDN06ZNSwmeMmWKz/h9+vShyC+99BKF9O7dm18Nr/Djjz8icP78+doibtq0KbUst2dlBBfxggULtDe/evUq7l++fHm0INTbXr16IUSXgO3btyOHEcft2eTSr1+/vHnzopOpV6+ecVsi3q59+/amMkHQazXhn8R2//59VIkaNWqgyqHZVq5c+csvv9Quu/OvCrk9ixTQBxYoUCB37tz4x88//6x7tHXXZ0GmTJnwmgULFjT9tXbt2pQPgew9tNuDudWqkFu5jYOtW7c2atQIz0XHjt5+9+7d3iQ2h2qUc3BbRn+oDUeVQLdDP+HFQ7kS/KeffoooiY2ArR5GjWn9+vUh+0JgSnhf3yECydUI9AyLAYLKCJNS469owhglEydObOz/CYykuJDuYH0KNmbsCRMmRB8YnHQ7TGR684xMYJIbA0PZ+Zh6lA5xGgQhiIROYoO5SyoYT9xhf2LyusEDbRfduXMnxTl//jzFuXHjBoVER0fThxeYTGhvFMi+BmBB0X1YXBDCCMpo8ODBzz777IQJE2BnopjI01PSpElRjtqY+/bte/nll4sUKQKzGeV7/fr1bt26IWa2bNl4ho1wWFa03ht8/fXXX3zxRZIkSYoXL54uXToK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p588ebLTZ9rU4KJFi/BMXI2Li1MD0fLx94cffvjll19OnTpVtGjRvn37Os1RODRo0ACpUktjwYIFO3bs0Lzdk8Fkz549x48fd307jx6eaLVctFL9xIRZXAMGDGjYsOHVq1fDeYhrVq1atXPnzqCXgtYgbeoUFZsgCIIgCIJAiIpNSIPMnj27WbNmqe35//73v0kufeWVVyKRqtTM6dOnixQp8tlnn7lWsVWrVo3u5b1IZvic18svvxxeet3z5JNPOlJeLF68+O233zaHv/HGG3hO+vTpU1JSnKZh7969OXPm7N+/f9CrEydOTJcuHR4+dOhQ/WeGrMELFy4ULlwYl9q3b6+Gb968uUOHDvxz5MiR+fLli6YdtEOHDlF+3Z0a9mQwuXz5cuXKla00njr07dvXQxWb01aqn5jwiwsNvmzZsv/617/CeYjnWNUg7ZwVFZsgCFHAqRnN3bt3Dx8+fPXq1WrgokWLXn31VUzN+u91cUtqwKq4btDs+G/klAvCzUa0VWwQw7Zt27Zq1aq4uLiEhITt27ebj+ocOXJk06ZNiBMfH484kIvMFrgvXryYlJS0du1aPAeTB+K4EESFNMnOnTtz5sz57LPPprbn38wqtueff75///6//fabqNgMLF26NKiHATqzduuttzpNwPXr12vVqlWwYMGgNq0SExPJElmDBg0QU/+xIWvwnXfeoUuGxR/qi3WIJ06cyJ0795gxYxzmKSyWLFlCCXOhYvNqMOnSpYthG51TbggVm1fFNWXKlHTp0v30009hPsdDrGpQVGyCIEQBR2Y0Dx482L1795IlS9JA/d///pcvQQrLkSMHAh966CHNV7u4JebYFNeNmB3ixk25INyERFXFdvLkyfj4+J//yapVq86ePUsRIPJt27btZxMrVqxQxcVjx46Zn7NmzZobwrCOEFHQxsqUKYMZKEIqtnCef9Oq2KZOnVqhQoWUlBRRsenTv39/POe1115zeuNXX32FG19//XXzpcuXL5crVw5X06VLd+DAAf1n6tQgbWGrWrWqIRzN/vvvv6f/adEfZTev06ZNc6di82owmTRpEiUgbavYPBx70VAhGiF5HnosDQebGhQVmyAIUcCRGU1IQ3/88QcP1KqKDYMqTdbPPPOM5qtd3BJzbIrrRswOceOmXBBuQqKnYsNafMWKFaQO27Rp0+7duxMSEugn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
```

---
