################################################################################ 
#
# Replication code for:
# Empathy-based counterspeech can reduce racist hate speech
# in a social media field experiment
#
# PNAS 2021
# 
# Data creation file. Output is: 'data_lasso2.RDS'
# This does not need to be run in order to replicate the analysis
#
################################################################################ 


rm(list = ls())

################################################################################ 
#  LIBRARIES
################################################################################ 

library(dplyr)
library(tidyr)
library(readr)
library(fastDummies)
library(data.table)

################################################################################ 
#   DATA AND FOLDER
################################################################################ 


wd = dirname(dirname(dirname(rstudioapi::getActiveDocumentContext()$path)))
wd_res = paste0(wd, '/results')
wd_data =  paste0(wd, '/data')


################################################################################ 

setwd(wd_data)

# Upload the data
rep = read.csv('main_dataset.csv')
attach(rep)

rep$coder_dummy = ifelse(!is.na(rep$coder), tolower(rep$coder), "NA")
rep$day = lapply(rep$created_at, function(x) strsplit(x, ' ')[[1]][1]) %>% unlist()


################################################################################ 
#   VARIABLES
################################################################################

rep$pre_HS_dummy = ifelse(rep$num_hate_tweets_pre>0, 1, 0)

rep$pre_hate_share_tot = (rep$num_hate_tweets_pre) / (rep$num_tweets_pre)
rep$pre_hate_share_tot[rep$num_tweets_pre==0] = 0

data = rep[(is.na(rep$deleted_suspended)), ]

################################################################################ 
#   Select controls for quintile transformation
################################################################################ 

dum = c("display_text_width", "favorite_count", "retweet_count", 
        "followers_count", "friends_count" , "statuses_count", "favourites_count",
        "lang_share")

cont_dummies = lapply(data[dum], function(x) 
  as.factor(cut(x, quantile(x, na.rm=T), labels = F, include.lowest = T))) %>% as.data.frame()

rm(dum)

data['year_agg'] = cut(as.numeric(data$year), c(2021, 2019, 2015, 2005) , labels = F, include.lowest = T)


################################################################################ 
#   Create dummies
################################################################################ 

source_dummies = dummy_cols(data['source_main'])[,-1]
language_dummies = dummy_cols(data['lang'])[,-1]
year_dummies = dummy_cols(data['year_agg'])[,-1]
day_dummies = dummy_cols(data['day'])[,-1]  # day the tweet is created
dum_controls = c("location_yes")  
cont_dummiespr = dummy_cols(cont_dummies)[,-(1:8)]


################################################################################ 
#   Asinh transformation for some count outcomes
################################################################################ 

controls = c('pre_hate_share_tot', 'num_tweets_pre', # 'pre_hate_share_target', 
             'num_hate_tweets_pre', 'num_keywords_pre', "tox_vader_neu_pre", #'tox_bert_pre', 
             "display_text_width", "favorite_count", "retweet_count", 
             "followers_count", "friends_count" , "listed_count",
             "statuses_count", "favourites_count", "lang_share")

data[controls] = lapply(data[controls], asinh)


################################################################################ 
#   Final Dataset
################################################################################ 

# only variables we want interacted 
X = cbind.data.frame(data[controls],
                     data[dum_controls], 
                     language_dummies,
                     year_dummies, 
                     source_dummies)
X <- lapply(X, as.numeric) %>% as.data.frame()

# find first interactions
C = data['exp_id']
done = c()

for (n in names(X)){
  for (m in names(X)){
    
    name = sort(c(n, m), decreasing=T)
    name = paste0(name[1], '_', name[2])
    
    if (name %in% done){
      next
    }else{
      prod <- X[n] * X[m]
      C[name] = prod
      done = c(done, name)
    }
  }}


# Add also non interacted variables
final = cbind.data.frame(exp_id=C[, 1], X, day_dummies, C[, -1]) %>% as.data.frame()
final[names(language_dummies)][is.na(final[names(language_dummies)])] = 0
final[names(year_dummies)][is.na(final[names(year_dummies)])] = 0
final[names(source_dummies)][is.na(final[names(source_dummies)])] = 0

# Impute missing as averages
for(i in 1:ncol(final)){
  final[is.na(final[,i]), i] <- mean(final[,i], na.rm = TRUE)
}

# exclude all constant variables
final = final[, which(apply(final, 2, var) != 0)] 

setwd(wd_data)
write_rds(final, 'data_lasso2.RDS')



