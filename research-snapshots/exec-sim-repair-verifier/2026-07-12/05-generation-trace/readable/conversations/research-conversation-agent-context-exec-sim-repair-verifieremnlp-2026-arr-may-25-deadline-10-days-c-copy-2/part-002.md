# Research conversation: <agent_context> 项目：exec-sim-repair-verifier。EMNLP 2026 ARR May 25 deadline (10 days)。论文题目：Classification Scales Where Ge — Part 2 of 2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-agent-context-exec-sim-repair-verifieremnlp-2026-arr-may-25-deadline-10-days-c-copy-2.md) · [Structured JSON](../../../sessions/91/9127a85d529c6747991c.json)

## Round 1

### Tool call

_source line 121 · 2026-05-15T14:46:55.524Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QihmPVQVe2SRxyLo3KXkyu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex",
  "content": "% Experiments draft — generated 2026-05-15, numbers from registry\n% NOTE: All numbers cross-checked against experiment registry.\n% exp_id references provided for key claims.\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the three formulations defined in \\S\\ref{sec:method} across two complexity levels---function-level and repository-level---to test the prediction that classification gains an increasing advantage over generation as code complexity grows.\n\n\\subsection{Experimental Setup}\n\\label{ssec:setup}\n\n\\paragraph{Function-Level Data.}\nWe construct a function-level benchmark from HumanEval~\\citep{chen2021humaneval} and MBPP~\\citep{austin2021mbpp} by applying five categories of systematic mutations---\\texttt{off\\_by\\_one}, \\texttt{operator\\_swap}, \\texttt{variable\\_swap}, \\texttt{return\\_value}, and \\texttt{boundary\\_removal}---to correct solutions, yielding 19,076 (code, test, label) triples.\nWe split by problem identity: 15,290 train / 1,896 validation / 1,890 test, with zero problem overlap between splits.\nThe test set is approximately class-balanced (51.7\\% \\textsc{Pass}, 48.3\\% \\textsc{Fail}).\n\n\\paragraph{Repo-Level Data.}\nWe derive a per-test verification dataset from SWE-bench Verified~\\citep{jimenez2024swebench} by pairing each candidate patch with individual test cases and their ground-truth outcomes.\nThe resulting dataset contains approximately 70K training samples, 9,335 validation samples, and 9,784 test samples.\nThe test set is class-imbalanced (72.96\\% \\textsc{Pass}); we report the majority-class baseline throughout.\nValidation and test splits have zero problem overlap and exhibit a mutation-type composition shift (operator\\_swap: 19.1\\% val $\\to$ 34.3\\% test), which we discuss in \\S\\ref{ssec:analysis}.\n\n\\paragraph{Models and Training.}\nAll models use Qwen3~\\citep{qwen2025qwen3} as the base architecture with LoRA adaptation~\\citep{hu2022lora} (rank$=$16, $\\alpha$$=$32).\nWe train Qwen3-4B and Qwen3-8B variants for CLS, CWM, and TRAJ formulations.\nTraining uses AdamW with learning rate $2 \\times 10^{-4}$ (function-level) or $5 \\times 10^{-5}$ (repo-level), weight decay 0.01, warmup ratio 0.05, batch size 32 (effective), and 3 epochs.\nFunction-level experiments use seeds 42, 123, 456, 789, and 0 (five seeds); 8B scaling experiments use seeds 42, 123, and 456 (three matched pairs).\nSeeds 42/123/456 use bfloat16 precision; seeds 789 and 0 use NF4 quantization due to hardware constraints.\\footnote{NF4 seeds appear only in 4B paired comparisons (\\S\\ref{ssec:equivalence}), where the within-seed paired design controls for quantization effects.}\n\n\\paragraph{Checkpoint Selection.}\nAll reported results use validation-selected checkpoints: we sweep all saved checkpoints on the validation split and select the one with highest accuracy, then evaluate on the held-out test split exactly once.\n\n\\paragraph{Statistical Methods.}\nWe report seed-level means $\\pm$ sample standard deviations.\nFor the CLS--CWM comparison, we use seed-paired bootstrap (10,000 resamples) with one-sided tests.\nFor CLS--TRAJ equivalence, we apply the two one-sided tests (TOST) procedure~\\citep{schuirmann1987tost} with a pre-specified $\\pm$2 percentage-point (pp) equivalence margin.\nFor repo-level results with clustered per-test predictions, we use clustered bootstrap with 114 problem-level clusters and 10,000 resamples.\nWe report the intra-cluster correlation coefficient (ICC) and design effect (DEFF) to characterize block-correlation structure.\n\n\n\\subsection{Function-Level Results}\n\\label{ssec:func_results}\n\n% exp_id: multi-seed-core, cwm-baseline, cwm-seed{123,456,789,0},\n%         cls-seed{789,0}, traj-level-{finetuned,seed123,seed456,seed789,seed0},\n%         llm-judge-8b-zeroshot, llm-judge-32b-zeroshot\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Accuracy (\\%)} & \\textbf{Seeds} \\\\\n\\midrule\nCLS & Qwen3-4B & 88.43 $\\pm$ 0.78 & 5 \\\\\nCWM & Qwen3-4B & 87.19 $\\pm$ 0.37 & 5 \\\\\nTRAJ & Qwen3-4B & 86.30 $\\pm$ 0.97 & 5 \\\\\n\\midrule\nZS Judge & Qwen3-8B & 64.40 & 1 \\\\\nZS Judge & Qwen3-32B\\textsuperscript{\\textdagger} & 71.69 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Function-level per-test verification accuracy on HumanEval+MBPP mutants ($n$$=$$1{,}890$). CLS, CWM, and TRAJ are fine-tuned with LoRA; ZS Judge uses zero-shot prompting. \\textsuperscript{\\textdagger}NF4 quantization. All three fine-tuned formulations achieve $>$86\\% accuracy, substantially outperforming zero-shot baselines.}\n\\label{tab:func_results}\n\\end{table}\n\nTable~\\ref{tab:func_results} presents function-level results.\nAll three fine-tuned formulations---CLS, CWM, and TRAJ---achieve strong accuracy in the 86--89\\% range, with CLS leading at 88.43\\%.\n\n\\paragraph{CLS vs.\\ CWM.}\nCLS outperforms CWM by 1.24pp across five matched seeds (bootstrap 95\\% CI: [0.46, 2.04], one-sided $p = 0.025$).\nThe gap is consistent: CLS achieves higher accuracy in all five seed pairs, with per-seed gaps ranging from 0.32pp (seed 42) to 2.33pp (seed 789).\nWhile statistically significant, this gap is modest---both formulations achieve near-equivalent accuracy on function-level code where execution outputs are short and CWM failure modes rarely activate.\n\n\\paragraph{Zero-shot baselines.}\nZero-shot LLM-as-judge performance lags far behind fine-tuned models: Qwen3-8B achieves only 64.40\\% and Qwen3-32B (NF4) reaches 71.69\\%, both exhibiting a systematic bias toward predicting \\textsc{Fail} (fail recall $>$92\\%, pass recall $<$53\\%).\nThe 16.7pp gap between the 32B zero-shot model and the fine-tuned 4B CLS confirms that task-specific fine-tuning is essential for execution simulation, and that the classification formulation's advantage is not an artifact of model scale.\n\n\n\\subsection{Scaling Behavior}\n\\label{ssec:scaling}\n\n% exp_id: model-size-scaling-cls8b, cls8b-seed{123,456},\n%         model-size-scaling-cwm8b, cwm8b-seed{123,456}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{4B} & \\textbf{8B} & \\textbf{$\\Delta$} & \\textbf{Gap} \\\\\n\\midrule\nCLS & 88.43 & 89.39 $\\pm$ 1.09 & +0.96 & \\multirow{2}{*}{} \\\\\nCWM & 87.19 & 86.96 $\\pm$ 0.72 & $-$0.23 & \\\\\n\\midrule\nCLS$-$CWM & 1.24 & 2.43 & & $p = 0.008$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scaling from 4B to 8B on function-level data. 4B uses five seeds; 8B uses three matched seeds (42, 123, 456). CLS gains +0.96pp from scaling; CWM loses $-$0.23pp. The CLS--CWM gap nearly doubles from 1.24pp to 2.43pp ($p = 0.008$).}\n\\label{tab:scaling}\n\\end{table}\n\nTable~\\ref{tab:scaling} examines scaling behavior by comparing 4B and 8B models with three matched seed pairs per formulation.\nThe key finding is asymmetric: CLS gains +0.96pp from doubling model size (88.43\\% $\\to$ 89.39\\%), while CWM shows no improvement ($-$0.23pp, 87.19\\% $\\to$ 86.96\\%).\nThe CLS--CWM gap consequently widens from 1.24pp at 4B to 2.43pp at 8B ($p = 0.008$, paired $t$-test across three seeds).\n\nThis asymmetry is consistent with a \\emph{generation bottleneck} rather than a capacity limitation.\nIf CWM's lower accuracy were due to insufficient model capacity, scaling should help CWM at least as much as CLS.\nInstead, the generation formulation appears to have a ceiling imposed by the exact-match evaluation criterion: additional capacity helps the model produce better token-level predictions, but exact-match accuracy is dominated by the hardest output tokens (precision-sensitive numbers, formatting characters) where even small errors cause failure.\nClassification sidesteps this bottleneck entirely---the model need only determine whether the output \\emph{would differ} from the expected value, not reconstruct the differing string.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{ssec:equivalence}\n\n% exp_id: 5-paired-clustered-bootstrap, block-corr-empirical\n\nPer-test classification decomposes the verification task into $|T|$ binary predictions that are aggregated to a patch verdict by conjunction.\nThis decomposition could either help (richer signal) or hurt (error compounding).\nWe compare CLS (aggregated to variant level) against TRAJ across five matched seed pairs using the clustered bootstrap framework from \\S\\ref{ssec:setup}.\n\nThe pooled CLS--TRAJ gap is $-$0.45pp (95\\% CI: [$-$1.71, +0.84], $p = 0.499$), with per-seed gaps ranging from $-$1.84pp (seed 456) to +1.45pp (seed 123).\nA TOST equivalence test confirms that the two formulations are statistically equivalent within $\\pm$2pp ($p = 0.007$).\nWe justify this margin on the basis of the block-correlation structure: with an empirically estimated ICC of 0.191 and design effect of 3.97 (\\S\\ref{ssec:analysis}), a 2pp variant-level difference corresponds to substantially less than 1pp in effective independent predictions.\n\nThe practical implication is that per-test classification achieves the \\emph{same} patch-level accuracy as trajectory-level scoring while providing strictly more information: for each patch, CLS identifies which specific tests are predicted to fail, enabling diagnostic applications (targeted re-repair, failure triage) that trajectory-level verifiers cannot support.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{ssec:frontier}\n\n% exp_id: oracle-f2p-stratified, p2p-regression-rate\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n$|T_{\\textsc{f2p}}|$ & \\textbf{\\% Instances} & \\textbf{Block Adv.\\ (pp)} & \\textbf{Contrib.\\ (\\%)} \\\\\n\\midrule\n1 & 68.7 & $-$0.09 & --- \\\\\n2 & 19.1 & 31.69 & 55.3 \\\\\n3--5 & 7.1 & 40.74 & 26.3 \\\\\n$\\geq$ 6 & 5.1 & 40.06 & 18.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Oracle accuracy-utility frontier stratified by the number of fail-to-pass tests $|T_{\\textsc{f2p}}|$ in SWE-bench Verified. Block advantage measures the oracle gain from per-test over trajectory-level verification under the empirical ICC. The advantage concentrates in instances with $T \\geq 2$ (31.3\\% of instances, 100\\% of advantage).}\n\\label{tab:frontier}\n\\end{table}\n\nPer-test verification provides value only when per-test predictions carry actionable information.\nTable~\\ref{tab:frontier} stratifies the per-test oracle advantage by the number of fail-to-pass tests ($|T_{\\textsc{f2p}}|$) using the empirical correlation structure (ICC$=$0.191).\n\nWhen $|T_{\\textsc{f2p}}| = 1$ (68.7\\% of SWE-bench Verified instances), per-test and trajectory-level formulations are informationally equivalent: there is only one fail-to-pass test, so knowing \\emph{which} test fails adds nothing beyond knowing \\emph{that} a test fails.\nThe advantage concentrates in multi-test instances: at $|T_{\\textsc{f2p}}| = 2$ (19.1\\% of instances), the block-correlated oracle advantage is 31.69pp, accounting for 55.3\\% of the total advantage.\n\n\\paragraph{Pass-to-pass regression rate.}\nWe also examine whether per-test verification provides value through pass-to-pass (P2P) regression detection.\nEmpirically, the P2P regression rate on SWE-bench Verified is approximately 1\\% (mean; 0\\% median) across incorrect patches: 77\\% of incorrect patches break zero P2P tests.\nAt this rate, per-test verification offers negligible advantage on the P2P dimension---the signal is too sparse.\nWe report this as an honest negative: the per-test formulation's value on SWE-bench Verified derives primarily from fail-to-pass discrimination in multi-test instances, not from regression detection.\nThe practical decision boundary is $|T_{\\textsc{f2p}}| \\geq 2$: below this threshold, trajectory-level scoring suffices.\n\n\n\\subsection{Repo-Level Results}\n\\label{ssec:repo_results}\n\n% exp_id: repo-level-cls-v5, repo-level-cwm-v12, repo-level-cwm-seed123-conda,\n%         cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Unp.\\ (\\%)} & \\textbf{vs Maj.} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Majority baseline}} \\\\\n--- & --- & --- & 72.96 & --- & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Same-size comparison (primary)}} \\\\\nCLS & 4B & 42 & 83.63 & 1.3 & +10.67 \\\\\nCWM & 4B & 42 & 58.04 & 53.7 & $-$14.92 \\\\\nCWM & 4B & 123 & 59.09 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Cross-size comparison (secondary)}} \\\\\nCLS & 8B & 42 & 83.52 & 0.0 & +10.56 \\\\\nCLS & 8B & 123 & 85.60 & 0.0 & +12.64 \\\\\nCWM & 8B & 42 & \\multicolumn{3}{c}{\\emph{in progress}} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Repo-level verification on SWE-bench Verified ($n$$=$$9{,}784$). Unp.\\ = unparseable prediction rate. CLS outperforms CWM by 25.59pp at matched 4B scale. CWM falls below the majority baseline in both seeds, with 54--67\\% of predictions unparseable.}\n\\label{tab:repo_results}\n\\end{table}\n\nTable~\\ref{tab:repo_results} presents the central result: at repository-level complexity, the CLS--CWM gap explodes from the 1--2pp range observed at function level to over 25pp.\n\n\\paragraph{Primary comparison (same-size 4B).}\nAt matched model scale and seed, CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%---a 25.59pp gap.\nThe gap is driven by CWM's catastrophic failure on repo-level code: 53.7--67.2\\% of CWM predictions are unparseable (the model generates execution traces that consume the entire token budget without reaching a verdict).\nCWM accuracy falls \\emph{below} the majority baseline (72.96\\%) by approximately 14pp in both seeds, meaning the CWM verifier provides negative value compared to always predicting the majority class.\nAmong the minority of parseable CWM predictions, accuracy is only 42--43\\%---below random chance---indicating that the model is anti-informative even when it produces interpretable output.\n\n\\paragraph{Secondary comparison (cross-size).}\nTwo 8B CLS seeds confirm the pattern: CLS at 83.52\\% (seed 42) and 85.60\\% (seed 123) versus matched-seed 4B CWM at 58.04\\% and 59.09\\%, yielding gaps of 25.48pp and 26.51pp respectively.\n8B CWM training on repo-level data is in progress; we will include 8B--8B comparisons in the final version.\n\n\\paragraph{Gap amplification.}\nThe CLS--CWM gap follows a clear complexity gradient: 1.24pp at function-level 4B, 2.43pp at function-level 8B, and $\\sim$25pp at repo-level 4B.\nThis 20$\\times$ amplification from function-level to repo-level confirms the complexity-dependent reformulation advantage predicted by the failure-mode analysis in \\S\\ref{ssec:failure_modes}: on simple code with short outputs, the generation formulation copes; on complex code with long traces, it collapses.\n\n\n\\subsection{Analysis}\n\\label{ssec:analysis}\n\n% exp_id: cwm-rank32-ablation-v2, cls8b-s42-ckpt1000-test-seq2048-ablation,\n%         block-corr-empirical\n\n\\paragraph{Error complementarity.}\nCLS and CWM exhibit systematically opposite error patterns on function-level data.\nOf CLS errors, 75.5\\% are false negatives (missed bugs: the model predicts \\textsc{Pass} for a truly failing test), while 83.1\\% of CWM errors are false positives (false alarms: the model predicts \\textsc{Fail} for a truly passing test).\nAn oracle that selects the correct prediction whenever the two models disagree achieves 90.63\\% accuracy---a 2.20pp gain over CLS alone and 3.44pp over CWM.\nThis complementarity suggests that formulation diversity (combining classification and generation verifiers) may be a productive strategy for verification pipelines, even at function-level complexity where the individual formulations achieve similar accuracy.\n\n\\paragraph{CWM error-mode breakdown.}\nA detailed analysis of 500 repo-level CWM predictions reveals three error modes in order of prevalence.\n\\emph{Token-budget exhaustion} (77\\% of unparseable predictions): the model generates realistic pytest execution traces---dots, warnings, file paths---that consume the entire 1,024-token generation budget before reaching any pass/fail verdict.\n\\emph{Keyword ambiguity} (23\\% of unparseable): the generated trace contains both pass-indicating and fail-indicating keywords (e.g., test names containing ``fail,'' deprecation warnings alongside success indicators), preventing reliable keyword extraction.\nAmong the minority of parseable predictions, the model hallucinates failures: 90\\% of parseable errors are \\textsc{Pass}$\\to$\\textsc{Fail} misclassifications (64 of 71 wrong parseable predictions).\nThese failure modes are structural to the generation formulation and cannot be addressed by increasing model capacity---as confirmed by the CWM scaling results in \\S\\ref{ssec:scaling}.\n\n\\paragraph{Per-repository variation.}\nCWM unparseable rates vary dramatically across repositories: from $\\sim$0\\% on scikit-learn (concise test output) to 100\\% on sphinx (verbose build output).\nThis variation reflects a fundamental dependency on the target repository's test output format---a dependency that CLS avoids by construction, since it never generates execution output.\n\n\\paragraph{Sequence-length confound ablation.}\nCLS and CWM use different maximum sequence lengths at repo-level (CLS: 8,192 tokens; CWM: 2,048 tokens), raising the concern that CLS's advantage could be an artifact of additional input context rather than formulation.\nTo control for this, we evaluate the CLS 8B model (seed 42, val-selected checkpoint) at $\\text{max\\_seq\\_length} = 2{,}048$ (matching CWM's configuration).\nAccuracy drops by only 0.69pp (83.52\\% $\\to$ 82.83\\%), leaving a 24.79pp gap over CWM.\nThis confirms that the classification advantage is driven by the formulation, not the input sequence length.\n\n\\paragraph{LoRA rank ablation.}\nTo address the concern that LoRA rank$=$16 may systematically disadvantage CWM (which must reconstruct output strings and might benefit from additional adapter capacity), we train a CWM 4B model with rank$=$32 on function-level data.\nThe rank$=$32 model achieves 87.0\\% accuracy versus 87.51\\% at rank$=$16 ($\\Delta = -$0.51pp), well within seed-level variance ($\\pm$0.53pp).\nCWM's capacity to generate execution outputs is not bottlenecked by adapter rank at this scale.\n\n\\paragraph{Block correlation.}\nThe empirical ICC of 0.191 ($p < 0.0001$) indicates significant block correlation: per-test predictions within the same patch are positively correlated, with a design effect of 3.97.\nIn practical terms, the 114 test-level clusters (problems) in our function-level evaluation yield an effective sample size of approximately $1{,}890 / 3.97 \\approx 476$ independent observations.\nThis correlation structure has two implications: (1) it motivates the clustered bootstrap procedure used throughout, and (2) it amplifies the per-test advantage in the oracle framework (\\S\\ref{ssec:frontier}), since correlated correct predictions within a cluster mean that a single per-test error is more likely to flip the patch-level verdict.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a406037-eb10-4c7e-8a27-de29cd0c9ec3",
  "isSidechain": false,
  "requestId": "req_011Cb4XuxQhb35heaWmxmjdX",
  "type": "assistant",
  "uuid": "6ecd63a7-3f50-474b-b59a-108b8fcf72bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZybJR6cS6sSg19mtcrVqY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11060,
      "cache_read_input_tokens": 110963,
      "output_tokens": 6101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6101,
          "cache_read_input_tokens": 110963,
          "cache_creation_input_tokens": 11060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11060
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

