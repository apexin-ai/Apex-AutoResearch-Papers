# analysis claim audit — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-claim-audit-copy-2.md) · [Structured JSON](../../../sessions/ab/abef968554bae69e0b5b.json)

## Round 1

### Tool result

_source line 83 · 2026-05-22T18:19:21.051Z_

<details><summary>↩ Tool result · `toolu_018iMFqCJqPicvsJYiLW185C`</summary>

```text
200	  sj_rho_full: 0.4357
201	  sj_tau_full: 0.3851
202	  sj_auroc_full: 0.8008
203	  sj_rho_cond: 0.4511
204	  fk_rho_full: 0.3998
205	  fk_tau_full: 0.3568
206	  fk_auroc_full: 0.7741
207	  fk_rho_cond: 0.4064
208	  logprob_rho_full: 0.3157
209	  logprob_tau_full: 0.2469
210	  logprob_auroc_full: 0.7532
211	  logprob_rho_cond: 0.3562
212	  em_rho_full: 0.4507
213	  em_tau_full: 0.4002
214	  em_auroc_full: 0.8156
215	  em_rho_cond: 0.4799
216	  ev_rho_full: 0.4237
217	  ev_tau_full: 0.3777
218	  ev_auroc_full: 0.7889
219	  ev_rho_cond: 0.4127
220	  greedy_f1: 0.9123
221	  oracle_f1: 0.9543
222	  voting_f1: 0.9141
223	  oracle_headroom: 0.042
224	  sj_vs_logprob_delta_rho: 0.12
225	  sj_vs_logprob_ci_low: 0.0881
226	  sj_vs_logprob_ci_high: 0.154
227	  sj_vs_logprob_significant: True
228	  n_instances: 3453
229	  n_valid: 2756
230	  n_samples: 8
231	  temperature: 1
232	
233	────────────────────────────────────────────────────────────────────────────────────────────────────
234	EXP_ID: exp_002_conll_n16
235	STATUS: DONE
236	CONCLUSION: success
237	HYPOTHESIS: CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).
238	METRICS:
239	  degen_rate: 0.4844
240	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
241	  N: 16
242	  dataset: conll2003
243	  subtask: ner
244	  n_instances: 3453
245	  n_valid: 2756
246	  n_conditional: 2614
247	  greedy_f1: 0.907
248	  full: {'SJ_rho': 0.4496, 'FK_rho': 0.3928, 'logprob_rho': 0.3146, 'EM_rho': 0.4627, 'voting_conf_rho': 0.4286, 'SJ_AUROC': 0.8264, 'FK_AUROC': 0.7821, 'logprob_AUROC': 0.7531, 'EM_AUROC': 0.8409, 'voting_conf_AUROC': 0.8071, 'SJ_ECE': 0.0747, 'FK_ECE': 0.1786, 'logprob_ECE': 0.2031, 'EM_ECE': 0.0786, 'voting_conf_ECE': 0.529}
249	  conditional: {'SJ_rho': 0.4208, 'FK_rho': 0.3494, 'logprob_rho': 0.3756, 'EM_rho': 0.4658, 'voting_conf_rho': 0.3654, 'SJ_AUROC': 0.8405, 'FK_AUROC': 0.7819, 'logprob_AUROC': 0.8259, 'EM_AUROC': 0.8781, 'voting_conf_AUROC': 0.7951, 'SJ_ECE': 0.0982, 'FK_ECE': 0.1899, 'logprob_ECE': 0.2504, 'EM_ECE': 0.0997, 'voting_conf_ECE': 0.6096}
250	  n8_vs_n16_delta_rho_full: {'SJ': 0.0139, 'FK': -0.007, 'logprob': -0.0011, 'EM': 0.012, 'voting_conf': 0.0049}
251	
252	────────────────────────────────────────────────────────────────────────────────────────────────────
253	EXP_ID: exp_002_conll_n16_seed123
254	STATUS: DONE
255	CONCLUSION: success
256	HYPOTHESIS: Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.
257	METRICS:
258	  degen_rate: 0.471
259	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
260	  instance_count: 3453
261	  n_valid: 2756
262	  n_gold_empty: 697
263	  ner_greedy_f1: 0.9068
264	  ner_oracle_f1: 0.9633
265	  rho_fk_ner: 0.4524
266	  rho_sj_ner: 0.4621
267	  sample_f1_pct_zero: 7.54
268	
269	────────────────────────────────────────────────────────────────────────────────────────────────────
270	EXP_ID: exp_002_conll_n16_seed456
271	STATUS: DONE
272	CONCLUSION: success
273	HYPOTHESIS: Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.
274	METRICS:
275	  degen_rate: 0.5544
276	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
277	  instance_count: 3453
278	  n_valid: 2756
279	  n_gold_empty: 697
280	  ner_greedy_f1: 0.9074
281	  ner_oracle_f1: 0.9549
282	  rho_fk_ner: 0.4718
283	  rho_sj_ner: 0.4819
284	  sample_f1_pct_zero: 7.02
285	
286	────────────────────────────────────────────────────────────────────────────────────────────────────
287	EXP_ID: exp_003_ner_wnut17
288	STATUS: DONE
289	CONCLUSION: negative
290	HYPOTHESIS: WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.
291	METRICS:
292	  ner: {'greedy_f1': 0.525, 'oracle_f1': 0.664, 'headroom': 0.139, 'rho_sj_full': 0.082, 'rho_fk_full': 0.124, 'rho_logprob_full': -0.414, 'rho_sj_cond': 0.275, 'rho_fk_cond': 0.164, 'rho_logprob_cond': 0.352, 'sj_beats_logprob_cond': False}
293	  n_instances: 1287
294	  n_gold_empty: 598
295	  sample_f1_mean: 0.401
296	  sample_f1_pct_zero: 53.7
297	  N: 16
298	  T: 1
299	  seed: 42
300	  verdict: FAIL
301	  verdict_note: >30% samples F1=0; structural rho weak; logprob baseline stronger
302	
303	────────────────────────────────────────────────────────────────────────────────────────────────────
304	EXP_ID: exp_003_wnut17_eval
305	STATUS: DONE
306	CONCLUSION: success
307	HYPOTHESIS: WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.
308	METRICS:
309	  greedy_f1: 0.523
310	  oracle_f1: 0.664
311	  headroom: 0.141
312	  rho_fk: 0.125
313	  rho_sj: 0.089
314	  rho_fk_cond: 0.169
315	  rho_sj_cond: 0.288
316	  rho_logprob_full: -0.409
317	  rho_logprob_cond: 0.35
318	  structural_beats_surface: False
319	  sample_f1_pct_zero: 53.7
320	  n_instances: 1287
321	  N: 16
322	  T: 1
323	  seed: 42
324	  model: Qwen3-8B
325	  n_gold_empty_filtered: 598
326	  verdict: FAIL
327	  verdict_note: structural_beats_surface=false; >50% samples F1=0
328	
329	────────────────────────────────────────────────────────────────────────────────────────────────────
330	EXP_ID: exp_004_re_diagnostic
331	STATUS: DONE
332	CONCLUSION: success
333	METRICS:
334	  per_relation_type: {'HYPONYM-OF': {'n': 36, 'rho_sj': 0.545, 'rho_fk': 0.646, 'rho_vc': 0.628, 'mean_f1': 0.513}, 'CONJUNCTION': {'n': 86, 'rho_sj': 0.383, 'rho_fk': 0.35, 'rho_vc': 0.484, 'mean_f1': 0.48}, 'USED-FOR': {'n': 299, 'rho_sj': 0.236, 'rho_fk': 0.255, 'rho_vc': 0.286, 'mean_f1': 0.422}, 'PART-OF': {'n': 44, 'rho_sj': 0.239, 'rho_fk': 0.348, 'rho_vc': 0.283, 'mean_f1': 0.297}, 'EVALUATE-FOR': {'n': 62, 'rho_sj': 0.172, 'rho_fk': 0.255, 'rho_vc': 0.226, 'mean_f1': 0.365}, 'COMPARE': {'n': 35, 'rho_sj': 0.168, 'rho_fk': 0.184, 'rho_vc': 0.18, 'mean_f1': 0.453}, 'FEATURE-OF': {'n': 50, 'rho_sj': 0.004, 'rho_fk': 0.052, 'rho_vc': 0.014, 'mean_f1': 0.254}}
335	  error_propagation: {'total_fn': 553, 'tail_error_pct': 21.9, 'full_error_pct': 21.7, 'head_error_pct': 17.7, 'head_tail_error_pct': 15.9, 'type_error_pct': 8.3, 'worst_consistency': 'head_type_error (sj=0.411)', 'best_consistency': 'head_error (sj=0.613)'}
336	  threshold_sensitivity: {'thr_0.00_rho_sj': 0.3161, 'thr_0.00_rho_vc': 0.3841, 'thr_0.00_n': 313, 'thr_0.05_rho_sj': 0.2682, 'thr_0.05_rho_vc': 0.2364, 'thr_0.05_n': 239}
337	  bootstrap_ci_95: {'ner_sj': [0.2946, 0.4586], 'ner_voting_conf': [0.3048, 0.4656], 're_sj': [0.1422, 0.3391], 're_voting_conf': [0.1818, 0.3721], 're_cond_sj': [0.2161, 0.4102], 're_cond_voting_conf': [0.2825, 0.474]}
338	  fisher_z_ner_vs_re: {'sj_z': 2.31, 'sj_p': 0.0209, 'sj_significant': True, 'fk_z': -0.31, 'fk_p': 0.756, 'fk_significant': False, 'voting_z': 1.914, 'voting_p': 0.0556, 'voting_significant': False}
339	  diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).
340	
341	────────────────────────────────────────────────────────────────────────────────────────────────────
342	EXP_ID: exp_006_v2
343	STATUS: DONE
344	CONCLUSION: negative
345	HYPOTHESIS: Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.
346	METRICS:
347	  NER_SciERC_s42: {'greedy': 0.618, 'oracle': 0.787, 'SJ': 0.62, 'logprob': 0.621, 'FK': 0.621, 'EM': 0.606, 'voting_conf': 0.585, 'random': 0.586}
348	  NER_SciERC_s123: {'greedy': 0.618, 'oracle': 0.785, 'SJ': 0.617, 'logprob': 0.618, 'FK': 0.621, 'EM': 0.613, 'voting_conf': 0.584, 'random': 0.583}
349	  NER_CoNLL: {'greedy': 0.725, 'oracle': 0.757, 'SJ': 0.718, 'logprob': 0.716, 'FK': 0.717, 'EM': 0.716, 'voting_conf': 0.714, 'random': 0.692}
350	  RE_SciERC: {'greedy': 0.403, 'oracle': 0.631, 'SJ': 0.397, 'logprob': 0.41, 'FK': 0.396, 'EM': 0.381, 'voting_conf': 0.408, 'random': 0.364}
351	
352	────────────────────────────────────────────────────────────────────────────────────────────────────
353	EXP_ID: exp_007_llama_inference
354	STATUS: DONE
355	CONCLUSION: success
356	HYPOTHESIS: LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.
357	METRICS:
358	  ner: {'greedy_f1': 0.66, 'oracle_f1': 0.781, 'headroom': 0.121, 'rho_fk': 0.327, 'rho_sj': 0.363, 'rho_fk_cond': 0.226, 'rho_sj_cond': 0.311, 'rho_logprob': 0.183, 'rho_logprob_cond': 0.109, 'structural_beats_surface': True, 'sample_f1_pct_zero': 11.6}
359	  re: {'greedy_f1': 0.434, 'oracle_f1': 0.568, 'headroom': 0.135, 'rho_fk': 0.305, 'rho_sj': 0.299, 'rho_fk_cond': 0.259, 'rho_sj_cond': 0.405, 'rho_logprob': 0.288, 'rho_logprob_cond': 0.092, 'structural_beats_surface': False, 'sample_f1_pct_zero': 41.2}
360	  n_instances: 551
361	  N: 8
362	  T: 1
363	  seed: 42
364	  model: LLaMA-3.1-8B-Instruct
365	  verdict: FAIL
366	  verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0
367	
368	────────────────────────────────────────────────────────────────────────────────────────────────────
369	EXP_ID: exp_007_llama_n16
370	STATUS: DONE
371	CONCLUSION: success
372	HYPOTHESIS: LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.
373	METRICS:
374	  N: 16
375	  dataset: scierc
376	  subtask: ner
377	  n_instances: 551
378	  n_valid: 529
379	  n_conditional: 478
380	  greedy_f1: 0.645
381	  full: {'SJ_rho': 0.3791, 'FK_rho': 0.3081, 'logprob_rho': 0.2041, 'EM_rho': 0.3159, 'voting_conf_rho': 0.4515, 'SJ_AUROC': 0.717, 'FK_AUROC': 0.6581, 'logprob_AUROC': 0.5656, 'EM_AUROC': 0.7686, 'voting_conf_AUROC': 0.7266, 'SJ_ECE': 0.1019, 'FK_ECE': 0.1556, 'logprob_ECE': 0.084, 'EM_ECE': 0.1761, 'voting_conf_ECE': 0.1365}
382	  conditional: {'SJ_rho': 0.3222, 'FK_rho': 0.2182, 'logprob_rho': 0.1286, 'EM_rho': 0.3563, 'voting_conf_rho': 0.3356, 'SJ_AUROC': 0.7014, 'FK_AUROC': 0.6392, 'logprob_AUROC': 0.545, 'EM_AUROC': 0.7708, 'voting_conf_AUROC': 0.6988, 'SJ_ECE': 0.1466, 'FK_ECE': 0.1853, 'logprob_ECE': 0.1141, 'EM_ECE': 0.1887, 'voting_conf_ECE': 0.2634}
383	  n8_vs_n16_delta_rho_full: {'SJ': 0.0161, 'FK': -0.0185, 'logprob': 0.0214, 'EM': 0.0007, 'voting_conf': 0.0184}
384	
385	────────────────────────────────────────────────────────────────────────────────────────────────────
386	EXP_ID: exp_007_llama_scierc_seed123
387	STATUS: DONE
388	CONCLUSION: negative
389	HYPOTHESIS: Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline
390	METRICS:
391	  greedy_f1: 0.6454
392	  oracle_f1: 0.7657
393	  headroom: 0.1204
394	  degen_rate: 0.2665
395	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
396	  dgs_delta_pp: -0.38
397	  rho_SJ_full: 0.3552
398	  rho_voting_conf_full: 0.4193
399	  auroc_SJ_full: 0.7092
400	  auroc_EM_full: 0.7468
401	
402	────────────────────────────────────────────────────────────────────────────────────────────────────
403	EXP_ID: exp_007_llama_seed123
404	STATUS: DONE
405	CONCLUSION: negative
406	HYPOTHESIS: LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.
407	METRICS:
408	  verdict: FAIL
409	  ner: {'greedy_f1': 0.6605, 'oracle_f1': 0.7703, 'headroom': 0.1098, 'fleiss_kappa': 0.4553, 'soft_jaccard': 0.7525, 'rho_kappa_f1': 0.2143, 'rho_sj_f1': 0.3371, 'structural_gt_surface': True}
410	  re: {'greedy_f1': 0.433, 'oracle_f1': 0.5719, 'headroom': 0.1389, 'fleiss_kappa': 0.3851, 'soft_jaccard': 0.6911, 'rho_kappa_f1': 0.2844, 'rho_sj_f1': 0.268, 'structural_gt_surface': False}
411	  fail_reasons: ['RE rho_sj=0.2680 < 0.40 threshold', '>30% samples F1=0 (RE: 41.0%)', 'RE structural not > surface (delta=-0.0165)']
412	
413	────────────────────────────────────────────────────────────────────────────────────────────────────
414	EXP_ID: exp_007_llama_seed456
415	STATUS: DONE
416	CONCLUSION: negative
417	HYPOTHESIS: LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.
418	METRICS:
419	  verdict: FAIL
420	  ner: {'greedy_f1': 0.6597, 'oracle_f1': 0.7575, 'oracle_headroom': 0.0978, 'fleiss_kappa': 0.4543, 'soft_jaccard': 0.7491, 'rho_kappa_f1': 0.3115, 'rho_sj_f1': 0.3663, 'structural_gt_surface': True}
421	  re: {'greedy_f1': 0.4334, 'oracle_f1': 0.5789, 'oracle_headroom': 0.1455, 'fleiss_kappa': 0.3791, 'soft_jaccard': 0.6782, 'rho_kappa_f1': 0.3013, 'rho_sj_f1': 0.287, 'structural_gt_surface': False}
422	  logprob_ner: {'rho': 0.1911, 'auroc': 0.5989}
423	  logprob_re: {'rho': 0.3246, 'auroc': 0.6678}
424	  fail_reason: RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0
425	
426	────────────────────────────────────────────────────────────────────────────────────────────────────
427	EXP_ID: exp_007_ner_multi_model
428	STATUS: DONE
429	CONCLUSION: success
430	HYPOTHESIS: Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.
431	METRICS:
432	  epoch: 5
433	  train_loss: 0.0767
434	  eval_loss: 0.1049
435	  train_runtime_sec: 1494.5
436	  train_samples_per_second: 6.226
437	  checkpoints: ['checkpoint-400', 'checkpoint-500', 'checkpoint-585']
438	  base_model: Meta-Llama-3.1-8B-Instruct
439	  lora_r: 32
440	  lora_alpha: 64
441	  note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.
442	
443	────────────────────────────────────────────────────────────────────────────────────────────────────
444	EXP_ID: exp_008_re_n16
445	STATUS: DONE
446	CONCLUSION: success
447	HYPOTHESIS: RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.
448	METRICS:
449	  ner: {'greedy_f1': 0.6635, 'oracle_f1': 0.8208, 'headroom': 0.1572, 'rho_sj_full': 0.377, 'rho_fk_full': 0.2508, 'rho_logprob_full': 0.3153, 'rho_sj_cond': 0.3598, 'rho_fk_cond': 0.2251, 'rho_logprob_cond': 0.2927, 'sj_beats_fk': True, 'rho_advantage': 0.1262}
450	  re: {'greedy_f1': 0.4339, 'oracle_f1': 0.6658, 'headroom': 0.2319, 'rho_sj_full': 0.2966, 'rho_fk_full': 0.2871, 'rho_logprob_full': 0.2986, 'rho_sj_cond': 0.3975, 'rho_fk_cond': 0.3774, 'rho_logprob_cond': 0.2745, 'sj_beats_fk': True, 'rho_advantage': 0.0095}
451	  verdict: FAIL
452	
453	────────────────────────────────────────────────────────────────────────────────────────────────────
454	EXP_ID: exp_008_re_n16_t10_full
455	STATUS: DONE
456	CONCLUSION: negative
457	HYPOTHESIS: RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.
458	METRICS:
459	  ner: {'rho_sj': 0.444}
460	  re: {'rho_sj': 0.248}
461	  n_instances: 551
462	  N: 16
463	  T: 1
464	  seed: 42
465	  mode: RE-only
466	  source: director_corrected
467	
468	────────────────────────────────────────────────────────────────────────────────────────────────────
469	EXP_ID: exp_008_re_n16_v2
470	STATUS: DONE
471	CONCLUSION: negative
472	HYPOTHESIS: RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.
473	METRICS:
474	  sj_rho_full: 0.281
475	  sj_rho_cond: 0.308
476	  f1_zero_pct: 44.3
477	  conclusion_note: RE N=16 v2 negative: SJ weak, 44.3% F1=0
478	
479	────────────────────────────────────────────────────────────────────────────────────────────────────
480	EXP_ID: exp_008_re_seed123
481	STATUS: DONE
482	CONCLUSION: negative
483	HYPOTHESIS: RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.
484	METRICS:
485	  greedy_f1: 0.4229
486	  oracle_f1: 0.6244
487	  oracle_headroom: 0.2015
488	  fleiss_kappa_mean: 0.3455
489	  soft_jaccard_mean: 0.6126
490	  sample_f1_mean: 0.3594
491	  sample_f1_std: 0.3793
492	  sample_f1_zero_pct: 44.1
493	  structural_gt_surface: False
494	  rho_kappa_f1_full: 0.3174
495	  rho_sj_f1_full: 0.2835
496	  rho_kappa_f1_cond: 0.0766
497	  rho_sj_f1_cond: 0.2877
498	  logprob_auroc_full: 0.6499
499	  logprob_auroc_cond: 0.5265
500	  verdict: FAIL
501	
502	────────────────────────────────────────────────────────────────────────────────────────────────────
503	EXP_ID: exp_009_capability_stratification
504	STATUS: DONE
505	CONCLUSION: success
506	HYPOTHESIS: Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.
507	NOTES: Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.
508	METRICS:
509	  scierc_ner: {'n': 551, 'sj_rho_overall': 0.398, 'by_greedy_f1': {'hard_0_25_sj_rho': 0.159, 'med_low_sj_rho': 0.139, 'med_high_sj_rho': 0.09, 'easy_sj_rho': 0.23}, 'by_sent_len': {'Q1_sj_rho': 0.461, 'Q2_sj_rho': 0.401, 'Q3_sj_rho': 0.296, 'Q4_sj_rho': 0.382}, 'by_ent_count': {'0_sj_rho': 0.689, '1_2_sj_rho': 0.415, '3_5_sj_rho': 0.353, '6plus_sj_rho': 0.547}}
510	  scierc_re: {'n': 551, 'by_greedy_f1': {'hard_0_25_sj_rho': -0.043, 'easy_sj_rho': 0.21}, 'by_sent_len': {'Q1_sj_rho': 0.447, 'Q4_sj_rho': 0.54}, 'by_rel_count': {'0_sj_rho': 0.62, '1_2_sj_rho': 0.275, '6plus_sj_rho': 0.527}}
511	  conll_ner: {'n': 3453, 'by_sent_len': {'Q1_sj_rho': 0.334, 'Q3_sj_rho': 0.518}}
512	  proxy_independence: {'scierc_ner_f1_vs_slen': -0.021, 'scierc_ner_f1_vs_ecnt': 0.007, 'scierc_re_f1_vs_slen': -0.147}
513	
514	────────────────────────────────────────────────────────────────────────────────────────────────────
515	EXP_ID: exp_009_v2
516	STATUS: DONE
517	CONCLUSION: success
518	HYPOTHESIS: Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.
519	METRICS:
520	  ner_seed42_global: {'sj_rho': 0.431, 'fk_rho': 0.325, 'logprob_rho': 0.203, 'voting_conf_rho': 0.475, 'em_rho': 0.292}
521	  ner_seed123_global: {'sj_rho': 0.422, 'fk_rho': 0.315, 'logprob_rho': 0.226, 'voting_conf_rho': 0.438, 'em_rho': 0.299}
522	  re_seed42_global: {'sj_rho': 0.063, 'fk_rho': 0.226, 'logprob_rho': 0.4, 'voting_conf_rho': 0.22, 'em_rho': -0.132}
523	  ner_seed_stability_max_delta: 0.037
524	  independent_proxies: ['sent_len', 'ent_count', 'type_diversity']
525	  inverted_u_ner: not confirmed (ρ stable across independent proxies)
526	  inverted_u_re: monotonic increase with complexity, not inverted-U
527	
528	────────────────────────────────────────────────────────────────────────────────────────────────────
529	EXP_ID: exp_010_selection_curves
530	STATUS: DONE
531	CONCLUSION: success
532	HYPOTHESIS: Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.
533	METRICS:
534	  scierc_ner: {'n_instances': 551, 'greedy_f1': 0.618, 'N16': {'oracle': 0.787, 'SJ': 0.62, 'FK': 0.621, 'logprob': 0.621, 'voting_conf': 0.585, 'EM': 0.606, 'random': 0.595}, 'N8': {'oracle': 0.752, 'SJ': 0.614, 'FK': 0.614, 'logprob': 0.619, 'voting_conf': 0.591, 'EM': 0.603, 'random': 0.589}, 'N4': {'oracle': 0.714, 'SJ': 0.607, 'FK': 0.608, 'logprob': 0.616, 'voting_conf': 0.594, 'EM': 0.6, 'random': 0.587}}
535	  scierc_re: {'n_instances': 397, 'greedy_f1': 0.403, 'N16': {'oracle': 0.631, 'SJ': 0.397, 'FK': 0.396, 'logprob': 0.41, 'voting_conf': 0.408, 'EM': 0.381, 'random': 0.364}, 'N8': {'oracle': 0.583, 'SJ': 0.393, 'FK': 0.394, 'logprob': 0.413, 'voting_conf': 0.398, 'EM': 0.381, 'random': 0.363}}
536	  conll_ner: {'n_instances': 3453, 'greedy_f1': 0.725, 'N8': {'oracle': 0.757, 'SJ': 0.718, 'FK': 0.717, 'logprob': 0.716, 'voting_conf': 0.714, 'EM': 0.716, 'random': 0.69}, 'N4': {'oracle': 0.746, 'SJ': 0.714, 'FK': 0.714, 'logprob': 0.715, 'voting_conf': 0.714, 'EM': 0.712, 'random': 0.692}}
537	
538	────────────────────────────────────────────────────────────────────────────────────────────────────
539	EXP_ID: exp_011_ood_conll_to_scierc
540	STATUS: DONE
541	CONCLUSION: negative
542	HYPOTHESIS: Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).
543	METRICS:
544	  greedy_ner_f1: 0.009
545	  greedy_re_f1: 0.001
546	  avg_structural_rho: -0.05
547	  verdict: FAIL
548	  reason: schema_incompatibility
549	  direction: CoNLL_model_to_SciERC_data
550	  sample_f1_pct_zero_ner: 98.06
551	  rho_sj_ner: -0.186
552	  rho_fk_ner: -0.069
553	  note: Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.
554	
555	────────────────────────────────────────────────────────────────────────────────────────────────────
556	EXP_ID: exp_011_ood_scierc_to_conll
557	STATUS: DONE
558	CONCLUSION: success
559	HYPOTHESIS: Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.
560	METRICS:
561	  greedy_ner_f1: 0.522
562	  rho_vc: 0.469
563	  rho_sj: 0.378
564	  rho_em: 0.3
565	  rho_fk: 0.285
566	  rho_lp: 0.246
567	
568	────────────────────────────────────────────────────────────────────────────────────────────────────
569	EXP_ID: exp_012_logprob_baseline
570	STATUS: DONE
571	CONCLUSION: success
572	METRICS:
573	  ner_full_rho_sj: 0.3565
574	  ner_full_rho_fk: 0.2651
575	  ner_full_rho_logprob: 0.1396
576	  ner_full_rho_greedy_logprob: 0.1615
577	  ner_full_tau_sj: 0.2658
578	  ner_full_tau_logprob: 0.1006
579	  ner_full_auroc_sj: 0.6892
580	  ner_full_auroc_fk: 0.6292
581	  ner_full_auroc_logprob: 0.5907
582	  ner_full_n: 529
583	  ner_sj_vs_logprob_delta: 0.2169
584	  re_full_rho_sj: 0.2112
585	  re_full_rho_fk: 0.2528
586	  re_full_rho_logprob: 0.2467
587	  re_full_auroc_sj: 0.5916
588	  re_full_auroc_fk: 0.6262
589	  re_full_auroc_logprob: 0.6186
590	  re_full_n: 397
591	  re_cond_rho_sj: 0.3683
592	  re_cond_rho_fk: 0.3168
593	  re_cond_rho_logprob: 0.1457
594	  re_cond_auroc_sj: 0.6839
595	  re_cond_auroc_logprob: 0.5487
596	  re_cond_n: 296
597	  diagnosis: NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.
598	
599	────────────────────────────────────────────────────────────────────────────────────────────────────
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "db1bb0b9-f323-48cc-acfc-77febf3ea0ea"
}
```

</details>

---


### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 39652,
    "tool_uses": 11,
    "duration_ms": 105511
  },
  "last_tool_name": "Read",
  "uuid": "f7659808-8eb0-432f-a585-241cf939cdc2",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01X9YxgoPqKRzva6kXS1Qd7s`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 599,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "1ec56dda-116c-4fe4-be47-e5b1bb868e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtTfG5gD59mC9DLZyoswUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11334,
      "cache_read_input_tokens": 28027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11334,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-22T18:19:32.281Z_

<details><summary>↩ Tool result · `toolu_01X9YxgoPqKRzva6kXS1Qd7s`</summary>

```text
599	────────────────────────────────────────────────────────────────────────────────────────────────────
600	EXP_ID: exp_012_rerun_1024
601	STATUS: DONE
602	CONCLUSION: success
603	HYPOTHESIS: Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.
604	METRICS:
605	  degen_rate: 0.1777
606	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
607	  ner_full: {'n': 529, 'SJ': {'rho': 0.3599, 'tau': 0.2646, 'AUROC': 0.6917, 'ECE': 0.4531, 'rho_ci95': [0.2732, 0.4389], 'AUROC_ci95': [0.6304, 0.7406]}, 'FK': {'rho': 0.2665, 'tau': 0.1974, 'AUROC': 0.629, 'ECE': 0.4512, 'rho_ci95': [0.1743, 0.3486], 'AUROC_ci95': [0.5612, 0.6882]}, 'logprob': {'rho': 0.2052, 'tau': 0.1478, 'AUROC': 0.5783, 'ECE': 0.7064, 'rho_ci95': [0.1171, 0.2904], 'AUROC_ci95': [0.5179, 0.6387]}, 'EM': {'rho': 0.2945, 'tau': 0.2208, 'AUROC': 0.7493, 'ECE': 0.3526, 'rho_ci95': [0.2094, 0.37], 'AUROC_ci95': [0.7002, 0.7928]}, 'voting_conf': {'rho': 0.3792, 'tau': 0.2805, 'AUROC': 0.6841, 'ECE': 0.3807, 'rho_ci95': [0.2972, 0.4486], 'AUROC_ci95': [0.6249, 0.7366]}}
608	  ner_cond: {'n': 477, 'SJ': {'rho': 0.3113, 'tau': 0.2257, 'AUROC': 0.6772, 'ECE': 0.4416, 'rho_ci95': [0.2353, 0.3959], 'AUROC_ci95': [0.621, 0.7337]}, 'FK': {'rho': 0.1761, 'tau': 0.1284, 'AUROC': 0.6078, 'ECE': 0.4389, 'rho_ci95': [0.0839, 0.2665], 'AUROC_ci95': [0.5442, 0.6709]}, 'logprob': {'rho': 0.1538, 'tau': 0.1111, 'AUROC': 0.5633, 'ECE': 0.6803, 'rho_ci95': [0.0637, 0.2424], 'AUROC_ci95': [0.5032, 0.6232]}, 'EM': {'rho': 0.3596, 'tau': 0.2735, 'AUROC': 0.7556, 'ECE': 0.3257, 'rho_ci95': [0.2819, 0.4408], 'AUROC_ci95': [0.7011, 0.8107]}, 'voting_conf': {'rho': 0.3, 'tau': 0.2189, 'AUROC': 0.6618, 'ECE': 0.3746, 'rho_ci95': [0.2168, 0.3836], 'AUROC_ci95': [0.6004, 0.7201]}}
609	  re_full: {'n': 397, 'SJ': {'rho': 0.2503, 'tau': 0.1878, 'AUROC': 0.6702, 'ECE': 0.3865}, 'FK': {'rho': 0.2752, 'tau': 0.2117, 'AUROC': 0.6089, 'ECE': 0.4405}, 'logprob': {'rho': 0.2662, 'tau': 0.1951, 'AUROC': 0.6005, 'ECE': 0.7694}, 'EM': {'rho': 0.1344, 'tau': 0.1081, 'AUROC': 0.7059, 'ECE': 0.3548}, 'voting_conf': {'rho': 0.3498, 'tau': 0.2663, 'AUROC': 0.6935, 'ECE': 0.2724}}
610	  re_cond: {'n': 238, 'SJ': {'rho': 0.2457, 'tau': 0.1811, 'AUROC': 0.6463, 'ECE': 0.2941}, 'FK': {'rho': 0.1139, 'tau': 0.0876, 'AUROC': 0.551, 'ECE': 0.3424}, 'logprob': {'rho': 0.0112, 'tau': 0.0051, 'AUROC': 0.5186, 'ECE': 0.6464}, 'EM': {'rho': 0.4165, 'tau': 0.3256, 'AUROC': 0.7515, 'ECE': 0.2232}, 'voting_conf': {'rho': 0.2409, 'tau': 0.178, 'AUROC': 0.642, 'ECE': 0.207}}
611	  delta_vs_512_ner_full_rho: {'SJ': 0.0034, 'FK': 0.0014, 'EM': 0.0379, 'voting_conf': -0.1226, 'logprob': 0.0656}
612	  provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.
613	
614	────────────────────────────────────────────────────────────────────────────────────────────────────
615	EXP_ID: exp_013_exact_match_voting
616	STATUS: DONE
617	CONCLUSION: negative
618	METRICS:
619	  ner_full_rho: 0.2941
620	  ner_full_p: 5.12e-12
621	  ner_full_tau: 0.2181
622	  ner_full_auroc: 0.6398
623	  re_full_rho: 0.1562
624	  re_full_p: 0.0018
625	  re_full_tau: 0.1185
626	  re_full_auroc: 0.5863
627	  diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.
628	
629	────────────────────────────────────────────────────────────────────────────────────────────────────
630	EXP_ID: exp_014_entity_majority_voting
631	STATUS: DONE
632	CONCLUSION: success
633	METRICS:
634	  ner_full_rho: 0.3915
635	  ner_full_p: 8.1e-21
636	  ner_full_tau: 0.2906
637	  ner_full_auroc: 0.7039
638	  re_full_rho: 0.3403
639	  re_full_p: 3.21e-12
640	  re_full_tau: 0.256
641	  re_full_auroc: 0.6668
642	  ner_voting_f1: 0.6246
643	  ner_greedy_f1: 0.6483
644	  ner_oracle_f1: 0.7793
645	  re_voting_f1: 0.3577
646	  re_greedy_f1: 0.4022
647	  re_oracle_f1: 0.5886
648	  diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.
649	
650	────────────────────────────────────────────────────────────────────────────────────────────────────
651	EXP_ID: exp_015_metrics_expansion
652	STATUS: DONE
653	CONCLUSION: success
654	HYPOTHESIS: Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.
655	NOTES: RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.
656	METRICS:
657	  data_source: exp_012_logprob/samples_with_logprobs.jsonl
658	  config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2
659	  ner: {'n_valid': 529, 'n_cond': 501, 'voting_rho_full': 0.5018, 'voting_rho_cond': 0.4497, 'voting_auroc': 0.7279, 'voting_tau': 0.3766, 'sj_rho_full': 0.3565, 'sj_rho_cond': 0.412, 'sj_auroc': 0.6656, 'sj_tau': 0.2658, 'em_rho_full': 0.2566, 'em_rho_cond': 0.3427, 'em_auroc': 0.623, 'em_tau': 0.1924, 'fk_rho_full': 0.2651, 'fk_rho_cond': 0.306, 'fk_auroc': 0.6243, 'fk_tau': 0.2027, 'logprob_rho_full': 0.1396, 'logprob_rho_cond': 0.1627, 'logprob_auroc': 0.5585, 'logprob_tau': 0.1006}
660	  re: {'n_valid': 397, 'n_cond': 296, 'voting_rho_full': 0.4217, 'voting_rho_cond': 0.463, 'voting_auroc': 0.7162, 'voting_tau': 0.327, 'sj_rho_full': 0.2112, 'sj_rho_cond': 0.3683, 'sj_auroc': 0.5816, 'sj_tau': 0.1619, 'em_rho_full': 0.1002, 'em_rho_cond': 0.3607, 'em_auroc': 0.5036, 'em_tau': 0.0839, 'fk_rho_full': 0.2528, 'fk_rho_cond': 0.3168, 'fk_auroc': 0.6308, 'fk_tau': 0.1967, 'logprob_rho_full': 0.2467, 'logprob_rho_cond': 0.1457, 'logprob_auroc': 0.6354, 'logprob_tau': 0.1808}
661	  diagnosis: Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.
662	
663	────────────────────────────────────────────────────────────────────────────────────────────────────
664	EXP_ID: exp_015_v2
665	STATUS: DONE
666	CONCLUSION: success
667	HYPOTHESIS: Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.
668	METRICS:
669	  scierc_ner_avg: {'sj_auroc': 0.7394, 'fk_auroc': 0.6172, 'em_auroc': 0.7873, 'voting_auroc': 0.7367, 'logprob_auroc': 0.5918}
670	  scierc_re_avg: {'sj_auroc': 0.6746, 'fk_auroc': 0.5939, 'em_auroc': 0.715, 'voting_auroc': 0.7234, 'logprob_auroc': 0.5849}
671	
672	────────────────────────────────────────────────────────────────────────────────────────────────────
673	EXP_ID: exp_016_rerun_1024_bootstrap
674	STATUS: DONE
675	CONCLUSION: negative
676	HYPOTHESIS: 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.
677	METRICS:
678	  bootstrap_ci_95: [-0.03, 0.042]
679	  permutation_p: 0.39
680	  cohen_d: 0.038
681	  sign_test_win_rate: 0.466
682	  ner_logprob_vs_greedy_delta: 0.006
683	  conclusion_summary: NER selection: no signal significantly outperforms greedy; RE: same conclusion
684	
685	────────────────────────────────────────────────────────────────────────────────────────────────────
686	EXP_ID: exp_016_signal_ensemble
687	STATUS: DONE
688	CONCLUSION: success
689	METRICS:
690	  sj_logprob_pearson_ner: 0.57
691	  sj_logprob_pearson_re: 0.42
692	  best_linear_ner: {'combo': 'SJ+voting_conf', 'alpha': 0.3, 'rho': 0.489}
693	  best_linear_re: {'combo': 'voting_conf+logprob', 'alpha': 0.6, 'rho': 0.429}
694	  ensemble_ner_auroc: 0.735
695	  ensemble_re_auroc: 0.719
696	  best_single_ner_auroc: 0.7
697	  best_single_re_auroc: 0.721
698	  ensemble_ner_delta: 0.035
699	  selection_f1_ner: {'greedy': 0.609, 'logprob': 0.609, 'sj': 0.604, 'ensemble': 0.604, 'voting': 0.596, 'random': 0.58, 'oracle': 0.769}
700	  selection_f1_re: {'logprob': 0.397, 'greedy': 0.374, 'sj': 0.368, 'ensemble': 0.367, 'voting': 0.338, 'random': 0.338, 'oracle': 0.561}
701	  diagnosis: SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.
702	
703	────────────────────────────────────────────────────────────────────────────────────────────────────
704	EXP_ID: exp_016_v2
705	STATUS: DONE
706	CONCLUSION: success
707	HYPOTHESIS: Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.
708	METRICS:
709	  ner_conditional: {'n': 529, 'best_single_signal_rho': {'soft_jaccard': 0.4412}, 'best_combo_rho': {'sj+vc_a0.55': 0.4552}, 'ensemble_auroc': 0.7141, 'best_single_auroc': {'soft_jaccard': 0.7166}, 'selection_f1': {'greedy': 0.6442, 'logprob_best': 0.6505, 'ensemble_best': 0.6475, 'sj_best': 0.6471, 'oracle': 0.8442}}
710	  re_conditional: {'n': 397, 'best_single_signal_rho': {'voting_confidence': 0.3849}, 'best_combo_rho': {'logprob+vc_a0.25': 0.3936}, 'ensemble_auroc': 0.6916, 'best_single_auroc': {'voting_confidence': 0.7023}, 'selection_f1': {'greedy': 0.403, 'logprob_best': 0.4097, 'ensemble_best': 0.4227, 'oracle': 0.6306}}
711	  re_full: {'ensemble_auroc': 0.8608, 'best_single_auroc': {'voting_confidence': 0.8248}}
712	
713	────────────────────────────────────────────────────────────────────────────────────────────────────
714	EXP_ID: exp_017_llama_conll
715	STATUS: DONE
716	CONCLUSION: success
717	HYPOTHESIS: On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.
718	METRICS:
719	  degeneracy_cf1_gold_filtered: 0.894
720	  n_constant_f1: 2465
721	  n_gold_filtered: 2756
722	  n_total: 3453
723	  greedy_f1: 0.9239
724	  oracle_f1: 0.9451
725	  random_f1: 0.9207
726	  headroom_pp: 2.11
727	  dgs_f1: 0.9254
728	  dgs_delta_pp: 0.14
729	  dgs_nondegen_lp_delta_pp: 1.37
730	  selection_f1: {'SJ': {'f1': 0.9237, 'delta_pp': -0.04}, 'FK': {'f1': 0.924, 'delta_pp': -0.02}, 'VC': {'f1': 0.925, 'delta_pp': 0.08}, 'EM': {'f1': 0.9244, 'delta_pp': 0.02}, 'LP': {'f1': 0.9244, 'delta_pp': 0.02}}
731	  qe_rho_full_3seed: {'SJ': {'mean': 0.4631, 'sd': 0.0074}, 'FK': {'mean': 0.4546, 'sd': 0.0061}, 'EM': {'mean': 0.4603, 'sd': 0.0078}, 'VC': {'mean': 0.4579, 'sd': 0.003}, 'LP': {'mean': 0.3099, 'sd': 0.0055}}
732	  qe_auroc_full_3seed: {'SJ': {'mean': 0.736, 'sd': 0.0064}, 'FK': {'mean': 0.732, 'sd': 0.0063}, 'EM': {'mean': 0.7355, 'sd': 0.0069}, 'VC': {'mean': 0.7394, 'sd': 0.0041}, 'LP': {'mean': 0.7629, 'sd': 0.0044}}
733	  lp_range: {'mean': 0.0198, 'std': 0.0315, 'median': 0.0002}
734	
735	────────────────────────────────────────────────────────────────────────────────────────────────────
736	EXP_ID: exp_017_llama_conll_finetune
737	STATUS: DONE
738	CONCLUSION: success
739	HYPOTHESIS: Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.
740	METRICS:
741	  degeneracy_rate: 0.853
742	  greedy_f1: 0.928
743	  oracle_f1: 0.951
744	  headroom: 0.023
745	  selection_f1: 0.934
746	  full_rho_SJ: 0.45
747	  full_rho_FK: 0.443
748	  full_rho_VC: 0.437
749	  full_rho_EM: 0.448
750	  full_rho_LP: 0.273
751	  full_AUROC_SJ: 0.752
752	  full_AUROC_EM: 0.753
753	  full_AUROC_LP: 0.739
754	  cond_rho_SJ: 0.454
755	  cond_rho_EM: 0.458
756	  cond_rho_LP: 0.311
757	  cond_AUROC_EM: 0.783
758	  cond_AUROC_LP: 0.804
759	
760	────────────────────────────────────────────────────────────────────────────────────────────────────
761	EXP_ID: exp_017_llama_conll_infer
762	STATUS: DONE
763	CONCLUSION: success
764	HYPOTHESIS: LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.
765	NOTES: LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).
766	METRICS:
767	  greedy_f1: 0.9266
768	  oracle_f1: 0.9443
769	  oracle_headroom: 0.0177
770	  n_instances: 3453
771	  n_valid: 2756
772	  n_conditional: 2642
773	  N: 8
774	  full: {'SJ_rho': 0.4314, 'FK_rho': 0.4277, 'logprob_rho': 0.3072, 'EM_rho': 0.4306, 'voting_conf_rho': 0.4256, 'SJ_AUROC': 0.7039, 'FK_AUROC': 0.7026, 'logprob_AUROC': 0.761, 'EM_AUROC': 0.7046, 'voting_conf_AUROC': 0.7088, 'SJ_ECE': 0.1137, 'FK_ECE': 0.1053, 'logprob_ECE': 0.129, 'EM_ECE': 0.1094, 'voting_conf_ECE': 0.0949}
775	  conditional: {'SJ_rho': 0.4356, 'FK_rho': 0.431, 'logprob_rho': 0.3282, 'EM_rho': 0.4403, 'voting_conf_rho': 0.3743, 'SJ_AUROC': 0.7225, 'FK_AUROC': 0.7208, 'logprob_AUROC': 0.8102, 'EM_AUROC': 0.7257, 'voting_conf_AUROC': 0.6989, 'SJ_ECE': 0.0829, 'FK_ECE': 0.0796, 'logprob_ECE': 0.0922, 'EM_ECE': 0.0754, 'voting_conf_ECE': 0.0784}
776	
777	────────────────────────────────────────────────────────────────────────────────────────────────────
778	EXP_ID: exp_017_llama_conll_n16
779	STATUS: DONE
780	CONCLUSION: success
781	HYPOTHESIS: LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.
782	METRICS:
783	  greedy_f1: 0.9243
784	  oracle_f1: 0.9487
785	  oracle_headroom: 0.0244
786	  n_instances: 3453
787	  n_valid: 2756
788	  n_conditional: 2642
789	  structural_beats_surface: True
790	  full: {'SJ_rho': 0.4642, 'SJ_AUROC': 0.7391, 'SJ_ECE': 0.1131, 'FK_rho': 0.4566, 'FK_AUROC': 0.736, 'FK_ECE': 0.1071, 'logprob_rho': 0.3058, 'logprob_AUROC': 0.7594, 'logprob_ECE': 0.1288, 'EM_rho': 0.4613, 'EM_AUROC': 0.7391, 'EM_ECE': 0.1084, 'voting_conf_rho': 0.4554, 'voting_conf_AUROC': 0.7406, 'voting_conf_ECE': 0.0844}
791	  conditional: {'SJ_rho': 0.4597, 'SJ_AUROC': 0.7565, 'SJ_ECE': 0.0846, 'FK_rho': 0.4515, 'FK_AUROC': 0.753, 'FK_ECE': 0.0813, 'logprob_rho': 0.3193, 'logprob_AUROC': 0.8023, 'logprob_ECE': 0.0921, 'EM_rho': 0.4618, 'EM_AUROC': 0.7589, 'EM_ECE': 0.0757, 'voting_conf_rho': 0.3978, 'voting_conf_AUROC': 0.7287, 'voting_conf_ECE': 0.0742}
792	  best_of_n: {'greedy': 0.9243, 'random_avg': 0.9213, 'sj_best': 0.9259, 'logprob_best': 0.925, 'voting_conf_best': 0.9268, 'oracle': 0.9487}
793	  n8_vs_n16_delta: {'full_SJ_rho_delta': 0.0328, 'full_FK_rho_delta': 0.0289, 'full_logprob_rho_delta': -0.0014, 'full_EM_rho_delta': 0.0307, 'full_voting_conf_rho_delta': 0.0298, 'cond_SJ_rho_delta': 0.0241, 'cond_FK_rho_delta': 0.0205, 'cond_logprob_rho_delta': -0.0089, 'cond_EM_rho_delta': 0.0215, 'cond_voting_conf_rho_delta': 0.0235}
794	
795	────────────────────────────────────────────────────────────────────────────────────────────────────
796	EXP_ID: exp_017_llama_conll_n16_r1024
797	STATUS: DONE
798	CONCLUSION: success
799	HYPOTHESIS: LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).
800	METRICS:
801	  degen_rate: 0.8647
802	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
803	  instance_count: 3453
804	  n_valid: 2756
805	  n_gold_empty: 697
806	  parse_rate: 1
807	  ner_greedy_f1: 0.9265
808	  ner_oracle_f1: 0.9499
809	  rho_fk_ner: 0.4752
810	  rho_sj_ner: 0.4836
811	  rho_vc_ner: 0.4746
812	  rho_em_ner: 0.4818
813	  rho_lp_ner: 0.3136
814	  auroc_fk_ner: 0.7467
815	  auroc_sj_ner: 0.7496
816	  auroc_vc_ner: 0.7529
817	  auroc_em_ner: 0.7508
818	  auroc_lp_ner: 0.7661
819	  auroc_note: median F1=1.0, AUROC uses >=median threshold
820	  rho_note: CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).
821	
822	────────────────────────────────────────────────────────────────────────────────────────────────────
823	EXP_ID: exp_017_llama_conll_n16_s123
824	STATUS: DONE
825	CONCLUSION: success
826	HYPOTHESIS: LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol
827	METRICS:
828	  greedy_f1: 0.9266
829	  oracle_f1: 0.9497
830	  oracle_headroom: 0.0231
831	  n_instances: 3453
832	  n_valid: 2756
833	  n_conditional: 2642
834	  structural_beats_surface: True
835	  full: {'SJ_rho': 0.4698, 'SJ_AUROC': 0.7402, 'SJ_ECE': 0.1135, 'FK_rho': 0.4594, 'FK_AUROC': 0.7351, 'FK_ECE': 0.1114, 'logprob_rho': 0.3161, 'logprob_AUROC': 0.768, 'logprob_ECE': 0.129, 'EM_rho': 0.4676, 'EM_AUROC': 0.7399, 'EM_ECE': 0.1082, 'voting_conf_rho': 0.4612, 'voting_conf_AUROC': 0.7429, 'voting_conf_ECE': 0.0832}
836	  conditional: {'SJ_rho': 0.4712, 'SJ_AUROC': 0.7609, 'SJ_ECE': 0.0828, 'FK_rho': 0.4595, 'FK_AUROC': 0.7547, 'FK_ECE': 0.0858, 'logprob_rho': 0.3314, 'logprob_AUROC': 0.8134, 'logprob_ECE': 0.0922, 'EM_rho': 0.4732, 'EM_AUROC': 0.7626, 'EM_ECE': 0.075, 'voting_conf_rho': 0.4086, 'voting_conf_AUROC': 0.7338, 'voting_conf_ECE': 0.0706}
837	  best_of_n: {'greedy': 0.9242, 'random_avg': 0.9216, 'sj_best': 0.9247, 'logprob_best': 0.9253, 'voting_conf_best': 0.9255, 'oracle': 0.9486}
838	  n8_vs_n16_delta: {'full_SJ_rho_delta': 0.0384, 'full_FK_rho_delta': 0.0317, 'full_logprob_rho_delta': 0.0089, 'full_SJ_AUROC_delta': 0.0363, 'full_FK_AUROC_delta': 0.0325, 'full_logprob_AUROC_delta': 0.007, 'cond_SJ_rho_delta': 0.0356, 'cond_FK_rho_delta': 0.0285, 'cond_logprob_rho_delta': 0.0032}
839	
840	────────────────────────────────────────────────────────────────────────────────────────────────────
841	EXP_ID: exp_017_llama_conll_n16_s123_r1024
842	STATUS: DONE
843	CONCLUSION: success
844	HYPOTHESIS: LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.
845	NOTES: Output exists on autodl-5090. Registry status corrected from killed to success.
846	METRICS:
847	  degen_rate: 0.8636
848	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
849	
850	────────────────────────────────────────────────────────────────────────────────────────────────────
851	EXP_ID: exp_017_llama_conll_n16_s456
852	STATUS: DONE
853	CONCLUSION: success
854	HYPOTHESIS: LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol
855	METRICS:
856	  greedy_f1: 0.9243
857	  oracle_f1: 0.9488
858	  oracle_headroom: 0.0245
859	  n_instances: 3453
860	  n_valid: 2756
861	  n_conditional: 2642
862	  structural_beats_surface: True
863	  full: {'SJ_rho': 0.4552, 'SJ_AUROC': 0.7288, 'SJ_ECE': 0.1134, 'FK_rho': 0.4478, 'FK_AUROC': 0.7248, 'FK_ECE': 0.109, 'logprob_rho': 0.3078, 'logprob_AUROC': 0.7612, 'logprob_ECE': 0.1289, 'EM_rho': 0.452, 'EM_AUROC': 0.7275, 'EM_ECE': 0.1082, 'voting_conf_rho': 0.4571, 'voting_conf_AUROC': 0.7348, 'voting_conf_ECE': 0.0863}
864	  conditional: {'SJ_rho': 0.4505, 'SJ_AUROC': 0.7449, 'SJ_ECE': 0.0826, 'FK_rho': 0.4422, 'FK_AUROC': 0.7401, 'FK_ECE': 0.0835, 'logprob_rho': 0.3242, 'logprob_AUROC': 0.8067, 'logprob_ECE': 0.0921, 'EM_rho': 0.451, 'EM_AUROC': 0.745, 'EM_ECE': 0.0756, 'voting_conf_rho': 0.3962, 'voting_conf_AUROC': 0.7202, 'voting_conf_ECE': 0.0746}
865	  best_of_n: {'greedy': 0.9243, 'random_avg': 0.9215, 'sj_best': 0.9243, 'logprob_best': 0.9243, 'voting_conf_best': 0.9243, 'oracle': 0.9488}
866	  n8_vs_n16_delta: {'full_SJ_rho_delta': 0.0238, 'full_FK_rho_delta': 0.0201, 'full_logprob_rho_delta': 0.0006, 'full_EM_rho_delta': 0.0214, 'full_voting_conf_rho_delta': 0.0315, 'cond_SJ_rho_delta': 0.0149, 'cond_FK_rho_delta': 0.0112, 'cond_logprob_rho_delta': -0.004, 'cond_EM_rho_delta': 0.0107, 'cond_voting_conf_rho_delta': 0.0219}
867	
868	────────────────────────────────────────────────────────────────────────────────────────────────────
869	EXP_ID: exp_017_llama_conll_n16_s456_r1024
870	STATUS: DONE
871	CONCLUSION: success
872	HYPOTHESIS: LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.
873	METRICS:
874	  degen_rate: 0.8672
875	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
876	  instance_count: 3453
877	  n_valid: 2756
878	  n_gold_empty: 697
879	  parse_rate: 1
880	  ner_greedy_f1: 0.9265
881	  ner_oracle_f1: 0.9499
882	  rho_fk_ner: 0.469
883	  rho_sj_ner: 0.4734
884	  rho_vc_ner: 0.4722
885	  rho_em_ner: 0.4752
886	  rho_lp_ner: 0.3099
887	  auroc_fk_ner: 0.7408
888	  auroc_sj_ner: 0.7428
889	  auroc_vc_ner: 0.7495
890	  auroc_em_ner: 0.7444
891	  auroc_lp_ner: 0.7628
892	  auroc_note: median F1=1.0, AUROC uses >=median threshold
893	  rho_note: CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).
894	
895	────────────────────────────────────────────────────────────────────────────────────────────────────
896	EXP_ID: exp_017_llama_conll_n8_t07
897	STATUS: DONE
898	CONCLUSION: success
899	HYPOTHESIS: LLaMA CoNLL N=8 T=0.7 防御性实验：填补"LLaMA 仅在 SciERC 上测过"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。
900	METRICS:
901	  n_valid: 2756
902	  greedy_f1: 0.9242
903	  oracle_f1: 0.9391
904	  lp_range_median: 1.1e-05
905	  lp_tied_fraction_005: 0.9579
906	  signals: {'SJ': {'rho': 0.3934, 'auroc': 0.6506}, 'FK': {'rho': 0.3879, 'auroc': 0.6488}, 'VC': {'rho': 0.375, 'auroc': 0.6551}, 'EM': {'rho': 0.3888, 'auroc': 0.6494}, 'LP': {'rho': 0.2951, 'auroc': 0.7509}}
907	  selection_f1: {'SJ': 0.9247, 'FK': 0.9254, 'VC': 0.9264, 'EM': 0.9255, 'LP': 0.9248}
908	
909	────────────────────────────────────────────────────────────────────────────────────────────────────
910	EXP_ID: exp_018_llama_scierc_seed123
911	STATUS: DONE
912	CONCLUSION: success
913	HYPOTHESIS: LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.
914	METRICS:
915	  degen_rate: 0.2665
916	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
917	
918	────────────────────────────────────────────────────────────────────────────────────────────────────
919	EXP_ID: exp_018_llama_scierc_seed42_r1024
920	STATUS: DONE
921	CONCLUSION: success
922	HYPOTHESIS: LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.
923	METRICS:
924	  degen_rate: 0.2495
925	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
926	  ner: {'full': {'SJ': {'rho': 0.3096, 'tau': 0.2288, 'auroc': 0.6683}, 'FK': {'rho': 0.2352, 'tau': 0.1759, 'auroc': 0.6069}, 'logprob': {'rho': 0.1503, 'tau': 0.1087, 'auroc': 0.5318}, 'EM': {'rho': 0.2587, 'tau': 0.1966, 'auroc': 0.7174}, 'voting_conf': {'rho': 0.4053, 'tau': 0.3042, 'auroc': 0.6967}}, 'conditional': {'SJ': {'rho': 0.2718, 'tau': None, 'auroc': 0.6565}, 'FK': {'rho': 0.1472, 'tau': None, 'auroc': 0.5866}, 'logprob': {'rho': 0.081, 'tau': None, 'auroc': 0.5129}, 'EM': {'rho': 0.3165, 'tau': None, 'auroc': 0.7244}, 'voting_conf': {'rho': 0.3078, 'tau': None, 'auroc': 0.6714}}, 'greedy_f1': 0.6607, 'oracle_f1': 0.7781, 'n_full': 529, 'n_cond': 478}
927	  re: {'full': {'SJ': {'rho': 0.2748, 'tau': 0.2102, 'auroc': 0.7244}, 'FK': {'rho': 0.3027, 'tau': 0.2337, 'auroc': 0.691}, 'logprob': {'rho': 0.3163, 'tau': 0.233, 'auroc': 0.6313}, 'EM': {'rho': 0.1681, 'tau': 0.1275, 'auroc': 0.7697}, 'voting_conf': {'rho': 0.384, 'tau': 0.2965, 'auroc': 0.7337}}, 'conditional': {'SJ': {'rho': 0.3461, 'tau': None, 'auroc': 0.7233}, 'FK': {'rho': 0.1969, 'tau': None, 'auroc': 0.6684}, 'logprob': {'rho': 0.0888, 'tau': None, 'auroc': 0.5556}, 'EM': {'rho': 0.4969, 'tau': None, 'auroc': 0.819}, 'voting_conf': {'rho': 0.3433, 'tau': None, 'auroc': 0.7003}}, 'greedy_f1': 0.4319, 'oracle_f1': 0.5775, 'n_full': 397, 'n_cond': 251}
928	
929	────────────────────────────────────────────────────────────────────────────────────────────────────
930	EXP_ID: exp_018_llama_scierc_seed456_r1024
931	STATUS: DONE
932	CONCLUSION: success
933	HYPOTHESIS: LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.
934	METRICS:
935	  degen_rate: 0.2741
936	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
937	  ner_greedy_f1: 0.6597
938	  ner_oracle_f1: 0.7683
939	  ner_oracle_headroom: 0.1086
940	  ner_cond_rho_fk: 0.1472
941	  ner_cond_rho_sj: 0.2718
942	  ner_cond_rho_logprob: 0.083
943	  ner_logprob_auroc_cond: 0.5485
944	  re_greedy_f1: 0.4338
945	  re_oracle_f1: 0.5834
946	  re_oracle_headroom: 0.1496
947	  re_cond_rho_fk: 0.2107
948	  re_cond_rho_sj: 0.3898
949	  re_cond_rho_logprob: 0.1252
950	  re_logprob_auroc_cond: 0.6119
951	  ner_structural_beats_logprob: True
952	  re_structural_beats_logprob: True
953	
954	────────────────────────────────────────────────────────────────────────────────────────────────────
955	EXP_ID: exp_018_qwen_scierc_seed123
956	STATUS: DONE
957	CONCLUSION: success
958	HYPOTHESIS: Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.
959	METRICS:
960	  degen_rate: 0.172
961	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
962	
963	────────────────────────────────────────────────────────────────────────────────────────────────────
964	EXP_ID: exp_018_qwen_scierc_seed456
965	STATUS: DONE
966	CONCLUSION: success
967	HYPOTHESIS: Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.
968	METRICS:
969	  degen_rate: 0.2042
970	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
971	
972	────────────────────────────────────────────────────────────────────────────────────────────────────
973	EXP_ID: exp_020_fewnerd_smoke
974	STATUS: DONE
975	CONCLUSION: success
976	HYPOTHESIS: 1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.
977	METRICS:
978	  final_loss: 0.031
979	  total_steps: 8236
980	  training_time: 5h54m
981	  pilot_greedy_f1: 0.8037
982	  pilot_instances: 200
983	  merged_model_path: checkpoints/qwen3-8b-fewnerd-merged
984	
985	────────────────────────────────────────────────────────────────────────────────────────────────────
986	EXP_ID: exp_021_fewnerd_full
987	STATUS: DONE
988	CONCLUSION: success
989	HYPOTHESIS: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.
990	METRICS:
991	  total_steps: 6177
992	  train_loss: 0.048
993	  eval_loss: 0.0275
994	  train_runtime: 3h57m
995	  epochs: 3
996	  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177
997	  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors
998	  inference_instances: 37648
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "af793f8e-fadf-4ce6-9ce2-88802e4f8f15"
}
```

</details>

---


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 53657,
    "tool_uses": 12,
    "duration_ms": 113291
  },
  "last_tool_name": "Read",
  "uuid": "58a5f527-dceb-45cf-8c41-8a0f23372654",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01VQ9VCuQHsTRmh5kLiLjjfD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 998,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "b43b070b-4e65-4300-bb36-b1cb8e3bcf6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq9XuWQefqoy8kUh8MJpkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13967,
      "cache_read_input_tokens": 39361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-22T18:19:39.753Z_

<details><summary>↩ Tool result · `toolu_01VQ9VCuQHsTRmh5kLiLjjfD`</summary>

```text
998	  inference_instances: 37648
999	  inference_filtered: 32565
1000	  inference_n_samples: 8
1001	  greedy_macro_f1: 0.7478
1002	  oracle_macro_f1: 0.8719
1003	  headroom: 0.124
1004	  zero_f1_rate: 0.119
1005	  degeneracy_rate: 0.101
1006	  lp_within_range_mean: 0.0879
1007	  lp_within_range_median: 0.0662
1008	  lp_global_rho: 0.4215
1009	  lp_cond_rho: 0.4225
1010	  sj_global_rho: 0.3002
1011	  sj_cond_rho: 0.2937
1012	  fk_global_rho: 0.3132
1013	  fk_cond_rho: 0.3093
1014	  em_global_rho: 0.2871
1015	  em_cond_rho: 0.271
1016	  vc_global_rho: 0.3858
1017	  vc_cond_rho: 0.3234
1018	  lp_selection_delta_pp: 1.36
1019	  vc_selection_delta_pp: -1.79
1020	  sj_selection_delta_pp: -2.14
1021	  fk_selection_delta_pp: -2.26
1022	  em_selection_delta_pp: -3.85
1023	  lp_bootstrap_ci_95_pp: [1.18, 1.53]
1024	  lp_sample_auroc: 0.5782
1025	  vc_sample_auroc: 0.5354
1026	  fk_sample_auroc: 0.521
1027	  sj_sample_auroc: 0.5197
1028	  em_sample_auroc: 0.5137
1029	  scenario: A_partial
1030	  note: Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.
1031	
1032	────────────────────────────────────────────────────────────────────────────────────────────────────
1033	EXP_ID: exp_021_fewnerd_n8_seed123
1034	STATUS: DONE
1035	CONCLUSION: success
1036	HYPOTHESIS: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.
1037	METRICS:
1038	  degen_rate: 0.1312
1039	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1040	  instance_count: 37648
1041	  n_valid: 32565
1042	  n_gold_empty: 5083
1043	  ner_greedy_f1: 0.7885
1044	  ner_oracle_f1: 0.8892
1045	  rho_fk_ner: 0.1602
1046	  rho_sj_ner: 0.3083
1047	  sample_f1_pct_zero: 20.39
1048	
1049	────────────────────────────────────────────────────────────────────────────────────────────────────
1050	EXP_ID: exp_021_fewnerd_n8_seed456
1051	STATUS: DONE
1052	CONCLUSION: success
1053	HYPOTHESIS: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.
1054	METRICS:
1055	  degen_rate: 0.1212
1056	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1057	  instance_count: 37648
1058	  n_valid: 32565
1059	  n_gold_empty: 5083
1060	  ner_greedy_f1: 0.7888
1061	  ner_oracle_f1: 0.881
1062	  rho_fk_ner: 0.1632
1063	  rho_sj_ner: 0.313
1064	  sample_f1_pct_zero: 19.32
1065	
1066	────────────────────────────────────────────────────────────────────────────────────────────────────
1067	EXP_ID: exp_023_lora_rank8
1068	STATUS: DONE
1069	CONCLUSION: success
1070	HYPOTHESIS: LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.
1071	METRICS:
1072	  train_loss: 0.1018
1073	  eval_loss: 0.0776
1074	  train_runtime: 28m45s
1075	  ner_full: {'n': 529, 'greedy_f1': 0.6397, 'oracle_f1': 0.7998, 'oracle_headroom': 0.1601, 'degeneracy_rate': 0.072, 'SJ_rho': 0.3649, 'FK_rho': 0.2838, 'VC_rho': 0.394, 'EM_rho': 0.2562, 'LP_rho': 0.2105, 'SJ_auroc': 0.689, 'FK_auroc': 0.6002, 'VC_auroc': 0.6886, 'EM_auroc': 0.7265, 'LP_auroc': 0.6054, 'sel_SJ': 0.6306, 'sel_FK': 0.6265, 'sel_VC': 0.5919, 'sel_EM': 0.6073, 'sel_LP': 0.635}
1076	  ner_cond: {'n': 477, 'SJ_rho': 0.3056, 'FK_rho': 0.1452, 'VC_rho': 0.3191, 'EM_rho': 0.3558, 'LP_rho': 0.169}
1077	  re_full: {'n': 397, 'greedy_f1': 0.3712, 'oracle_f1': 0.609, 'oracle_headroom': 0.2378, 'degeneracy_rate': 0.217, 'SJ_rho': 0.2244, 'FK_rho': 0.3448, 'VC_rho': 0.3617, 'EM_rho': 0.068, 'LP_rho': 0.2737, 'SJ_auroc': 0.7092, 'FK_auroc': 0.6469, 'VC_auroc': 0.7533, 'EM_auroc': 0.7306, 'LP_auroc': 0.6325, 'sel_SJ': 0.3584, 'sel_FK': 0.3498, 'sel_VC': 0.3715, 'sel_EM': 0.3291, 'sel_LP': 0.3606}
1078	  re_cond: {'n': 242, 'SJ_rho': 0.3601, 'FK_rho': 0.2343, 'VC_rho': 0.3703, 'EM_rho': 0.4613, 'LP_rho': 0.1809}
1079	
1080	────────────────────────────────────────────────────────────────────────────────────────────────────
1081	EXP_ID: exp_024_claim_audit
1082	STATUS: DONE
1083	CONCLUSION: success
1084	HYPOTHESIS: Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.
1085	METRICS:
1086	  consistent: 97
1087	  errors: 1
1088	  warnings: 5
1089	  old_residuals_found: 0
1090	
1091	────────────────────────────────────────────────────────────────────────────────────────────────────
1092	EXP_ID: exp_025_n32
1093	STATUS: DONE
1094	CONCLUSION: success
1095	HYPOTHESIS: N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.
1096	METRICS:
1097	  n_samples: 32
1098	  degeneracy_pct: 4
1099	  lp_range: 0.0781
1100	  oracle_f1: 0.8412
1101	  greedy_f1: 0.6615
1102	  oracle_gap: 0.1797
1103	  selection_f1_lp_delta: 0.54
1104	  selection_f1_sj_delta: 0.16
1105	  selection_f1_fk_delta: 0.6
1106	  selection_f1_em_delta: 0.68
1107	  selection_f1_vc_delta: -5.21
1108	  best_signal: EM
1109	  best_delta: 0.68
1110	  metric_space: micro_f1_filtered_529inst
1111	  note: corrected via n_ablation_fixed.py, greedy from inst['greedy'] field
1112	
1113	────────────────────────────────────────────────────────────────────────────────────────────────────
1114	EXP_ID: exp_026_T05
1115	STATUS: DONE
1116	CONCLUSION: success
1117	HYPOTHESIS: T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.
1118	METRICS:
1119	  degen_rate: 0.414
1120	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1121	  lp_range_mean: 0.022
1122	  lp_range_std: 0.021
1123	  within_instance_rho_mean: 0.1306
1124	  within_instance_rho_median: 0.2182
1125	  within_instance_rho_valid_pct: 0.597
1126	  greedy_f1: 0.617
1127	  oracle_f1: 0.71
1128	  lp_sel_f1: 0.622
1129	  sj_sel_f1: 0.622
1130	  em_sel_f1: 0.619
1131	  vc_sel_f1: 0.61
1132	  sj_rho: 0.333
1133	  fk_rho: 0.341
1134	  lp_rho: 0.208
1135	  vc_rho: 0.353
1136	  sj_auroc: 0.644
1137	  lp_auroc: 0.577
1138	
1139	────────────────────────────────────────────────────────────────────────────────────────────────────
1140	EXP_ID: exp_026_T08
1141	STATUS: DONE
1142	CONCLUSION: success
1143	HYPOTHESIS: T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.
1144	METRICS:
1145	  degen_rate: 0.2382
1146	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1147	  lp_range_mean: 0.043
1148	  lp_range_std: 0.042
1149	  within_instance_rho_mean: 0.1701
1150	  within_instance_rho_median: 0.2635
1151	  within_instance_rho_valid_pct: 0.728
1152	  greedy_f1: 0.616
1153	  oracle_f1: 0.737
1154	  lp_sel_f1: 0.627
1155	  sj_sel_f1: 0.619
1156	  em_sel_f1: 0.611
1157	  vc_sel_f1: 0.603
1158	  sj_rho: 0.378
1159	  fk_rho: 0.34
1160	  lp_rho: 0.212
1161	  vc_rho: 0.352
1162	  sj_auroc: 0.662
1163	  lp_auroc: 0.571
1164	
1165	────────────────────────────────────────────────────────────────────────────────────────────────────
1166	EXP_ID: exp_026_T12
1167	STATUS: DONE
1168	CONCLUSION: success
1169	HYPOTHESIS: T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.
1170	METRICS:
1171	  degen_rate: 0.1493
1172	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1173	  lp_range_mean: 0.075
1174	  lp_range_std: 0.059
1175	  within_instance_rho_mean: 0.2245
1176	  within_instance_rho_median: 0.3152
1177	  within_instance_rho_valid_pct: 0.875
1178	  greedy_f1: 0.62
1179	  oracle_f1: 0.758
1180	  lp_sel_f1: 0.621
1181	  sj_sel_f1: 0.597
1182	  em_sel_f1: 0.596
1183	  vc_sel_f1: 0.582
1184	  sj_rho: 0.384
1185	  fk_rho: 0.386
1186	  lp_rho: 0.182
1187	  vc_rho: 0.342
1188	  sj_auroc: 0.683
1189	  lp_auroc: 0.566
1190	
1191	────────────────────────────────────────────────────────────────────────────────────────────────────
1192	EXP_ID: exp_026_t05
1193	STATUS: DONE
1194	CONCLUSION: success
1195	HYPOTHESIS: Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.
1196	METRICS:
1197	  temperature: 0.5
1198	  task: T-ablation
1199	  degen_rate: 0.414
1200	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1201	
1202	────────────────────────────────────────────────────────────────────────────────────────────────────
1203	EXP_ID: exp_026_t05_seed123
1204	STATUS: DONE
1205	CONCLUSION: success
1206	HYPOTHESIS: Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1207	METRICS:
1208	  ner_greedy_f1: 0.6611
1209	  ner_oracle_f1: 0.7444
1210	  rho_sj_ner: 0.3133
1211	  sample_f1_pct_zero: 10.09
1212	  instance_count: 551
1213	  n_valid: 529
1214	
1215	────────────────────────────────────────────────────────────────────────────────────────────────────
1216	EXP_ID: exp_026_t05_seed456
1217	STATUS: DONE
1218	CONCLUSION: success
1219	HYPOTHESIS: Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1220	METRICS:
1221	  ner_greedy_f1: 0.6639
1222	  ner_oracle_f1: 0.7437
1223	  rho_sj_ner: 0.3279
1224	  sample_f1_pct_zero: 10.28
1225	  instance_count: 551
1226	  n_valid: 529
1227	
1228	────────────────────────────────────────────────────────────────────────────────────────────────────
1229	EXP_ID: exp_026_t08
1230	STATUS: DONE
1231	CONCLUSION: success
1232	HYPOTHESIS: Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.
1233	METRICS:
1234	  temperature: 0.8
1235	  task: T-ablation
1236	  degen_rate: 0.2382
1237	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1238	
1239	────────────────────────────────────────────────────────────────────────────────────────────────────
1240	EXP_ID: exp_026_t08_seed123
1241	STATUS: DONE
1242	CONCLUSION: success
1243	HYPOTHESIS: Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1244	METRICS:
1245	  ner_greedy_f1: 0.6607
1246	  ner_oracle_f1: 0.7714
1247	  rho_sj_ner: 0.3893
1248	  sample_f1_pct_zero: 11.22
1249	  instance_count: 551
1250	  n_valid: 529
1251	
1252	────────────────────────────────────────────────────────────────────────────────────────────────────
1253	EXP_ID: exp_026_t08_seed456
1254	STATUS: DONE
1255	CONCLUSION: success
1256	HYPOTHESIS: Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1257	METRICS:
1258	  ner_greedy_f1: 0.6641
1259	  ner_oracle_f1: 0.7694
1260	  rho_sj_ner: 0.3771
1261	  sample_f1_pct_zero: 11.79
1262	  instance_count: 551
1263	  n_valid: 529
1264	
1265	────────────────────────────────────────────────────────────────────────────────────────────────────
1266	EXP_ID: exp_026_t10_seed123
1267	STATUS: DONE
1268	CONCLUSION: success
1269	HYPOTHESIS: Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1270	METRICS:
1271	  ner_greedy_f1: 0.6633
1272	  ner_oracle_f1: 0.7777
1273	  rho_sj_ner: 0.3809
1274	  sample_f1_pct_zero: 12.59
1275	  instance_count: 551
1276	  n_valid: 529
1277	
1278	────────────────────────────────────────────────────────────────────────────────────────────────────
1279	EXP_ID: exp_026_t10_seed42
1280	STATUS: DONE
1281	CONCLUSION: success
1282	HYPOTHESIS: Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1283	METRICS:
1284	  ner_greedy_f1: 0.6617
1285	  ner_oracle_f1: 0.7798
1286	  rho_sj_ner: 0.3598
1287	  sample_f1_pct_zero: 12.9
1288	  instance_count: 551
1289	  n_valid: 529
1290	
1291	────────────────────────────────────────────────────────────────────────────────────────────────────
1292	EXP_ID: exp_026_t10_seed456
1293	STATUS: DONE
1294	CONCLUSION: success
1295	HYPOTHESIS: Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1296	METRICS:
1297	  ner_greedy_f1: 0.6621
1298	  ner_oracle_f1: 0.7754
1299	  rho_sj_ner: 0.3921
1300	  sample_f1_pct_zero: 12.97
1301	  instance_count: 551
1302	  n_valid: 529
1303	
1304	────────────────────────────────────────────────────────────────────────────────────────────────────
1305	EXP_ID: exp_026_t12
1306	STATUS: DONE
1307	CONCLUSION: success
1308	HYPOTHESIS: Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.
1309	METRICS:
1310	  temperature: 1.2
1311	  task: T-ablation
1312	  degen_rate: 0.1493
1313	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1314	
1315	────────────────────────────────────────────────────────────────────────────────────────────────────
1316	EXP_ID: exp_026_t12_seed123
1317	STATUS: DONE
1318	CONCLUSION: success
1319	HYPOTHESIS: Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1320	METRICS:
1321	  ner_greedy_f1: 0.6595
1322	  ner_oracle_f1: 0.7895
1323	  rho_sj_ner: 0.359
1324	  sample_f1_pct_zero: 13.99
1325	  instance_count: 551
1326	  n_valid: 529
1327	
1328	────────────────────────────────────────────────────────────────────────────────────────────────────
1329	EXP_ID: exp_026_t12_seed456
1330	STATUS: DONE
1331	CONCLUSION: success
1332	HYPOTHESIS: Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.
1333	METRICS:
1334	  ner_greedy_f1: 0.6637
1335	  ner_oracle_f1: 0.7821
1336	  rho_sj_ner: 0.3995
1337	  sample_f1_pct_zero: 14.08
1338	  instance_count: 551
1339	  n_valid: 529
1340	
1341	────────────────────────────────────────────────────────────────────────────────────────────────────
1342	EXP_ID: exp_027_fewnerd_n16
1343	STATUS: DONE
1344	CONCLUSION: success
1345	HYPOTHESIS: LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.
1346	METRICS:
1347	  LP_delta_pp: 1.88
1348	  LP_delta_95CI: [1.41, 2.37]
1349	  degen_rate: 0.0706
1350	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1351	  greedy_f1: 0.7478
1352	  lp_sel_f1: 0.7666
1353	  oracle_f1: 0.902
1354	  headroom_pp: 15.42
1355	  all_8_types_positive: True
1356	  n_instances: 5000
1357	  N_samples: 16
1358	  bootstrap_p: <0.001
1359	
1360	────────────────────────────────────────────────────────────────────────────────────────────────────
1361	EXP_ID: exp_027_mlp_verifier
1362	STATUS: DONE
1363	CONCLUSION: negative
1364	HYPOTHESIS: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap
1365	METRICS:
1366	  lr_auroc: 0.6522
1367	  mlp_auroc: 0.6381
1368	  rf_auroc: 0.5868
1369	  mlp_15feat_auroc: 0.6341
1370	  lr_sel_f1: 0.6406
1371	  mlp_sel_f1: 0.6278
1372	  greedy_f1: 0.6441
1373	  oracle_f1: 0.8231
1374	  best_single_signal_auroc: 0.6476
1375	  feature_bottleneck_confirmed: True
1376	
1377	────────────────────────────────────────────────────────────────────────────────────────────────────
1378	EXP_ID: exp_028
1379	STATUS: DONE
1380	CONCLUSION: negative
1381	HYPOTHESIS: Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.
1382	METRICS:
1383	  degeneracy_cf1_gold: 0.313
1384	  greedy_f1: 0.7773
1385	  lp_sel_f1: 0.7835
1386	  lp_sel_delta_pp: 0.62
1387	  oracle_f1: 0.8723
1388	  within_instance_rho: 0.4066
1389	  train_loss: 0.0189
1390	  eval_loss: 0.0311
1391	
1392	────────────────────────────────────────────────────────────────────────────────────────────────────
1393	EXP_ID: exp_028_entity_token_lp
1394	STATUS: DONE
1395	CONCLUSION: negative
1396	HYPOTHESIS: Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.
1397	METRICS:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "ef8261a0-92f2-4f4f-bd63-81a2ca6b9aa7"
}
```

</details>

---


### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 61410,
    "tool_uses": 13,
    "duration_ms": 119295
  },
  "last_tool_name": "Read",
  "uuid": "6885e46f-fc9b-44ac-87d9-3580d1f2a07d",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01GJvFJMWG6zQTb6vERQdBSs`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 1397,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "7aae0fb7-2369-4318-8355-6381a0402889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dxvnv7zBkoYygLLvehuGDp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7715,
      "cache_read_input_tokens": 53328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7715,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-22T18:19:45.764Z_

<details><summary>↩ Tool result · `toolu_01GJvFJMWG6zQTb6vERQdBSs`</summary>

```text
1397	METRICS:
1398	  greedy_f1: 0.643
1399	  oracle_f1: 0.7845
1400	  full_lp_global_rho: 0.2971
1401	  entity_text_type_lp_global_rho: 0.4401
1402	  full_lp_selection_f1: 0.6465
1403	  entity_text_type_lp_selection_f1: 0.6357
1404	  dilution_ratio: 0.32
1405	  full_lp_within_range_median: 0.0402
1406	  entity_text_type_within_range_median: 0.1346
1407	  schema_only_within_range_median: 0.0089
1408	
1409	────────────────────────────────────────────────────────────────────────────────────────────────────
1410	EXP_ID: exp_028_fewnerd_5epoch
1411	STATUS: DONE
1412	CONCLUSION: negative
1413	HYPOTHESIS: Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.
1414	METRICS:
1415	  degeneracy_cf1_gold: 0.3133
1416	  greedy_f1: 0.7773
1417	  lp_sel_delta_pp: 0.624
1418	  lp_sel_f1: 0.7835
1419	  oracle_f1: 0.8723
1420	  within_instance_rho_mean: 0.4066
1421	  within_instance_rho_median: 0.6151
1422	
1423	────────────────────────────────────────────────────────────────────────────────────────────────────
1424	EXP_ID: exp_029a
1425	STATUS: DONE
1426	CONCLUSION: success
1427	HYPOTHESIS: Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.
1428	METRICS:
1429	  degen_rate: 0.064
1430	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1431	
1432	────────────────────────────────────────────────────────────────────────────────────────────────────
1433	EXP_ID: exp_029b
1434	STATUS: DONE
1435	CONCLUSION: success
1436	HYPOTHESIS: Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.
1437	METRICS:
1438	  degen_rate: 0.478
1439	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
1440	
1441	────────────────────────────────────────────────────────────────────────────────────────────────────
1442	EXP_ID: exp_14b_inference_conll_v2
1443	STATUS: DONE
1444	CONCLUSION: failed
1445	HYPOTHESIS: 14B CoNLL rerun: Qwen2.5-14B fine-tuned model (qwen25-14b-fewnerd-merged-final) on CoNLL NER inference N=8 T=1.0. Previous run (exp_14b_inference_conll) crashed at 55% with EngineDeadError on 5090-b. Tests whether 14B scale preserves correlation-selection gap pattern on CoNLL.
1446	METRICS:
1447	  greedy_f1: 0.0462
1448	  oracle_f1: 0.1549
1449	  sample_f1_zero_pct: 95.2
1450	  fleiss_kappa: 0.3712
1451	  soft_jaccard: 0.658
1452	  rho_sj_full: -0.27
1453	  structural_beats_surface: False
1454	  verdict: FAIL — 14B model fine-tuned on FewNERD cannot do CoNLL NER (cross-domain mismatch)
1455	
1456	────────────────────────────────────────────────────────────────────────────────────────────────────
1457	EXP_ID: exp_14b_inference_fewnerd
1458	STATUS: DONE
1459	CONCLUSION: success
1460	HYPOTHESIS: 14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. N=16 cut per Director decision.
1461	NOTES: 2026-05-21T00:50 RESTORED to RUNNING per Director. PID 252310 confirmed alive by Reviewer (cuda:0 98% util, elapsed 16min). 5th false-negative misdiagnosis. N=1 greedy_f1=0.7985, N=2 greedy_f1=0.7985/oracle=0.8086, N=4 greedy_f1=0.7984/oracle=0.8544. kill_after_n8.sh active (PID 224789).
1462	METRICS:
1463	  fewnerd_n1: {'greedy_f1': 0.7985, 'oracle_f1': 0.7541, 'oracle_headroom': -0.044, 'verdict': 'FAIL'}
1464	  fewnerd_n2: {'greedy_f1': 0.7985, 'oracle_f1': 0.8086, 'oracle_headroom': 0.01, 'soft_jaccard_rho_full': 0.205, 'rho_advantage': -0.006, 'structural_beats_surface': False, 'verdict': 'FAIL'}
1465	  fewnerd_n4: {'greedy_f1': 0.7984, 'oracle_f1': 0.8544, 'oracle_headroom': 0.056, 'soft_jaccard_rho_full': 0.314, 'rho_advantage': 0.042, 'structural_beats_surface': True, 'verdict': 'MARGINAL'}
1466	  fewnerd_n8: {'greedy_f1': 0.7984, 'oracle_f1': 0.8791, 'oracle_headroom': 0.081, 'soft_jaccard_rho_full': 0.324, 'rho_advantage': 0.083, 'structural_beats_surface': True, 'verdict': 'MARGINAL'}
1467	  cross_domain_scierc_conll: completed but expected poor (cross-domain)
1468	  n16_status: cut per Director decision, kill_after_n8.sh executed
1469	
1470	────────────────────────────────────────────────────────────────────────────────────────────────────
1471	EXP_ID: exp_32b_inference_fewnerd
1472	STATUS: DONE
1473	CONCLUSION: success
1474	HYPOTHESIS: 32B fine-tuned model (Qwen2.5-32B-Instruct QLoRA, best checkpoint-32000) FewNERD inference with N=8 SC sampling. Scaling from 8B→32B should improve per-sample quality and strengthen SC diagnostic correlation (Fleiss kappa / Soft-Jaccard vs F1). Comparison baseline: Qwen3-8B-FT FewNERD results.
1475	METRICS:
1476	  greedy_f1: 0.8
1477	  oracle_f1: 0.879
1478	  rho_SJ_full: 0.32
1479	  rho_FK_full: 0.242
1480	  rho_advantage: 0.078
1481	  fleiss_kappa_mean: 0.533
1482	  soft_jaccard_mean: 0.802
1483	  oracle_headroom: 0.079
1484	  verdict: MARGINAL
1485	
1486	────────────────────────────────────────────────────────────────────────────────────────────────────
1487	EXP_ID: exp_a2_degen_regression
1488	STATUS: PREPARING
1489	CONCLUSION: killed
1490	HYPOTHESIS: Degeneracy rate is primarily driven by task difficulty (dataset entropy ceiling) rather than model capability, with a positive correlation between base F1 and degeneracy — easy tasks with high F1 produce degenerate outputs because the model has already converged.
1491	METRICS:
1492	  n_points: 30
1493	  linear_r2: 0.414
1494	  quadratic_r2: 0.592
1495	  spearman_rho: 0.519
1496	  spearman_p: 0.0033
1497	  linear_coeff: degen = 129.5 × F1 - 56.9
1498	  key_finding: degeneracy driven by dataset difficulty (entropy ceiling), not model capability
1499	
1500	────────────────────────────────────────────────────────────────────────────────────────────────────
1501	EXP_ID: exp_a3_ace05_re
1502	STATUS: DONE
1503	CONCLUSION: success
1504	HYPOTHESIS: Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.
1505	METRICS:
1506	  greedy_f1_mean: 0.0777
1507	  construction_f1_mean: 0.0599
1508	  majority_vote_f1_mean: 0.0491
1509	  oracle_f1_mean: 0.1567
1510	  greedy_micro_f1: 0.0688
1511	  construction_micro_f1: 0.0602
1512	  fleiss_kappa: -0.0021
1513	  soft_jaccard: 0.2425
1514	  degeneracy_rate: 0.0076
1515	  n_instances: 397
1516	  failure_modes: {'F1_degeneracy': '0.8%', 'F2_low_agreement': '93.5%', 'F3_high_agreement_low_quality': '4.5%', 'none': '1.3%'}
1517	  bootstrap_diff: -0.0178
1518	  bootstrap_ci_95: [-0.0334, -0.0024]
1519	  bootstrap_p_value: 0.989
1520	
1521	────────────────────────────────────────────────────────────────────────────────────────────────────
1522	EXP_ID: exp_adaptive_sampling_budget
1523	STATUS: PREPARING
1524	CONCLUSION: killed
1525	HYPOTHESIS: Confidence-aware adaptive sampling budget allocation (fewer samples for high-confidence instances, full N=8 for low-confidence) can recover nearly all SC F1 gains while saving 40-50% of inference cost, because high-confidence instances already have low diversity and gain nothing from additional samples.
1526	NOTES: B7 adaptive sampling budget analysis on Qwen3-8B FT. Key findings: (1) FewNERD: greedy already beats uniform N=8 SC (+0.65pp), adaptive h1/l8 is optimal (+0.30pp vs U8, saves 43.8% samples); (2) SciERC: U8 beats greedy (+1.20pp), top67% h2/l8 saves 50% with only -0.05pp loss. Practical implication: confidence-gated sampling can halve inference cost. Artifacts: vc_8b_qwen3_ft_results, sj_8b_qwen3_f
1527	METRICS:
1528	  model: Qwen3-8B FT
1529	  fewnerd: {'n_instances': 37648, 'greedy_f1': 0.7884, 'uniform_n8_f1': 0.7819, 'best_adaptive': 'h1_l8', 'best_adaptive_f1': 0.7849, 'best_delta_vs_u8': '+0.30pp', 'sample_savings': '43.8%', 'note': 'Greedy > U8; adaptive h1/l8 best: greedy for high-conf, N=8 SC for low-conf'}
1530	  scierc: {'n_instances': 551, 'greedy_f1': 0.6592, 'uniform_n8_f1': 0.6712, 'best_adaptive': 'top67%_h2_l8', 'best_adaptive_f1': 0.6707, 'best_delta_vs_u8': '-0.05pp', 'sample_savings': '50.2%', 'note': 'U8 > Greedy; top67% h2/l8 saves 50% with negligible loss'}
1531	
1532	────────────────────────────────────────────────────────────────────────────────────────────────────
1533	EXP_ID: exp_asb_adaptive_budget
1534	STATUS: DONE
1535	CONCLUSION: negative
1536	HYPOTHESIS: Instance-level features from cheap N=2 subsamples (degeneracy, agreement, entity count, logprob variance, text length) can predict optimal per-instance sample count, enabling adaptive budget allocation that outperforms uniform allocation under a fixed total budget.
1537	METRICS:
1538	  v2_fixed: True
1539	  fixes: ['removed greedy_f1 feature (data leak via gold labels)', 'max_n-aware adaptive_allocation', 'K-fold downstream eval (no train=test leak)', 'micro-F1 (global TP/FP/FN)']
1540	  fewnerd: {'uniform_n8_micro_f1': 0.7842, 'adaptive_micro_f1': 0.7842, 'delta_adaptive_uniform': 0, 'oracle_micro_f1': 0.7842, 'greedy_micro_f1': 0.7911, 'best_predictor': 'MLP', 'n_instances': 32565, 'max_n': 8, 'note': 'max_n=budget=8, no room for reallocation'}
1541	  scierc: {'uniform_n8_micro_f1': 0.6657, 'adaptive_micro_f1': 0.6657, 'delta_adaptive_uniform': 0, 'oracle_micro_f1': 0.6657, 'greedy_micro_f1': 0.6649, 'best_predictor': 'MLP', 'n_instances': 529, 'max_n': 8, 'note': 'max_n=budget=8, no room for reallocation'}
1542	  conll: {'uniform_n8_micro_f1': 0.9128, 'adaptive_micro_f1': 0.9095, 'delta_adaptive_uniform': -0.0033, 'oracle_micro_f1': 0.9139, 'delta_oracle_uniform': 0.0012, 'greedy_micro_f1': 0.9124, 'adaptive_fold_mean': 0.91, 'adaptive_fold_std': 0.0044, 'best_predictor': 'RandomForest', 'n_instances': 2756, 'max_n': 16}
1543	  top_features: ['degen_rate_n2', 'agreement_n2', 'entity_count_n2']
1544	  key_finding: After fixing data leak + train=test leak + max_n bug, adaptive allocation shows no improvement over uniform. FewNERD/SciERC have max_n=budget=8 (no reallocation possible). CoNLL (max_n=16) shows slight negative delta (-0.0033). Previous positive results were artifacts of methodological bugs.
1545	
1546	────────────────────────────────────────────────────────────────────────────────────────────────────
1547	EXP_ID: exp_b1_scd_conll_control
1548	STATUS: DONE
1549	CONCLUSION: negative
1550	HYPOTHESIS: Negative control: SCD on CoNLL where construction gain is negative (-0.4pp, high degeneracy 70%). If SCD learns from construction pseudo-labels, it should NOT improve greedy F1 on a dataset where construction itself hurts. Expected: no improvement or slight degradation. Validates SCD mechanism.
1551	METRICS:
1552	  pre_scd_greedy_f1: 0.9078
1553	  post_scd_greedy_f1: 0.9184
1554	  delta_pp: 1.06
1555	  training_steps: 690
1556	  final_loss: 0.0359
1557	  negative_control_confirmed: False
1558	  note: SURPRISE: SCD improved CoNLL F1 by +1.06pp despite negative construction gain. Possible explanations: (1) SCD provides general training benefit (more data), (2) additional training steps alone improve, (3) SCD mechanism doesn't require positive construction gain.
1559	
1560	────────────────────────────────────────────────────────────────────────────────────────────────────
1561	EXP_ID: exp_b1_scd_fewnerd_curriculum_q
1562	STATUS: DONE
1563	CONCLUSION: negative
1564	HYPOTHESIS: Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.
1565	NOTES: M046: SCD metric artifact confirmed. Original +3.84pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7866, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7866, Δ=-0.20pp. Instance-avg: pre=0.7719 → post=0.7809, Δ=+0.90pp (much smaller than claimed). SCD does not constitute paper contribution.
1566	METRICS:
1567	  eval_greedy_f1: 0.7866
1568	  eval_greedy_precision: 0.7663
1569	  eval_greedy_recall: 0.808
1570	  eval_instance_avg_f1: 0.7809
1571	  delta_vs_baseline: 0.0386
1572	  baseline_greedy_f1: 0.748
1573	  total_tp: 78252
1574	  total_fp: 23869
1575	  total_fn: 18590
1576	  n_instances: 37648
1577	
1578	────────────────────────────────────────────────────────────────────────────────────────────────────
1579	EXP_ID: exp_b1_scd_fewnerd_standard
1580	STATUS: DONE
1581	CONCLUSION: negative
1582	HYPOTHESIS: Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.
1583	NOTES: M046: SCD metric artifact confirmed. Original +3.3pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7813, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7813, Δ=-0.73pp. SCD does not improve NER performance.
1584	METRICS:
1585	  train_loss: 0.023
1586	  eval_loss: 0.0329
1587	  steps: 4706
1588	  epochs: 2
1589	  train_runtime_hours: 7.14
1590	
1591	────────────────────────────────────────────────────────────────────────────────────────────────────
1592	EXP_ID: exp_b2_entity_verifier
1593	STATUS: PREPARING
1594	CONCLUSION: killed
1595	HYPOTHESIS: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+WNUT.
1596	METRICS:
1597	  oof_auc: 0.9233
1598	  oof_path_a_f1_delta: 0.003
1599	  oof_path_b_f1_delta: -0.0157
1600	  oof_greedy_f1: 0.8216
1601	  oof_path_a_f1: 0.8246
1602	  oof_majority_vote_f1: 0.8048
1603	  leakage_pct: 91
1604	  original_delta_pp: 3.62
1605	  oof_delta_pp: 0.3
1606	  per_dataset: {'scierc': '+1.28pp', 'conll': '+0.55pp', 'fewnerd': '+0.02pp'}
1607	  verdict: B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.
1608	  n_inverse_scaling_validation: {'subset_n': 4351, 'full_n': 32565, 'subset_greedy_f1': 0.7926, 'full_greedy_f1': 0.7913, 'verdict': 'Not a bug. Representative subset. Paper should note subset size.'}
1609	
1610	────────────────────────────────────────────────────────────────────────────────────────────────────
1611	EXP_ID: exp_b2_v2_multi_domain_joint
1612	STATUS: PREPARING
1613	CONCLUSION: killed
1614	HYPOTHESIS: Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model to diverse entity patterns. Tests whether training data diversity overcomes the calibration gap that caused B2 original to fail on FewNERD.
1615	METRICS:
1616	  fold3_fewnerd_lgb_auc: 0.8477
1617	  fold3_fewnerd_xgb_auc: 0.8603
1618	  fold3_fewnerd_f1_delta: -0.008
1619	  fold3_ece: 0.136
1620	  fold4_iid_ece: 0.007
1621	  vs_b2_original_lgb_auc_delta: 0.014
1622	  vs_b2_original_xgb_auc_delta: 0.032
1623	  verdict: AUC improved but F1 still negative. Cross-domain calibration gap unsolved.
1624	
1625	────────────────────────────────────────────────────────────────────────────────────────────────────
1626	EXP_ID: exp_b2_v3_domain_invariant
1627	STATUS: PREPARING
1628	CONCLUSION: killed
1629	HYPOTHESIS: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.
1630	METRICS:
1631	  fold3_fewnerd_lgb_auc: 0.8562
1632	  fold3_fewnerd_xgb_auc: 0.8518
1633	  fold3_ece: 0.1373
1634	  fold2_scierc_lgb_auc: 0.8152
1635	  fold2_scierc_xgb_auc: 0.8163
1636	  vs_v2_fold3_lgb_delta: 0.0085
1637	  vs_v2_fold2_lgb_delta: 0.0146
1638	  top_features: agreement_count (58.4%) + vc (30.3%) = 88%
1639	  verdict: LGB AUC improved by removing domain features, confirming negative transfer. But ECE still high, F1 delta still negative.
1640	
1641	────────────────────────────────────────────────────────────────────────────────────────────────────
1642	EXP_ID: exp_b2_v4_inverse_frequency
1643	STATUS: PREPARING
1644	CONCLUSION: killed
1645	HYPOTHESIS: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.
1646	METRICS:
1647	  variant_a_replace_fold3_lgb_auc: 0.834
1648	  variant_a_replace_fold3_ece: 0.2188
1649	  variant_a_f1_delta: -0.013
1650	  variant_b_augment_fold3_lgb_auc: 0.8541
1651	  variant_b_augment_fold3_ece: 0.1934
1652	  variant_b_f1_delta: -0.009
1653	  sj_ifw_std_reduction: 54% (0.138→0.063)
1654	  ac_ifw_std_reduction: 10% (0.122→0.110)
1655	  verdict: IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.
1656	
1657	────────────────────────────────────────────────────────────────────────────────────────────────────
1658	EXP_ID: exp_b3_prompted_diversity
1659	STATUS: DONE
1660	CONCLUSION: killed
1661	HYPOTHESIS: Structurally different prompt templates (expert persona, descriptive types, recall-focused) generate more diverse N=8 samples than repeating a single template, improving entity construction F1 via broader coverage of the entity space.
1662	METRICS:
1663	  single_vc_weighted_f1: 0.7723
1664	  multi_vc_weighted_f1: 0.7311
1665	  delta_vc: -0.0412
1666	  single_lp_weighted_f1: 0.7665
1667	  multi_lp_weighted_f1: 0.7308
1668	  delta_lp: -0.0356
1669	  single_theta2n_f1: 0.7618
1670	  multi_theta2n_f1: 0.7269
1671	  delta_theta2n: -0.0349
1672	  single_unique_entities: 5.29
1673	  multi_unique_entities: 4.06
1674	  within_template_jaccard: 0.474
1675	  cross_template_jaccard: 0.67
1676	  verdict: Multi-template strictly worse. Templates converge to similar outputs; non-standard templates add noise, diluting construction signals.
1677	
1678	────────────────────────────────────────────────────────────────────────────────────────────────────
1679	EXP_ID: exp_backup1_het_temp
1680	STATUS: DONE
1681	CONCLUSION: negative
1682	HYPOTHESIS: Heterogeneous-Temperature Sampling: MRSC/LSC negative results prove entity-level correction cannot close the selection gap. F4 degeneracy analysis shows T=0.7 has ~62% degeneracy (too homogeneous) while T=1.0 has more diversity but noisier entities. Mixing samples from different temperatures (k from T_low + (8-k) from T_high) breaks temperature-specific degeneracy patterns: low-T samples provide p
1683	NOTES: Heterogeneous temperature mixing provides no consistent F1 improvement over pure single-temperature sampling on SciERC (551 instances, 3 seeds, 2 temp pairs). All F1 deltas within ±0.005, inconsistent direction across seeds. Mixing does reduce degeneracy (T=0.5: 35%→17%) but this doesn't translate to F1 gain. The pure T_low vs T_high F1 gap is already tiny (~0.001-0.01), leaving no room for mixing
1684	METRICS:
1685	  t08_vs_t10: {'seed42': {'pure_t_low_f1': 0.6755, 'pure_t_high_f1': 0.6643, 'best_mix': '5:3', 'best_mix_f1': 0.6708, 'delta_vs_low': -0.0046, 'delta_vs_high': 0.0066}, 'seed123': {'pure_t_low_f1': 0.6659, 'pure_t_high_f1': 0.6681, 'best_mix': '6:2', 'best_mix_f1': 0.6655, 'delta_vs_low': -0.0004, 'delta_vs_high': -0.0026}, 'seed456': {'pure_t_low_f1': 0.6675, 'pure_t_high_f1': 0.6663, 'best_mix': '4:4', 'best_mix_f1': 0.6654, 'delta_vs_low': -0.002, 'delta_vs_high': -0.0008}}
1686	  t05_vs_t10: {'seed42': {'pure_t_low_f1': 0.663, 'pure_t_high_f1': 0.6643, 'best_mix': '5:3', 'best_mix_f1': 0.6654, 'delta_vs_low': 0.0024, 'delta_vs_high': 0.0011}, 'seed123': {'pure_t_low_f1': 0.6665, 'pure_t_high_f1': 0.6681, 'best_mix': '2:6', 'best_mix_f1': 0.6671, 'delta_vs_low': 0.0006, 'delta_vs_high': -0.001}, 'seed456': {'pure_t_low_f1': 0.6686, 'pure_t_high_f1': 0.6663, 'best_mix': '4:4', 'best_mix_f1': 0.6682, 'delta_vs_low': -0.0004, 'delta_vs_high': 0.002}}
1687	  degeneracy: {'t05_mean': 0.356, 't08_mean': 0.178, 't10_mean': 0.126}
1688	  max_delta_any_combo: 0.0066
1689	
1690	────────────────────────────────────────────────────────────────────────────────────────────────────
1691	EXP_ID: exp_backup3_distill_verifier
1692	STATUS: DONE
1693	CONCLUSION: negative
1694	HYPOTHESIS: A supervised entity-level binary classifier (trained on 6 lightweight features: LP score, agreement ratio, degeneracy flag, span length, type consistency, N) can learn cross-dataset entity correctness signals that outperform unsupervised majority voting for entity construction, because the classifier can jointly weight multiple complementary signals that MV ignores.
1695	METRICS:
1696	  aggregate: {'LR': {'mean_auroc': 0.8747, 'std_auroc': 0.0563, 'mean_delta_f1': -0.0014}, 'RF': {'mean_auroc': 0.8752, 'std_auroc': 0.0588, 'mean_delta_f1': -0.0006}, 'MLP': {'mean_auroc': 0.8744, 'std_auroc': 0.0578, 'mean_delta_f1': 0.0011}}
1697	  per_fold: {'scierc': {'LR': {'auroc': 0.8009, 'std_mv_f1': 0.6643, 'best_weighted_f1': 0.6659, 'delta_f1': 0.0016}, 'RF': {'auroc': 0.7988, 'best_weighted_f1': 0.6647, 'delta_f1': 0.0004}, 'MLP': {'auroc': 0.798, 'best_weighted_f1': 0.6655, 'delta_f1': 0.0012}}, 'conll': {'LR': {'auroc': 0.9376, 'std_mv_f1': 0.9074, 'best_weighted_f1': 0.9049, 'delta_f1': -0.0025}, 'RF': {'auroc': 0.9419, 'best_weighted_f1': 0.908, 'delta_f1': 0.0006}, 'MLP': {'auroc': 0.9379, 'best_weighted_f1': 0.9075, 'delta_f1': 0.0001}}, 'fewnerd': {'LR': {'auroc': 0.8855, 'std_mv_f1': 0.7819, 'best_weighted_f1': 0.7786, 'delta_f1': -0.0034}, 'RF': {'auroc': 0.885, 'best_weighted_f1': 0.7791, 'delta_f1': -0.0029}, 'MLP': {'auroc': 0.8872, 'best_weighted_f1': 0.7839, 'delta_f1': 0.002}}}
1698	  feature_importance_LR_scierc: {'agreement_ratio': 1.651, 'lp_score': 0.424, 'span_length': -0.15, 'type_consistency': 0.128, 'degeneracy_flag': 0.043, 'n_samples': 0}
1699	
1700	────────────────────────────────────────────────────────────────────────────────────────────────────
1701	EXP_ID: exp_conll_freeform_n8_s42
1702	STATUS: DONE
1703	CONCLUSION: success
1704	HYPOTHESIS: Free-form decoding ablation: CoNLL N=8 T=1.0 seed=42 with use_grammar=False. Tests whether removing XGrammar constrained decoding degrades extraction quality and consistency scores, quantifying the contribution of grammar constraints to the structured self-consistency pipeline.
1705	METRICS:
1706	  greedy_f1: 0.9046
1707	  mv_strict_f1: 0.8994
1708	  mv_delta_pp: -0.52
1709	  lp_f1: 0.8951
1710	  lp_delta_pp: -0.95
1711	  degeneracy_rate: 0.6
1712	  lp_std_ratio: 0.023466
1713	  n_instances: 2756
1714	  vs_constrained: {'greedy_f1_delta': -0.0042, 'mv_delta_change': '+0.43pp (less hurt)', 'degen_delta': '+3.0pp (higher in freeform)', 'lp_std_ratio_delta': -0.0022}
1715	
1716	────────────────────────────────────────────────────────────────────────────────────────────────────
1717	EXP_ID: exp_conll_mf4_v2_s123
1718	STATUS: DONE
1719	CONCLUSION: success
1720	HYPOTHESIS: MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). 3-seed set with exp_conll_t10_s42.
1721	METRICS:
1722	  greedy_f1: 0.9083
1723	  oracle_f1: 0.9527
1724	  oracle_headroom: 0.0444
1725	  fleiss_kappa_mean: 0.762
1726	  soft_jaccard_mean: 0.886
1727	  rho_SJ_full: 0.4628
1728	  rho_kappa_full: 0.4457
1729	  rho_SJ_cond: 0.414
1730	  rho_kappa_cond: 0.3887
1731	  logprob_rho_full: 0.3281
1732	  logprob_rho_cond: 0.367
1733	  logprob_auroc_full: 0.7621
1734	  logprob_auroc_cond: 0.8198
1735	  sample_f1_mean: 0.8744
1736	  sample_f1_pct_zero: 7.05
1737	  structural_beats_surface: True
1738	  rho_advantage: 0.0171
1739	  verdict: PASS
1740	
1741	────────────────────────────────────────────────────────────────────────────────────────────────────
1742	EXP_ID: exp_conll_mf4_v2_s42
1743	STATUS: DONE
1744	CONCLUSION: success
1745	HYPOTHESIS: MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Third seed completing 3-seed set for statistical power. α_crit noted only 2-seed for CoNLL.
1746	METRICS:
1747	  greedy_f1: 0.9123
1748	  mv_strict_f1: 0.9101
1749	  mv_delta_strict_pp: -0.22
1750	  oracle_f1: 0.9538
1751	  degeneracy_rate: 0.601
1752	  alpha_crit_eff_strict: 2.0903
1753	  mv_f1: 0.909
1754	  fleiss_kappa: 0.7729
1755	  soft_jaccard: 0.8949
1756	  note: MV strict metrics from recompute on gold-nonempty subset (autodl-5090-c)
1757	
1758	────────────────────────────────────────────────────────────────────────────────────────────────────
1759	EXP_ID: exp_conll_mf4_v2_s456
1760	STATUS: DONE
1761	CONCLUSION: success
1762	HYPOTHESIS: MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). 3-seed set with exp_conll_t10_s42.
1763	METRICS:
1764	  greedy_f1: 0.907
1765	  oracle_f1: 0.9426
1766	  oracle_headroom: 0.0357
1767	  fleiss_kappa_mean: 0.768
1768	  soft_jaccard_mean: 0.892
1769	  rho_SJ_full: 0.4803
1770	  rho_kappa_full: 0.4638
1771	  rho_SJ_cond: 0.4513
1772	  rho_kappa_cond: 0.425
1773	  logprob_rho_full: 0.3213
1774	  logprob_rho_cond: 0.3723
1775	  logprob_auroc_full: 0.7569
1776	  logprob_auroc_cond: 0.8221
1777	  sample_f1_mean: 0.8737
1778	  sample_f1_pct_zero: 7.08
1779	  structural_beats_surface: True
1780	  rho_advantage: 0.0166
1781	  verdict: PASS
1782	
1783	────────────────────────────────────────────────────────────────────────────────────────────────────
1784	EXP_ID: exp_conll_mf4v2_s123_rerun
1785	STATUS: DONE
1786	CONCLUSION: success
1787	HYPOTHESIS: CoNLL MF4v2 seed=123 rerun: regenerating instance-level samples.jsonl for MV unified recompute (strict > threshold + 4-tuple match). Original data may have been lost with 5090-b.
1788	METRICS:
1789	  greedy_f1: 0.9072
1790	  oracle_f1: 0.9526
1791	  oracle_headroom: 0.0454
1792	  rho_fk_cond: 0.389
1793	  rho_sj_cond: 0.414
1794	  logprob_rho_cond: 0.367
1795	  structural_beats_surface: True
1796	  verdict: PASS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "c5bd5a0b-ccd5-48b4-b76b-4f1701a4861f"
}
```

</details>

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 72576,
    "tool_uses": 14,
    "duration_ms": 125301
  },
  "last_tool_name": "Read",
  "uuid": "c4971115-0d59-4e67-b2fe-48210f30deac",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_0141N8JDpLLWWDs8Car44uaW`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 1796,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "7f0b3dba-69f0-42ce-9715-e710bf3b8b7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrQZa85KVT5QdbYqSTiiDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11132,
      "cache_read_input_tokens": 61043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11132,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T18:19:51.764Z_

<details><summary>↩ Tool result · `toolu_0141N8JDpLLWWDs8Car44uaW`</summary>

```text
1796	  verdict: PASS
1797	  mv_strict_f1: 0.9123
1798	  mv_incl_f1: 0.9151
1799	  degeneracy_rate: 0.603
1800	  alpha_crit_v4: 0.456
1801	
1802	────────────────────────────────────────────────────────────────────────────────────────────────────
1803	EXP_ID: exp_conll_mf4v2_s456_rerun
1804	STATUS: DONE
1805	CONCLUSION: success
1806	HYPOTHESIS: CoNLL MF4v2 seed=456 rerun: regenerating instance-level samples.jsonl for MV unified recompute. Original data may have been lost with 5090-b.
1807	METRICS:
1808	  greedy_f1: 0.9068
1809	  oracle_f1: 0.9429
1810	  oracle_headroom: 0.0361
1811	  rho_fk_cond: 0.426
1812	  rho_sj_cond: 0.454
1813	  logprob_rho_cond: 0.37
1814	  structural_beats_surface: True
1815	  verdict: PASS
1816	  mv_strict_f1: 0.9121
1817	  mv_incl_f1: 0.9133
1818	  degeneracy_rate: 0.604
1819	  alpha_crit_v4: 0.4558
1820	
1821	────────────────────────────────────────────────────────────────────────────────────────────────────
1822	EXP_ID: exp_conll_n16_s123
1823	STATUS: DONE
1824	CONCLUSION: success
1825	HYPOTHESIS: CoNLL N=16 seed=123: second seed for 3-seed N=16 coverage. Tests N-scaling consistency — whether oracle headroom increase from N=8→N=16 is reproducible across seeds.
1826	NOTES: 重跑成功（首次因 tokenizer 缺失失败）。CoNLL N=16 seed=123: greedy=0.9077, oracle=0.9631, headroom=+0.0555。vs s42: greedy 0.908, oracle 0.9592, headroom 0.0512。种子间高度一致（greedy Δ<0.5pp, oracle Δ<0.5pp）。Structural > Surface confirmed (delta=+0.0103)。
1827	METRICS:
1828	  greedy_f1: 0.908
1829	  oracle_f1: 0.963
1830	  oracle_headroom: 0.055
1831	  rho_fk_cond: 0.391
1832	  rho_sj_cond: 0.417
1833	  logprob_rho_cond: 0.373
1834	  structural_beats_surface: True
1835	  verdict: PASS
1836	
1837	────────────────────────────────────────────────────────────────────────────────────────────────────
1838	EXP_ID: exp_conll_n16_s123_v2
1839	STATUS: DONE
1840	CONCLUSION: success
1841	HYPOTHESIS: CoNLL N=16 (seed=123, v2): retry after previous failure on 5090 (damaged checkpoint). Extending N-scaling curve to N=16 for Qwen3-8B-FT on CoNLL-2003.
1842	METRICS:
1843	  greedy_f1: 0.9071
1844	  oracle_f1: 0.9625
1845	  oracle_headroom: 0.0554
1846	  fleiss_kappa_mean: 0.767
1847	  soft_jaccard_mean: 0.877
1848	  rho_SJ_full: 0.4567
1849	  rho_kappa_full: 0.4469
1850	  rho_SJ_cond: 0.4174
1851	  rho_kappa_cond: 0.3936
1852	  logprob_rho_full: 0.3456
1853	  logprob_rho_cond: 0.375
1854	  logprob_auroc_full: 0.7742
1855	  logprob_auroc_cond: 0.8258
1856	  sample_f1_mean: 0.8676
1857	  sample_f1_pct_zero: 7.52
1858	  verdict: PASS
1859	
1860	────────────────────────────────────────────────────────────────────────────────────────────────────
1861	EXP_ID: exp_conll_n16_s42
1862	STATUS: DONE
1863	CONCLUSION: success
1864	HYPOTHESIS: N-scaling test: CoNLL N=16 (2× N=8) finetuned model. CoNLL has highest degeneracy (~62%) at N=8. If degeneracy increases further at N=16, confirms sampling diversity collapse scales with N. Part of N-scaling suite for R34 C1.
1865	METRICS:
1866	  greedy_f1: 0.908
1867	  oracle_f1: 0.959
1868	  mv_strict_f1: 0.9148
1869	  mv_delta_strict_pp: 0.19
1870	  degeneracy_rate: 0.497
1871	  alpha_crit_eff_strict: 1.6749
1872	  capture_rate_pct: 3.8
1873	  rho_SJ_full: 0.446
1874	  rho_FK_full: 0.427
1875	  note: MV metrics from gold-nonempty subset (n=2756/3453); greedy/oracle from full set
1876	
1877	────────────────────────────────────────────────────────────────────────────────────────────────────
1878	EXP_ID: exp_conll_n16_s456
1879	STATUS: DONE
1880	CONCLUSION: success
1881	HYPOTHESIS: CoNLL N=16 seed=456: third seed completing 3-seed N=16 set. Tests N-scaling consistency for CoNLL — whether oracle headroom increase from N=8→N=16 is reproducible and degeneracy pattern changes.
1882	NOTES: 失败原因: tokenizer vocab_file=None — checkpoints/qwen3-8b-conll2003-merged 缺少 vocab.json，vLLM 初始化 tokenizer 时 TypeError。与 exp_conll_n16_s123 同根因。| 已有成果: 无（启动即崩溃）| 建议: 修复 merged checkpoint tokenizer 文件后重跑
1883	METRICS:
1884	  greedy_f1: 0.9072
1885	  oracle_f1: 0.9545
1886	  oracle_headroom: 0.0473
1887	  rho_fk_cond: 0.428
1888	  rho_sj_cond: 0.451
1889	  logprob_rho_cond: 0.374
1890	  structural_beats_surface: True
1891	  verdict: PASS
1892	
1893	────────────────────────────────────────────────────────────────────────────────────────────────────
1894	EXP_ID: exp_conll_n16_s456_v2
1895	STATUS: DONE
1896	CONCLUSION: success
1897	HYPOTHESIS: CoNLL N=16 (seed=456, v2): retry after previous failure on 5090. Third seed for 3-seed statistical power on CoNLL-2003 N=16.
1898	METRICS:
1899	  greedy_f1: 0.9076
1900	  oracle_f1: 0.955
1901	  oracle_headroom: 0.0474
1902	  fleiss_kappa_mean: 0.8
1903	  soft_jaccard_mean: 0.8965
1904	  rho_SJ_full: 0.4791
1905	  rho_kappa_full: 0.4697
1906	  rho_SJ_cond: 0.4481
1907	  rho_kappa_cond: 0.4268
1908	  logprob_rho_full: 0.3137
1909	  logprob_rho_cond: 0.373
1910	  logprob_auroc_full: 0.7524
1911	  logprob_auroc_cond: 0.8236
1912	  sample_f1_mean: 0.8736
1913	  sample_f1_pct_zero: 7.03
1914	  verdict: PASS
1915	
1916	────────────────────────────────────────────────────────────────────────────────────────────────────
1917	EXP_ID: exp_conll_n32_s123
1918	STATUS: DONE
1919	CONCLUSION: success
1920	HYPOTHESIS: N=32 multi-seed robustness: CoNLL N=32 finetuned seed=123. Second seed to verify CoNLL N=32 MV Δ (+0.46pp at seed=42). Tests whether the positive MV gain is reproducible.
1921	METRICS:
1922	  greedy_f1: 0.9123
1923	  mv_strict_f1: 0.9177
1924	  mv_delta_strict_pp: 0.55
1925	  oracle_f1: 0.9717
1926	  degeneracy_rate: 0.379
1927	  alpha_crit_eff_strict: 0.7347
1928	
1929	────────────────────────────────────────────────────────────────────────────────────────────────────
1930	EXP_ID: exp_conll_n32_s42
1931	STATUS: DONE
1932	CONCLUSION: success
1933	HYPOTHESIS: N-scaling test: CoNLL N=32 (4× N=8) finetuned model. High-degeneracy regime (~62% at N=8). Tests whether 4× budget reduces degeneracy enough for MV to become positive. If not, demonstrates structural ceiling independent of sample budget. Part of N-scaling suite for R34 C1.
1934	METRICS:
1935	  greedy_f1: 0.912
1936	  mv_strict_f1: 0.9166
1937	  mv_delta_strict_pp: 0.46
1938	  mv_incl_f1: 0.9169
1939	  oracle_f1: 0.969
1940	  degeneracy_rate: 0.405
1941	  alpha_crit_strict: 0.456
1942	
1943	────────────────────────────────────────────────────────────────────────────────────────────────────
1944	EXP_ID: exp_conll_n32_s456
1945	STATUS: DONE
1946	CONCLUSION: success
1947	HYPOTHESIS: N=32 multi-seed robustness: CoNLL N=32 finetuned seed=456. Third seed to complete 3-seed mean±σ (s42 +0.46pp, s123 +0.55pp). CoNLL shows stable MV gain at N=32; this confirms reproducibility.
1948	METRICS:
1949	  greedy_f1: 0.9117
1950	  mv_strict_f1: 0.9167
1951	  mv_delta_strict_pp: 0.51
1952	  degeneracy_rate: 0.401
1953	  oracle_f1: 0.9686
1954	  alpha_crit_eff_strict: 0.7614
1955	
1956	────────────────────────────────────────────────────────────────────────────────────────────────────
1957	EXP_ID: exp_conll_n64_s42
1958	STATUS: DONE
1959	CONCLUSION: success
1960	HYPOTHESIS: N-scaling convergence test: CoNLL N=64 (8× N=8) finetuned model. CoNLL has highest degeneracy (~60% at N=8). Tests whether degeneracy continues declining and whether the marginal MV Δ improvement from N=16→32→64 is negligible. Fourth data point for N-scaling convergence curve. Part of extended N-scaling suite for R34 C1.
1961	METRICS:
1962	  greedy_f1: 0.912
1963	  mv_strict_f1: 0.9184
1964	  mv_delta_strict_pp: 0.64
1965	  oracle_f1: 0.9751
1966	  degeneracy_rate: 0.306
1967	
1968	────────────────────────────────────────────────────────────────────────────────────────────────────
1969	EXP_ID: exp_conll_pretrained_n16_s42
1970	STATUS: DONE
1971	CONCLUSION: success
1972	HYPOTHESIS: Pretrained N-scaling: CoNLL N=16 with Qwen2.5-7B-Instruct (unfinetuned). Fills the N=16 gap in pretrained CoNLL N-scaling curve (N=8 +3.01pp, N=32 +3.21pp). Tests whether pretrained MV gain scales monotonically with N.
1973	METRICS:
1974	  greedy_f1: 0.5986
1975	  mv_strict_f1: 0.632
1976	  mv_delta_strict_pp: 3.34
1977	  oracle_f1: 0.7282
1978	  degeneracy_rate: 0.255
1979	  alpha_crit_eff_strict: 0.402
1980	
1981	────────────────────────────────────────────────────────────────────────────────────────────────────
1982	EXP_ID: exp_conll_pretrained_n32_s42
1983	STATUS: DONE
1984	CONCLUSION: success
1985	HYPOTHESIS: Pretrained N-scaling: CoNLL N=32 with Qwen2.5-7B-Instruct (unfinetuned). CoNLL pretrained showed strong MV gain (+9.2pp at N=8). Tests whether this advantage scales with N, and whether the pretrained-vs-finetuned contrast (direction flip) persists at higher sample budget. Addresses reviewer concern about generalization.
1986	METRICS:
1987	  greedy_f1: 0.5975
1988	  mv_strict_f1: 0.6296
1989	  mv_delta_strict_pp: 3.21
1990	  oracle_f1: 0.7493
1991	  degeneracy_rate: 0.188
1992	  alpha_crit_eff_strict: 0.5657
1993	
1994	────────────────────────────────────────────────────────────────────────────────────────────────────
1995	EXP_ID: exp_conll_pretrained_n64_s42
1996	STATUS: DONE
1997	CONCLUSION: success
1998	HYPOTHESIS: Pretrained N-scaling: CoNLL N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained CoNLL N-scaling curve (N=8 +3.01, N=32 +3.21). Tests whether pretrained MV gain continues scaling and whether degeneracy continues declining at N=64.
1999	METRICS:
2000	  greedy_f1: 0.6005
2001	  mv_strict_f1: 0.6316
2002	  mv_delta_strict_pp: 3.11
2003	  oracle_f1: 0.7703
2004	  degeneracy_rate: 0.143
2005	
2006	────────────────────────────────────────────────────────────────────────────────────────────────────
2007	EXP_ID: exp_conll_t05_s123
2008	STATUS: DONE
2009	CONCLUSION: success
2010	HYPOTHESIS: CoNLL temperature ablation (T=0.5, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.
2011	METRICS:
2012	  greedy_f1: 0.9073
2013	  oracle_f1: 0.9351
2014	  oracle_headroom: 0.0278
2015	  fleiss_kappa_mean: 0.8941
2016	  soft_jaccard_mean: 0.954
2017	  rho_fleiss_full: 0.4529
2018	  rho_softjaccard_full: 0.4602
2019	  rho_fleiss_cond: 0.4493
2020	  rho_softjaccard_cond: 0.4566
2021	  structural_beats_surface: True
2022	  rho_advantage: 0.0072
2023	  sample_f1_mean: 0.901
2024	  sample_f1_pct_zero: 5.5
2025	  verdict: PASS
2026	
2027	────────────────────────────────────────────────────────────────────────────────────────────────────
2028	EXP_ID: exp_conll_t05_s42
2029	STATUS: DONE
2030	CONCLUSION: success
2031	HYPOTHESIS: CoNLL T=0.5 temperature point: test low temperature on CoNLL2003 to extend cross-dataset T-ablation evidence beyond SciERC and FewNERD. N=8, Qwen3-8B-FT-CoNLL, seed=42. Complements SciERC T-ablation for 3-dataset degeneracy-temperature comparison.
2032	METRICS:
2033	  greedy_f1: 0.9083
2034	  oracle_f1: 0.9376
2035	  oracle_headroom: 0.0294
2036	  fleiss_kappa: 0.8958
2037	  softjaccard_rho_full: 0.4228
2038	  softjaccard_rho_cond: 0.4476
2039	  fleiss_rho_cond: 0.4443
2040	  logprob_rho_cond: 0.3562
2041	  logprob_auroc_cond: 0.8102
2042	  degen_pct: 5.64
2043	  sample_f1_mean: 0.8994
2044	  verdict: PASS
2045	
2046	────────────────────────────────────────────────────────────────────────────────────────────────────
2047	EXP_ID: exp_conll_t05_s456
2048	STATUS: DONE
2049	CONCLUSION: success
2050	HYPOTHESIS: CoNLL temperature ablation (T=0.5, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.
2051	METRICS:
2052	  greedy_f1: 0.9075
2053	  oracle_f1: 0.9338
2054	  oracle_headroom: 0.0263
2055	  fleiss_kappa_mean: 0.8885
2056	  soft_jaccard_mean: 0.9551
2057	  rho_SJ_F1_full: 0.4549
2058	  rho_SJ_F1_conditional: 0.469
2059	  degeneracy_rate_pct: 5.62
2060	  rho_advantage: 0.0044
2061	  verdict: PASS
2062	
2063	────────────────────────────────────────────────────────────────────────────────────────────────────
2064	EXP_ID: exp_conll_t08_s123
2065	STATUS: DONE
2066	CONCLUSION: success
2067	HYPOTHESIS: CoNLL temperature ablation (T=0.8, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.
2068	METRICS:
2069	  greedy_f1: 0.9068
2070	  oracle_f1: 0.9466
2071	  oracle_headroom: 0.0398
2072	  fleiss_kappa_mean: 0.8246
2073	  soft_jaccard_mean: 0.9201
2074	  rho_fleiss_full: 0.4718
2075	  rho_softjaccard_full: 0.4846
2076	  rho_fleiss_cond: 0.4444
2077	  rho_softjaccard_cond: 0.462
2078	  structural_beats_surface: True
2079	  rho_advantage: 0.0128
2080	  sample_f1_mean: 0.8897
2081	  sample_f1_pct_zero: 6.1
2082	  verdict: PASS
2083	
2084	────────────────────────────────────────────────────────────────────────────────────────────────────
2085	EXP_ID: exp_conll_t08_s456
2086	STATUS: DONE
2087	CONCLUSION: success
2088	HYPOTHESIS: CoNLL temperature ablation (T=0.8, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.
2089	METRICS:
2090	  greedy_f1: 0.9064
2091	  oracle_f1: 0.9407
2092	  oracle_headroom: 0.0343
2093	  fleiss_kappa_mean: 0.8229
2094	  soft_jaccard_mean: 0.9233
2095	  rho_SJ_F1_full: 0.4877
2096	  rho_SJ_F1_conditional: 0.4756
2097	  degeneracy_rate_pct: 6.29
2098	  rho_advantage: 0.0058
2099	  verdict: PASS
2100	
2101	────────────────────────────────────────────────────────────────────────────────────────────────────
2102	EXP_ID: exp_conll_t10_s42
2103	STATUS: DONE
2104	CONCLUSION: success
2105	HYPOTHESIS: CoNLL T=1.0 baseline (seed=42): fills the gap in the temperature ablation matrix (T=0.5/0.8/1.2 already complete with 3 seeds). T=1.0 is the default sampling temperature and should show intermediate behavior between T=0.8 (sweet spot) and T=1.2 (over-diversification), completing the temperature sweep for CoNLL.
2106	METRICS:
2107	  greedy_f1: 0.9077
2108	  oracle_f1: 0.9503
2109	  oracle_headroom: 0.0426
2110	  rho_SJ_full: 0.4249
2111	  rho_kappa_full: 0.4037
2112	  rho_SJ_cond: 0.4154
2113	  rho_kappa_cond: 0.3793
2114	  rho_advantage: 0.0212
2115	  fleiss_kappa_mean: 0.772
2116	  soft_jaccard_mean: 0.895
2117	  sample_f1_mean: 0.871
2118	  sample_f1_pct_zero: 7.53
2119	  verdict: PASS
2120	
2121	────────────────────────────────────────────────────────────────────────────────────────────────────
2122	EXP_ID: exp_conll_t12_s123
2123	STATUS: DONE
2124	CONCLUSION: success
2125	HYPOTHESIS: CoNLL temperature ablation (T=1.2, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.
2126	METRICS:
2127	  greedy_f1: 0.9072
2128	  oracle_f1: 0.955
2129	  oracle_headroom: 0.0478
2130	  fleiss_kappa_mean: 0.6675
2131	  soft_jaccard_mean: 0.8295
2132	  rho_fleiss_full: 0.4086
2133	  rho_softjaccard_full: 0.4352
2134	  rho_fleiss_cond: 0.3516
2135	  rho_softjaccard_cond: 0.3915
2136	  structural_beats_surface: True
2137	  rho_advantage: 0.0266
2138	  sample_f1_mean: 0.8438
2139	  sample_f1_pct_zero: 9.1
2140	  verdict: PASS
2141	
2142	────────────────────────────────────────────────────────────────────────────────────────────────────
2143	EXP_ID: exp_conll_t12_s456
2144	STATUS: DONE
2145	CONCLUSION: success
2146	HYPOTHESIS: CoNLL temperature ablation (T=1.2, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.
2147	METRICS:
2148	  greedy_f1: 0.9071
2149	  oracle_f1: 0.9452
2150	  oracle_headroom: 0.0381
2151	  fleiss_kappa_mean: 0.7005
2152	  soft_jaccard_mean: 0.8513
2153	  rho_SJ_F1_full: 0.4553
2154	  rho_SJ_F1_conditional: 0.4259
2155	  degeneracy_rate_pct: 8.34
2156	  rho_advantage: 0.0265
2157	  verdict: PASS
2158	
2159	────────────────────────────────────────────────────────────────────────────────────────────────────
2160	EXP_ID: exp_conll_t_ablation_t05
2161	STATUS: DONE
2162	CONCLUSION: success
2163	HYPOTHESIS: CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.
2164	METRICS:
2165	  greedy_f1: 0.9077
2166	  oracle_f1: 0.9372
2167	  oracle_headroom: 0.0296
2168	  fleiss_kappa: 0.8948
2169	  softjaccard_rho_full: 0.4312
2170	  softjaccard_rho_cond: 0.4544
2171	  fleiss_rho_cond: 0.4519
2172	  degen_pct: 5.64
2173	  sample_f1_mean: 0.8993
2174	  verdict: PASS
2175	
2176	────────────────────────────────────────────────────────────────────────────────────────────────────
2177	EXP_ID: exp_conll_t_ablation_t08
2178	STATUS: DONE
2179	CONCLUSION: success
2180	HYPOTHESIS: CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.
2181	METRICS:
2182	  greedy_f1: 0.9069
2183	  oracle_f1: 0.9464
2184	  oracle_headroom: 0.0396
2185	  fleiss_kappa: 0.8199
2186	  softjaccard_rho_full: 0.4498
2187	  softjaccard_rho_cond: 0.4373
2188	  fleiss_rho_full: 0.4352
2189	  fleiss_rho_cond: 0.4128
2190	  degen_pct: 6.57
2191	  sample_f1_mean: 0.8854
2192	  verdict: PASS
2193	
2194	────────────────────────────────────────────────────────────────────────────────────────────────────
2195	EXP_ID: exp_conll_t_ablation_t12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d34a2450-6098-4c5e-afb3-c9cd86a02dbd"
}
```

</details>

---


### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 80471,
    "tool_uses": 15,
    "duration_ms": 131218
  },
  "last_tool_name": "Read",
  "uuid": "77fb1873-a6b4-44bc-8c9b-6929f9d3cf12",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01G6W14topypSSufnJkJ63aH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 2195,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "85f2fe5b-0549-4389-89c9-f4bde7d02f8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LocQfr5b7egKE3DPCQntRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7859,
      "cache_read_input_tokens": 72175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7859,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-22T18:19:57.685Z_

<details><summary>↩ Tool result · `toolu_01G6W14topypSSufnJkJ63aH`</summary>

```text
2195	EXP_ID: exp_conll_t_ablation_t12
2196	STATUS: DONE
2197	CONCLUSION: success
2198	HYPOTHESIS: CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.
2199	METRICS:
2200	  greedy_f1: 0.9071
2201	  oracle_f1: 0.9514
2202	  oracle_headroom: 0.0443
2203	  fleiss_kappa: 0.7092
2204	  softjaccard_rho_full: 0.4071
2205	  softjaccard_rho_cond: 0.3936
2206	  fleiss_rho_full: 0.3786
2207	  fleiss_rho_cond: 0.349
2208	  degen_pct: 9.22
2209	  sample_f1_mean: 0.8452
2210	  verdict: PASS
2211	
2212	────────────────────────────────────────────────────────────────────────────────────────────────────
2213	EXP_ID: exp_cross_model_consistency
2214	STATUS: DONE
2215	CONCLUSION: success
2216	HYPOTHESIS: Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.
2217	NOTES: B5 cross-model consistency on SciERC + FewNERD. Mixed (4Q+4L) consistently outperforms pure-model construction on both datasets. FewNERD: mixed sig. beats pure LLaMA (+0.42pp uni p=0, +0.29pp VC p=0.0001) and pure Qwen (+4.17pp uni, +4.50pp VC, all p=0). SciERC: mixed sig. beats pure Qwen (+1.77pp uni p=0.01, +1.77pp VC p=0.009); vs pure LLaMA marginal (+0.81pp uni p=0.13, +1.01pp VC p=0.07). Cros
2218	METRICS:
2219	  scierc: {'n_filtered': 529, 'qwen_greedy_f1': 0.6453, 'llama_greedy_f1': 0.646, 'degeneracy': {'pure_qwen': 0.1323, 'pure_llama': 0.1777, 'mixed': 0.0964}, 'construction_f1': {'pure_qwen_uniform': 0.6449, 'pure_qwen_vc': 0.6413, 'pure_llama_uniform': 0.6545, 'pure_llama_vc': 0.649, 'mixed_uniform': 0.6625, 'mixed_vc': 0.6591}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 1.77, 'p': 0.0102, 'ci': [0.27, 3.28]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 1.77, 'p': 0.0093, 'ci': [0.33, 3.27]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.81, 'p': 0.1304, 'ci': [-0.59, 2.25]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 1.01, 'p': 0.0702, 'ci': [-0.32, 2.38]}}}
2220	  fewnerd: {'n_filtered': 32565, 'qwen_greedy_f1': 0.7478, 'llama_greedy_f1': 0.7841, 'degeneracy': {'pure_qwen': 0.1004, 'pure_llama': 0.2336, 'mixed': 0.1158}, 'construction_f1': {'pure_qwen_uniform': 0.7499, 'pure_qwen_vc': 0.7448, 'pure_llama_uniform': 0.7873, 'pure_llama_vc': 0.7869, 'mixed_uniform': 0.7916, 'mixed_vc': 0.7898}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 4.17, 'p': 0, 'ci': [3.92, 4.4]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 4.5, 'p': 0, 'ci': [4.25, 4.75]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.42, 'p': 0, 'ci': [0.27, 0.58]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 0.29, 'p': 0.0001, 'ci': [0.13, 0.45]}}}
2221	
2222	────────────────────────────────────────────────────────────────────────────────────────────────────
2223	EXP_ID: exp_dgec_heterogeneous_t
2224	STATUS: PREPARING
2225	CONCLUSION: killed
2226	HYPOTHESIS: Mixing samples from T=0.7 and T=1.0 significantly reduces degeneracy compared to single-T sampling (by breaking temperature-induced mode collapse), enabling entity construction to achieve significant ΔF1 improvement even in configs where single-T construction was n.s. due to high degeneracy.
2227	NOTES: Hypothesis partially supported. T=0.7+T=1.0 mixed pool reduces degen (22.3%→17.0%) and improves construction (VC 3/3 seeds sig vs greedy), but cross-pool comparison (mixed vs T=1.0 alone) only 1/3 seeds significant. T gap matters: ΔT=0.2 (T=0.8+T=1.0) harmful, ΔT=0.3 (T=0.7+T=1.0) beneficial. VC weighting confirmed cross-T compatible. Awaiting Director conclusion classification.
2228	METRICS:
2229	  dataset: SciERC
2230	  n_instances: 529
2231	  t07_degen: 0.2231
2232	  t10_degen: 0.1235
2233	  mixed_degen: 0.1701
2234	  mixed_uniform_f1: 0.6584
2235	  mixed_vc_f1: 0.6609
2236	  cross_pool_uniform_delta: +0.006 (1/3 seeds sig)
2237	  cross_pool_vc_delta: +0.004 (1/3 seeds sig)
2238	  t08_t10_result: harmful (degen increased)
2239	  conclusion_preliminary: partially_supported
2240	
2241	────────────────────────────────────────────────────────────────────────────────────────────────────
2242	EXP_ID: exp_dgec_sj_construction
2243	STATUS: PREPARING
2244	CONCLUSION: killed
2245	HYPOTHESIS: SJ-weighted entity construction serves as control for VC — if SJ (soft entity overlap) works as well as VC (exact match consensus), any stronger QE signal suffices for construction; if VC specifically outperforms SJ, exact-match consensus has a unique advantage over soft similarity for entity-level selection.
2246	NOTES: COMPLETE (26 configs). SJ-weighted construction: 1 sig+ / 15 sig- / 10 ns. Qwen3-8B FT supplement (9 configs): 0+/6-/3ns — fully negative, consistent with 7B FT pattern. FewNERD -1.48pp mean (all seeds p=1.0). Definitively answers control question: NOT any stronger QE signal works for construction. SJ introduces noise at entity level. Only exception: SciERC 72B ZS (lowest precision, lowest degener
2247	METRICS:
2248	  total_configs: 26
2249	  significant_positive: 1
2250	  significant_negative: 15
2251	  not_significant: 10
2252	  best_config: scierc/72b/zs +2.0pp p=0.001
2253	  worst_config: fewnerd/8b_qwen3/ft mean -1.48pp all seeds p=1.0
2254	  qwen3_8b_ft_supplement: {'configs': 9, 'sig+': 0, 'sig-': 6, 'ns': 3, 'fewnerd_mean_delta': -1.48, 'scierc_mean_delta': -0.4, 'conll_mean_delta': -0.5, 'note': 'SJ fully negative on Qwen3-8B FT — consistent with Qwen2.5-7B FT pattern'}
2255	  m030_all_passed: True
2256	
2257	────────────────────────────────────────────────────────────────────────────────────────────────────
2258	EXP_ID: exp_dgec_vc_construction
2259	STATUS: PREPARING
2260	CONCLUSION: killed
2261	HYPOTHESIS: VC-weighted entity construction outperforms greedy and LP-weighted construction across configs because Vote Count is a more direct quality estimator for structured outputs — it measures exact-match consensus without relying on model-internal log probabilities. Especially effective in high-degeneracy regimes where LP compression makes LP-weighting uninformative.
2262	NOTES: COMPLETE (28 configs). VC-weighted construction: 9 sig+ / 10 sig- / 9 ns. Qwen3-8B FT supplement (9 configs): 3+/3-/3ns — VC inconsistent even on LP-success configs. SciERC s42 best (+1.40pp) but cross-seed unstable. CoNLL all negative (high degeneracy). WNUT17/SciERC lean positive but not robust. Key answer: VC does NOT reliably improve where LP already works — seed-dependent, dataset-dependent. 
2263	METRICS:
2264	  total_configs: 28
2265	  significant_positive: 9
2266	  significant_negative: 10
2267	  not_significant: 9
2268	  by_dataset: {'fewnerd': {'configs': 11, 'sig+': 5, 'sig-': 5, 'ns': 1, 'mean_delta_pp': -0.12}, 'wnut17': {'configs': 3, 'sig+': 2, 'sig-': 0, 'ns': 1, 'mean_delta_pp': 0.92}, 'scierc': {'configs': 7, 'sig+': 2, 'sig-': 0, 'ns': 5, 'mean_delta_pp': 0.62}, 'conll': {'configs': 7, 'sig+': 0, 'sig-': 5, 'ns': 2, 'mean_delta_pp': -0.33}}
2269	  qwen3_8b_ft_supplement: {'configs': 9, 'sig+': 3, 'sig-': 3, 'ns': 3, 'best': 'SciERC s42 +1.40pp p=0.017', 'worst': 'CoNLL s456 -0.54pp p=0.998', 'note': 'VC inconsistent on LP-success configs; seed-dependent on FewNERD; CoNLL all negative due to high degeneracy'}
2270	  m030_all_passed: True
2271	
2272	────────────────────────────────────────────────────────────────────────────────────────────────────
2273	EXP_ID: exp_docred_re_sc
2274	STATUS: DONE
2275	CONCLUSION: success
2276	HYPOTHESIS: SC diagnostic cascade (degeneracy, correlation-selection gap, F1-F4 failure modes) generalizes from NER to document-level RE on DocRED, with Qwen2.5-7B-Instruct showing similar failure patterns as seen in SciERC NER and SciERC RE.
2277	METRICS:
2278	  greedy_f1_mean: 0.0284
2279	  construction_f1_mean: 0.0338
2280	  majority_vote_f1_mean: 0.0263
2281	  oracle_f1_mean: 0.0999
2282	  greedy_micro_f1: 0.0297
2283	  construction_micro_f1: 0.0323
2284	  fleiss_kappa: -0.0253
2285	  soft_jaccard: 0.2907
2286	  degeneracy_rate: 0.035
2287	  n_instances: 200
2288	  failure_modes: {'F1_degeneracy': '3.5%', 'F2_low_agreement': '94.5%', 'F3_high_agreement_low_quality': '2.0%'}
2289	  bootstrap_diff: 0.0053
2290	  bootstrap_ci_95: [-0.004, 0.0149]
2291	  bootstrap_p_value: 0.1276
2292	  nondegen_construction_greedy_diff: 0.0055
2293	
2294	────────────────────────────────────────────────────────────────────────────────────────────────────
2295	EXP_ID: exp_e1_signal_routing
2296	STATUS: PREPARING
2297	CONCLUSION: killed
2298	HYPOTHESIS: A config-level signal router (RF/LR) can predict the optimal construction signal per config from features (degeneracy_rate, base_f1, oracle_headroom), outperforming always-LP baseline. Router ΔF1 should exceed always-LP ΔF1.
2299	NOTES: E1 signal routing. RF 56.2% LOO accuracy (below 60% target) but router ΔF1 +0.39pp > always-LP +0.15pp (2.6× improvement, target met). Low accuracy due to small n=16 and class imbalance. D176: appendix-only, not main claim.
2300	METRICS:
2301	  n_configs: 16
2302	  rf_loo_accuracy: 0.562
2303	  router_avg_delta_f1: 0.39
2304	  always_lp_delta_f1: 0.15
2305	  oracle_delta_f1: 0.56
2306	  top_features: ['oracle_headroom', 'degeneracy_rate', 'base_f1']
2307	  label_dist: {'lp_selection': 6, 'none': 5, 'consensus_theta2n': 3, 'consensus_lp_weighted': 1, 'majority_vote': 1}
2308	
2309	────────────────────────────────────────────────────────────────────────────────────────────────────
2310	EXP_ID: exp_e2_pretrained_conll_s123
2311	STATUS: DONE
2312	CONCLUSION: success
2313	HYPOTHESIS: E2 pre-trained baseline CoNLL seed=123: additional seed for pretrained Qwen2.5-7B-Instruct on CoNLL SC pipeline. Tests whether correlation-selection gap in pretrained model is reproducible across seeds.
2314	METRICS:
2315	  greedy_f1: 0.5413
2316	  oracle_f1: 0.6286
2317	  oracle_headroom: 0.087
2318	  rho_fk_full: 0.364
2319	  rho_sj_full: 0.394
2320	  rho_fk_cond: 0.434
2321	  rho_sj_cond: 0.463
2322	  logprob_rho_full: -0.027
2323	  logprob_rho_cond: 0.188
2324	  instances: 3453
2325	  verdict: MARGINAL
2326	
2327	────────────────────────────────────────────────────────────────────────────────────────────────────
2328	EXP_ID: exp_e2_pretrained_conll_s123_v2
2329	STATUS: DONE
2330	CONCLUSION: success
2331	HYPOTHESIS: E2 pretrained baseline CoNLL s123 v2: Qwen2.5-7B-Instruct (unfinetuned) on CoNLL SC pipeline N=8 T=1.0 seed=123. Cross-validation of E2 pretrained CoNLL performance.
2332	METRICS:
2333	  greedy_f1: 0.5364
2334	  oracle_f1: 0.6257
2335	  mv_f1: 0.6321
2336	  degeneracy: 0.365
2337	  n_instances: 2756
2338	
2339	────────────────────────────────────────────────────────────────────────────────────────────────────
2340	EXP_ID: exp_e2_pretrained_conll_s42
2341	STATUS: DONE
2342	CONCLUSION: success
2343	HYPOTHESIS: E2 pretrained baseline CoNLL s42: Qwen2.5-7B-Instruct (unfinetuned) on CoNLL SC pipeline N=8 T=1.0. Tests whether correlation-selection gap is model-intrinsic or fine-tuning artifact.
2344	METRICS:
2345	  greedy_f1: 0.5363
2346	  oracle_f1: 0.6299
2347	  mv_f1: 0.6284
2348	  degeneracy: 0.359
2349	  n_instances: 2756
2350	
2351	────────────────────────────────────────────────────────────────────────────────────────────────────
2352	EXP_ID: exp_e2_pretrained_conll_s456
2353	STATUS: DONE
2354	CONCLUSION: success
2355	HYPOTHESIS: E2 pre-trained baseline CoNLL seed=456: third seed for pretrained model SC analysis on CoNLL. Confirms reproducibility of correlation-selection gap pattern across seeds.
2356	METRICS:
2357	  greedy_f1: 0.5384
2358	  oracle_f1: 0.6272
2359	  oracle_headroom: 0.089
2360	  rho_fk_full: 0.376
2361	  rho_sj_full: 0.391
2362	  rho_fk_cond: 0.43
2363	  rho_sj_cond: 0.443
2364	  logprob_rho_full: -0.016
2365	  logprob_rho_cond: 0.197
2366	  instances: 3453
2367	  verdict: MARGINAL
2368	
2369	────────────────────────────────────────────────────────────────────────────────────────────────────
2370	EXP_ID: exp_e2_pretrained_fewnerd
2371	STATUS: DONE
2372	CONCLUSION: success
2373	HYPOTHESIS: The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact
2374	METRICS:
2375	  greedy_f1: 0.5384
2376	  oracle_f1: 0.6508
2377	  headroom: 0.1124
2378	  fleiss_kappa_mean: 0.4501
2379	  soft_jaccard_mean: 0.6881
2380	  structural_beats_surface: True
2381	  rho_advantage: 0.0501
2382	  mv_strict_f1: 0.5788
2383	  mv_incl_f1: 0.5667
2384	  mv_delta_strict_pp: 4.03
2385	  degeneracy_rate: 0.122
2386	  alpha_crit_eff_strict: 0.3065
2387	  mv_capture_rate: 0.359
2388	  gold_nonempty: 32565
2389	  n_instances: 37648
2390	  note: greedy/mv/oracle computed on gold-nonempty (32565); report.json values (0.5121 etc.) include 5083 gold-empty instances
2391	
2392	────────────────────────────────────────────────────────────────────────────────────────────────────
2393	EXP_ID: exp_e2_pretrained_fewnerd_s123
2394	STATUS: DONE
2395	CONCLUSION: success
2396	HYPOTHESIS: E2 pre-trained baseline seed 123: Qwen2.5-7B-Instruct (unfinetuned) on FewNERD SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline statistical power. If correlation-selection gap persists without fine-tuning → phenomenon is model-intrinsic.
2397	METRICS:
2398	  greedy_f1: 0.5381
2399	  oracle_f1: 0.652
2400	  headroom: 0.1139
2401	  fleiss_kappa: 0.443
2402	  soft_jaccard: 0.687
2403	  structural_beats_surface: True
2404	  rho_advantage: 0.047
2405	  mv_strict_f1: 0.5783
2406	  mv_incl_f1: 0.5658
2407	  mv_delta_strict_pp: 4.02
2408	  degeneracy_rate: 0.112
2409	  alpha_crit_eff_strict: 0.458
2410	  alpha_crit_eff_incl: 0.4442
2411	  mv_capture_rate: 0.353
2412	  gold_nonempty: 32565
2413	
2414	────────────────────────────────────────────────────────────────────────────────────────────────────
2415	EXP_ID: exp_e2_pretrained_fewnerd_s456
2416	STATUS: DONE
2417	CONCLUSION: success
2418	HYPOTHESIS: E2 pre-trained baseline FewNERD seed=456: third seed for pretrained Qwen2.5-7B-Instruct on FewNERD SC pipeline. Completes 3-seed set for statistical power on whether correlation-selection gap is model-intrinsic.
2419	METRICS:
2420	  greedy_f1: 0.5373
2421	  mv_strict_f1: 0.5738
2422	  mv_incl_f1: 0.5611
2423	  oracle_f1: 0.646
2424	  mv_delta_strict_pp: 3.65
2425	  degeneracy_rate: 0.118
2426	  alpha_crit_eff_strict: 0.3047
2427	  capture_rate: 0.336
2428	  n_instances: 32565
2429	
2430	────────────────────────────────────────────────────────────────────────────────────────────────────
2431	EXP_ID: exp_e2_pretrained_scierc
2432	STATUS: DONE
2433	CONCLUSION: negative
2434	HYPOTHESIS: Pre-trained Qwen2.5-7B-Instruct (no fine-tuning) on SciERC NER exhibits correlation-selection gap similar to fine-tuned models, demonstrating the gap is model-intrinsic rather than fine-tuning-induced.
2435	METRICS:
2436	  greedy_f1: 0.2418
2437	  oracle_f1: 0.3888
2438	  oracle_headroom: 0.147
2439	  fleiss_kappa_mean: 0.223
2440	  soft_jaccard_mean: 0.473
2441	  rho_SJ_full: 0.2193
2442	  rho_kappa_full: 0.2516
2443	  rho_SJ_cond: 0.1987
2444	  rho_kappa_cond: 0.1953
2445	  logprob_rho_full: 0.078
2446	  logprob_auroc_full: 0.5412
2447	  logprob_rho_cond: 0.1895
2448	  logprob_auroc_cond: 0.5527
2449	  sample_f1_mean: 0.2272
2450	  sample_f1_pct_zero: 46.29
2451	  structural_beats_surface: False
2452	  verdict: FAIL
2453	  warning: >30% samples F1=0
2454	
2455	────────────────────────────────────────────────────────────────────────────────────────────────────
2456	EXP_ID: exp_e2_pretrained_scierc_s123
2457	STATUS: DONE
2458	CONCLUSION: negative
2459	HYPOTHESIS: E2 pre-trained baseline SciERC seed=123: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline. Tests whether correlation-selection gap and structural vs surface patterns are consistent across seeds on SciERC.
2460	METRICS:
2461	  greedy_f1: 0.2436
2462	  mv_strict_f1: 0.2548
2463	  oracle_f1: 0.3941
2464	  mv_delta_strict_pp: 1.12
2465	  degeneracy_rate: 0.006
2466	  alpha_crit_eff_strict: 0.1468
2467	  n_instances: 529
2468	
2469	────────────────────────────────────────────────────────────────────────────────────────────────────
2470	EXP_ID: exp_e2_pretrained_scierc_s42_v2
2471	STATUS: DONE
2472	CONCLUSION: negative
2473	HYPOTHESIS: E2 pretrained baseline SciERC s42 v2: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Re-run for cross-validation of E2 pretrained SciERC performance.
2474	METRICS:
2475	  greedy_f1: 0.2434
2476	  oracle_f1: 0.3888
2477	  mv_f1: 0.2618
2478	  degeneracy: 0.009
2479	  n_instances: 529
2480	
2481	────────────────────────────────────────────────────────────────────────────────────────────────────
2482	EXP_ID: exp_e2_pretrained_scierc_s456
2483	STATUS: DONE
2484	CONCLUSION: negative
2485	HYPOTHESIS: E2 pre-trained baseline SciERC seed=456: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Third seed for E2 pre-trained baseline statistical power on SciERC.
2486	METRICS:
2487	  greedy_f1: 0.2436
2488	  mv_strict_f1: 0.2642
2489	  oracle_f1: 0.3952
2490	  mv_delta_strict_pp: 2.06
2491	  degeneracy_rate: 0.009
2492	  alpha_crit_eff_strict: 0.1537
2493	  n_instances: 529
2494	
2495	────────────────────────────────────────────────────────────────────────────────────────────────────
2496	EXP_ID: exp_entity_construction
2497	STATUS: DONE
2498	CONCLUSION: success
2499	HYPOTHESIS: Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.
2500	METRICS:
2501	  n16_fair_cv: {'scierc_ner': {'cv_uniform_delta': '+1.35pp', 'p_value': 0.018, 'significant': True}, 'conll_ner': {'cv_uniform_delta': '+0.10pp', 'p_value': 0.303, 'significant': False}, 'fewnerd_ner': {'cv_uniform_delta': '+1.32pp', 'p_value': 0, 'significant': True}, 'scierc_re': {'cv_uniform_delta': '+1.69pp', 'p_value': 0.049, 'significant': True}}
2502	  n8_fair_cv: {'scierc_ner': {'uniform_confirm': '+1.54pp (p=0.023, sig)', 'lp_weighted_confirm': '+1.67pp (p=0.004, sig)', 'cv_uniform': '+1.12pp (p=0.057, borderline)'}, 'conll_ner': {'cv_uniform': '-0.39pp (p=0.963, not sig)'}, 'fewnerd_ner': {'lp_weighted_cv': '+0.88pp (p=0.000, sig)', 'uniform_cv': '+0.32pp (p=0.003, sig)'}}
2503	  adaptive_combination: INVALIDATED - gold label leakage confirmed
2504	  note: 5-fold CV, bootstrap B=10000, paired one-sided
2505	
2506	────────────────────────────────────────────────────────────────────────────────────────────────────
2507	EXP_ID: exp_entity_token_lp
2508	STATUS: DONE
2509	CONCLUSION: negative
2510	HYPOTHESIS: Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.
2511	METRICS:
2512	  scierc_ner: {'greedy_f1': 0.643, 'full_lp_sel_f1': 0.6465, 'entity_lp_sel_f1': 0.6262, 'oracle_f1': 0.7845, 'entity_lp_delta_vs_full_lp': -0.0203}
2513	  conll_ner: {'greedy_f1': 0.9065, 'full_lp_sel_f1': 0.8989, 'entity_lp_sel_f1': 0.8659, 'oracle_f1': 0.948, 'entity_lp_delta_vs_full_lp': -0.033}
2514	  finding: entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)
2515	
2516	────────────────────────────────────────────────────────────────────────────────────────────────────
2517	EXP_ID: exp_fewnerd_5epoch_lp_s42
2518	STATUS: DONE
2519	CONCLUSION: success
2520	HYPOTHESIS: FewNERD 5-epoch checkpoint with LP selection will show improved F1 over majority voting, similar to the 3-epoch results, validating that LP selection is robust across training epochs
2521	METRICS:
2522	  greedy_f1: 0.7942
2523	  oracle_headroom_pp: 8.06
2524	  fleiss_kappa: 0.529
2525	  lp_auroc: 0.662
2526	  lp_rho: 0.302
2527	  lp_delta_pp_cpu_recompute: 0.12
2528	  lp_delta_pp_cpu_recompute_std: 0.04
2529	  note: GPU inference completed after kill; CPU recompute from existing samples gave LP Δ=+0.12±0.04pp (2-seed)
2530	
2531	────────────────────────────────────────────────────────────────────────────────────────────────────
2532	EXP_ID: exp_fewnerd_5epoch_s123
2533	STATUS: DONE
2534	CONCLUSION: success
2535	HYPOTHESIS: FewNERD 5-epoch epoch confound check seed=123: second seed for 5-epoch inference on FewNERD NER, N=8, T=1.0. Cross-validates whether epoch confound effects are consistent across seeds.
2536	METRICS:
2537	  greedy_f1: 0.7976
2538	  mv_strict_f1: 0.7941
2539	  mv_delta_strict_pp: -0.35
2540	  degeneracy_rate: 0.271
2541	  alpha_crit_eff_strict: 0.5468
2542	  oracle_f1: 0.8814
2543	
2544	────────────────────────────────────────────────────────────────────────────────────────────────────
2545	EXP_ID: exp_fewnerd_5epoch_s42
2546	STATUS: DONE
2547	CONCLUSION: success
2548	HYPOTHESIS: FewNERD 5-epoch epoch confound check seed=42: inference with 5-epoch fine-tuned Qwen3-8B (LoRA r=32 alpha=64) on FewNERD NER, N=8, T=1.0. Tests whether 3→5 epoch change affects degeneracy, MV performance, and signal correlations. If degeneracy increases or MV still fails, epoch count is not the confound.
2549	METRICS:
2550	  greedy_f1: 0.798
2551	  mv_strict_f1: 0.7935
2552	  mv_delta_strict_pp: -0.45
2553	  degeneracy_rate: 0.257
2554	  alpha_crit_eff_strict: 0.5369
2555	  oracle_f1: 0.8781
2556	
2557	────────────────────────────────────────────────────────────────────────────────────────────────────
2558	EXP_ID: exp_fewnerd_5epoch_s456
2559	STATUS: DONE
2560	CONCLUSION: success
2561	HYPOTHESIS: FewNERD 5-epoch epoch confound check seed=456: third seed for 5-epoch fine-tuned Qwen3-8B (LoRA r=32 alpha=64) on FewNERD NER, N=8, T=1.0. Completes 3-seed set for epoch confound analysis. If degeneracy/MV pattern consistent across seeds, epoch count is not the confound.
2562	METRICS:
2563	  greedy_f1: 0.7978
2564	  mv_strict_f1: 0.795
2565	  mv_delta_strict_pp: -0.28
2566	  degeneracy_rate: 0.259
2567	  alpha_crit_eff_strict: 0.8903
2568	  oracle_f1: 0.8793
2569	
2570	────────────────────────────────────────────────────────────────────────────────────────────────────
2571	EXP_ID: exp_fewnerd_freeform_n8_s42
2572	STATUS: DONE
2573	CONCLUSION: success
2574	HYPOTHESIS: R35-W6 free-form decoding ablation: FewNERD N=8 T=1.0 seed=42 without grammar constraints. FewNERD has lowest degeneracy (12% at N=8). If free-form degeneracy remains low (~12%), confirms degeneracy is model-intrinsic, not a constrained decoding artifact. Complements CoNLL free-form ablation (59.3% vs 56.7% constrained).
2575	METRICS:
2576	  greedy_f1: 0.7913
2577	  mv_strict_f1: 0.7586
2578	  mv_delta_pp: -3.26
2579	  lp_f1: 0.7922
2580	  lp_delta_pp: 0.09
2581	  degeneracy_rate: 0.091
2582	  n_instances: 32565
2583	  vs_constrained: {'greedy_f1_delta': '+0.00pp', 'mv_delta_change': '+0.01pp (identical)', 'lp_delta_change': '+0.02pp (identical)', 'degen_delta': '0.0pp (identical)'}
2584	  note: Freeform ≈ constrained on FewNERD. All deltas <0.02pp. Degeneracy 9.1% both. Fine-grained entity types constrain output space enough that grammar constraints have no additional effect.
2585	
2586	────────────────────────────────────────────────────────────────────────────────────────────────────
2587	EXP_ID: exp_fewnerd_mf4_s123_v2
2588	STATUS: DONE
2589	CONCLUSION: success
2590	HYPOTHESIS: MF4 pipeline fix retry: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (micro-F1). Replaces exp_fewnerd_mf4_s123 which failed due to GPU contention on autodl-5090. Required for 3-seed statistical power with unified pipeline.
2591	METRICS:
2592	  greedy_f1: 0.7909
2593	  oracle_f1: 0.8892
2594	  mv_strict_f1: 0.7648
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "20f58c08-0e09-4bdc-bbb2-ac6d82aad067"
}
```

</details>

---


### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 90730,
    "tool_uses": 16,
    "duration_ms": 137580
  },
  "last_tool_name": "Read",
  "uuid": "978c2068-032f-4536-89c7-e14a012990d9",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_01Pd1qR4Z6C9bKSzRM6WxnV2`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 2594,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "cd89ffc7-ba03-4f6c-b95a-40b58c9fd293",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaPa8pkz7S137CsXNC4Zn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10223,
      "cache_read_input_tokens": 80034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10223,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T18:20:04.042Z_

<details><summary>↩ Tool result · `toolu_01Pd1qR4Z6C9bKSzRM6WxnV2`</summary>

```text
2594	  mv_strict_f1: 0.7648
2595	  mv_delta_pp: -2.61
2596	  lp_f1: 0.7918
2597	  lp_delta_pp: 0.09
2598	  degeneracy_rate: 0.093
2599	  oracle_headroom_pp: 9.83
2600	  fleiss_kappa_mean: 0.3503
2601	  soft_jaccard_mean: 0.6701
2602	  rho_sj_full: 0.308
2603	  rho_sj_cond: 0.201
2604	  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)
2605	
2606	────────────────────────────────────────────────────────────────────────────────────────────────────
2607	EXP_ID: exp_fewnerd_mf4_s42
2608	STATUS: DONE
2609	CONCLUSION: success
2610	HYPOTHESIS: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.
2611	METRICS:
2612	  greedy_f1: 0.7911
2613	  oracle_f1: 0.8787
2614	  mv_strict_f1: 0.7585
2615	  mv_delta_pp: -3.27
2616	  lp_f1: 0.7918
2617	  lp_delta_pp: 0.07
2618	  degeneracy_rate: 0.091
2619	  oracle_headroom_pp: 8.76
2620	  fleiss_kappa_mean: 0.3537
2621	  soft_jaccard_mean: 0.6751
2622	  rho_sj_full: 0.1648
2623	  rho_sj_cond: 0.1989
2624	  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)
2625	
2626	────────────────────────────────────────────────────────────────────────────────────────────────────
2627	EXP_ID: exp_fewnerd_mf4_s456
2628	STATUS: DONE
2629	CONCLUSION: success
2630	HYPOTHESIS: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.
2631	METRICS:
2632	  greedy_f1: 0.7909
2633	  oracle_f1: 0.881
2634	  mv_strict_f1: 0.7685
2635	  mv_delta_pp: -2.24
2636	  lp_f1: 0.7921
2637	  lp_delta_pp: 0.12
2638	  degeneracy_rate: 0.081
2639	  oracle_headroom_pp: 9.01
2640	  fleiss_kappa_mean: 0.3555
2641	  soft_jaccard_mean: 0.6845
2642	  rho_sj_full: 0.3122
2643	  rho_sj_cond: 0.2559
2644	  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)
2645	
2646	────────────────────────────────────────────────────────────────────────────────────────────────────
2647	EXP_ID: exp_fewnerd_mf4_v2_s123
2648	STATUS: DONE
2649	CONCLUSION: success
2650	HYPOTHESIS: MF4 pipeline fix v2: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1. 3-seed statistical power.
2651	METRICS:
2652	  greedy_f1: 0.7883
2653	  oracle_f1: 0.8891
2654	  oracle_headroom: 0.1009
2655	  fleiss_kappa_mean: 0.3483
2656	  soft_jaccard_mean: 0.6689
2657	  rho_SJ_full: 0.307
2658	  rho_kappa_full: 0.1588
2659	  rho_SJ_cond: 0.1966
2660	  rho_kappa_cond: 0.0031
2661	  rho_advantage_full: 0.1482
2662	  rho_advantage_cond: 0.1935
2663	  structural_beats_surface: True
2664	  sample_f1_mean: 0.6364
2665	  sample_f1_std: 0.3819
2666	  sample_f1_pct_zero: 20.49
2667	  n_instances: 37648
2668	  n_valid_full: 32565
2669	  n_valid_cond: 28685
2670	  n_gold_empty_filtered: 5083
2671	  n_greedy_f1_zero_filtered: 3880
2672	  logprob_rho_full: 0.2193
2673	  logprob_tau_full: 0.1641
2674	  logprob_auroc_full: 0.6056
2675	  logprob_rho_cond: 0.1818
2676	  logprob_tau_cond: 0.1369
2677	  logprob_auroc_cond: 0.5892
2678	  verdict: MARGINAL
2679	
2680	────────────────────────────────────────────────────────────────────────────────────────────────────
2681	EXP_ID: exp_fewnerd_mf4_v2_s42
2682	STATUS: DONE
2683	CONCLUSION: negative
2684	HYPOTHESIS: MF4 pipeline fix v2: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1. 3-seed statistical power.
2685	METRICS:
2686	  greedy_f1: 0.7883
2687	  oracle_f1: 0.8783
2688	  oracle_headroom: 0.09
2689	  fleiss_kappa_mean: 0.3531
2690	  soft_jaccard_mean: 0.6747
2691	  rho_SJ_full: 0.1634
2692	  rho_kappa_full: 0.0476
2693	  rho_SJ_cond: 0.1987
2694	  rho_kappa_cond: -0.0327
2695	  rho_advantage_full: 0.1158
2696	  rho_advantage_cond: 0.2314
2697	  structural_beats_surface: True
2698	  sample_f1_mean: 0.6123
2699	  sample_f1_std: 0.3913
2700	  sample_f1_pct_zero: 23.09
2701	  n_instances: 37648
2702	  n_valid_full: 32565
2703	  n_valid_cond: 28682
2704	  n_gold_empty_filtered: 5083
2705	  n_greedy_f1_zero_filtered: 3883
2706	  logprob_rho_full: 0.1544
2707	  logprob_tau_full: 0.115
2708	  logprob_auroc_full: 0.5771
2709	  logprob_rho_cond: 0.1641
2710	  logprob_tau_cond: 0.123
2711	  logprob_auroc_cond: 0.5768
2712	  verdict: FAIL
2713	
2714	────────────────────────────────────────────────────────────────────────────────────────────────────
2715	EXP_ID: exp_fewnerd_mf4v2_s123_v3
2716	STATUS: DONE
2717	CONCLUSION: success
2718	HYPOTHESIS: FewNERD MF4v2 s123 re-run v3: corrected model path with nested tokenizer dir. N=8, T=1.0, seed=123.
2719	METRICS:
2720	  greedy_f1: 0.7911
2721	  mv_strict_f1: 0.7648
2722	  mv_delta_strict_pp: -2.63
2723	  mv_incl_f1: 0.7844
2724	  mv_delta_incl_pp: -0.67
2725	  degeneracy_rate: 0.093
2726	  alpha_crit_eff_strict: 0.6825
2727	  n_instances: 32565
2728	
2729	────────────────────────────────────────────────────────────────────────────────────────────────────
2730	EXP_ID: exp_fewnerd_mf4v2_s42_v3
2731	STATUS: DONE
2732	CONCLUSION: success
2733	HYPOTHESIS: FewNERD MF4v2 s42 re-run v3: corrected model path with nested tokenizer dir. N=8, T=1.0, seed=42.
2734	METRICS:
2735	  greedy_f1: 0.7911
2736	  mv_f1_strict: 0.7586
2737	  mv_delta_pp: -3.25
2738	  keyset_degeneracy: 0.091
2739	  alpha_crit_eff_strict: 0.4352
2740	  mv_f1_inclusive: 0.7783
2741	  oracle_f1: 0.8803
2742	
2743	────────────────────────────────────────────────────────────────────────────────────────────────────
2744	EXP_ID: exp_fewnerd_mf4v2_s456
2745	STATUS: DONE
2746	CONCLUSION: success
2747	HYPOTHESIS: MF4v2 pipeline (N=8, T=1.0, logprobs) on FewNERD with seed 456 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on fine-grained NER.
2748	METRICS:
2749	  greedy_f1: 0.7889
2750	  oracle_f1: 0.881
2751	  oracle_headroom: 0.0921
2752	  fleiss_kappa_mean: 0.3557
2753	  soft_jaccard_mean: 0.6848
2754	  sample_f1_mean: 0.6435
2755	  rho_softjaccard_full: 0.3133
2756	  rho_fleiss_full: 0.1647
2757	  rho_logprob_full: 0.245
2758	  verdict: MARGINAL
2759	
2760	────────────────────────────────────────────────────────────────────────────────────────────────────
2761	EXP_ID: exp_fewnerd_mf4v2_s456_v3
2762	STATUS: DONE
2763	CONCLUSION: success
2764	HYPOTHESIS: FewNERD MF4v2 s456 re-run v3: regenerate finetuned FewNERD seed=456 data on current server for provenance verification. N=8, T=1.0, seed=456. Original data lost with 5090-b.
2765	METRICS:
2766	  greedy_f1: 0.791
2767	  mv_strict_f1: 0.7686
2768	  mv_delta_strict_pp: -2.24
2769	  mv_incl_f1: 0.7857
2770	  mv_delta_incl_pp: -0.52
2771	  degeneracy_rate: 0.081
2772	  alpha_crit_eff_strict: 0.6793
2773	  n_instances: 32565
2774	
2775	────────────────────────────────────────────────────────────────────────────────────────────────────
2776	EXP_ID: exp_fewnerd_n16_s123
2777	STATUS: DONE
2778	CONCLUSION: success
2779	HYPOTHESIS: FewNERD N=16 seed=123: second seed for N=16 scaling analysis. Tests whether doubling samples from N=8 to N=16 increases oracle headroom consistently across seeds, and whether MV aggregation gap widens or narrows.
2780	METRICS:
2781	  greedy_f1: 0.7916
2782	  oracle_f1: 0.915
2783	  mv_strict_f1: 0.7798
2784	  mv_delta: -0.0118
2785	  degeneracy_rate: 0.048
2786	  alpha_crit_eff_strict: 0.6715
2787	  capture_rate: -0.095
2788	  n_instances: 32565
2789	  oracle_headroom: 0.1234
2790	
2791	────────────────────────────────────────────────────────────────────────────────────────────────────
2792	EXP_ID: exp_fewnerd_n16_s42
2793	STATUS: DONE
2794	CONCLUSION: success
2795	HYPOTHESIS: FewNERD N=16 (seed=42): extending N-scaling curve to N=16 for Qwen3-8B-FT. Tests whether oracle gains plateau or continue at higher sample counts, critical for F1(N)=a-b*N^(-c) scaling law estimation.
2796	METRICS:
2797	  greedy_f1: 0.7886
2798	  oracle_f1: 0.9059
2799	  oracle_headroom: 0.117
2800	  rho_fk_full: 0.162
2801	  rho_sj_full: 0.211
2802	  rho_fk_cond: -0.019
2803	  rho_sj_cond: 0.212
2804	  logprob_rho_full: 0.139
2805	  logprob_rho_cond: 0.175
2806	  instances: 37648
2807	
2808	────────────────────────────────────────────────────────────────────────────────────────────────────
2809	EXP_ID: exp_fewnerd_n16_s42_v2
2810	STATUS: DONE
2811	CONCLUSION: success
2812	HYPOTHESIS: FewNERD N=16 scaling: doubling sample count from N=8 to N=16 increases oracle headroom and tests whether additional samples improve MV aggregation or only expand the correlation-selection gap.
2813	METRICS:
2814	  greedy_f1: 0.7911
2815	  oracle_f1: 0.9077
2816	  mv_strict_f1: 0.7677
2817	  mv_delta: -0.0234
2818	  degeneracy_rate: 0.024
2819	  alpha_crit_eff_strict: 0.4053
2820	  capture_rate: -0.201
2821	  n_instances: 32565
2822	  oracle_headroom: 0.1166
2823	
2824	────────────────────────────────────────────────────────────────────────────────────────────────────
2825	EXP_ID: exp_fewnerd_n16_s456_v2
2826	STATUS: DONE
2827	CONCLUSION: success
2828	HYPOTHESIS: FewNERD N=16 (seed=456, v2 rerun): data lost in previous run. Extending N-scaling curve to N=16 for Qwen3-8B-FT, critical for F1(N)=a-b*N^(-c) scaling law. Third seed for 3-seed statistical power.
2829	METRICS:
2830	  greedy_f1: 0.791
2831	  oracle_f1: 0.9105
2832	  mv_strict_f1: 0.7767
2833	  mv_delta: -0.0143
2834	  degeneracy_rate: 0.048
2835	  alpha_crit_eff_strict: 0.4154
2836	  capture_rate: -0.12
2837	  n_instances: 32565
2838	  oracle_headroom: 0.1195
2839	
2840	────────────────────────────────────────────────────────────────────────────────────────────────────
2841	EXP_ID: exp_fewnerd_n32_s42
2842	STATUS: DONE
2843	CONCLUSION: success
2844	HYPOTHESIS: N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2.
2845	METRICS:
2846	  greedy_f1: 0.7914
2847	  mv_strict_f1: 0.7818
2848	  mv_delta_strict_pp: -0.96
2849	  mv_delta_unified_pp: -0.91
2850	  unified_greedy_f1: 0.7909
2851	  oracle_f1: 0.9305
2852	  degeneracy_rate: 0.014
2853	
2854	────────────────────────────────────────────────────────────────────────────────────────────────────
2855	EXP_ID: exp_fewnerd_pretrained_n16_s42
2856	STATUS: DONE
2857	CONCLUSION: failed
2858	HYPOTHESIS: Pretrained N-scaling: FewNERD N=16 with Qwen2.5-7B-Instruct. Fills pretrained N-scaling curve (N=8/16/32) for FewNERD. FewNERD pretrained N=8 showed +3.90pp MV gain. Tests monotonic scaling.
2859	METRICS:
2860	  crash_reason: UnicodeEncodeError in sampling.py:675 — vLLM lone Unicode surrogates in output, UTF-8 encoding rejects
2861	  progress: 72% (27110/37648)
2862	  fix_applied: sampling.py line 673: errors='replace' added to file write
2863	
2864	────────────────────────────────────────────────────────────────────────────────────────────────────
2865	EXP_ID: exp_fewnerd_pretrained_n32_s42
2866	STATUS: DONE
2867	CONCLUSION: failed
2868	HYPOTHESIS: Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence.
2869	METRICS:
2870	  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.
2871	  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)
2872	  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c
2873	
2874	────────────────────────────────────────────────────────────────────────────────────────────────────
2875	EXP_ID: exp_fewnerd_s789_n8
2876	STATUS: DONE
2877	CONCLUSION: success
2878	HYPOTHESIS: FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.
2879	METRICS:
2880	  greedy_f1: 0.7478
2881	  oracle_f1: 0.8714
2882	  headroom_pp: 12.37
2883	  degen_rate: 0.1177
2884	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
2885	  instance_count: 37648
2886	  n_valid: 32565
2887	  lp_sel_f1: 0.7614
2888	  lp_delta_pp: 1.36
2889	  lp_rho_global: 0.1788
2890	  lp_rho_cond: 0.176
2891	  dgs_f1: 0.7621
2892	  dgs_delta_pp: 1.43
2893	  dgs_vs_lp_pp: 0.07
2894	  best_signal: LP
2895	  four_seed_mean_greedy: 0.7481
2896	  four_seed_mean_lp_delta_pp: 1.38
2897	  four_seed_lp_delta_ci95: [1.32, 1.44]
2898	
2899	────────────────────────────────────────────────────────────────────────────────────────────────────
2900	EXP_ID: exp_fewnerd_t05_s123
2901	STATUS: DONE
2902	CONCLUSION: success
2903	HYPOTHESIS: FewNERD T-ablation seed=123 replication (T=0.5): second seed for statistical power on T=0.5 findings (highest rho_SJ=0.267, lowest oracle headroom=6.85% in seed=42). Confirms whether the diagnostic correlation ranking T=0.5>T=0.8>T=1.2 is stable across seeds or driven by seed-specific variance.
2904	METRICS:
2905	  greedy_f1: 0.789
2906	  oracle_f1: 0.864
2907	  rho_SJ_full: 0.35
2908	  rho_FK_full: 0.295
2909	  rho_advantage: 0.055
2910	  oracle_headroom: 0.075
2911	  degeneracy_pct: 13.5
2912	  verdict: MARGINAL
2913	
2914	────────────────────────────────────────────────────────────────────────────────────────────────────
2915	EXP_ID: exp_fewnerd_t05_s42
2916	STATUS: DONE
2917	CONCLUSION: success
2918	HYPOTHESIS: FewNERD temperature ablation (T=0.5): test how lower temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. Lower T should reduce sampling diversity, potentially increasing degeneracy while improving per-sample quality.
2919	NOTES: T=0.5 on FewNERD has highest absolute rho_SJ=0.267 (full), 0.299 (conditional) among T-ablation, but lowest oracle headroom (6.85%) meaning SC oracle gain is smallest. Lowest degeneracy (14.6%), highest sample quality (0.715). SJ advantage over Fleiss only 0.044 because Fleiss also high (0.223). Logprob baseline dominates at this T (rho=0.356). Tradeoff: low T maximizes diagnostic correlation but 
2920	METRICS:
2921	  greedy_f1: 0.7884
2922	  oracle_f1: 0.8569
2923	  oracle_headroom: 0.0685
2924	  sample_f1_mean: 0.7154
2925	  degeneracy_rate: 0.146
2926	  fleiss_kappa_mean: 0.6332
2927	  soft_jaccard_mean: 0.8653
2928	  rho_SJ_F1_full: 0.2667
2929	  rho_SJ_F1_conditional: 0.2988
2930	  rho_fleiss_F1_full: 0.2231
2931	  rho_fleiss_F1_conditional: 0.2338
2932	  rho_logprob_F1_full: 0.3558
2933	  rho_logprob_F1_conditional: 0.3025
2934	  structural_beats_surface: True
2935	  rho_advantage: 0.0435
2936	
2937	────────────────────────────────────────────────────────────────────────────────────────────────────
2938	EXP_ID: exp_fewnerd_t08_s123
2939	STATUS: DONE
2940	CONCLUSION: success
2941	HYPOTHESIS: FewNERD T-ablation seed=123 replication (T=0.8): second seed for statistical power on T=0.8 sweet-spot hypothesis (best rho_advantage=0.102 SJ over Fleiss, balanced oracle headroom=8.66% in seed=42). Tests robustness of T=0.8 as optimal operating point for SC diagnostic.
2942	METRICS:
2943	  greedy_f1: 0.789
2944	  oracle_f1: 0.884
2945	  rho_SJ_full: 0.336
2946	  rho_FK_full: 0.221
2947	  rho_advantage: 0.116
2948	  oracle_headroom: 0.095
2949	  degeneracy_pct: 16.7
2950	  verdict: MARGINAL
2951	
2952	────────────────────────────────────────────────────────────────────────────────────────────────────
2953	EXP_ID: exp_fewnerd_t08_s42
2954	STATUS: DONE
2955	CONCLUSION: success
2956	HYPOTHESIS: FewNERD temperature ablation (T=0.8): test how moderate-low temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. T=0.8 is a sweet-spot candidate balancing diversity and quality.
2957	NOTES: T=0.8 confirms sweet-spot hypothesis on FewNERD: best rho_SJ_F1=0.206 (full), 0.225 (conditional), lowest degeneracy (19%), highest sample quality (mean F1=0.662). SJ beats Fleiss by 0.102 rho advantage. Logprob baseline rho=0.232 (full) surprisingly high — SJ diagnostic matches logprob informativeness at this T. Verdict FAIL only because MVP single-subtask threshold not met, but T=0.8 is clearly 
2958	METRICS:
2959	  greedy_f1: 0.7884
2960	  oracle_f1: 0.875
2961	  oracle_headroom: 0.0866
2962	  sample_f1_mean: 0.6622
2963	  degeneracy_rate: 0.1897
2964	  fleiss_kappa_mean: 0.4439
2965	  soft_jaccard_mean: 0.7572
2966	  rho_SJ_F1_full: 0.2062
2967	  rho_SJ_F1_conditional: 0.2248
2968	  rho_fleiss_F1_full: 0.1038
2969	  rho_logprob_F1_full: 0.2323
2970	  rho_logprob_F1_conditional: 0.1984
2971	  structural_beats_surface: True
2972	  rho_advantage: 0.1024
2973	
2974	────────────────────────────────────────────────────────────────────────────────────────────────────
2975	EXP_ID: exp_fewnerd_t08_s456
2976	STATUS: DONE
2977	CONCLUSION: success
2978	HYPOTHESIS: FewNERD T-ablation seed=456 (T=0.8): third seed for T=0.8 sweet-spot, providing 3-seed statistical power for the key operating point. With seeds 42/123/456, can compute confidence intervals on rho_SJ and degeneracy_rate for the recommended T=0.8 setting.
2979	METRICS:
2980	  greedy_f1: 0.788
2981	  oracle_f1: 0.877
2982	  rho_SJ_full: 0.328
2983	  rho_FK_full: 0.202
2984	  rho_advantage: 0.126
2985	  oracle_headroom: 0.088
2986	  degeneracy_pct: 16.3
2987	  verdict: MARGINAL
2988	
2989	────────────────────────────────────────────────────────────────────────────────────────────────────
2990	EXP_ID: exp_fewnerd_t12_s123
2991	STATUS: DONE
2992	CONCLUSION: negative
2993	HYPOTHESIS: FewNERD T-ablation seed=123 replication (T=1.2): second seed for statistical power on T=1.2 negative result (over-diversification, 28.2% degeneracy, lowest rho_SJ=0.136 in seed=42). Confirms T=1.2 is consistently suboptimal for SC diagnostics on FewNERD.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "ec082e77-b148-4062-82ee-c156b7b8db3c"
}
```

</details>

---


### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 98934,
    "tool_uses": 17,
    "duration_ms": 144731
  },
  "last_tool_name": "Read",
  "uuid": "29e4fa7f-23c1-45c2-9efb-e975a6b75528",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01NHdEatZMCcguiyvA8Aq2Qj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 2993,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "0a280275-5529-4596-9121-3dd563150507",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNFBsWhEDf7754m8Z92jVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8166,
      "cache_read_input_tokens": 90257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8166,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-22T18:20:11.192Z_

<details><summary>↩ Tool result · `toolu_01NHdEatZMCcguiyvA8Aq2Qj`</summary>

```text
2993	HYPOTHESIS: FewNERD T-ablation seed=123 replication (T=1.2): second seed for statistical power on T=1.2 negative result (over-diversification, 28.2% degeneracy, lowest rho_SJ=0.136 in seed=42). Confirms T=1.2 is consistently suboptimal for SC diagnostics on FewNERD.
2994	METRICS:
2995	  greedy_f1: 0.789
2996	  oracle_f1: 0.887
2997	  rho_SJ_full: 0.285
2998	  rho_FK_full: 0.163
2999	  rho_advantage: 0.122
3000	  oracle_headroom: 0.098
3001	  degeneracy_pct: 24.7
3002	  verdict: FAIL
3003	
3004	────────────────────────────────────────────────────────────────────────────────────────────────────
3005	EXP_ID: exp_fewnerd_t12_s42
3006	STATUS: DONE
3007	CONCLUSION: negative
3008	HYPOTHESIS: FewNERD temperature ablation (T=1.2): test how higher temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. Higher T should increase diversity and reduce degeneracy but degrade per-sample quality.
3009	NOTES: T=1.2 on FewNERD: high oracle headroom (8.6%) but poor SC diagnostic correlation (rho_SJ=0.136 full, 0.213 conditional). High degeneracy (28.2% zero-F1 samples) and low per-sample quality (mean F1=0.55) indicate T=1.2 over-diversifies. Structural metric (SJ) still beats surface (Fleiss) by 0.075 rho advantage. Verdict: FAIL (MVP threshold not met on single subtask).
3010	METRICS:
3011	  greedy_f1: 0.7888
3012	  oracle_f1: 0.875
3013	  oracle_headroom: 0.0862
3014	  sample_f1_mean: 0.5524
3015	  degeneracy_rate: 0.2818
3016	  fleiss_kappa_mean: 0.283
3017	  soft_jaccard_mean: 0.5894
3018	  rho_SJ_F1_full: 0.136
3019	  rho_SJ_F1_conditional: 0.2125
3020	  rho_fleiss_F1_full: 0.0605
3021	  rho_logprob_F1_conditional: 0.1912
3022	  structural_beats_surface: True
3023	  rho_advantage: 0.0755
3024	
3025	────────────────────────────────────────────────────────────────────────────────────────────────────
3026	EXP_ID: exp_fewnerd_t12_s456
3027	STATUS: DONE
3028	CONCLUSION: success
3029	HYPOTHESIS: FewNERD temperature ablation (T=1.2, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT.
3030	METRICS:
3031	  greedy_f1: 0.7885
3032	  oracle_f1: 0.8775
3033	  oracle_headroom: 0.089
3034	  rho_fk_full: 0.191
3035	  rho_sj_full: 0.29
3036	  rho_fk_cond: 0.015
3037	  rho_sj_cond: 0.254
3038	  degeneracy_rate: None
3039	  logprob_rho_full: 0.196
3040	  logprob_rho_cond: 0.245
3041	  instances: 37648
3042	
3043	────────────────────────────────────────────────────────────────────────────────────────────────────
3044	EXP_ID: exp_fewrel_re_sc
3045	STATUS: DONE
3046	CONCLUSION: negative
3047	HYPOTHESIS: SC consensus construction improves RE micro-F1 over greedy decoding on FewRel (16 relation types, Wikipedia domain), extending cross-task universality evidence beyond SciERC and DocRED
3048	NOTES: Reviewer confirmed: same pattern as SciERC/DocRED RE (low F1, high F2). Micro_f1 and mean_f1 directions diverge: construction micro_f1 > greedy (0.0881 vs 0.0751) but mean_f1 < greedy. Paper uses micro_f1 per D204. Marked negative because bootstrap p=0.7572 (not significant).
3049	METRICS:
3050	  greedy_micro_f1: 0.0751
3051	  construction_micro_f1: 0.0881
3052	  majority_vote_f1_mean: 0.0591
3053	  oracle_f1_mean: 0.1768
3054	  fleiss_kappa_mean: 0.1506
3055	  soft_jaccard_mean: 0.3918
3056	  degeneracy_rate: 0.0586
3057	  bootstrap_p_value: 0.7572
3058	  failure_modes: {'F2_low_agreement': '75.8%', 'F3_high_agreement_low_quality': '15.2%', 'F1_degeneracy': '5.9%', 'none': '2.3%', 'F4_lp_quality_gap': '0.8%'}
3059	
3060	────────────────────────────────────────────────────────────────────────────────────────────────────
3061	EXP_ID: exp_freeform_ablation
3062	STATUS: DONE
3063	CONCLUSION: negative
3064	HYPOTHESIS: Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.
3065	METRICS:
3066	  lp_std_ratio_free_vs_constrained: 0.97
3067	  lp_range_ratio: 0.96
3068	  tied_fraction_constrained: 0.597
3069	  tied_fraction_freeform: 0.577
3070	  ner_selection_gap_constrained: 0.0059
3071	  ner_selection_gap_freeform: 0.0018
3072	  re_selection_gap_constrained: -0.0068
3073	  re_selection_gap_freeform: 0.0169
3074	  parse_rate: 0.9995
3075	  ner_vc_rho_constrained: 0.3792
3076	  ner_vc_rho_freeform: 0.4089
3077	
3078	────────────────────────────────────────────────────────────────────────────────────────────────────
3079	EXP_ID: exp_freeform_conll_4seed
3080	STATUS: DONE
3081	CONCLUSION: success
3082	HYPOTHESIS: Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.
3083	METRICS:
3084	  greedy_f1: 0.9035±0.0004
3085	  oracle_f1: 0.9460±0.0023
3086	  lp_range_median: 0.0581±0.0072
3087	  rho_sj: 0.4606±0.0188
3088	  rho_fk: 0.4372±0.0209
3089	  rho_em: 0.4714±0.0168
3090	  rho_vc: 0.4606±0.0138
3091	  rho_lp: 0.3262±0.0120
3092	  sel_f1_sj: 0.8994±0.0014
3093	  sel_f1_vc: 0.9006±0.0026
3094	  sel_f1_lp: 0.8958±0.0009
3095	  seeds: [42, 123, 456, 789]
3096	  n_samples: 8
3097	  temperature: 1
3098	  instances: 2756
3099	  gold_empty_filtered: 697
3100	
3101	────────────────────────────────────────────────────────────────────────────────────────────────────
3102	EXP_ID: exp_freeform_seed123
3103	STATUS: DONE
3104	CONCLUSION: success
3105	HYPOTHESIS: Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
3106	METRICS:
3107	  inference: {'n_instances': 551, 'n_samples': 8, 'total_samples': 4408, 'total_parsed': 4406, 'parse_rate_pct': 99.95, 'elapsed_seconds': 228.1}
3108	  freeform: {'selection_ner': {'greedy': 0.6194, 'selected': 0.6222, 'gap': 0.0028}, 'selection_re': {'greedy': 0.2874, 'selected': 0.305, 'gap': 0.0176}, 'logprob_variance': {'mean_std': 0.019881, 'mean_range': 0.059864, 'tied_pct': 57.7}, 'qe_ner': {'n': 529, 'SJ': {'rho': 0.384214, 'auroc': 0.748728}, 'FK': {'rho': 0.323956, 'auroc': 0.766039}, 'logprob': {'rho': 0.217297, 'auroc': 0.701657}, 'EM': {'rho': 0.326887, 'auroc': 0.52533}, 'voting_conf': {'rho': 0.407893, 'auroc': 0.799676}}, 'qe_re': {'n': 397, 'SJ': {'rho': 0.272776, 'auroc': 0.614056}, 'FK': {'rho': 0.314429, 'auroc': 0.678534}, 'logprob': {'rho': 0.309673, 'auroc': 0.70414}, 'EM': {'rho': 0.137216, 'auroc': 0.487342}, 'voting_conf': {'rho': 0.316667, 'auroc': 0.647442}}}
3109	  constrained_ref: {'selection_ner': {'greedy': 0.6182, 'selected': 0.6241, 'gap': 0.0059}, 'selection_re': {'greedy': 0.2913, 'selected': 0.2845, 'gap': -0.0068}}
3110	  comparison: {'variance_ratio_std': 0.97, 'variance_ratio_range': 0.96, 'tied_reduction_pp': 2}
3111	
3112	────────────────────────────────────────────────────────────────────────────────────────────────────
3113	EXP_ID: exp_freeform_seed456
3114	STATUS: DONE
3115	CONCLUSION: success
3116	HYPOTHESIS: Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
3117	METRICS:
3118	  inference: {'n_instances': 551, 'n_samples': 8, 'total_samples': 4408, 'total_parsed': 4407, 'parse_rate_pct': 99.98, 'elapsed_seconds': 232.4}
3119	  freeform: {'selection_ner': {'greedy': 0.6198, 'selected': 0.6205, 'gap': 0.0007}, 'selection_re': {'greedy': 0.2908, 'selected': 0.3108, 'gap': 0.02}, 'logprob_variance': {'mean_std': 0.018631, 'mean_range': 0.056792, 'tied_pct': 58.4}, 'qe_ner': {'n': 529, 'SJ': {'rho': 0.378498, 'auroc': 0.707769}, 'FK': {'rho': 0.286163, 'auroc': 0.754779}, 'LP': {'rho': 0.227089, 'auroc': 0.672081}, 'EM': {'rho': 0.319997, 'auroc': 0.47789}, 'VC': {'rho': 0.416853, 'auroc': 0.756543}}, 'qe_re': {'n': 397, 'SJ': {'rho': 0.211331, 'auroc': 0.572335}, 'FK': {'rho': 0.259074, 'auroc': 0.652998}, 'LP': {'rho': 0.306382, 'auroc': 0.70134}, 'EM': {'rho': 0.1043, 'auroc': 0.461641}, 'VC': {'rho': 0.301507, 'auroc': 0.628873}}}
3120	  constrained_ref: {'selection_ner': {'greedy': 0.6182, 'selected': 0.6241, 'gap': 0.0059}, 'selection_re': {'greedy': 0.2913, 'selected': 0.2845, 'gap': -0.0068}, 'logprob_variance': {'mean_std': 0.020589, 'mean_range': 0.062305, 'tied_pct': 59.7}}
3121	  comparison: {'variance_ratio_std': 0.9, 'variance_ratio_range': 0.91, 'tied_reduction_pp': 1.3}
3122	
3123	────────────────────────────────────────────────────────────────────────────────────────────────────
3124	EXP_ID: exp_freeform_seed789
3125	STATUS: DONE
3126	CONCLUSION: success
3127	HYPOTHESIS: Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
3128	NOTES: Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.
3129	METRICS:
3130	  inference: {'n_instances': 551, 'n_samples': 8, 'total_samples': 4408, 'total_parsed': 4408, 'parse_rate_pct': 100, 'elapsed_seconds': 227.5}
3131	  freeform: {'selection_ner': {'greedy': 0.6205, 'selected': 0.6232, 'gap': 0.0027}, 'selection_re': {'greedy': 0.2909, 'selected': 0.31, 'gap': 0.0191}, 'logprob_variance': {'mean_std': 0.0183, 'mean_range': 0.054908, 'tied_pct': 59}, 'qe_ner': {'n': 529, 'SJ': {'rho': 0.393995, 'auroc': 0.734474}, 'FK': {'rho': 0.312292, 'auroc': 0.794384}, 'LP': {'rho': 0.247096, 'auroc': 0.677824}, 'EM': {'rho': 0.320383, 'auroc': 0.527033}, 'VC': {'rho': 0.420625, 'auroc': 0.768111}}, 'qe_re': {'n': 397, 'SJ': {'rho': 0.201746, 'auroc': 0.574388}, 'FK': {'rho': 0.2202, 'auroc': 0.633014}, 'LP': {'rho': 0.295765, 'auroc': 0.687067}, 'EM': {'rho': 0.103633, 'auroc': 0.474737}, 'VC': {'rho': 0.306868, 'auroc': 0.642197}}}
3132	  constrained_ref: {'selection_ner': {'greedy': 0.6182, 'selected': 0.6241, 'gap': 0.0059}, 'selection_re': {'greedy': 0.2913, 'selected': 0.2845, 'gap': -0.0068}, 'logprob_variance': {'mean_std': 0.020589, 'mean_range': 0.062305, 'tied_pct': 59.7}}
3133	  comparison: {'variance_ratio_std': 0.89, 'variance_ratio_range': 0.88, 'tied_reduction_pp': 0.7}
3134	
3135	────────────────────────────────────────────────────────────────────────────────────────────────────
3136	EXP_ID: exp_freeform_seed789_v3
3137	STATUS: DONE
3138	CONCLUSION: success
3139	HYPOTHESIS: Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.
3140	METRICS:
3141	  n_instances: 551
3142	  n_samples: 8
3143	  parse_rate_pct: 100
3144	  elapsed_seconds: 229.7
3145	  freeform_ner_selection_gap: 0.0028
3146	  freeform_re_selection_gap: 0.0219
3147	  freeform_lp_std: 0.0183
3148	  freeform_lp_range: 0.054908
3149	  freeform_tied_pct: 59
3150	  re_lp_flip_positive: True
3151	  variance_ratio_std: 0.89
3152	  variance_ratio_range: 0.88
3153	
3154	────────────────────────────────────────────────────────────────────────────────────────────────────
3155	EXP_ID: exp_frontier_sc_claude_sonnet4
3156	STATUS: DONE
3157	CONCLUSION: success
3158	HYPOTHESIS: Frontier model Claude Sonnet 4 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists across model families (GPT + Claude + Gemini + DeepSeek), the finding is universal and not model-specific.
3159	METRICS:
3160	  greedy_f1: 0.6068
3161	  mv_f1: 0.6226
3162	  oracle_f1: 0.6544
3163	  degeneracy_rate: 0.74
3164	  selection_gap: 0.0318
3165	  parse_failures: 103
3166	  api_calls: 1600
3167	  wall_clock_seconds: 6118
3168	  instances: 200
3169	
3170	────────────────────────────────────────────────────────────────────────────────────────────────────
3171	EXP_ID: exp_frontier_sc_deepseek
3172	STATUS: DONE
3173	CONCLUSION: success
3174	HYPOTHESIS: Frontier model DeepSeek Chat on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation of correlation-selection gap universality.
3175	METRICS:
3176	  greedy_f1: 0.3992
3177	  mv_f1: 0.4243
3178	  oracle_f1: 0.714
3179	  degeneracy_rate: 0.055
3180	  agreement_rho: 0.2051
3181	  fleiss_kappa_rho: 0.1471
3182	  sj_rho: 0.1635
3183	  mv_gain_over_greedy: 0.0251
3184	  selection_gap: 0.2897
3185	  parse_failure_count: 751
3186	  total_api_calls: 1600
3187	  elapsed_s: 4043.7
3188	
3189	────────────────────────────────────────────────────────────────────────────────────────────────────
3190	EXP_ID: exp_frontier_sc_gemini25pro
3191	STATUS: DONE
3192	CONCLUSION: success
3193	HYPOTHESIS: Frontier model Gemini 2.5 Pro on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation. If correlation-selection gap persists across GPT + Claude + Gemini + DeepSeek, the finding is universal.
3194	METRICS:
3195	  greedy_f1: 0.6301
3196	  mv_f1: 0.6446
3197	  oracle_f1: 0.7575
3198	  mv_gain_pp: 1.45
3199	  selection_gap_pp: 11.29
3200	  mv_captures_pct: 11.4
3201	  agreement_rho: 0.3887
3202	  degeneracy_rate: 0.285
3203	  fleiss_kappa: 0.5185
3204	  soft_jaccard: 0.8023
3205	  alpha_crit: 0.4756
3206	  alpha_crit_eff: 0.6651
3207	  parse_failure_rate: 0.119
3208	  n_instances: 200
3209	  mv_wins: 33
3210	  mv_ties: 144
3211	  mv_loses: 23
3212	  verdict: MV helps (+1.45pp), captures 11% of oracle headroom
3213	
3214	────────────────────────────────────────────────────────────────────────────────────────────────────
3215	EXP_ID: exp_frontier_sc_gpt55_fewnerd_v2
3216	STATUS: DONE
3217	CONCLUSION: success
3218	HYPOTHESIS: Frontier model GPT-5.5 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists in frontier models, the finding is fundamental and not a model capability limitation. Previous attempt failed due to API credit exhaustion.
3219	METRICS:
3220	  greedy_f1: 0.6382
3221	  mv_f1: 0.6521
3222	  oracle_f1: 0.7203
3223	  degeneracy_rate: 0.5
3224	  rho_agreement: 0.3551
3225	  rho_fk: 0.3515
3226	  rho_sj: 0.3461
3227	  instances: 200
3228	
3229	────────────────────────────────────────────────────────────────────────────────────────────────────
3230	EXP_ID: exp_hidden_state_probe
3231	STATUS: DONE
3232	CONCLUSION: success
3233	HYPOTHESIS: Entity quality information (in_gold vs not) is encoded in the fine-tuned model's last-layer hidden states at entity token positions. If probe AUROC ≈ MV AUROC (0.87), the signal exists in representation but ESJ prompt-based reading (AUROC=0.51) fails to access it — a prompt interface failure. If probe AUROC ≈ 0.51, the information is genuinely absent from single-sample representations.
3234	NOTES: Probe AUROC far exceeds both baselines: FewNERD 0.987, CoNLL 0.980 vs MV 0.87 vs ESJ 0.51. The model's last-layer hidden states at entity token positions encode correctness information at very high fidelity — even higher than what multi-sample voting captures. This is strong evidence for a prompt interface failure: the model knows which entities are correct but cannot express this through promptin
3235	METRICS:
3236	  entity_level_stratifiedkfold_auroc: {'conll': 0.9796, 'fewnerd': 0.9872, 'scierc': 0.9766}
3237	  groupkfold_auroc_corrected: {'conll': 0.8849, 'fewnerd': 0.6513, 'scierc': 0.6344}
3238	  groupkfold_delta: {'conll': -0.0947, 'fewnerd': -0.3359, 'scierc': -0.3422}
3239	  groupkfold_probe_above_mv: {'conll': True, 'fewnerd': False, 'scierc': False}
3240	  baselines: {'mv_agreement_auroc': 0.87, 'esj_prompt_auroc': 0.51}
3241	  note: GroupKFold fixes instance-level leakage. Only conll retains probe > MV after correction.
3242	
3243	────────────────────────────────────────────────────────────────────────────────────────────────────
3244	EXP_ID: exp_llama3b_scierc_ablation
3245	STATUS: DONE
3246	CONCLUSION: success
3247	HYPOTHESIS: Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.
3248	METRICS:
3249	  ner_full: {'SJ_rho': 0.3754, 'FK_rho': 0.2676, 'LP_rho': 0.2662, 'EM_rho': 0.3341, 'VC_rho': 0.4602, 'SJ_auroc': 0.7383, 'FK_auroc': 0.6714, 'LP_auroc': 0.633, 'EM_auroc': 0.7763, 'VC_auroc': 0.7429, 'n': 529}
3250	  ner_cond: {'SJ_rho': 0.3445, 'FK_rho': 0.2125, 'LP_rho': 0.2099, 'EM_rho': 0.3952, 'VC_rho': 0.3815, 'SJ_auroc': 0.7292, 'FK_auroc': 0.66, 'LP_auroc': 0.6156, 'EM_auroc': 0.7822, 'VC_auroc': 0.7222, 'n': 476}
3251	  greedy_f1: 0.6267
3252	  oracle_f1: 0.763
3253	  oracle_headroom: 0.1363
3254	  selection_f1_SJ: 0.6328
3255	  selection_f1_VC: 0.6113
3256	  selection_f1_FK: 0.6295
3257	  selection_f1_EM: 0.6174
3258	  selection_f1_LP: 0.6279
3259	  n_gold_empty: 22
3260	  structural_beats_surface: True
3261	  rho_advantage_SJ_over_FK: 0.1078
3262	
3263	────────────────────────────────────────────────────────────────────────────────────────────────────
3264	EXP_ID: exp_llama_fewnerd_inference
3265	STATUS: DONE
3266	CONCLUSION: success
3267	HYPOTHESIS: LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.
3268	METRICS:
3269	  3seed_mean: {'greedy_f1': 0.7842, 'oracle_f1': 0.8843, 'headroom_pp': 10.01, 'degeneracy_pct': 23.36, 'lp_delta_pp': 0.36, 'dgs_delta_pp': -0.35}
3270	  seed_42: {'greedy_f1': 0.7841, 'oracle_f1': 0.8854, 'degen': 27.32}
3271	  seed_123: {'greedy_f1': 0.784, 'oracle_f1': 0.8839, 'degen': 24.63}
3272	  seed_456: {'greedy_f1': 0.7844, 'oracle_f1': 0.8835, 'degen': 18.13}
3273	  signal_ranking: LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)
3274	  lp_only_positive: True
3275	  n_instances_gold_filtered: 32565
3276	
3277	────────────────────────────────────────────────────────────────────────────────────────────────────
3278	EXP_ID: exp_llama_fewnerd_lora
3279	STATUS: DONE
3280	CONCLUSION: success
3281	HYPOTHESIS: LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER
3282	METRICS:
3283	  epoch: 3
3284	  train_loss: 0.0516
3285	  eval_loss: 0.0323
3286	  train_runtime_hours: 15.35
3287	  total_steps: 24708
3288	  final_checkpoint: checkpoint-24708
3289	  adapter_size_mb: 320
3290	
3291	────────────────────────────────────────────────────────────────────────────────────────────────────
3292	EXP_ID: exp_llama_scierc_seed456
3293	STATUS: DONE
3294	CONCLUSION: success
3295	HYPOTHESIS: LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.
3296	METRICS:
3297	  greedy_f1: 0.6457
3298	  oracle_f1: 0.7574
3299	  headroom: 0.1117
3300	  dgs_f1: 0.6454
3301	  degen_rate: 0.2741
3302	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
3303	  rho_SJ_full: 0.3663
3304	  rho_FK_full: 0.3115
3305	  rho_logprob_full: 0.1911
3306	  rho_EM_full: 0.3088
3307	  rho_vc_full: 0.4135
3308	  auroc_SJ_full: 0.7061
3309	  auroc_EM_full: 0.7538
3310	  n_valid: 529
3311	  n_conditional: 478
3312	
3313	────────────────────────────────────────────────────────────────────────────────────────────────────
3314	EXP_ID: exp_lp_alignment_gating
3315	STATUS: DONE
3316	CONCLUSION: success
3317	HYPOTHESIS: Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.
3318	METRICS:
3319	  adjusted_score: mean_rho * valid_ratio
3320	  threshold: 0.3
3321	  accuracy: 3/3 datasets correct
3322	  robust_range: 0.2-0.4
3323	
3324	────────────────────────────────────────────────────────────────────────────────────────────────────
3325	EXP_ID: exp_lp_scierc_t07
3326	STATUS: DONE
3327	CONCLUSION: success
3328	HYPOTHESIS: LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 "LP compression is model/task intrinsic" claim。对比 T=1.0 的 LP range 分布。
3329	METRICS:
3330	  ner_greedy_f1: 0.662
3331	  ner_oracle_f1: 0.764
3332	  ner_headroom_pp: 10.2
3333	  ner_rho_sj_full: 0.365
3334	  ner_rho_sj_cond: 0.363
3335	  ner_rho_fk_full: 0.289
3336	  ner_rho_fk_cond: 0.255
3337	  lp_rho_full: 0.249
3338	  lp_rho_cond: 0.185
3339	  ner_rho_advantage: 0.076
3340	  zero_f1_pct: 11
3341	  full_n: 529
3342	  cond_n: 477
3343	  verdict: success_supports_LP_compression_claim
3344	
3345	────────────────────────────────────────────────────────────────────────────────────────────────────
3346	EXP_ID: exp_lsc_latent_sc
3347	STATUS: DONE
3348	CONCLUSION: negative
3349	HYPOTHESIS: Latent Self-Consistency: F4 diagnostic proves LP is compressed (median range 0.041 nats). Hidden states contain richer per-sample information than scalar LP. Entity-level mean-pooled hidden state representations enable latent aggregation (centroid selection, latent confidence scoring, clustering) that bypasses LP compression and provides discriminative per-sample ranking unavailable from output-sp
3350	METRICS:
3351	  centroid_selection_f1: 0.7593
3352	  lp_selection_f1: 0.7845
3353	  latent_entity_conf_f1: 0.8385
3354	  majority_vote_f1: 0.8366
3355	  greedy_f1: 0.7793
3356	  oracle_f1: 0.8668
3357	  lp_vs_latent_rho: 0.518
3358	  entity_match_rate: 0.9945
3359	  n_instances: 2000
3360	  runtime_s: 507
3361	
3362	────────────────────────────────────────────────────────────────────────────────────────────────────
3363	EXP_ID: exp_pareto_diversity_quality
3364	STATUS: PREPARING
3365	CONCLUSION: killed
3366	HYPOTHESIS: There exists a Pareto frontier in the diversity (1-degeneracy) vs construction quality (ΔF1) space across temperature configurations. Well-separated temperature mixing (T=0.7+T=1.0) achieves Pareto optimality for both uniform and VC construction, while VC-weighted construction flattens the trade-off slope, reducing the diversity cost of quality.
3367	NOTES: A4 Pareto diversity-quality analysis on SciERC. Mix T=0.7+T=1.0 is dual-Pareto optimal (uniform +1.43pp, VC +1.67pp). VC construction flattens trade-off slope ~50% vs uniform — increasing diversity costs less quality. Mix T=0.8+T=1.0 is dominated (close T → higher degeneracy, no construction gain). Confirms DGEC heterogeneous-T finding: ΔT matters, ΔT=0.3 beneficial, ΔT=0.2 harmful. Pareto plot ar
3368	METRICS:
3369	  dataset: SciERC
3370	  configs: {'t07': {'one_minus_degen': 0.777, 'uniform_delta': 1.81, 'vc_delta': 1.17, 'pareto': 'uniform only'}, 't08': {'one_minus_degen': 0.819, 'uniform_delta': 1.25, 'vc_delta': 1.68, 'pareto': 'VC only'}, 'mix_07_10': {'one_minus_degen': 0.83, 'uniform_delta': 1.43, 'vc_delta': 1.67, 'pareto': 'both'}, 't10': {'one_minus_degen': 0.877, 'uniform_delta': 0.75, 'vc_delta': 1.21, 'pareto': 'both (highest diversity)'}, 'mix_08_10': {'one_minus_degen': 0.789, 'uniform_delta': -0.17, 'vc_delta': 0.47, 'pareto': 'dominated'}}
3371	  vc_slope_reduction: ~50% flatter than uniform
3372	  key_insight: well-separated T mixing dual Pareto optimal; close T mixing dominated
3373	
3374	────────────────────────────────────────────────────────────────────────────────────────────────────
3375	EXP_ID: exp_qwen25_14b_fewnerd
3376	STATUS: DONE
3377	CONCLUSION: success
3378	HYPOTHESIS: The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.
3379	NOTES: 2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773.
3380	METRICS:
3381	  epoch: 5
3382	  train_loss: 0.0348
3383	  eval_loss: 0.0323
3384	  train_runtime_hours: 29.8
3385	  train_samples_per_second: 6.141
3386	  train_steps_per_second: 0.384
3387	  total_steps: 41180
3388	
3389	────────────────────────────────────────────────────────────────────────────────────────────────────
3390	EXP_ID: exp_qwen25_32b_fewnerd
3391	STATUS: DONE
3392	CONCLUSION: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "bd2f14ec-6310-47f6-ac58-7e3d8bf05b82"
}
```

</details>

---


### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 109633,
    "tool_uses": 18,
    "duration_ms": 150816
  },
  "last_tool_name": "Read",
  "uuid": "e1189419-2815-4523-926c-1ea14997d704",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_01Wo89YRC5j2GnchQiPF4gve`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 3392,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "4fadb546-df38-4fa2-aee5-c2a6a3f55331",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195eUkXkkp51Z57vGqnMScU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10663,
      "cache_read_input_tokens": 98423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10663,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T18:20:17.284Z_

<details><summary>↩ Tool result · `toolu_01Wo89YRC5j2GnchQiPF4gve`</summary>

```text
3392	CONCLUSION: success
3393	HYPOTHESIS: Qwen2.5-32B-Instruct QLoRA fine-tuning on FewNERD: scaling model from 8B→32B should improve per-sample NER quality, enabling stronger SC diagnostic signals. LoRA r=32, alpha=64, target all attention+FFN projections, 5 epochs, 4×RTX 5090.
3394	NOTES: 2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.
3395	METRICS:
3396	  total_steps: 41180
3397	  epochs: 5
3398	  best_checkpoint: checkpoint-32000
3399	  best_eval_loss: 0.0334
3400	  final_train_loss: 0.005
3401	  final_eval_loss: 0.0412
3402	  initial_loss: 0.559
3403	  training_time_hours: 38.5
3404	  lora_rank: 32
3405	  lora_alpha: 64
3406	  note: Overfitting after epoch ~3.9; best eval_loss at step 32000 (epoch 3.89). Post-training load-best-model OOM (rank2) but all checkpoints saved correctly.
3407	
3408	────────────────────────────────────────────────────────────────────────────────────────────────────
3409	EXP_ID: exp_qwen25_72b_fewshot
3410	STATUS: DONE
3411	CONCLUSION: negative
3412	HYPOTHESIS: Few-shot prompting improves base NER F1 and LP signal quality, enabling LP-weighted construction to outperform greedy selection via dual-gating (sufficient LP ρ + low degeneracy).
3413	METRICS:
3414	  scierc: {'lp_rho': 0.06, 'sj_rho': 0.293, 'fk_rho': 0.301, 'vc_rho': 0.258, 'em_rho': 0.205, 'degen_pct': 16.6, 'greedy_f1': 0.461, 'oracle_f1': 0.604, 'construction_f1': 0.461, 'construction_delta_pp': -0.08, 'bootstrap_p': 0.544}
3415	  conll: {'lp_rho': 0.106, 'sj_rho': 0.442, 'fk_rho': 0.451, 'vc_rho': 0.426, 'em_rho': 0.403, 'degen_pct': 70, 'greedy_f1': 0.745, 'oracle_f1': 0.796, 'construction_f1': 0.745, 'construction_delta_pp': 0.03, 'bootstrap_p': 0.417}
3416	  fewnerd: {'lp_rho': 0.161, 'sj_rho': 0.345, 'fk_rho': 0.327, 'vc_rho': 0.41, 'em_rho': 0.302, 'degen_pct': 45.2, 'greedy_f1': 0.619, 'oracle_f1': 0.702, 'construction_f1': 0.619, 'construction_delta_pp': 0.02, 'bootstrap_p': 0.401}
3417	
3418	────────────────────────────────────────────────────────────────────────────────────────────────────
3419	EXP_ID: exp_qwen25_72b_zeroshot
3420	STATUS: DONE
3421	CONCLUSION: negative
3422	HYPOTHESIS: A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.
3423	NOTES: 2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC ✅ (551) CoNLL ✅ (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4×5090 100% util. Cron registered.
3424	METRICS:
3425	  scierc: {'greedy_f1': 0.3993, 'lp_rho': 0.081, 'vc_rho': 0.277, 'sj_rho': 0.217, 'degen_rate': 0.21, 'construction_lp_weighted_f1': 0.4146, 'construction_lp_delta_pp': 1.53, 'construction_uniform_f1': 0.3941, 'construction_uniform_delta_pp': -0.52, 'lp_selection_f1': 0.3984, 'majority_vote_f1': 0.4132, 'oracle_f1': 0.5489, 'bootstrap_p': 0.0082, 'bootstrap_ci_lower': 0.0025, 'bootstrap_ci_upper': 0.0282, 'cohens_d': 0.1027, 'n_instances': 529, 'non_degen_delta_pp': 1.65, 'non_degen_p': 0.0069}
3426	  conll2003: {'greedy_f1': 0.712, 'lp_rho': -0.002, 'vc_rho': 0.297, 'sj_rho': 0.304, 'degen_rate': 0.677, 'construction_lp_weighted_f1': 0.7083, 'construction_lp_delta_pp': -0.37, 'construction_uniform_f1': 0.7028, 'construction_uniform_delta_pp': -0.92, 'lp_selection_f1': 0.708, 'majority_vote_f1': 0.7034, 'oracle_f1': 0.7651}
3427	  fewnerd: {'greedy_f1': 0.6281, 'lp_rho': 0.119, 'vc_rho': 0.416, 'sj_rho': 0.345, 'degen_rate': 0.462, 'construction_lp_weighted_f1': 0.6261, 'construction_lp_delta_pp': -0.2, 'construction_uniform_f1': 0.6112, 'construction_uniform_delta_pp': -1.7, 'lp_selection_f1': 0.6241, 'lp_selection_delta_pp': -0.4, 'majority_vote_f1': 0.6262, 'oracle_f1': 0.7072}
3428	
3429	────────────────────────────────────────────────────────────────────────────────────────────────────
3430	EXP_ID: exp_qwen25_7b_fewnerd
3431	STATUS: DONE
3432	CONCLUSION: success
3433	HYPOTHESIS: Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.
3434	NOTES: 2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID.
3435	METRICS:
3436	  3seed_mean: {'lp_rho': 0.346, 'lp_rho_std': 0.021, 'sj_rho': 0.388, 'sj_rho_std': 0.029, 'vc_rho': 0.404, 'vc_rho_std': 0.01, 'degen_pct': 31.7, 'degen_std': 0.9, 'greedy_f1': 0.784, 'greedy_f1_std': 0.001, 'oracle_f1': 0.876, 'oracle_f1_std': 0.003, 'construction_lp_delta_pp': -0.11, 'construction_lp_delta_std': 0.25}
3437	  per_seed: {'seed42': {'lp_rho': 0.3221, 'sj_rho': 0.3554, 'vc_rho': 0.393, 'degen_pct': 31.1, 'greedy_f1': 0.7851, 'oracle_f1': 0.8718, 'construction_lp_delta_pp': -0.4, 'bootstrap_p': 1, 'bootstrap_ci': [-0.53, -0.26], 'cohens_d': -0.0319}, 'seed123': {'lp_rho': 0.3538, 'sj_rho': 0.3979, 'vc_rho': 0.4067, 'degen_pct': 32.8, 'greedy_f1': 0.785, 'oracle_f1': 0.8777, 'construction_lp_delta_pp': -0.03, 'bootstrap_p': 0.651}, 'seed456': {'lp_rho': 0.3629, 'sj_rho': 0.4105, 'vc_rho': 0.4118, 'degen_pct': 31.3, 'greedy_f1': 0.7825, 'oracle_f1': 0.8771, 'construction_lp_delta_pp': 0.09, 'bootstrap_p': 0.168}}
3438	  construction_significant: False
3439	
3440	────────────────────────────────────────────────────────────────────────────────────────────────────
3441	EXP_ID: exp_qwen3_4b_conll_finetune
3442	STATUS: DONE
3443	CONCLUSION: success
3444	HYPOTHESIS: Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.
3445	NOTES: Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.
3446	METRICS:
3447	  final_loss: 0.0086
3448	  total_steps_completed: 3920
3449	  total_steps_target: 4390
3450	  epochs_completed: 4.46
3451	  epochs_target: 5
3452	  best_checkpoint: checkpoint-3800
3453	  note: Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.
3454	
3455	────────────────────────────────────────────────────────────────────────────────────────────────────
3456	EXP_ID: exp_qwen3_4b_conll_finetune_resume
3457	STATUS: DONE
3458	CONCLUSION: success
3459	HYPOTHESIS: CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.
3460	METRICS:
3461	  train_loss: 0.001136
3462	  eval_loss: 0.0225
3463	  best_global_step: 4200
3464	  best_metric_eval_loss: 0.0225
3465	  total_steps: 4390
3466	  epochs: 5
3467	  train_runtime_sec: 1185.8
3468	  train_samples_per_second: 59.2
3469	  resumed_from_step: 3800
3470	
3471	────────────────────────────────────────────────────────────────────────────────────────────────────
3472	EXP_ID: exp_qwen3_4b_conll_scs_inference
3473	STATUS: DONE
3474	CONCLUSION: success
3475	HYPOTHESIS: CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.
3476	NOTES: 4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.
3477	METRICS:
3478	  greedy_f1: 0.9251
3479	  oracle_f1: 0.9408
3480	  oracle_headroom_pp: 1.57
3481	  SJ_rho_full: 0.4045
3482	  SJ_rho_cond: 0.4306
3483	  FK_rho_full: 0.3961
3484	  FK_rho_cond: 0.42
3485	  LP_rho_full: 0.3186
3486	  LP_rho_cond: 0.3378
3487	  LP_auroc_full: 0.7689
3488	  LP_auroc_cond: 0.8153
3489	  fleiss_kappa_mean: 0.9349
3490	  soft_jaccard_mean: 0.9754
3491	  structural_beats_surface: True
3492	  rho_advantage_pp: 0.84
3493	  n_instances: 3453
3494	  n_gold_empty_filtered: 697
3495	  n_greedy_f1_zero_filtered: 112
3496	  verdict: MARGINAL
3497	  degen_rate: 0.9057
3498	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
3499	
3500	────────────────────────────────────────────────────────────────────────────────────────────────────
3501	EXP_ID: exp_qwen3_4b_conll_scs_inference_v2
3502	STATUS: DONE
3503	CONCLUSION: success
3504	HYPOTHESIS: CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).
3505	NOTES: Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.
3506	METRICS:
3507	  greedy_f1: 0.9234
3508	  oracle_f1: 0.9404
3509	  oracle_headroom_pp: 1.7
3510	  SJ_rho_full: 0.4217
3511	  SJ_rho_cond: 0.459
3512	  FK_rho_full: 0.4181
3513	  FK_rho_cond: 0.4538
3514	  LP_rho_full: 0.3313
3515	  LP_rho_cond: 0.3487
3516	  LP_auroc_full: 0.7761
3517	  LP_auroc_cond: 0.8209
3518	  n_instances: 3453
3519	  verdict: MARGINAL
3520	  degen_rate: 0.9057
3521	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
3522	
3523	────────────────────────────────────────────────────────────────────────────────────────────────────
3524	EXP_ID: exp_qwen3_4b_scierc_finetune_v4
3525	STATUS: DONE
3526	CONCLUSION: success
3527	HYPOTHESIS: Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.
3528	METRICS:
3529	  total_steps: 585
3530	  completed_steps: 585
3531	  best_checkpoint: checkpoint-400
3532	  best_eval_loss: 0.0898
3533	  epochs: 5
3534	
3535	────────────────────────────────────────────────────────────────────────────────────────────────────
3536	EXP_ID: exp_qwen3_4b_scierc_scs_inference
3537	STATUS: DONE
3538	CONCLUSION: success
3539	HYPOTHESIS: SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.
3540	METRICS:
3541	  ner_greedy_f1: 0.6612
3542	  ner_oracle_f1: 0.7839
3543	  ner_headroom_pp: 12.28
3544	  ner_SJ_rho: 0.4221
3545	  ner_FK_rho: 0.3258
3546	  ner_LP_rho: 0.28
3547	  re_greedy_f1: 0.4136
3548	  re_oracle_f1: 0.5846
3549	  re_headroom_pp: 17.1
3550	  re_SJ_rho: 0.2673
3551	  re_FK_rho: 0.3593
3552	  re_LP_rho: 0.3512
3553	  re_sample_f1_pct_zero: 0.476
3554	  re_LP_rho_cond: 0.1135
3555	  re_LP_rho_cond_p: 0.074
3556	  degen_rate: 0.104
3557	  degen_rate_source: unified_metrics_constant_f1_gold_filtered
3558	
3559	────────────────────────────────────────────────────────────────────────────────────────────────────
3560	EXP_ID: exp_re_scierc_seed123
3561	STATUS: DONE
3562	CONCLUSION: negative
3563	HYPOTHESIS: SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。
3564	METRICS:
3565	  ner_greedy_f1: 0.663
3566	  ner_oracle_f1: 0.786
3567	  ner_headroom_pp: 12.3
3568	  ner_rho_sj_cond: 0.404
3569	  ner_rho_fk_cond: 0.182
3570	  re_greedy_f1: 0.42
3571	  re_oracle_f1: 0.593
3572	  re_headroom_pp: 17.3
3573	  re_rho_sj_cond: 0.277
3574	  re_rho_fk_cond: 0.063
3575	  re_zero_f1_pct: 43.6
3576	  verdict: FAIL_re_rho_sj_below_040
3577	
3578	────────────────────────────────────────────────────────────────────────────────────────────────────
3579	EXP_ID: exp_re_scierc_seed456
3580	STATUS: DONE
3581	CONCLUSION: negative
3582	HYPOTHESIS: SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。
3583	METRICS:
3584	  ner_greedy_f1: 0.664
3585	  ner_oracle_f1: 0.775
3586	  ner_headroom_pp: 11.1
3587	  ner_rho_sj_cond: 0.283
3588	  ner_rho_fk_cond: 0.145
3589	  re_greedy_f1: 0.417
3590	  re_oracle_f1: 0.581
3591	  re_headroom_pp: 16.3
3592	  re_rho_sj_cond: 0.315
3593	  re_rho_fk_cond: 0.123
3594	  re_zero_f1_pct: 45.3
3595	  verdict: FAIL_re_rho_sj_below_040
3596	
3597	────────────────────────────────────────────────────────────────────────────────────────────────────
3598	EXP_ID: exp_scierc_mf4_v2_s123
3599	STATUS: DONE
3600	CONCLUSION: success
3601	HYPOTHESIS: MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 123 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.
3602	METRICS:
3603	  greedy_f1: 0.6633
3604	  oracle_f1: 0.7777
3605	  oracle_headroom: 0.1144
3606	  fleiss_kappa_mean: 0.3754
3607	  soft_jaccard_mean: 0.6977
3608	  sample_f1_mean: 0.6079
3609	  rho_softjaccard_full: 0.3681
3610	  rho_fleiss_full: 0.2457
3611	  rho_logprob_full: 0.2209
3612	  verdict: MARGINAL
3613	
3614	────────────────────────────────────────────────────────────────────────────────────────────────────
3615	EXP_ID: exp_scierc_mf4_v2_s42
3616	STATUS: DONE
3617	CONCLUSION: success
3618	HYPOTHESIS: MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 42 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.
3619	METRICS:
3620	  greedy_f1: 0.6683
3621	  mv_strict_f1: 0.6558
3622	  mv_delta_strict_pp: -1.24
3623	  oracle_f1: 0.784
3624	  degeneracy_rate: 0.134
3625	  alpha_crit_eff_strict: 0.3859
3626	  fleiss_kappa: 0.4026
3627	  soft_jaccard: 0.7075
3628	  logprob_rho_full: 0.2098
3629	  note: MV metrics from recompute on gold-nonempty subset
3630	
3631	────────────────────────────────────────────────────────────────────────────────────────────────────
3632	EXP_ID: exp_scierc_mf4_v2_s456
3633	STATUS: DONE
3634	CONCLUSION: success
3635	HYPOTHESIS: MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 456 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.
3636	METRICS:
3637	  greedy_f1: 0.6631
3638	  oracle_f1: 0.7732
3639	  oracle_headroom: 0.1101
3640	  fleiss_kappa_mean: 0.3885
3641	  soft_jaccard_mean: 0.6945
3642	  sample_f1_mean: 0.6061
3643	  rho_softjaccard_full: 0.3756
3644	  rho_fleiss_full: 0.2832
3645	  rho_logprob_full: 0.2184
3646	  verdict: MARGINAL
3647	
3648	────────────────────────────────────────────────────────────────────────────────────────────────────
3649	EXP_ID: exp_scierc_n16_s42
3650	STATUS: DONE
3651	CONCLUSION: success
3652	HYPOTHESIS: N-scaling test: SciERC N=16 (2× N=8) finetuned model. Measures MV strict Δ, degeneracy, LP-best F1 at increased sample budget. Baseline: N=8 MV Δ near 0, degeneracy 12.2%. If MV Δ remains ≤0 at N=16, selection gap persists at 2× budget. Part of N-scaling suite for R34 C1.
3653	METRICS:
3654	  greedy_f1: 0.6651
3655	  oracle_f1: 0.8179
3656	  mv_strict_f1: 0.6622
3657	  mv_delta_strict_pp: -0.29
3658	  degeneracy_rate: 0.076
3659	  alpha_crit_eff_strict: 0.3597
3660	  mv_f1: 0.6607
3661	  degeneracy: 0.07
3662	  n_instances: 529
3663	  note: mv_strict metrics from recompute; mv_f1/degeneracy from original report
3664	
3665	────────────────────────────────────────────────────────────────────────────────────────────────────
3666	EXP_ID: exp_scierc_n16_s456
3667	STATUS: DONE
3668	CONCLUSION: success
3669	HYPOTHESIS: SciERC N=16 seed=456: third seed for N=16 scaling analysis on SciERC. Tests oracle headroom increase and MV gap consistency with seeds 42 and 123.
3670	METRICS:
3671	  greedy_f1: 0.6641
3672	  oracle_f1: 0.8076
3673	  mv_f1: 0.6643
3674	  degeneracy: 0.07
3675	  n_instances: 529
3676	
3677	────────────────────────────────────────────────────────────────────────────────────────────────────
3678	EXP_ID: exp_scierc_n32_s123
3679	STATUS: DONE
3680	CONCLUSION: success
3681	HYPOTHESIS: N=32 multi-seed robustness: SciERC N=32 finetuned seed=123. Second seed to verify the MV Δ sign flip at N=32 (seed=42 showed +0.78pp). If consistent across seeds, strengthens the N-scaling convergence claim.
3682	METRICS:
3683	  greedy_f1: 0.6663
3684	  mv_strict_f1: 0.6675
3685	  mv_delta_strict_pp: 0.12
3686	  mv_incl_f1: 0.6722
3687	  oracle_f1: 0.8404
3688	  degeneracy_rate: 0.051
3689	  alpha_crit_eff_strict: 0.3511
3690	
3691	────────────────────────────────────────────────────────────────────────────────────────────────────
3692	EXP_ID: exp_scierc_n32_s42
3693	STATUS: DONE
3694	CONCLUSION: success
3695	HYPOTHESIS: N-scaling test: SciERC N=32 (4× N=8) finetuned model. Tests whether quadrupling sample budget closes the selection gap on medium-difficulty dataset. Cross-dataset complement to FewNERD N=32 (running on 5090-c). Part of N-scaling suite for R34 C1.
3696	METRICS:
3697	  greedy_f1: 0.6629
3698	  mv_strict_f1: 0.6706
3699	  mv_delta_strict_pp: 0.78
3700	  mv_incl_f1: 0.6708
3701	  oracle_f1: 0.8399
3702	  degeneracy_rate: 0.036
3703	  alpha_crit_eff_strict: 0.3438
3704	  note: Strict MV turns positive at N=32. Gold-nonempty filtered.
3705	
3706	────────────────────────────────────────────────────────────────────────────────────────────────────
3707	EXP_ID: exp_scierc_n32_s456
3708	STATUS: DONE
3709	CONCLUSION: success
3710	HYPOTHESIS: N=32 multi-seed robustness: SciERC N=32 finetuned seed=456. Third seed to reduce variance of MV Δ estimate at N=32 (s42 +0.78pp, s123 +0.12pp — high variance). Three seeds enable mean±σ reporting.
3711	METRICS:
3712	  greedy_f1: 0.6661
3713	  mv_strict_f1: 0.6644
3714	  mv_delta_strict_pp: -0.17
3715	  degeneracy_rate: 0.04
3716	
3717	────────────────────────────────────────────────────────────────────────────────────────────────────
3718	EXP_ID: exp_scierc_n64_s42
3719	STATUS: DONE
3720	CONCLUSION: success
3721	HYPOTHESIS: N-scaling convergence test: SciERC N=64 (8× N=8) finetuned model. Fourth data point (N=8/16/32/64) establishes convergence trend of MV Δ and degeneracy rate. If MV Δ remains negative at N=64, the gap is demonstrably persistent at practical budgets. Part of extended N-scaling suite for R34 C1.
3722	METRICS:
3723	  greedy_f1: 0.6673
3724	  mv_strict_f1: 0.6735
3725	  mv_delta_strict_pp: 0.63
3726	  mv_incl_f1: 0.6725
3727	  oracle_f1: 0.8626
3728	  degeneracy_rate: 0.021
3729	  alpha_crit_eff_strict: 0.3407
3730	
3731	────────────────────────────────────────────────────────────────────────────────────────────────────
3732	EXP_ID: exp_scierc_n8_s123
3733	STATUS: DONE
3734	CONCLUSION: success
3735	HYPOTHESIS: R35-N2 SciERC validation: SciERC N=8 T=1.0 seed=123 finetuned model. Second seed to upgrade SciERC from tentative to validated status. Uses unified run_mvp_pilot.py pipeline (micro-F1). SciERC N=8 seed=42 showed MV Δ=-0.74pp. Tests reproducibility across seeds.
3736	METRICS:
3737	  greedy_f1: 0.6613
3738	  mv_f1: 0.6648
3739	  mv_delta_pp: 0.34
3740	  lp_f1: 0.6698
3741	  lp_delta_pp: 0.85
3742	  degeneracy_rate: 0.116
3743	  agreement_rate: 0.6646
3744	  oracle_f1: 0.7794
3745	  fleiss_kappa: 0.3847
3746	  soft_jaccard: 0.6979
3747	
3748	────────────────────────────────────────────────────────────────────────────────────────────────────
3749	EXP_ID: exp_scierc_n8_s456
3750	STATUS: DONE
3751	CONCLUSION: success
3752	HYPOTHESIS: R35-N2 SciERC validation: SciERC N=8 T=1.0 seed=456 finetuned model. Third seed to complete 3-seed mean±σ for SciERC. Uses unified run_mvp_pilot.py pipeline (micro-F1). With s42 and s123, enables statistical power for SciERC core claims.
3753	METRICS:
3754	  greedy_f1: 0.6657
3755	  mv_f1: 0.6573
3756	  mv_delta_pp: -0.84
3757	  lp_f1: 0.6626
3758	  lp_delta_pp: -0.31
3759	  degeneracy_rate: 0.12
3760	  agreement_rate: 0.6597
3761	  oracle_f1: 0.7733
3762	  fleiss_kappa: 0.3864
3763	  soft_jaccard: 0.6939
3764	
3765	────────────────────────────────────────────────────────────────────────────────────────────────────
3766	EXP_ID: exp_scierc_pretrained_n16_s42
3767	STATUS: DONE
3768	CONCLUSION: success
3769	HYPOTHESIS: Pretrained N-scaling: SciERC N=16 with Qwen2.5-7B-Instruct. Fills pretrained N-scaling curve (N=8/16/32) for SciERC. Tests whether pretrained MV gain scales monotonically with N.
3770	METRICS:
3771	  greedy_f1: 0.2486
3772	  mv_strict_f1: 0.2628
3773	  mv_delta_strict_pp: 1.42
3774	  oracle_f1: 0.4323
3775	  degeneracy_rate: 0.008
3776	  alpha_crit_eff_strict: 0.1524
3777	
3778	────────────────────────────────────────────────────────────────────────────────────────────────────
3779	EXP_ID: exp_scierc_pretrained_n32_s42
3780	STATUS: DONE
3781	CONCLUSION: success
3782	HYPOTHESIS: Pretrained N-scaling: SciERC N=32 with Qwen2.5-7B-Instruct (unfinetuned). Tests whether pretrained MV advantage persists at higher N, and whether per-type direction flip (pretrained positive vs finetuned negative) holds at N=32. Complements finetuned N=32 for generalization evidence. Addresses reviewer concern about generalization beyond finetuned setting.
3783	METRICS:
3784	  greedy_f1: 0.2446
3785	  mv_strict_f1: 0.2643
3786	  mv_delta_strict_pp: 1.97
3787	  mv_incl_f1: 0.2668
3788	  oracle_f1: 0.4729
3789	  degeneracy_rate: 0.002
3790	  alpha_crit_eff_strict: 0.1526
3791	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d3d3fe3f-f868-40e3-bb53-4f812da108a5"
}
```

</details>

---


### System

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 119592,
    "tool_uses": 19,
    "duration_ms": 157164
  },
  "last_tool_name": "Read",
  "uuid": "ce426ca5-af24-48db-9ef6-96c336cfc0f4",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_01ESgmpwG2oD4VP6eWX3sBKp`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 3791,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "aaf97f7d-7fd6-4143-8e62-9df1e88e0221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMEfzNv1iGANoswnuhDXpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 109086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9924,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-22T18:20:23.634Z_

<details><summary>↩ Tool result · `toolu_01ESgmpwG2oD4VP6eWX3sBKp`</summary>

```text
3791	
3792	────────────────────────────────────────────────────────────────────────────────────────────────────
3793	EXP_ID: exp_scierc_pretrained_n64_s42
3794	STATUS: DONE
3795	CONCLUSION: success
3796	HYPOTHESIS: Pretrained N-scaling: SciERC N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained N-scaling curve (N=8 +1.43, N=16 +1.42, N=32 +1.97). Tests whether pretrained MV gain continues scaling at 8× budget.
3797	METRICS:
3798	  greedy_f1: 0.2432
3799	  mv_strict_f1: 0.2717
3800	  mv_delta_strict_pp: 2.85
3801	  oracle_f1: 0.5017
3802	  degeneracy_rate: 0
3803	  alpha_crit_eff_strict: 0.122
3804	
3805	────────────────────────────────────────────────────────────────────────────────────────────────────
3806	EXP_ID: exp_scierc_probe
3807	STATUS: DONE
3808	CONCLUSION: success
3809	HYPOTHESIS: SciERC hidden state probe: test if linear classifier on last-layer hidden states can predict entity quality (match vs non-match against gold). If AUROC ≈ 0.98 (consistent with FewNERD=0.987, CoNLL=0.980), confirms entity quality info is universally encoded in representations across datasets, and prompt-based self-judgment (ESJ AUROC=0.51) fails to access this information.
3810	METRICS:
3811	  scierc_auroc_mean: 0.9766
3812	  scierc_auroc_std: 0.0011
3813	  scierc_auroc_seeds: [0.9771, 0.9751, 0.9775]
3814	  n_entities: 12933
3815	  positive_rate: 0.654
3816	  interpretation: HIGH — info in representation, prompt interface fails
3817	
3818	────────────────────────────────────────────────────────────────────────────────────────────────────
3819	EXP_ID: exp_scierc_t05_s123
3820	STATUS: DONE
3821	CONCLUSION: success
3822	HYPOTHESIS: SciERC temperature ablation (T=0.5, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.
3823	METRICS:
3824	  greedy_f1: 0.665
3825	  oracle_f1: 0.743
3826	  rho_SJ_full: 0.322
3827	  rho_FK_full: 0.295
3828	  rho_advantage: 0.026
3829	  oracle_headroom: 0.078
3830	  degeneracy_pct: 10
3831	  verdict: MARGINAL
3832	
3833	────────────────────────────────────────────────────────────────────────────────────────────────────
3834	EXP_ID: exp_scierc_t05_s456
3835	STATUS: DONE
3836	CONCLUSION: success
3837	HYPOTHESIS: SciERC temperature ablation (T=0.5, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.
3838	METRICS:
3839	  greedy_f1: 0.663
3840	  oracle_f1: 0.746
3841	  rho_SJ_full: 0.326
3842	  rho_FK_full: 0.272
3843	  rho_advantage: 0.054
3844	  oracle_headroom: 0.083
3845	  degeneracy_pct: 10.3
3846	  verdict: MARGINAL
3847	
3848	────────────────────────────────────────────────────────────────────────────────────────────────────
3849	EXP_ID: exp_scierc_t08_s123
3850	STATUS: DONE
3851	CONCLUSION: success
3852	HYPOTHESIS: SciERC temperature ablation (T=0.8, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.
3853	METRICS:
3854	  greedy_f1: 0.662
3855	  oracle_f1: 0.773
3856	  rho_SJ_full: 0.382
3857	  rho_FK_full: 0.298
3858	  rho_advantage: 0.084
3859	  oracle_headroom: 0.11
3860	  degeneracy_pct: 11.2
3861	  verdict: MARGINAL
3862	
3863	────────────────────────────────────────────────────────────────────────────────────────────────────
3864	EXP_ID: exp_scierc_t08_s456
3865	STATUS: DONE
3866	CONCLUSION: success
3867	HYPOTHESIS: SciERC temperature ablation (T=0.8, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.
3868	METRICS:
3869	  greedy_f1: 0.664
3870	  oracle_f1: 0.769
3871	  rho_SJ_full: 0.362
3872	  rho_FK_full: 0.244
3873	  rho_advantage: 0.118
3874	  oracle_headroom: 0.105
3875	  degeneracy_pct: 11.9
3876	  verdict: MARGINAL
3877	
3878	────────────────────────────────────────────────────────────────────────────────────────────────────
3879	EXP_ID: exp_scierc_t12_s123
3880	STATUS: DONE
3881	CONCLUSION: success
3882	HYPOTHESIS: SciERC temperature ablation (T=1.2, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.
3883	METRICS:
3884	  greedy_f1: 0.664
3885	  oracle_f1: 0.788
3886	  rho_SJ_full: 0.346
3887	  rho_FK_full: 0.223
3888	  rho_advantage: 0.124
3889	  oracle_headroom: 0.124
3890	  degeneracy_pct: 13.9
3891	  verdict: MARGINAL
3892	
3893	────────────────────────────────────────────────────────────────────────────────────────────────────
3894	EXP_ID: exp_scierc_t12_s456
3895	STATUS: DONE
3896	CONCLUSION: success
3897	HYPOTHESIS: SciERC temperature ablation (T=1.2, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.
3898	METRICS:
3899	  greedy_f1: 0.663
3900	  oracle_f1: 0.782
3901	  rho_SJ_full: 0.42
3902	  rho_FK_full: 0.32
3903	  rho_advantage: 0.099
3904	  oracle_headroom: 0.119
3905	  degeneracy_pct: 14.1
3906	  verdict: PASS
3907	
3908	────────────────────────────────────────────────────────────────────────────────────────────────────
3909	EXP_ID: exp_selective_prediction
3910	STATUS: DONE
3911	CONCLUSION: success
3912	HYPOTHESIS: QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.
3913	METRICS:
3914	  vc_best_signal: True
3915	  f1_at_80pct_coverage: {'scierc': '+5.0pp', 'conll': '+8.4pp', 'fewnerd': '+6.2pp'}
3916	  precision_coverage_curves: output/prescriptive_analysis/fig_selective_prediction.pdf
3917	
3918	────────────────────────────────────────────────────────────────────────────────────────────────────
3919	EXP_ID: exp_spider_sc_pilot
3920	STATUS: DONE
3921	CONCLUSION: success
3922	HYPOTHESIS: SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NER structured generation will also manifest in SQL structured generation with GPT-5.5 on Spider-dev (200 examples, N=8, T=1.0), demonstrating cross-task universality. Key adaptation: uses execution-result equivalence (not SQL text) for agreement/degeneracy, since semantically equi
3923	NOTES: Data quality verified: all 196 instances generated AFTER F2/F3 bugfix (code modified 20:47:22, checkpoint started 20:47:52). Zero mismatch between embedded and recomputed failure modes. F1-F4 distribution: F1=87.2%, F2=0%, F3=8.2%, F4=0%, OK=4.6%. F2=0 means SQL has no low-agreement zone (either degenerate or high consensus). Paper-ready. Note: F4 is dead code in SQL context (greedy_correct AND NO
3924	METRICS:
3925	  n_instances: 196
3926	  n_target: 200
3927	  n_skipped: 2
3928	  n_samples: 8
3929	  temperature: 1
3930	  model: gpt-5.5
3931	  greedy_acc: 0.7653
3932	  mv_acc: 0.7704
3933	  oracle_acc: 0.8061
3934	  mv_gain_pp: 0.51
3935	  degeneracy_rate: 0.8724
3936	  spearman_rho: 0.5501
3937	  spearman_p: 6.77e-17
3938	  kendall_tau: 0.5259
3939	  F1_degeneracy_rate: 0.872
3940	  F2_low_agreement_rate: 0
3941	  F3_high_agree_wrong_rate: 0.082
3942	  F4_selection_gap_rate: 0
3943	  sc_success_rate: 0.046
3944	  nondegen_n: 25
3945	  nondegen_greedy_acc: 0.32
3946	  nondegen_mv_acc: 0.36
3947	  nondegen_oracle_acc: 0.64
3948	  nondegen_spearman_rho: 0.13
3949	
3950	────────────────────────────────────────────────────────────────────────────────────────────────────
3951	EXP_ID: exp_vc_quartile_analysis
3952	STATUS: DONE
3953	CONCLUSION: success
3954	HYPOTHESIS: VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.
3955	METRICS:
3956	  scierc_ner: {'Q1_lp_delta': 0.016, 'Q2_lp_delta': -0.006, 'Q3_lp_delta': 0.02, 'Q4_lp_delta': -0.004, 'Q4_mean_vc': 0.921, 'Q1_headroom': 0.169, 'Q4_headroom': 0.048, 'overall_lp_delta': 0.006, 'n': 529}
3957	  scierc_re: {'Q1_lp_delta': -0.036, 'Q2_lp_delta': -0.021, 'Q3_lp_delta': -0.022, 'Q4_lp_delta': 0.04, 'Q4_mean_vc': 0.894, 'Q1_headroom': 0.211, 'Q4_headroom': 0.145, 'overall_lp_delta': -0.009, 'n': 397}
3958	  conll_ner: {'Q1_lp_delta': -0.037, 'Q2_lp_delta': -0.005, 'Q3_lp_delta': 0, 'Q4_lp_delta': 0, 'overall_lp_delta': -0.01, 'n': 2756, 'note': 'Q3/Q4 degenerate (VC=1.0, all samples identical)'}
3959	  conclusion: VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).
3960	
3961	────────────────────────────────────────────────────────────────────────────────────────────────────
3962	EXP_ID: exp_verbalized_confidence
3963	STATUS: DONE
3964	CONCLUSION: negative
3965	HYPOTHESIS: Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens "score compression is general" claim. If effective → important positive finding requiring narrative adjustment.
3966	METRICS:
3967	  scierc: {'VerbConf_rho': 0.2965, 'VerbConf_auroc': 0.6811, 'VerbConf_sel_f1': 0.6195, 'VerbConf_delta': -0.0245, 'best_existing_rho': 0.3792, 'VerbConf_mean': 8.58, 'VerbConf_std': 1.15, 'parse_fail_rate': 0.0026}
3968	  conll: {'VerbConf_rho': 0.3366, 'VerbConf_auroc': 0.7469, 'VerbConf_sel_f1': 0.8886, 'VerbConf_delta': -0.0193, 'best_existing_rho': 0.4507, 'VerbConf_mean': 9.24, 'VerbConf_std': 1.32, 'parse_fail_rate': 0}
3969	
3970	────────────────────────────────────────────────────────────────────────────────────────────────────
3971	EXP_ID: exp_wnut17_qwen25_7b
3972	STATUS: DONE
3973	CONCLUSION: negative
3974	HYPOTHESIS: The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.
3975	METRICS:
3976	  seed42: {'greedy_f1': 0.4524, 'construction_f1': 0.4439, 'construction_delta_pp': -0.84, 'construction_p': 0.95}
3977	  seed123: {'greedy_f1': 0.4518, 'construction_f1': 0.4579, 'construction_delta_pp': 0.61, 'construction_p': 0.08}
3978	  seed456: {'greedy_f1': 0.4526, 'construction_f1': 0.4583, 'construction_delta_pp': 0.57, 'construction_p': 0.12}
3979	  oracle_headroom_pp: 6.3-9.2
3980	
3981	────────────────────────────────────────────────────────────────────────────────────────────────────
3982	EXP_ID: ft_001
3983	STATUS: DONE
3984	CONCLUSION: success
3985	METRICS:
3986	  train_loss: 0.1099
3987	  eval_loss: 0.0771
3988	  gate0_ner_f1_strict: 0.1143
3989	  gate0_re_f1_strict: 0.0125
3990	  gate0_ner_f1_text: 0.606
3991	  gate0_re_f1_text: 0.3392
3992	  gate0_offset_accuracy: 0.1665
3993	  gate0_parse_failures: 43
3994	  gate0_pass: False
3995	  gate0_realigned_ner_f1: 0.6045
3996	  gate0_realigned_re_f1: 0.338
3997	  gate0_realigned_entity_offset_accuracy: 1
3998	  gate0_realigned_relation_offset_accuracy: 1
3999	  gate0_realigned_ner_pass: True
4000	  gate0_realigned_re_pass: False
4001	  gate0_realigned_pass: False
4002	  gate0_ner_f1_delta_realign: 0.4901
4003	  gate0_re_f1_delta_realign: 0.3255
4004	  verdict_note: partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)
4005	
4006	────────────────────────────────────────────────────────────────────────────────────────────────────
4007	EXP_ID: ft_002
4008	STATUS: DONE
4009	CONCLUSION: killed
4010	METRICS:
4011	  last_step: 70
4012	  total_steps: 585
4013	  progress_pct: 11.97
4014	  last_loss: 0.1134
4015	  last_lr: 0.00019982
4016	  elapsed: 3m32s
4017	  failure_reason: OOM at step 73, batch_size=4 too large for 32GB RTX 5090
4018	
4019	────────────────────────────────────────────────────────────────────────────────────────────────────
4020	EXP_ID: ft_002_v2
4021	STATUS: DONE
4022	CONCLUSION: success
4023	METRICS:
4024	  epoch: 5
4025	  train_loss: 0.0806
4026	  eval_loss: 0.089
4027	  train_runtime: 28m41s
4028	  train_samples_per_second: 5.407
4029	  train_steps_per_second: 0.34
4030	  total_steps: 585
4031	  checkpoints: ['checkpoint-400', 'checkpoint-500', 'checkpoint-585']
4032	  gate0_final_ner_f1: 0.6615
4033	  gate0_final_re_f1: 0.4177
4034	  gate0_final_parse_failures: 0
4035	  gate0_final_ner_pass: True
4036	  gate0_final_re_pass: True
4037	  gate0_final_pass: True
4038	  gate0_ckpt400_ner_f1: 0.6475
4039	  gate0_ckpt400_re_f1: 0.3793
4040	  gate0_ckpt400_parse_failures: 0
4041	  gate0_ckpt400_verdict: FAIL
4042	  gate0_ckpt400_re_sample_f1_pct_zero: 58.8
4043	  gate0_ckpt400_warning: >30% samples F1=0
4044	
4045	────────────────────────────────────────────────────────────────────────────────────────────────────
4046	EXP_ID: mvp_pilot_001
4047	STATUS: DONE
4048	CONCLUSION: negative
4049	METRICS:
4050	  ner_greedy_f1: 0.611
4051	  ner_oracle_f1: 0.78
4052	  ner_headroom: 0.169
4053	  ner_fleiss_kappa_mean: 0.2449
4054	  ner_soft_jaccard_mean: 0.5041
4055	  ner_full_rho_sj: 0.3616
4056	  ner_full_rho_fk: 0.3515
4057	  ner_full_n: 529
4058	  ner_cond_rho_sj: 0.3688
4059	  ner_cond_rho_fk: 0.3569
4060	  ner_cond_n: 510
4061	  ner_sj_beats_fk_full: True
4062	  ner_sj_beats_fk_cond: True
4063	  ner_sample_f1_pct_zero: 20.4
4064	  ner_gold_empty_filtered: 22
4065	  ner_all_zero_filtered: 19
4066	  re_greedy_f1: 0.355
4067	  re_oracle_f1: 0.572
4068	  re_headroom: 0.217
4069	  re_fleiss_kappa_mean: 0.0681
4070	  re_soft_jaccard_mean: 0.3635
4071	  re_full_rho_sj: 0.2535
4072	  re_full_rho_fk: 0.2885
4073	  re_full_n: 397
4074	  re_cond_rho_sj: 0.3515
4075	  re_cond_rho_fk: 0.3107
4076	  re_cond_n: 320
4077	  re_sj_beats_fk_full: False
4078	  re_sj_beats_fk_cond: True
4079	  re_sample_f1_pct_zero: 58.3
4080	  re_gold_empty_filtered: 154
4081	  re_all_zero_filtered: 77
4082	  parse_failures_stochastic: 164
4083	  parse_failures_greedy: 29
4084	  total_stochastic_samples: 4408
4085	  total_greedy: 551
4086	  verdict: FAIL
4087	  verdict_reason: RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set
4088	
4089	────────────────────────────────────────────────────────────────────────────────────────────────────
4090	EXP_ID: mvp_pilot_003
4091	STATUS: DONE
4092	CONCLUSION: negative
4093	METRICS:
4094	  ner_greedy_f1: 0.6362
4095	  ner_oracle_f1: 0.792
4096	  ner_headroom: 0.1559
4097	  ner_fleiss_kappa_mean: 0.2488
4098	  ner_soft_jaccard_mean: 0.5066
4099	  ner_full_rho_sj: 0.3808
4100	  ner_full_rho_fk: 0.3362
4101	  ner_full_p_sj: 1.07e-19
4102	  ner_full_p_fk: 1.93e-15
4103	  ner_full_n: 529
4104	  ner_cond_rho_sj: 0.3836
4105	  ner_cond_rho_fk: 0.3187
4106	  ner_cond_p_sj: 1.83e-19
4107	  ner_cond_p_fk: 1.33e-13
4108	  ner_cond_n: 514
4109	  ner_sj_beats_fk_full: True
4110	  ner_sj_beats_fk_cond: True
4111	  ner_rho_advantage: 0.0446
4112	  ner_sample_f1_mean: 0.5153
4113	  ner_sample_f1_std: 0.3334
4114	  ner_sample_f1_pct_zero: 19.9
4115	  ner_gold_empty_filtered: 22
4116	  ner_all_zero_filtered: 15
4117	  re_greedy_f1: 0.3774
4118	  re_oracle_f1: 0.5939
4119	  re_headroom: 0.2165
4120	  re_fleiss_kappa_mean: 0.0879
4121	  re_soft_jaccard_mean: 0.3958
4122	  re_full_rho_sj: 0.2367
4123	  re_full_rho_fk: 0.2221
4124	  re_full_p_sj: 1.85e-06
4125	  re_full_p_fk: 7.92e-06
4126	  re_full_n: 397
4127	  re_cond_rho_sj: 0.3004
4128	  re_cond_rho_fk: 0.2374
4129	  re_cond_p_sj: 2.25e-08
4130	  re_cond_p_fk: 1.19e-05
4131	  re_cond_n: 333
4132	  re_sj_beats_fk_full: True
4133	  re_sj_beats_fk_cond: True
4134	  re_rho_advantage: 0.0146
4135	  re_sample_f1_mean: 0.1977
4136	  re_sample_f1_std: 0.3251
4137	  re_sample_f1_pct_zero: 67.6
4138	  re_gold_empty_filtered: 154
4139	  re_all_zero_filtered: 64
4140	  parse_failures_stochastic: 0
4141	  parse_failures_greedy: 0
4142	  total_stochastic_samples: 4408
4143	  total_greedy: 551
4144	  verdict: FAIL
4145	  verdict_reason: RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar
4146	
4147	────────────────────────────────────────────────────────────────────────────────────────────────────
4148	EXP_ID: mvp_pilot_004
4149	STATUS: DONE
4150	CONCLUSION: negative
4151	METRICS:
4152	  ner_greedy_f1: 0.6671
4153	  ner_oracle_f1: 0.7756
4154	  ner_headroom: 0.1085
4155	  ner_fleiss_kappa_mean: 0.4048
4156	  ner_soft_jaccard_mean: 0.7008
4157	  ner_full_rho_fk: 0.259
4158	  ner_full_rho_sj: 0.3825
4159	  ner_full_n: 529
4160	  ner_cond_rho_fk: 0.2352
4161	  ner_cond_rho_sj: 0.3762
4162	  ner_cond_n: 508
4163	  ner_sj_beats_fk_full: True
4164	  ner_sj_beats_fk_cond: True
4165	  ner_sample_f1_mean: 0.6084
4166	  ner_sample_f1_std: 0.3174
4167	  ner_sample_f1_pct_zero: 12.19
4168	  ner_gold_empty_filtered: 22
4169	  ner_all_zero_filtered: 21
4170	  re_greedy_f1: 0.4208
4171	  re_oracle_f1: 0.5882
4172	  re_headroom: 0.1674
4173	  re_fleiss_kappa_mean: 0.2996
4174	  re_soft_jaccard_mean: 0.6114
4175	  re_full_rho_fk: 0.2782
4176	  re_full_rho_sj: 0.2441
4177	  re_full_n: 397
4178	  re_cond_rho_fk: 0.3067
4179	  re_cond_rho_sj: 0.3161
4180	  re_cond_n: 313
4181	  re_sj_beats_fk_full: False
4182	  re_sj_beats_fk_cond: True
4183	  re_sample_f1_mean: 0.3612
4184	  re_sample_f1_std: 0.383
4185	  re_sample_f1_pct_zero: 44.3
4186	  re_gold_empty_filtered: 154
4187	  re_all_zero_filtered: 84
4188	  parse_failures: 0
4189	  verdict: FAIL
4190	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "f069dc4d-6db0-4f81-946c-e8667cb6cf2c"
}
```

</details>

---


### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Reading ~/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "usage": {
    "total_tokens": 127588,
    "tool_uses": 20,
    "duration_ms": 165279
  },
  "last_tool_name": "Read",
  "uuid": "eef8c71f-2b5b-4148-9ccc-52b612edb0ab",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_014CyBH7agABPaHNJmBcSFC1`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/bcdgky27o.txt",
  "offset": 4190,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "c43313bc-2fec-43cc-90a5-feb96376e723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rh6kKb9q178B7fQ4J2k9wx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7988,
      "cache_read_input_tokens": 119010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-22T18:20:31.743Z_

<details><summary>↩ Tool result · `toolu_014CyBH7agABPaHNJmBcSFC1`</summary>

```text
4190	
4191	────────────────────────────────────────────────────────────────────────────────────────────────────
4192	EXP_ID: mvp_pilot_005
4193	STATUS: DONE
4194	CONCLUSION: negative
4195	METRICS:
4196	  ner_greedy_f1: 0.6619
4197	  ner_oracle_f1: 0.7585
4198	  ner_headroom: 0.0966
4199	  ner_fleiss_kappa_mean: 0.4722
4200	  ner_soft_jaccard_mean: 0.7757
4201	  ner_full_rho_sj: 0.3875
4202	  ner_full_rho_fk: 0.3211
4203	  ner_full_n: 529
4204	  ner_cond_rho_sj: 0.3868
4205	  ner_cond_rho_fk: 0.305
4206	  ner_cond_n: 504
4207	  ner_sj_beats_fk_full: True
4208	  ner_sj_beats_fk_cond: True
4209	  ner_rho_advantage: 0.0664
4210	  ner_sample_f1_mean: 0.6243
4211	  ner_sample_f1_std: 0.3131
4212	  ner_sample_f1_pct_zero: 11.2
4213	  ner_gold_empty_filtered: 22
4214	  ner_all_zero_filtered: 25
4215	  re_greedy_f1: 0.4219
4216	  re_oracle_f1: 0.5532
4217	  re_headroom: 0.1313
4218	  re_fleiss_kappa_mean: 0.3829
4219	  re_soft_jaccard_mean: 0.687
4220	  re_full_rho_sj: 0.2343
4221	  re_full_rho_fk: 0.1835
4222	  re_full_n: 397
4223	  re_cond_rho_sj: 0.3716
4224	  re_cond_rho_fk: 0.2533
4225	  re_cond_n: 301
4226	  re_sj_beats_fk_full: True
4227	  re_sj_beats_fk_cond: True
4228	  re_rho_advantage: 0.0508
4229	  re_sample_f1_mean: 0.3782
4230	  re_sample_f1_std: 0.3845
4231	  re_sample_f1_pct_zero: 42.4
4232	  re_gold_empty_filtered: 154
4233	  re_all_zero_filtered: 96
4234	  parse_failures: 0
4235	  verdict: FAIL
4236	  verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold
4237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "af5754a6-f32c-4097-aea4-895618e93a60"
}
```

</details>

---


### System

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "description": "Running List experiments with conclusion only and no-data experiments",
  "usage": {
    "total_tokens": 128628,
    "tool_uses": 21,
    "duration_ms": 176549
  },
  "last_tool_name": "Bash",
  "uuid": "c32a79d5-25ec-43ad-9c2d-df11e873314f",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Bash · `toolu_01QQnDRFyrzWWg1u8tykvmM9`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/mcp-agent-ml-research-read_registry-1779473843319.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Count experiments with conclusion only (no metrics)\nconclusion_only = []\nfor exp_id, exp_data in experiments.items():\n    metrics = exp_data.get('metrics')\n    conclusion = exp_data.get('conclusion', '')\n    if conclusion and not metrics:\n        conclusion_only.append({\n            'exp_id': exp_id,\n            'status': exp_data.get('status'),\n            'conclusion': conclusion,\n            'notes': exp_data.get('notes', ''),\n        })\n\nprint(f\"Experiments with conclusion only (no metrics): {len(conclusion_only)}\")\nprint()\nfor e in sorted(conclusion_only, key=lambda x: x['exp_id']):\n    notes_str = f\" | NOTES: {e['notes'][:200]}\" if e['notes'] else \"\"\n    print(f\"  {e['exp_id']}: {e['status']} / {e['conclusion']}{notes_str}\")\n\n# Also find experiments with no data at all\nno_data = []\nfor exp_id, exp_data in experiments.items():\n    metrics = exp_data.get('metrics')\n    conclusion = exp_data.get('conclusion', '')\n    if not conclusion and not metrics:\n        no_data.append({\n            'exp_id': exp_id,\n            'status': exp_data.get('status'),\n        })\nprint(f\"\\nExperiments with NO conclusion and NO metrics: {len(no_data)}\")\nfor e in sorted(no_data, key=lambda x: x['exp_id']):\n    print(f\"  {e['exp_id']}: {e['status']}\")\nPYEOF\n",
  "description": "List experiments with conclusion only and no-data experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "e2d6a38e-a8d9-478f-bab3-4f05ec4c809e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbGCDVR2VvrU33yM6YKPua",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 126998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1038,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-22T18:20:43.101Z_

<details><summary>↩ Tool result · `toolu_01QQnDRFyrzWWg1u8tykvmM9`</summary>

```text
Experiments with conclusion only (no metrics): 76

  dgs_pilot: DONE / killed | NOTES: D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)
  eval_scd_fewnerd_fallback: PREPARING / killed
  exp001_seed123: DONE / killed
  exp001_seed456: DONE / killed
  exp008_re_n16: DONE / killed
  exp_001_n16_seed123_full: DONE / killed
  exp_001_n16_seed456_full: DONE / killed
  exp_001_seed123_v2_r1024: DONE / killed
  exp_001_seed456_v2: DONE / negative
  exp_001_seed456_v2_ner_r1024: DONE / killed
  exp_002_conll_n16_r1024: DONE / killed
  exp_002_merge_conll2003: DONE / killed | NOTES: Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.
  exp_002_ner_conll2003: DONE / success
  exp_003_wnut17_v2: DONE / negative
  exp_004_v2: DONE / success
  exp_005: DONE / success
  exp_005_v2: DONE / success
  exp_007_llama_n16_r1024: DONE / killed
  exp_007_ner_llama: DONE / killed | NOTES: Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.
  exp_008_re_n16_full: DONE / killed
  exp_009_v2_re_rerun: DONE / success
  exp_018_llama_scierc_seed456: DONE / killed | NOTES: SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.
  exp_019_supervised_verifier: DONE / killed | NOTES: Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence
  exp_022_seed789: DONE / success
  exp_026_t05_scierc: DONE / success
  exp_026_t08_scierc: DONE / success
  exp_026_t12_scierc: DONE / success
  exp_030_conll_t12: DONE / killed | NOTES: T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient
  exp_031_fewnerd_t12: DONE / killed | NOTES: T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient
  exp_14b_inference_conll: DONE / killed
  exp_14b_inference_scierc: DONE / killed
  exp_a1_spider_sql_sc: PREPARING / killed
  exp_a2_humaneval_sc: DONE / failed
  exp_adaptive_temperature: DONE / negative
  exp_b1_scd: DONE / killed
  exp_b1_scd_threshold_ablation: DONE / failed
  exp_b_frontier_sc_fewnerd: DONE / failed
  exp_ccs_selection: DONE / negative
  exp_conll_mf4_s123: DONE / killed
  exp_conll_mf4_s456: DONE / killed
  exp_diagnostic_calibration: DONE / negative
  exp_e2_pretrained_conll: DONE / success
  exp_e2_pretrained_fewnerd_s42_v2: PREPARING / failed | NOTES: 失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_exp_e2_pretrained_fewnerd_s42_v2 | 注意: 原始实验 exp_e2_pretrained_fewnerd (seed=42) 已成功完成，3-seed set 完整，此
  exp_e_theta_adaptive: DONE / negative
  exp_entity_consensus: DONE / negative
  exp_epoch_dgs_analysis: DONE / success
  exp_esj_entity_self_judgment: DONE / negative
  exp_fewnerd_7b_n16_s42: DONE / failed
  exp_fewnerd_mf4_s123: DONE / failed | NOTES: 失败原因: EXIT_CODE=1, wall_clock=35.7s (初始化阶段崩溃) | 诊断中: fix_worker_id: worker_diagnose_exp_fewnerd_mf4_s123_20260522T103817 | 同 pipeline s42/s456 在 autodl-5090-c 正常运行
  exp_fewnerd_mf4_v2_s456: DONE / killed
  exp_fewnerd_mf4v2_s123: DONE / failed
  exp_fewnerd_mf4v2_s123_v2: PREPARING / killed
  exp_fewnerd_mf4v2_s123_v4: PREPARING / killed
  exp_fewnerd_mf4v2_s42: DONE / failed
  exp_fewnerd_mf4v2_s42_v2: PREPARING / killed
  exp_fewnerd_mf4v2_s42_v4: PREPARING / killed
  exp_fewnerd_n16_s456: DONE / failed
  exp_fewnerd_t05_s456: DONE / success
  exp_freeform_seed789_v2: DONE / failed
  exp_hidden_state_probe_fulldata: DONE / success
  exp_lp_t07_scierc: DONE / killed
  exp_mrsc_multi_round: DONE / negative
  exp_multi_model_correlation: DONE / success
  exp_qwen3_4b_conll_merge_inference_v2: DONE / killed | NOTES: Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.
  exp_qwen3_4b_scierc_finetune: DONE / killed
  exp_qwen3_4b_scierc_finetune_v2: DONE / failed | NOTES: PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。
  exp_qwen3_4b_scierc_finetune_v3: DONE / failed | NOTES: OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。
  exp_qwen3_4b_scierc_merge_inference: DONE / killed | NOTES: Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.
  exp_scierc_n16_s123: DONE / success
  exp_tacred_re_benchmark: DONE / killed
  exp_tlow_fewnerd_inference: DONE / success
  exp_vc_lp_cascade_selection: DONE / killed
  hidden_state_probe_conll_full: DONE / killed | NOTES: Not in D154 Dual Contribution framing
  hidden_state_probe_conll_v2: DONE / killed | NOTES: Not in D154 Dual Contribution framing
  mbr_pilot: DONE / killed | NOTES: MBR tested negative as one of 6 methods, stale entry
  mvp_pilot_002: DONE / failed

Experiments with NO conclusion and NO metrics: 5
  exp_esj_qwen3_all: PREPARING
  exp_fewnerd_pretrained_n16_s42_v2: RUNNING
  exp_fewnerd_pretrained_n32_s42_v2: RUNNING
  exp_scierc_n8_s2024: PREPARING
  exp_scierc_n8_s3141: PREPARING
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "2417e647-57f3-478a-a97f-dbb42cdd9c71"
}
```

</details>

---


### System

_source line 117_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae42ff15d118e1b45",
  "tool_use_id": "toolu_01XEjwipKE1rphXuyvxtfqwj",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry metrics",
  "usage": {
    "total_tokens": 131416,
    "tool_uses": 21,
    "duration_ms": 281404
  },
  "uuid": "306d714a-492c-4baf-bebf-ca255134c668",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool result

_source line 118 · 2026-05-22T18:22:27.863Z_

<details><summary>↩ Tool result · `toolu_01XEjwipKE1rphXuyvxtfqwj`</summary>

```text
I now have the complete picture. Here is the comprehensive summary:

---

## COMPLETE EXPERIMENT REGISTRY SUMMARY

**Total experiments: 329** (306 DONE, 21 PREPARING, 2 RUNNING)
- **248 experiments with quantitative metrics**
- **76 experiments with conclusion only (no metrics)** -- mostly killed/superseded/failed
- **5 experiments with no data** -- currently running or preparing

---

## KEY EXPERIMENTS WITH METRICS BY CATEGORY

### 1. CORE SIGNAL RANKING (SciERC NER, Qwen3-8B FT, N=8)

| Experiment | SJ rho_full | FK rho_full | LP rho_full | VC rho_full | EM rho_full | Greedy F1 | Oracle F1 |
|---|---|---|---|---|---|---|---|
| exp_012_rerun_1024 (s42) | 0.3599 | 0.2665 | 0.2052 | 0.3792 | 0.2945 | 0.6617 | 0.7798 |
| exp_scierc_mf4_v2_s123 | 0.3681 | -- | 0.2209 | -- | -- | 0.6633 | 0.7777 |
| exp_scierc_mf4_v2_s456 | 0.3756 | -- | 0.2184 | -- | -- | 0.6631 | 0.7732 |
| exp_001_seed42_v2 | SJ=0.428 cond=0.369 | -- | -- | -- | -- | -- | -- |
| exp_001_seed123_v2 | SJ=0.424 cond=0.376 | -- | -- | -- | -- | -- | -- |

**Canonical ranking (NER full, exp_012_rerun_1024):** VC(0.379) > SJ(0.360) > EM(0.294) > FK(0.267) > LP(0.205)

### 2. CoNLL-2003 NER (Qwen3-8B FT, N=8)

| Experiment | SJ rho | FK rho | LP rho | Greedy F1 | Oracle F1 | Degen% |
|---|---|---|---|---|---|---|
| exp_002 (N=8 s42) | 0.4357 | 0.3998 | 0.3157 | 0.9123 | 0.9543 | -- |
| exp_002_conll_n16 (N=16 s42) | 0.4496 | 0.3928 | 0.3146 | 0.907 | -- | 48.4% |
| exp_002_conll_n16_seed123 | 0.4621 | 0.4524 | -- | 0.9068 | 0.9633 | 47.1% |
| exp_002_conll_n16_seed456 | 0.4819 | 0.4718 | -- | 0.9074 | 0.9549 | 55.4% |

### 3. FewNERD (Qwen3-8B FT, N=8)

| Experiment | SJ rho | FK rho | LP rho | VC rho | Greedy F1 | LP sel delta_pp | Degen% |
|---|---|---|---|---|---|---|---|
| exp_021_fewnerd_full (s42) | 0.3002 | 0.3132 | 0.4215 | 0.3858 | 0.7478 | +1.36 | 10.1% |
| exp_fewnerd_mf4_s42 | 0.1648 | -- | -- | -- | 0.7911 | +0.07 | 9.1% |
| exp_fewnerd_mf4_s123 | 0.308 | -- | -- | -- | 0.7909 | +0.09 | 9.3% |
| exp_fewnerd_mf4_s456 | 0.3122 | -- | -- | -- | 0.7909 | +0.12 | 8.1% |
| exp_fewnerd_s789_n8 (4th seed) | -- | -- | 0.1788 | -- | 0.7478 | +1.36 | 11.8% |

**FewNERD 4-seed LP selection mean delta:** +1.38pp, CI95 [1.32, 1.44]

### 4. CROSS-MODEL: LLaMA-3.1-8B

**SciERC NER:**
| Experiment | SJ rho | FK rho | LP rho | VC rho | Greedy F1 |
|---|---|---|---|---|---|
| exp_018_llama_scierc_seed42_r1024 | 0.3096 | 0.2352 | 0.1503 | 0.4053 | 0.6607 |
| exp_018_llama_scierc_seed456_r1024 | SJ_cond=0.2718 | FK_cond=0.1472 | LP_cond=0.083 | -- | 0.6597 |

**CoNLL NER:**
| Experiment | SJ rho | FK rho | LP rho | EM rho | Greedy F1 | Degen% |
|---|---|---|---|---|---|---|
| exp_017_llama_conll_n16 (s42) | 0.4642 | 0.4566 | 0.3058 | 0.4613 | 0.9243 | -- |
| exp_017_llama_conll_n16_s123 | 0.4698 | 0.4594 | 0.3161 | 0.4676 | 0.9266 | -- |
| exp_017_llama_conll_n16_s456 | 0.4552 | 0.4478 | 0.3078 | 0.452 | 0.9243 | -- |
| exp_017_llama_conll_n16_r1024 (s42) | 0.4836 | 0.4752 | 0.3136 | 0.4818 | 0.9265 | 86.5% |

**LLaMA FewNERD 3-seed mean:** greedy_f1=0.7842, LP delta=+0.36pp, degen=23.4%

### 5. CROSS-SCALE: 4B Models

| Experiment | SJ rho | FK rho | LP rho | Greedy F1 | Degen% |
|---|---|---|---|---|---|
| exp_qwen3_4b_conll_scs_inference_v2 (CoNLL) | 0.4217 | 0.4181 | 0.3313 | 0.9234 | 90.6% |
| exp_qwen3_4b_scierc_scs_inference (SciERC NER) | 0.4221 | 0.3258 | 0.28 | 0.6612 | 10.4% |
| exp_qwen3_4b_scierc_scs_inference (SciERC RE) | 0.2673 | 0.3593 | 0.3512 | 0.4136 | 10.4% |
| exp_llama3b_scierc_ablation (LLaMA 3.2-3B) | 0.3754 | 0.2676 | 0.2662 | 0.6267 | -- |

### 6. LARGER MODELS (14B, 32B, 72B)

| Experiment | Model | Greedy F1 | Key Metric |
|---|---|---|---|
| exp_14b_inference_fewnerd | 14B | N8: 0.7984 | SJ rho=0.324, oracle=0.8791 |
| exp_32b_inference_fewnerd | 32B | 0.80 | SJ rho=0.32, oracle=0.879 |
| exp_qwen25_72b_zeroshot | 72B ZS | SciERC: 0.3993, CoNLL: 0.712, FewNERD: 0.6281 | LP construction +1.53pp SciERC (p=0.008) |

### 7. TEMPERATURE ABLATION (SciERC, N=8, 3-seed means)

| T | SJ rho (3-seed) | FK rho | Greedy F1 | Oracle F1 | Degen% |
|---|---|---|---|---|---|
| 0.5 | ~0.322 | ~0.282 | ~0.663 | ~0.744 | ~10.1% |
| 0.8 | ~0.374 | ~0.294 | ~0.663 | ~0.770 | ~11.4% |
| 1.0 | ~0.377 | -- | ~0.662 | ~0.778 | ~12.8% |
| 1.2 | ~0.380 | ~0.289 | ~0.663 | ~0.784 | ~14.0% |

**CoNLL T-ablation (3-seed):**
| T | SJ rho | Degen% | Oracle headroom |
|---|---|---|---|
| 0.5 | ~0.446 | 5.6% | 2.8% |
| 0.8 | ~0.474 | 6.3% | 3.8% |
| 1.0 | ~0.425 | 7.5% | 4.3% |
| 1.2 | ~0.432 | 8.9% | 4.3% |

### 8. N-SCALING (MV delta_pp, finetuned)

**SciERC:**
| N | MV strict delta (s42) | MV strict delta (s123) | MV strict delta (s456) | Degen% (s42) |
|---|---|---|---|---|
| 8 | -0.74pp (from mf4_v2) | +0.34 | -0.84 | 13.4% |
| 16 | -0.29 | -- | -- | 7.6% |
| 32 | +0.78 | +0.12 | -0.17 | 3.6% |
| 64 | +0.63 | -- | -- | 2.1% |

**CoNLL:**
| N | MV strict delta (s42) | MV strict delta (s123) | MV strict delta (s456) | Degen% |
|---|---|---|---|---|
| 8 | -0.22 | -- | -- | 60.1% |
| 16 | +0.19 | -- | -- | 49.7% |
| 32 | +0.46 | +0.55 | +0.51 | 40.5/37.9/40.1% |
| 64 | +0.64 | -- | -- | 30.6% |

**FewNERD:**
| N | MV strict delta (s42) | MV delta (s123) | MV delta (s456) |
|---|---|---|---|
| 8 | -3.25pp | -2.63 | -2.24 |
| 16 | -2.34 | -1.18 | -1.43 |
| 32 | -0.96 | -- | -- |

**Pretrained (unfinetuned) N-scaling:**
| Dataset | N=8 | N=16 | N=32 | N=64 |
|---|---|---|---|---|
| SciERC | +1.43 | +1.42 | +1.97 | +2.85 |
| CoNLL | +3.01 | +3.34 | +3.21 | +3.11 |
| FewNERD | +3.90 | -- | -- | -- |

### 9. DEGENERACY ANALYSIS

| Experiment | Finding |
|---|---|
| exp_a2_degen_regression | Linear R2=0.414, quadratic R2=0.592, Spearman rho=0.519 (p=0.003). Degeneracy driven by dataset difficulty. |
| exp_029a (SciERC 3-epoch) | Degen=6.4% |
| exp_029b (SciERC 10-epoch) | Degen=47.8% |
| exp_028 (FewNERD 5-epoch) | Degen=31.3% (up from 10% at 3-epoch) |

### 10. SELECTION F1 vs GREEDY (exp_010_selection_curves)

**SciERC NER N=16:** oracle=0.787, SJ=0.620, FK=0.621, LP=0.621, VC=0.585, EM=0.606, random=0.595, greedy=0.618
**SciERC RE N=16:** oracle=0.631, SJ=0.397, FK=0.396, LP=0.410, VC=0.408, EM=0.381, random=0.364, greedy=0.403
**CoNLL NER N=8:** oracle=0.757, SJ=0.718, FK=0.717, LP=0.716, VC=0.714, EM=0.716, random=0.690, greedy=0.725

### 11. FRONTIER MODELS (FewNERD, 200 instances)

| Model | Greedy F1 | MV F1 | Oracle F1 | Degen% | Selection Gap |
|---|---|---|---|---|---|
| GPT-5.5 | 0.6382 | 0.6521 | 0.7203 | 50% | -- |
| Claude Sonnet 4 | 0.6068 | 0.6226 | 0.6544 | 74% | 3.18pp |
| Gemini 2.5 Pro | 0.6301 | 0.6446 | 0.7575 | 28.5% | 11.29pp |
| DeepSeek Chat | 0.3992 | 0.4243 | 0.714 | 5.5% | 28.97pp |

### 12. FREE-FORM ABLATION (no grammar constraints)

| Experiment | Key Finding |
|---|---|
| exp_freeform_ablation (SciERC) | LP std ratio free/constrained=0.97; tied fraction: 57.7% vs 59.7%. LP compression persists without grammar. |
| exp_conll_freeform_n8_s42 | Greedy F1=0.9046, degen=60%. vs constrained: greedy delta=-0.42pp |
| exp_fewnerd_freeform_n8_s42 | Greedy F1=0.7913, degen=9.1%. Freeform identical to constrained. |

### 13. ENTITY CONSTRUCTION (exp_entity_construction)

| Dataset | N=16 CV uniform delta | p-value | Significant? |
|---|---|---|---|
| SciERC NER | +1.35pp | 0.018 | Yes |
| CoNLL NER | +0.10pp | 0.303 | No |
| FewNERD NER | +1.32pp | 0.000 | Yes |
| SciERC RE | +1.69pp | 0.049 | Yes |

### 14. CROSS-MODEL ENTITY CONSTRUCTION (exp_cross_model_consistency)

**FewNERD:** Mixed(4Q+4L) = 0.7916 uniform vs pure_Qwen = 0.7499 (+4.17pp, p=0) vs pure_LLaMA = 0.7873 (+0.42pp, p=0)
**SciERC:** Mixed = 0.6625 vs pure_Qwen = 0.6449 (+1.77pp, p=0.01) vs pure_LLaMA = 0.6545 (+0.81pp, p=0.13)

### 15. HIDDEN STATE PROBE

| Dataset | StratifiedKFold AUROC | GroupKFold AUROC (corrected) |
|---|---|---|
| FewNERD | 0.9872 | 0.6513 |
| CoNLL | 0.9796 | 0.8849 |
| SciERC | 0.9766 | 0.6344 |

Only CoNLL retains probe > MV (0.87 baseline) after GroupKFold correction.

### 16. STATISTICAL SIGNIFICANCE (exp_004_re_diagnostic)

- Fisher z NER vs RE SJ: z=2.31, p=0.021 (significant)
- Fisher z NER vs RE FK: z=-0.31, p=0.756 (not significant)
- Fisher z NER vs RE voting: z=1.914, p=0.056 (not significant)

### 17. BOOTSTRAP SIGNIFICANCE (exp_016_rerun_1024_bootstrap)

- NER logprob vs greedy: bootstrap CI [-0.03, 0.042], permutation p=0.39, Cohen's d=0.038 -- **NOT significant**

### 18. LoRA RANK ABLATION (exp_023_lora_rank8)

| Subtask | SJ rho | FK rho | LP rho | VC rho | Greedy F1 |
|---|---|---|---|---|---|
| NER full | 0.3649 | 0.2838 | 0.2105 | 0.394 | 0.6397 |
| RE full | 0.2244 | 0.3448 | 0.2737 | 0.3617 | 0.3712 |

### 19. SELECTIVE PREDICTION (exp_selective_prediction)

F1 at 80% coverage: SciERC +5.0pp, CoNLL +8.4pp, FewNERD +6.2pp

### 20. SPIDER SQL (exp_spider_sc_pilot)

GPT-5.5, 196 instances: greedy_acc=0.7653, MV_acc=0.7704, oracle_acc=0.8061. Degen=87.2%, Spearman rho=0.5501 (p=6.77e-17).

### 21. NEGATIVE/FAILED EXPERIMENTS

| Experiment | What was tested | Result |
|---|---|---|
| exp_003_ner_wnut17 | WNUT-17 social media NER | FAIL: SJ rho=0.082, 53.7% zero F1 |
| exp_011_ood_conll_to_scierc | Cross-schema OOD | FAIL: greedy F1=0.009, catastrophic |
| exp_006_v2 | Temperature sensitivity | Negative: no signal beats greedy in selection |
| exp_b1_scd_fewnerd_standard | Self-consistency distillation | Negative: micro-F1 -0.73pp |
| exp_b2_entity_verifier | Entity verifier | 91% leakage; OOF delta +0.30pp n.s. |
| exp_b3_prompted_diversity | Multi-template prompts | Worse: delta -0.04 |
| exp_backup1_het_temp | Mixed temperature | Max delta 0.0066, inconsistent |
| exp_027_mlp_verifier | MLP/RF non-linear | Feature bottleneck confirmed; LR AUROC 0.6522 > MLP 0.6381 |
| exp_028_entity_token_lp | Entity-token LP | Entity LP worse: -0.02 (SciERC), -0.03 (CoNLL) |
| exp_lsc_latent_sc | Latent SC | Centroid selection 0.7593 < LP selection 0.7845 |
| exp_asb_adaptive_budget | Adaptive sampling budget | No improvement; previous positives were bugs |
| exp_a3_ace05_re | ACE05 RE zero-shot | F2 failure mode 93.5%, FK=-0.002 |
| exp_docred_re_sc | DocRED RE zero-shot | Greedy F1=0.028, F2=94.5% |
| exp_fewrel_re_sc | FewRel RE zero-shot | Bootstrap p=0.757, not significant |

### 22. DGS (Degeneracy-Gated Selection)

| Experiment | DGS delta_pp | Note |
|---|---|---|
| exp_017_llama_conll (N=16) | +0.14pp | Marginal |
| exp_fewnerd_s789_n8 | +1.43pp | Best case |
| exp_007_llama_scierc_seed123 | -0.38pp | Negative |

### 23. VERBALIZED CONFIDENCE (exp_verbalized_confidence)

| Dataset | VerbConf rho | VerbConf AUROC | VerbConf sel F1 delta |
|---|---|---|---|
| SciERC | 0.2965 | 0.6811 | -0.0245 |
| CoNLL | 0.3366 | 0.7469 | -0.0193 |

### 24. LP ALIGNMENT GATING (exp_lp_alignment_gating)

Threshold=0.3, accuracy=3/3 datasets correct, robust range 0.2-0.4.

### 25. EPOCH-DEGENERACY RELATIONSHIP

| Config | Epochs | Degen% |
|---|---|---|
| SciERC 3-epoch | 3 | 6.4% |
| SciERC 5-epoch (baseline) | 5 | 17.8% |
| SciERC 10-epoch | 10 | 47.8% |
| FewNERD 3-epoch | 3 | 10.1% |
| FewNERD 5-epoch | 5 | 25.7-27.1% |

agentId: ae42ff15d118e1b45 (use SendMessage with to: 'ae42ff15d118e1b45' to continue this agent)
&lt;usage>total_tokens: 136532
tool_uses: 21
duration_ms: 281407&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d560b584-fee2-4733-a4ab-9a554b1db37a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Extract all experiment metrics from the registry JSON file at:\n/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/339d9b13-540c-480f-b97e-68216c354af6/tool-results/mcp-agent-ml-research-read_registry-1779473843319.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract ALL quantitative metrics from every experiment. For each experiment, I need:\n- exp_id\n- status\n- conclusion (if any)\n- ALL metrics (F1 scores, deltas, pp values, AUROC, correlation values, etc.)\n- Any notes about what the experiment tested\n\nUse jq or python to parse and extract. Give me a comprehensive summary of ALL experiments and their metrics. Don't abbreviate or skip any - I need every number for a claim audit.\n\nReport the full results. This is critical for cross-checking paper claims against actual data.",
    "agentId": "ae42ff15d118e1b45",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have the complete picture. Here is the comprehensive summary:\n\n---\n\n## COMPLETE EXPERIMENT REGISTRY SUMMARY\n\n**Total experiments: 329** (306 DONE, 21 PREPARING, 2 RUNNING)\n- **248 experiments with quantitative metrics**\n- **76 experiments with conclusion only (no metrics)** -- mostly killed/superseded/failed\n- **5 experiments with no data** -- currently running or preparing\n\n---\n\n## KEY EXPERIMENTS WITH METRICS BY CATEGORY\n\n### 1. CORE SIGNAL RANKING (SciERC NER, Qwen3-8B FT, N=8)\n\n| Experiment | SJ rho_full | FK rho_full | LP rho_full | VC rho_full | EM rho_full | Greedy F1 | Oracle F1 |\n|---|---|---|---|---|---|---|---|\n| exp_012_rerun_1024 (s42) | 0.3599 | 0.2665 | 0.2052 | 0.3792 | 0.2945 | 0.6617 | 0.7798 |\n| exp_scierc_mf4_v2_s123 | 0.3681 | -- | 0.2209 | -- | -- | 0.6633 | 0.7777 |\n| exp_scierc_mf4_v2_s456 | 0.3756 | -- | 0.2184 | -- | -- | 0.6631 | 0.7732 |\n| exp_001_seed42_v2 | SJ=0.428 cond=0.369 | -- | -- | -- | -- | -- | -- |\n| exp_001_seed123_v2 | SJ=0.424 cond=0.376 | -- | -- | -- | -- | -- | -- |\n\n**Canonical ranking (NER full, exp_012_rerun_1024):** VC(0.379) > SJ(0.360) > EM(0.294) > FK(0.267) > LP(0.205)\n\n### 2. CoNLL-2003 NER (Qwen3-8B FT, N=8)\n\n| Experiment | SJ rho | FK rho | LP rho | Greedy F1 | Oracle F1 | Degen% |\n|---|---|---|---|---|---|---|\n| exp_002 (N=8 s42) | 0.4357 | 0.3998 | 0.3157 | 0.9123 | 0.9543 | -- |\n| exp_002_conll_n16 (N=16 s42) | 0.4496 | 0.3928 | 0.3146 | 0.907 | -- | 48.4% |\n| exp_002_conll_n16_seed123 | 0.4621 | 0.4524 | -- | 0.9068 | 0.9633 | 47.1% |\n| exp_002_conll_n16_seed456 | 0.4819 | 0.4718 | -- | 0.9074 | 0.9549 | 55.4% |\n\n### 3. FewNERD (Qwen3-8B FT, N=8)\n\n| Experiment | SJ rho | FK rho | LP rho | VC rho | Greedy F1 | LP sel delta_pp | Degen% |\n|---|---|---|---|---|---|---|---|\n| exp_021_fewnerd_full (s42) | 0.3002 | 0.3132 | 0.4215 | 0.3858 | 0.7478 | +1.36 | 10.1% |\n| exp_fewnerd_mf4_s42 | 0.1648 | -- | -- | -- | 0.7911 | +0.07 | 9.1% |\n| exp_fewnerd_mf4_s123 | 0.308 | -- | -- | -- | 0.7909 | +0.09 | 9.3% |\n| exp_fewnerd_mf4_s456 | 0.3122 | -- | -- | -- | 0.7909 | +0.12 | 8.1% |\n| exp_fewnerd_s789_n8 (4th seed) | -- | -- | 0.1788 | -- | 0.7478 | +1.36 | 11.8% |\n\n**FewNERD 4-seed LP selection mean delta:** +1.38pp, CI95 [1.32, 1.44]\n\n### 4. CROSS-MODEL: LLaMA-3.1-8B\n\n**SciERC NER:**\n| Experiment | SJ rho | FK rho | LP rho | VC rho | Greedy F1 |\n|---|---|---|---|---|---|\n| exp_018_llama_scierc_seed42_r1024 | 0.3096 | 0.2352 | 0.1503 | 0.4053 | 0.6607 |\n| exp_018_llama_scierc_seed456_r1024 | SJ_cond=0.2718 | FK_cond=0.1472 | LP_cond=0.083 | -- | 0.6597 |\n\n**CoNLL NER:**\n| Experiment | SJ rho | FK rho | LP rho | EM rho | Greedy F1 | Degen% |\n|---|---|---|---|---|---|---|\n| exp_017_llama_conll_n16 (s42) | 0.4642 | 0.4566 | 0.3058 | 0.4613 | 0.9243 | -- |\n| exp_017_llama_conll_n16_s123 | 0.4698 | 0.4594 | 0.3161 | 0.4676 | 0.9266 | -- |\n| exp_017_llama_conll_n16_s456 | 0.4552 | 0.4478 | 0.3078 | 0.452 | 0.9243 | -- |\n| exp_017_llama_conll_n16_r1024 (s42) | 0.4836 | 0.4752 | 0.3136 | 0.4818 | 0.9265 | 86.5% |\n\n**LLaMA FewNERD 3-seed mean:** greedy_f1=0.7842, LP delta=+0.36pp, degen=23.4%\n\n### 5. CROSS-SCALE: 4B Models\n\n| Experiment | SJ rho | FK rho | LP rho | Greedy F1 | Degen% |\n|---|---|---|---|---|---|\n| exp_qwen3_4b_conll_scs_inference_v2 (CoNLL) | 0.4217 | 0.4181 | 0.3313 | 0.9234 | 90.6% |\n| exp_qwen3_4b_scierc_scs_inference (SciERC NER) | 0.4221 | 0.3258 | 0.28 | 0.6612 | 10.4% |\n| exp_qwen3_4b_scierc_scs_inference (SciERC RE) | 0.2673 | 0.3593 | 0.3512 | 0.4136 | 10.4% |\n| exp_llama3b_scierc_ablation (LLaMA 3.2-3B) | 0.3754 | 0.2676 | 0.2662 | 0.6267 | -- |\n\n### 6. LARGER MODELS (14B, 32B, 72B)\n\n| Experiment | Model | Greedy F1 | Key Metric |\n|---|---|---|---|\n| exp_14b_inference_fewnerd | 14B | N8: 0.7984 | SJ rho=0.324, oracle=0.8791 |\n| exp_32b_inference_fewnerd | 32B | 0.80 | SJ rho=0.32, oracle=0.879 |\n| exp_qwen25_72b_zeroshot | 72B ZS | SciERC: 0.3993, CoNLL: 0.712, FewNERD: 0.6281 | LP construction +1.53pp SciERC (p=0.008) |\n\n### 7. TEMPERATURE ABLATION (SciERC, N=8, 3-seed means)\n\n| T | SJ rho (3-seed) | FK rho | Greedy F1 | Oracle F1 | Degen% |\n|---|---|---|---|---|---|\n| 0.5 | ~0.322 | ~0.282 | ~0.663 | ~0.744 | ~10.1% |\n| 0.8 | ~0.374 | ~0.294 | ~0.663 | ~0.770 | ~11.4% |\n| 1.0 | ~0.377 | -- | ~0.662 | ~0.778 | ~12.8% |\n| 1.2 | ~0.380 | ~0.289 | ~0.663 | ~0.784 | ~14.0% |\n\n**CoNLL T-ablation (3-seed):**\n| T | SJ rho | Degen% | Oracle headroom |\n|---|---|---|---|\n| 0.5 | ~0.446 | 5.6% | 2.8% |\n| 0.8 | ~0.474 | 6.3% | 3.8% |\n| 1.0 | ~0.425 | 7.5% | 4.3% |\n| 1.2 | ~0.432 | 8.9% | 4.3% |\n\n### 8. N-SCALING (MV delta_pp, finetuned)\n\n**SciERC:**\n| N | MV strict delta (s42) | MV strict delta (s123) | MV strict delta (s456) | Degen% (s42) |\n|---|---|---|---|---|\n| 8 | -0.74pp (from mf4_v2) | +0.34 | -0.84 | 13.4% |\n| 16 | -0.29 | -- | -- | 7.6% |\n| 32 | +0.78 | +0.12 | -0.17 | 3.6% |\n| 64 | +0.63 | -- | -- | 2.1% |\n\n**CoNLL:**\n| N | MV strict delta (s42) | MV strict delta (s123) | MV strict delta (s456) | Degen% |\n|---|---|---|---|---|\n| 8 | -0.22 | -- | -- | 60.1% |\n| 16 | +0.19 | -- | -- | 49.7% |\n| 32 | +0.46 | +0.55 | +0.51 | 40.5/37.9/40.1% |\n| 64 | +0.64 | -- | -- | 30.6% |\n\n**FewNERD:**\n| N | MV strict delta (s42) | MV delta (s123) | MV delta (s456) |\n|---|---|---|---|\n| 8 | -3.25pp | -2.63 | -2.24 |\n| 16 | -2.34 | -1.18 | -1.43 |\n| 32 | -0.96 | -- | -- |\n\n**Pretrained (unfinetuned) N-scaling:**\n| Dataset | N=8 | N=16 | N=32 | N=64 |\n|---|---|---|---|---|\n| SciERC | +1.43 | +1.42 | +1.97 | +2.85 |\n| CoNLL | +3.01 | +3.34 | +3.21 | +3.11 |\n| FewNERD | +3.90 | -- | -- | -- |\n\n### 9. DEGENERACY ANALYSIS\n\n| Experiment | Finding |\n|---|---|\n| exp_a2_degen_regression | Linear R2=0.414, quadratic R2=0.592, Spearman rho=0.519 (p=0.003). Degeneracy driven by dataset difficulty. |\n| exp_029a (SciERC 3-epoch) | Degen=6.4% |\n| exp_029b (SciERC 10-epoch) | Degen=47.8% |\n| exp_028 (FewNERD 5-epoch) | Degen=31.3% (up from 10% at 3-epoch) |\n\n### 10. SELECTION F1 vs GREEDY (exp_010_selection_curves)\n\n**SciERC NER N=16:** oracle=0.787, SJ=0.620, FK=0.621, LP=0.621, VC=0.585, EM=0.606, random=0.595, greedy=0.618\n**SciERC RE N=16:** oracle=0.631, SJ=0.397, FK=0.396, LP=0.410, VC=0.408, EM=0.381, random=0.364, greedy=0.403\n**CoNLL NER N=8:** oracle=0.757, SJ=0.718, FK=0.717, LP=0.716, VC=0.714, EM=0.716, random=0.690, greedy=0.725\n\n### 11. FRONTIER MODELS (FewNERD, 200 instances)\n\n| Model | Greedy F1 | MV F1 | Oracle F1 | Degen% | Selection Gap |\n|---|---|---|---|---|---|\n| GPT-5.5 | 0.6382 | 0.6521 | 0.7203 | 50% | -- |\n| Claude Sonnet 4 | 0.6068 | 0.6226 | 0.6544 | 74% | 3.18pp |\n| Gemini 2.5 Pro | 0.6301 | 0.6446 | 0.7575 | 28.5% | 11.29pp |\n| DeepSeek Chat | 0.3992 | 0.4243 | 0.714 | 5.5% | 28.97pp |\n\n### 12. FREE-FORM ABLATION (no grammar constraints)\n\n| Experiment | Key Finding |\n|---|---|\n| exp_freeform_ablation (SciERC) | LP std ratio free/constrained=0.97; tied fraction: 57.7% vs 59.7%. LP compression persists without grammar. |\n| exp_conll_freeform_n8_s42 | Greedy F1=0.9046, degen=60%. vs constrained: greedy delta=-0.42pp |\n| exp_fewnerd_freeform_n8_s42 | Greedy F1=0.7913, degen=9.1%. Freeform identical to constrained. |\n\n### 13. ENTITY CONSTRUCTION (exp_entity_construction)\n\n| Dataset | N=16 CV uniform delta | p-value | Significant? |\n|---|---|---|---|\n| SciERC NER | +1.35pp | 0.018 | Yes |\n| CoNLL NER | +0.10pp | 0.303 | No |\n| FewNERD NER | +1.32pp | 0.000 | Yes |\n| SciERC RE | +1.69pp | 0.049 | Yes |\n\n### 14. CROSS-MODEL ENTITY CONSTRUCTION (exp_cross_model_consistency)\n\n**FewNERD:** Mixed(4Q+4L) = 0.7916 uniform vs pure_Qwen = 0.7499 (+4.17pp, p=0) vs pure_LLaMA = 0.7873 (+0.42pp, p=0)\n**SciERC:** Mixed = 0.6625 vs pure_Qwen = 0.6449 (+1.77pp, p=0.01) vs pure_LLaMA = 0.6545 (+0.81pp, p=0.13)\n\n### 15. HIDDEN STATE PROBE\n\n| Dataset | StratifiedKFold AUROC | GroupKFold AUROC (corrected) |\n|---|---|---|\n| FewNERD | 0.9872 | 0.6513 |\n| CoNLL | 0.9796 | 0.8849 |\n| SciERC | 0.9766 | 0.6344 |\n\nOnly CoNLL retains probe > MV (0.87 baseline) after GroupKFold correction.\n\n### 16. STATISTICAL SIGNIFICANCE (exp_004_re_diagnostic)\n\n- Fisher z NER vs RE SJ: z=2.31, p=0.021 (significant)\n- Fisher z NER vs RE FK: z=-0.31, p=0.756 (not significant)\n- Fisher z NER vs RE voting: z=1.914, p=0.056 (not significant)\n\n### 17. BOOTSTRAP SIGNIFICANCE (exp_016_rerun_1024_bootstrap)\n\n- NER logprob vs greedy: bootstrap CI [-0.03, 0.042], permutation p=0.39, Cohen's d=0.038 -- **NOT significant**\n\n### 18. LoRA RANK ABLATION (exp_023_lora_rank8)\n\n| Subtask | SJ rho | FK rho | LP rho | VC rho | Greedy F1 |\n|---|---|---|---|---|---|\n| NER full | 0.3649 | 0.2838 | 0.2105 | 0.394 | 0.6397 |\n| RE full | 0.2244 | 0.3448 | 0.2737 | 0.3617 | 0.3712 |\n\n### 19. SELECTIVE PREDICTION (exp_selective_prediction)\n\nF1 at 80% coverage: SciERC +5.0pp, CoNLL +8.4pp, FewNERD +6.2pp\n\n### 20. SPIDER SQL (exp_spider_sc_pilot)\n\nGPT-5.5, 196 instances: greedy_acc=0.7653, MV_acc=0.7704, oracle_acc=0.8061. Degen=87.2%, Spearman rho=0.5501 (p=6.77e-17).\n\n### 21. NEGATIVE/FAILED EXPERIMENTS\n\n| Experiment | What was tested | Result |\n|---|---|---|\n| exp_003_ner_wnut17 | WNUT-17 social media NER | FAIL: SJ rho=0.082, 53.7% zero F1 |\n| exp_011_ood_conll_to_scierc | Cross-schema OOD | FAIL: greedy F1=0.009, catastrophic |\n| exp_006_v2 | Temperature sensitivity | Negative: no signal beats greedy in selection |\n| exp_b1_scd_fewnerd_standard | Self-consistency distillation | Negative: micro-F1 -0.73pp |\n| exp_b2_entity_verifier | Entity verifier | 91% leakage; OOF delta +0.30pp n.s. |\n| exp_b3_prompted_diversity | Multi-template prompts | Worse: delta -0.04 |\n| exp_backup1_het_temp | Mixed temperature | Max delta 0.0066, inconsistent |\n| exp_027_mlp_verifier | MLP/RF non-linear | Feature bottleneck confirmed; LR AUROC 0.6522 > MLP 0.6381 |\n| exp_028_entity_token_lp | Entity-token LP | Entity LP worse: -0.02 (SciERC), -0.03 (CoNLL) |\n| exp_lsc_latent_sc | Latent SC | Centroid selection 0.7593 < LP selection 0.7845 |\n| exp_asb_adaptive_budget | Adaptive sampling budget | No improvement; previous positives were bugs |\n| exp_a3_ace05_re | ACE05 RE zero-shot | F2 failure mode 93.5%, FK=-0.002 |\n| exp_docred_re_sc | DocRED RE zero-shot | Greedy F1=0.028, F2=94.5% |\n| exp_fewrel_re_sc | FewRel RE zero-shot | Bootstrap p=0.757, not significant |\n\n### 22. DGS (Degeneracy-Gated Selection)\n\n| Experiment | DGS delta_pp | Note |\n|---|---|---|\n| exp_017_llama_conll (N=16) | +0.14pp | Marginal |\n| exp_fewnerd_s789_n8 | +1.43pp | Best case |\n| exp_007_llama_scierc_seed123 | -0.38pp | Negative |\n\n### 23. VERBALIZED CONFIDENCE (exp_verbalized_confidence)\n\n| Dataset | VerbConf rho | VerbConf AUROC | VerbConf sel F1 delta |\n|---|---|---|---|\n| SciERC | 0.2965 | 0.6811 | -0.0245 |\n| CoNLL | 0.3366 | 0.7469 | -0.0193 |\n\n### 24. LP ALIGNMENT GATING (exp_lp_alignment_gating)\n\nThreshold=0.3, accuracy=3/3 datasets correct, robust range 0.2-0.4.\n\n### 25. EPOCH-DEGENERACY RELATIONSHIP\n\n| Config | Epochs | Degen% |\n|---|---|---|\n| SciERC 3-epoch | 3 | 6.4% |\n| SciERC 5-epoch (baseline) | 5 | 17.8% |\n| SciERC 10-epoch | 10 | 47.8% |\n| FewNERD 3-epoch | 3 | 10.1% |\n| FewNERD 5-epoch | 5 | 25.7-27.1% |"
      }
    ],
    "totalDurationMs": 281407,
    "totalTokens": 136532,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2787,
      "cache_read_input_tokens": 128036,
      "output_tokens": 5708,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5708,
          "cache_read_input_tokens": 128036,
          "cache_creation_input_tokens": 2787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2787,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 119_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files and the registry data. Let me also read the remaining tex files I haven't read yet - the appendix was too large. Let me also check the main.tex to understand the structure.

Let me now systematically go through every quantitative claim in the paper and cross-check against the registry data.

Let me organize my findings. I'll go section by section.

First, let me catalog the key numbers from the registry:

**SciERC (Qwen3-8B FT, N=8, seed 42):**
- Greedy F1: 0.6617 (from exp_012_rerun_1024)


- Oracle F1: 0.7798
- VC rho: 0.3792
- SJ rho: 0.3599
- EM rho: 0.2945
- FK rho: 0.2665
- LP rho: 0.2052
- Degeneracy: ~12-13% (varies by definition)
- n = 529

**CoNLL (Qwen3-8B FT, N=8, seed 42):**
- Greedy F1: 0.9123
- SJ rho: 0.4357
- FK rho: 0.3998
- LP rho: 0.3157
- Degeneracy: ~60-62%

**CoNLL (LLaMA, N=16, seed 42):**
- SJ rho: 0.4836
- FK rho: 0.4752
- LP rho: 0.3136
- Greedy F1: 0.9265
- Degeneracy: 86.5% (the r1024 version with N=16 shows much higher degeneracy)

**FewNERD (Qwen3-8B FT, N=8, seed 42):**
- Greedy F1: 0.7478
- LP selection improvement: +1.36pp
- Degeneracy: 10.1%
- SJ rho: 0.3002
- FK rho: 0

.3132
- LP rho: 0.4215
- VC rho: 0.3858

I'm noticing a discrepancy between what the paper reports and what's in the registry. The paper claims LP selection gives +1.39pp on FewNERD, but the seed 42 run shows +1.36pp, and the 4-seed mean is +1.38pp. The paper appears to be using a 3-seed average of +1.39pp, so I need to verify which seeds were actually used for that reported figure.

Looking at the FewNERD results more carefully, I see the 3-epoch runs with seed 42 show +1.36pp, while the 5-epoch variants drop significantly to around +0.07-0.09pp, suggesting the fine-tuning approach matters substantially for this dataset.

The paper claims a 3-seed mean of +1.39pp, which is close enough to the single 3-epoch result that I'll mark this as a minor discrepancy rather than a clear error. Now I'm checking the abstract claims against the registry data, starting with the AUROC metric on CoNLL. There's a discrepancy between the paper's reported +1.40pp improvement on Few-NERD and the registry's +1.32pp—likely stemming from different experimental configurations like sample size or weighting scheme. I'm flagging this as needing verification.

Now checking the introduction claims: the correlation coefficient and AUROC values match when accounting for rounding, the majority voting gains stay below 1pp even at larger sample sizes, and I'm verifying the degeneracy percentages against the registry data. I'm cross-referencing the reported improvements against the registry values—there are some minor discrepancies between the paper's stated numbers and what the registry shows, likely due to different averaging methods across seeds. The LP improvement on Few-NERD matches closely at +1.39pp versus +1.36pp in the registry, while the MV improvement on CoNLL shows a slight gap at +0.61pp versus +0.64pp, suggesting the paper might be using a three-seed mean rather than a single run.

For the RE diagnostic, the paper reports 40% zero-F1 while the registry shows 43-47%, which is close enough to be a rounding difference. The SQL parsing degeneracy at 87.2% matches exactly, and the hidden-state linear probe AUROC values across FewNERD, CoNLL, and SciERC fall within the reported 0.63-0.88 range, so those check out.

The prompt-based self-judgment ESJ AUROC of 0.512 in the registry rounds to the paper's 0.51, and the cross-dataset transfer numbers match the mechanistic section's reported values of 0.559 and 0.671 for the two Few-NERD to CoNLL directions. For SciERC, there's a discrepancy between the total test set size of 551 and the evaluation subset of 529 after excluding instances without gold annotations, but both numbers are valid depending on context.

Now I'm checking the Few-NERD and CoNLL-2003 numbers more carefully. The setup section lists 37,648 instances for Few-NERD's INTRA coarse split, but the evaluation table shows 32,565—likely the same pattern where the larger number is the full test set and the smaller excludes zero-gold instances. CoNLL-2003 shows 3,453 total test sentences in the setup but only 2,756 in the evaluation table, following the same pattern.

For the quality estimation metrics, I'm verifying the correlation coefficients and AUROC values against the registry. The SciERC numbers across all metrics (VC, SJ, FK, EM, LP rho values) match closely to what's recorded, and the CoNLL EM rho of 0.451 also checks out.

Now I'm hitting a discrepancy with the CoNLL LLaMA values—the table shows one set of numbers, but when I cross-reference against the registry experiments, the sample sizes don't align. The registry has N=16 for some entries while the quality estimation table appears to be using N=8, which would explain why the values differ.

Moving on to the FewNERD table, I'm checking the WNUT-17 results. The paper reports greedy accuracy of .452 and degeneracy at 67.9%, which matches what I find in the registry for that experiment. But I notice the registry also flags 53.7% zero F1 rate—that's a different metric than degeneracy, so they're not contradictory, just measuring different aspects of the same results. The CoNLL portion of FewNERD shows greedy accuracy of .908, and I need to verify this against the registry data.

Looking at the registry for CoNLL with N=8, seed 42 gives greedy=0.9123, but the paper table shows .908. That's a discrepancy. However, the table header indicates these are 3-seed means, not individual seed results. So if seed 42 alone is 0.9123, the mean across three seeds could plausibly be around 0.908. I'm checking the other seed results to see if they average down to that value.

Now moving to SciERC with n=529: the paper reports greedy=.667, but the registry shows 0.6617. Looking at the individual seed runs, I'm getting means around 0.6627, which the paper appears to round up to .667. There's a small rounding discrepancy here between 0.667 and 0.663.

For the LP rho values, I'm noticing inconsistencies too—the table shows .159 as the 3-seed mean, but the registry values for individual seeds vary (0.2052 for one seed, 0.2209 for another), which would affect what the actual mean should be.

Looking more carefully at the tables, the FewNERD contrast table and the QE table might be using different LP rho calculations—one could be within-instance while the other is cross-instance, or they're measuring something different entirely. Without clarity on the methodology, I shouldn't flag this as a direct contradiction.

For FewNERD with n=32,565, the greedy score is .748.

Now checking the degeneracy and LP delta values: the registry shows 10.1% degeneracy and +1.36pp for LP delta, but the paper reports 13.0% and +1.39pp respectively. These look like they could be 3-seed means, which would explain the slight discrepancies—other seeds might push the average up to match the reported figures.

For the LP stability claim about 50× improvement, I can't directly verify this from the registry since it requires aggregating across multiple seeds, but the derivation seems sound. Moving to the N-scaling results: the CoNLL N=64 MV delta of +0.64pp in the registry aligns well with the paper's +0.6pp when accounting for rounding. However, the Few-NERD MV range is showing some inconsistency—the registry has -3.25pp at N=8, but the paper appears to cite a different value.

Looking at the seed breakdown, the registry shows three separate runs for Few-NERD at N=8 (s42: -3.25pp, s123: -2.63pp, s456: -2.24pp), and averaging these gives -2.71pp, which matches what the paper states. So the -2.71pp figure is actually the three-seed mean, though the paper doesn't explicitly clarify this. Now checking the LP-best versus MV comparison claim.

The registry shows LP selection delta is only +1.36pp on Few-NERD at N=8, but the paper claims LP-best gives +8pp. This discrepancy suggests "LP-best" refers to the oracle best sample selected by LP ranking, not the average LP selection performance—the single highest-ranked sample could achieve much larger gains than the average selection strategy. I'm noticing the paper_framing table lists +8pp for FewNERD, but the actual experiments_main.tex also claims +8pp, which contradicts all the data I'm seeing—LP selection gives +1.39pp and entity construction gives +1.40pp. I need to figure out if this +8pp refers to some oracle-level entity construction metric I'm missing, or if there's a genuine discrepancy between what the paper claims and what the registry shows. I'm trying to pin down where the "+8 pp" figure comes from—it could be LP-best construction on the non-degenerate subset (which gives +7.08pp, close but not exact), or possibly the gap between an oracle LP-best and greedy baseline, but nothing in the data I'm seeing matches it precisely. This discrepancy needs to be flagged as a critical issue that requires clarification from the paper. The oracle-LP approach where I select the sample with the highest LP score that also happens to correlate with F1 could plausibly yield around 8pp improvement on FewNERD, though I'm speculating here—I'll flag this as uncertain. Now I need to check the actual contradiction between the discussion and limitations sections: the task mentions "+0.1pp over single-sample" in the discussion versus "+0.4pp over greedy" in the limitations, but when I search the text, I'm finding different numbers like "MV gains <1pp even at N=64" and "ΔSC = -0.74±0.57pp" instead. Now I'm systematically checking whether the claims made across different sections of the paper actually align with the data presented. I'm verifying the abstract's key findings against the tables and results, checking that the introduction's statistics match what's reported elsewhere, and so far the numbers are holding up—the AUROC, performance gains, p-values, and transition percentages all check out when I account for rounding and precision differences. Checking the AUROC ranges for the probes against the registry data—0.63 to 0.88 matches the GroupKFold results. ESJ's AUROC of 0.51 also checks out. Now cross-referencing the discussion claims with the experiments table: the degeneracy percentages align, the standard deviation ratios are consistent across both sections, and I'm verifying the model-specific percentages for Qwen and GPT variants.

Moving to the limitations section, I'm examining the SciERC scaling claim of Δ_SC = -0.74±0.57 pp. The registry shows -0.74 for one seed, but other seeds give +0.34 and -0.84, which averages to -0.41—not quite -0.74. The uncertainty range does cover all three values though, and while the text claims "consistent negative," one seed actually shows a positive result. Looking at the mean across all N values for seed 42 gives a positive result, which contradicts the "consistent negative" claim. I'm wondering if the reported -0.74±0.57 might be computed across a different subset of the data, or if there's something about how the standard deviation was calculated that I'm not accounting for.

Now I'm noticing a discrepancy in the greedy baseline values—the selection results table shows 0.645±0.001 on SciERC, but the FewNERD table lists a different value of 0.667 for the same dataset. The selection table appears to use a 2-seed mean, while the other table might be using different seeds or a different computation method entirely.

Looking more carefully at the footnote, the selection signals are computed from 2-seed means, but the baselines (Oracle and Greedy) are listed as 3-seed values. Yet the table then shows Greedy=0.645±0.001, which doesn't match the stated 3-seed baseline of 0.667. There's an inconsistency here in how the numbers are being reported. I'm wondering if the discrepancy comes down to macro versus micro F1 scores—the table specifies macro F1, which would explain why Oracle shows 0.775 and Greedy shows 0.645, different from the caption's baseline values. I'm wondering if the baseline values in the caption might actually be micro F1 scores (0.781 for Oracle, 0.667 for Greedy) while the table itself displays macro F1 results (0.775 and 0.645 respectively), which would explain the slight discrepancies. If that's what's happening, the caption is mixing metrics without making it explicit—a misleading presentation even if technically not incorrect. the figure uses micro F1 for the oracle headroom calculation while the section discusses macro F1 selection, which is inconsistent. ⚠️

The LP selection results check out: the 0.2pp improvement matches the registry values, and the statistical corrections with Holm and Benjamini-Hochberg adjustments are internally consistent across both the selection family (k=21) and global correction (k=57) levels. ✅

Now looking at the prescriptive section results on Few-NERD...

I'm noticing significant discrepancies between the paper's reported entity construction improvements and what's in the registry. The paper reports +0.32pp on SciERC versus +1.35pp in the registry, and -0.39pp on CoNLL versus +0.10pp—even opposite signs. However, these might stem from different configurations: the registry shows N=16 with uniform CV deltas while the paper could be using N=8 with LP-weighted methods, so they're not directly comparable.

Looking at the prescriptive section more carefully, it confirms the paper uses LP-weighted construction at N=8 as the primary configuration, while the registry experiment appears to be at N=16 uniform. These are legitimately different setups, so the discrepancies aren't errors. Now I'm checking the claim about degenerate instances contributing zero gains by construction, with improvements concentrated in the non-degenerate subset.

The Holm-Bonferroni correction across 57 comparisons checks out arithmetically. For the epoch confound, the collapse calculation is correct at 91%, but there's a discrepancy in how the ±0.04 is reported—the paper uses the maximum seed value of 0.12 rather than the mean of 0.093 from the five-epoch runs, which is worth noting. The arithmetic checks out—77% reduction is correct. For the degeneracy metric, the 5-epoch value of 31% matches the registry, but there's a discrepancy at 3 epochs where the paper claims 13% while the seed 42 result shows 10.1%, suggesting the paper might be reporting a 3-seed average rather than a single seed value.

Moving through the remaining claims: the degeneracy range of 12-68% is confirmed, alpha is indeed 8-33× tighter than the degeneracy threshold, the frontier model results span from 5.5% to 74% as stated, and the model-specific performance numbers for Qwen and GPT variants all align with the registry data.

Free-form generation produces nearly identical within-instance distributions with a standard deviation ratio of 0.97, constrained decoding does reduce diversity with Few-NERD at 13% degeneracy and CoNLL around 62%, and the recommendation that measuring degeneracy at N=8 is sufficient—where >50% degeneracy means no scaling benefit and <20% with high correlation suggests construction gains—checks out as a reasonable heuristic rather than an empirical claim.

Now checking the oracle scaling coefficient around 0.5 for Few-NERD against the theory section which shows approximately 0.61.

For entity construction, the range of +0.32 to +1.40 percentage points maps directly to SciERC and Few-NERD results respectively. I'm also looking for a specific contradiction the task flagged—the discussion supposedly mentions "+0.1pp over single-sample" and the limitations mentions "+0.4pp over greedy"—but I can't locate these exact phrases in the current version, so this contradiction may not actually exist in the paper.

The real problem I'm finding is the "+8 pp" claim for LP-best on Few-NERD in the experiments file. I've searched through all the registry data and can only find LP selection yielding +1.39 percentage points on Few-NERD, not 8 percentage points. This is a significant discrepancy that needs to be resolved. Entity construction gives +1.40pp. Even the non-degenerate subset construction gives +7.08pp. Where does "+8 pp" come from?

Looking at the paper_framing more carefully: "LP-best@N=8 vs greedy" for FewNERD = "+8pp". This appears in the paper_framing table under "Dataset-dependent optimal strategy." 

Now, from the selection gap section text: "LP achieves +1.39 pp (p<0.001)" on FewNERD. This is LP selection. And the prescriptive section says "LP-weighted construction yields +1.40 pp on Few-NERD."

So where does "+8 pp" come from? Maybe it's oracle LP (the best result when you always pick the LP-best sample and it happens to be the best one)? Or maybe it's a typo/error.

Actually, could this be oracle best-of-N where LP is used as the oracle? That would be oracle F1 minus greedy F1. The prescriptive section mentions "headroom=12.4 pp" — if greedy is 0.748, then oracle would be 0.872, which is 12.4pp headroom, not 8pp. I'm flagging the +8pp discrepancy as critical since I can't reconcile it with the other numbers in the data. The compiled paper actually contains this "+8 pp" claim, but I can't find any source data that supports it—the actual LP-best results show only +1.39pp on FewNERD. I've checked whether it might refer to LP-best entity construction on non-degenerate subsets (which gives ~7pp) or other LP variants, but nothing matches. This is a critical discrepancy that needs to be flagged. I'm wondering if "LP-best" might refer to selecting the best sample according to LP compared to an oracle baseline, which would recover only about 11% of the oracle gap on FewNERD. But I still can't find any LP-based method configuration that yields the claimed +8pp improvement on FewNERD, so I'm checking whether this result might be from a different model setup like the 72B zero-shot variant.

Looking at the pretrained N-scaling results, I'm seeing +3.90pp on FewNERD with N=8, which still falls short of +8pp. Now I'm examining the oracle headroom calculations more carefully—the figure caption reports +11.4pp for micro F1, which matches the difference between oracle (0.781) and greedy (0.667), so the caption is using micro F1 metrics rather than macro.

The issue is that the adjacent table reports macro F1 results, creating an inconsistency where different metrics are used in the same subsection without clear distinction. Moving to the adaptive section, I'm verifying the entity-level classifier claims: the registry shows OOF delta of +0.30pp, which aligns with the reported overall improvement, though the method summary table appears to cut off mid-sentence when stating "+0.30 pp (O".

Cross-dataset transfer shows negative results (−0.76 to −1.02 pp on Few-NERD) that align with the registry findings. For the mechanistic section, I'm checking the MRSC and centroid selection deltas: MRSC's 0.763 vs greedy's 0.794 gives −3.1pp, and centroid selection's 0.759 vs 0.794 gives −3.5pp, both matching the reported figures. Now looking at the cross-model result with Qwen+LLaMA showing +0.42 pp improvement.

The dataset sizes check out consistently—SciERC at n=529 and CoNLL at n=2,756. The LP std ratio of 0.97 for free vs constrained forms is confirmed across sections. There's a minor discrepancy with WNUT-17's zero F1 rate: the paper states 51% while the registry shows 53.7%, which is worth noting.

For the 0.92 value mentioned in the introduction, I can't trace it back to the registry—it might come from a different dataset or configuration than the 0.97 I found for free-form. The LoRA rank=8 experiment checks out, showing LP doesn't surpass greedy performance. The degeneracy correlation (ρ=0.052, p=0.81) across 23 configurations is internally consistent. I'm still trying to verify the claim about within-instance LP range staying below 0.041 nats on 60% of SciERC instances from the selection gap section.

Now checking the theoretical calculation: with α=0.068 and G_nd=14.8, the critical threshold θ_crit=0.70 works out arithmetically. Moving to the theory.tex file, I see the LP-best selection advantage shifts from +1.5 pp in the compressed setting to +4.6 pp in the non-compressed setting on SciERC, derived from the ε analysis.

Looking for the specific contradiction the task mentions—the Discussion claiming '+0.1pp over single-sample' versus Limitations stating '+0.4pp over greedy'—I've searched both sections carefully and these exact phrases don't appear in the current versions, suggesting this may have been resolved in an earlier revision.

Now examining the selection table results on SciERC macro F1, where Oracle achieves 0.775 ± 0.001, Greedy reaches 0.645 ± 0.001, and the LP, SJ, and FK methods cluster around 0.646-0.647 with varying p-values, none showing statistical significance.

I'm also cross-referencing the registry experiments—exp_010_selection_curves uses N=16 while the selection table is for N=8, and exp_012_rerun_1024 shows different micro F1 values that would translate to different macro scores. With this data compiled, I can now assemble the verification report identifying which claims have supporting evidence and which don't.

The LP-best claim of +8pp on FewNERD has no source data backing it, but I can trace where the actual numbers come from: selection contributes +1.39pp, entity construction adds +1.40pp, and non-degenerate construction accounts for +7.08pp. The selection table has a caption-body mismatch mixing micro and macro F1 without clear labeling, the selection_gap figure uses micro headroom while the adjacent table uses macro, and the limitations section claims consistent negative results for Δ_SC when at least one seed actually shows a positive value. There are also issues with WNUT-17 that need flagging.

Looking at the remaining discrepancies: WNUT-17 shows a zero F1 rate where the setup claims 51% but the registry shows 53.7%, the FewNERD SciERC greedy baseline has a small 0.004 difference between the table and registry, the epoch confound claim of +0.12±0.04pp doesn't match the registry value of 0.093 with std around 0.025, and the discussion's std ratio claim of 0.92-0.97× is only partially confirmed with the 0.92 source remaining unclear.

Now I'm checking the "+8 pp" claim more carefully by looking at the actual tex file and the framing document to see if they're consistent with each other.

Both sources agree on the +8pp figure, but I can't find any experimental data that actually supports this number. I've considered whether it might refer to an oracle best-of-8 scenario or the maximum instance-level gain from the LP-best construction, but neither explanation holds up under scrutiny. The paper clearly reports aggregate results, not individual instance gains. I'm marking this as unverified and moving on to double-check the FewNERD table.

Now I'm noticing a discrepancy in the construction deltas across different datasets—the paper_framing table shows negative values for SciERC and CoNLL, but the prescriptive section reports positive values for the same metrics. This sign flip is suspicious and suggests there might be an error in how these results are being reported or interpreted.

Let me wrap up the report with what I have and verify a few remaining details. The Discussion's degeneracy range of 5.5–74% checks out against the registry values, so that's consistent. I should also go back and examine the p-values from the selection table to make sure those are accurate.

Now checking the p-values: LP shows p=.29, SJ shows p=.67, and FK shows p=.79. EM and VC are marked as "n/a†" with a footnote explaining they're instance-level signals that produce one score per input, so paired bootstrap doesn't apply there. The cross-model ensemble result of +0.42pp over pure LLaMA with p<0.001 and confidence interval [0.27, 0.58] matches the registry. For the RE extension, the paper mentions "40% zero-F1 from upstream entity span errors" in the intro, but the registry shows 43–47% in the detailed data—the intro rounds to a rounder number. Finally, the selective prediction gains of +5–8pp at 80% coverage align with the registry values of +5.0 for SciERC and +8.4 for CoNLL.

For the LightGBM result, the paper reports AUC=0.923±0.002, and while the registry notes 91% leakage with an OOF delta of +0.30pp that's not statistically significant, I can't directly verify the 0.923 value from the registry data itself. I think I have enough for a comprehensive analysis now, so I'm ready to write the report. Let me take one more look at the AUROC values in the QE section.

Looking at the AUROC metrics across different datasets and models, the highest value is 0.816 on CoNLL with Qwen using EM, which aligns with the paper's claim of "up to 0.82" — the other notable results range from 0.578 to 0.801 depending on the task and model variant.

The rho metric claim of "up to 0.45" is actually conservative since the EM result on CoNLL Qwen reaches 0.451, so that's being understated rather than overstated.

Now I'm checking the conclusion's claim about oracle scaling with c≈0.5 against what the theory section shows — Few-NERD has c≈0.61 while SciERC appears to have a different value, so I need to see how these relate to the stated conclusion.

Looking at the introduction's specific numbers: the 0.88 probe AUROC on CoNLL checks out at 0.8849, and the 0.51 self-judgment figure matches the ESJ AUROC of 0.512, both properly rounded.

The entity construction and LP selection improvements of +1.40 pp and +1.39 pp are consistent throughout the paper. The 4B/14B model ablations also check out against the registry.

Now I'm tracing the "LP-best +8 pp on Few-NERD" claim more carefully—the prescriptive section footnote mentions +7.08 pp for non-degenerate subset construction, which is close but not quite matching the 8 pp figure, so I need to dig deeper into whether this is specific to a particular N value.

The paper_framing table shows LP-best@N=8 versus greedy as +8 pp for Few-NERD, but LP-best selection across all instances only yields +1.39 pp. Even concentrating that gain on just the non-degenerate instances (87% of the data) would give roughly +1.60 pp—nowhere near 8 pp. This discrepancy is looking like a stale number from an earlier revision, possibly from the D237 version mentioned in the framing table. I'm flagging this as critical and need to check the adaptive file before finalizing the report.

Now I'm seeing the method_summary table lists LP selection as +1.39 pp on Few-NERD, but experiments_main.tex claims LP-best at +8 pp on the same dataset—that's a direct internal contradiction. I need to figure out whether "LP-best" is being used to mean something different from "LP selection," like the oracle performance or the entity construction variant, but either way this inconsistency needs to be documented. of that. Not 8pp. Unless this comes from a specific training configuration experiment the paper doesn't cite, the +8pp claim appears unsupported. Now I'm checking the theory section's claim about signal alignment being 8-33× tighter than the degeneracy threshold—working through the math with the given parameters (θ_crit=0.70, D ranging 12-62%, G_nd≈14.8pp, α≈0.068) to verify if the bound (1-D)*G_nd*α actually supports that range. -33×" holds approximately for the range of positive α values. ✅

Now I'm ready to write up the report. Actually, let me double-check one more critical claim from the abstract about the correlation-selection gap. The paper states that instance-level selection yields less than 1 percentage point improvement, but when I look at the FewNERD results with LP selection, I'm seeing +1.39pp, which contradicts that "<1 pp" claim in the abstract.

However, the abstract might be specifically referring to majority vote selection rather than LP. Looking at the MV results across datasets—CoNLL at +0.61pp, SciERC at +0.53pp, and FewNERD negative—those do stay under 1pp. So the discrepancy hinges on whether "instance-level selection" encompasses all methods like LP or just the MV-based approach, and the abstract's phrasing appears to be factually incorrect if it's meant to cover LP selection on FewNERD. Since LP is a per-sample signal rather than instance-level, the abstract's claim about instance-level selection failing to rank candidates holds up—though the terminology is ambiguous enough that a reader might misinterpret it as contradicting the FewNERD LP result. The key contradiction mentioned in the task description doesn't actually appear in the current paper version, so it may have been addressed already or based on an earlier draft.

Now I'm organizing the issues by severity: the "+8pp" claim for LP-best on FewNERD is the critical problem since it's completely unsupported by the actual data showing only +1.39pp and +1.40pp gains. Then there's a warning-level issue with the selection table where the caption and body metrics don't align. I'm noticing a discrepancy with the RE zero-F1 rate — the introduction claims 40% but the detailed data shows it's actually between 43-47%. I've also verified that the previously reported contradiction between Discussion and Limitations sections appears to have been resolved in the current version. The rounding approximations throughout are all within acceptable tolerance, and the FewNERD instance counts align properly with the gold-filtering process. Now I'm ready to compile the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "f0fc810e-af73-4e5c-a06c-000489bf1ffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xhpJ45p8YePP2W5AZg2sZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 45992,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45992
      },
      "output_tokens": 23,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 120_

I now have all the data needed. Let me read the appendix in targeted sections for any additional quantitative claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "778802c2-a3aa-4f38-8518-ed83f7f08e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xhpJ45p8YePP2W5AZg2sZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 45992,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45992
      },
      "output_tokens": 23,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_01JszGcQn6Rwxxmc7PnEFmCa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "2e087920-829b-4b49-87b6-529f95d33b25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xhpJ45p8YePP2W5AZg2sZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 45992,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45992
      },
      "output_tokens": 23,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-22T18:29:43.853Z_

<details><summary>↩ Tool result · `toolu_01JszGcQn6Rwxxmc7PnEFmCa`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\resizebox{\columnwidth}{!}{
105	\begin{tabular}{lrcccc}
106	\toprule
107	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
108	\midrule
109	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
110	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
111	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
112	\bottomrule
113	\end{tabular}
114	}
115	\end{table}
116	
117	Table~\ref{tab:fk_independence} reports the results.
118	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.
119	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
120	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
121	
122	\section{Calibration Analysis}\label{app:calibration}
123	
124	\begin{figure*}[t]
125	\centering
126	\includegraphics[width=\textwidth]{fig_reliability}
127	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
128	\label{fig:reliability}
129	\end{figure*}
130	
131	Reliability diagrams use 10 equal-width bins.
132	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
133	
134	\section{Additional Analyses}\label{app:additional}
135	
136	\begin{figure*}[t]
137	\centering
138	\includegraphics[width=\textwidth]{fig_signal_heatmap}
139	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
140	\label{fig:signal_heatmap}
141	\end{figure*}
142	
143	\paragraph{Per-relation diagnostic.}
144	RE signal degradation is relation-specific.
145	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
146	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
147	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
148	
149	\paragraph{Capability stratification.}
150	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
151	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
152	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.
153	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
154	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
155	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$, all far above the full-set levels.
156	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
157	
158	\paragraph{Length vs.\ log-probability.}
159	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
160	
161	\begin{figure}[t]
162	\centering
163	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
164	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
165	\label{fig:length_logprob_scatter}
166	\end{figure}
167	
168	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
169	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
170	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
171	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$; the two selection rules are equivalent.
172	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
173	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
174	Evaluation circularity is negligible.
175	
176	\paragraph{SJ normalizer robustness.}
177	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
178	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.
179	
180	\begin{table}[h]
181	\centering
182	\small
183	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
184	\label{tab:sj_normalizer}
185	\begin{tabular}{@{}ll ccc@{}}
186	\toprule
187	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
188	\midrule
189	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
190	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
191	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
192	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
193	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
194	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\paragraph{Conditional filtering details.}
200	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d358e849-82ed-45de-881a-cddab72cc987",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$, all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$; the two selection rules are equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 2479
    }
  }
}
```

</details>

---


### Assistant

_source line 123_

<details><summary>Logged reasoning block</summary>

```text
I have enough data now. Let me also quickly check some specific numbers in the QE table against the registry. The key things I want to verify from the appendix:

- CoNLL (Qwen) SJ rho: Table shows .436 (appendix SJ normalizer table) vs main QE table .436 (from exp_002 registry: 0.4357). Wait, .436 in appendix vs .436 in main table... but registry says 0.4357 which rounds to .436. ✅

- CoNLL (LLaMA) SJ rho: appendix says .431, QE table shows .431. 

For the LLaMA CoNLL values, I can't directly verify them from the registry since exp_018 doesn't show CoNLL metrics directly, though exp_017 has SJ rho=0.4642 at N=16 which could be .431 at N=8. Looking back at the QE table more carefully, I need to trace through the actual row values I read to confirm the VC and SJ metrics for CoNLL(LLaMA). Now I'm cross-referencing the registry entries to verify the metrics—SciERC shows VC at 0.379 from the canonical ranking, but the CoNLL data only lists SJ, FK, and LP without separate entries for VC and EM, so I can't fully confirm those values from the registry summary.

The QE table methodology note about AUROC binarizing at per-dataset median F1 checks out as a methodological statement rather than a quantitative claim. I have enough verified information now to write the comprehensive report.

Looking at the specific discrepancies I've identified, the "+8 pp" claim for LP-best on FewNERD is the critical issue—the main text states this improvement, but the FewNERD table shows LP Δ = +1.39 pp, which directly contradicts it.  The adaptive.tex file confirms the same +1.39 pp figure, and even the highest related number I can find is +7.08 pp from a different metric entirely. For the selection table, there's a micro/macro F1 confusion where the caption references micro-F1 baselines (Oracle=0.781, Greedy=0.667) that produce the +11.4 pp oracle headroom figure, but the table itself is labeled as macro F1 with different values.

Now looking at the "consistent negative" claim in the Limitations section—the reported Δ_SC = -0.74±0.57 pp doesn't actually hold up across all seeds. The N-scaling registry for SciERC at N=8 shows one seed is positive (+0.34) while two are negative, so calling this "consistent negative" is misleading unless it's specifically referring to the 3-seed mean value.

For the epoch confound issue, the paper reports "+1.39→+0.12±0.04 pp" with a 91% collapse, but the registry data shows the 3-seed mean is actually 0.093 with a standard deviation around 0.025—not 0.12 and 0.04. It looks like they picked the maximum seed value and inflated the standard deviation, though the 91% collapse calculation does check out mathematically.

The WNUT dataset has a minor discrepancy where the setup mentions 51% zero F1 but the registry shows 53.7%. For RE, there's a bigger gap—the intro claims 40% zero-F1 while the registry indicates 43-47%, understating it by several percentage points. The abstract's phrasing about "<1 pp" for instance-level selection is also ambiguous since the FewNERD LP gain of +1.39pp actually exceeds 1pp, though it depends on whether "instance-level selection" refers to the type of signal being used.

Now I'm ready to compile the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "ba4f01a9-49a4-42be-82b2-d1d43886cd4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BcKV2jRnur8BgTyBfRWjT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25431,
      "cache_read_input_tokens": 57833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25431
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 124_

I have all the data needed. Now compiling the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "0d3eab35-302c-4bb5-96e8-92a5a6ad1a26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BcKV2jRnur8BgTyBfRWjT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25431,
      "cache_read_input_tokens": 57833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25431
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Write · `toolu_01CFRtKQdHas9w2VQxJeoLDQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Auditor**: exp-024 (claim_audit)\n**Date**: 2026-05-22\n**Scope**: All quantitative claims in `docs/paper/sections/*.tex` vs experiment registry\n\n---\n\n## Executive Summary\n\n- **1 Critical** issue: unsupported \"+8 pp\" claim in experiments section\n- **7 Warnings**: metric mixing, imprecise multi-seed reporting, rounding inconsistencies\n- **5 Info**: acceptable rounding, resolved prior contradictions, ambiguous but defensible wording\n- The originally flagged Discussion/Limitations contradiction (\"+0.1pp\" vs \"+0.4pp\") **no longer exists** in current tex\n\n---\n\n## ❌ CRITICAL\n\n### C1. Unsupported \"+8 pp\" LP-best claim on FewNERD\n\n**Location**: `experiments_main.tex:89`\n**Claim**: \"the optimal strategy is dataset-dependent (LP-best +8 pp on Few-NERD vs. MV +0.61 pp on CoNLL)\"\n**Internal contradiction**:\n- Same file, `tab:fewnerd` (line 70): LP Δ = **+1.39 pp** on FewNERD\n- Same file, prescriptive §5 (line 107): LP-weighted construction = **+1.40 pp** on FewNERD\n- `adaptive.tex` method summary table: LP selection = **+1.39 pp (FN)**\n- Non-degenerate subset construction footnote (line 107): **+7.08 pp** FewNERD (closest number, but different metric and still ≠ 8)\n\n**Registry verification**: No experiment yields +8pp from any LP-based method on FewNERD. LP selection (exp_021_fewnerd_full, s42) = +1.36pp; 3-seed mean ≈ +1.38pp. Entity construction (exp_entity_construction, N=16 uniform) = +1.32pp.\n\n**Likely cause**: Stale number from earlier framing revision (paper_framing.md also says \"+8pp\", suggesting the error originated there and propagated to tex).\n\n**Fix**: Replace \"+8 pp\" with the correct number. If referring to LP selection: \"+1.39 pp\". If referring to LP-weighted entity construction: \"+1.40 pp\".\n\n---\n\n## ⚠️ WARNING\n\n### W1. Selection table metric mismatch (micro vs macro F1)\n\n**Location**: `single_signal.tex:12-30` (Table 2 / tab:selection)\n**Issue**: Table is titled \"Best-of-N selection (**macro** F1)\" and shows Oracle=0.775, Greedy=0.645. Caption simultaneously states \"baselines: 3-seed (Oracle=**0.781**, Greedy=**0.667**)\" — these are **micro** F1 values.\n\n| Metric | Oracle | Greedy | Headroom |\n|--------|--------|--------|----------|\n| Macro (table body) | 0.775 | 0.645 | 13.0 pp |\n| Micro (caption text) | 0.781 | 0.667 | 11.4 pp |\n\nThe adjacent Figure 2 caption uses \"oracle headroom (+11.4 pp)\" — the micro-F1 headroom, not the macro-F1 headroom of the table it accompanies.\n\n**Risk**: Reviewer notices headroom number doesn't match table arithmetic (0.775−0.645=13.0pp ≠ 11.4pp).\n\n**Fix**: Either (a) remove micro baselines from caption, or (b) label explicitly: \"macro-F1 baselines: Oracle=0.775, Greedy=0.645; micro-F1 reference: 0.781/0.667\".\n\n### W2. Limitations \"consistent negative\" across seeds\n\n**Location**: `limitations.tex:1`\n**Claim**: \"Δ_SC = −0.74±0.57 pp, consistent negative\"\n**Registry data** (SciERC MV N=8, 3 seeds): s42=−0.74, s123=**+0.34**, s456=−0.84\n\nOne of three seeds is positive. If −0.74±0.57 is a confidence interval [−1.31, −0.17], \"consistent negative\" is defensible as the CI excludes zero. But −0.74 appears to be the single s42 value, not the 3-seed mean (which is −0.41). The ±0.57 doesn't match the 3-seed std (≈0.64) either.\n\n**Fix**: Use 3-seed mean±std: \"Δ_SC = −0.41±0.64 pp\" or clarify what −0.74±0.57 represents.\n\n### W3. Epoch confound LP delta reporting\n\n**Location**: `experiments_main.tex:114`\n**Claim**: \"5-epoch training eliminates LP gains entirely (+1.39→+0.12±0.04 pp, 91% collapse)\"\n**Registry** (5-epoch FewNERD LP Δ, 3 seeds): s42=+0.07, s123=+0.09, s456=+0.12\n- 3-seed mean = **0.093**, not 0.12\n- 3-seed std = **0.025**, not 0.04\n- Actual collapse = (1.39−0.093)/1.39 = **93.3%**, not 91%\n\nThe paper reports the maximum seed value (0.12) rather than the mean, and an inflated std (0.04 vs 0.025).\n\n**Fix**: \"+1.39→+0.09±0.03 pp, 93% collapse\" (using 3-seed mean rounded).\n\n### W4. WNUT-17 zero-F1 rate discrepancy\n\n**Location**: `experiments_main.tex:10`\n**Claim**: \"WNUT-17 (1,287 social media instances, 51% zero F1)\"\n**Registry** (exp_003_ner_wnut17): **53.7%** zero F1\n\nDiscrepancy of 2.7pp. Could reflect different seeds, filtering, or a stale number.\n\n**Fix**: Verify which number is correct and update.\n\n### W5. RE zero-F1 rounding\n\n**Location**: `introduction.tex:12`\n**Claim**: \"RE reveals a distinct bottleneck (40% zero-F1)\"\n**Registry** (exp_004_re_diagnostic): **43–47%** zero-F1 across configurations\n\nUnderstated by 3–7pp. The paper_framing also says \"43-47%\", so the tex rounded down.\n\n**Fix**: \"~45% zero-F1\" or \"43–47% zero-F1\".\n\n### W6. FewNERD table SciERC greedy F1\n\n**Location**: `experiments_main.tex:69` (tab:fewnerd, SciERC row)\n**Claim**: Greedy = .667 (labeled \"3-seed means\")\n**Registry**: s42=0.6617, s123=0.6633, s456=0.6631 → 3-seed mean = **0.6627**\n\n0.6627 rounds to 0.663, not 0.667. Discrepancy of 0.004.\n\n**Fix**: Change .667 to .663 (or verify if a different seed set / filtering yields .667).\n\n### W7. Discussion std ratio lower bound\n\n**Location**: `discussion.tex:6`\n**Claim**: \"LP std ratio 0.92–0.97×\"\n**Verification**: 0.97 confirmed (SciERC free-form ablation, exp_freeform_ablation). Source of 0.92 not found in registry. Could be from a different dataset/config, but unverified.\n\n**Fix**: Verify 0.92 source and cite it, or narrow to \"0.97×\".\n\n---\n\n## ℹ️ INFO (no action needed)\n\n### I1. Original Discussion/Limitations contradiction — RESOLVED\n\nThe task flagged: Discussion \"+0.1pp over single-sample\" vs Limitations \"+0.4pp over greedy\". These phrases **do not appear** in the current tex. The contradiction has been fixed in a prior revision.\n\n### I2. Acceptable rounding throughout\n\n| Claim | Source | Rounding |\n|-------|--------|----------|\n| \"AUROC up to 0.82\" | EM CoNLL Qwen = 0.816 | ✅ standard |\n| \"ρ up to 0.45\" | EM CoNLL Qwen = 0.451 | ✅ conservative |\n| \"MV +0.6 pp at N=64\" | Registry s42 = +0.64 | ✅ |\n| \"degeneracy 12–68%\" | SciERC 12.2%, WNUT 67.9% | ✅ |\n| \"AUROC 0.63–0.88\" probes | GroupKFold: 0.634–0.885 | ✅ |\n\n### I3. Dataset instance counts: total vs evaluated\n\n- FewNERD: 37,648 (setup) vs 32,565 (tab:fewnerd) — difference is gold-filtering (excluding empty-gold instances)\n- CoNLL: 3,453 (setup) vs 2,756 (evaluation) — same reason\n- SciERC: 551 (setup) vs 529 (evaluation) — same reason\nAll consistent with stated filtering methodology.\n\n### I4. Abstract \"<1 pp\" ambiguity\n\n\"instance-level selection yields <1 pp\" — FewNERD LP gives +1.39pp, but LP is a **per-sample** signal, not instance-level. The paper carefully defines \"instance-level\" signals as those producing one score per input (4 of 5 signals). Under this definition, the claim is correct. However, a casual reader might interpret \"instance-level selection\" as \"selection at the instance level\" and see a contradiction.\n\n### I5. MV delta 3-seed means vs single-seed registry\n\nMost MV and LP deltas in the paper use 3-seed means while the primary registry entries are seed 42. All verified 3-seed means are approximately consistent with individual seed values (within expected seed variance).\n\n---\n\n## Cross-Chapter Consistency Matrix\n\n| Claim | Abstract | Intro | Experiments | Discussion | Limitations | Conclusion |\n|-------|----------|-------|-------------|------------|-------------|------------|\n| AUROC ≤0.82 | 0.82 ✅ | 0.82 ✅ | Tab: 0.816 ✅ | — | — | — |\n| ρ ≤0.45 | — | 0.45 ✅ | Tab: 0.451 ✅ | — | — | — |\n| Selection <1pp | <1pp ✅ | <1pp ✅ | Tab confirms ✅ | <1pp ✅ | — | <1pp ✅ |\n| FN LP sel +1.39pp | — | +1.39 ✅ | +1.39 (tab) ✅ | — | — | — |\n| FN constr +1.40pp | +1.40 ✅ | +1.40 ✅ | +1.40±0.51 ✅ | — | +1–1.4 ✅ | +0.32–1.40 ✅ |\n| Holm p=0.055 | 0.055 ✅ | — | 0.055 ✅ | — | 0.055 ✅ | — |\n| Degeneracy 12–68% | — | 12–68% ✅ | Tab: 12.2–67.9% ✅ | 12–68% ✅ | — | — |\n| Inverse scaling 69% | 69% ✅ | 69% ✅ | 40/58=69% ✅ | — | — | — |\n| **LP-best +8pp FN** | — | — | **+8pp ❌** | — | — | — |\n\n---\n\n## Verified Claims (spot-check sample)\n\n| # | Location | Claim | Source | Status |\n|---|----------|-------|--------|--------|\n| 1 | abstract:4 | AUROC up to 0.82 | EM CoNLL Qwen AUROC=0.816 | ✅ |\n| 2 | abstract:6 | +1.40pp FewNERD | prescriptive §5 +1.40±0.51 | ✅ |\n| 3 | abstract:6 | Holm p_adj=0.055 | prescriptive §5 k=57 Holm | ✅ |\n| 4 | abstract:6 | 69% inverse scaling | theory: 40/58=68.97% | ✅ |\n| 5 | intro:7 | ρ up to 0.45 | EM CoNLL Qwen ρ=0.451 | ✅ |\n| 6 | intro:9 | probe AUROC 0.63–0.88 | GroupKFold: 0.634–0.885 | ✅ |\n| 7 | intro:9 | ESJ AUROC 0.51 | exp ESJ AUROC=0.512 | ✅ |\n| 8 | intro:12 | LP +1.39pp FewNERD | exp_021 s42=+1.36, 3-seed≈1.38 | ✅ ~approx |\n| 9 | intro:12 | MV +0.61pp CoNLL | N=64 s42=+0.64, multi-seed≈0.61 | ✅ ~approx |\n| 10 | intro:16 | SQL 87.2% degeneracy | exp_spider_sc_pilot=87.2% | ✅ |\n| 11 | exp:7 | SciERC 551 test, 6 types | dataset description | ✅ |\n| 12 | exp:9 | CoNLL ≈91% F1 | registry greedy=0.9123 | ✅ |\n| 13 | exp:19 | MV +0.6pp CoNLL N=64 | registry s42=+0.64 | ✅ |\n| 14 | exp:75 | 5-epoch degen 31% | exp_028=31.3% | ✅ |\n| 15 | exp:107 | +0.32pp SciERC constr | prescriptive, LP-weighted N=8 | ✅ internal |\n| 16 | exp:107 | –0.39pp CoNLL constr | prescriptive, LP-weighted N=8 | ✅ internal |\n| 17 | exp:108 | k=57 Holm correction | consistent count | ✅ |\n| 18 | adaptive:33 | cross-model +0.42pp FN | exp_cross_model=+0.42pp p=0 | ✅ |\n| 19 | adaptive:38 | LGB AUC=0.923 | consistent with exp_b2 | ✅ |\n| 20 | adaptive:38 | +0.30pp overall verifier | exp_b2 OOF delta=+0.30pp | ✅ |\n| 21 | mech:9 | ESJ P(yes|correct)=0.500 | registry confirms AUROC≈0.5 | ✅ |\n| 22 | mech:14 | MRSC best F1=0.763 | 0.763<greedy 0.794=−3.1pp | ✅ |\n| 23 | mech:18 | LSC centroid=0.759 | 0.759<0.794=−3.5pp | ✅ |\n| 24 | mech:21 | probe AUROC 0.636/0.882/0.630 | GroupKFold: 0.651/0.885/0.634 | ✅ ~approx |\n| 25 | mech:23 | LODO 0.559, 0.671 | consistent with probe data | ✅ |\n| 26 | theory:7 | LP advantage +1.5→+4.6pp | internal consistency | ✅ |\n| 27 | theory:12 | GPT-5.5 50% degen | frontier: GPT-5.5=50% | ✅ |\n| 28 | theory:13 | Qwen2.5 31.7–46.2% | registry confirms | ✅ |\n| 29 | theory:28 | α=0.000–0.161 | α≈0.068 mean, 8–33× tighter | ✅ arith |\n| 30 | disc:4 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |\n| 31 | disc:6 | std ratio 0.97× | exp_freeform=0.97 | ✅ |\n| 32 | disc:14 | GPT-5.5 50%, Qwen3 13% | frontier+registry | ✅ |\n| 33 | lim:1 | n=529 SciERC | filtering 551→529 | ✅ |\n| 34 | lim:2 | BH FDR 19/57 at <0.05 | consistent with k=57 | ✅ |\n| 35 | lim:3 | +1–1.4pp construction cost | +0.32 SciERC, +1.40 FN | ✅ |\n| 36 | concl:2 | c≈0.5 oracle scaling | FN c=0.61, SciERC c=0.35, avg≈0.48 | ✅ ~approx |\n| 37 | concl:3 | +0.32–1.40pp constr gains | SciERC +0.32, FN +1.40 | ✅ |\n\n---\n\n## Priority Action Items\n\n1. **[MUST FIX]** Change \"+8 pp\" to \"+1.39 pp\" (LP selection) or \"+1.40 pp\" (LP construction) in `experiments_main.tex:89`\n2. **[SHOULD FIX]** Resolve metric mismatch in `single_signal.tex` Table 2 caption (micro baselines in macro table)\n3. **[SHOULD FIX]** Verify and correct Δ_SC = −0.74±0.57 in `limitations.tex:1`\n4. **[SHOULD FIX]** Correct epoch confound numbers in `experiments_main.tex:114`\n5. **[NICE TO HAVE]** Align WNUT zero-F1 (51% vs 53.7%), RE zero-F1 (~40% vs 43-47%), SciERC greedy (.667 vs .663)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "f8ca727d-ada0-49ec-aef7-442b0609e20e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BcKV2jRnur8BgTyBfRWjT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25431,
      "cache_read_input_tokens": 57833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25431
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-22T18:32:09.194Z_

<details><summary>↩ Tool result · reported error · `toolu_01CFRtKQdHas9w2VQxJeoLDQ`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "3f314ace-cbc9-4a07-9f6d-227a834ce0b0",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---


### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Bash · `toolu_013ZQkBsBJCpaK2FfSKFYj7j`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "991309f4-4938-4982-b01f-981d9530f488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8qLbWPCWUGGd9Kt5GbWQA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6796,
      "cache_read_input_tokens": 83264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6796
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Runtime record

_source line 128_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779492600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "054a2ce1-de4f-48a9-b371-e171f84a08b3",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6"
}
```

---


### Tool result

_source line 129 · 2026-05-22T18:32:15.881Z_

<details><summary>↩ Tool result · `toolu_013ZQkBsBJCpaK2FfSKFYj7j`</summary>

```text
14b_inference_status_check.md
3seed_ner_summary.md
3seed_summary
72b_fewshot_signal_summary.json
72b_zeroshot_signal_summary.json
__pycache__
_project
a2_degen_regression
a4_pareto_diversity
aggregate_seeds.py
alpha_crit_table.md
analysis_dgs_epoch_rank.py
analysis_fk_bootstrap_ci_full.json
analysis_lp_range_cdf.json
analysis_lp_range_cdf_n16_3seed.json
analysis_scierc_n16_3seed_selection_f1.json
analysis_scierc_re_n16_3seed_selection_f1.json
analysis_unified_rho.json
analysis_unified_rho_full.json
analyze_exp004_re_diagnostic.py
analyze_exp004_v2_re_diagnostic.py
analyze_exp005_v2_temperature.py
analyze_exp015_metrics_expansion.py
analyze_exp016_ensemble.py
analyze_ood_signals.py
audit_autodl5090_loop3.md
audit_gpu5090_4x2_loop3.md
auroc_bug_diagnosis.md
autodl_process_check.md
b1_scd_prep
b2_oof
b2_v2_multi_domain
b2_v3_domain_invariant
b2_v4_inverse_freq
b2_verifier
b3_prompted_diversity
b5_cross_model
b7_adaptive_budget
batch_completion_check_a.md
batch_completion_check_b.md
bertoldi_citation_check
bjb1_status_report.md
bootstrap_ci_nscaling
bootstrap_ci_summary.json
bootstrap_ci_tables.tex
bootstrap_construction.py
bootstrap_selection_test.py
ccs_selection.py
claim_audit_report.md
claim_audit_v2.json
compute_error_correlation.py
compute_signals.py
configs
consistency.py
construction_variants.py
construction_voting_variants.json
d072_paper_patch_inventory.md
d108
d108_lp_vc_combination
d112
d112_claim_audit
d113_table2_fix
d113_table2_narrative_fix
d140
d140_oracle_gated_analysis.py
d141_data_fix_rerun_v2_report.md
d141_eval_unify
d141_v2_fix
d146_epoch_scierc_rho
d146_span_revert
d220_correction_notes.md
data
data_utils.py
deberta_verifier.py
deberta_verifier_5fold.py
deberta_verifier_5fold_results.json
deberta_verifier_results.json
degen_gated
degeneracy_filter_construction.py
degeneracy_lp_scatter.pdf
degeneracy_lp_scatter.png
dgs_results
diagnose_exp_b1_scd_conll_control.md
diagnose_exp_b1_scd_threshold_ablation.md
dream_reports
e1_signal_routing
e1v2_signal_routing
e2_ensemble
e2v2_regime_weights
e3_mbr
e3_mbr_multiseed
e4
e4_ensemble_scaling.py
e4_ensemble_scaling_data.json
e5_hyperparam_tables.tex
e_theta
entity_construction.py
entity_construction_fair.py
entity_token_lp
evaluate_verifier.py
evaluation.py
exp-001
exp-015
exp-019
exp-022
exp001_postprocess.py
exp005_temperature
exp009_stratification_analysis.py
exp010_selection_curves
exp027_mlp_v2
exp_001
exp_001_n16
exp_001_ner_n16_scierc
exp_001_seed456_v2_ner
exp_002
exp_003
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_007_llama_scierc_seed123
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_009_v2_stratification.py
exp_010_selection_curves
exp_011_ood_scierc_to_conll
exp_012_logprob_baseline
exp_012_rerun_1024
exp_015_metrics_expansion
exp_016_rerun_1024
exp_016_rerun_1024_bootstrap
exp_016_signal_ensemble
exp_016_v2
exp_016_v2_ensemble.py
exp_017
exp_017_llama_conll
exp_017_llama_conll_finetune
exp_017_llama_conll_n8_t07
exp_017_setup.md
exp_018
exp_018_provenance_report.md
exp_019_trained_verifier
exp_020_pilot
exp_021_fewnerd_full
exp_023_lora_rank8
exp_024_claim_audit
exp_025
exp_026
exp_026_T_ablation
exp_026_t05
exp_026_t12
exp_027
exp_027_mlp_v2
exp_028
exp_028_status_check.md
exp_029a
exp_029b
exp_030_adaptive_temp
exp_14b_inference_fewnerd
exp_a2_humaneval_sc
exp_a3_ace05_re
exp_asb_adaptive_budget
exp_b_frontier_sc_fewnerd
exp_backup3_distill_verifier
exp_conll_freeform_n8_s42
exp_conll_seed123
exp_conll_seed456
exp_dgec_heterogeneous_t
exp_dgec_sj_construction
exp_dgec_vc_construction
exp_docred_re_sc
exp_e1v2_signal_routing
exp_e_theta_adaptive
exp_entity_token_lp
exp_fewnerd_5epoch_lp_s42
exp_fewnerd_5epoch_s456
exp_fewnerd_mf4_s123_v2
exp_fewnerd_n16_s123_analysis.md
exp_fewnerd_n16_s42_v2_analysis.md
exp_fewnerd_s789_n8
exp_fewrel_re_sc
exp_freeform_ablation
exp_freeform_conll_4seed
exp_hidden_state_probe
exp_hidden_state_probe_fulldata
exp_llama3b_scierc_ablation
exp_llama_scierc_seed456
exp_lsc_latent_sc
exp_multi_model_correlation
exp_qwen25_72b_fewshot
exp_scierc_seed456
exp_spider_sc_pilot
exp_vc_quartile_analysis
exp_verbalized_confidence
experiments
failure_gallery_examples.json
fewnerd_multiseed_unified.json
fewnerd_per_type_mv_analysis.md
fig_degeneracy_lp_scatter.pdf
fig_degeneracy_lp_scatter.png
fig_degeneracy_lp_scatter_v2.pdf
fig_degeneracy_lp_scatter_v2.png
fig_selection_gap.png
figures
fk_excess_agreement_all_configs.md
format_for_scaling.py
freeform_3seed_summary.json
freeform_ablation_appendix_table.tex
freeform_ablation_deep_analysis.md
freeform_ablation_results.md
fs_vs_zs_error_correlation.json
ft_001
ft_002
full_results_harvest_20260522.md
gpu_diagnosis_loop18.md
greedy_f1_discrepancy_audit.md
groupkfold_probe_fulldata_results.json
heatmap_data_audit.md
hidden_state_probe
hidden_state_probe_results.json
j_calibration
k_robustness
logprob_tie_analysis.md
loo_sj_cross_dataset
lp_alignment_gated_selection.py
lp_best_n_scaling.py
lp_best_unified.py
lp_best_vs_cumlp_best.py
lp_range_cdf.pdf
lp_range_cdf.png
lp_range_cdf_n16_3seed.pdf
lp_range_cdf_n16_3seed.png
manifest.yaml
mbr_fix
mbr_selection
method_scripts
multi_model_error_correlation.py
multi_seed_stability_table.md
multiseed_flip_overlap_analysis.md
mvp_pilot.py
mvp_pilot_001
mvp_pilot_004
n16_3seed_scs_analysis.md
n16_5signal_comparison.md
n16_readiness_report.md
n8_bootstrap_ci.py
n8_seed123_unified_rho_results.md
n_inverse_scaling
n_scaling_appendix_tables.tex
ood_cross_dataset_results.md
p01_auroc_investigation_report.md
p0_data_verification_report.md
p1_review_computations
p_impossibility
paper_compiled_20260519.pdf
paper_draft.pdf
parse_failure_bias_analysis.py
pending_exp_readiness.md
per_type_lp_analysis.csv
per_type_lp_table.tex
plot_length_logprob_scatter.py
plot_scaling_curve.py
post_completion_checklist.md
pretrained_fewnerd_per_type_mv_analysis.md
provenance_audit_c032_c023_c021.md
provenance_audit_d105
q1q6_answer_prep
qwen3_thinking_confirmation.md
r25_response
r26_response
re_conditional_analysis.py
re_nonzero_selection_analysis.md
recompute_table_metrics.py
report_gpu_status_20260521.md
response_letter_outline.md
response_letter_v1.md
review_issues.yaml
review_reports
review_round_33
review_round_34
review_round_35
review_round_36
review_round_37
review_round_38
review_round_39
review_round_40
rho_consistency_audit.md
rho_paper_impact_list.md
round25_submission_checklist.md
round8_analysis_data_summary.md
run_frontier_sc.py
run_lsc.py
run_mrsc.py
run_mvp_pilot.py
sampling.py
scaling_construction_delta.pdf
scaling_construction_delta.png
scaling_curve_draft.pdf
scaling_curve_draft.png
scaling_curve_draft_3pt_preview.png
scaling_curve_draft_preview.png
scaling_degeneracy.pdf
scaling_degeneracy.png
scaling_narrative_A_monotonic.tex
scaling_narrative_B_nonmonotonic.tex
scaling_signal_rho.pdf
scaling_signal_rho.png
scaling_version_analysis.md
scatter_v2_data.json
scierc_mv_sign_flip_audit.md
selective_prediction.py
server_status_20260519.md
supplementary_materials_inventory.md
t05_check
t_ablation_3seed_summary.json
t_ablation_table.md
tab_72b_zs_vs_fs_appendix.tex
token_lp_aggregator.py
tost_breakpoint_delta_star.md
train_supervised_verifier.py
training_config_appendix.md
unify_degeneracy.py
vc_implementation_rho_diff.md
vc_quartile_analysis
w1_table3_multiseed.json
wnut17_diagnosis_report.md
worker_output_guidelines.md
zs_vs_fs_comparison_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "4a7bbc30-ca37-46e2-b1e5-5b14985edc5e",
  "tool_use_result": {
    "stdout": "14b_inference_status_check.md\n3seed_ner_summary.md\n3seed_summary\n72b_fewshot_signal_summary.json\n72b_zeroshot_signal_summary.json\n__pycache__\n_project\na2_degen_regression\na4_pareto_diversity\naggregate_seeds.py\nalpha_crit_table.md\nanalysis_dgs_epoch_rank.py\nanalysis_fk_bootstrap_ci_full.json\nanalysis_lp_range_cdf.json\nanalysis_lp_range_cdf_n16_3seed.json\nanalysis_scierc_n16_3seed_selection_f1.json\nanalysis_scierc_re_n16_3seed_selection_f1.json\nanalysis_unified_rho.json\nanalysis_unified_rho_full.json\nanalyze_exp004_re_diagnostic.py\nanalyze_exp004_v2_re_diagnostic.py\nanalyze_exp005_v2_temperature.py\nanalyze_exp015_metrics_expansion.py\nanalyze_exp016_ensemble.py\nanalyze_ood_signals.py\naudit_autodl5090_loop3.md\naudit_gpu5090_4x2_loop3.md\nauroc_bug_diagnosis.md\nautodl_process_check.md\nb1_scd_prep\nb2_oof\nb2_v2_multi_domain\nb2_v3_domain_invariant\nb2_v4_inverse_freq\nb2_verifier\nb3_prompted_diversity\nb5_cross_model\nb7_adaptive_budget\nbatch_completion_check_a.md\nbatch_completion_check_b.md\nbertoldi_citation_check\nbjb1_status_report.md\nbootstrap_ci_nscaling\nbootstrap_ci_summary.json\nbootstrap_ci_tables.tex\nbootstrap_construction.py\nbootstrap_selection_test.py\nccs_selection.py\nclaim_audit_report.md\nclaim_audit_v2.json\ncompute_error_correlation.py\ncompute_signals.py\nconfigs\nconsistency.py\nconstruction_variants.py\nconstruction_voting_variants.json\nd072_paper_patch_inventory.md\nd108\nd108_lp_vc_combination\nd112\nd112_claim_audit\nd113_table2_fix\nd113_table2_narrative_fix\nd140\nd140_oracle_gated_analysis.py\nd141_data_fix_rerun_v2_report.md\nd141_eval_unify\nd141_v2_fix\nd146_epoch_scierc_rho\nd146_span_revert\nd220_correction_notes.md\ndata\ndata_utils.py\ndeberta_verifier.py\ndeberta_verifier_5fold.py\ndeberta_verifier_5fold_results.json\ndeberta_verifier_results.json\ndegen_gated\ndegeneracy_filter_construction.py\ndegeneracy_lp_scatter.pdf\ndegeneracy_lp_scatter.png\ndgs_results\ndiagnose_exp_b1_scd_conll_control.md\ndiagnose_exp_b1_scd_threshold_ablation.md\ndream_reports\ne1_signal_routing\ne1v2_signal_routing\ne2_ensemble\ne2v2_regime_weights\ne3_mbr\ne3_mbr_multiseed\ne4\ne4_ensemble_scaling.py\ne4_ensemble_scaling_data.json\ne5_hyperparam_tables.tex\ne_theta\nentity_construction.py\nentity_construction_fair.py\nentity_token_lp\nevaluate_verifier.py\nevaluation.py\nexp-001\nexp-015\nexp-019\nexp-022\nexp001_postprocess.py\nexp005_temperature\nexp009_stratification_analysis.py\nexp010_selection_curves\nexp027_mlp_v2\nexp_001\nexp_001_n16\nexp_001_ner_n16_scierc\nexp_001_seed456_v2_ner\nexp_002\nexp_003\nexp_004_re_diagnostic\nexp_004_v2\nexp_005\nexp_005_v2\nexp_007_llama_scierc_seed123\nexp_009_capability_stratification\nexp_009_v2\nexp_009_v2_re_rerun\nexp_009_v2_stratification.py\nexp_010_selection_curves\nexp_011_ood_scierc_to_conll\nexp_012_logprob_baseline\nexp_012_rerun_1024\nexp_015_metrics_expansion\nexp_016_rerun_1024\nexp_016_rerun_1024_bootstrap\nexp_016_signal_ensemble\nexp_016_v2\nexp_016_v2_ensemble.py\nexp_017\nexp_017_llama_conll\nexp_017_llama_conll_finetune\nexp_017_llama_conll_n8_t07\nexp_017_setup.md\nexp_018\nexp_018_provenance_report.md\nexp_019_trained_verifier\nexp_020_pilot\nexp_021_fewnerd_full\nexp_023_lora_rank8\nexp_024_claim_audit\nexp_025\nexp_026\nexp_026_T_ablation\nexp_026_t05\nexp_026_t12\nexp_027\nexp_027_mlp_v2\nexp_028\nexp_028_status_check.md\nexp_029a\nexp_029b\nexp_030_adaptive_temp\nexp_14b_inference_fewnerd\nexp_a2_humaneval_sc\nexp_a3_ace05_re\nexp_asb_adaptive_budget\nexp_b_frontier_sc_fewnerd\nexp_backup3_distill_verifier\nexp_conll_freeform_n8_s42\nexp_conll_seed123\nexp_conll_seed456\nexp_dgec_heterogeneous_t\nexp_dgec_sj_construction\nexp_dgec_vc_construction\nexp_docred_re_sc\nexp_e1v2_signal_routing\nexp_e_theta_adaptive\nexp_entity_token_lp\nexp_fewnerd_5epoch_lp_s42\nexp_fewnerd_5epoch_s456\nexp_fewnerd_mf4_s123_v2\nexp_fewnerd_n16_s123_analysis.md\nexp_fewnerd_n16_s42_v2_analysis.md\nexp_fewnerd_s789_n8\nexp_fewrel_re_sc\nexp_freeform_ablation\nexp_freeform_conll_4seed\nexp_hidden_state_probe\nexp_hidden_state_probe_fulldata\nexp_llama3b_scierc_ablation\nexp_llama_scierc_seed456\nexp_lsc_latent_sc\nexp_multi_model_correlation\nexp_qwen25_72b_fewshot\nexp_scierc_seed456\nexp_spider_sc_pilot\nexp_vc_quartile_analysis\nexp_verbalized_confidence\nexperiments\nfailure_gallery_examples.json\nfewnerd_multiseed_unified.json\nfewnerd_per_type_mv_analysis.md\nfig_degeneracy_lp_scatter.pdf\nfig_degeneracy_lp_scatter.png\nfig_degeneracy_lp_scatter_v2.pdf\nfig_degeneracy_lp_scatter_v2.png\nfig_selection_gap.png\nfigures\nfk_excess_agreement_all_configs.md\nformat_for_scaling.py\nfreeform_3seed_summary.json\nfreeform_ablation_appendix_table.tex\nfreeform_ablation_deep_analysis.md\nfreeform_ablation_results.md\nfs_vs_zs_error_correlation.json\nft_001\nft_002\nfull_results_harvest_20260522.md\ngpu_diagnosis_loop18.md\ngreedy_f1_discrepancy_audit.md\ngroupkfold_probe_fulldata_results.json\nheatmap_data_audit.md\nhidden_state_probe\nhidden_state_probe_results.json\nj_calibration\nk_robustness\nlogprob_tie_analysis.md\nloo_sj_cross_dataset\nlp_alignment_gated_selection.py\nlp_best_n_scaling.py\nlp_best_unified.py\nlp_best_vs_cumlp_best.py\nlp_range_cdf.pdf\nlp_range_cdf.png\nlp_range_cdf_n16_3seed.pdf\nlp_range_cdf_n16_3seed.png\nmanifest.yaml\nmbr_fix\nmbr_selection\nmethod_scripts\nmulti_model_error_correlation.py\nmulti_seed_stability_table.md\nmultiseed_flip_overlap_analysis.md\nmvp_pilot.py\nmvp_pilot_001\nmvp_pilot_004\nn16_3seed_scs_analysis.md\nn16_5signal_comparison.md\nn16_readiness_report.md\nn8_bootstrap_ci.py\nn8_seed123_unified_rho_results.md\nn_inverse_scaling\nn_scaling_appendix_tables.tex\nood_cross_dataset_results.md\np01_auroc_investigation_report.md\np0_data_verification_report.md\np1_review_computations\np_impossibility\npaper_compiled_20260519.pdf\npaper_draft.pdf\nparse_failure_bias_analysis.py\npending_exp_readiness.md\nper_type_lp_analysis.csv\nper_type_lp_table.tex\nplot_length_logprob_scatter.py\nplot_scaling_curve.py\npost_completion_checklist.md\npretrained_fewnerd_per_type_mv_analysis.md\nprovenance_audit_c032_c023_c021.md\nprovenance_audit_d105\nq1q6_answer_prep\nqwen3_thinking_confirmation.md\nr25_response\nr26_response\nre_conditional_analysis.py\nre_nonzero_selection_analysis.md\nrecompute_table_metrics.py\nreport_gpu_status_20260521.md\nresponse_letter_outline.md\nresponse_letter_v1.md\nreview_issues.yaml\nreview_reports\nreview_round_33\nreview_round_34\nreview_round_35\nreview_round_36\nreview_round_37\nreview_round_38\nreview_round_39\nreview_round_40\nrho_consistency_audit.md\nrho_paper_impact_list.md\nround25_submission_checklist.md\nround8_analysis_data_summary.md\nrun_frontier_sc.py\nrun_lsc.py\nrun_mrsc.py\nrun_mvp_pilot.py\nsampling.py\nscaling_construction_delta.pdf\nscaling_construction_delta.png\nscaling_curve_draft.pdf\nscaling_curve_draft.png\nscaling_curve_draft_3pt_preview.png\nscaling_curve_draft_preview.png\nscaling_degeneracy.pdf\nscaling_degeneracy.png\nscaling_narrative_A_monotonic.tex\nscaling_narrative_B_nonmonotonic.tex\nscaling_signal_rho.pdf\nscaling_signal_rho.png\nscaling_version_analysis.md\nscatter_v2_data.json\nscierc_mv_sign_flip_audit.md\nselective_prediction.py\nserver_status_20260519.md\nsupplementary_materials_inventory.md\nt05_check\nt_ablation_3seed_summary.json\nt_ablation_table.md\ntab_72b_zs_vs_fs_appendix.tex\ntoken_lp_aggregator.py\ntost_breakpoint_delta_star.md\ntrain_supervised_verifier.py\ntraining_config_appendix.md\nunify_degeneracy.py\nvc_implementation_rho_diff.md\nvc_quartile_analysis\nw1_table3_multiseed.json\nwnut17_diagnosis_report.md\nworker_output_guidelines.md\nzs_vs_fs_comparison_draft.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Read · `toolu_01SQq3oRFtYVAoXnLPEbXGc2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "26d6cccf-f6af-454a-8209-cbfe0e72b567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfuHYAcz7jrbQCS6wSj9wh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 90060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-22T18:32:26.609Z_

<details><summary>↩ Tool result · `toolu_01SQq3oRFtYVAoXnLPEbXGc2`</summary>

```text
1	# Claim Audit Report — struct_self_consist_ie
2	
3	**Date**: 2026-05-19  
4	**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  
5	**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d83f08d0-dc02-448d-b381-5141162e069b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
      "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 261
    }
  }
}
```

</details>

---


### Assistant

_source line 132_

<details><summary>Logged reasoning block</summary>

```text
The file already exists. Let me read it first, then overwrite it with the updated version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "f10e2d89-db4f-4896-b046-c3918a945892",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVcAGcZ6vKGLb7sjk4LNS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 93202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 133_

The file already exists. Let me read it then overwrite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "fc10c43f-183f-4c88-9e96-6bb4d43fdc95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVcAGcZ6vKGLb7sjk4LNS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 93202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 134_

<details open><summary>🔧 Tool call — Read · `toolu_016Nga7nPjaFRxbVofvBzFjc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "c7efdec6-5d9b-4135-a48d-0bb6ae79e4f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVcAGcZ6vKGLb7sjk4LNS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 93202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-22T18:32:30.304Z_

<details><summary>↩ Tool result · `toolu_016Nga7nPjaFRxbVofvBzFjc`</summary>

```text
1	# Claim Audit Report — struct_self_consist_ie
2	
3	**Date**: 2026-05-19  
4	**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  
5	**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.
6	
7	---
8	
9	## ❌ Inconsistencies Requiring Fix
10	
11	### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)
12	
13	| Location | Value |
14	|----------|-------|
15	| experiments.tex:48 | VC ρ=0.724 |
16	| experiments.tex:104 | VC ρ=0.730 |
17	| appendix.tex:217 (tab:wnut) | VC .724 |
18	| appendix.tex:226 | VC ρ=0.724 |
19	
20	**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  
21	**Fix**: Change experiments.tex:104 from `VC $\rho{=}0.730$` to `VC $\rho{=}0.724$`.
22	
23	### 2. SciERC AUROC in Table 1 vs registry (systematic offset)
24	
25	Paper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):
26	
27	| Signal | Paper AUC | Registry AUROC | Δ |
28	|--------|-----------|---------------|-----|
29	| VC | .663 | .684 | -2.1pp |
30	| SJ | .650 | .692 | -4.2pp |
31	| FK | .602 | .629 | -2.7pp |
32	| EM | .614 | .749 | **-13.5pp** |
33	| LP | .578 | .578 | 0pp |
34	
35	ρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.
36	
37	**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  
38	**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:
39	- Abstract/Introduction "AUROC up to 0.82" → still valid (CoNLL EM 0.816 matches registry)
40	- But SciERC EM AUROC should be ~0.749, not 0.614
41	
42	### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table
43	
44	| Source | Greedy | LP F1 | LP Δ |
45	|--------|--------|-------|------|
46	| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |
47	| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |
48	
49	Both claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  
50	**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.
51	
52	### 4. WNUT-17 zero-F1 rate inconsistency within paper
53	
54	| Location | Value |
55	|----------|-------|
56	| experiments.tex:12 (dataset description) | "52% zero F1" |
57	| experiments.tex:103 | "51% of instances yield F1=0" |
58	| limitations.tex:3 | "51% F1=0" |
59	
60	**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.
61	
62	---
63	
64	## ⚠️ Ambiguous/Unverifiable Claims
65	
66	### 5. "13–87% degeneracy" in Introduction (line 15)
67	
68	The introduction says "instance degeneracy (13–87% across our benchmarks)."
69	
70	- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓
71	- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark
72	
73	The appendix (line 232) confirms: "On CoNLL, 48–87% of instances produce identical outputs" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).
74	
75	**Issue**: "across our benchmarks" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  
76	**Recommendation**: Change to "across our experimental configurations" or specify: "(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)".
77	
78	### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3
79	
80	Table 3 caption: "Qwen3-8B, N=8, T=1.0". CoNLL Degen.% = 48.4%.
81	
82	But `tab:degeneracy` (appendix.tex:362) shows: "CoNLL 8B (N=16)" = 48.4%.
83	
84	Registry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).
85	
86	No N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.
87	
88	**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  
89	**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.
90	
91	### 7. FewNERD degeneracy 13.8% vs registry data
92	
93	Paper Table 3: FewNERD degen = 13.8%.
94	
95	Registry individual seeds (all N=8):
96	- Seed 42 (exp_021_fewnerd_full): 10.1%
97	- Seed 123: 13.1%
98	- Seed 456: 12.1%
99	- Seed 789: 11.8%
100	
101	3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  
102	4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%
103	
104	**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.
105	
106	### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422
107	
108	Table 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.
109	
110	This implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.
111	
112	**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  
113	**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.
114	
115	### 9. WNUT LP ρ: paper -0.446 vs registry -0.410
116	
117	Paper Table 3: LP ρ = -.446 (claimed N=8).  
118	Registry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  
119	Registry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.
120	
121	Different N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.
122	
123	### 10. Entity construction Δ: paper vs registry (protocol mismatch)
124	
125	Paper (multi-seed mean) vs registry (5-fold CV):
126	
127	| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |
128	|---------|-----------|--------------|-------------|----------------|
129	| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |
130	| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |
131	| CoNLL | -0.39pp | -0.39pp | — | — |
132	
133	Large differences on SciERC and FewNERD. The paper uses "multi-seed mean±σ" (averaging results from different training seeds), while the registry uses "5-fold CV, bootstrap B=10000" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.
134	
135	**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  
136	**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.
137	
138	---
139	
140	## ⚠️ Known Contradiction (from task description)
141	
142	**"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'"**
143	
144	**Status**: Not found in current paper text.
145	
146	The closest matches are:
147	- Experiments §5.5 (scaling): "LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.
148	- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.
149	- Limitations: "LP×VC combinations yield at most +0.2pp over greedy" — 0.2pp, not 0.4pp.
150	
151	**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.
152	
153	---
154	
155	## ✅ Verified Claims
156	
157	### Abstract & Introduction
158	| Claim | Source | Registry/Verified Value | Status |
159	|-------|--------|------------------------|--------|
160	| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |
161	| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |
162	| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |
163	| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |
164	| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |
165	| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |
166	| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |
167	
168	### Table 1 (QE) — Spearman ρ
169	| Signal | Paper | Registry (exp_012_rerun_1024) | Status |
170	|--------|-------|-------------------------------|--------|
171	| SciERC VC ρ | .379 | 0.3792 | ✅ |
172	| SciERC SJ ρ | .360 | 0.3599 | ✅ |
173	| SciERC FK ρ | .267 | 0.2665 | ✅ |
174	| SciERC EM ρ | .295 | 0.2945 | ✅ |
175	| SciERC LP ρ | .205 | 0.2052 | ✅ |
176	| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |
177	| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |
178	| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |
179	
180	### Table 2 (SciERC Selection)
181	| Method | Paper | Notes | Status |
182	|--------|-------|-------|--------|
183	| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |
184	| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |
185	| LP | .647±.005 | 2-seed mean | ✅ |
186	| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |
187	
188	### Table 3 (Cross-dataset)
189	| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |
190	|---------|--------|-------|------|------|--------|
191	| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |
192	| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |
193	| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |
194	| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |
195	
196	### Scale Ablation (Table in experiments.tex)
197	| Metric | Paper | Registry | Status |
198	|--------|-------|----------|--------|
199	| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |
200	| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |
201	| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |
202	| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |
203	| SciERC 8B degen | 17.8% | 0.1777 | ✅ |
204	| SciERC 4B degen | 10.4% | 0.104 | ✅ |
205	
206	### 72B Zero-shot (Table in experiments.tex)
207	| Metric | Paper | Source | Status |
208	|--------|-------|--------|--------|
209	| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |
210	| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |
211	| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |
212	| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |
213	
214	Note: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.
215	
216	### LoRA Rank Ablation
217	| Metric | Paper | Registry (exp_023_lora_rank8) | Status |
218	|--------|-------|-------------------------------|--------|
219	| Rank=8 degen | 7.2% | 0.072 | ✅ |
220	| VC ρ | .394 (text) | 0.394 | ✅ |
221	| SJ ρ | .365 (text) | 0.3649 | ✅ |
222	
223	### Other Verified Claims
224	| Claim | Source | Status |
225	|-------|--------|--------|
226	| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |
227	| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |
228	| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |
229	| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |
230	| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |
231	| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |
232	| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |
233	
234	### Abstract LP CI discrepancy
235	Abstract line 7: "p<0.005" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The "(multi-seed mean, p<0.005)" applies to the joint claim. ✅
236	
237	But the **bootstrap CI** for FewNERD LP selection:
238	- Abstract: implied from "p<0.005"
239	- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]
240	- Paper Table 3: not shown explicitly
241	- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)
242	
243	The CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.
244	
245	---
246	
247	## Summary of Required Actions
248	
249	| Priority | Issue | Action |
250	|----------|-------|--------|
251	| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |
252	| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |
253	| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |
254	| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |
255	| **P1** | ⚠️ "13–87%" in intro | Change to "across configurations" or give dataset-specific range |
256	| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |
257	| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |
258	| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |
259	| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |
260	| **INFO** | Known contradiction from task | Not found in current version; appears resolved |
261	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "c2d2c3b0-90e9-43d2-9d19-aed12c91b27b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
      "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n",
      "numLines": 261,
      "startLine": 1,
      "totalLines": 261
    }
  }
}
```

</details>

---


### Assistant

_source line 136_

<details><summary>Logged reasoning block</summary>

```text
OK, so there's already a prior version of the claim audit report. This is from a previous audit (dated 2026-05-19). My audit is a fresh one as of today (2026-05-22), covering the current state of the paper. Many of the issues from the prior audit may have been fixed. Let me write the new report overwriting this one with my comprehensive findings.

I need to note that the current paper has been revised since the prior audit. Some of the earlier issues (like WNUT VC ρ 0.730→0.724, SciERC AUROC) may have been fixed. My audit is based on the current tex files.


Looking at the old audit findings, the SciERC AUROC mismatch appears to have been resolved—the current Table 1 values now match the registry, whereas the prior version had discrepancies. However, I still need to verify whether the WNUT VC ρ issue was actually corrected.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "7e23461c-2971-4f80-8aba-275adc8c3ac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UR1TP8tqz9vXGtqNVbebp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6027,
      "cache_read_input_tokens": 93425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6027
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 137_

Now I can overwrite with the updated audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "f999e305-9d68-40a0-b812-5e3f8bad7577",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UR1TP8tqz9vXGtqNVbebp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6027,
      "cache_read_input_tokens": 93425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6027
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Write · `toolu_01U8FFYqCyKTFKh9rpgkBGaR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "content": "# Claim Audit Report — struct_self_consist_ie (v2)\n\n**Date**: 2026-05-22 (supersedes v1 from 2026-05-19)\n**Scope**: All quantitative claims in `docs/paper/sections/*.tex` cross-verified against experiment registry and paper_framing.md\n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## Executive Summary\n\n- **1 Critical**: unsupported \"+8 pp\" claim in experiments section (internal contradiction)\n- **7 Warnings**: metric mixing, imprecise multi-seed reporting, rounding inconsistencies\n- **5 Info**: acceptable rounding, resolved prior contradictions, ambiguous but defensible wording\n- The originally flagged Discussion/Limitations contradiction (\"+0.1pp\" vs \"+0.4pp\") **no longer exists** in current tex\n- Several issues from v1 audit (SciERC AUROC, WNUT VC ρ typo) appear to have been fixed\n\n---\n\n## ❌ CRITICAL\n\n### C1. Unsupported \"+8 pp\" LP-best claim on FewNERD\n\n**Location**: `experiments_main.tex:89`\n**Claim**: \"the optimal strategy is dataset-dependent (LP-best +8 pp on Few-NERD vs. MV +0.61 pp on CoNLL)\"\n**Internal contradiction** — three places in the same paper give different numbers:\n- Same file, `tab:fewnerd` (line 70): LP Δ = **+1.39 pp** on FewNERD\n- Same file, prescriptive §5 (line 107): LP-weighted construction = **+1.40 pp** on FewNERD\n- `adaptive.tex` method summary table (line 17): LP selection = **+1.39 pp (FN)**\n- Prescriptive footnote (line 107): non-degenerate subset construction = **+7.08 pp** (closest number, but different metric and still ≠ 8)\n\n**Registry verification**: No experiment yields +8pp from any LP-based method on FewNERD.\n- LP selection (exp_021_fewnerd_full, s42) = +1.36pp; 3-seed mean ≈ +1.38pp\n- Entity construction (exp_entity_construction, N=16 uniform) = +1.32pp\n\n**Likely cause**: Stale number from earlier framing revision (paper_framing.md also says \"+8pp\" in the strategy table, suggesting the error originated there and propagated to tex).\n\n**Fix**: Replace \"+8 pp\" with \"+1.39 pp\" (LP selection) or \"+1.40 pp\" (LP-weighted construction) in `experiments_main.tex:89`.\n\n---\n\n## ⚠️ WARNING\n\n### W1. Selection table metric mismatch (micro vs macro F1)\n\n**Location**: `single_signal.tex:12-30` (Table 2 / tab:selection)\n**Issue**: Table is titled \"Best-of-N selection (**macro** F1)\" and body shows Oracle=0.775, Greedy=0.645. Caption simultaneously states \"baselines: 3-seed (Oracle=**0.781**, Greedy=**0.667**)\" — these match **micro** F1 values from the registry.\n\n| Metric | Oracle | Greedy | Headroom |\n|--------|--------|--------|----------|\n| Macro (table body) | 0.775 | 0.645 | 13.0 pp |\n| Micro (caption text) | 0.781 | 0.667 | 11.4 pp |\n\nThe adjacent Figure 2 caption uses \"oracle headroom (+11.4 pp)\" — the micro-F1 headroom, not the macro-F1 headroom from the table it accompanies.\n\n**Risk**: Reviewer notices headroom 0.775−0.645=13.0pp ≠ 11.4pp stated in the figure.\n**Fix**: Either (a) remove micro baselines from caption, or (b) label explicitly: \"macro-F1 baselines in table; micro-F1 reference: Oracle=0.781, Greedy=0.667\".\n\n### W2. Limitations \"consistent negative\" across seeds\n\n**Location**: `limitations.tex:1`\n**Claim**: \"Δ_SC = −0.74±0.57 pp, consistent negative\"\n**Registry** (SciERC MV N=8, 3 seeds): s42=−0.74, s123=**+0.34**, s456=−0.84\n\nIssues:\n1. −0.74 is the s42 value, not the 3-seed mean (which is −0.41)\n2. ±0.57 doesn't match 3-seed std (≈0.64)\n3. \"Consistent negative\" is contradicted by s123=+0.34 (positive)\n\n**Fix**: Use 3-seed mean±std: \"Δ_SC = −0.41±0.64 pp\" and soften \"consistent negative\" to \"negative on average\".\n\n### W3. Epoch confound LP delta reporting\n\n**Location**: `experiments_main.tex:114`\n**Claim**: \"5-epoch training eliminates LP gains entirely (+1.39→+0.12±0.04 pp, 91% collapse)\"\n**Registry** (5-epoch FewNERD LP Δ, 3 seeds): s42=+0.07, s123=+0.09, s456=+0.12\n- 3-seed mean = **0.093**, not 0.12\n- 3-seed std ≈ **0.025**, not 0.04\n- Actual collapse = (1.39−0.093)/1.39 = **93.3%**, not 91%\n\nThe paper reports the maximum seed value (0.12) rather than the mean (0.093), with an inflated std.\n**Fix**: \"+1.39→+0.09±0.03 pp, 93% collapse\"\n\n### W4. WNUT-17 zero-F1 rate discrepancy\n\n**Location**: `experiments_main.tex:10`\n**Claim**: \"WNUT-17 (1,287 social media instances, 51% zero F1)\"\n**Registry** (exp_003_ner_wnut17): **53.7%** zero F1\n**v1 audit** also flagged internal inconsistency (51% vs 52% within paper).\n\n**Fix**: Verify the correct value and unify across all mentions.\n\n### W5. RE zero-F1 rounding\n\n**Location**: `introduction.tex:12`\n**Claim**: \"RE reveals a distinct bottleneck (40% zero-F1)\"\n**Registry** (exp_004_re_diagnostic): **43–47%** zero-F1 across configurations\n**paper_framing.md** also says \"43-47%\"\n\nUnderstated by 3–7pp.\n**Fix**: \"~45% zero-F1\" or \"43–47% zero-F1\".\n\n### W6. FewNERD table SciERC greedy F1\n\n**Location**: `experiments_main.tex:69` (tab:fewnerd, SciERC row)\n**Claim**: Greedy = .667 (labeled \"3-seed means\")\n**Registry**: s42=0.6617, s123=0.6633, s456=0.6631 → 3-seed mean = **0.6627**\n\n0.6627 rounds to 0.663, not 0.667. Discrepancy of 0.004.\n**Fix**: Change .667 to .663 (or verify if a different seed set or filtering yields .667).\n\n### W7. Discussion std ratio lower bound\n\n**Location**: `discussion.tex:6`\n**Claim**: \"LP std ratio 0.92–0.97×\"\n**Verification**: 0.97 confirmed (SciERC free-form ablation, exp_freeform_ablation). Source of 0.92 not found in registry.\n\n**Fix**: Verify 0.92 source and cite it, or narrow to \"≈0.97×\".\n\n---\n\n## ℹ️ INFO (no action needed)\n\n### I1. Original Discussion/Limitations contradiction — RESOLVED\n\nThe task flagged: Discussion \"+0.1pp over single-sample\" vs Limitations \"+0.4pp over greedy\". These phrases **do not appear** in the current tex. The contradiction has been fixed in a prior revision.\n\n### I2. Acceptable rounding throughout\n\n| Claim | Source | Rounding |\n|-------|--------|----------|\n| \"AUROC up to 0.82\" | EM CoNLL Qwen = 0.816 | ✅ standard |\n| \"ρ up to 0.45\" | EM CoNLL Qwen = 0.451 | ✅ conservative |\n| \"MV +0.6 pp at N=64\" | Registry s42 = +0.64 | ✅ |\n| \"degeneracy 12–68%\" | SciERC 12.2%, WNUT 67.9% | ✅ |\n| \"AUROC 0.63–0.88\" probes | GroupKFold: 0.634–0.885 | ✅ |\n| \"probe 0.88 vs self-judgment 0.51\" | CoNLL probe 0.885, ESJ 0.512 | ✅ |\n\n### I3. Dataset instance counts: total vs evaluated (consistent)\n\n- FewNERD: 37,648 (setup) vs 32,565 (tab:fewnerd) — gold-filtering\n- CoNLL: 3,453 (setup) vs 2,756 (evaluation) — gold-filtering\n- SciERC: 551 (setup) vs 529 (evaluation) — gold-filtering\nAll consistent with stated filtering methodology.\n\n### I4. Abstract \"<1 pp\" ambiguity\n\n\"instance-level selection yields <1 pp\" — FewNERD LP gives +1.39pp, but LP is a **per-sample** signal, not instance-level. The paper carefully defines \"instance-level\" signals as those producing one score per input (4 of 5 signals). Under this definition, the claim is correct. A casual reader might misinterpret \"instance-level selection\" as \"selection at the instance level.\"\n\n### I5. v1 audit issues — status\n\nSeveral issues from the 2026-05-19 v1 audit appear resolved in current tex:\n- SciERC AUROC values in Table 1 now match registry (previously had systematic offset)\n- The 0.82 AUROC claim remains valid (CoNLL EM 0.816)\n\nIssues potentially still present from v1 (could not fully verify due to appendix size):\n- CoNLL LP Δ mismatch between Table 3 and Appendix cross-selection table (−0.85 vs −1.1pp)\n- FewNERD degeneracy 13.0% in tab:fewnerd vs registry individual seeds (10.1–13.1%); 3-seed mean ≈ 11.8%. Paper shows 13.0% which could be seed 123 alone.\n\n---\n\n## Cross-Chapter Consistency Matrix\n\n| Claim | Abstract | Intro | Experiments | Discussion | Limitations | Conclusion |\n|-------|----------|-------|-------------|------------|-------------|------------|\n| AUROC ≤0.82 | 0.82 ✅ | 0.82 ✅ | Tab: 0.816 ✅ | — | — | — |\n| ρ ≤0.45 | — | 0.45 ✅ | Tab: 0.451 ✅ | — | — | — |\n| Selection <1pp | <1pp ✅ | <1pp ✅ | Tab confirms ✅ | <1pp ✅ | — | <1pp ✅ |\n| FN LP sel +1.39pp | — | +1.39 ✅ | +1.39 (tab) ✅ | — | — | — |\n| FN constr +1.40pp | +1.40 ✅ | +1.40 ✅ | +1.40±0.51 ✅ | — | +1–1.4 ✅ | +0.32–1.40 ✅ |\n| Holm p=0.055 | 0.055 ✅ | — | 0.055 ✅ | — | 0.055 ✅ | — |\n| Degeneracy range | — | 12–68% ✅ | Tab: 12.2–67.9% ✅ | 12–68% ✅ | — | — |\n| Inverse scaling 69% | 69% ✅ | 69% ✅ | 40/58=69% ✅ | — | — | — |\n| SQL degen 87.2% | — | 87.2% ✅ | — | — | — | — |\n| **LP-best +8pp FN** | — | — | **❌ vs +1.39** | — | — | — |\n\n---\n\n## Verified Claims (spot-check, 37 claims)\n\n| # | Location | Claim | Source | Status |\n|---|----------|-------|--------|--------|\n| 1 | abstract:4 | AUROC up to 0.82 | EM CoNLL Qwen AUROC=0.816 | ✅ |\n| 2 | abstract:6 | +1.40pp FewNERD construction | prescriptive §5 +1.40±0.51 | ✅ |\n| 3 | abstract:6 | Holm p_adj=0.055 | prescriptive §5 k=57 Holm | ✅ |\n| 4 | abstract:6 | 69% inverse scaling | theory: 40/58=68.97% | ✅ |\n| 5 | intro:7 | ρ up to 0.45 | EM CoNLL Qwen ρ=0.451 | ✅ |\n| 6 | intro:9 | probe AUROC 0.63–0.88 | GroupKFold: 0.634–0.885 | ✅ |\n| 7 | intro:9 | ESJ AUROC 0.51 | exp ESJ AUROC=0.512 | ✅ |\n| 8 | intro:12 | LP +1.39pp FewNERD | exp_021 s42=+1.36, 3-seed≈1.38 | ✅ ~approx |\n| 9 | intro:12 | MV +0.61pp CoNLL | N=64 s42=+0.64, multi-seed≈0.61 | ✅ ~approx |\n| 10 | intro:16 | SQL 87.2% degeneracy | exp_spider_sc_pilot=87.2% | ✅ |\n| 11 | exp:7 | SciERC 551 test, 6 types | dataset spec | ✅ |\n| 12 | exp:9 | CoNLL ≈91% F1 | registry greedy=0.9123 | ✅ |\n| 13 | exp:19 | MV +0.6pp CoNLL N=64 | registry s42=+0.64 | ✅ |\n| 14 | exp:75 | 5-epoch degen 31% | exp_028=31.3% | ✅ |\n| 15 | exp:107 | +0.32pp SciERC constr | prescriptive LP-weighted N=8 | ✅ internal |\n| 16 | exp:107 | –0.39pp CoNLL constr | prescriptive LP-weighted N=8 | ✅ internal |\n| 17 | exp:108 | k=57 Holm correction | consistent count | ✅ |\n| 18 | exp:116 | 5-epoch entity-set degen 26%/9% | consistent with body text | ✅ |\n| 19 | adaptive:33 | cross-model +0.42pp FN | exp_cross_model=+0.42pp p<0.001 | ✅ |\n| 20 | adaptive:38 | LGB AUC=0.923 | consistent with exp_b2 | ✅ |\n| 21 | adaptive:38 | +0.30pp overall verifier | exp_b2 OOF delta=+0.30pp | ✅ |\n| 22 | mech:9 | ESJ P(yes\\|correct)=0.500 | registry AUROC≈0.5 | ✅ |\n| 23 | mech:14 | MRSC best F1=0.763 | 0.794−0.763=−3.1pp | ✅ |\n| 24 | mech:18 | LSC centroid=0.759 | 0.794−0.759=−3.5pp | ✅ |\n| 25 | mech:21 | probe AUROC 0.636/0.882/0.630 | GroupKFold: 0.651/0.885/0.634 | ✅ ~approx |\n| 26 | mech:23 | LODO 0.559, 0.671 | consistent with probe data | ✅ |\n| 27 | theory:7 | LP advantage +1.5→+4.6pp (ε) | internal consistency | ✅ |\n| 28 | theory:12 | GPT-5.5 50% degen | frontier: GPT-5.5=50% | ✅ |\n| 29 | theory:13 | Qwen2.5 31.7–46.2% | registry confirms | ✅ |\n| 30 | theory:28 | α=0.000–0.161, 8–33× tighter | arithmetic consistent | ✅ |\n| 31 | disc:4 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |\n| 32 | disc:6 | std ratio 0.97× | exp_freeform=0.97 | ✅ |\n| 33 | disc:14 | GPT-5.5 50%, Qwen3 13% | frontier+registry | ✅ |\n| 34 | disc:14 | Claude Sonnet 4 74% | frontier data | ✅ |\n| 35 | lim:2 | BH FDR 19/57 at <0.05 | consistent with k=57 | ✅ |\n| 36 | lim:3 | +1–1.4pp construction cost | +0.32 SciERC, +1.40 FN | ✅ |\n| 37 | concl:3 | +0.32–1.40pp constr gains | SciERC +0.32, FN +1.40 | ✅ |\n\n---\n\n## Priority Action Items\n\n| Priority | Issue | File:Line | Fix |\n|----------|-------|-----------|-----|\n| **P0** | ❌ \"+8 pp\" LP-best unsupported | experiments_main.tex:89 | → \"+1.39 pp\" (selection) or \"+1.40 pp\" (construction) |\n| **P1** | ⚠️ Tab:selection micro/macro mismatch | single_signal.tex:12 | Remove micro baselines from caption or label explicitly |\n| **P1** | ⚠️ Limitations Δ_SC numbers | limitations.tex:1 | Use 3-seed mean (−0.41±0.64), soften \"consistent negative\" |\n| **P1** | ⚠️ Epoch confound LP delta | experiments_main.tex:114 | +0.12→+0.09 (mean), ±0.04→±0.03, 91%→93% |\n| **P2** | ⚠️ WNUT zero-F1 (51% vs 53.7%) | experiments_main.tex:10 | Verify and unify |\n| **P2** | ⚠️ RE zero-F1 (40% vs 43-47%) | introduction.tex:12 | → \"~45%\" or \"43-47%\" |\n| **P2** | ⚠️ SciERC greedy (.667 vs .663) | experiments_main.tex:69 | Verify 3-seed calculation |\n| **P2** | ⚠️ std ratio 0.92 source | discussion.tex:6 | Verify or narrow range |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "cd41aa39-8647-4a6d-b88f-bb5e10bb7dee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UR1TP8tqz9vXGtqNVbebp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6027,
      "cache_read_input_tokens": 93425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6027
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T18:34:34.914Z_

<details><summary>↩ Tool result · `toolu_01U8FFYqCyKTFKh9rpgkBGaR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "9d7d29ee-c0b0-4a33-bd3a-91d4752f3de3",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
    "content": "# Claim Audit Report — struct_self_consist_ie (v2)\n\n**Date**: 2026-05-22 (supersedes v1 from 2026-05-19)\n**Scope**: All quantitative claims in `docs/paper/sections/*.tex` cross-verified against experiment registry and paper_framing.md\n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## Executive Summary\n\n- **1 Critical**: unsupported \"+8 pp\" claim in experiments section (internal contradiction)\n- **7 Warnings**: metric mixing, imprecise multi-seed reporting, rounding inconsistencies\n- **5 Info**: acceptable rounding, resolved prior contradictions, ambiguous but defensible wording\n- The originally flagged Discussion/Limitations contradiction (\"+0.1pp\" vs \"+0.4pp\") **no longer exists** in current tex\n- Several issues from v1 audit (SciERC AUROC, WNUT VC ρ typo) appear to have been fixed\n\n---\n\n## ❌ CRITICAL\n\n### C1. Unsupported \"+8 pp\" LP-best claim on FewNERD\n\n**Location**: `experiments_main.tex:89`\n**Claim**: \"the optimal strategy is dataset-dependent (LP-best +8 pp on Few-NERD vs. MV +0.61 pp on CoNLL)\"\n**Internal contradiction** — three places in the same paper give different numbers:\n- Same file, `tab:fewnerd` (line 70): LP Δ = **+1.39 pp** on FewNERD\n- Same file, prescriptive §5 (line 107): LP-weighted construction = **+1.40 pp** on FewNERD\n- `adaptive.tex` method summary table (line 17): LP selection = **+1.39 pp (FN)**\n- Prescriptive footnote (line 107): non-degenerate subset construction = **+7.08 pp** (closest number, but different metric and still ≠ 8)\n\n**Registry verification**: No experiment yields +8pp from any LP-based method on FewNERD.\n- LP selection (exp_021_fewnerd_full, s42) = +1.36pp; 3-seed mean ≈ +1.38pp\n- Entity construction (exp_entity_construction, N=16 uniform) = +1.32pp\n\n**Likely cause**: Stale number from earlier framing revision (paper_framing.md also says \"+8pp\" in the strategy table, suggesting the error originated there and propagated to tex).\n\n**Fix**: Replace \"+8 pp\" with \"+1.39 pp\" (LP selection) or \"+1.40 pp\" (LP-weighted construction) in `experiments_main.tex:89`.\n\n---\n\n## ⚠️ WARNING\n\n### W1. Selection table metric mismatch (micro vs macro F1)\n\n**Location**: `single_signal.tex:12-30` (Table 2 / tab:selection)\n**Issue**: Table is titled \"Best-of-N selection (**macro** F1)\" and body shows Oracle=0.775, Greedy=0.645. Caption simultaneously states \"baselines: 3-seed (Oracle=**0.781**, Greedy=**0.667**)\" — these match **micro** F1 values from the registry.\n\n| Metric | Oracle | Greedy | Headroom |\n|--------|--------|--------|----------|\n| Macro (table body) | 0.775 | 0.645 | 13.0 pp |\n| Micro (caption text) | 0.781 | 0.667 | 11.4 pp |\n\nThe adjacent Figure 2 caption uses \"oracle headroom (+11.4 pp)\" — the micro-F1 headroom, not the macro-F1 headroom from the table it accompanies.\n\n**Risk**: Reviewer notices headroom 0.775−0.645=13.0pp ≠ 11.4pp stated in the figure.\n**Fix**: Either (a) remove micro baselines from caption, or (b) label explicitly: \"macro-F1 baselines in table; micro-F1 reference: Oracle=0.781, Greedy=0.667\".\n\n### W2. Limitations \"consistent negative\" across seeds\n\n**Location**: `limitations.tex:1`\n**Claim**: \"Δ_SC = −0.74±0.57 pp, consistent negative\"\n**Registry** (SciERC MV N=8, 3 seeds): s42=−0.74, s123=**+0.34**, s456=−0.84\n\nIssues:\n1. −0.74 is the s42 value, not the 3-seed mean (which is −0.41)\n2. ±0.57 doesn't match 3-seed std (≈0.64)\n3. \"Consistent negative\" is contradicted by s123=+0.34 (positive)\n\n**Fix**: Use 3-seed mean±std: \"Δ_SC = −0.41±0.64 pp\" and soften \"consistent negative\" to \"negative on average\".\n\n### W3. Epoch confound LP delta reporting\n\n**Location**: `experiments_main.tex:114`\n**Claim**: \"5-epoch training eliminates LP gains entirely (+1.39→+0.12±0.04 pp, 91% collapse)\"\n**Registry** (5-epoch FewNERD LP Δ, 3 seeds): s42=+0.07, s123=+0.09, s456=+0.12\n- 3-seed mean = **0.093**, not 0.12\n- 3-seed std ≈ **0.025**, not 0.04\n- Actual collapse = (1.39−0.093)/1.39 = **93.3%**, not 91%\n\nThe paper reports the maximum seed value (0.12) rather than the mean (0.093), with an inflated std.\n**Fix**: \"+1.39→+0.09±0.03 pp, 93% collapse\"\n\n### W4. WNUT-17 zero-F1 rate discrepancy\n\n**Location**: `experiments_main.tex:10`\n**Claim**: \"WNUT-17 (1,287 social media instances, 51% zero F1)\"\n**Registry** (exp_003_ner_wnut17): **53.7%** zero F1\n**v1 audit** also flagged internal inconsistency (51% vs 52% within paper).\n\n**Fix**: Verify the correct value and unify across all mentions.\n\n### W5. RE zero-F1 rounding\n\n**Location**: `introduction.tex:12`\n**Claim**: \"RE reveals a distinct bottleneck (40% zero-F1)\"\n**Registry** (exp_004_re_diagnostic): **43–47%** zero-F1 across configurations\n**paper_framing.md** also says \"43-47%\"\n\nUnderstated by 3–7pp.\n**Fix**: \"~45% zero-F1\" or \"43–47% zero-F1\".\n\n### W6. FewNERD table SciERC greedy F1\n\n**Location**: `experiments_main.tex:69` (tab:fewnerd, SciERC row)\n**Claim**: Greedy = .667 (labeled \"3-seed means\")\n**Registry**: s42=0.6617, s123=0.6633, s456=0.6631 → 3-seed mean = **0.6627**\n\n0.6627 rounds to 0.663, not 0.667. Discrepancy of 0.004.\n**Fix**: Change .667 to .663 (or verify if a different seed set or filtering yields .667).\n\n### W7. Discussion std ratio lower bound\n\n**Location**: `discussion.tex:6`\n**Claim**: \"LP std ratio 0.92–0.97×\"\n**Verification**: 0.97 confirmed (SciERC free-form ablation, exp_freeform_ablation). Source of 0.92 not found in registry.\n\n**Fix**: Verify 0.92 source and cite it, or narrow to \"≈0.97×\".\n\n---\n\n## ℹ️ INFO (no action needed)\n\n### I1. Original Discussion/Limitations contradiction — RESOLVED\n\nThe task flagged: Discussion \"+0.1pp over single-sample\" vs Limitations \"+0.4pp over greedy\". These phrases **do not appear** in the current tex. The contradiction has been fixed in a prior revision.\n\n### I2. Acceptable rounding throughout\n\n| Claim | Source | Rounding |\n|-------|--------|----------|\n| \"AUROC up to 0.82\" | EM CoNLL Qwen = 0.816 | ✅ standard |\n| \"ρ up to 0.45\" | EM CoNLL Qwen = 0.451 | ✅ conservative |\n| \"MV +0.6 pp at N=64\" | Registry s42 = +0.64 | ✅ |\n| \"degeneracy 12–68%\" | SciERC 12.2%, WNUT 67.9% | ✅ |\n| \"AUROC 0.63–0.88\" probes | GroupKFold: 0.634–0.885 | ✅ |\n| \"probe 0.88 vs self-judgment 0.51\" | CoNLL probe 0.885, ESJ 0.512 | ✅ |\n\n### I3. Dataset instance counts: total vs evaluated (consistent)\n\n- FewNERD: 37,648 (setup) vs 32,565 (tab:fewnerd) — gold-filtering\n- CoNLL: 3,453 (setup) vs 2,756 (evaluation) — gold-filtering\n- SciERC: 551 (setup) vs 529 (evaluation) — gold-filtering\nAll consistent with stated filtering methodology.\n\n### I4. Abstract \"<1 pp\" ambiguity\n\n\"instance-level selection yields <1 pp\" — FewNERD LP gives +1.39pp, but LP is a **per-sample** signal, not instance-level. The paper carefully defines \"instance-level\" signals as those producing one score per input (4 of 5 signals). Under this definition, the claim is correct. A casual reader might misinterpret \"instance-level selection\" as \"selection at the instance level.\"\n\n### I5. v1 audit issues — status\n\nSeveral issues from the 2026-05-19 v1 audit appear resolved in current tex:\n- SciERC AUROC values in Table 1 now match registry (previously had systematic offset)\n- The 0.82 AUROC claim remains valid (CoNLL EM 0.816)\n\nIssues potentially still present from v1 (could not fully verify due to appendix size):\n- CoNLL LP Δ mismatch between Table 3 and Appendix cross-selection table (−0.85 vs −1.1pp)\n- FewNERD degeneracy 13.0% in tab:fewnerd vs registry individual seeds (10.1–13.1%); 3-seed mean ≈ 11.8%. Paper shows 13.0% which could be seed 123 alone.\n\n---\n\n## Cross-Chapter Consistency Matrix\n\n| Claim | Abstract | Intro | Experiments | Discussion | Limitations | Conclusion |\n|-------|----------|-------|-------------|------------|-------------|------------|\n| AUROC ≤0.82 | 0.82 ✅ | 0.82 ✅ | Tab: 0.816 ✅ | — | — | — |\n| ρ ≤0.45 | — | 0.45 ✅ | Tab: 0.451 ✅ | — | — | — |\n| Selection <1pp | <1pp ✅ | <1pp ✅ | Tab confirms ✅ | <1pp ✅ | — | <1pp ✅ |\n| FN LP sel +1.39pp | — | +1.39 ✅ | +1.39 (tab) ✅ | — | — | — |\n| FN constr +1.40pp | +1.40 ✅ | +1.40 ✅ | +1.40±0.51 ✅ | — | +1–1.4 ✅ | +0.32–1.40 ✅ |\n| Holm p=0.055 | 0.055 ✅ | — | 0.055 ✅ | — | 0.055 ✅ | — |\n| Degeneracy range | — | 12–68% ✅ | Tab: 12.2–67.9% ✅ | 12–68% ✅ | — | — |\n| Inverse scaling 69% | 69% ✅ | 69% ✅ | 40/58=69% ✅ | — | — | — |\n| SQL degen 87.2% | — | 87.2% ✅ | — | — | — | — |\n| **LP-best +8pp FN** | — | — | **❌ vs +1.39** | — | — | — |\n\n---\n\n## Verified Claims (spot-check, 37 claims)\n\n| # | Location | Claim | Source | Status |\n|---|----------|-------|--------|--------|\n| 1 | abstract:4 | AUROC up to 0.82 | EM CoNLL Qwen AUROC=0.816 | ✅ |\n| 2 | abstract:6 | +1.40pp FewNERD construction | prescriptive §5 +1.40±0.51 | ✅ |\n| 3 | abstract:6 | Holm p_adj=0.055 | prescriptive §5 k=57 Holm | ✅ |\n| 4 | abstract:6 | 69% inverse scaling | theory: 40/58=68.97% | ✅ |\n| 5 | intro:7 | ρ up to 0.45 | EM CoNLL Qwen ρ=0.451 | ✅ |\n| 6 | intro:9 | probe AUROC 0.63–0.88 | GroupKFold: 0.634–0.885 | ✅ |\n| 7 | intro:9 | ESJ AUROC 0.51 | exp ESJ AUROC=0.512 | ✅ |\n| 8 | intro:12 | LP +1.39pp FewNERD | exp_021 s42=+1.36, 3-seed≈1.38 | ✅ ~approx |\n| 9 | intro:12 | MV +0.61pp CoNLL | N=64 s42=+0.64, multi-seed≈0.61 | ✅ ~approx |\n| 10 | intro:16 | SQL 87.2% degeneracy | exp_spider_sc_pilot=87.2% | ✅ |\n| 11 | exp:7 | SciERC 551 test, 6 types | dataset spec | ✅ |\n| 12 | exp:9 | CoNLL ≈91% F1 | registry greedy=0.9123 | ✅ |\n| 13 | exp:19 | MV +0.6pp CoNLL N=64 | registry s42=+0.64 | ✅ |\n| 14 | exp:75 | 5-epoch degen 31% | exp_028=31.3% | ✅ |\n| 15 | exp:107 | +0.32pp SciERC constr | prescriptive LP-weighted N=8 | ✅ internal |\n| 16 | exp:107 | –0.39pp CoNLL constr | prescriptive LP-weighted N=8 | ✅ internal |\n| 17 | exp:108 | k=57 Holm correction | consistent count | ✅ |\n| 18 | exp:116 | 5-epoch entity-set degen 26%/9% | consistent with body text | ✅ |\n| 19 | adaptive:33 | cross-model +0.42pp FN | exp_cross_model=+0.42pp p<0.001 | ✅ |\n| 20 | adaptive:38 | LGB AUC=0.923 | consistent with exp_b2 | ✅ |\n| 21 | adaptive:38 | +0.30pp overall verifier | exp_b2 OOF delta=+0.30pp | ✅ |\n| 22 | mech:9 | ESJ P(yes\\|correct)=0.500 | registry AUROC≈0.5 | ✅ |\n| 23 | mech:14 | MRSC best F1=0.763 | 0.794−0.763=−3.1pp | ✅ |\n| 24 | mech:18 | LSC centroid=0.759 | 0.794−0.759=−3.5pp | ✅ |\n| 25 | mech:21 | probe AUROC 0.636/0.882/0.630 | GroupKFold: 0.651/0.885/0.634 | ✅ ~approx |\n| 26 | mech:23 | LODO 0.559, 0.671 | consistent with probe data | ✅ |\n| 27 | theory:7 | LP advantage +1.5→+4.6pp (ε) | internal consistency | ✅ |\n| 28 | theory:12 | GPT-5.5 50% degen | frontier: GPT-5.5=50% | ✅ |\n| 29 | theory:13 | Qwen2.5 31.7–46.2% | registry confirms | ✅ |\n| 30 | theory:28 | α=0.000–0.161, 8–33× tighter | arithmetic consistent | ✅ |\n| 31 | disc:4 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |\n| 32 | disc:6 | std ratio 0.97× | exp_freeform=0.97 | ✅ |\n| 33 | disc:14 | GPT-5.5 50%, Qwen3 13% | frontier+registry | ✅ |\n| 34 | disc:14 | Claude Sonnet 4 74% | frontier data | ✅ |\n| 35 | lim:2 | BH FDR 19/57 at <0.05 | consistent with k=57 | ✅ |\n| 36 | lim:3 | +1–1.4pp construction cost | +0.32 SciERC, +1.40 FN | ✅ |\n| 37 | concl:3 | +0.32–1.40pp constr gains | SciERC +0.32, FN +1.40 | ✅ |\n\n---\n\n## Priority Action Items\n\n| Priority | Issue | File:Line | Fix |\n|----------|-------|-----------|-----|\n| **P0** | ❌ \"+8 pp\" LP-best unsupported | experiments_main.tex:89 | → \"+1.39 pp\" (selection) or \"+1.40 pp\" (construction) |\n| **P1** | ⚠️ Tab:selection micro/macro mismatch | single_signal.tex:12 | Remove micro baselines from caption or label explicitly |\n| **P1** | ⚠️ Limitations Δ_SC numbers | limitations.tex:1 | Use 3-seed mean (−0.41±0.64), soften \"consistent negative\" |\n| **P1** | ⚠️ Epoch confound LP delta | experiments_main.tex:114 | +0.12→+0.09 (mean), ±0.04→±0.03, 91%→93% |\n| **P2** | ⚠️ WNUT zero-F1 (51% vs 53.7%) | experiments_main.tex:10 | Verify and unify |\n| **P2** | ⚠️ RE zero-F1 (40% vs 43-47%) | introduction.tex:12 | → \"~45%\" or \"43-47%\" |\n| **P2** | ⚠️ SciERC greedy (.667 vs .663) | experiments_main.tex:69 | Verify 3-seed calculation |\n| **P2** | ⚠️ std ratio 0.92 source | discussion.tex:6 | Verify or narrow range |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 260,
        "newStart": 1,
        "newLines": 233,
        "lines": [
          "-# Claim Audit Report — struct_self_consist_ie",
          "+# Claim Audit Report — struct_self_consist_ie (v2)",
          " ",
          "-**Date**: 2026-05-19  ",
          "-**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  ",
          "+**Date**: 2026-05-22 (supersedes v1 from 2026-05-19)",
          "+**Scope**: All quantitative claims in `docs/paper/sections/*.tex` cross-verified against experiment registry and paper_framing.md",
          " **Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.",
          " ",
          " ---",
          " ",
          "-## ❌ Inconsistencies Requiring Fix",
          "+## Executive Summary",
          " ",
          "-### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)",
          "+- **1 Critical**: unsupported \"+8 pp\" claim in experiments section (internal contradiction)",
          "+- **7 Warnings**: metric mixing, imprecise multi-seed reporting, rounding inconsistencies",
          "+- **5 Info**: acceptable rounding, resolved prior contradictions, ambiguous but defensible wording",
          "+- The originally flagged Discussion/Limitations contradiction (\"+0.1pp\" vs \"+0.4pp\") **no longer exists** in current tex",
          "+- Several issues from v1 audit (SciERC AUROC, WNUT VC ρ typo) appear to have been fixed",
          " ",
          "-| Location | Value |",
          "-|----------|-------|",
          "-| experiments.tex:48 | VC ρ=0.724 |",
          "-| experiments.tex:104 | VC ρ=0.730 |",
          "-| appendix.tex:217 (tab:wnut) | VC .724 |",
          "-| appendix.tex:226 | VC ρ=0.724 |",
          "+---",
          " ",
          "-**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  ",
          "-**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.",
          "+## ❌ CRITICAL",
          " ",
          "-### 2. SciERC AUROC in Table 1 vs registry (systematic offset)",
          "+### C1. Unsupported \"+8 pp\" LP-best claim on FewNERD",
          " ",
          "-Paper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):",
          "+**Location**: `experiments_main.tex:89`",
          "+**Claim**: \"the optimal strategy is dataset-dependent (LP-best +8 pp on Few-NERD vs. MV +0.61 pp on CoNLL)\"",
          "+**Internal contradiction** — three places in the same paper give different numbers:",
          "+- Same file, `tab:fewnerd` (line 70): LP Δ = **+1.39 pp** on FewNERD",
          "+- Same file, prescriptive §5 (line 107): LP-weighted construction = **+1.40 pp** on FewNERD",
          "+- `adaptive.tex` method summary table (line 17): LP selection = **+1.39 pp (FN)**",
          "+- Prescriptive footnote (line 107): non-degenerate subset construction = **+7.08 pp** (closest number, but different metric and still ≠ 8)",
          " ",
          "-| Signal | Paper AUC | Registry AUROC | Δ |",
          "-|--------|-----------|---------------|-----|",
          "-| VC | .663 | .684 | -2.1pp |",
          "-| SJ | .650 | .692 | -4.2pp |",
          "-| FK | .602 | .629 | -2.7pp |",
          "-| EM | .614 | .749 | **-13.5pp** |",
          "-| LP | .578 | .578 | 0pp |",
          "+**Registry verification**: No experiment yields +8pp from any LP-based method on FewNERD.",
          "+- LP selection (exp_021_fewnerd_full, s42) = +1.36pp; 3-seed mean ≈ +1.38pp",
          "+- Entity construction (exp_entity_construction, N=16 uniform) = +1.32pp",
          " ",
          "-ρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.",
          "+**Likely cause**: Stale number from earlier framing revision (paper_framing.md also says \"+8pp\" in the strategy table, suggesting the error originated there and propagated to tex).",
          " ",
          "-**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  ",
          "-**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:",
          "-- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)",
          "-- But SciERC EM AUROC should be ~0.749, not 0.614",
          "+**Fix**: Replace \"+8 pp\" with \"+1.39 pp\" (LP selection) or \"+1.40 pp\" (LP-weighted construction) in `experiments_main.tex:89`.",
          " ",
          "-### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table",
          "-",
          "-| Source | Greedy | LP F1 | LP Δ |",
          "-|--------|--------|-------|------|",
          "-| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |",
          "-| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |",
          "-",
          "-Both claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  ",
          "-**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.",
          "-",
          "-### 4. WNUT-17 zero-F1 rate inconsistency within paper",
          "-",
          "-| Location | Value |",
          "-|----------|-------|",
          "-| experiments.tex:12 (dataset description) | \"52% zero F1\" |",
          "-| experiments.tex:103 | \"51% of instances yield F1=0\" |",
          "-| limitations.tex:3 | \"51% F1=0\" |",
          "-",
          "-**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.",
          "-",
          " ---",
          " ",
          "-## ⚠️ Ambiguous/Unverifiable Claims",
          "+## ⚠️ WARNING",
          " ",
          "-### 5. \"13–87% degeneracy\" in Introduction (line 15)",
          "+### W1. Selection table metric mismatch (micro vs macro F1)",
          " ",
          "-The introduction says \"instance degeneracy (13–87% across our benchmarks).\"",
          "+**Location**: `single_signal.tex:12-30` (Table 2 / tab:selection)",
          "+**Issue**: Table is titled \"Best-of-N selection (**macro** F1)\" and body shows Oracle=0.775, Greedy=0.645. Caption simultaneously states \"baselines: 3-seed (Oracle=**0.781**, Greedy=**0.667**)\" — these match **micro** F1 values from the registry.",
          " ",
          "-- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓",
          "-- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark",
          "+| Metric | Oracle | Greedy | Headroom |",
          "+|--------|--------|--------|----------|",
          "+| Macro (table body) | 0.775 | 0.645 | 13.0 pp |",
          "+| Micro (caption text) | 0.781 | 0.667 | 11.4 pp |",
          " ",
          "-The appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).",
          "+The adjacent Figure 2 caption uses \"oracle headroom (+11.4 pp)\" — the micro-F1 headroom, not the macro-F1 headroom from the table it accompanies.",
          " ",
          "-**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  ",
          "-**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".",
          "+**Risk**: Reviewer notices headroom 0.775−0.645=13.0pp ≠ 11.4pp stated in the figure.",
          "+**Fix**: Either (a) remove micro baselines from caption, or (b) label explicitly: \"macro-F1 baselines in table; micro-F1 reference: Oracle=0.781, Greedy=0.667\".",
          " ",
          "-### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3",
          "+### W2. Limitations \"consistent negative\" across seeds",
          " ",
          "-Table 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.",
          "+**Location**: `limitations.tex:1`",
          "+**Claim**: \"Δ_SC = −0.74±0.57 pp, consistent negative\"",
          "+**Registry** (SciERC MV N=8, 3 seeds): s42=−0.74, s123=**+0.34**, s456=−0.84",
          " ",
          "-But `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.",
          "+Issues:",
          "+1. −0.74 is the s42 value, not the 3-seed mean (which is −0.41)",
          "+2. ±0.57 doesn't match 3-seed std (≈0.64)",
          "+3. \"Consistent negative\" is contradicted by s123=+0.34 (positive)",
          " ",
          "-Registry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).",
          "+**Fix**: Use 3-seed mean±std: \"Δ_SC = −0.41±0.64 pp\" and soften \"consistent negative\" to \"negative on average\".",
          " ",
          "-No N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.",
          "+### W3. Epoch confound LP delta reporting",
          " ",
          "-**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  ",
          "-**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.",
          "+**Location**: `experiments_main.tex:114`",
          "+**Claim**: \"5-epoch training eliminates LP gains entirely (+1.39→+0.12±0.04 pp, 91% collapse)\"",
          "+**Registry** (5-epoch FewNERD LP Δ, 3 seeds): s42=+0.07, s123=+0.09, s456=+0.12",
          "+- 3-seed mean = **0.093**, not 0.12",
          "+- 3-seed std ≈ **0.025**, not 0.04",
          "+- Actual collapse = (1.39−0.093)/1.39 = **93.3%**, not 91%",
          " ",
          "-### 7. FewNERD degeneracy 13.8% vs registry data",
          "+The paper reports the maximum seed value (0.12) rather than the mean (0.093), with an inflated std.",
          "+**Fix**: \"+1.39→+0.09±0.03 pp, 93% collapse\"",
          " ",
          "-Paper Table 3: FewNERD degen = 13.8%.",
          "+### W4. WNUT-17 zero-F1 rate discrepancy",
          " ",
          "-Registry individual seeds (all N=8):",
          "-- Seed 42 (exp_021_fewnerd_full): 10.1%",
          "-- Seed 123: 13.1%",
          "-- Seed 456: 12.1%",
          "-- Seed 789: 11.8%",
          "+**Location**: `experiments_main.tex:10`",
          "+**Claim**: \"WNUT-17 (1,287 social media instances, 51% zero F1)\"",
          "+**Registry** (exp_003_ner_wnut17): **53.7%** zero F1",
          "+**v1 audit** also flagged internal inconsistency (51% vs 52% within paper).",
          " ",
          "-3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  ",
          "-4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%",
          "+**Fix**: Verify the correct value and unify across all mentions.",
          " ",
          "-**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.",
          "+### W5. RE zero-F1 rounding",
          " ",
          "-### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422",
          "+**Location**: `introduction.tex:12`",
          "+**Claim**: \"RE reveals a distinct bottleneck (40% zero-F1)\"",
          "+**Registry** (exp_004_re_diagnostic): **43–47%** zero-F1 across configurations",
          "+**paper_framing.md** also says \"43-47%\"",
          " ",
          "-Table 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.",
          "+Understated by 3–7pp.",
          "+**Fix**: \"~45% zero-F1\" or \"43–47% zero-F1\".",
          " ",
          "-This implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.",
          "+### W6. FewNERD table SciERC greedy F1",
          " ",
          "-**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  ",
          "-**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.",
          "+**Location**: `experiments_main.tex:69` (tab:fewnerd, SciERC row)",
          "+**Claim**: Greedy = .667 (labeled \"3-seed means\")",
          "+**Registry**: s42=0.6617, s123=0.6633, s456=0.6631 → 3-seed mean = **0.6627**",
          " ",
          "-### 9. WNUT LP ρ: paper -0.446 vs registry -0.410",
          "+0.6627 rounds to 0.663, not 0.667. Discrepancy of 0.004.",
          "+**Fix**: Change .667 to .663 (or verify if a different seed set or filtering yields .667).",
          " ",
          "-Paper Table 3: LP ρ = -.446 (claimed N=8).  ",
          "-Registry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  ",
          "-Registry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.",
          "+### W7. Discussion std ratio lower bound",
          " ",
          "-Different N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.",
          "+**Location**: `discussion.tex:6`",
          "+**Claim**: \"LP std ratio 0.92–0.97×\"",
          "+**Verification**: 0.97 confirmed (SciERC free-form ablation, exp_freeform_ablation). Source of 0.92 not found in registry.",
          " ",
          "-### 10. Entity construction Δ: paper vs registry (protocol mismatch)",
          "+**Fix**: Verify 0.92 source and cite it, or narrow to \"≈0.97×\".",
          " ",
          "-Paper (multi-seed mean) vs registry (5-fold CV):",
          "-",
          "-| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |",
          "-|---------|-----------|--------------|-------------|----------------|",
          "-| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |",
          "-| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |",
          "-| CoNLL | -0.39pp | -0.39pp | — | — |",
          "-",
          "-Large differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.",
          "-",
          "-**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  ",
          "-**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.",
          "-",
          " ---",
          " ",
          "-## ⚠️ Known Contradiction (from task description)",
          "+## ℹ️ INFO (no action needed)",
          " ",
          "-**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**",
          "+### I1. Original Discussion/Limitations contradiction — RESOLVED",
          " ",
          "-**Status**: Not found in current paper text.",
          "+The task flagged: Discussion \"+0.1pp over single-sample\" vs Limitations \"+0.4pp over greedy\". These phrases **do not appear** in the current tex. The contradiction has been fixed in a prior revision.",
          " ",
          "-The closest matches are:",
          "-- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.",
          "-- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.",
          "-- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.",
          "+### I2. Acceptable rounding throughout",
          " ",
          "-**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.",
          "+| Claim | Source | Rounding |",
          "+|-------|--------|----------|",
          "+| \"AUROC up to 0.82\" | EM CoNLL Qwen = 0.816 | ✅ standard |",
          "+| \"ρ up to 0.45\" | EM CoNLL Qwen = 0.451 | ✅ conservative |",
          "+| \"MV +0.6 pp at N=64\" | Registry s42 = +0.64 | ✅ |",
          "+| \"degeneracy 12–68%\" | SciERC 12.2%, WNUT 67.9% | ✅ |",
          "+| \"AUROC 0.63–0.88\" probes | GroupKFold: 0.634–0.885 | ✅ |",
          "+| \"probe 0.88 vs self-judgment 0.51\" | CoNLL probe 0.885, ESJ 0.512 | ✅ |",
          " ",
          "----",
          "+### I3. Dataset instance counts: total vs evaluated (consistent)",
          " ",
          "-## ✅ Verified Claims",
          "+- FewNERD: 37,648 (setup) vs 32,565 (tab:fewnerd) — gold-filtering",
          "+- CoNLL: 3,453 (setup) vs 2,756 (evaluation) — gold-filtering",
          "+- SciERC: 551 (setup) vs 529 (evaluation) — gold-filtering",
          "+All consistent with stated filtering methodology.",
          " ",
          "-### Abstract & Introduction",
          "-| Claim | Source | Registry/Verified Value | Status |",
          "-|-------|--------|------------------------|--------|",
          "-| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |",
          "-| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |",
          "-| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |",
          "-| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |",
          "-| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |",
          "-| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |",
          "-| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |",
          "+### I4. Abstract \"<1 pp\" ambiguity",
          " ",
          "-### Table 1 (QE) — Spearman ρ",
          "-| Signal | Paper | Registry (exp_012_rerun_1024) | Status |",
          "-|--------|-------|-------------------------------|--------|",
          "-| SciERC VC ρ | .379 | 0.3792 | ✅ |",
          "-| SciERC SJ ρ | .360 | 0.3599 | ✅ |",
          "-| SciERC FK ρ | .267 | 0.2665 | ✅ |",
          "-| SciERC EM ρ | .295 | 0.2945 | ✅ |",
          "-| SciERC LP ρ | .205 | 0.2052 | ✅ |",
          "-| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |",
          "-| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |",
          "-| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |",
          "+\"instance-level selection yields <1 pp\" — FewNERD LP gives +1.39pp, but LP is a **per-sample** signal, not instance-level. The paper carefully defines \"instance-level\" signals as those producing one score per input (4 of 5 signals). Under this definition, the claim is correct. A casual reader might misinterpret \"instance-level selection\" as \"selection at the instance level.\"",
          " ",
          "-### Table 2 (SciERC Selection)",
          "-| Method | Paper | Notes | Status |",
          "-|--------|-------|-------|--------|",
          "-| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |",
          "-| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |",
          "-| LP | .647±.005 | 2-seed mean | ✅ |",
          "-| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |",
          "+### I5. v1 audit issues — status",
          " ",
          "-### Table 3 (Cross-dataset)",
          "-| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |",
          "-|---------|--------|-------|------|------|--------|",
          "-| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |",
          "-| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |",
          "-| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |",
          "-| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |",
          "+Several issues from the 2026-05-19 v1 audit appear resolved in current tex:",
          "+- SciERC AUROC values in Table 1 now match registry (previously had systematic offset)",
          "+- The 0.82 AUROC claim remains valid (CoNLL EM 0.816)",
          " ",
          "-### Scale Ablation (Table in experiments.tex)",
          "-| Metric | Paper | Registry | Status |",
          "-|--------|-------|----------|--------|",
          "-| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |",
          "-| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |",
          "-| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |",
          "-| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |",
          "-| SciERC 8B degen | 17.8% | 0.1777 | ✅ |",
          "-| SciERC 4B degen | 10.4% | 0.104 | ✅ |",
          "+Issues potentially still present from v1 (could not fully verify due to appendix size):",
          "+- CoNLL LP Δ mismatch between Table 3 and Appendix cross-selection table (−0.85 vs −1.1pp)",
          "+- FewNERD degeneracy 13.0% in tab:fewnerd vs registry individual seeds (10.1–13.1%); 3-seed mean ≈ 11.8%. Paper shows 13.0% which could be seed 123 alone.",
          " ",
          "-### 72B Zero-shot (Table in experiments.tex)",
          "-| Metric | Paper | Source | Status |",
          "-|--------|-------|--------|--------|",
          "-| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |",
          "-| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |",
          "-| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |",
          "-| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |",
          "+---",
          " ",
          "-Note: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.",
          "+## Cross-Chapter Consistency Matrix",
          " ",
          "-### LoRA Rank Ablation",
          "-| Metric | Paper | Registry (exp_023_lora_rank8) | Status |",
          "-|--------|-------|-------------------------------|--------|",
          "-| Rank=8 degen | 7.2% | 0.072 | ✅ |",
          "-| VC ρ | .394 (text) | 0.394 | ✅ |",
          "-| SJ ρ | .365 (text) | 0.3649 | ✅ |",
          "+| Claim | Abstract | Intro | Experiments | Discussion | Limitations | Conclusion |",
          "+|-------|----------|-------|-------------|------------|-------------|------------|",
          "+| AUROC ≤0.82 | 0.82 ✅ | 0.82 ✅ | Tab: 0.816 ✅ | — | — | — |",
          "+| ρ ≤0.45 | — | 0.45 ✅ | Tab: 0.451 ✅ | — | — | — |",
          "+| Selection <1pp | <1pp ✅ | <1pp ✅ | Tab confirms ✅ | <1pp ✅ | — | <1pp ✅ |",
          "+| FN LP sel +1.39pp | — | +1.39 ✅ | +1.39 (tab) ✅ | — | — | — |",
          "+| FN constr +1.40pp | +1.40 ✅ | +1.40 ✅ | +1.40±0.51 ✅ | — | +1–1.4 ✅ | +0.32–1.40 ✅ |",
          "+| Holm p=0.055 | 0.055 ✅ | — | 0.055 ✅ | — | 0.055 ✅ | — |",
          "+| Degeneracy range | — | 12–68% ✅ | Tab: 12.2–67.9% ✅ | 12–68% ✅ | — | — |",
          "+| Inverse scaling 69% | 69% ✅ | 69% ✅ | 40/58=69% ✅ | — | — | — |",
          "+| SQL degen 87.2% | — | 87.2% ✅ | — | — | — | — |",
          "+| **LP-best +8pp FN** | — | — | **❌ vs +1.39** | — | — | — |",
          " ",
          "-### Other Verified Claims",
          "-| Claim | Source | Status |",
          "-|-------|--------|--------|",
          "-| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |",
          "-| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |",
          "-| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |",
          "-| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |",
          "-| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |",
          "-| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |",
          "-| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |",
          "+---",
          " ",
          "-### Abstract LP CI discrepancy",
          "-Abstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅",
          "+## Verified Claims (spot-check, 37 claims)",
          " ",
          "-But the **bootstrap CI** for FewNERD LP selection:",
          "-- Abstract: implied from \"p<0.005\"",
          "-- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]",
          "-- Paper Table 3: not shown explicitly",
          "-- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)",
          "+| # | Location | Claim | Source | Status |",
          "+|---|----------|-------|--------|--------|",
          "+| 1 | abstract:4 | AUROC up to 0.82 | EM CoNLL Qwen AUROC=0.816 | ✅ |",
          "+| 2 | abstract:6 | +1.40pp FewNERD construction | prescriptive §5 +1.40±0.51 | ✅ |",
          "+| 3 | abstract:6 | Holm p_adj=0.055 | prescriptive §5 k=57 Holm | ✅ |",
          "+| 4 | abstract:6 | 69% inverse scaling | theory: 40/58=68.97% | ✅ |",
          "+| 5 | intro:7 | ρ up to 0.45 | EM CoNLL Qwen ρ=0.451 | ✅ |",
          "+| 6 | intro:9 | probe AUROC 0.63–0.88 | GroupKFold: 0.634–0.885 | ✅ |",
          "+| 7 | intro:9 | ESJ AUROC 0.51 | exp ESJ AUROC=0.512 | ✅ |",
          "+| 8 | intro:12 | LP +1.39pp FewNERD | exp_021 s42=+1.36, 3-seed≈1.38 | ✅ ~approx |",
          "+| 9 | intro:12 | MV +0.61pp CoNLL | N=64 s42=+0.64, multi-seed≈0.61 | ✅ ~approx |",
          "+| 10 | intro:16 | SQL 87.2% degeneracy | exp_spider_sc_pilot=87.2% | ✅ |",
          "+| 11 | exp:7 | SciERC 551 test, 6 types | dataset spec | ✅ |",
          "+| 12 | exp:9 | CoNLL ≈91% F1 | registry greedy=0.9123 | ✅ |",
          "+| 13 | exp:19 | MV +0.6pp CoNLL N=64 | registry s42=+0.64 | ✅ |",
          "+| 14 | exp:75 | 5-epoch degen 31% | exp_028=31.3% | ✅ |",
          "+| 15 | exp:107 | +0.32pp SciERC constr | prescriptive LP-weighted N=8 | ✅ internal |",
          "+| 16 | exp:107 | –0.39pp CoNLL constr | prescriptive LP-weighted N=8 | ✅ internal |",
          "+| 17 | exp:108 | k=57 Holm correction | consistent count | ✅ |",
          "+| 18 | exp:116 | 5-epoch entity-set degen 26%/9% | consistent with body text | ✅ |",
          "+| 19 | adaptive:33 | cross-model +0.42pp FN | exp_cross_model=+0.42pp p<0.001 | ✅ |",
          "+| 20 | adaptive:38 | LGB AUC=0.923 | consistent with exp_b2 | ✅ |",
          "+| 21 | adaptive:38 | +0.30pp overall verifier | exp_b2 OOF delta=+0.30pp | ✅ |",
          "+| 22 | mech:9 | ESJ P(yes\\|correct)=0.500 | registry AUROC≈0.5 | ✅ |",
          "+| 23 | mech:14 | MRSC best F1=0.763 | 0.794−0.763=−3.1pp | ✅ |",
          "+| 24 | mech:18 | LSC centroid=0.759 | 0.794−0.759=−3.5pp | ✅ |",
          "+| 25 | mech:21 | probe AUROC 0.636/0.882/0.630 | GroupKFold: 0.651/0.885/0.634 | ✅ ~approx |",
          "+| 26 | mech:23 | LODO 0.559, 0.671 | consistent with probe data | ✅ |",
          "+| 27 | theory:7 | LP advantage +1.5→+4.6pp (ε) | internal consistency | ✅ |",
          "+| 28 | theory:12 | GPT-5.5 50% degen | frontier: GPT-5.5=50% | ✅ |",
          "+| 29 | theory:13 | Qwen2.5 31.7–46.2% | registry confirms | ✅ |",
          "+| 30 | theory:28 | α=0.000–0.161, 8–33× tighter | arithmetic consistent | ✅ |",
          "+| 31 | disc:4 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |",
          "+| 32 | disc:6 | std ratio 0.97× | exp_freeform=0.97 | ✅ |",
          "+| 33 | disc:14 | GPT-5.5 50%, Qwen3 13% | frontier+registry | ✅ |",
          "+| 34 | disc:14 | Claude Sonnet 4 74% | frontier data | ✅ |",
          "+| 35 | lim:2 | BH FDR 19/57 at <0.05 | consistent with k=57 | ✅ |",
          "+| 36 | lim:3 | +1–1.4pp construction cost | +0.32 SciERC, +1.40 FN | ✅ |",
          "+| 37 | concl:3 | +0.32–1.40pp constr gains | SciERC +0.32, FN +1.40 | ✅ |",
          " ",
          "-The CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.",
          "-",
          " ---",
          " ",
          "-## Summary of Required Actions",
          "+## Priority Action Items",
          " ",
          "-| Priority | Issue | Action |",
          "-|----------|-------|--------|",
          "-| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |",
          "-| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |",
          "-| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |",
          "-| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |",
          "-| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |",
          "-| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |",
          "-| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |",
          "-| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |",
          "-| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |",
          "-| **INFO** | Known contradiction from task | Not found in current version; appears resolved |",
          "+| Priority | Issue | File:Line | Fix |",
          "+|----------|-------|-----------|-----|",
          "+| **P0** | ❌ \"+8 pp\" LP-best unsupported | experiments_main.tex:89 | → \"+1.39 pp\" (selection) or \"+1.40 pp\" (construction) |",
          "+| **P1** | ⚠️ Tab:selection micro/macro mismatch | single_signal.tex:12 | Remove micro baselines from caption or label explicitly |",
          "+| **P1** | ⚠️ Limitations Δ_SC numbers | limitations.tex:1 | Use 3-seed mean (−0.41±0.64), soften \"consistent negative\" |",
          "+| **P1** | ⚠️ Epoch confound LP delta | experiments_main.tex:114 | +0.12→+0.09 (mean), ±0.04→±0.03, 91%→93% |",
          "+| **P2** | ⚠️ WNUT zero-F1 (51% vs 53.7%) | experiments_main.tex:10 | Verify and unify |",
          "+| **P2** | ⚠️ RE zero-F1 (40% vs 43-47%) | introduction.tex:12 | → \"~45%\" or \"43-47%\" |",
          "+| **P2** | ⚠️ SciERC greedy (.667 vs .663) | experiments_main.tex:69 | Verify 3-seed calculation |",
          "+| **P2** | ⚠️ std ratio 0.92 source | discussion.tex:6 | Verify or narrow range |"
        ]
      }
    ],
    "originalFile": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n",
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 140_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d406a59f-6319-48c3-a8fa-3ad8f323e12d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jp88WLbX1HrcXJZosrHpqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5920,
      "cache_read_input_tokens": 99452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5920
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01QT84Tsyj3rQ1wRbneX6KoY`</summary>

```json
{
  "name": "claim_audit_report_v2",
  "type": "report",
  "description": "Full quantitative claim audit (v2, 2026-05-22): 1 Critical (+8pp unsupported), 7 Warnings, 37 verified claims. Supersedes v1 from 2026-05-19.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_024_claim_audit",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "tags": [
    "claim-audit",
    "paper-quality",
    "DDL-sprint"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "e6b8975c-4b06-40b9-b265-7b17e690aba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jp88WLbX1HrcXJZosrHpqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5920,
      "cache_read_input_tokens": 99452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5920
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-22T18:34:43.801Z_

<details><summary>↩ Tool result · `toolu_01QT84Tsyj3rQ1wRbneX6KoY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_59e546\", \"name\": \"claim_audit_report_v2\", \"type\": \"report\", \"description\": \"Full quantitative claim audit (v2, 2026-05-22): 1 Critical (+8pp unsupported), 7 Warnings, 37 verified claims. Supersedes v1 from 2026-05-19.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report_59e546.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_024_claim_audit\", \"skill\": \"\", \"created_at\": \"2026-05-22T18:34:43.042046+00:00\", \"tags\": [\"claim-audit\", \"paper-quality\", \"DDL-sprint\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "5cfcafa0-67be-487a-ab11-b48734b55820",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_59e546\\\", \\\"name\\\": \\\"claim_audit_report_v2\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full quantitative claim audit (v2, 2026-05-22): 1 Critical (+8pp unsupported), 7 Warnings, 37 verified claims. Supersedes v1 from 2026-05-19.\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report_59e546.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_024_claim_audit\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T18:34:43.042046+00:00\\\", \\\"tags\\\": [\\\"claim-audit\\\", \\\"paper-quality\\\", \\\"DDL-sprint\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_59e546\", \"name\": \"claim_audit_report_v2\", \"type\": \"report\", \"description\": \"Full quantitative claim audit (v2, 2026-05-22): 1 Critical (+8pp unsupported), 7 Warnings, 37 verified claims. Supersedes v1 from 2026-05-19.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report_59e546.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_024_claim_audit\", \"skill\": \"\", \"created_at\": \"2026-05-22T18:34:43.042046+00:00\", \"tags\": [\"claim-audit\", \"paper-quality\", \"DDL-sprint\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 143_

Audit complete. Key findings:

**❌ Critical (1)**: `experiments_main.tex:89` claims "LP-best +8 pp on Few-NERD" — no data supports this. The same paper says +1.39pp (LP selection) and +1.40pp (LP construction) in three other locations. Must fix before submission.

**⚠️ Warning (7)**:
1. Selection table mixes micro/macro F1 baselines in caption vs body (11.4pp vs 13.0pp headroom)
2. Limitations "Δ_SC = −0.74±0.57 pp, consistent negative" — uses single-seed value, not 3-seed mean; one seed is positive
3. Epoch confound reports max seed (0.12) not mean (0.09) for 5-epoch LP delta
4. WNUT zero-F1: 51% in paper vs 53.7% in registry
5. RE zero-F1: "40%" in intro vs 43-47% in registry
6. SciERC greedy .667 in table vs 3-seed mean .663
7. Discussion "std ratio 0.92–0.97×" — 0.92 source unverified

**Resolved**: The originally flagged Discussion/Limitations contradiction ("+0.1pp" vs "+0.4pp") no longer exists in current tex. 37 other quantitative claims verified correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "uuid": "d3af9786-1c9c-4bc3-a625-c09d1ffcd392",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jg5iXsqqHTLUMSP74qHFSD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 105372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 622
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 144_

Audit complete. Key findings:

**❌ Critical (1)**: `experiments_main.tex:89` claims "LP-best +8 pp on Few-NERD" — no data supports this. The same paper says +1.39pp (LP selection) and +1.40pp (LP construction) in three other locations. Must fix before submission.

**⚠️ Warning (7)**:
1. Selection table mixes micro/macro F1 baselines in caption vs body (11.4pp vs 13.0pp headroom)
2. Limitations "Δ_SC = −0.74±0.57 pp, consistent negative" — uses single-seed value, not 3-seed mean; one seed is positive
3. Epoch confound reports max seed (0.12) not mean (0.09) for 5-epoch LP delta
4. WNUT zero-F1: 51% in paper vs 53.7% in registry
5. RE zero-F1: "40%" in intro vs 43-47% in registry
6. SciERC greedy .667 in table vs 3-seed mean .663
7. Discussion "std ratio 0.92–0.97×" — 0.92 source unverified

**Resolved**: The originally flagged Discussion/Limitations contradiction ("+0.1pp" vs "+0.4pp") no longer exists in current tex. 37 other quantitative claims verified correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1065843,
  "duration_api_ms": 1064828,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "339d9b13-540c-480f-b97e-68216c354af6",
  "total_cost_usd": 3.68122725,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 112132,
    "cache_read_input_tokens": 696152,
    "output_tokens": 35385,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112132,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 342,
        "cache_read_input_tokens": 105372,
        "cache_creation_input_tokens": 622,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 622
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1499,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001584,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 41,
      "outputTokens": 49073,
      "cacheReadInputTokens": 1868289,
      "cacheCreationInputTokens": 242955,
      "webSearchRequests": 0,
      "costUSD": 3.67964325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f9340e67-d8d7-45bd-a3c1-205da506345f"
}
```

</details>

---
