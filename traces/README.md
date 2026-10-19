# Research Trace Atlas

Browse recorded tasks, user-role instructions, assistant responses, tool calls, and tool results from **17 trace collections**. Open **Readable Markdown** in any project guide for a GitHub reading view, or select the adjacent JSON link for the complete structured record.

[Offline preview](demo.html) · [Interactive browser](index.html) · [Format and provenance](FORMAT.md)

For the complete browser, run `python3 scripts/serve_traces.py --open` from a downloaded repository. The offline preview embeds one actual bounded round per project when a matching round exists.

| Project | Conversations | Worker logs | Results | Context notes | Events | Readable Markdown |
|---|---:|---:|---:|---:|---:|---|
| [acr-vla-conformal-refinement](../paper-assets/acr-vla-conformal-refinement/05-generation-trace/README.md) | 1,796 | 2,883 | 2,064 | 371 | 391,607 | [Read](../paper-assets/acr-vla-conformal-refinement/05-generation-trace/readable/README.md) |
| [causal_annot_error_attrib](../paper-assets/causal_annot_error_attrib/05-generation-trace/README.md) | 78 | 225 | 163 | 9 | 66,314 | [Read](../paper-assets/causal_annot_error_attrib/05-generation-trace/readable/README.md) |
| [causal_style_decomp_judge](../paper-assets/causal_style_decomp_judge/05-generation-trace/README.md) | 69 | 221 | 211 | 5 | 73,378 | [Read](../paper-assets/causal_style_decomp_judge/05-generation-trace/readable/README.md) |
| [cert_manip_resist_eval](../paper-assets/cert_manip_resist_eval/05-generation-trace/README.md) | 137 | 381 | 358 | 4 | 97,735 | [Read](../paper-assets/cert_manip_resist_eval/05-generation-trace/readable/README.md) |
| [clkc_mech_interp](../paper-assets/clkc_mech_interp/05-generation-trace/README.md) | 92 | 310 | 282 | 5 | 76,491 | [Read](../paper-assets/clkc_mech_interp/05-generation-trace/readable/README.md) |
| [crosscoder-behavioral-circuit-transplant](../paper-assets/crosscoder-behavioral-circuit-transplant/05-generation-trace/README.md) | 5 | 9 | 6 | 0 | 1,393 | [Read](../paper-assets/crosscoder-behavioral-circuit-transplant/05-generation-trace/readable/README.md) |
| [diagprm-stage-reasoning](../paper-assets/diagprm-stage-reasoning/05-generation-trace/README.md) | 4 | 6 | 8 | 0 | 851 | [Read](../paper-assets/diagprm-stage-reasoning/05-generation-trace/readable/README.md) |
| [ec_hte_llm_annotation](../paper-assets/ec_hte_llm_annotation/05-generation-trace/README.md) | 72 | 183 | 175 | 4 | 75,488 | [Read](../paper-assets/ec_hte_llm_annotation/05-generation-trace/readable/README.md) |
| [entrainment_gated_ft](../paper-assets/entrainment_gated_ft/05-generation-trace/README.md) | 99 | 266 | 223 | 11 | 80,801 | [Read](../paper-assets/entrainment_gated_ft/05-generation-trace/readable/README.md) |
| [importance_margin_vla_compress](../paper-assets/importance_margin_vla_compress/05-generation-trace/README.md) | 1,235 | 2,223 | 2,107 | 189 | 413,702 | [Read](../paper-assets/importance_margin_vla_compress/05-generation-trace/readable/README.md) |
| [prod42](../paper-assets/prod42/05-generation-trace/README.md) | 0 | 0 | 0 | 0 | 0 | [Read](../paper-assets/prod42/05-generation-trace/readable/README.md) |
| [prod_0510](../paper-assets/prod_0510/05-generation-trace/README.md) | 0 | 0 | 0 | 0 | 0 | [Read](../paper-assets/prod_0510/05-generation-trace/readable/README.md) |
| [ratekv](../paper-assets/ratekv/05-generation-trace/README.md) | 260 | 513 | 419 | 58 | 87,631 | [Read](../paper-assets/ratekv/05-generation-trace/readable/README.md) |
| [recursive_gen_depth_est](../paper-assets/recursive_gen_depth_est/05-generation-trace/README.md) | 347 | 686 | 642 | 104 | 166,550 | [Read](../paper-assets/recursive_gen_depth_est/05-generation-trace/readable/README.md) |
| [schema-dag-extraction](../paper-assets/schema-dag-extraction/05-generation-trace/README.md) | 217 | 506 | 474 | 45 | 131,771 | [Read](../paper-assets/schema-dag-extraction/05-generation-trace/readable/README.md) |
| [xling_calab_direction](../paper-assets/xling_calab_direction/05-generation-trace/README.md) | 0 | 1 | 1 | 0 | 404 | [Read](../paper-assets/xling_calab_direction/05-generation-trace/readable/README.md) |
| [xling_calib_direction](../paper-assets/xling_calib_direction/05-generation-trace/README.md) | 48 | 123 | 119 | 0 | 27,260 | [Read](../paper-assets/xling_calib_direction/05-generation-trace/readable/README.md) |

**21,052 source records · 1,691,376 recorded messages/events.** Counts include overlapping snapshots and parallel logs; they are not deduplicated research actions.

Source language and order are retained. A user-role message can originate from another agent or system and does not identify a human author. Missing prompts and timestamps are not reconstructed. Credentials and embedded attachment payloads are redacted.
