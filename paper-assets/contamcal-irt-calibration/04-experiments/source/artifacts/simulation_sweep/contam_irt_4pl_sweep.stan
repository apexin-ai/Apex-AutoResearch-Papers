// 4PL+γ IRT model for simulation sweep
// Accepts gamma_prior_sd as data for prior sensitivity analysis
// No generated quantities (saves time in sweep)

data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
  matrix[N_models, N_items] exposure;
  real<lower=0> gamma_prior_sd;
}

parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
  vector<lower=0, upper=1>[N_items] c;
  vector<lower=0, upper=1>[N_items] d;
  real gamma;
}

model {
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  c ~ beta(5, 20);
  d ~ beta(20, 5);
  gamma ~ normal(0, gamma_prior_sd);

  for (i in 1:N_models) {
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      y[i, j] ~ bernoulli(p);
    }
  }
}