_source line 122 · 2026-05-15T14:46:55.564Z_

<details><summary>↩ Tool result · `toolu_01QihmPVQVe2SRxyLo3KXkyu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ecd63a7-3f50-474b-b59a-108b8fcf72bd",
  "isSidechain": false,
  "promptId": "3f812c82-5531-4de9-bbf7-0056200f4795",
  "type": "user",
  "uuid": "feb90ea3-5289-4bdc-b751-c7c1f84ca5d7",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex",
    "content": "% Experiments draft — generated 2026-05-15, numbers from registry\n% NOTE: All numbers cross-checked against experiment registry.\n% exp_id references provided for key claims.\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the three formulations defined in \\S\\ref{sec:method} across two complexity levels---function-level and repository-level---to test the prediction that classification gains an increasing advantage over generation as code complexity grows.\n\n\\subsection{Experimental Setup}\n\\label{ssec:setup}\n\n\\paragraph{Function-Level Data.}\nWe construct a function-level benchmark from HumanEval~\\citep{chen2021humaneval} and MBPP~\\citep{austin2021mbpp} by applying five categories of systematic mutations---\\texttt{off\\_by\\_one}, \\texttt{operator\\_swap}, \\texttt{variable\\_swap}, \\texttt{return\\_value}, and \\texttt{boundary\\_removal}---to correct solutions, yielding 19,076 (code, test, label) triples.\nWe split by problem identity: 15,290 train / 1,896 validation / 1,890 test, with zero problem overlap between splits.\nThe test set is approximately class-balanced (51.7\\% \\textsc{Pass}, 48.3\\% \\textsc{Fail}).\n\n\\paragraph{Repo-Level Data.}\nWe derive a per-test verification dataset from SWE-bench Verified~\\citep{jimenez2024swebench} by pairing each candidate patch with individual test cases and their ground-truth outcomes.\nThe resulting dataset contains approximately 70K training samples, 9,335 validation samples, and 9,784 test samples.\nThe test set is class-imbalanced (72.96\\% \\textsc{Pass}); we report the majority-class baseline throughout.\nValidation and test splits have zero problem overlap and exhibit a mutation-type composition shift (operator\\_swap: 19.1\\% val $\\to$ 34.3\\% test), which we discuss in \\S\\ref{ssec:analysis}.\n\n\\paragraph{Models and Training.}\nAll models use Qwen3~\\citep{qwen2025qwen3} as the base architecture with LoRA adaptation~\\citep{hu2022lora} (rank$=$16, $\\alpha$$=$32).\nWe train Qwen3-4B and Qwen3-8B variants for CLS, CWM, and TRAJ formulations.\nTraining uses AdamW with learning rate $2 \\times 10^{-4}$ (function-level) or $5 \\times 10^{-5}$ (repo-level), weight decay 0.01, warmup ratio 0.05, batch size 32 (effective), and 3 epochs.\nFunction-level experiments use seeds 42, 123, 456, 789, and 0 (five seeds); 8B scaling experiments use seeds 42, 123, and 456 (three matched pairs).\nSeeds 42/123/456 use bfloat16 precision; seeds 789 and 0 use NF4 quantization due to hardware constraints.\\footnote{NF4 seeds appear only in 4B paired comparisons (\\S\\ref{ssec:equivalence}), where the within-seed paired design controls for quantization effects.}\n\n\\paragraph{Checkpoint Selection.}\nAll reported results use validation-selected checkpoints: we sweep all saved checkpoints on the validation split and select the one with highest accuracy, then evaluate on the held-out test split exactly once.\n\n\\paragraph{Statistical Methods.}\nWe report seed-level means $\\pm$ sample standard deviations.\nFor the CLS--CWM comparison, we use seed-paired bootstrap (10,000 resamples) with one-sided tests.\nFor CLS--TRAJ equivalence, we apply the two one-sided tests (TOST) procedure~\\citep{schuirmann1987tost} with a pre-specified $\\pm$2 percentage-point (pp) equivalence margin.\nFor repo-level results with clustered per-test predictions, we use clustered bootstrap with 114 problem-level clusters and 10,000 resamples.\nWe report the intra-cluster correlation coefficient (ICC) and design effect (DEFF) to characterize block-correlation structure.\n\n\n\\subsection{Function-Level Results}\n\\label{ssec:func_results}\n\n% exp_id: multi-seed-core, cwm-baseline, cwm-seed{123,456,789,0},\n%         cls-seed{789,0}, traj-level-{finetuned,seed123,seed456,seed789,seed0},\n%         llm-judge-8b-zeroshot, llm-judge-32b-zeroshot\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Accuracy (\\%)} & \\textbf{Seeds} \\\\\n\\midrule\nCLS & Qwen3-4B & 88.43 $\\pm$ 0.78 & 5 \\\\\nCWM & Qwen3-4B & 87.19 $\\pm$ 0.37 & 5 \\\\\nTRAJ & Qwen3-4B & 86.30 $\\pm$ 0.97 & 5 \\\\\n\\midrule\nZS Judge & Qwen3-8B & 64.40 & 1 \\\\\nZS Judge & Qwen3-32B\\textsuperscript{\\textdagger} & 71.69 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Function-level per-test verification accuracy on HumanEval+MBPP mutants ($n$$=$$1{,}890$). CLS, CWM, and TRAJ are fine-tuned with LoRA; ZS Judge uses zero-shot prompting. \\textsuperscript{\\textdagger}NF4 quantization. All three fine-tuned formulations achieve $>$86\\% accuracy, substantially outperforming zero-shot baselines.}\n\\label{tab:func_results}\n\\end{table}\n\nTable~\\ref{tab:func_results} presents function-level results.\nAll three fine-tuned formulations---CLS, CWM, and TRAJ---achieve strong accuracy in the 86--89\\% range, with CLS leading at 88.43\\%.\n\n\\paragraph{CLS vs.\\ CWM.}\nCLS outperforms CWM by 1.24pp across five matched seeds (bootstrap 95\\% CI: [0.46, 2.04], one-sided $p = 0.025$).\nThe gap is consistent: CLS achieves higher accuracy in all five seed pairs, with per-seed gaps ranging from 0.32pp (seed 42) to 2.33pp (seed 789).\nWhile statistically significant, this gap is modest---both formulations achieve near-equivalent accuracy on function-level code where execution outputs are short and CWM failure modes rarely activate.\n\n\\paragraph{Zero-shot baselines.}\nZero-shot LLM-as-judge performance lags far behind fine-tuned models: Qwen3-8B achieves only 64.40\\% and Qwen3-32B (NF4) reaches 71.69\\%, both exhibiting a systematic bias toward predicting \\textsc{Fail} (fail recall $>$92\\%, pass recall $<$53\\%).\nThe 16.7pp gap between the 32B zero-shot model and the fine-tuned 4B CLS confirms that task-specific fine-tuning is essential for execution simulation, and that the classification formulation's advantage is not an artifact of model scale.\n\n\n\\subsection{Scaling Behavior}\n\\label{ssec:scaling}\n\n% exp_id: model-size-scaling-cls8b, cls8b-seed{123,456},\n%         model-size-scaling-cwm8b, cwm8b-seed{123,456}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{4B} & \\textbf{8B} & \\textbf{$\\Delta$} & \\textbf{Gap} \\\\\n\\midrule\nCLS & 88.43 & 89.39 $\\pm$ 1.09 & +0.96 & \\multirow{2}{*}{} \\\\\nCWM & 87.19 & 86.96 $\\pm$ 0.72 & $-$0.23 & \\\\\n\\midrule\nCLS$-$CWM & 1.24 & 2.43 & & $p = 0.008$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scaling from 4B to 8B on function-level data. 4B uses five seeds; 8B uses three matched seeds (42, 123, 456). CLS gains +0.96pp from scaling; CWM loses $-$0.23pp. The CLS--CWM gap nearly doubles from 1.24pp to 2.43pp ($p = 0.008$).}\n\\label{tab:scaling}\n\\end{table}\n\nTable~\\ref{tab:scaling} examines scaling behavior by comparing 4B and 8B models with three matched seed pairs per formulation.\nThe key finding is asymmetric: CLS gains +0.96pp from doubling model size (88.43\\% $\\to$ 89.39\\%), while CWM shows no improvement ($-$0.23pp, 87.19\\% $\\to$ 86.96\\%).\nThe CLS--CWM gap consequently widens from 1.24pp at 4B to 2.43pp at 8B ($p = 0.008$, paired $t$-test across three seeds).\n\nThis asymmetry is consistent with a \\emph{generation bottleneck} rather than a capacity limitation.\nIf CWM's lower accuracy were due to insufficient model capacity, scaling should help CWM at least as much as CLS.\nInstead, the generation formulation appears to have a ceiling imposed by the exact-match evaluation criterion: additional capacity helps the model produce better token-level predictions, but exact-match accuracy is dominated by the hardest output tokens (precision-sensitive numbers, formatting characters) where even small errors cause failure.\nClassification sidesteps this bottleneck entirely---the model need only determine whether the output \\emph{would differ} from the expected value, not reconstruct the differing string.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{ssec:equivalence}\n\n% exp_id: 5-paired-clustered-bootstrap, block-corr-empirical\n\nPer-test classification decomposes the verification task into $|T|$ binary predictions that are aggregated to a patch verdict by conjunction.\nThis decomposition could either help (richer signal) or hurt (error compounding).\nWe compare CLS (aggregated to variant level) against TRAJ across five matched seed pairs using the clustered bootstrap framework from \\S\\ref{ssec:setup}.\n\nThe pooled CLS--TRAJ gap is $-$0.45pp (95\\% CI: [$-$1.71, +0.84], $p = 0.499$), with per-seed gaps ranging from $-$1.84pp (seed 456) to +1.45pp (seed 123).\nA TOST equivalence test confirms that the two formulations are statistically equivalent within $\\pm$2pp ($p = 0.007$).\nWe justify this margin on the basis of the block-correlation structure: with an empirically estimated ICC of 0.191 and design effect of 3.97 (\\S\\ref{ssec:analysis}), a 2pp variant-level difference corresponds to substantially less than 1pp in effective independent predictions.\n\nThe practical implication is that per-test classification achieves the \\emph{same} patch-level accuracy as trajectory-level scoring while providing strictly more information: for each patch, CLS identifies which specific tests are predicted to fail, enabling diagnostic applications (targeted re-repair, failure triage) that trajectory-level verifiers cannot support.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{ssec:frontier}\n\n% exp_id: oracle-f2p-stratified, p2p-regression-rate\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n$|T_{\\textsc{f2p}}|$ & \\textbf{\\% Instances} & \\textbf{Block Adv.\\ (pp)} & \\textbf{Contrib.\\ (\\%)} \\\\\n\\midrule\n1 & 68.7 & $-$0.09 & --- \\\\\n2 & 19.1 & 31.69 & 55.3 \\\\\n3--5 & 7.1 & 40.74 & 26.3 \\\\\n$\\geq$ 6 & 5.1 & 40.06 & 18.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Oracle accuracy-utility frontier stratified by the number of fail-to-pass tests $|T_{\\textsc{f2p}}|$ in SWE-bench Verified. Block advantage measures the oracle gain from per-test over trajectory-level verification under the empirical ICC. The advantage concentrates in instances with $T \\geq 2$ (31.3\\% of instances, 100\\% of advantage).}\n\\label{tab:frontier}\n\\end{table}\n\nPer-test verification provides value only when per-test predictions carry actionable information.\nTable~\\ref{tab:frontier} stratifies the per-test oracle advantage by the number of fail-to-pass tests ($|T_{\\textsc{f2p}}|$) using the empirical correlation structure (ICC$=$0.191).\n\nWhen $|T_{\\textsc{f2p}}| = 1$ (68.7\\% of SWE-bench Verified instances), per-test and trajectory-level formulations are informationally equivalent: there is only one fail-to-pass test, so knowing \\emph{which} test fails adds nothing beyond knowing \\emph{that} a test fails.\nThe advantage concentrates in multi-test instances: at $|T_{\\textsc{f2p}}| = 2$ (19.1\\% of instances), the block-correlated oracle advantage is 31.69pp, accounting for 55.3\\% of the total advantage.\n\n\\paragraph{Pass-to-pass regression rate.}\nWe also examine whether per-test verification provides value through pass-to-pass (P2P) regression detection.\nEmpirically, the P2P regression rate on SWE-bench Verified is approximately 1\\% (mean; 0\\% median) across incorrect patches: 77\\% of incorrect patches break zero P2P tests.\nAt this rate, per-test verification offers negligible advantage on the P2P dimension---the signal is too sparse.\nWe report this as an honest negative: the per-test formulation's value on SWE-bench Verified derives primarily from fail-to-pass discrimination in multi-test instances, not from regression detection.\nThe practical decision boundary is $|T_{\\textsc{f2p}}| \\geq 2$: below this threshold, trajectory-level scoring suffices.\n\n\n\\subsection{Repo-Level Results}\n\\label{ssec:repo_results}\n\n% exp_id: repo-level-cls-v5, repo-level-cwm-v12, repo-level-cwm-seed123-conda,\n%         cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Unp.\\ (\\%)} & \\textbf{vs Maj.} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Majority baseline}} \\\\\n--- & --- & --- & 72.96 & --- & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Same-size comparison (primary)}} \\\\\nCLS & 4B & 42 & 83.63 & 1.3 & +10.67 \\\\\nCWM & 4B & 42 & 58.04 & 53.7 & $-$14.92 \\\\\nCWM & 4B & 123 & 59.09 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Cross-size comparison (secondary)}} \\\\\nCLS & 8B & 42 & 83.52 & 0.0 & +10.56 \\\\\nCLS & 8B & 123 & 85.60 & 0.0 & +12.64 \\\\\nCWM & 8B & 42 & \\multicolumn{3}{c}{\\emph{in progress}} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Repo-level verification on SWE-bench Verified ($n$$=$$9{,}784$). Unp.\\ = unparseable prediction rate. CLS outperforms CWM by 25.59pp at matched 4B scale. CWM falls below the majority baseline in both seeds, with 54--67\\% of predictions unparseable.}\n\\label{tab:repo_results}\n\\end{table}\n\nTable~\\ref{tab:repo_results} presents the central result: at repository-level complexity, the CLS--CWM gap explodes from the 1--2pp range observed at function level to over 25pp.\n\n\\paragraph{Primary comparison (same-size 4B).}\nAt matched model scale and seed, CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%---a 25.59pp gap.\nThe gap is driven by CWM's catastrophic failure on repo-level code: 53.7--67.2\\% of CWM predictions are unparseable (the model generates execution traces that consume the entire token budget without reaching a verdict).\nCWM accuracy falls \\emph{below} the majority baseline (72.96\\%) by approximately 14pp in both seeds, meaning the CWM verifier provides negative value compared to always predicting the majority class.\nAmong the minority of parseable CWM predictions, accuracy is only 42--43\\%---below random chance---indicating that the model is anti-informative even when it produces interpretable output.\n\n\\paragraph{Secondary comparison (cross-size).}\nTwo 8B CLS seeds confirm the pattern: CLS at 83.52\\% (seed 42) and 85.60\\% (seed 123) versus matched-seed 4B CWM at 58.04\\% and 59.09\\%, yielding gaps of 25.48pp and 26.51pp respectively.\n8B CWM training on repo-level data is in progress; we will include 8B--8B comparisons in the final version.\n\n\\paragraph{Gap amplification.}\nThe CLS--CWM gap follows a clear complexity gradient: 1.24pp at function-level 4B, 2.43pp at function-level 8B, and $\\sim$25pp at repo-level 4B.\nThis 20$\\times$ amplification from function-level to repo-level confirms the complexity-dependent reformulation advantage predicted by the failure-mode analysis in \\S\\ref{ssec:failure_modes}: on simple code with short outputs, the generation formulation copes; on complex code with long traces, it collapses.\n\n\n\\subsection{Analysis}\n\\label{ssec:analysis}\n\n% exp_id: cwm-rank32-ablation-v2, cls8b-s42-ckpt1000-test-seq2048-ablation,\n%         block-corr-empirical\n\n\\paragraph{Error complementarity.}\nCLS and CWM exhibit systematically opposite error patterns on function-level data.\nOf CLS errors, 75.5\\% are false negatives (missed bugs: the model predicts \\textsc{Pass} for a truly failing test), while 83.1\\% of CWM errors are false positives (false alarms: the model predicts \\textsc{Fail} for a truly passing test).\nAn oracle that selects the correct prediction whenever the two models disagree achieves 90.63\\% accuracy---a 2.20pp gain over CLS alone and 3.44pp over CWM.\nThis complementarity suggests that formulation diversity (combining classification and generation verifiers) may be a productive strategy for verification pipelines, even at function-level complexity where the individual formulations achieve similar accuracy.\n\n\\paragraph{CWM error-mode breakdown.}\nA detailed analysis of 500 repo-level CWM predictions reveals three error modes in order of prevalence.\n\\emph{Token-budget exhaustion} (77\\% of unparseable predictions): the model generates realistic pytest execution traces---dots, warnings, file paths---that consume the entire 1,024-token generation budget before reaching any pass/fail verdict.\n\\emph{Keyword ambiguity} (23\\% of unparseable): the generated trace contains both pass-indicating and fail-indicating keywords (e.g., test names containing ``fail,'' deprecation warnings alongside success indicators), preventing reliable keyword extraction.\nAmong the minority of parseable predictions, the model hallucinates failures: 90\\% of parseable errors are \\textsc{Pass}$\\to$\\textsc{Fail} misclassifications (64 of 71 wrong parseable predictions).\nThese failure modes are structural to the generation formulation and cannot be addressed by increasing model capacity---as confirmed by the CWM scaling results in \\S\\ref{ssec:scaling}.\n\n\\paragraph{Per-repository variation.}\nCWM unparseable rates vary dramatically across repositories: from $\\sim$0\\% on scikit-learn (concise test output) to 100\\% on sphinx (verbose build output).\nThis variation reflects a fundamental dependency on the target repository's test output format---a dependency that CLS avoids by construction, since it never generates execution output.\n\n\\paragraph{Sequence-length confound ablation.}\nCLS and CWM use different maximum sequence lengths at repo-level (CLS: 8,192 tokens; CWM: 2,048 tokens), raising the concern that CLS's advantage could be an artifact of additional input context rather than formulation.\nTo control for this, we evaluate the CLS 8B model (seed 42, val-selected checkpoint) at $\\text{max\\_seq\\_length} = 2{,}048$ (matching CWM's configuration).\nAccuracy drops by only 0.69pp (83.52\\% $\\to$ 82.83\\%), leaving a 24.79pp gap over CWM.\nThis confirms that the classification advantage is driven by the formulation, not the input sequence length.\n\n\\paragraph{LoRA rank ablation.}\nTo address the concern that LoRA rank$=$16 may systematically disadvantage CWM (which must reconstruct output strings and might benefit from additional adapter capacity), we train a CWM 4B model with rank$=$32 on function-level data.\nThe rank$=$32 model achieves 87.0\\% accuracy versus 87.51\\% at rank$=$16 ($\\Delta = -$0.51pp), well within seed-level variance ($\\pm$0.53pp).\nCWM's capacity to generate execution outputs is not bottlenecked by adapter rank at this scale.\n\n\\paragraph{Block correlation.}\nThe empirical ICC of 0.191 ($p < 0.0001$) indicates significant block correlation: per-test predictions within the same patch are positively correlated, with a design effect of 3.97.\nIn practical terms, the 114 test-level clusters (problems) in our function-level evaluation yield an effective sample size of approximately $1{,}890 / 3.97 \\approx 476$ independent observations.\nThis correlation structure has two implications: (1) it motivates the clustered bootstrap procedure used throughout, and (2) it amplifies the per-test advantage in the oracle framework (\\S\\ref{ssec:frontier}), since correlated correct predictions within a cluster mean that a single per-test error is more likely to flip the patch-level verdict.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6ecd63a7-3f50-474b-b59a-108b8fcf72bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 123 · 2026-05-15T14:46:55.572Z_

```json
{
  "parentUuid": "feb90ea3-5289-4bdc-b751-c7c1f84ca5d7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "15554239-97e7-494b-8456-55a3422432bd",
  "timestamp": "2026-05-15T14:46:55.572Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "leafUuid": "15554239-97e7-494b-8456-55a3422432bd",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428"
}
```

---


### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Experiments section for EMNLP 2026 paper",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428"
}
```

