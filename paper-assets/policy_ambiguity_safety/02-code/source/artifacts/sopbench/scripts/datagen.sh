cd ..

for domain in "bank" "hotel" "university" "dmv" "healthcare" "library" "online_market"; do
    python run_datagen.py \
        --domain_str $domain
done