import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    plot_dict = {}
    plot_set = set()
    for country,val in gdp_countries.items():
        for key1,value in plot_countries.items():
            if country == value and val!='':
                plot_dict[key1] = country
        
    for key1,value in plot_countries.items():
        if value in gdp_countries:
            pass
        else:
            plot_set.add(key1)
    
    return plot_dict, plot_set

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    plot_dict ={}
    plot_dict_1 ={}
    plot_set_1 = set()
    plot_set_2 = set()
    
    new_data_dict = {}
    with open(gdpinfo['gdpfile'], 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=gdpinfo['separator']
                                        ,quotechar = gdpinfo['quote'])
        for row in data:
            new_data_dict[row[gdpinfo['country_name']]] = row

    plot_dict, plot_set_1 = reconcile_countries_by_name(plot_countries, new_data_dict)
    
    for key,value in plot_dict.items():
        for key1,val1 in new_data_dict.items():
            if value == key1:
                if val1[year]!='':
                    plot_dict_1[key] = math.log(float(val1[year]),10)
                else:
                    plot_set_2.add(key)
    return plot_dict_1, set(plot_set_1), set(plot_set_2)

def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    plot_dict_1, plot_set_1,plot_set_2 = build_map_dict_by_name(gdpinfo, plot_countries, year)
    worldmap_chart = pygal.maps.world.World()
    title_map = 'GDP by country for ' + year + ' (log scale), unifiedby common country NAME'
    worldmap_chart.title = title_map
    label_map = 'GDP for ' + year
    worldmap_chart.add(label_map,plot_dict_1 )
    worldmap_chart.add('Missing from World Bank Data',plot_set_1 )
    worldmap_chart.add('No GDP Data' ,plot_set_2 )
    worldmap_chart.render_in_browser()
    
    return


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.
#test_render_world_map()