---


### Assistant

_source line 126 · 2026-05-15T14:46:58.769Z_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15554239-97e7-494b-8456-55a3422432bd",
  "isSidechain": false,
  "requestId": "req_011Cb4Y5cSC3X2Yek5sS2hWJ",
  "type": "assistant",
  "uuid": "1445e873-8d39-42e8-9ba3-566bc6ef6dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjoKiEohBDCYaR6z8oL1Vm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6261,
      "cache_read_input_tokens": 122023,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 122023,
          "cache_creation_input_tokens": 6261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6261
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

_source line 127 · 2026-05-15T14:46:59.149Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RqM66wiTburxtJed54pucf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1445e873-8d39-42e8-9ba3-566bc6ef6dde",
  "isSidechain": false,
  "requestId": "req_011Cb4Y5cSC3X2Yek5sS2hWJ",
  "type": "assistant",
  "uuid": "0961275e-e6ac-42ed-a0a8-968708aa977b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjoKiEohBDCYaR6z8oL1Vm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6261,
      "cache_read_input_tokens": 122023,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 122023,
          "cache_creation_input_tokens": 6261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6261
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

_source line 128 · 2026-05-15T14:46:59.152Z_

<details><summary>↩ Tool result · `toolu_01RqM66wiTburxtJed54pucf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0961275e-e6ac-42ed-a0a8-968708aa977b",
  "isSidechain": false,
  "promptId": "3f812c82-5531-4de9-bbf7-0056200f4795",
  "type": "user",
  "uuid": "489897d1-bb77-4257-8019-d074747efc61",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "0961275e-e6ac-42ed-a0a8-968708aa977b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-15T14:47:05.054Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01JCdsT3wQcNvQSr3isL5qhi`</summary>

