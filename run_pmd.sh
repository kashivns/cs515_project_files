pmd_path=~/soft-good/pmd-bin-6.23.0/bin/
for file in ./final/*
do
    echo $file
    $pmd_path/run.sh cpd --minimum-tokens 60 --language java --files "$file" --format xml >> output_final.xml
done
