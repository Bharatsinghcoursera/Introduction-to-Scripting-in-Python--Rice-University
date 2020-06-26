#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    
    new_data_dict = {}
    with open(filename, 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=separator,quotechar = quote)
        for row in data:
            keyid = row[keyfield]
            new_data_dict[keyid] = row
                
    return new_data_dict


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    
    list_of_tuples = []
    for key, value in gdpdata.items():
        try:
            if (value != ""):
                if (int(key) <= gdpinfo["max_year"]) and (int(key)  >= gdpinfo["min_year"]):
                    list_of_tuples.append((int(key), float(value)))
        except ValueError:
            pass
                
    list_of_tuples.sort(key = lambda pair: pair[0])
    return list_of_tuples


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    
    plot = {}
    plot_data = read_csv_as_nested_dict(gdpinfo["gdpfile"], 
                                       gdpinfo["country_name"], 
                                       gdpinfo["separator"], gdpinfo["quote"])
    for country in country_list:
        plot[country] = []
        for key, value in plot_data.items():
            if key == country:
                tuple_list = build_plot_values(gdpinfo, value)
                plot[country] = tuple_list
    
    return plot


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    
    plot = build_plot_dict(gdpinfo, country_list)
    line_chart = pygal.XY(xrange=(1960, 2016))
    line_chart.title = 'Plot of GDP for select countries spanning 1960 to 2015'
    line_chart.x_title = 'Year'
    line_chart.y_title = 'GDP in current US Dollars'
    
    for country in country_list:
        for key,item in plot.items():
            try:
                if (key != ""):
                    if key == country:
                        line_chart.add(key, item)
            except ValueError:
                pass

    #Function forviewing graphs in browser
    #line_chart.render_in_browser()        
    line_chart.render_to_file(plot_file)
 
    
    
def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
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

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],"isp_gdp_xy_uk+usa.svg")

# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.
#test_render_xy_plot()