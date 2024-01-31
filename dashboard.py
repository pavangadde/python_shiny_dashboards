import shinyswatch
import pandas as pd
import numpy as np
from shiny import *
from siuba import *
from shinywidgets import *
import plotly.express as px
import plotly.graph_objs as go

df=pd.read_excel(r'D:\shiny\UK_accident_data_filtered.xlsx')

df['accident_year']=df['accident_year'].apply(lambda x:str(x))

val="All"

filt_accident_year=list(set(df['accident_year']))
filt_accident_severity=list(set(df['accident_severity']))
filt_police_force=list(set(df['police_force']))
filt_local_authority_district=list(set(df['local_authority_district']))
filt_local_authority_ons_district=list(set(df['local_authority_ons_district']))
filt_first_road_class=list(set(df['first_road_class']))
filt_road_type=list(set(df['road_type']))
filt_junction_detail=list(set(df['junction_detail']))
filt_junction_control=list(set(df['junction_control']))
filt_light_conditions=list(set(df['light_conditions']))
filt_weather_conditions=list(set(df['weather_conditions']))
filt_road_surface_conditions=list(set(df['road_surface_conditions']))
filt_special_conditions_at_site=list(set(df['special_conditions_at_site']))
filt_carriageway_hazards=list(set(df['carriageway_hazards']))
filt_urban_or_rural_area=list(set(df['urban_or_rural_area']))
filt_did_police_officer_attend_scene_of_accident=list(set(df['did_police_officer_attend_scene_of_accident']))
filt_pedestrian_crossing_human_control=list(set(df['pedestrian_crossing_human_control']))
filt_trunk_road_flag=list(set(df['trunk_road_flag']))
filt_pedestrian_crossing_physical_facilities=list(set(df['pedestrian_crossing_physical_facilities']))
filt_second_road_class=list(set(df['second_road_class']))

filt_accident_year.insert(0,val)
filt_accident_severity.insert(0,val)
filt_police_force.insert(0,val)
filt_local_authority_district.insert(0,val)
filt_local_authority_ons_district.insert(0,val)
filt_first_road_class.insert(0,val)
filt_road_type.insert(0,val)
filt_junction_detail.insert(0,val)
filt_junction_control.insert(0,val)
filt_light_conditions.insert(0,val)
filt_weather_conditions.insert(0,val)
filt_road_surface_conditions.insert(0,val)
filt_special_conditions_at_site.insert(0,val)
filt_carriageway_hazards.insert(0,val)
filt_urban_or_rural_area.insert(0,val)
filt_did_police_officer_attend_scene_of_accident.insert(0,val)
filt_pedestrian_crossing_human_control.insert(0,val)
filt_trunk_road_flag.insert(0,val)
filt_pedestrian_crossing_physical_facilities.insert(0,val)
filt_second_road_class.insert(0,val)
    
app_ui = ui.page_sidebar(
                            ui.sidebar(

                                                    ui.input_selectize('accident_year','Accident Year:',filt_accident_year,multiple=True,selected='All'),
                                                    ui.input_selectize('accident_severity','Accident Severity:',filt_accident_severity,multiple=True,selected='All'),
                                                    ui.input_selectize('police_force','Police Force:',filt_police_force,multiple=True,selected='All'),
                                                    ui.input_selectize('local_authority_district','Local_Authority District:',filt_local_authority_district,multiple=True,selected='All'),
                                                    ui.input_selectize('local_authority_ons_district','Local_Authority_Ons District:',filt_local_authority_ons_district,multiple=True,selected='All'),
                                                    ui.input_selectize('first_road_class','First_Road Class:',filt_first_road_class,multiple=True,selected='All'),
                                                    ui.input_selectize('road_type','Road Type:',filt_road_type,multiple=True,selected='All'),
                                                    ui.input_selectize('junction_detail','Junction Detail:',filt_junction_detail,multiple=True,selected='All'),
                                                    ui.input_selectize('junction_control','Junction Control:',filt_junction_control,multiple=True,selected='All'),
                                                    ui.input_selectize('light_conditions','Light Conditions:',filt_light_conditions,multiple=True,selected='All'),
                                                    ui.input_selectize('weather_conditions','Weather Conditions:',filt_weather_conditions,multiple=True,selected='All'),
                                                    ui.input_selectize('road_surface_conditions','Road_Surface Conditions:',filt_road_surface_conditions,multiple=True,selected='All'),
                                                    ui.input_selectize('special_conditions_at_site','Special_Conditions_At Site:',filt_special_conditions_at_site,multiple=True,selected='All'),
                                                    ui.input_selectize('carriageway_hazards','Carriageway Hazards:',filt_carriageway_hazards,multiple=True,selected='All'),
                                                    ui.input_selectize('urban_or_rural_area','Urban_Or_Rural Area:',filt_urban_or_rural_area,multiple=True,selected='All'),
                                                    ui.input_selectize('did_police_officer_attend_scene_of_accident','Did_Police_Officer_Attend_Scene_Of Accident:',filt_did_police_officer_attend_scene_of_accident,multiple=True,selected='All'),
                                                    ui.input_selectize('pedestrian_crossing_human_control','Pedestrian_Crossing_Human Control:',filt_pedestrian_crossing_human_control,multiple=True,selected='All'),
                                                    ui.input_selectize('trunk_road_flag','Trunk_Road Flag:',filt_trunk_road_flag,multiple=True,selected='All'),
                                                    ui.input_selectize('pedestrian_crossing_physical_facilities','Pedestrian_Crossing_Physical Facilities:',filt_pedestrian_crossing_physical_facilities,multiple=True,selected='All'),
                                                    ui.input_selectize('second_road_class','Second_Road Class:',filt_second_road_class,multiple=True,selected='All'),
                                                    width=250,



                                        ),

                                ui.navset_bar(

                                        shinyswatch.theme.lumen(),

                                        ui.nav("Summary Data", ui.output_data_frame("summary_data")),title=""

                                            ),

                                            title="UK Motor Accidents Dashboard"





                        )

