#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library(lme4)
  library(jsonlite)
})

args <- commandArgs(trailingOnly = TRUE)
input_path  <- ifelse(length(args) >= 1, args[1],
                      "results/analysis/cross_model_llama_gemma.csv")
output_path <- ifelse(length(args) >= 2, args[2],
                      "results/analysis/cross_model_reml.json")
sample_frac <- ifelse(length(args) >= 3, as.numeric(args[3]), 1.0)

cat("Reading data from", input_path, "\n")

if (grepl("\\.jsonl$", input_path)) {
  lines <- readLines(input_path)
  df <- do.call(rbind, lapply(lines, function(l) {
    as.data.frame(fromJSON(l, simplifyVector = TRUE), stringsAsFactors = FALSE)
  }))
} else {
  df <- read.csv(input_path, stringsAsFactors = FALSE)
}

cat("Loaded", nrow(df), "rows\n")

if (!"binary_correct" %in% names(df)) {
  if ("correct" %in% names(df)) {
    df$binary_correct <- df$correct
  } else {
    stop("No 'binary_correct' or 'correct' column found")
  }
}

if (sample_frac < 1.0) {
  set.seed(42)
  n_sample <- round(nrow(df) * sample_frac)
  df <- df[sample(nrow(df), n_sample), ]
  cat("Sampled down to", nrow(df), "rows\n")
}

facets <- c("model", "precision", "temperature",
            "prompt_template", "seed", "ordering", "item_id")

for (f in facets) {
  df[[f]] <- as.factor(df[[f]])
}

cat("Factor levels:\n")
for (f in facets) {
  cat(sprintf("  %s: %d levels\n", f, nlevels(df[[f]])))
}

cat("\nFitting REML model...\n")
t0 <- proc.time()

formula_str <- paste0(
  "binary_correct ~ 1 + ",
  paste0("(1|", facets, ")", collapse = " + "),
  " + ",
  paste0(
    "(1|", apply(combn(facets, 2), 2, function(x) paste(x, collapse=":")), ")",
    collapse = " + "
  )
)

cat("Formula:", formula_str, "\n\n")

m <- lmer(
  as.formula(formula_str),
  data = df,
  REML = TRUE,
  control = lmerControl(
    optimizer = "bobyqa",
    optCtrl = list(maxfun = 50000),
    check.nobs.vs.nRE = "warning",
    check.nobs.vs.nlev = "warning"
  )
)

elapsed <- (proc.time() - t0)[["elapsed"]]
cat(sprintf("Model fit completed in %.1f seconds\n", elapsed))

vc <- as.data.frame(VarCorr(m))
cat("\nVariance components:\n")
print(vc[, c("grp", "vcov")])

vc_named <- setNames(vc$vcov, vc$grp)
total_var <- sum(vc_named)

result <- list()
result$variance_components <- list()
for (i in seq_len(nrow(vc))) {
  name <- vc$grp[i]
  est  <- vc$vcov[i]
  result$variance_components[[name]] <- list(
    estimate = est,
    pct = est / total_var * 100
  )
}

result$total_variance <- total_var
result$n_observations <- nrow(df)
result$method <- "REML (lme4::lmer)"
result$elapsed_seconds <- elapsed
result$convergence <- m@optinfo$conv$opt == 0
result$n_levels <- setNames(
  sapply(facets, function(f) nlevels(df[[f]])),
  facets
)
result$formula <- formula_str

result$fixed_intercept <- fixef(m)[["(Intercept)"]]
result$aic <- AIC(m)
result$bic <- BIC(m)
result$loglik <- as.numeric(logLik(m))
result$deviance <- deviance(m)

json_out <- toJSON(result, pretty = TRUE, auto_unbox = TRUE, digits = 10)
writeLines(json_out, output_path)
cat(sprintf("\nResults saved to %s\n", output_path))

cat("\n=== Variance Component Summary ===\n")
cat(sprintf("%-30s %12s %8s\n", "Component", "Estimate", "%"))
cat(paste(rep("-", 52), collapse=""), "\n")
for (name in names(result$variance_components)) {
  info <- result$variance_components[[name]]
  cat(sprintf("%-30s %12.6f %7.1f%%\n", name, info$estimate, info$pct))
}
cat(sprintf("\nTotal variance: %.6f\n", total_var))
cat(sprintf("Fixed intercept (grand mean): %.4f\n", result$fixed_intercept))