```json
{
  "name": "experiments.tex",
  "type": "paper",
  "description": "Experiments section (§4) for EMNLP 2026 paper — ~2800 words, 4 tables, 7 subsections covering function-level results, scaling, CLS-TRAJ equivalence, oracle frontier, repo-level results, and analysis (ablations + error modes)",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex",
  "tags": [
    "paper",
    "experiments",
    "emnlp2026",
    "draft"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "489897d1-bb77-4257-8019-d074747efc61",
  "isSidechain": false,
  "requestId": "req_011Cb4Y5sihSm2WebEqcR2eG",
  "type": "assistant",
  "uuid": "107340bb-fe02-4b35-9764-dc9125573a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uWyihdRxUcGwQRKtQmdJs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 128284,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 281,
          "cache_read_input_tokens": 128284,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 130 · 2026-05-15T14:47:05.204Z_

<details><summary>↩ Tool result · `toolu_01JCdsT3wQcNvQSr3isL5qhi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_3378f2\", \"name\": \"experiments.tex\", \"type\": \"paper\", \"description\": \"Experiments section (§4) for EMNLP 2026 paper — ~2800 words, 4 tables, 7 subsections covering function-level results, scaling, CLS-TRAJ equivalence, oracle frontier, repo-level results, and analysis (ablations + error modes)\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments_3378f2.tex\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:47:05.060065+00:00\", \"tags\": [\"paper\", \"experiments\", \"emnlp2026\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "107340bb-fe02-4b35-9764-dc9125573a6d",
  "isSidechain": false,
  "promptId": "3f812c82-5531-4de9-bbf7-0056200f4795",
  "type": "user",
  "uuid": "94471977-2cc3-4856-a94c-354b086d3487",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_3378f2\\\", \\\"name\\\": \\\"experiments.tex\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Experiments section (§4) for EMNLP 2026 paper — ~2800 words, 4 tables, 7 subsections covering function-level results, scaling, CLS-TRAJ equivalence, oracle frontier, repo-level results, and analysis (ablations + error modes)\\\", \\\"path\\\": \\\"projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments_3378f2.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"exec-sim-repair-verifier\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T14:47:05.060065+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"emnlp2026\\\", \\\"draft\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_3378f2\", \"name\": \"experiments.tex\", \"type\": \"paper\", \"description\": \"Experiments section (§4) for EMNLP 2026 paper — ~2800 words, 4 tables, 7 subsections covering function-level results, scaling, CLS-TRAJ equivalence, oracle frontier, repo-level results, and analysis (ablations + error modes)\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments_3378f2.tex\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:47:05.060065+00:00\", \"tags\": [\"paper\", \"experiments\", \"emnlp2026\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "107340bb-fe02-4b35-9764-dc9125573a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 131 · 2026-05-15T14:47:08.222Z_

