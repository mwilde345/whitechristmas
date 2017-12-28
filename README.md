# whitechristmas
Cities that get snow on christmas eve/christmas day

api docs: https://www.wunderground.com/weather/api/d/docs
api key: https://www.wunderground.com/weather/api/d/f7eed24421d6124d/edit.html
city data: https://simplemaps.com/data/us-cities

Use this excel file for city population: https://www2.census.gov/programs-surveys/popest/datasets/2010-2016/cities/totals/sub-est2016_all.csv
We want name column: 9 and popestimate16 column: 19


Trim lowercase words from city name, fill with understore, get abbrev of the state, and query like this:
http://api.wunderground.com/api/<apikey>/conditions/q/UT/Bryce_Canyon.json

sample ➜  whitechristmas git:(master) ✗ awk -F"," '{print $9 ":" $19}' 2016US_Cities_all.csv | grep "Cedar City"

The csv file has State listed with all the cities. Then the cities are repeated under their respective counties.
