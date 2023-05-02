# Coronavirus twitter analysis

This project involved analyzing Twitter data related to the coronavirus pandemic. The goal was to track the usage of hashtags on both a language and country level, and visualize the results.

In Task 0, we used the map.py file to track the usage of hashtags on both a language and country level. The output of running map.py resulted in two files, one that ends in .lang for the language dictionary and one that ends in .country for the country dictionary.

In Task 1, we created a shell script called run_maps.sh that looped over each file in the dataset and ran the map.py command on that file. Each call to map.py ran in parallel using the nohup command and the & operator.

In Task 2, we used the reduce.py file to combine all of the .lang files into a single file and all of the .country files into a different file.

In Task 3, we modified the visualize.py file to generate a bar graph of the results and stored the bar graph as a png file. The final results were sorted from low to high, and we included only the top 10 keys. We ran the visualize.py file with the --input_path equal to both the country and lang files created in the reduce phase, and the --key set to #coronavirus and #코로나바이러스, resulting in four plots in total.The four plots are listed below:
1. number of tweets that mention  #코로나바이러스 , sorted by language 
<img src=coronavirus2_lang.png width=100% />
2. number of tweets that mention  #코로나바이러스, sorted by country
<img src=coronavirus2_country.png width=100% />
3. number of tweet that mention #coronavirus, sorted by language
<img src=coronavirus_lang.png width=100% /> 
4. number of tweet that mention #coronavirus, sorted by country
<img src=coronavirus_country.png width=100% />

In Task 4, we created a new file alternative_reduce.py that took as input on the command line a list of hashtags and output a line plot where there was one line per input hashtag, the x-axis was the day of the year, and the y-axis was the number of tweets that used that hashtag during the year.

The generated png files can be found in the outputs folder of the github repo. Overall, this project involved working with large amounts of Twitter data, processing it, and visualizing the results using Python and various libraries.