<details><summary>Logged reasoning block</summary>

```text
The file has been written and registered. Let me verify the file was written correctly by reading a portion of it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94471977-2cc3-4856-a94c-354b086d3487",
  "isSidechain": false,
  "requestId": "req_011Cb4Y6K9ADrk6ZreMZAesp",
  "type": "assistant",
  "uuid": "ac4af970-bf14-4eaf-a57f-0965cb91ed13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YNjsL7xAqtrSS8HPYGnCJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 129004,
      "output_tokens": 610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 610,
          "cache_read_input_tokens": 129004,
          "cache_creation_input_tokens": 603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 603
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

_source line 132 · 2026-05-15T14:47:21.227Z_

文件已写入 `artifacts/_project/paper/experiments.tex` 并注册。

结构和数据摘要：

**§4.1 Setup** — 数据集规模、模型配置、LoRA、seed/精度说明（789/0 NF4 已注明）、val-best checkpoint 协议、统计方法（clustered bootstrap + TOST）

**§4.2 Function-Level (Table 1)** — CLS 88.43±0.78 vs CWM 87.19±0.37 (gap 1.24pp, p=0.025)；TRAJ 86.30±0.97；ZS 8B 64.40% / 32B NF4 71.69%

**§4.3 Scaling (Table 2)** — 8B CLS 89.39 vs CWM 86.96 (gap 2.43pp, p=0.008)；CLS +0.96pp scaling gain, CWM −0.23pp；generation bottleneck 论证

**§4.4 CLS-TRAJ Equivalence** — gap −0.45pp, TOST p=0.007, ICC=0.191, DEFF=3.97；等价精度+免费诊断粒度

**§4.5 Oracle Frontier (Table 3)** — T=1 (69%) 无优势；T=2 (19%) block advantage 31.69pp, 55% contribution；P2P ~1% honest negative

**§4.6 Repo-Level (Table 4)** — 4B CLS 83.63% vs CWM 58.04% = 25.59pp (primary)；8B CLS 83.52/85.60% (secondary)；CWM 低于 majority baseline 14pp；unparseable 54-67%；8B-8B CWM 标 in progress

**§4.7 Analysis** — error complementarity (oracle 90.63%)、CWM 三类 error mode (77% token exhaustion / 23% ambiguous / hallucinated failures)、per-repo variation、seq_length ablation (drop 0.69pp)、LoRA rank ablation (−0.51pp)、ICC=0.191

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4af970-bf14-4eaf-a57f-0965cb91ed13",
  "isSidechain": false,
  "requestId": "req_011Cb4Y6K9ADrk6ZreMZAesp",
  "type": "assistant",
  "uuid": "31ad66d2-ecc0-4902-a8f0-93d13a0631f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YNjsL7xAqtrSS8HPYGnCJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 129004,
      "output_tokens": 610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 610,
          "cache_read_input_tokens": 129004,
          "cache_creation_input_tokens": 603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 603
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


### Runtime record

_source line 133_

```json
{
  "type": "last-prompt",
  "leafUuid": "31ad66d2-ecc0-4902-a8f0-93d13a0631f3",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428"
}
```

---


### Runtime record

_source line 134_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Experiments section for EMNLP 2026 paper",
  "sessionId": "717f96bf-e494-4f5a-bcaa-a1b2aab8a428"
}
```

---
