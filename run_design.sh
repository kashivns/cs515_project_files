pmd_path=~/soft/pmd-bin-6.23.0/bin/
for file in ./file-data/*
do
    echo $file
    java -jar DesigniteJava.jar -i "$file" -o "$file"/output/
#    $pmd_path/run.sh cpd --minimum-tokens 60 --language java --files "$file" --format xml >> output.xml
done