def server(input,output, session):


    user_provided_values_1=reactive.Value([])
    user_provided_values_2=reactive.Value([])
    user_provided_values_3=reactive.Value([])
    user_provided_values_4=reactive.Value([])
    user_provided_values_5=reactive.Value([])
    user_provided_values_6=reactive.Value([])
    user_provided_values_7=reactive.Value([])
    user_provided_values_8=reactive.Value([])
    user_provided_values_9=reactive.Value([])
    user_provided_values_10=reactive.Value([])
    user_provided_values_11=reactive.Value([])
    user_provided_values_12=reactive.Value([])
    user_provided_values_13=reactive.Value([])
    user_provided_values_14=reactive.Value([])
    user_provided_values_15=reactive.Value([])
    user_provided_values_16=reactive.Value([])
    user_provided_values_17=reactive.Value([])
    user_provided_values_18=reactive.Value([])
    user_provided_values_19=reactive.Value([])
    user_provided_values_20=reactive.Value([])


    @reactive.Effect
    @reactive.event(input.accident_year,input.accident_severity,input.police_force,input.local_authority_district,input.local_authority_ons_district,input.first_road_class,input.road_type,
                    input.junction_detail,
                    input.junction_control,
                    input.light_conditions,
                    input.weather_conditions,
                    input.road_surface_conditions,
                    input.special_conditions_at_site,
                    input.carriageway_hazards,
                    input.urban_or_rural_area,
                    input.did_police_officer_attend_scene_of_accident,
                    input.pedestrian_crossing_human_control,
                    input.trunk_road_flag,
                    input.pedestrian_crossing_physical_facilities,
                    input.second_road_class
                    )
    def add_value_to_list():

        if 'All' in input.accident_year() or len(input.accident_year())==0:
            user_provided_values_1.set(df['accident_year'].unique().tolist())
        else:
            user_provided_values_1.set(ele for ele in input.accident_year())

        if 'All' in input.accident_severity() or len(input.accident_severity())==0:
            user_provided_values_2.set(df['accident_severity'].unique().tolist())
        else:
            user_provided_values_2.set(ele for ele in input.accident_severity())

        if 'All' in input.police_force() or len(input.police_force())==0:
            user_provided_values_3.set(df['police_force'].unique().tolist())
        else:
            user_provided_values_3.set(ele for ele in input.police_force())

        if 'All' in input.local_authority_district() or len(input.local_authority_district())==0:
            user_provided_values_4.set(df['local_authority_district'].unique().tolist())
        else:
            user_provided_values_4.set(ele for ele in input.local_authority_district())

        if 'All' in input.local_authority_ons_district() or len(input.local_authority_ons_district())==0:
            user_provided_values_5.set(df['local_authority_ons_district'].unique().tolist())
        else:
            user_provided_values_5.set(ele for ele in input.local_authority_ons_district())

        if 'All' in input.first_road_class() or len(input.first_road_class())==0:
            user_provided_values_6.set(df['first_road_class'].unique().tolist())
        else:
            user_provided_values_6.set(ele for ele in input.first_road_class())

        if 'All' in input.road_type() or len(input.road_type())==0:
            user_provided_values_7.set(df['road_type'].unique().tolist())
        else:
            user_provided_values_7.set(ele for ele in input.road_type())

        if 'All' in input.junction_detail() or len(input.junction_detail())==0:
            user_provided_values_8.set(df['junction_detail'].unique().tolist())
        else:
            user_provided_values_8.set(ele for ele in input.junction_detail())


        if 'All' in input.junction_control() or len(input.junction_control())==0:
            user_provided_values_9.set(df['junction_control'].unique().tolist())
        else:
            user_provided_values_9.set(ele for ele in input.junction_control())

        if 'All' in input.light_conditions() or len(input.light_conditions())==0:
            user_provided_values_10.set(df['light_conditions'].unique().tolist())
        else:
            user_provided_values_10.set(ele for ele in input.light_conditions())

        if 'All' in input.weather_conditions() or len(input.weather_conditions())==0:
            user_provided_values_11.set(df['weather_conditions'].unique().tolist())
        else:
            user_provided_values_11.set(ele for ele in input.weather_conditions())

        if 'All' in input.road_surface_conditions() or len(input.road_surface_conditions())==0:
            user_provided_values_12.set(df['road_surface_conditions'].unique().tolist())
        else:
            user_provided_values_12.set(ele for ele in input.road_surface_conditions())

        if 'All' in input.special_conditions_at_site() or len(input.special_conditions_at_site())==0:
            user_provided_values_13.set(df['special_conditions_at_site'].unique().tolist())
        else:
            user_provided_values_13.set(ele for ele in input.special_conditions_at_site())

        if 'All' in input.carriageway_hazards() or len(input.carriageway_hazards())==0:
            user_provided_values_14.set(df['carriageway_hazards'].unique().tolist())
        else:
            user_provided_values_14.set(ele for ele in input.carriageway_hazards())

        if 'All' in input.urban_or_rural_area() or len(input.urban_or_rural_area())==0:
            user_provided_values_15.set(df['urban_or_rural_area'].unique().tolist())
        else:
            user_provided_values_15.set(ele for ele in input.urban_or_rural_area())

        if 'All' in input.did_police_officer_attend_scene_of_accident() or len(input.did_police_officer_attend_scene_of_accident())==0:
            user_provided_values_16.set(df['did_police_officer_attend_scene_of_accident'].unique().tolist())
        else:
            user_provided_values_16.set(ele for ele in input.did_police_officer_attend_scene_of_accident())

        if 'All' in input.pedestrian_crossing_human_control() or len(input.pedestrian_crossing_human_control())==0:
            user_provided_values_17.set(df['pedestrian_crossing_human_control'].unique().tolist())
        else:
            user_provided_values_17.set(ele for ele in input.pedestrian_crossing_human_control())

        if 'All' in input.trunk_road_flag() or len(input.trunk_road_flag())==0:
            user_provided_values_18.set(df['trunk_road_flag'].unique().tolist())
        else:
            user_provided_values_18.set(ele for ele in input.trunk_road_flag())

        if 'All' in input.pedestrian_crossing_physical_facilities() or len(input.pedestrian_crossing_physical_facilities())==0:
            user_provided_values_19.set(df['pedestrian_crossing_physical_facilities'].unique().tolist())
        else:
            user_provided_values_19.set(ele for ele in input.pedestrian_crossing_physical_facilities())

        if 'All' in input.second_road_class() or len(input.second_road_class())==0:
            user_provided_values_20.set(df['second_road_class'].unique().tolist())
        else:
            user_provided_values_20.set(ele for ele in input.second_road_class())

    
    @reactive.Calc
    def filtered_data():

        df_filtered=(df>> filter(_['accident_year'].isin(user_provided_values_1()))
                    >> filter(_['accident_severity'].isin(user_provided_values_2()))
                    >> filter(_['police_force'].isin(user_provided_values_3()))
                    >> filter(_['local_authority_district'].isin(user_provided_values_4()))
                    >> filter(_['local_authority_ons_district'].isin(user_provided_values_5()))
                    >> filter(_['first_road_class'].isin(user_provided_values_6()))
                    >> filter(_['road_type'].isin(user_provided_values_7()))
                    >> filter(_['junction_detail'].isin(user_provided_values_8()))
                    >> filter(_['junction_control'].isin(user_provided_values_9()))
                    >> filter(_['light_conditions'].isin(user_provided_values_10()))
                    >> filter(_['weather_conditions'].isin(user_provided_values_11()))
                    >> filter(_['road_surface_conditions'].isin(user_provided_values_12()))
                    >> filter(_['special_conditions_at_site'].isin(user_provided_values_13()))
                    >> filter(_['carriageway_hazards'].isin(user_provided_values_14()))
                    >> filter(_['urban_or_rural_area'].isin(user_provided_values_15()))
                    >> filter(_['did_police_officer_attend_scene_of_accident'].isin(user_provided_values_16()))
                    >> filter(_['pedestrian_crossing_human_control'].isin(user_provided_values_17()))
                    >> filter(_['trunk_road_flag'].isin(user_provided_values_18()))
                    >> filter(_['pedestrian_crossing_physical_facilities'].isin(user_provided_values_19()))
                    >> filter(_['second_road_class'].isin(user_provided_values_20()))          
                     )

        return df_filtered

    @render.data_frame
    def summary_data():

        return render.DataGrid(filtered_data())
    

 
app=App(app_ui,server)    





